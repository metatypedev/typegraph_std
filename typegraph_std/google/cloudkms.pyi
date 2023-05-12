from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    KeyOperationAttestationIn: t.typedef = ...
    KeyOperationAttestationOut: t.typedef = ...
    WrappingPublicKeyIn: t.typedef = ...
    WrappingPublicKeyOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    ListCryptoKeysResponseIn: t.typedef = ...
    ListCryptoKeysResponseOut: t.typedef = ...
    PublicKeyIn: t.typedef = ...
    PublicKeyOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    VerifyConnectivityResponseIn: t.typedef = ...
    VerifyConnectivityResponseOut: t.typedef = ...
    DecryptResponseIn: t.typedef = ...
    DecryptResponseOut: t.typedef = ...
    EncryptResponseIn: t.typedef = ...
    EncryptResponseOut: t.typedef = ...
    EkmConnectionIn: t.typedef = ...
    EkmConnectionOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    DecryptRequestIn: t.typedef = ...
    DecryptRequestOut: t.typedef = ...
    CryptoKeyVersionIn: t.typedef = ...
    CryptoKeyVersionOut: t.typedef = ...
    DestroyCryptoKeyVersionRequestIn: t.typedef = ...
    DestroyCryptoKeyVersionRequestOut: t.typedef = ...
    MacVerifyResponseIn: t.typedef = ...
    MacVerifyResponseOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    UpdateCryptoKeyPrimaryVersionRequestIn: t.typedef = ...
    UpdateCryptoKeyPrimaryVersionRequestOut: t.typedef = ...
    DigestIn: t.typedef = ...
    DigestOut: t.typedef = ...
    MacSignResponseIn: t.typedef = ...
    MacSignResponseOut: t.typedef = ...
    GenerateRandomBytesRequestIn: t.typedef = ...
    GenerateRandomBytesRequestOut: t.typedef = ...
    LocationMetadataIn: t.typedef = ...
    LocationMetadataOut: t.typedef = ...
    MacVerifyRequestIn: t.typedef = ...
    MacVerifyRequestOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    GenerateRandomBytesResponseIn: t.typedef = ...
    GenerateRandomBytesResponseOut: t.typedef = ...
    ImportCryptoKeyVersionRequestIn: t.typedef = ...
    ImportCryptoKeyVersionRequestOut: t.typedef = ...
    RestoreCryptoKeyVersionRequestIn: t.typedef = ...
    RestoreCryptoKeyVersionRequestOut: t.typedef = ...
    AsymmetricSignRequestIn: t.typedef = ...
    AsymmetricSignRequestOut: t.typedef = ...
    ListEkmConnectionsResponseIn: t.typedef = ...
    ListEkmConnectionsResponseOut: t.typedef = ...
    AsymmetricDecryptRequestIn: t.typedef = ...
    AsymmetricDecryptRequestOut: t.typedef = ...
    AsymmetricDecryptResponseIn: t.typedef = ...
    AsymmetricDecryptResponseOut: t.typedef = ...
    ListImportJobsResponseIn: t.typedef = ...
    ListImportJobsResponseOut: t.typedef = ...
    CryptoKeyIn: t.typedef = ...
    CryptoKeyOut: t.typedef = ...
    ExternalProtectionLevelOptionsIn: t.typedef = ...
    ExternalProtectionLevelOptionsOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    CertificateChainsIn: t.typedef = ...
    CertificateChainsOut: t.typedef = ...
    CertificateIn: t.typedef = ...
    CertificateOut: t.typedef = ...
    EkmConfigIn: t.typedef = ...
    EkmConfigOut: t.typedef = ...
    ImportJobIn: t.typedef = ...
    ImportJobOut: t.typedef = ...
    KeyRingIn: t.typedef = ...
    KeyRingOut: t.typedef = ...
    CryptoKeyVersionTemplateIn: t.typedef = ...
    CryptoKeyVersionTemplateOut: t.typedef = ...
    MacSignRequestIn: t.typedef = ...
    MacSignRequestOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    EncryptRequestIn: t.typedef = ...
    EncryptRequestOut: t.typedef = ...
    ListKeyRingsResponseIn: t.typedef = ...
    ListKeyRingsResponseOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    ServiceResolverIn: t.typedef = ...
    ServiceResolverOut: t.typedef = ...
    AsymmetricSignResponseIn: t.typedef = ...
    AsymmetricSignResponseOut: t.typedef = ...
    ListCryptoKeyVersionsResponseIn: t.typedef = ...
    ListCryptoKeyVersionsResponseOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsGetEkmConfig: t.func = ...
    projectsLocationsUpdateEkmConfig: t.func = ...
    projectsLocationsGenerateRandomBytes: t.func = ...
    projectsLocationsEkmConnectionsCreate: t.func = ...
    projectsLocationsEkmConnectionsList: t.func = ...
    projectsLocationsEkmConnectionsPatch: t.func = ...
    projectsLocationsEkmConnectionsVerifyConnectivity: t.func = ...
    projectsLocationsEkmConnectionsTestIamPermissions: t.func = ...
    projectsLocationsEkmConnectionsGetIamPolicy: t.func = ...
    projectsLocationsEkmConnectionsGet: t.func = ...
    projectsLocationsEkmConnectionsSetIamPolicy: t.func = ...
    projectsLocationsKeyRingsGetIamPolicy: t.func = ...
    projectsLocationsKeyRingsSetIamPolicy: t.func = ...
    projectsLocationsKeyRingsGet: t.func = ...
    projectsLocationsKeyRingsList: t.func = ...
    projectsLocationsKeyRingsTestIamPermissions: t.func = ...
    projectsLocationsKeyRingsCreate: t.func = ...
    projectsLocationsKeyRingsCryptoKeysGet: t.func = ...
    projectsLocationsKeyRingsCryptoKeysEncrypt: t.func = ...
    projectsLocationsKeyRingsCryptoKeysGetIamPolicy: t.func = ...
    projectsLocationsKeyRingsCryptoKeysPatch: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCreate: t.func = ...
    projectsLocationsKeyRingsCryptoKeysUpdatePrimaryVersion: t.func = ...
    projectsLocationsKeyRingsCryptoKeysTestIamPermissions: t.func = ...
    projectsLocationsKeyRingsCryptoKeysSetIamPolicy: t.func = ...
    projectsLocationsKeyRingsCryptoKeysList: t.func = ...
    projectsLocationsKeyRingsCryptoKeysDecrypt: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGetPublicKey: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsMacVerify: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsPatch: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsDestroy: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsAsymmetricDecrypt: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsList: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsAsymmetricSign: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsMacSign: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsImport: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsGet: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsRestore: t.func = ...
    projectsLocationsKeyRingsCryptoKeysCryptoKeyVersionsCreate: t.func = ...
    projectsLocationsKeyRingsImportJobsTestIamPermissions: t.func = ...
    projectsLocationsKeyRingsImportJobsSetIamPolicy: t.func = ...
    projectsLocationsKeyRingsImportJobsGet: t.func = ...
    projectsLocationsKeyRingsImportJobsList: t.func = ...
    projectsLocationsKeyRingsImportJobsGetIamPolicy: t.func = ...
    projectsLocationsKeyRingsImportJobsCreate: t.func = ...
    projectsLocationsEkmConfigTestIamPermissions: t.func = ...
    projectsLocationsEkmConfigGetIamPolicy: t.func = ...
    projectsLocationsEkmConfigSetIamPolicy: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_cloudkms() -> Import: ...
