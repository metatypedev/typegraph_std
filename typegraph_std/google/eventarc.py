from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_eventarc() -> Import:
    eventarc = HTTPRuntime("https://eventarc.googleapis.com/")

    renames = {
        "ErrorResponse": "_eventarc_1_ErrorResponse",
        "StateConditionIn": "_eventarc_2_StateConditionIn",
        "StateConditionOut": "_eventarc_3_StateConditionOut",
        "EmptyIn": "_eventarc_4_EmptyIn",
        "EmptyOut": "_eventarc_5_EmptyOut",
        "TestIamPermissionsRequestIn": "_eventarc_6_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_eventarc_7_TestIamPermissionsRequestOut",
        "GoogleLongrunningOperationIn": "_eventarc_8_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_eventarc_9_GoogleLongrunningOperationOut",
        "EventTypeIn": "_eventarc_10_EventTypeIn",
        "EventTypeOut": "_eventarc_11_EventTypeOut",
        "ListChannelsResponseIn": "_eventarc_12_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_eventarc_13_ListChannelsResponseOut",
        "DestinationIn": "_eventarc_14_DestinationIn",
        "DestinationOut": "_eventarc_15_DestinationOut",
        "ListChannelConnectionsResponseIn": "_eventarc_16_ListChannelConnectionsResponseIn",
        "ListChannelConnectionsResponseOut": "_eventarc_17_ListChannelConnectionsResponseOut",
        "ProviderIn": "_eventarc_18_ProviderIn",
        "ProviderOut": "_eventarc_19_ProviderOut",
        "TriggerIn": "_eventarc_20_TriggerIn",
        "TriggerOut": "_eventarc_21_TriggerOut",
        "OperationMetadataIn": "_eventarc_22_OperationMetadataIn",
        "OperationMetadataOut": "_eventarc_23_OperationMetadataOut",
        "GKEIn": "_eventarc_24_GKEIn",
        "GKEOut": "_eventarc_25_GKEOut",
        "AuditConfigIn": "_eventarc_26_AuditConfigIn",
        "AuditConfigOut": "_eventarc_27_AuditConfigOut",
        "PubsubIn": "_eventarc_28_PubsubIn",
        "PubsubOut": "_eventarc_29_PubsubOut",
        "ListLocationsResponseIn": "_eventarc_30_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_eventarc_31_ListLocationsResponseOut",
        "BindingIn": "_eventarc_32_BindingIn",
        "BindingOut": "_eventarc_33_BindingOut",
        "ChannelConnectionIn": "_eventarc_34_ChannelConnectionIn",
        "ChannelConnectionOut": "_eventarc_35_ChannelConnectionOut",
        "PolicyIn": "_eventarc_36_PolicyIn",
        "PolicyOut": "_eventarc_37_PolicyOut",
        "TransportIn": "_eventarc_38_TransportIn",
        "TransportOut": "_eventarc_39_TransportOut",
        "FilteringAttributeIn": "_eventarc_40_FilteringAttributeIn",
        "FilteringAttributeOut": "_eventarc_41_FilteringAttributeOut",
        "EventFilterIn": "_eventarc_42_EventFilterIn",
        "EventFilterOut": "_eventarc_43_EventFilterOut",
        "SetIamPolicyRequestIn": "_eventarc_44_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_eventarc_45_SetIamPolicyRequestOut",
        "ExprIn": "_eventarc_46_ExprIn",
        "ExprOut": "_eventarc_47_ExprOut",
        "CloudRunIn": "_eventarc_48_CloudRunIn",
        "CloudRunOut": "_eventarc_49_CloudRunOut",
        "GoogleChannelConfigIn": "_eventarc_50_GoogleChannelConfigIn",
        "GoogleChannelConfigOut": "_eventarc_51_GoogleChannelConfigOut",
        "ListProvidersResponseIn": "_eventarc_52_ListProvidersResponseIn",
        "ListProvidersResponseOut": "_eventarc_53_ListProvidersResponseOut",
        "TestIamPermissionsResponseIn": "_eventarc_54_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_eventarc_55_TestIamPermissionsResponseOut",
        "ListTriggersResponseIn": "_eventarc_56_ListTriggersResponseIn",
        "ListTriggersResponseOut": "_eventarc_57_ListTriggersResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_eventarc_58_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_eventarc_59_GoogleLongrunningListOperationsResponseOut",
        "ChannelIn": "_eventarc_60_ChannelIn",
        "ChannelOut": "_eventarc_61_ChannelOut",
        "AuditLogConfigIn": "_eventarc_62_AuditLogConfigIn",
        "AuditLogConfigOut": "_eventarc_63_AuditLogConfigOut",
        "LocationIn": "_eventarc_64_LocationIn",
        "LocationOut": "_eventarc_65_LocationOut",
        "GoogleRpcStatusIn": "_eventarc_66_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_eventarc_67_GoogleRpcStatusOut",
        "GoogleLongrunningCancelOperationRequestIn": "_eventarc_68_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_eventarc_69_GoogleLongrunningCancelOperationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["EventTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EventTypeIn"]
    )
    types["EventTypeOut"] = t.struct(
        {
            "description": t.string().optional(),
            "eventSchemaUri": t.string().optional(),
            "type": t.string().optional(),
            "filteringAttributes": t.array(
                t.proxy(renames["FilteringAttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTypeOut"])
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
    types["DestinationIn"] = t.struct(
        {
            "cloudFunction": t.string().optional(),
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
            "gke": t.proxy(renames["GKEIn"]).optional(),
            "workflow": t.string().optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "cloudFunction": t.string().optional(),
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "gke": t.proxy(renames["GKEOut"]).optional(),
            "workflow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
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
    types["ProviderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProviderIn"]
    )
    types["ProviderOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "eventTypes": t.array(t.proxy(renames["EventTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProviderOut"])
    types["TriggerIn"] = t.struct(
        {
            "transport": t.proxy(renames["TransportIn"]).optional(),
            "channel": t.string().optional(),
            "destination": t.proxy(renames["DestinationIn"]),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "eventDataContentType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "transport": t.proxy(renames["TransportOut"]).optional(),
            "channel": t.string().optional(),
            "conditions": t.struct({"_": t.string().optional()}).optional(),
            "destination": t.proxy(renames["DestinationOut"]),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "eventDataContentType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GKEIn"] = t.struct(
        {
            "location": t.string(),
            "path": t.string().optional(),
            "cluster": t.string(),
            "service": t.string(),
            "namespace": t.string(),
        }
    ).named(renames["GKEIn"])
    types["GKEOut"] = t.struct(
        {
            "location": t.string(),
            "path": t.string().optional(),
            "cluster": t.string(),
            "service": t.string(),
            "namespace": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GKEOut"])
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
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ChannelConnectionIn"] = t.struct(
        {
            "activationToken": t.string().optional(),
            "channel": t.string(),
            "name": t.string(),
        }
    ).named(renames["ChannelConnectionIn"])
    types["ChannelConnectionOut"] = t.struct(
        {
            "activationToken": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "channel": t.string(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelConnectionOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TransportIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubsubIn"]).optional()}
    ).named(renames["TransportIn"])
    types["TransportOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubsubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportOut"])
    types["FilteringAttributeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilteringAttributeIn"]
    )
    types["FilteringAttributeOut"] = t.struct(
        {
            "required": t.boolean().optional(),
            "pathPatternSupported": t.boolean().optional(),
            "attribute": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteringAttributeOut"])
    types["EventFilterIn"] = t.struct(
        {
            "attribute": t.string(),
            "value": t.string(),
            "operator": t.string().optional(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "attribute": t.string(),
            "value": t.string(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["CloudRunIn"] = t.struct(
        {"region": t.string(), "service": t.string(), "path": t.string().optional()}
    ).named(renames["CloudRunIn"])
    types["CloudRunOut"] = t.struct(
        {
            "region": t.string(),
            "service": t.string(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunOut"])
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
    types["ListProvidersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "providers": t.array(t.proxy(renames["ProviderIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListProvidersResponseIn"])
    types["ListProvidersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "providers": t.array(t.proxy(renames["ProviderOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProvidersResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListTriggersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "triggers": t.array(t.proxy(renames["TriggerIn"])).optional(),
        }
    ).named(renames["ListTriggersResponseIn"])
    types["ListTriggersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "triggers": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTriggersResponseOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["ChannelIn"] = t.struct(
        {
            "cryptoKeyName": t.string().optional(),
            "name": t.string(),
            "provider": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "state": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "name": t.string(),
            "activationToken": t.string().optional(),
            "provider": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])

    functions = {}
    functions["projectsLocationsUpdateGoogleChannelConfig"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChannelConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChannelConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChannelConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetGoogleChannelConfig"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChannelConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvidersList"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProviderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvidersGet"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProviderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = eventarc.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = eventarc.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = eventarc.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = eventarc.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersPatch"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersList"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersSetIamPolicy"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersDelete"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersCreate"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersTestIamPermissions"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGetIamPolicy"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGet"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsSetIamPolicy"] = eventarc.get(
        "v1/{parent}/channelConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsGet"] = eventarc.get(
        "v1/{parent}/channelConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsGetIamPolicy"] = eventarc.get(
        "v1/{parent}/channelConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsCreate"] = eventarc.get(
        "v1/{parent}/channelConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsTestIamPermissions"] = eventarc.get(
        "v1/{parent}/channelConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsDelete"] = eventarc.get(
        "v1/{parent}/channelConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsList"] = eventarc.get(
        "v1/{parent}/channelConnections",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsSetIamPolicy"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsCreate"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
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
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "provider": t.string().optional(),
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
