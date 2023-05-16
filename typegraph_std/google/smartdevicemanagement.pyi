from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ListStructuresResponseIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ListStructuresResponseOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1RoomIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1RoomOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ParentRelationIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ParentRelationOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1StructureIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1StructureOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1DeviceIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1DeviceOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ListDevicesResponseIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ListDevicesResponseOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ListRoomsResponseIn: t.typedef = ...
    GoogleHomeEnterpriseSdmV1ListRoomsResponseOut: t.typedef = ...

class FuncList:
    enterprisesDevicesExecuteCommand: t.func = ...
    enterprisesDevicesList: t.func = ...
    enterprisesDevicesGet: t.func = ...
    enterprisesStructuresList: t.func = ...
    enterprisesStructuresGet: t.func = ...
    enterprisesStructuresRoomsList: t.func = ...
    enterprisesStructuresRoomsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_smartdevicemanagement() -> Import: ...
