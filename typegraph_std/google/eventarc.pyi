from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    GoogleLongrunningOperationIn: t.typedef = ...
    GoogleLongrunningOperationOut: t.typedef = ...
    GoogleLongrunningListOperationsResponseIn: t.typedef = ...
    GoogleLongrunningListOperationsResponseOut: t.typedef = ...
    CloudRunIn: t.typedef = ...
    CloudRunOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    FilteringAttributeIn: t.typedef = ...
    FilteringAttributeOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    GoogleLongrunningCancelOperationRequestIn: t.typedef = ...
    GoogleLongrunningCancelOperationRequestOut: t.typedef = ...
    GoogleChannelConfigIn: t.typedef = ...
    GoogleChannelConfigOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    StateConditionIn: t.typedef = ...
    StateConditionOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    ListTriggersResponseIn: t.typedef = ...
    ListTriggersResponseOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    EventTypeIn: t.typedef = ...
    EventTypeOut: t.typedef = ...
    PubsubIn: t.typedef = ...
    PubsubOut: t.typedef = ...
    ProviderIn: t.typedef = ...
    ProviderOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    TransportIn: t.typedef = ...
    TransportOut: t.typedef = ...
    DestinationIn: t.typedef = ...
    DestinationOut: t.typedef = ...
    ListChannelConnectionsResponseIn: t.typedef = ...
    ListChannelConnectionsResponseOut: t.typedef = ...
    GoogleRpcStatusIn: t.typedef = ...
    GoogleRpcStatusOut: t.typedef = ...
    ListChannelsResponseIn: t.typedef = ...
    ListChannelsResponseOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    GKEIn: t.typedef = ...
    GKEOut: t.typedef = ...
    ChannelConnectionIn: t.typedef = ...
    ChannelConnectionOut: t.typedef = ...
    TriggerIn: t.typedef = ...
    TriggerOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    ListProvidersResponseIn: t.typedef = ...
    ListProvidersResponseOut: t.typedef = ...
    EventFilterIn: t.typedef = ...
    EventFilterOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    ChannelIn: t.typedef = ...
    ChannelOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsGetGoogleChannelConfig: t.func = ...
    projectsLocationsUpdateGoogleChannelConfig: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsChannelConnectionsSetIamPolicy: t.func = ...
    projectsLocationsChannelConnectionsGetIamPolicy: t.func = ...
    projectsLocationsChannelConnectionsCreate: t.func = ...
    projectsLocationsChannelConnectionsDelete: t.func = ...
    projectsLocationsChannelConnectionsTestIamPermissions: t.func = ...
    projectsLocationsChannelConnectionsList: t.func = ...
    projectsLocationsChannelConnectionsGet: t.func = ...
    projectsLocationsChannelsList: t.func = ...
    projectsLocationsChannelsCreate: t.func = ...
    projectsLocationsChannelsPatch: t.func = ...
    projectsLocationsChannelsDelete: t.func = ...
    projectsLocationsChannelsTestIamPermissions: t.func = ...
    projectsLocationsChannelsGetIamPolicy: t.func = ...
    projectsLocationsChannelsSetIamPolicy: t.func = ...
    projectsLocationsChannelsGet: t.func = ...
    projectsLocationsProvidersGet: t.func = ...
    projectsLocationsProvidersList: t.func = ...
    projectsLocationsTriggersTestIamPermissions: t.func = ...
    projectsLocationsTriggersCreate: t.func = ...
    projectsLocationsTriggersGetIamPolicy: t.func = ...
    projectsLocationsTriggersGet: t.func = ...
    projectsLocationsTriggersDelete: t.func = ...
    projectsLocationsTriggersSetIamPolicy: t.func = ...
    projectsLocationsTriggersPatch: t.func = ...
    projectsLocationsTriggersList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_eventarc() -> Import: ...
