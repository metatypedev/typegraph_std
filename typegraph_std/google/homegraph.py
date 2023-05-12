from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_homegraph() -> Import:
    homegraph = HTTPRuntime("https://homegraph.googleapis.com/")

    renames = {
        "ErrorResponse": "_homegraph_1_ErrorResponse",
        "ReportStateAndNotificationRequestIn": "_homegraph_2_ReportStateAndNotificationRequestIn",
        "ReportStateAndNotificationRequestOut": "_homegraph_3_ReportStateAndNotificationRequestOut",
        "AgentDeviceIdIn": "_homegraph_4_AgentDeviceIdIn",
        "AgentDeviceIdOut": "_homegraph_5_AgentDeviceIdOut",
        "StateAndNotificationPayloadIn": "_homegraph_6_StateAndNotificationPayloadIn",
        "StateAndNotificationPayloadOut": "_homegraph_7_StateAndNotificationPayloadOut",
        "QueryResponseIn": "_homegraph_8_QueryResponseIn",
        "QueryResponseOut": "_homegraph_9_QueryResponseOut",
        "RequestSyncDevicesResponseIn": "_homegraph_10_RequestSyncDevicesResponseIn",
        "RequestSyncDevicesResponseOut": "_homegraph_11_RequestSyncDevicesResponseOut",
        "DeviceInfoIn": "_homegraph_12_DeviceInfoIn",
        "DeviceInfoOut": "_homegraph_13_DeviceInfoOut",
        "QueryRequestIn": "_homegraph_14_QueryRequestIn",
        "QueryRequestOut": "_homegraph_15_QueryRequestOut",
        "ReportStateAndNotificationDeviceIn": "_homegraph_16_ReportStateAndNotificationDeviceIn",
        "ReportStateAndNotificationDeviceOut": "_homegraph_17_ReportStateAndNotificationDeviceOut",
        "DeviceNamesIn": "_homegraph_18_DeviceNamesIn",
        "DeviceNamesOut": "_homegraph_19_DeviceNamesOut",
        "QueryRequestPayloadIn": "_homegraph_20_QueryRequestPayloadIn",
        "QueryRequestPayloadOut": "_homegraph_21_QueryRequestPayloadOut",
        "EmptyIn": "_homegraph_22_EmptyIn",
        "EmptyOut": "_homegraph_23_EmptyOut",
        "RequestSyncDevicesRequestIn": "_homegraph_24_RequestSyncDevicesRequestIn",
        "RequestSyncDevicesRequestOut": "_homegraph_25_RequestSyncDevicesRequestOut",
        "DeviceIn": "_homegraph_26_DeviceIn",
        "DeviceOut": "_homegraph_27_DeviceOut",
        "SyncResponseIn": "_homegraph_28_SyncResponseIn",
        "SyncResponseOut": "_homegraph_29_SyncResponseOut",
        "SyncRequestIn": "_homegraph_30_SyncRequestIn",
        "SyncRequestOut": "_homegraph_31_SyncRequestOut",
        "SyncResponsePayloadIn": "_homegraph_32_SyncResponsePayloadIn",
        "SyncResponsePayloadOut": "_homegraph_33_SyncResponsePayloadOut",
        "AgentOtherDeviceIdIn": "_homegraph_34_AgentOtherDeviceIdIn",
        "AgentOtherDeviceIdOut": "_homegraph_35_AgentOtherDeviceIdOut",
        "QueryRequestInputIn": "_homegraph_36_QueryRequestInputIn",
        "QueryRequestInputOut": "_homegraph_37_QueryRequestInputOut",
        "QueryResponsePayloadIn": "_homegraph_38_QueryResponsePayloadIn",
        "QueryResponsePayloadOut": "_homegraph_39_QueryResponsePayloadOut",
        "ReportStateAndNotificationResponseIn": "_homegraph_40_ReportStateAndNotificationResponseIn",
        "ReportStateAndNotificationResponseOut": "_homegraph_41_ReportStateAndNotificationResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReportStateAndNotificationRequestIn"] = t.struct(
        {
            "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
            "agentUserId": t.string(),
            "eventId": t.string().optional(),
            "requestId": t.string().optional(),
            "followUpToken": t.string().optional(),
        }
    ).named(renames["ReportStateAndNotificationRequestIn"])
    types["ReportStateAndNotificationRequestOut"] = t.struct(
        {
            "payload": t.proxy(renames["StateAndNotificationPayloadOut"]),
            "agentUserId": t.string(),
            "eventId": t.string().optional(),
            "requestId": t.string().optional(),
            "followUpToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationRequestOut"])
    types["AgentDeviceIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["AgentDeviceIdIn"]
    )
    types["AgentDeviceIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentDeviceIdOut"])
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
    types["QueryResponseIn"] = t.struct(
        {
            "payload": t.proxy(renames["QueryResponsePayloadIn"]).optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "payload": t.proxy(renames["QueryResponsePayloadOut"]).optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["RequestSyncDevicesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestSyncDevicesResponseIn"])
    types["RequestSyncDevicesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestSyncDevicesResponseOut"])
    types["DeviceInfoIn"] = t.struct(
        {
            "model": t.string().optional(),
            "swVersion": t.string().optional(),
            "manufacturer": t.string().optional(),
            "hwVersion": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "model": t.string().optional(),
            "swVersion": t.string().optional(),
            "manufacturer": t.string().optional(),
            "hwVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "agentUserId": t.string(),
            "requestId": t.string().optional(),
            "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "agentUserId": t.string(),
            "requestId": t.string().optional(),
            "inputs": t.array(t.proxy(renames["QueryRequestInputOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
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
    types["DeviceNamesIn"] = t.struct(
        {
            "nicknames": t.array(t.string()).optional(),
            "defaultNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DeviceNamesIn"])
    types["DeviceNamesOut"] = t.struct(
        {
            "nicknames": t.array(t.string()).optional(),
            "defaultNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceNamesOut"])
    types["QueryRequestPayloadIn"] = t.struct(
        {"devices": t.array(t.proxy(renames["AgentDeviceIdIn"])).optional()}
    ).named(renames["QueryRequestPayloadIn"])
    types["QueryRequestPayloadOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["AgentDeviceIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestPayloadOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["DeviceIn"] = t.struct(
        {
            "structureHint": t.string().optional(),
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["DeviceNamesIn"]).optional(),
            "type": t.string().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoIn"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "traits": t.array(t.string()).optional(),
            "willReportState": t.boolean().optional(),
            "id": t.string().optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdIn"])
            ).optional(),
            "roomHint": t.string().optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "structureHint": t.string().optional(),
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "name": t.proxy(renames["DeviceNamesOut"]).optional(),
            "type": t.string().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoOut"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "traits": t.array(t.string()).optional(),
            "willReportState": t.boolean().optional(),
            "id": t.string().optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdOut"])
            ).optional(),
            "roomHint": t.string().optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
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
    types["QueryRequestInputIn"] = t.struct(
        {"payload": t.proxy(renames["QueryRequestPayloadIn"]).optional()}
    ).named(renames["QueryRequestInputIn"])
    types["QueryRequestInputOut"] = t.struct(
        {
            "payload": t.proxy(renames["QueryRequestPayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestInputOut"])
    types["QueryResponsePayloadIn"] = t.struct(
        {"devices": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["QueryResponsePayloadIn"])
    types["QueryResponsePayloadOut"] = t.struct(
        {
            "devices": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponsePayloadOut"])
    types["ReportStateAndNotificationResponseIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ReportStateAndNotificationResponseIn"])
    types["ReportStateAndNotificationResponseOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationResponseOut"])

    functions = {}
    functions["devicesSync"] = homegraph.post(
        "v1/devices:reportStateAndNotification",
        t.struct(
            {
                "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
                "agentUserId": t.string(),
                "eventId": t.string().optional(),
                "requestId": t.string().optional(),
                "followUpToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportStateAndNotificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesRequestSync"] = homegraph.post(
        "v1/devices:reportStateAndNotification",
        t.struct(
            {
                "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
                "agentUserId": t.string(),
                "eventId": t.string().optional(),
                "requestId": t.string().optional(),
                "followUpToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportStateAndNotificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesQuery"] = homegraph.post(
        "v1/devices:reportStateAndNotification",
        t.struct(
            {
                "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
                "agentUserId": t.string(),
                "eventId": t.string().optional(),
                "requestId": t.string().optional(),
                "followUpToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportStateAndNotificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesReportStateAndNotification"] = homegraph.post(
        "v1/devices:reportStateAndNotification",
        t.struct(
            {
                "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
                "agentUserId": t.string(),
                "eventId": t.string().optional(),
                "requestId": t.string().optional(),
                "followUpToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportStateAndNotificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["agentUsersDelete"] = homegraph.delete(
        "v1/{agentUserId}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "agentUserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="homegraph",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
