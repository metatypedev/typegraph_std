from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    AutomaticIn: t.typedef = ...
    AutomaticOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    AccessSecretVersionResponseIn: t.typedef = ...
    AccessSecretVersionResponseOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    UserManagedIn: t.typedef = ...
    UserManagedOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    AutomaticStatusIn: t.typedef = ...
    AutomaticStatusOut: t.typedef = ...
    AddSecretVersionRequestIn: t.typedef = ...
    AddSecretVersionRequestOut: t.typedef = ...
    CustomerManagedEncryptionStatusIn: t.typedef = ...
    CustomerManagedEncryptionStatusOut: t.typedef = ...
    ListSecretsResponseIn: t.typedef = ...
    ListSecretsResponseOut: t.typedef = ...
    DestroySecretVersionRequestIn: t.typedef = ...
    DestroySecretVersionRequestOut: t.typedef = ...
    SecretPayloadIn: t.typedef = ...
    SecretPayloadOut: t.typedef = ...
    DisableSecretVersionRequestIn: t.typedef = ...
    DisableSecretVersionRequestOut: t.typedef = ...
    SecretIn: t.typedef = ...
    SecretOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    EnableSecretVersionRequestIn: t.typedef = ...
    EnableSecretVersionRequestOut: t.typedef = ...
    SecretVersionIn: t.typedef = ...
    SecretVersionOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    ReplicaStatusIn: t.typedef = ...
    ReplicaStatusOut: t.typedef = ...
    ListSecretVersionsResponseIn: t.typedef = ...
    ListSecretVersionsResponseOut: t.typedef = ...
    TopicIn: t.typedef = ...
    TopicOut: t.typedef = ...
    ReplicationStatusIn: t.typedef = ...
    ReplicationStatusOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    RotationIn: t.typedef = ...
    RotationOut: t.typedef = ...
    CustomerManagedEncryptionIn: t.typedef = ...
    CustomerManagedEncryptionOut: t.typedef = ...
    ReplicationIn: t.typedef = ...
    ReplicationOut: t.typedef = ...
    UserManagedStatusIn: t.typedef = ...
    UserManagedStatusOut: t.typedef = ...
    ReplicaIn: t.typedef = ...
    ReplicaOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsSecretsCreate: t.func = ...
    projectsSecretsGet: t.func = ...
    projectsSecretsTestIamPermissions: t.func = ...
    projectsSecretsPatch: t.func = ...
    projectsSecretsAddVersion: t.func = ...
    projectsSecretsSetIamPolicy: t.func = ...
    projectsSecretsDelete: t.func = ...
    projectsSecretsGetIamPolicy: t.func = ...
    projectsSecretsList: t.func = ...
    projectsSecretsVersionsDisable: t.func = ...
    projectsSecretsVersionsEnable: t.func = ...
    projectsSecretsVersionsList: t.func = ...
    projectsSecretsVersionsAccess: t.func = ...
    projectsSecretsVersionsDestroy: t.func = ...
    projectsSecretsVersionsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_secretmanager() -> Import: ...
