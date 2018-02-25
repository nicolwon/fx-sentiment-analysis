"""Generated message classes for cloudkms version v1.

Manages encryption for your cloud services the same way you do on-premises.
You can generate, use, rotate, and destroy AES256 encryption keys.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudkms'


class AuditConfig(_messages.Message):
  """Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs.  If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted.  Example Policy with
  multiple AuditConfigs:      {       "audit_configs": [         {
  "service": "allServices"           "audit_log_configs": [             {
  "log_type": "DATA_READ",               "exempted_members": [
  "user:foo@gmail.com"               ]             },             {
  "log_type": "DATA_WRITE",             },             {
  "log_type": "ADMIN_READ",             }           ]         },         {
  "service": "fooservice.googleapis.com"           "audit_log_configs": [
  {               "log_type": "DATA_READ",             },             {
  "log_type": "DATA_WRITE",               "exempted_members": [
  "user:bar@gmail.com"               ]             }           ]         }
  ]     }  For fooservice, this policy enables DATA_READ, DATA_WRITE and
  ADMIN_READ logging. It also exempts foo@gmail.com from DATA_READ logging,
  and bar@gmail.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
      Next ID: 4
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  """Provides the configuration for logging a type of permissions. Example:
  {       "audit_log_configs": [         {           "log_type": "DATA_READ",
  "exempted_members": [             "user:foo@gmail.com"           ]
  },         {           "log_type": "DATA_WRITE",         }       ]     }
  This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting
  foo@gmail.com from DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    """The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class Binding(_messages.Message):
  """Associates `members` with a `role`.

  Fields:
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example, `alice@gmail.com`
      or `joe@example.com`.   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.
      * `domain:{domain}`: A Google Apps domain name that represents all the
      users of that domain. For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`. Required
  """

  members = _messages.StringField(1, repeated=True)
  role = _messages.StringField(2)


class CloudkmsProjectsLocationsGetRequest(_messages.Message):
  """A CloudkmsProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class CloudkmsProjectsLocationsKeyRingsCreateRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCreateRequest object.

  Fields:
    keyRing: A KeyRing resource to be passed as the request body.
    keyRingId: Required. It must be unique within a location and match the
      regular expression `[a-zA-Z0-9_-]{1,63}`
    parent: Required. The resource name of the location associated with the
      KeyRings, in the format `projects/*/locations/*`.
  """

  keyRing = _messages.MessageField('KeyRing', 1)
  keyRingId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysCreateRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysCreateRequest object.

  Fields:
    cryptoKey: A CryptoKey resource to be passed as the request body.
    cryptoKeyId: Required. It must be unique within a KeyRing and match the
      regular expression `[a-zA-Z0-9_-]{1,63}`
    parent: Required. The name of the KeyRing associated with the CryptoKeys.
  """

  cryptoKey = _messages.MessageField('CryptoKey', 1)
  cryptoKeyId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsCreateRequest(_messages.Message):
  """A
  CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsCreateRequest
  object.

  Fields:
    cryptoKeyVersion: A CryptoKeyVersion resource to be passed as the request
      body.
    parent: Required. The name of the CryptoKey associated with the
      CryptoKeyVersions.
  """

  cryptoKeyVersion = _messages.MessageField('CryptoKeyVersion', 1)
  parent = _messages.StringField(2, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsDestroyRequest(_messages.Message):
  """A
  CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsDestroyRequest
  object.

  Fields:
    destroyCryptoKeyVersionRequest: A DestroyCryptoKeyVersionRequest resource
      to be passed as the request body.
    name: The resource name of the CryptoKeyVersion to destroy.
  """

  destroyCryptoKeyVersionRequest = _messages.MessageField('DestroyCryptoKeyVersionRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGetRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGetRequest
  object.

  Fields:
    name: The name of the CryptoKeyVersion to get.
  """

  name = _messages.StringField(1, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsListRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsListRequest
  object.

  Fields:
    pageSize: Optional limit on the number of CryptoKeyVersions to include in
      the response. Further CryptoKeyVersions can subsequently be obtained by
      including the ListCryptoKeyVersionsResponse.next_page_token in a
      subsequent request. If unspecified, the server will pick an appropriate
      default.
    pageToken: Optional pagination token, returned earlier via
      ListCryptoKeyVersionsResponse.next_page_token.
    parent: Required. The resource name of the CryptoKey to list, in the
      format `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsPatchRequest(_messages.Message):
  """A
  CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsPatchRequest
  object.

  Fields:
    cryptoKeyVersion: A CryptoKeyVersion resource to be passed as the request
      body.
    name: Output only. The resource name for this CryptoKeyVersion in the
      format
      `projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*`.
    updateMask: Required list of fields to be updated in this request.
  """

  cryptoKeyVersion = _messages.MessageField('CryptoKeyVersion', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsRestoreRequest(_messages.Message):
  """A
  CloudkmsProjectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsRestoreRequest
  object.

  Fields:
    name: The resource name of the CryptoKeyVersion to restore.
    restoreCryptoKeyVersionRequest: A RestoreCryptoKeyVersionRequest resource
      to be passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  restoreCryptoKeyVersionRequest = _messages.MessageField('RestoreCryptoKeyVersionRequest', 2)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysDecryptRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysDecryptRequest object.

  Fields:
    decryptRequest: A DecryptRequest resource to be passed as the request
      body.
    name: Required. The resource name of the CryptoKey to use for decryption.
      The server will choose the appropriate version.
  """

  decryptRequest = _messages.MessageField('DecryptRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysEncryptRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysEncryptRequest object.

  Fields:
    encryptRequest: A EncryptRequest resource to be passed as the request
      body.
    name: Required. The resource name of the CryptoKey or CryptoKeyVersion to
      use for encryption.  If a CryptoKey is specified, the server will use
      its primary version.
  """

  encryptRequest = _messages.MessageField('EncryptRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysGetIamPolicyRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysGetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  resource = _messages.StringField(1, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysGetRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysGetRequest object.

  Fields:
    name: The name of the CryptoKey to get.
  """

  name = _messages.StringField(1, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysListRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysListRequest object.

  Fields:
    pageSize: Optional limit on the number of CryptoKeys to include in the
      response.  Further CryptoKeys can subsequently be obtained by including
      the ListCryptoKeysResponse.next_page_token in a subsequent request.  If
      unspecified, the server will pick an appropriate default.
    pageToken: Optional pagination token, returned earlier via
      ListCryptoKeysResponse.next_page_token.
    parent: Required. The resource name of the KeyRing to list, in the format
      `projects/*/locations/*/keyRings/*`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysPatchRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysPatchRequest object.

  Fields:
    cryptoKey: A CryptoKey resource to be passed as the request body.
    name: Output only. The resource name for this CryptoKey in the format
      `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
    updateMask: Required list of fields to be updated in this request.
  """

  cryptoKey = _messages.MessageField('CryptoKey', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysSetIamPolicyRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysTestIamPermissionsRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysTestIamPermissionsRequest
  object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class CloudkmsProjectsLocationsKeyRingsCryptoKeysUpdatePrimaryVersionRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsCryptoKeysUpdatePrimaryVersionRequest
  object.

  Fields:
    name: The resource name of the CryptoKey to update.
    updateCryptoKeyPrimaryVersionRequest: A
      UpdateCryptoKeyPrimaryVersionRequest resource to be passed as the
      request body.
  """

  name = _messages.StringField(1, required=True)
  updateCryptoKeyPrimaryVersionRequest = _messages.MessageField('UpdateCryptoKeyPrimaryVersionRequest', 2)


class CloudkmsProjectsLocationsKeyRingsGetIamPolicyRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsGetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  resource = _messages.StringField(1, required=True)


class CloudkmsProjectsLocationsKeyRingsGetRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsGetRequest object.

  Fields:
    name: The name of the KeyRing to get.
  """

  name = _messages.StringField(1, required=True)


class CloudkmsProjectsLocationsKeyRingsListRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsListRequest object.

  Fields:
    pageSize: Optional limit on the number of KeyRings to include in the
      response.  Further KeyRings can subsequently be obtained by including
      the ListKeyRingsResponse.next_page_token in a subsequent request.  If
      unspecified, the server will pick an appropriate default.
    pageToken: Optional pagination token, returned earlier via
      ListKeyRingsResponse.next_page_token.
    parent: Required. The resource name of the location associated with the
      KeyRings, in the format `projects/*/locations/*`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudkmsProjectsLocationsKeyRingsSetIamPolicyRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class CloudkmsProjectsLocationsKeyRingsTestIamPermissionsRequest(_messages.Message):
  """A CloudkmsProjectsLocationsKeyRingsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class CloudkmsProjectsLocationsListRequest(_messages.Message):
  """A CloudkmsProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class CryptoKey(_messages.Message):
  """A CryptoKey represents a logical key that can be used for cryptographic
  operations.  A CryptoKey is made up of one or more versions, which represent
  the actual key material used in cryptographic operations.

  Enums:
    PurposeValueValuesEnum: The immutable purpose of this CryptoKey.
      Currently, the only acceptable purpose is ENCRYPT_DECRYPT.

  Messages:
    LabelsValue: Labels with user-defined metadata. For more information, see
      [Labeling Keys](/kms/docs/labeling-keys).

  Fields:
    createTime: Output only. The time at which this CryptoKey was created.
    labels: Labels with user-defined metadata. For more information, see
      [Labeling Keys](/kms/docs/labeling-keys).
    name: Output only. The resource name for this CryptoKey in the format
      `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
    nextRotationTime: At next_rotation_time, the Key Management Service will
      automatically:  1. Create a new version of this CryptoKey. 2. Mark the
      new version as primary.  Key rotations performed manually via
      CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect
      next_rotation_time.
    primary: Output only. A copy of the "primary" CryptoKeyVersion that will
      be used by Encrypt when this CryptoKey is given in EncryptRequest.name.
      The CryptoKey's primary version can be updated via
      UpdateCryptoKeyPrimaryVersion.
    purpose: The immutable purpose of this CryptoKey. Currently, the only
      acceptable purpose is ENCRYPT_DECRYPT.
    rotationPeriod: next_rotation_time will be advanced by this period when
      the service automatically rotates a key. Must be at least one day.  If
      rotation_period is set, next_rotation_time must also be set.
  """

  class PurposeValueValuesEnum(_messages.Enum):
    """The immutable purpose of this CryptoKey. Currently, the only acceptable
    purpose is ENCRYPT_DECRYPT.

    Values:
      CRYPTO_KEY_PURPOSE_UNSPECIFIED: Not specified.
      ENCRYPT_DECRYPT: CryptoKeys with this purpose may be used with Encrypt
        and Decrypt.
    """
    CRYPTO_KEY_PURPOSE_UNSPECIFIED = 0
    ENCRYPT_DECRYPT = 1

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """Labels with user-defined metadata. For more information, see [Labeling
    Keys](/kms/docs/labeling-keys).

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  name = _messages.StringField(3)
  nextRotationTime = _messages.StringField(4)
  primary = _messages.MessageField('CryptoKeyVersion', 5)
  purpose = _messages.EnumField('PurposeValueValuesEnum', 6)
  rotationPeriod = _messages.StringField(7)


class CryptoKeyVersion(_messages.Message):
  """A CryptoKeyVersion represents an individual cryptographic key, and the
  associated key material.  It can be used for cryptographic operations either
  directly, or via its parent CryptoKey, in which case the server will choose
  the appropriate version for the operation.  For security reasons, the raw
  cryptographic key material represented by a CryptoKeyVersion can never be
  viewed or exported. It can only be used to encrypt or decrypt data when an
  authorized user or application invokes Cloud KMS.

  Enums:
    StateValueValuesEnum: The current state of the CryptoKeyVersion.

  Fields:
    createTime: Output only. The time at which this CryptoKeyVersion was
      created.
    destroyEventTime: Output only. The time this CryptoKeyVersion's key
      material was destroyed. Only present if state is DESTROYED.
    destroyTime: Output only. The time this CryptoKeyVersion's key material is
      scheduled for destruction. Only present if state is DESTROY_SCHEDULED.
    name: Output only. The resource name for this CryptoKeyVersion in the
      format
      `projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*`.
    state: The current state of the CryptoKeyVersion.
  """

  class StateValueValuesEnum(_messages.Enum):
    """The current state of the CryptoKeyVersion.

    Values:
      CRYPTO_KEY_VERSION_STATE_UNSPECIFIED: Not specified.
      ENABLED: This version may be used in Encrypt and Decrypt requests.
      DISABLED: This version may not be used, but the key material is still
        available, and the version can be placed back into the ENABLED state.
      DESTROYED: This version is destroyed, and the key material is no longer
        stored. A version may not leave this state once entered.
      DESTROY_SCHEDULED: This version is scheduled for destruction, and will
        be destroyed soon. Call RestoreCryptoKeyVersion to put it back into
        the DISABLED state.
    """
    CRYPTO_KEY_VERSION_STATE_UNSPECIFIED = 0
    ENABLED = 1
    DISABLED = 2
    DESTROYED = 3
    DESTROY_SCHEDULED = 4

  createTime = _messages.StringField(1)
  destroyEventTime = _messages.StringField(2)
  destroyTime = _messages.StringField(3)
  name = _messages.StringField(4)
  state = _messages.EnumField('StateValueValuesEnum', 5)


class DecryptRequest(_messages.Message):
  """Request message for KeyManagementService.Decrypt.

  Fields:
    additionalAuthenticatedData: Optional data that must match the data
      originally supplied in EncryptRequest.additional_authenticated_data.
    ciphertext: Required. The encrypted data originally returned in
      EncryptResponse.ciphertext.
  """

  additionalAuthenticatedData = _messages.BytesField(1)
  ciphertext = _messages.BytesField(2)


class DecryptResponse(_messages.Message):
  """Response message for KeyManagementService.Decrypt.

  Fields:
    plaintext: The decrypted data originally supplied in
      EncryptRequest.plaintext.
  """

  plaintext = _messages.BytesField(1)


class DestroyCryptoKeyVersionRequest(_messages.Message):
  """Request message for KeyManagementService.DestroyCryptoKeyVersion."""


class EncryptRequest(_messages.Message):
  """Request message for KeyManagementService.Encrypt.

  Fields:
    additionalAuthenticatedData: Optional data that, if specified, must also
      be provided during decryption through
      DecryptRequest.additional_authenticated_data.  Must be no larger than
      64KiB.
    plaintext: Required. The data to encrypt. Must be no larger than 64KiB.
  """

  additionalAuthenticatedData = _messages.BytesField(1)
  plaintext = _messages.BytesField(2)


class EncryptResponse(_messages.Message):
  """Response message for KeyManagementService.Encrypt.

  Fields:
    ciphertext: The encrypted data.
    name: The resource name of the CryptoKeyVersion used in encryption.
  """

  ciphertext = _messages.BytesField(1)
  name = _messages.StringField(2)


class KeyRing(_messages.Message):
  """A KeyRing is a toplevel logical grouping of CryptoKeys.

  Fields:
    createTime: Output only. The time at which this KeyRing was created.
    name: Output only. The resource name for the KeyRing in the format
      `projects/*/locations/*/keyRings/*`.
  """

  createTime = _messages.StringField(1)
  name = _messages.StringField(2)


class ListCryptoKeyVersionsResponse(_messages.Message):
  """Response message for KeyManagementService.ListCryptoKeyVersions.

  Fields:
    cryptoKeyVersions: The list of CryptoKeyVersions.
    nextPageToken: A token to retrieve next page of results. Pass this value
      in ListCryptoKeyVersionsRequest.page_token to retrieve the next page of
      results.
    totalSize: The total number of CryptoKeyVersions that matched the query.
  """

  cryptoKeyVersions = _messages.MessageField('CryptoKeyVersion', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  totalSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class ListCryptoKeysResponse(_messages.Message):
  """Response message for KeyManagementService.ListCryptoKeys.

  Fields:
    cryptoKeys: The list of CryptoKeys.
    nextPageToken: A token to retrieve next page of results. Pass this value
      in ListCryptoKeysRequest.page_token to retrieve the next page of
      results.
    totalSize: The total number of CryptoKeys that matched the query.
  """

  cryptoKeys = _messages.MessageField('CryptoKey', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  totalSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class ListKeyRingsResponse(_messages.Message):
  """Response message for KeyManagementService.ListKeyRings.

  Fields:
    keyRings: The list of KeyRings.
    nextPageToken: A token to retrieve next page of results. Pass this value
      in ListKeyRingsRequest.page_token to retrieve the next page of results.
    totalSize: The total number of KeyRings that matched the query.
  """

  keyRings = _messages.MessageField('KeyRing', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  totalSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class ListLocationsResponse(_messages.Message):
  """The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class Location(_messages.Message):
  """A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  labels = _messages.MessageField('LabelsValue', 1)
  locationId = _messages.StringField(2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)


class Policy(_messages.Message):
  """Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Cloud Platform resources.   A `Policy`
  consists of a list of `bindings`. A `Binding` binds a list of `members` to a
  `role`, where the members can be user accounts, Google groups, Google
  domains, and service accounts. A `role` is a named list of permissions
  defined by IAM.  **Example**      {       "bindings": [         {
  "role": "roles/owner",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-other-
  app@appspot.gserviceaccount.com",           ]         },         {
  "role": "roles/viewer",           "members": ["user:sean@example.com"]
  }       ]     }  For a description of IAM and its features, see the [IAM
  developer's guide](https://cloud.google.com/iam/docs).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. `bindings` with no
      members will result in an error.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  If no `etag` is provided in the call to `setIamPolicy`, then
      the existing policy is overwritten blindly.
    version: Deprecated.
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class RestoreCryptoKeyVersionRequest(_messages.Message):
  """Request message for KeyManagementService.RestoreCryptoKeyVersion."""


class SetIamPolicyRequest(_messages.Message):
  """Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
    updateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, the following default mask is used: paths: "bindings, etag"
      This field is only used by Cloud IAM.
  """

  policy = _messages.MessageField('Policy', 1)
  updateMask = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class TestIamPermissionsRequest(_messages.Message):
  """Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  """Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class UpdateCryptoKeyPrimaryVersionRequest(_messages.Message):
  """Request message for KeyManagementService.UpdateCryptoKeyPrimaryVersion.

  Fields:
    cryptoKeyVersionId: The id of the child CryptoKeyVersion to use as
      primary.
  """

  cryptoKeyVersionId = _messages.StringField(1)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
