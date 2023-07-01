from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_eventarc():
    eventarc = HTTPRuntime("https://eventarc.googleapis.com/")

    renames = {
        "ErrorResponse": "_eventarc_1_ErrorResponse",
        "EmptyIn": "_eventarc_2_EmptyIn",
        "EmptyOut": "_eventarc_3_EmptyOut",
        "LocationIn": "_eventarc_4_LocationIn",
        "LocationOut": "_eventarc_5_LocationOut",
        "GoogleLongrunningOperationIn": "_eventarc_6_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_eventarc_7_GoogleLongrunningOperationOut",
        "GoogleLongrunningListOperationsResponseIn": "_eventarc_8_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_eventarc_9_GoogleLongrunningListOperationsResponseOut",
        "CloudRunIn": "_eventarc_10_CloudRunIn",
        "CloudRunOut": "_eventarc_11_CloudRunOut",
        "ExprIn": "_eventarc_12_ExprIn",
        "ExprOut": "_eventarc_13_ExprOut",
        "FilteringAttributeIn": "_eventarc_14_FilteringAttributeIn",
        "FilteringAttributeOut": "_eventarc_15_FilteringAttributeOut",
        "AuditConfigIn": "_eventarc_16_AuditConfigIn",
        "AuditConfigOut": "_eventarc_17_AuditConfigOut",
        "GoogleLongrunningCancelOperationRequestIn": "_eventarc_18_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_eventarc_19_GoogleLongrunningCancelOperationRequestOut",
        "GoogleChannelConfigIn": "_eventarc_20_GoogleChannelConfigIn",
        "GoogleChannelConfigOut": "_eventarc_21_GoogleChannelConfigOut",
        "TestIamPermissionsResponseIn": "_eventarc_22_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_eventarc_23_TestIamPermissionsResponseOut",
        "StateConditionIn": "_eventarc_24_StateConditionIn",
        "StateConditionOut": "_eventarc_25_StateConditionOut",
        "SetIamPolicyRequestIn": "_eventarc_26_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_eventarc_27_SetIamPolicyRequestOut",
        "ListTriggersResponseIn": "_eventarc_28_ListTriggersResponseIn",
        "ListTriggersResponseOut": "_eventarc_29_ListTriggersResponseOut",
        "OperationMetadataIn": "_eventarc_30_OperationMetadataIn",
        "OperationMetadataOut": "_eventarc_31_OperationMetadataOut",
        "EventTypeIn": "_eventarc_32_EventTypeIn",
        "EventTypeOut": "_eventarc_33_EventTypeOut",
        "PubsubIn": "_eventarc_34_PubsubIn",
        "PubsubOut": "_eventarc_35_PubsubOut",
        "ProviderIn": "_eventarc_36_ProviderIn",
        "ProviderOut": "_eventarc_37_ProviderOut",
        "AuditLogConfigIn": "_eventarc_38_AuditLogConfigIn",
        "AuditLogConfigOut": "_eventarc_39_AuditLogConfigOut",
        "TransportIn": "_eventarc_40_TransportIn",
        "TransportOut": "_eventarc_41_TransportOut",
        "DestinationIn": "_eventarc_42_DestinationIn",
        "DestinationOut": "_eventarc_43_DestinationOut",
        "ListChannelConnectionsResponseIn": "_eventarc_44_ListChannelConnectionsResponseIn",
        "ListChannelConnectionsResponseOut": "_eventarc_45_ListChannelConnectionsResponseOut",
        "GoogleRpcStatusIn": "_eventarc_46_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_eventarc_47_GoogleRpcStatusOut",
        "ListChannelsResponseIn": "_eventarc_48_ListChannelsResponseIn",
        "ListChannelsResponseOut": "_eventarc_49_ListChannelsResponseOut",
        "PolicyIn": "_eventarc_50_PolicyIn",
        "PolicyOut": "_eventarc_51_PolicyOut",
        "TestIamPermissionsRequestIn": "_eventarc_52_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_eventarc_53_TestIamPermissionsRequestOut",
        "GKEIn": "_eventarc_54_GKEIn",
        "GKEOut": "_eventarc_55_GKEOut",
        "ChannelConnectionIn": "_eventarc_56_ChannelConnectionIn",
        "ChannelConnectionOut": "_eventarc_57_ChannelConnectionOut",
        "TriggerIn": "_eventarc_58_TriggerIn",
        "TriggerOut": "_eventarc_59_TriggerOut",
        "BindingIn": "_eventarc_60_BindingIn",
        "BindingOut": "_eventarc_61_BindingOut",
        "ListProvidersResponseIn": "_eventarc_62_ListProvidersResponseIn",
        "ListProvidersResponseOut": "_eventarc_63_ListProvidersResponseOut",
        "EventFilterIn": "_eventarc_64_EventFilterIn",
        "EventFilterOut": "_eventarc_65_EventFilterOut",
        "ListLocationsResponseIn": "_eventarc_66_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_eventarc_67_ListLocationsResponseOut",
        "ChannelIn": "_eventarc_68_ChannelIn",
        "ChannelOut": "_eventarc_69_ChannelOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["CloudRunIn"] = t.struct(
        {"path": t.string().optional(), "region": t.string(), "service": t.string()}
    ).named(renames["CloudRunIn"])
    types["CloudRunOut"] = t.struct(
        {
            "path": t.string().optional(),
            "region": t.string(),
            "service": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["FilteringAttributeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FilteringAttributeIn"]
    )
    types["FilteringAttributeOut"] = t.struct(
        {
            "description": t.string().optional(),
            "pathPatternSupported": t.boolean().optional(),
            "required": t.boolean().optional(),
            "attribute": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilteringAttributeOut"])
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
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["ListTriggersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "triggers": t.array(t.proxy(renames["TriggerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTriggersResponseIn"])
    types["ListTriggersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "triggers": t.array(t.proxy(renames["TriggerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTriggersResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["EventTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EventTypeIn"]
    )
    types["EventTypeOut"] = t.struct(
        {
            "eventSchemaUri": t.string().optional(),
            "filteringAttributes": t.array(
                t.proxy(renames["FilteringAttributeOut"])
            ).optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTypeOut"])
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
    types["ProviderIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProviderIn"]
    )
    types["ProviderOut"] = t.struct(
        {
            "eventTypes": t.array(t.proxy(renames["EventTypeOut"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProviderOut"])
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
    types["TransportIn"] = t.struct(
        {"pubsub": t.proxy(renames["PubsubIn"]).optional()}
    ).named(renames["TransportIn"])
    types["TransportOut"] = t.struct(
        {
            "pubsub": t.proxy(renames["PubsubOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportOut"])
    types["DestinationIn"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunIn"]).optional(),
            "cloudFunction": t.string().optional(),
            "gke": t.proxy(renames["GKEIn"]).optional(),
            "workflow": t.string().optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "cloudRun": t.proxy(renames["CloudRunOut"]).optional(),
            "cloudFunction": t.string().optional(),
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GKEIn"] = t.struct(
        {
            "cluster": t.string(),
            "path": t.string().optional(),
            "location": t.string(),
            "namespace": t.string(),
            "service": t.string(),
        }
    ).named(renames["GKEIn"])
    types["GKEOut"] = t.struct(
        {
            "cluster": t.string(),
            "path": t.string().optional(),
            "location": t.string(),
            "namespace": t.string(),
            "service": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GKEOut"])
    types["ChannelConnectionIn"] = t.struct(
        {
            "activationToken": t.string().optional(),
            "name": t.string(),
            "channel": t.string(),
        }
    ).named(renames["ChannelConnectionIn"])
    types["ChannelConnectionOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "activationToken": t.string().optional(),
            "name": t.string(),
            "channel": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelConnectionOut"])
    types["TriggerIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "transport": t.proxy(renames["TransportIn"]).optional(),
            "name": t.string(),
            "eventDataContentType": t.string().optional(),
            "destination": t.proxy(renames["DestinationIn"]),
            "serviceAccount": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TriggerIn"])
    types["TriggerOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "uid": t.string().optional(),
            "transport": t.proxy(renames["TransportOut"]).optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "conditions": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "eventDataContentType": t.string().optional(),
            "destination": t.proxy(renames["DestinationOut"]),
            "serviceAccount": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ListProvidersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "providers": t.array(t.proxy(renames["ProviderIn"])).optional(),
        }
    ).named(renames["ListProvidersResponseIn"])
    types["ListProvidersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "providers": t.array(t.proxy(renames["ProviderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProvidersResponseOut"])
    types["EventFilterIn"] = t.struct(
        {
            "value": t.string(),
            "operator": t.string().optional(),
            "attribute": t.string(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "value": t.string(),
            "operator": t.string().optional(),
            "attribute": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
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
    types["ChannelIn"] = t.struct(
        {
            "provider": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "provider": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string(),
            "pubsubTopic": t.string().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "activationToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])

    functions = {}
    functions["projectsLocationsGet"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChannelConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChannelConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetGoogleChannelConfig"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChannelConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateGoogleChannelConfig"] = eventarc.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "cryptoKeyName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChannelConfigOut"]),
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
    functions["projectsLocationsOperationsGet"] = eventarc.delete(
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
    functions["projectsLocationsOperationsDelete"] = eventarc.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsChannelConnectionsGetIamPolicy"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelConnectionOut"]),
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
    functions["projectsLocationsChannelConnectionsDelete"] = eventarc.get(
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
    functions["projectsLocationsChannelConnectionsList"] = eventarc.get(
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
    functions["projectsLocationsChannelsList"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsCreate"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsPatch"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsDelete"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsTestIamPermissions"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsGetIamPolicy"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsSetIamPolicy"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsChannelsGet"] = eventarc.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvidersGet"] = eventarc.get(
        "v1/{parent}/providers",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProvidersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersTestIamPermissions"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersCreate"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGetIamPolicy"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersGet"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersDelete"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersSetIamPolicy"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersPatch"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTriggersList"] = eventarc.get(
        "v1/{parent}/triggers",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="eventarc", renames=renames, types=Box(types), functions=Box(functions)
    )
