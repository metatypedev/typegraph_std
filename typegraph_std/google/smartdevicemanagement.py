from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_smartdevicemanagement() -> Import:
    smartdevicemanagement = HTTPRuntime("https://smartdevicemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_smartdevicemanagement_1_ErrorResponse",
        "GoogleHomeEnterpriseSdmV1ListRoomsResponseIn": "_smartdevicemanagement_2_GoogleHomeEnterpriseSdmV1ListRoomsResponseIn",
        "GoogleHomeEnterpriseSdmV1ListRoomsResponseOut": "_smartdevicemanagement_3_GoogleHomeEnterpriseSdmV1ListRoomsResponseOut",
        "GoogleHomeEnterpriseSdmV1RoomIn": "_smartdevicemanagement_4_GoogleHomeEnterpriseSdmV1RoomIn",
        "GoogleHomeEnterpriseSdmV1RoomOut": "_smartdevicemanagement_5_GoogleHomeEnterpriseSdmV1RoomOut",
        "GoogleHomeEnterpriseSdmV1StructureIn": "_smartdevicemanagement_6_GoogleHomeEnterpriseSdmV1StructureIn",
        "GoogleHomeEnterpriseSdmV1StructureOut": "_smartdevicemanagement_7_GoogleHomeEnterpriseSdmV1StructureOut",
        "GoogleHomeEnterpriseSdmV1ListDevicesResponseIn": "_smartdevicemanagement_8_GoogleHomeEnterpriseSdmV1ListDevicesResponseIn",
        "GoogleHomeEnterpriseSdmV1ListDevicesResponseOut": "_smartdevicemanagement_9_GoogleHomeEnterpriseSdmV1ListDevicesResponseOut",
        "GoogleHomeEnterpriseSdmV1ParentRelationIn": "_smartdevicemanagement_10_GoogleHomeEnterpriseSdmV1ParentRelationIn",
        "GoogleHomeEnterpriseSdmV1ParentRelationOut": "_smartdevicemanagement_11_GoogleHomeEnterpriseSdmV1ParentRelationOut",
        "GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestIn": "_smartdevicemanagement_12_GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestIn",
        "GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestOut": "_smartdevicemanagement_13_GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestOut",
        "GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseIn": "_smartdevicemanagement_14_GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseIn",
        "GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut": "_smartdevicemanagement_15_GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut",
        "GoogleHomeEnterpriseSdmV1DeviceIn": "_smartdevicemanagement_16_GoogleHomeEnterpriseSdmV1DeviceIn",
        "GoogleHomeEnterpriseSdmV1DeviceOut": "_smartdevicemanagement_17_GoogleHomeEnterpriseSdmV1DeviceOut",
        "GoogleHomeEnterpriseSdmV1ListStructuresResponseIn": "_smartdevicemanagement_18_GoogleHomeEnterpriseSdmV1ListStructuresResponseIn",
        "GoogleHomeEnterpriseSdmV1ListStructuresResponseOut": "_smartdevicemanagement_19_GoogleHomeEnterpriseSdmV1ListStructuresResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleHomeEnterpriseSdmV1ListRoomsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rooms": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1RoomIn"])
            ).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ListRoomsResponseIn"])
    types["GoogleHomeEnterpriseSdmV1ListRoomsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rooms": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1RoomOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ListRoomsResponseOut"])
    types["GoogleHomeEnterpriseSdmV1RoomIn"] = t.struct(
        {"traits": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleHomeEnterpriseSdmV1RoomIn"])
    types["GoogleHomeEnterpriseSdmV1RoomOut"] = t.struct(
        {
            "name": t.string().optional(),
            "traits": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1RoomOut"])
    types["GoogleHomeEnterpriseSdmV1StructureIn"] = t.struct(
        {"traits": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleHomeEnterpriseSdmV1StructureIn"])
    types["GoogleHomeEnterpriseSdmV1StructureOut"] = t.struct(
        {
            "traits": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1StructureOut"])
    types["GoogleHomeEnterpriseSdmV1ListDevicesResponseIn"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1DeviceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ListDevicesResponseIn"])
    types["GoogleHomeEnterpriseSdmV1ListDevicesResponseOut"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1DeviceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ListDevicesResponseOut"])
    types["GoogleHomeEnterpriseSdmV1ParentRelationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleHomeEnterpriseSdmV1ParentRelationIn"])
    types["GoogleHomeEnterpriseSdmV1ParentRelationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ParentRelationOut"])
    types["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "command": t.string().optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestIn"])
    types["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "command": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequestOut"])
    types["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseIn"] = t.struct(
        {"results": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseIn"])
    types["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut"] = t.struct(
        {
            "results": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut"])
    types["GoogleHomeEnterpriseSdmV1DeviceIn"] = t.struct(
        {
            "name": t.string(),
            "parentRelations": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1ParentRelationIn"])
            ).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1DeviceIn"])
    types["GoogleHomeEnterpriseSdmV1DeviceOut"] = t.struct(
        {
            "name": t.string(),
            "type": t.string().optional(),
            "parentRelations": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1ParentRelationOut"])
            ).optional(),
            "traits": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1DeviceOut"])
    types["GoogleHomeEnterpriseSdmV1ListStructuresResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "structures": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1StructureIn"])
            ).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ListStructuresResponseIn"])
    types["GoogleHomeEnterpriseSdmV1ListStructuresResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "structures": t.array(
                t.proxy(renames["GoogleHomeEnterpriseSdmV1StructureOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleHomeEnterpriseSdmV1ListStructuresResponseOut"])

    functions = {}
    functions["enterprisesDevicesGet"] = smartdevicemanagement.post(
        "v1/{name}:executeCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "command": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesList"] = smartdevicemanagement.post(
        "v1/{name}:executeCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "command": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesExecuteCommand"] = smartdevicemanagement.post(
        "v1/{name}:executeCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "command": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesStructuresGet"] = smartdevicemanagement.get(
        "v1/{parent}/structures",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleHomeEnterpriseSdmV1ListStructuresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesStructuresList"] = smartdevicemanagement.get(
        "v1/{parent}/structures",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleHomeEnterpriseSdmV1ListStructuresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesStructuresRoomsList"] = smartdevicemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleHomeEnterpriseSdmV1RoomOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesStructuresRoomsGet"] = smartdevicemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleHomeEnterpriseSdmV1RoomOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="smartdevicemanagement",
        renames=renames,
        types=types,
        functions=functions,
    )
