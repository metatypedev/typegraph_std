from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    StopWorkstationRequestIn: t.typedef = ...
    StopWorkstationRequestOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    ReadinessCheckIn: t.typedef = ...
    ReadinessCheckOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    ListUsableWorkstationConfigsResponseIn: t.typedef = ...
    ListUsableWorkstationConfigsResponseOut: t.typedef = ...
    GenerateAccessTokenResponseIn: t.typedef = ...
    GenerateAccessTokenResponseOut: t.typedef = ...
    GenerateAccessTokenRequestIn: t.typedef = ...
    GenerateAccessTokenRequestOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    ContainerIn: t.typedef = ...
    ContainerOut: t.typedef = ...
    GceConfidentialInstanceConfigIn: t.typedef = ...
    GceConfidentialInstanceConfigOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    WorkstationConfigIn: t.typedef = ...
    WorkstationConfigOut: t.typedef = ...
    StartWorkstationRequestIn: t.typedef = ...
    StartWorkstationRequestOut: t.typedef = ...
    ListWorkstationClustersResponseIn: t.typedef = ...
    ListWorkstationClustersResponseOut: t.typedef = ...
    WorkstationIn: t.typedef = ...
    WorkstationOut: t.typedef = ...
    ListWorkstationConfigsResponseIn: t.typedef = ...
    ListWorkstationConfigsResponseOut: t.typedef = ...
    PersistentDirectoryIn: t.typedef = ...
    PersistentDirectoryOut: t.typedef = ...
    GceInstanceIn: t.typedef = ...
    GceInstanceOut: t.typedef = ...
    AcceleratorIn: t.typedef = ...
    AcceleratorOut: t.typedef = ...
    CustomerEncryptionKeyIn: t.typedef = ...
    CustomerEncryptionKeyOut: t.typedef = ...
    ListWorkstationsResponseIn: t.typedef = ...
    ListWorkstationsResponseOut: t.typedef = ...
    GceRegionalPersistentDiskIn: t.typedef = ...
    GceRegionalPersistentDiskOut: t.typedef = ...
    WorkstationClusterIn: t.typedef = ...
    WorkstationClusterOut: t.typedef = ...
    PrivateClusterConfigIn: t.typedef = ...
    PrivateClusterConfigOut: t.typedef = ...
    GceShieldedInstanceConfigIn: t.typedef = ...
    GceShieldedInstanceConfigOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    GoogleProtobufEmptyIn: t.typedef = ...
    GoogleProtobufEmptyOut: t.typedef = ...
    ListUsableWorkstationsResponseIn: t.typedef = ...
    ListUsableWorkstationsResponseOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    HostIn: t.typedef = ...
    HostOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...

class FuncList:
    projectsLocationsWorkstationClustersGet: t.func = ...
    projectsLocationsWorkstationClustersList: t.func = ...
    projectsLocationsWorkstationClustersDelete: t.func = ...
    projectsLocationsWorkstationClustersPatch: t.func = ...
    projectsLocationsWorkstationClustersCreate: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsSetIamPolicy: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsTestIamPermissions: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsListUsable: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsList: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsPatch: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsGetIamPolicy: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsGet: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsCreate: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsDelete: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsList: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsPatch: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsListUsable: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsSetIamPolicy: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGenerateAccessToken: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsDelete: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStart: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGet: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGetIamPolicy: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsTestIamPermissions: t.func = (
        ...
    )
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStop: t.func = ...
    projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsCreate: t.func = (
        ...
    )
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_workstations() -> Import: ...
