from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_eventarc() -> Import:
    eventarc = HTTPRuntime("https://eventarc.googleapis.com/")

    renames = {
        "ErrorResponse": "_eventarc_1_ErrorResponse",
        "ChannelConnectionIn": "_eventarc_2_ChannelConnectionIn",
        "ChannelConnectionOut": "_eventarc_3_ChannelConnectionOut",
        "TestIamPermissionsRequestIn": "_eventarc_4_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_eventarc_5_TestIamPermissionsRequestOut",
        "CloudRunIn": "_eventarc_6_CloudRunIn",
        "CloudRunOut": "_eventarc_7_CloudRunOut",
        "PolicyIn": "_eventarc_8_PolicyIn",
        "PolicyOut": "_eventarc_9_PolicyOut",
        "ExprIn": "_eventarc_10_ExprIn",
        "ExprOut": "_eventarc_11_ExprOut",
        "ListChannelsResponseIn": "_eventarc_12_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_eventarc_13_ListChannelsResponseOut",
        "FilteringAttributeIn": "_eventarc_14_FilteringAttributeIn",
        "FilteringAttributeOut": "_eventarc_15_FilteringAttributeOut",
        "GoogleRpcStatusIn": "_eventarc_16_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_eventarc_17_GoogleRpcStatusOut",
        "GoogleLongrunningListOperationsResponseIn": "_eventarc_18_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_eventarc_19_GoogleLongrunningListOperationsResponseOut",
        "ProviderIn": "_eventarc_20_ProviderIn",
        "ProviderOut": "_eventarc_21_ProviderOut",
        "ChannelIn": "_eventarc_22_ChannelIn",
        "ChannelOut": "_eventarc_23_ChannelOut",
        "EmptyIn": "_eventarc_24_EmptyIn",
        "EmptyOut": "_eventarc_25_EmptyOut",
        "GoogleLongrunningCancelOperationRequestIn": "_eventarc_26_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_eventarc_27_GoogleLongrunningCancelOperationRequestOut",
        "SetIamPolicyRequestIn": "_eventarc_28_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_eventarc_29_SetIamPolicyRequestOut",
        "PubsubIn": "_eventarc_30_PubsubIn",
        "PubsubOut": "_eventarc_31_PubsubOut",
        "EventFilterIn": "_eventarc_32_EventFilterIn",
        "EventFilterOut": "_eventarc_33_EventFilterOut",
        "ListProvidersResponseIn": "_eventarc_34_ListProvidersResponseIn",
        "ListProvidersResponseOut": "_eventarc_35_ListProvidersResponseOut",
        "TriggerIn": "_eventarc_36_TriggerIn",
        "TriggerOut": "_eventarc_37_TriggerOut",
        "DestinationIn": "_eventarc_38_DestinationIn",
        "DestinationOut": "_eventarc_39_DestinationOut",
        "LocationIn": "_eventarc_40_LocationIn",
        "LocationOut": "_eventarc_41_LocationOut",
        "AuditLogConfigIn": "_eventarc_42_AuditLogConfigIn",
        "AuditLogConfigOut": "_eventarc_43_AuditLogConfigOut",
        "TransportIn": "_eventarc_44_TransportIn",
        "TransportOut": "_eventarc_45_TransportOut",
        "EventTypeIn": "_eventarc_46_EventTypeIn",
        "EventTypeOut": "_eventarc_47_EventTypeOut",
        "BindingIn": "_eventarc_48_BindingIn",
        "BindingOut": "_eventarc_49_BindingOut",
        "GoogleChannelConfigIn": "_eventarc_50_GoogleChannelConfigIn",
        "GoogleChannelConfigOut": "_eventarc_51_GoogleChannelConfigOut",
        "ListTriggersResponseIn": "_eventarc_52_ListTriggersResponseIn",
        "ListTriggersResponseOut": "_eventarc_53_ListTriggersResponseOut",
        "ListChannelConnectionsResponseIn": "_eventarc_54_ListChannelConnectionsResponseIn",
        "ListChannelConnectionsResponseOut": "_eventarc_55_ListChannelConnectionsResponseOut",
        "StateConditionIn": "_eventarc_56_StateConditionIn",
        "StateConditionOut": "_eventarc_57_StateConditionOut",
        "OperationMetadataIn": "_eventarc_58_OperationMetadataIn",
        "OperationMetadataOut": "_eventarc_59_OperationMetadataOut",
        "TestIamPermissionsResponseIn": "_eventarc_60_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_eventarc_61_TestIamPermissionsResponseOut",
        "ListLocationsResponseIn": "_eventarc_62_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_eventarc_63_ListLocationsResponseOut",
        "GoogleLongrunningOperationIn": "_eventarc_64_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_eventarc_65_GoogleLongrunningOperationOut",
        "AuditConfigIn": "_eventarc_66_AuditConfigIn",
        "AuditConfigOut": "_eventarc_67_AuditConfigOut",
        "GKEIn": "_eventarc_68_GKEIn",
        "GKEOut": "_eventarc_69_GKEOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "channel": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelConnectionOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ListChannelsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListChannelsResponseIn"])
    types["ListChannelsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelsResponseOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["ProviderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProviderIn"]
    )
    types["ProviderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "eventTypes": t.array(t.proxy(renames["EventTypeOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProviderOut"])
    types["ChannelIn"] = t.struct(
        {
            "cryptoKeyName": t.string().optional(),
            "name": t.string(),
            "provider": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "cryptoKeyName": t.string().optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "provider": t.string().optional(),
            "activationToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["EventFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "attribute": t.string(),
            "value": t.string(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "attribute": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
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
    types["TriggerIn"] = t.struct(
        {
            "transport": t.proxy(renames["TransportIn"]).optional(),
            "name": t.string(),
            "channel": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "eventDataContentType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])),
            "destination": t.proxy(renames["DestinationIn"]),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "transport": t.proxy(renames["TransportOut"]).optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "channel": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "eventDataContentType": t.string().optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "conditions": t.struct({"_": t.string().optional()}).optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])),
            "destination": t.proxy(renames["DestinationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["DestinationIn"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
            "gke": t.proxy(renames["GKEIn"]).optional(),
            "cloudFunction": t.string().optional(),
            "workflow": t.string().optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "gke": t.proxy(renames["GKEOut"]).optional(),
            "cloudFunction": t.string().optional(),
            "workflow": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["TransportIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubsubIn"]).optional()}
    ).named(renames["TransportIn"])
    types["TransportOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubsubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportOut"])
    types["EventTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EventTypeIn"]
    )
    types["EventTypeOut"] = t.struct(
        {
            "eventSchemaUri": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "filteringAttributes": t.array(
                t.proxy(renames["FilteringAttributeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTypeOut"])
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
    types["GoogleChannelConfigIn"] = t.struct(
        {"cryptoKeyName": t.string().optional(), "name": t.string()}
    ).named(renames["GoogleChannelConfigIn"])
    types["GoogleChannelConfigOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChannelConfigOut"])
    types["ListTriggersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "triggers": t.array(t.proxy(renames["TriggerIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListTriggersResponseIn"])
    types["ListTriggersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "triggers": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTriggersResponseOut"])
    types["ListChannelConnectionsResponseIn"] = t.struct(
        {
            "channelConnections": t.array(
                t.proxy(renames["ChannelConnectionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListChannelConnectionsResponseIn"])
    types["ListChannelConnectionsResponseOut"] = t.struct(
        {
            "channelConnections": t.array(
                t.proxy(renames["ChannelConnectionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChannelConnectionsResponseOut"])
    types["StateConditionIn"] = t.struct(
        {"message": t.string().optional(), "code": t.string().optional()}
    ).named(renames["StateConditionIn"])
    types["StateConditionOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateConditionOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["GKEIn"] = t.struct(
        {
            "location": t.string(),
            "service": t.string(),
            "cluster": t.string(),
            "namespace": t.string(),
            "path": t.string().optional(),
        }
    ).named(renames["GKEIn"])
    types["GKEOut"] = t.struct(
        {
            "location": t.string(),
            "service": t.string(),
            "cluster": t.string(),
            "namespace": t.string(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GKEOut"])

    functions = {}
    functions["projectsLocationsGet"] = eventarc.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateGoogleChannelConfig"] = eventarc.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetGoogleChannelConfig"] = eventarc.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = eventarc.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsChannelConnectionsCreate"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsList"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsSetIamPolicy"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsDelete"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsGetIamPolicy"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsTestIamPermissions"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelConnectionsGet"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = eventarc.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersCreate"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersPatch"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersSetIamPolicy"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGet"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersDelete"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersList"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGetIamPolicy"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersTestIamPermissions"] = eventarc.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsGetIamPolicy"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsSetIamPolicy"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsGet"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsPatch"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsTestIamPermissions"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsCreate"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsDelete"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsList"] = eventarc.get(
        "v1/{parent}/channels",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListChannelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="eventarc", renames=renames, types=types, functions=functions
    )
