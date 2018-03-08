# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""'functions deploy' utilities for triggers."""
from googlecloudsdk.api_lib.functions import exceptions
from googlecloudsdk.api_lib.functions import triggers
from googlecloudsdk.api_lib.functions import util as api_util
from googlecloudsdk.api_lib.storage import storage_util
from googlecloudsdk.calliope import exceptions as calliope_exceptions
from googlecloudsdk.core import exceptions as core_exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


TRIGGER_BUCKET_NOTICE = (
    'The default trigger_event for `--trigger-bucket` will soon '
    'change to `object.finalize` from `object.change`. '
    'To opt-in to the new behavior early, run'
    '`gcloud config set functions/use_new_object_trigger True`. To restore old '
    'behavior you can run '
    '`gcloud config set functions/use_new_object_trigger False` '
    'or use the `--trigger-event` flag e.g. '
    '`gcloud functions deploy --trigger-event '
    'providers/cloud.storage/eventTypes/object.change '
    '--trigger-resource gs://...`'
    'Please see https://cloud.google.com/storage/docs/pubsub-notifications'
    'for more information on storage event types.')

TRIGGER_TOPIC_NOTICE = (
    'The default event schema returned by Cloud Functions with a pub/sub '
    '(`--trigger-topic`) trigger will soon change. The `eventId`, `timestamp`, '
    '`eventType`, and `resource` properties will all be moved into the '
    '`event.context` property. To opt-in to the new behavior early, run'
    '`gcloud config set functions/use_new_pubsub_trigger True`. To restore old '
    'behavior you can run '
    '`gcloud config set functions/use_new_pubsub_trigger False` '
    'or use the `--trigger-event` flag e.g. '
    '`gcloud functions deploy --trigger-event '
    'providers/cloud.pubsub/eventTypes/topic.publish '
    '--trigger-resource <TOPIC_NAME>` Please see '
    'https://cloud.google.com/functions/docs/writing/background#event_parameter'
    'for more information on the new schema.')


def CheckTriggerSpecified(args):
  if not (args.IsSpecified('trigger_topic')
          or args.IsSpecified('trigger_bucket')
          or args.IsSpecified('trigger_http')
          or args.IsSpecified('trigger_event')):
    # --trigger-provider is hidden for now so not mentioning it.
    raise calliope_exceptions.OneOfArgumentsRequiredException(
        ['--trigger-topic', '--trigger-bucket', '--trigger-http',
         '--trigger-event'],
        'You must specify a trigger when deploying a new function.'
    )


def ValidateTriggerArgs(trigger_event, trigger_resource, retry_specified,
                        trigger_http_specified):
  """Check if args related function triggers are valid.

  Args:
    trigger_event: The trigger event
    trigger_resource: The trigger resource
    retry_specified: Whether or not `--retry` was specified
    trigger_http_specified: Whether or not `--trigger-http` was specified
  Raises:
    FunctionsError.
  """
  # Check that Event Type is valid
  if trigger_event:
    trigger_provider = (
        triggers.INPUT_TRIGGER_PROVIDER_REGISTRY.ProviderForEvent(
            trigger_event).label)
    if not trigger_provider:
      raise exceptions.FunctionsError(
          'Unsupported trigger_event {}'.format(trigger_event))

    resource_type = triggers.INPUT_TRIGGER_PROVIDER_REGISTRY.Event(
        trigger_provider, trigger_event).resource_type
    if trigger_resource is None and resource_type != triggers.Resources.PROJECT:
      raise exceptions.FunctionsError(
          'You must provide --trigger-resource when using '
          '--trigger-event={}'.format(trigger_event))
  if retry_specified and trigger_http_specified:
    raise calliope_exceptions.ConflictingArgumentsException(
        '--trigger-http', '--retry')


def _GetBucketTriggerEventParams(trigger_bucket):
  bucket_name = trigger_bucket[5:-1]
  new_behavior = properties.VALUES.functions.use_new_object_trigger.GetBool()
  if new_behavior is None:
    log.warn(TRIGGER_BUCKET_NOTICE)

  return {
      'trigger_provider': 'cloud.storage',
      'trigger_event':
          ('google.storage.object.finalize' if new_behavior
           else 'providers/cloud.storage/eventTypes/object.change'),
      'trigger_resource': bucket_name,
  }


def _GetTopicTriggerEventParams(trigger_topic):
  new_behavior = properties.VALUES.functions.use_new_pubsub_trigger.GetBool()
  if new_behavior is None:
    log.warn(TRIGGER_TOPIC_NOTICE)

  return {
      'trigger_provider': 'cloud.pubsub',
      'trigger_event': ('google.pubsub.topic.publish' if new_behavior
                        else 'providers/cloud.pubsub/eventTypes/topic.publish'),
      'trigger_resource': trigger_topic,
  }


def _GetEventTriggerEventParams(trigger_event, trigger_resource):
  """Get the args for creating an event trigger.

  Args:
    trigger_event: The trigger event
    trigger_resource: The trigger resource
  Returns:
    A dictionary containing trigger_provider, trigger_event, and
    trigger_resource.
  """
  trigger_provider = triggers.INPUT_TRIGGER_PROVIDER_REGISTRY.ProviderForEvent(
      trigger_event).label
  resource_type = triggers.INPUT_TRIGGER_PROVIDER_REGISTRY.Event(
      trigger_provider, trigger_event).resource_type
  if resource_type == triggers.Resources.TOPIC:
    trigger_resource = api_util.ValidatePubsubTopicNameOrRaise(
        trigger_resource)
  elif resource_type == triggers.Resources.BUCKET:
    trigger_resource = storage_util.BucketReference.FromBucketUrl(
        trigger_resource).bucket
  elif resource_type == triggers.Resources.PROJECT:
    if trigger_resource:
      properties.VALUES.core.project.Validate(trigger_resource)
  else:
    # Check if programmer allowed other methods in
    # api_util.PROVIDER_EVENT_RESOURCE but forgot to update code here
    raise core_exceptions.InternalError()
  # checked if provided resource and path have correct format
  return {
      'trigger_provider': trigger_provider,
      'trigger_event': trigger_event,
      'trigger_resource': trigger_resource,
  }


def GetTriggerEventParams(trigger_http, trigger_bucket, trigger_topic,
                          trigger_event, trigger_resource):
  """Check --trigger-*  arguments and deduce if possible.

  0. if --trigger-http is return None.
  1. if --trigger-bucket return bucket trigger args (_GetBucketTriggerArgs)
  2. if --trigger-topic return pub-sub trigger args (_GetTopicTriggerArgs)
  3. if --trigger-event, deduce provider and resource from registry and return

  Args:
    trigger_http: The trigger http
    trigger_bucket: The trigger bucket
    trigger_topic: The trigger topic
    trigger_event: The trigger event
    trigger_resource: The trigger resource

  Returns:
    None, when using HTTPS trigger. Otherwise a dictionary containing
    trigger_provider, trigger_event, and trigger_resource.
  """
  if trigger_http:
    return None
  if trigger_bucket:
    return _GetBucketTriggerEventParams(trigger_bucket)
  if trigger_topic:
    return _GetTopicTriggerEventParams(trigger_topic)
  if trigger_event:
    return _GetEventTriggerEventParams(trigger_event, trigger_resource)


def ConvertTriggerArgsToRelativeName(trigger_provider, trigger_event,
                                     trigger_resource):
  """Prepares resource field for Function EventTrigger to use in API call.

  API uses relative resource name in EventTrigger message field. The
  structure of that identifier depends on the resource type which depends on
  combination of --trigger-provider and --trigger-event arguments' values.
  This function chooses the appropriate form, fills it with required data and
  returns as a string.

  Args:
    trigger_provider: The --trigger-provider flag value.
    trigger_event: The --trigger-event flag value.
    trigger_resource: The --trigger-resource flag value.
  Returns:
    Relative resource name to use in EventTrigger field.
  """
  resource_type = triggers.INPUT_TRIGGER_PROVIDER_REGISTRY.Event(
      trigger_provider, trigger_event).resource_type
  params = {}
  if resource_type.value.collection_id == 'cloudresourcemanager.projects':
    params['projectId'] = properties.VALUES.core.project.GetOrFail
  elif resource_type.value.collection_id == 'pubsub.projects.topics':
    params['projectsId'] = properties.VALUES.core.project.GetOrFail
  elif resource_type.value.collection_id == 'cloudfunctions.projects.buckets':
    pass

  ref = resources.REGISTRY.Parse(
      trigger_resource,
      params,
      collection=resource_type.value.collection_id,
  )
  return ref.RelativeName()


def CreateEventTrigger(trigger_provider, trigger_event, trigger_resource):
  messages = api_util.GetApiMessagesModule()
  event_trigger = messages.EventTrigger()
  event_trigger.eventType = trigger_event
  event_trigger.resource = (
      ConvertTriggerArgsToRelativeName(
          trigger_provider,
          trigger_event,
          trigger_resource))
  return event_trigger
