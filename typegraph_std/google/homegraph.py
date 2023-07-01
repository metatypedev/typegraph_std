from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_homegraph():
    homegraph = HTTPRuntime("https://homegraph.googleapis.com/")

    renames = {
        "ErrorResponse": "_homegraph_1_ErrorResponse",
        "RequestSyncDevicesResponseIn": "_homegraph_2_RequestSyncDevicesResponseIn",
        "RequestSyncDevicesResponseOut": "_homegraph_3_RequestSyncDevicesResponseOut",
        "SyncRequestIn": "_homegraph_4_SyncRequestIn",
        "SyncRequestOut": "_homegraph_5_SyncRequestOut",
        "SyncResponseIn": "_homegraph_6_SyncResponseIn",
        "SyncResponseOut": "_homegraph_7_SyncResponseOut",
        "QueryRequestPayloadIn": "_homegraph_8_QueryRequestPayloadIn",
        "QueryRequestPayloadOut": "_homegraph_9_QueryRequestPayloadOut",
        "QueryRequestInputIn": "_homegraph_10_QueryRequestInputIn",
        "QueryRequestInputOut": "_homegraph_11_QueryRequestInputOut",
        "ReportStateAndNotificationResponseIn": "_homegraph_12_ReportStateAndNotificationResponseIn",
        "ReportStateAndNotificationResponseOut": "_homegraph_13_ReportStateAndNotificationResponseOut",
        "SyncResponsePayloadIn": "_homegraph_14_SyncResponsePayloadIn",
        "SyncResponsePayloadOut": "_homegraph_15_SyncResponsePayloadOut",
        "QueryRequestIn": "_homegraph_16_QueryRequestIn",
        "QueryRequestOut": "_homegraph_17_QueryRequestOut",
        "RequestSyncDevicesRequestIn": "_homegraph_18_RequestSyncDevicesRequestIn",
        "RequestSyncDevicesRequestOut": "_homegraph_19_RequestSyncDevicesRequestOut",
        "ReportStateAndNotificationRequestIn": "_homegraph_20_ReportStateAndNotificationRequestIn",
        "ReportStateAndNotificationRequestOut": "_homegraph_21_ReportStateAndNotificationRequestOut",
        "DeviceNamesIn": "_homegraph_22_DeviceNamesIn",
        "DeviceNamesOut": "_homegraph_23_DeviceNamesOut",
        "DeviceIn": "_homegraph_24_DeviceIn",
        "DeviceOut": "_homegraph_25_DeviceOut",
        "DeviceInfoIn": "_homegraph_26_DeviceInfoIn",
        "DeviceInfoOut": "_homegraph_27_DeviceInfoOut",
        "ReportStateAndNotificationDeviceIn": "_homegraph_28_ReportStateAndNotificationDeviceIn",
        "ReportStateAndNotificationDeviceOut": "_homegraph_29_ReportStateAndNotificationDeviceOut",
        "EmptyIn": "_homegraph_30_EmptyIn",
        "EmptyOut": "_homegraph_31_EmptyOut",
        "AgentOtherDeviceIdIn": "_homegraph_32_AgentOtherDeviceIdIn",
        "AgentOtherDeviceIdOut": "_homegraph_33_AgentOtherDeviceIdOut",
        "QueryResponseIn": "_homegraph_34_QueryResponseIn",
        "QueryResponseOut": "_homegraph_35_QueryResponseOut",
        "QueryResponsePayloadIn": "_homegraph_36_QueryResponsePayloadIn",
        "QueryResponsePayloadOut": "_homegraph_37_QueryResponsePayloadOut",
        "AgentDeviceIdIn": "_homegraph_38_AgentDeviceIdIn",
        "AgentDeviceIdOut": "_homegraph_39_AgentDeviceIdOut",
        "StateAndNotificationPayloadIn": "_homegraph_40_StateAndNotificationPayloadIn",
        "StateAndNotificationPayloadOut": "_homegraph_41_StateAndNotificationPayloadOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RequestSyncDevicesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RequestSyncDevicesResponseIn"])
    types["RequestSyncDevicesResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RequestSyncDevicesResponseOut"])
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
    types["SyncResponseIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "payload": t.proxy(renames["SyncResponsePayloadIn"]).optional(),
        }
    ).named(renames["SyncResponseIn"])
    types["SyncResponseOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "payload": t.proxy(renames["SyncResponsePayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncResponseOut"])
    types["QueryRequestPayloadIn"] = t.struct(
        {"devices": t.array(t.proxy(renames["AgentDeviceIdIn"])).optional()}
    ).named(renames["QueryRequestPayloadIn"])
    types["QueryRequestPayloadOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["AgentDeviceIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestPayloadOut"])
    types["QueryRequestInputIn"] = t.struct(
        {"payload": t.proxy(renames["QueryRequestPayloadIn"]).optional()}
    ).named(renames["QueryRequestInputIn"])
    types["QueryRequestInputOut"] = t.struct(
        {
            "payload": t.proxy(renames["QueryRequestPayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestInputOut"])
    types["ReportStateAndNotificationResponseIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["ReportStateAndNotificationResponseIn"])
    types["ReportStateAndNotificationResponseOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationResponseOut"])
    types["SyncResponsePayloadIn"] = t.struct(
        {
            "agentUserId": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
        }
    ).named(renames["SyncResponsePayloadIn"])
    types["SyncResponsePayloadOut"] = t.struct(
        {
            "agentUserId": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncResponsePayloadOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["QueryRequestInputIn"])),
            "requestId": t.string().optional(),
            "agentUserId": t.string(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "inputs": t.array(t.proxy(renames["QueryRequestInputOut"])),
            "requestId": t.string().optional(),
            "agentUserId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
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
    types["ReportStateAndNotificationRequestIn"] = t.struct(
        {
            "agentUserId": t.string(),
            "payload": t.proxy(renames["StateAndNotificationPayloadIn"]),
            "followUpToken": t.string().optional(),
            "eventId": t.string().optional(),
            "requestId": t.string().optional(),
        }
    ).named(renames["ReportStateAndNotificationRequestIn"])
    types["ReportStateAndNotificationRequestOut"] = t.struct(
        {
            "agentUserId": t.string(),
            "payload": t.proxy(renames["StateAndNotificationPayloadOut"]),
            "followUpToken": t.string().optional(),
            "eventId": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStateAndNotificationRequestOut"])
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
    types["DeviceIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "willReportState": t.boolean().optional(),
            "roomHint": t.string().optional(),
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoIn"]).optional(),
            "structureHint": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "traits": t.array(t.string()).optional(),
            "name": t.proxy(renames["DeviceNamesIn"]).optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdIn"])
            ).optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "willReportState": t.boolean().optional(),
            "roomHint": t.string().optional(),
            "customData": t.struct({"_": t.string().optional()}).optional(),
            "notificationSupportedByAgent": t.boolean().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoOut"]).optional(),
            "structureHint": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "traits": t.array(t.string()).optional(),
            "name": t.proxy(renames["DeviceNamesOut"]).optional(),
            "otherDeviceIds": t.array(
                t.proxy(renames["AgentOtherDeviceIdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["DeviceInfoIn"] = t.struct(
        {
            "hwVersion": t.string().optional(),
            "swVersion": t.string().optional(),
            "model": t.string().optional(),
            "manufacturer": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "hwVersion": t.string().optional(),
            "swVersion": t.string().optional(),
            "model": t.string().optional(),
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["QueryResponsePayloadIn"] = t.struct(
        {"devices": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["QueryResponsePayloadIn"])
    types["QueryResponsePayloadOut"] = t.struct(
        {
            "devices": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponsePayloadOut"])
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

    functions = {}
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
    functions["devicesQuery"] = homegraph.post(
        "v1/devices:requestSync",
        t.struct(
            {
                "async": t.boolean().optional(),
                "agentUserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RequestSyncDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesReportStateAndNotification"] = homegraph.post(
        "v1/devices:requestSync",
        t.struct(
            {
                "async": t.boolean().optional(),
                "agentUserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RequestSyncDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesSync"] = homegraph.post(
        "v1/devices:requestSync",
        t.struct(
            {
                "async": t.boolean().optional(),
                "agentUserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RequestSyncDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesRequestSync"] = homegraph.post(
        "v1/devices:requestSync",
        t.struct(
            {
                "async": t.boolean().optional(),
                "agentUserId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RequestSyncDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="homegraph",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
