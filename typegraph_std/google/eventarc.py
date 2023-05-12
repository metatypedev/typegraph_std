from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_eventarc() -> Import:
    eventarc = HTTPRuntime("https://eventarc.googleapis.com/")

    renames = {
        "ErrorResponse": "_eventarc_1_ErrorResponse",
        "GoogleRpcStatusIn": "_eventarc_2_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_eventarc_3_GoogleRpcStatusOut",
        "GoogleLongrunningOperationIn": "_eventarc_4_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_eventarc_5_GoogleLongrunningOperationOut",
        "TriggerIn": "_eventarc_6_TriggerIn",
        "TriggerOut": "_eventarc_7_TriggerOut",
        "TestIamPermissionsResponseIn": "_eventarc_8_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_eventarc_9_TestIamPermissionsResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_eventarc_10_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_eventarc_11_GoogleLongrunningListOperationsResponseOut",
        "LocationIn": "_eventarc_12_LocationIn",
        "LocationOut": "_eventarc_13_LocationOut",
        "ProviderIn": "_eventarc_14_ProviderIn",
        "ProviderOut": "_eventarc_15_ProviderOut",
        "PolicyIn": "_eventarc_16_PolicyIn",
        "PolicyOut": "_eventarc_17_PolicyOut",
        "ListChannelsResponseIn": "_eventarc_18_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_eventarc_19_ListChannelsResponseOut",
        "ChannelIn": "_eventarc_20_ChannelIn",
        "ChannelOut": "_eventarc_21_ChannelOut",
        "CloudRunIn": "_eventarc_22_CloudRunIn",
        "CloudRunOut": "_eventarc_23_CloudRunOut",
        "DestinationIn": "_eventarc_24_DestinationIn",
        "DestinationOut": "_eventarc_25_DestinationOut",
        "GoogleChannelConfigIn": "_eventarc_26_GoogleChannelConfigIn",
        "GoogleChannelConfigOut": "_eventarc_27_GoogleChannelConfigOut",
        "PubsubIn": "_eventarc_28_PubsubIn",
        "PubsubOut": "_eventarc_29_PubsubOut",
        "AuditConfigIn": "_eventarc_30_AuditConfigIn",
        "AuditConfigOut": "_eventarc_31_AuditConfigOut",
        "StateConditionIn": "_eventarc_32_StateConditionIn",
        "StateConditionOut": "_eventarc_33_StateConditionOut",
        "SetIamPolicyRequestIn": "_eventarc_34_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_eventarc_35_SetIamPolicyRequestOut",
        "OperationMetadataIn": "_eventarc_36_OperationMetadataIn",
        "OperationMetadataOut": "_eventarc_37_OperationMetadataOut",
        "AuditLogConfigIn": "_eventarc_38_AuditLogConfigIn",
        "AuditLogConfigOut": "_eventarc_39_AuditLogConfigOut",
        "ListLocationsResponseIn": "_eventarc_40_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_eventarc_41_ListLocationsResponseOut",
        "ChannelConnectionIn": "_eventarc_42_ChannelConnectionIn",
        "ChannelConnectionOut": "_eventarc_43_ChannelConnectionOut",
        "FilteringAttributeIn": "_eventarc_44_FilteringAttributeIn",
        "FilteringAttributeOut": "_eventarc_45_FilteringAttributeOut",
        "TestIamPermissionsRequestIn": "_eventarc_46_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_eventarc_47_TestIamPermissionsRequestOut",
        "GoogleLongrunningCancelOperationRequestIn": "_eventarc_48_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_eventarc_49_GoogleLongrunningCancelOperationRequestOut",
        "GKEIn": "_eventarc_50_GKEIn",
        "GKEOut": "_eventarc_51_GKEOut",
        "ListTriggersResponseIn": "_eventarc_52_ListTriggersResponseIn",
        "ListTriggersResponseOut": "_eventarc_53_ListTriggersResponseOut",
        "BindingIn": "_eventarc_54_BindingIn",
        "BindingOut": "_eventarc_55_BindingOut",
        "EventTypeIn": "_eventarc_56_EventTypeIn",
        "EventTypeOut": "_eventarc_57_EventTypeOut",
        "EventFilterIn": "_eventarc_58_EventFilterIn",
        "EventFilterOut": "_eventarc_59_EventFilterOut",
        "EmptyIn": "_eventarc_60_EmptyIn",
        "EmptyOut": "_eventarc_61_EmptyOut",
        "ExprIn": "_eventarc_62_ExprIn",
        "ExprOut": "_eventarc_63_ExprOut",
        "TransportIn": "_eventarc_64_TransportIn",
        "TransportOut": "_eventarc_65_TransportOut",
        "ListProvidersResponseIn": "_eventarc_66_ListProvidersResponseIn",
        "ListProvidersResponseOut": "_eventarc_67_ListProvidersResponseOut",
        "ListChannelConnectionsResponseIn": "_eventarc_68_ListChannelConnectionsResponseIn",
        "ListChannelConnectionsResponseOut": "_eventarc_69_ListChannelConnectionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["TriggerIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "eventDataContentType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "destination": t.proxy(renames["DestinationIn"]),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "transport": t.proxy(renames["TransportIn"]).optional(),
            "name": t.string(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "conditions": t.struct({"_": t.string().optional()}).optional(),
            "channel": t.string().optional(),
            "eventDataContentType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "destination": t.proxy(renames["DestinationOut"]),
            "updateTime": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "transport": t.proxy(renames["TransportOut"]).optional(),
            "name": t.string(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ProviderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProviderIn"]
    )
    types["ProviderOut"] = t.struct(
        {
            "eventTypes": t.array(t.proxy(renames["EventTypeOut"])).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProviderOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListChannelsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
        }
    ).named(renames["ListChannelsResponseIn"])
    types["ListChannelsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelsResponseOut"])
    types["ChannelIn"] = t.struct(
        {
            "provider": t.string().optional(),
            "name": t.string(),
            "cryptoKeyName": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "provider": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "uid": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "activationToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["CloudRunIn"] = t.struct(
        {"path": t.string().optional(), "service": t.string(), "region": t.string()}
    ).named(renames["CloudRunIn"])
    types["CloudRunOut"] = t.struct(
        {
            "path": t.string().optional(),
            "service": t.string(),
            "region": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunOut"])
    types["DestinationIn"] = t.struct(
        {
            "workflow": t.string().optional(),
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
            "cloudFunction": t.string().optional(),
            "gke": t.proxy(renames["GKEIn"]).optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "workflow": t.string().optional(),
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "cloudFunction": t.string().optional(),
            "gke": t.proxy(renames["GKEOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
    types["GoogleChannelConfigIn"] = t.struct(
        {"cryptoKeyName": t.string().optional(), "name": t.string()}
    ).named(renames["GoogleChannelConfigIn"])
    types["GoogleChannelConfigOut"] = t.struct(
        {
            "cryptoKeyName": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChannelConfigOut"])
    types["PubsubIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubsubIn"]
    )
    types["PubsubOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "subscription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["StateConditionIn"] = t.struct(
        {"code": t.string().optional(), "message": t.string().optional()}
    ).named(renames["StateConditionIn"])
    types["StateConditionOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateConditionOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["ChannelConnectionIn"] = t.struct(
        {
            "channel": t.string(),
            "activationToken": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["ChannelConnectionIn"])
    types["ChannelConnectionOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "channel": t.string(),
            "createTime": t.string().optional(),
            "activationToken": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelConnectionOut"])
    types["FilteringAttributeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilteringAttributeIn"]
    )
    types["FilteringAttributeOut"] = t.struct(
        {
            "attribute": t.string().optional(),
            "required": t.boolean().optional(),
            "pathPatternSupported": t.boolean().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteringAttributeOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GKEIn"] = t.struct(
        {
            "service": t.string(),
            "namespace": t.string(),
            "cluster": t.string(),
            "location": t.string(),
            "path": t.string().optional(),
        }
    ).named(renames["GKEIn"])
    types["GKEOut"] = t.struct(
        {
            "service": t.string(),
            "namespace": t.string(),
            "cluster": t.string(),
            "location": t.string(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GKEOut"])
    types["ListTriggersResponseIn"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListTriggersResponseIn"])
    types["ListTriggersResponseOut"] = t.struct(
        {
            "triggers": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTriggersResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["EventTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EventTypeIn"]
    )
    types["EventTypeOut"] = t.struct(
        {
            "type": t.string().optional(),
            "eventSchemaUri": t.string().optional(),
            "filteringAttributes": t.array(
                t.proxy(renames["FilteringAttributeOut"])
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTypeOut"])
    types["EventFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "value": t.string(),
            "attribute": t.string(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "value": t.string(),
            "attribute": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TransportIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubsubIn"]).optional()}
    ).named(renames["TransportIn"])
    types["TransportOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubsubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportOut"])
    types["ListProvidersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "providers": t.array(t.proxy(renames["ProviderIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProvidersResponseIn"])
    types["ListProvidersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "providers": t.array(t.proxy(renames["ProviderOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProvidersResponseOut"])
    types["ListChannelConnectionsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "channelConnections": t.array(
                t.proxy(renames["ChannelConnectionIn"])
            ).optional(),
        }
    ).named(renames["ListChannelConnectionsResponseIn"])
    types["ListChannelConnectionsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "channelConnections": t.array(
                t.proxy(renames["ChannelConnectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelConnectionsResponseOut"])

    functions = {}
    functions["projectsLocationsList"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateGoogleChannelConfig"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetGoogleChannelConfig"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvidersGet"] = eventarc.get(
        "v1/{parent}/providers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvidersList"] = eventarc.get(
        "v1/{parent}/providers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsCreate"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsGetIamPolicy"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsSetIamPolicy"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsTestIamPermissions"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsGet"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsDelete"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsList"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsPatch"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "provider": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsCreate"] = eventarc.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsDelete"] = eventarc.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsGet"] = eventarc.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsList"] = eventarc.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsSetIamPolicy"] = eventarc.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsTestIamPermissions"] = eventarc.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsGetIamPolicy"] = eventarc.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = eventarc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = eventarc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = eventarc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = eventarc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersList"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersPatch"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGetIamPolicy"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersSetIamPolicy"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGet"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersCreate"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersTestIamPermissions"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersDelete"] = eventarc.delete(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="eventarc", renames=renames, types=Box(types), functions=Box(functions)
    )
