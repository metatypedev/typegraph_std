from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_networkconnectivity() -> Import:
    networkconnectivity = HTTPRuntime("https://networkconnectivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkconnectivity_1_ErrorResponse",
        "InternalRangeIn": "_networkconnectivity_2_InternalRangeIn",
        "InternalRangeOut": "_networkconnectivity_3_InternalRangeOut",
        "GoogleLongrunningListOperationsResponseIn": "_networkconnectivity_4_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_networkconnectivity_5_GoogleLongrunningListOperationsResponseOut",
        "ListSpokesResponseIn": "_networkconnectivity_6_ListSpokesResponseIn",
        "ListSpokesResponseOut": "_networkconnectivity_7_ListSpokesResponseOut",
        "OperationMetadataIn": "_networkconnectivity_8_OperationMetadataIn",
        "OperationMetadataOut": "_networkconnectivity_9_OperationMetadataOut",
        "SpokeIn": "_networkconnectivity_10_SpokeIn",
        "SpokeOut": "_networkconnectivity_11_SpokeOut",
        "SetIamPolicyRequestIn": "_networkconnectivity_12_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkconnectivity_13_SetIamPolicyRequestOut",
        "RouterApplianceInstanceIn": "_networkconnectivity_14_RouterApplianceInstanceIn",
        "RouterApplianceInstanceOut": "_networkconnectivity_15_RouterApplianceInstanceOut",
        "GoogleLongrunningOperationIn": "_networkconnectivity_16_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_networkconnectivity_17_GoogleLongrunningOperationOut",
        "LinkedInterconnectAttachmentsIn": "_networkconnectivity_18_LinkedInterconnectAttachmentsIn",
        "LinkedInterconnectAttachmentsOut": "_networkconnectivity_19_LinkedInterconnectAttachmentsOut",
        "GoogleRpcStatusIn": "_networkconnectivity_20_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_networkconnectivity_21_GoogleRpcStatusOut",
        "HubIn": "_networkconnectivity_22_HubIn",
        "HubOut": "_networkconnectivity_23_HubOut",
        "LocationMetadataIn": "_networkconnectivity_24_LocationMetadataIn",
        "LocationMetadataOut": "_networkconnectivity_25_LocationMetadataOut",
        "TestIamPermissionsRequestIn": "_networkconnectivity_26_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkconnectivity_27_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_networkconnectivity_28_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkconnectivity_29_TestIamPermissionsResponseOut",
        "ListHubsResponseIn": "_networkconnectivity_30_ListHubsResponseIn",
        "ListHubsResponseOut": "_networkconnectivity_31_ListHubsResponseOut",
        "BindingIn": "_networkconnectivity_32_BindingIn",
        "BindingOut": "_networkconnectivity_33_BindingOut",
        "GoogleLongrunningCancelOperationRequestIn": "_networkconnectivity_34_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_networkconnectivity_35_GoogleLongrunningCancelOperationRequestOut",
        "AuditLogConfigIn": "_networkconnectivity_36_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkconnectivity_37_AuditLogConfigOut",
        "LinkedRouterApplianceInstancesIn": "_networkconnectivity_38_LinkedRouterApplianceInstancesIn",
        "LinkedRouterApplianceInstancesOut": "_networkconnectivity_39_LinkedRouterApplianceInstancesOut",
        "PolicyIn": "_networkconnectivity_40_PolicyIn",
        "PolicyOut": "_networkconnectivity_41_PolicyOut",
        "LinkedVpnTunnelsIn": "_networkconnectivity_42_LinkedVpnTunnelsIn",
        "LinkedVpnTunnelsOut": "_networkconnectivity_43_LinkedVpnTunnelsOut",
        "ListLocationsResponseIn": "_networkconnectivity_44_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkconnectivity_45_ListLocationsResponseOut",
        "AuditConfigIn": "_networkconnectivity_46_AuditConfigIn",
        "AuditConfigOut": "_networkconnectivity_47_AuditConfigOut",
        "RoutingVPCIn": "_networkconnectivity_48_RoutingVPCIn",
        "RoutingVPCOut": "_networkconnectivity_49_RoutingVPCOut",
        "LocationIn": "_networkconnectivity_50_LocationIn",
        "LocationOut": "_networkconnectivity_51_LocationOut",
        "ExprIn": "_networkconnectivity_52_ExprIn",
        "ExprOut": "_networkconnectivity_53_ExprOut",
        "EmptyIn": "_networkconnectivity_54_EmptyIn",
        "EmptyOut": "_networkconnectivity_55_EmptyOut",
        "ListInternalRangesResponseIn": "_networkconnectivity_56_ListInternalRangesResponseIn",
        "ListInternalRangesResponseOut": "_networkconnectivity_57_ListInternalRangesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["InternalRangeIn"] = t.struct(
        {
            "peering": t.string().optional(),
            "usage": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ipCidrRange": t.string().optional(),
            "description": t.string().optional(),
            "overlaps": t.array(t.string()).optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "createTime": t.string().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["InternalRangeIn"])
    types["InternalRangeOut"] = t.struct(
        {
            "peering": t.string().optional(),
            "usage": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ipCidrRange": t.string().optional(),
            "description": t.string().optional(),
            "overlaps": t.array(t.string()).optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "createTime": t.string().optional(),
            "network": t.string().optional(),
            "users": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalRangeOut"])
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
    types["ListSpokesResponseIn"] = t.struct(
        {
            "spokes": t.array(t.proxy(renames["SpokeIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSpokesResponseIn"])
    types["ListSpokesResponseOut"] = t.struct(
        {
            "spokes": t.array(t.proxy(renames["SpokeOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSpokesResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SpokeIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsIn"]
            ).optional(),
            "hub": t.string().optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesIn"]
            ).optional(),
        }
    ).named(renames["SpokeIn"])
    types["SpokeOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "uniqueId": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsOut"]).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "hub": t.string().optional(),
            "state": t.string().optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpokeOut"])
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
    types["RouterApplianceInstanceIn"] = t.struct(
        {"virtualMachine": t.string().optional(), "ipAddress": t.string().optional()}
    ).named(renames["RouterApplianceInstanceIn"])
    types["RouterApplianceInstanceOut"] = t.struct(
        {
            "virtualMachine": t.string().optional(),
            "ipAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouterApplianceInstanceOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["LinkedInterconnectAttachmentsIn"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
        }
    ).named(renames["LinkedInterconnectAttachmentsIn"])
    types["LinkedInterconnectAttachmentsOut"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "vpcNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedInterconnectAttachmentsOut"])
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
    types["HubIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
        }
    ).named(renames["HubIn"])
    types["HubOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "routingVpcs": t.array(t.proxy(renames["RoutingVPCOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HubOut"])
    types["LocationMetadataIn"] = t.struct(
        {"locationFeatures": t.array(t.string()).optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "locationFeatures": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListHubsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "hubs": t.array(t.proxy(renames["HubIn"])).optional(),
        }
    ).named(renames["ListHubsResponseIn"])
    types["ListHubsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "hubs": t.array(t.proxy(renames["HubOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHubsResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
    types["LinkedRouterApplianceInstancesIn"] = t.struct(
        {
            "instances": t.array(
                t.proxy(renames["RouterApplianceInstanceIn"])
            ).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
        }
    ).named(renames["LinkedRouterApplianceInstancesIn"])
    types["LinkedRouterApplianceInstancesOut"] = t.struct(
        {
            "vpcNetwork": t.string().optional(),
            "instances": t.array(
                t.proxy(renames["RouterApplianceInstanceOut"])
            ).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedRouterApplianceInstancesOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["LinkedVpnTunnelsIn"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
        }
    ).named(renames["LinkedVpnTunnelsIn"])
    types["LinkedVpnTunnelsOut"] = t.struct(
        {
            "vpcNetwork": t.string().optional(),
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedVpnTunnelsOut"])
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
    types["RoutingVPCIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["RoutingVPCIn"]
    )
    types["RoutingVPCOut"] = t.struct(
        {
            "requiredForNewSiteToSiteDataTransferSpokes": t.boolean().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutingVPCOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListInternalRangesResponseIn"] = t.struct(
        {
            "internalRanges": t.array(t.proxy(renames["InternalRangeIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListInternalRangesResponseIn"])
    types["ListInternalRangesResponseOut"] = t.struct(
        {
            "internalRanges": t.array(t.proxy(renames["InternalRangeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInternalRangesResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = networkconnectivity.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = networkconnectivity.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionPoliciesGetIamPolicy"
    ] = networkconnectivity.post(
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
    functions[
        "projectsLocationsServiceConnectionPoliciesSetIamPolicy"
    ] = networkconnectivity.post(
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
    functions[
        "projectsLocationsServiceConnectionPoliciesTestIamPermissions"
    ] = networkconnectivity.post(
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
    functions["projectsLocationsGlobalHubsPatch"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalHubsTestIamPermissions"
    ] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsGet"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsList"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsSetIamPolicy"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsGetIamPolicy"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsCreate"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsDelete"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalPolicyBasedRoutesTestIamPermissions"
    ] = networkconnectivity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalPolicyBasedRoutesSetIamPolicy"
    ] = networkconnectivity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalPolicyBasedRoutesGetIamPolicy"
    ] = networkconnectivity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsGetIamPolicy"
    ] = networkconnectivity.post(
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
    functions[
        "projectsLocationsServiceConnectionMapsSetIamPolicy"
    ] = networkconnectivity.post(
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
    functions[
        "projectsLocationsServiceConnectionMapsTestIamPermissions"
    ] = networkconnectivity.post(
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
    functions[
        "projectsLocationsServiceClassesTestIamPermissions"
    ] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceClassesGetIamPolicy"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceClassesSetIamPolicy"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesSetIamPolicy"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesTestIamPermissions"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesList"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesDelete"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesPatch"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesGetIamPolicy"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesGet"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesCreate"] = networkconnectivity.post(
        "v1/{parent}/spokes",
        t.struct(
            {
                "spokeId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "linkedInterconnectAttachments": t.proxy(
                    renames["LinkedInterconnectAttachmentsIn"]
                ).optional(),
                "hub": t.string().optional(),
                "linkedRouterApplianceInstances": t.proxy(
                    renames["LinkedRouterApplianceInstancesIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesList"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesGet"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesPatch"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesCreate"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesDelete"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networkconnectivity",
        renames=renames,
        types=types,
        functions=functions,
    )
