from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ResourceUpdateIn: t.typedef = ...
    ResourceUpdateOut: t.typedef = ...
    DeploymentIn: t.typedef = ...
    DeploymentOut: t.typedef = ...
    ManifestsListResponseIn: t.typedef = ...
    ManifestsListResponseOut: t.typedef = ...
    DeploymentUpdateIn: t.typedef = ...
    DeploymentUpdateOut: t.typedef = ...
    DeploymentsStopRequestIn: t.typedef = ...
    DeploymentsStopRequestOut: t.typedef = ...
    ConfigFileIn: t.typedef = ...
    ConfigFileOut: t.typedef = ...
    ResourceAccessControlIn: t.typedef = ...
    ResourceAccessControlOut: t.typedef = ...
    OperationsListResponseIn: t.typedef = ...
    OperationsListResponseOut: t.typedef = ...
    TargetConfigurationIn: t.typedef = ...
    TargetConfigurationOut: t.typedef = ...
    DeploymentLabelEntryIn: t.typedef = ...
    DeploymentLabelEntryOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    TypesListResponseIn: t.typedef = ...
    TypesListResponseOut: t.typedef = ...
    ResourceIn: t.typedef = ...
    ResourceOut: t.typedef = ...
    GlobalSetPolicyRequestIn: t.typedef = ...
    GlobalSetPolicyRequestOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    DeploymentsListResponseIn: t.typedef = ...
    DeploymentsListResponseOut: t.typedef = ...
    DeploymentUpdateLabelEntryIn: t.typedef = ...
    DeploymentUpdateLabelEntryOut: t.typedef = ...
    ManifestIn: t.typedef = ...
    ManifestOut: t.typedef = ...
    TestPermissionsRequestIn: t.typedef = ...
    TestPermissionsRequestOut: t.typedef = ...
    TestPermissionsResponseIn: t.typedef = ...
    TestPermissionsResponseOut: t.typedef = ...
    TypeIn: t.typedef = ...
    TypeOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    ResourcesListResponseIn: t.typedef = ...
    ResourcesListResponseOut: t.typedef = ...
    DeploymentsCancelPreviewRequestIn: t.typedef = ...
    DeploymentsCancelPreviewRequestOut: t.typedef = ...
    ImportFileIn: t.typedef = ...
    ImportFileOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...

class FuncList:
    resourcesList: t.func = ...
    resourcesGet: t.func = ...
    typesList: t.func = ...
    operationsList: t.func = ...
    operationsGet: t.func = ...
    deploymentsCancelPreview: t.func = ...
    deploymentsStop: t.func = ...
    deploymentsPatch: t.func = ...
    deploymentsDelete: t.func = ...
    deploymentsInsert: t.func = ...
    deploymentsGetIamPolicy: t.func = ...
    deploymentsSetIamPolicy: t.func = ...
    deploymentsGet: t.func = ...
    deploymentsTestIamPermissions: t.func = ...
    deploymentsList: t.func = ...
    deploymentsUpdate: t.func = ...
    manifestsList: t.func = ...
    manifestsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_deploymentmanager() -> Import: ...
