from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_homegraph() -> Import:
    homegraph = HTTPRuntime("https://homegraph.googleapis.com/")

    renames = {
        "ErrorResponse": "_homegraph_1_ErrorResponse",
        "QueryRequestInputIn": "_homegraph_2_QueryRequestInputIn",
        "QueryRequestInputOut": "_homegraph_3_QueryRequestInputOut",
        "SyncResponsePayloadIn": "_homegraph_4_SyncResponsePayloadIn",
        "SyncResponsePayloadOut": "_homegraph_5_SyncResponsePayloadOut",
        "AgentDeviceIdIn": "_homegraph_6_AgentDeviceIdIn",
        "AgentDeviceIdOut": "_homegraph_7_AgentDeviceIdOut",
        "ReportStateAndNotificationRequestIn": "_homegraph_8_ReportStateAndNotificationRequestIn",
        "ReportStateAndNotificationRequestOut": "_homegraph_9_ReportStateAndNotificationRequestOut",
        "RequestSyncDevicesRequestIn": "_homegraph_10_RequestSyncDevicesRequestIn",
        "RequestSyncDevicesRequestOut": "_homegraph_11_RequestSyncDevicesRequestOut",
        "ReportStateAndNotificationResponseIn": "_homegraph_12_ReportStateAndNotificationResponseIn",
        "ReportStateAndNotificationResponseOut": "_homegraph_13_ReportStateAndNotificationResponseOut",
        "SyncResponseIn": "_homegraph_14_SyncResponseIn",
        "SyncResponseOut": "_homegraph_15_SyncResponseOut",
        "QueryResponseIn": "_homegraph_16_QueryResponseIn",
        "QueryResponseOut": "_homegraph_17_QueryResponseOut",
        "StateAndNotificationPayloadIn": "_homegraph_18_StateAndNotificationPayloadIn",
        "StateAndNotificationPayloadOut": "_homegraph_19_StateAndNotificationPayloadOut",
        "DeviceNamesIn": "_homegraph_20_DeviceNamesIn",
        "DeviceNamesOut": "_homegraph_21_DeviceNamesOut",
        "SyncRequestIn": "_homegraph_22_SyncRequestIn",
        "SyncRequestOut": "_homegraph_23_SyncRequestOut",
        "AgentOtherDeviceIdIn": "_homegraph_24_AgentOtherDeviceIdIn",
        "AgentOtherDeviceIdOut": "_homegraph_25_AgentOtherDeviceIdOut",
        "QueryRequestPayloadIn": "_homegraph_26_QueryRequestPayloadIn",
        "QueryRequestPayloadOut": "_homegraph_27_QueryRequestPayloadOut",
        "QueryRequestIn": "_homegraph_28_QueryRequestIn",
        "QueryRequestOut": "_homegraph_29_QueryRequestOut",
        "QueryResponsePayloadIn": "_homegraph_30_QueryResponsePayloadIn",
        "QueryResponsePayloadOut": "_homegraph_31_QueryResponsePayloadOut",
        "DeviceIn": "_homegraph_32_DeviceIn",
        "DeviceOut": "_homegraph_33_DeviceOut",
        "EmptyIn": "_homegraph_34_EmptyIn",
        "EmptyOut": "_homegraph_35_EmptyOut",
        "RequestSyncDevicesResponseIn": "_homegraph_36_RequestSyncDevicesResponseIn",
        "RequestSyncDevicesResponseOut": "_homegraph_37_RequestSyncDevicesResponseOut",
        "DeviceInfoIn": "_homegraph_38_DeviceInfoIn",
        "DeviceInfoOut": "_homegraph_39_DeviceInfoOut",
        "ReportStateAndNotificationDeviceIn": "_homegraph_40_ReportStateAndNotificationDeviceIn",
        "ReportStateAndNotificationDeviceOut": "_homegraph_41_ReportStateAndNotificationDeviceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["QueryRequestInputIn"] = t.struct(
        {"payload": t.proxy(renames["QueryRequestPayloadIn"]).optional()}
    ).named(renames["QueryRequestInputIn"])
    types["QueryRequestInputOut"] = t.struct(
        {
            "payload": t.proxy(renames["QueryRequestPayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestInputOut"])
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
    types["AgentDeviceIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["AgentDeviceIdIn"]
    )
    types["AgentDeviceIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentDeviceIdOut"])
    types["ReportStateAndNotificationRequestIn"] = t.struct(
        {
            "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
            "followUpToken": t.string().optional(),
            "eventId": t.string().optional(),
            "agentUserId": t.string(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ReportStateAndNotificationRequestIn"])
    types["ReportStateAndNotificationRequestOut"] = t.struct(
        {
            "payload": t.proxy(renames["StateAndNotificationPayloadOut"]),
            "followUpToken": t.string().optional(),
            "eventId": t.string().optional(),
            "agentUserId": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationRequestOut"])
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
    types["ReportStateAndNotificationResponseIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ReportStateAndNotificationResponseIn"])
    types["ReportStateAndNotificationResponseOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationResponseOut"])
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
    types["DeviceNamesIn"] = t.struct(
        {
            "defaultNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "nicknames": t.array(t.string()).optional(),
        }
    ).named(renames["DeviceNamesIn"])
    types["DeviceNamesOut"] = t.struct(
        {
            "defaultNames": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "nicknames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceNamesOut"])
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
    types["AgentOtherDeviceIdIn"] = t.struct(
        {"deviceId": t.string().optional(), "agentId": t.string().optional()}
    ).named(renames["AgentOtherDeviceIdIn"])
    types["AgentOtherDeviceIdOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "agentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgentOtherDeviceIdOut"])
    types["QueryRequestPayloadIn"] = t.struct(
        {"devices": t.array(t.proxy(renames["AgentDeviceIdIn"])).optional()}
    ).named(renames["QueryRequestPayloadIn"])
    types["QueryRequestPayloadOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["AgentDeviceIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestPayloadOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
            "agentUserId": t.string(),
            "requestId": t.string().optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["QueryRequestInputOut"])),
            "agentUserId": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
    types["QueryResponsePayloadIn"] = t.struct(
        {"devices": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["QueryResponsePayloadIn"])
    types["QueryResponsePayloadOut"] = t.struct(
        {
            "devices": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponsePayloadOut"])
    types["DeviceIn"] = t.struct(
        {
            "structureHint": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoIn"]).optional(),
            "traits": t.array(t.string()).optional(),
            "willReportState": t.boolean().optional(),
            "id": t.string().optional(),
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
            "roomHint": t.string().optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdIn"])
            ).optional(),
            "name": t.proxy(renames["DeviceNamesIn"]).optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "structureHint": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoOut"]).optional(),
            "traits": t.array(t.string()).optional(),
            "willReportState": t.boolean().optional(),
            "id": t.string().optional(),
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
            "roomHint": t.string().optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdOut"])
            ).optional(),
            "name": t.proxy(renames["DeviceNamesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RequestSyncDevicesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestSyncDevicesResponseIn"])
    types["RequestSyncDevicesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestSyncDevicesResponseOut"])
    types["DeviceInfoIn"] = t.struct(
        {
            "model": t.string().optional(),
            "hwVersion": t.string().optional(),
            "swVersion": t.string().optional(),
            "manufacturer": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "model": t.string().optional(),
            "hwVersion": t.string().optional(),
            "swVersion": t.string().optional(),
            "manufacturer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
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
    functions["devicesQuery"] = homegraph.post(
        "v1/devices:sync",
        t.struct(
            {
                "agentUserId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SyncResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesRequestSync"] = homegraph.post(
        "v1/devices:sync",
        t.struct(
            {
                "agentUserId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SyncResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesReportStateAndNotification"] = homegraph.post(
        "v1/devices:sync",
        t.struct(
            {
                "agentUserId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SyncResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesSync"] = homegraph.post(
        "v1/devices:sync",
        t.struct(
            {
                "agentUserId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SyncResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="homegraph",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
