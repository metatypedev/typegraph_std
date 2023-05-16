from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    EndpointIn: t.typedef = ...
    EndpointOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    CloudSQLInstanceInfoIn: t.typedef = ...
    CloudSQLInstanceInfoOut: t.typedef = ...
    AppEngineVersionInfoIn: t.typedef = ...
    AppEngineVersionInfoOut: t.typedef = ...
    VpcConnectorInfoIn: t.typedef = ...
    VpcConnectorInfoOut: t.typedef = ...
    AppEngineVersionEndpointIn: t.typedef = ...
    AppEngineVersionEndpointOut: t.typedef = ...
    ListConnectivityTestsResponseIn: t.typedef = ...
    ListConnectivityTestsResponseOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    CloudRunRevisionInfoIn: t.typedef = ...
    CloudRunRevisionInfoOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    ReachabilityDetailsIn: t.typedef = ...
    ReachabilityDetailsOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    RerunConnectivityTestRequestIn: t.typedef = ...
    RerunConnectivityTestRequestOut: t.typedef = ...
    VpnGatewayInfoIn: t.typedef = ...
    VpnGatewayInfoOut: t.typedef = ...
    ForwardingRuleInfoIn: t.typedef = ...
    ForwardingRuleInfoOut: t.typedef = ...
    AbortInfoIn: t.typedef = ...
    AbortInfoOut: t.typedef = ...
    NetworkInfoIn: t.typedef = ...
    NetworkInfoOut: t.typedef = ...
    CloudFunctionEndpointIn: t.typedef = ...
    CloudFunctionEndpointOut: t.typedef = ...
    RouteInfoIn: t.typedef = ...
    RouteInfoOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    ForwardInfoIn: t.typedef = ...
    ForwardInfoOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    InstanceInfoIn: t.typedef = ...
    InstanceInfoOut: t.typedef = ...
    DropInfoIn: t.typedef = ...
    DropInfoOut: t.typedef = ...
    VpnTunnelInfoIn: t.typedef = ...
    VpnTunnelInfoOut: t.typedef = ...
    LoadBalancerInfoIn: t.typedef = ...
    LoadBalancerInfoOut: t.typedef = ...
    CloudFunctionInfoIn: t.typedef = ...
    CloudFunctionInfoOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    CloudRunRevisionEndpointIn: t.typedef = ...
    CloudRunRevisionEndpointOut: t.typedef = ...
    GKEMasterInfoIn: t.typedef = ...
    GKEMasterInfoOut: t.typedef = ...
    DeliverInfoIn: t.typedef = ...
    DeliverInfoOut: t.typedef = ...
    FirewallInfoIn: t.typedef = ...
    FirewallInfoOut: t.typedef = ...
    TraceIn: t.typedef = ...
    TraceOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    ConnectivityTestIn: t.typedef = ...
    ConnectivityTestOut: t.typedef = ...
    StepIn: t.typedef = ...
    StepOut: t.typedef = ...
    LoadBalancerBackendIn: t.typedef = ...
    LoadBalancerBackendOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    EndpointInfoIn: t.typedef = ...
    EndpointInfoOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsGlobalOperationsGet: t.func = ...
    projectsLocationsGlobalOperationsList: t.func = ...
    projectsLocationsGlobalOperationsDelete: t.func = ...
    projectsLocationsGlobalOperationsCancel: t.func = ...
    projectsLocationsGlobalConnectivityTestsList: t.func = ...
    projectsLocationsGlobalConnectivityTestsDelete: t.func = ...
    projectsLocationsGlobalConnectivityTestsPatch: t.func = ...
    projectsLocationsGlobalConnectivityTestsRerun: t.func = ...
    projectsLocationsGlobalConnectivityTestsCreate: t.func = ...
    projectsLocationsGlobalConnectivityTestsGetIamPolicy: t.func = ...
    projectsLocationsGlobalConnectivityTestsTestIamPermissions: t.func = ...
    projectsLocationsGlobalConnectivityTestsSetIamPolicy: t.func = ...
    projectsLocationsGlobalConnectivityTestsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_networkmanagement() -> Import: ...
