from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_homegraph() -> Import:
    homegraph = HTTPRuntime("https://homegraph.googleapis.com/")

    renames = {
        "ErrorResponse": "_homegraph_1_ErrorResponse",
        "SyncResponsePayloadIn": "_homegraph_2_SyncResponsePayloadIn",
        "SyncResponsePayloadOut": "_homegraph_3_SyncResponsePayloadOut",
        "QueryResponsePayloadIn": "_homegraph_4_QueryResponsePayloadIn",
        "QueryResponsePayloadOut": "_homegraph_5_QueryResponsePayloadOut",
        "SyncRequestIn": "_homegraph_6_SyncRequestIn",
        "SyncRequestOut": "_homegraph_7_SyncRequestOut",
        "ReportStateAndNotificationRequestIn": "_homegraph_8_ReportStateAndNotificationRequestIn",
        "ReportStateAndNotificationRequestOut": "_homegraph_9_ReportStateAndNotificationRequestOut",
        "QueryResponseIn": "_homegraph_10_QueryResponseIn",
        "QueryResponseOut": "_homegraph_11_QueryResponseOut",
        "ReportStateAndNotificationDeviceIn": "_homegraph_12_ReportStateAndNotificationDeviceIn",
        "ReportStateAndNotificationDeviceOut": "_homegraph_13_ReportStateAndNotificationDeviceOut",
        "QueryRequestInputIn": "_homegraph_14_QueryRequestInputIn",
        "QueryRequestInputOut": "_homegraph_15_QueryRequestInputOut",
        "AgentOtherDeviceIdIn": "_homegraph_16_AgentOtherDeviceIdIn",
        "AgentOtherDeviceIdOut": "_homegraph_17_AgentOtherDeviceIdOut",
        "StateAndNotificationPayloadIn": "_homegraph_18_StateAndNotificationPayloadIn",
        "StateAndNotificationPayloadOut": "_homegraph_19_StateAndNotificationPayloadOut",
        "SyncResponseIn": "_homegraph_20_SyncResponseIn",
        "SyncResponseOut": "_homegraph_21_SyncResponseOut",
        "RequestSyncDevicesRequestIn": "_homegraph_22_RequestSyncDevicesRequestIn",
        "RequestSyncDevicesRequestOut": "_homegraph_23_RequestSyncDevicesRequestOut",
        "QueryRequestPayloadIn": "_homegraph_24_QueryRequestPayloadIn",
        "QueryRequestPayloadOut": "_homegraph_25_QueryRequestPayloadOut",
        "DeviceInfoIn": "_homegraph_26_DeviceInfoIn",
        "DeviceInfoOut": "_homegraph_27_DeviceInfoOut",
        "RequestSyncDevicesResponseIn": "_homegraph_28_RequestSyncDevicesResponseIn",
        "RequestSyncDevicesResponseOut": "_homegraph_29_RequestSyncDevicesResponseOut",
        "DeviceIn": "_homegraph_30_DeviceIn",
        "DeviceOut": "_homegraph_31_DeviceOut",
        "AgentDeviceIdIn": "_homegraph_32_AgentDeviceIdIn",
        "AgentDeviceIdOut": "_homegraph_33_AgentDeviceIdOut",
        "DeviceNamesIn": "_homegraph_34_DeviceNamesIn",
        "DeviceNamesOut": "_homegraph_35_DeviceNamesOut",
        "ReportStateAndNotificationResponseIn": "_homegraph_36_ReportStateAndNotificationResponseIn",
        "ReportStateAndNotificationResponseOut": "_homegraph_37_ReportStateAndNotificationResponseOut",
        "EmptyIn": "_homegraph_38_EmptyIn",
        "EmptyOut": "_homegraph_39_EmptyOut",
        "QueryRequestIn": "_homegraph_40_QueryRequestIn",
        "QueryRequestOut": "_homegraph_41_QueryRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SyncResponsePayloadIn"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "agentUserId": t.string().optional(),
        }
    ).named(renames["SyncResponsePayloadIn"])
    types["SyncResponsePayloadOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "agentUserId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncResponsePayloadOut"])
    types["QueryResponsePayloadIn"] = t.struct(
        {"devices": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["QueryResponsePayloadIn"])
    types["QueryResponsePayloadOut"] = t.struct(
        {
            "devices": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponsePayloadOut"])
    types["SyncRequestIn"] = t.struct(
        {"agentUserId": t.string(), "requestId": t.string().optional()}
    ).named(renames["SyncRequestIn"])
    types["SyncRequestOut"] = t.struct(
        {
            "agentUserId": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncRequestOut"])
    types["ReportStateAndNotificationRequestIn"] = t.struct(
        {
            "eventId": t.string().optional(),
            "agentUserId": t.string(),
            "followUpToken": t.string().optional(),
            "requestId": t.string().optional(),
            "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
        }
    ).named(renames["ReportStateAndNotificationRequestIn"])
    types["ReportStateAndNotificationRequestOut"] = t.struct(
        {
            "eventId": t.string().optional(),
            "agentUserId": t.string(),
            "followUpToken": t.string().optional(),
            "requestId": t.string().optional(),
            "payload": t.proxy(renames["StateAndNotificationPayloadOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationRequestOut"])
    types["QueryResponseIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "payload": t.proxy(renames["QueryResponsePayloadIn"]).optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "payload": t.proxy(renames["QueryResponsePayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["ReportStateAndNotificationDeviceIn"] = t.struct(
        {
            "states": t.struct({"_": t.string().optional()}).optional(),
            "notifications": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ReportStateAndNotificationDeviceIn"])
    types["ReportStateAndNotificationDeviceOut"] = t.struct(
        {
            "states": t.struct({"_": t.string().optional()}).optional(),
            "notifications": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationDeviceOut"])
    types["QueryRequestInputIn"] = t.struct(
        {"payload": t.proxy(renames["QueryRequestPayloadIn"]).optional()}
    ).named(renames["QueryRequestInputIn"])
    types["QueryRequestInputOut"] = t.struct(
        {
            "payload": t.proxy(renames["QueryRequestPayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestInputOut"])
    types["AgentOtherDeviceIdIn"] = t.struct(
        {"agentId": t.string().optional(), "deviceId": t.string().optional()}
    ).named(renames["AgentOtherDeviceIdIn"])
    types["AgentOtherDeviceIdOut"] = t.struct(
        {
            "agentId": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentOtherDeviceIdOut"])
    types["StateAndNotificationPayloadIn"] = t.struct(
        {"devices": t.proxy(renames["ReportStateAndNotificationDeviceIn"]).optional()}
    ).named(renames["StateAndNotificationPayloadIn"])
    types["StateAndNotificationPayloadOut"] = t.struct(
        {
            "devices": t.proxy(
                renames["ReportStateAndNotificationDeviceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateAndNotificationPayloadOut"])
    types["SyncResponseIn"] = t.struct(
        {
            "payload": t.proxy(renames["SyncResponsePayloadIn"]).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["SyncResponseIn"])
    types["SyncResponseOut"] = t.struct(
        {
            "payload": t.proxy(renames["SyncResponsePayloadOut"]).optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncResponseOut"])
    types["RequestSyncDevicesRequestIn"] = t.struct(
        {"async": t.boolean().optional(), "agentUserId": t.string()}
    ).named(renames["RequestSyncDevicesRequestIn"])
    types["RequestSyncDevicesRequestOut"] = t.struct(
        {
            "async": t.boolean().optional(),
            "agentUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestSyncDevicesRequestOut"])
    types["QueryRequestPayloadIn"] = t.struct(
        {"devices": t.array(t.proxy(renames["AgentDeviceIdIn"])).optional()}
    ).named(renames["QueryRequestPayloadIn"])
    types["QueryRequestPayloadOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["AgentDeviceIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestPayloadOut"])
    types["DeviceInfoIn"] = t.struct(
        {
            "manufacturer": t.string().optional(),
            "model": t.string().optional(),
            "swVersion": t.string().optional(),
            "hwVersion": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "manufacturer": t.string().optional(),
            "model": t.string().optional(),
            "swVersion": t.string().optional(),
            "hwVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
    types["RequestSyncDevicesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestSyncDevicesResponseIn"])
    types["RequestSyncDevicesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestSyncDevicesResponseOut"])
    types["DeviceIn"] = t.struct(
        {
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["DeviceNamesIn"]).optional(),
            "traits": t.array(t.string()).optional(),
            "roomHint": t.string().optional(),
            "structureHint": t.string().optional(),
            "willReportState": t.boolean().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoIn"]).optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdIn"])
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["DeviceNamesOut"]).optional(),
            "traits": t.array(t.string()).optional(),
            "roomHint": t.string().optional(),
            "structureHint": t.string().optional(),
            "willReportState": t.boolean().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoOut"]).optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdOut"])
            ).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["AgentDeviceIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["AgentDeviceIdIn"]
    )
    types["AgentDeviceIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentDeviceIdOut"])
    types["DeviceNamesIn"] = t.struct(
        {
            "nicknames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "defaultNames": t.array(t.string()).optional(),
        }
    ).named(renames["DeviceNamesIn"])
    types["DeviceNamesOut"] = t.struct(
        {
            "nicknames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "defaultNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceNamesOut"])
    types["ReportStateAndNotificationResponseIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ReportStateAndNotificationResponseIn"])
    types["ReportStateAndNotificationResponseOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "agentUserId": t.string(),
            "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
            "requestId": t.string().optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "agentUserId": t.string(),
            "inputs": t.array(t.proxy(renames["QueryRequestInputOut"])),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])

    functions = {}
    functions["agentUsersDelete"] = homegraph.delete(
        "v1/{agentUserId}",
        t.struct(
            {
                "agentUserId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesReportStateAndNotification"] = homegraph.post(
        "v1/devices:query",
        t.struct(
            {
                "agentUserId": t.string(),
                "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesRequestSync"] = homegraph.post(
        "v1/devices:query",
        t.struct(
            {
                "agentUserId": t.string(),
                "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesSync"] = homegraph.post(
        "v1/devices:query",
        t.struct(
            {
                "agentUserId": t.string(),
                "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesQuery"] = homegraph.post(
        "v1/devices:query",
        t.struct(
            {
                "agentUserId": t.string(),
                "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="homegraph", renames=renames, types=types, functions=functions
    )
