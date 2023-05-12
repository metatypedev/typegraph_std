from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ReportStateAndNotificationRequestIn: t.typedef = ...
    ReportStateAndNotificationRequestOut: t.typedef = ...
    AgentDeviceIdIn: t.typedef = ...
    AgentDeviceIdOut: t.typedef = ...
    StateAndNotificationPayloadIn: t.typedef = ...
    StateAndNotificationPayloadOut: t.typedef = ...
    QueryResponseIn: t.typedef = ...
    QueryResponseOut: t.typedef = ...
    RequestSyncDevicesResponseIn: t.typedef = ...
    RequestSyncDevicesResponseOut: t.typedef = ...
    DeviceInfoIn: t.typedef = ...
    DeviceInfoOut: t.typedef = ...
    QueryRequestIn: t.typedef = ...
    QueryRequestOut: t.typedef = ...
    ReportStateAndNotificationDeviceIn: t.typedef = ...
    ReportStateAndNotificationDeviceOut: t.typedef = ...
    DeviceNamesIn: t.typedef = ...
    DeviceNamesOut: t.typedef = ...
    QueryRequestPayloadIn: t.typedef = ...
    QueryRequestPayloadOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    RequestSyncDevicesRequestIn: t.typedef = ...
    RequestSyncDevicesRequestOut: t.typedef = ...
    DeviceIn: t.typedef = ...
    DeviceOut: t.typedef = ...
    SyncResponseIn: t.typedef = ...
    SyncResponseOut: t.typedef = ...
    SyncRequestIn: t.typedef = ...
    SyncRequestOut: t.typedef = ...
    SyncResponsePayloadIn: t.typedef = ...
    SyncResponsePayloadOut: t.typedef = ...
    AgentOtherDeviceIdIn: t.typedef = ...
    AgentOtherDeviceIdOut: t.typedef = ...
    QueryRequestInputIn: t.typedef = ...
    QueryRequestInputOut: t.typedef = ...
    QueryResponsePayloadIn: t.typedef = ...
    QueryResponsePayloadOut: t.typedef = ...
    ReportStateAndNotificationResponseIn: t.typedef = ...
    ReportStateAndNotificationResponseOut: t.typedef = ...

class FuncList:
    devicesSync: t.func = ...
    devicesRequestSync: t.func = ...
    devicesQuery: t.func = ...
    devicesReportStateAndNotification: t.func = ...
    agentUsersDelete: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_homegraph() -> Import: ...
