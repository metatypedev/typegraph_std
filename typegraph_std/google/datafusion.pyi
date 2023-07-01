from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    VersionIn: t.typedef = ...
    VersionOut: t.typedef = ...
    DnsPeeringIn: t.typedef = ...
    DnsPeeringOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    CryptoKeyConfigIn: t.typedef = ...
    CryptoKeyConfigOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    NetworkConfigIn: t.typedef = ...
    NetworkConfigOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    ListInstancesResponseIn: t.typedef = ...
    ListInstancesResponseOut: t.typedef = ...
    AcceleratorIn: t.typedef = ...
    AcceleratorOut: t.typedef = ...
    InstanceIn: t.typedef = ...
    InstanceOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    RestartInstanceRequestIn: t.typedef = ...
    RestartInstanceRequestOut: t.typedef = ...
    ListDnsPeeringsResponseIn: t.typedef = ...
    ListDnsPeeringsResponseOut: t.typedef = ...
    ListAvailableVersionsResponseIn: t.typedef = ...
    ListAvailableVersionsResponseOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    EventPublishConfigIn: t.typedef = ...
    EventPublishConfigOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsInstancesRestart: t.func = ...
    projectsLocationsInstancesCreate: t.func = ...
    projectsLocationsInstancesPatch: t.func = ...
    projectsLocationsInstancesSetIamPolicy: t.func = ...
    projectsLocationsInstancesGet: t.func = ...
    projectsLocationsInstancesDelete: t.func = ...
    projectsLocationsInstancesList: t.func = ...
    projectsLocationsInstancesTestIamPermissions: t.func = ...
    projectsLocationsInstancesGetIamPolicy: t.func = ...
    projectsLocationsInstancesDnsPeeringsList: t.func = ...
    projectsLocationsInstancesDnsPeeringsDelete: t.func = ...
    projectsLocationsInstancesDnsPeeringsCreate: t.func = ...
    projectsLocationsVersionsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_datafusion() -> Import: ...
