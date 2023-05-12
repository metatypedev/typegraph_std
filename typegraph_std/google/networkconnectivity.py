from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_networkconnectivity() -> Import:
    networkconnectivity = HTTPRuntime("https://networkconnectivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkconnectivity_1_ErrorResponse",
        "TestIamPermissionsRequestIn": "_networkconnectivity_2_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkconnectivity_3_TestIamPermissionsRequestOut",
        "SetIamPolicyRequestIn": "_networkconnectivity_4_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkconnectivity_5_SetIamPolicyRequestOut",
        "HubIn": "_networkconnectivity_6_HubIn",
        "HubOut": "_networkconnectivity_7_HubOut",
        "GoogleLongrunningOperationIn": "_networkconnectivity_8_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_networkconnectivity_9_GoogleLongrunningOperationOut",
        "SpokeIn": "_networkconnectivity_10_SpokeIn",
        "SpokeOut": "_networkconnectivity_11_SpokeOut",
        "ListInternalRangesResponseIn": "_networkconnectivity_12_ListInternalRangesResponseIn",
        "ListInternalRangesResponseOut": "_networkconnectivity_13_ListInternalRangesResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_networkconnectivity_14_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_networkconnectivity_15_GoogleLongrunningListOperationsResponseOut",
        "TestIamPermissionsResponseIn": "_networkconnectivity_16_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkconnectivity_17_TestIamPermissionsResponseOut",
        "ListHubsResponseIn": "_networkconnectivity_18_ListHubsResponseIn",
        "ListHubsResponseOut": "_networkconnectivity_19_ListHubsResponseOut",
        "RoutingVPCIn": "_networkconnectivity_20_RoutingVPCIn",
        "RoutingVPCOut": "_networkconnectivity_21_RoutingVPCOut",
        "AuditConfigIn": "_networkconnectivity_22_AuditConfigIn",
        "AuditConfigOut": "_networkconnectivity_23_AuditConfigOut",
        "PolicyIn": "_networkconnectivity_24_PolicyIn",
        "PolicyOut": "_networkconnectivity_25_PolicyOut",
        "GoogleRpcStatusIn": "_networkconnectivity_26_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_networkconnectivity_27_GoogleRpcStatusOut",
        "ListSpokesResponseIn": "_networkconnectivity_28_ListSpokesResponseIn",
        "ListSpokesResponseOut": "_networkconnectivity_29_ListSpokesResponseOut",
        "ListLocationsResponseIn": "_networkconnectivity_30_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkconnectivity_31_ListLocationsResponseOut",
        "RouterApplianceInstanceIn": "_networkconnectivity_32_RouterApplianceInstanceIn",
        "RouterApplianceInstanceOut": "_networkconnectivity_33_RouterApplianceInstanceOut",
        "LocationIn": "_networkconnectivity_34_LocationIn",
        "LocationOut": "_networkconnectivity_35_LocationOut",
        "OperationMetadataIn": "_networkconnectivity_36_OperationMetadataIn",
        "OperationMetadataOut": "_networkconnectivity_37_OperationMetadataOut",
        "GoogleLongrunningCancelOperationRequestIn": "_networkconnectivity_38_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_networkconnectivity_39_GoogleLongrunningCancelOperationRequestOut",
        "LocationMetadataIn": "_networkconnectivity_40_LocationMetadataIn",
        "LocationMetadataOut": "_networkconnectivity_41_LocationMetadataOut",
        "LinkedRouterApplianceInstancesIn": "_networkconnectivity_42_LinkedRouterApplianceInstancesIn",
        "LinkedRouterApplianceInstancesOut": "_networkconnectivity_43_LinkedRouterApplianceInstancesOut",
        "BindingIn": "_networkconnectivity_44_BindingIn",
        "BindingOut": "_networkconnectivity_45_BindingOut",
        "LinkedVpnTunnelsIn": "_networkconnectivity_46_LinkedVpnTunnelsIn",
        "LinkedVpnTunnelsOut": "_networkconnectivity_47_LinkedVpnTunnelsOut",
        "InternalRangeIn": "_networkconnectivity_48_InternalRangeIn",
        "InternalRangeOut": "_networkconnectivity_49_InternalRangeOut",
        "EmptyIn": "_networkconnectivity_50_EmptyIn",
        "EmptyOut": "_networkconnectivity_51_EmptyOut",
        "LinkedInterconnectAttachmentsIn": "_networkconnectivity_52_LinkedInterconnectAttachmentsIn",
        "LinkedInterconnectAttachmentsOut": "_networkconnectivity_53_LinkedInterconnectAttachmentsOut",
        "ExprIn": "_networkconnectivity_54_ExprIn",
        "ExprOut": "_networkconnectivity_55_ExprOut",
        "AuditLogConfigIn": "_networkconnectivity_56_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkconnectivity_57_AuditLogConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
            "state": t.string().optional(),
            "uniqueId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "routingVpcs": t.array(t.proxy(renames["RoutingVPCOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HubOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["SpokeIn"] = t.struct(
        {
            "hub": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesIn"]
            ).optional(),
            "description": t.string().optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SpokeIn"])
    types["SpokeOut"] = t.struct(
        {
            "hub": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesOut"]
            ).optional(),
            "description": t.string().optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsOut"]
            ).optional(),
            "state": t.string().optional(),
            "uniqueId": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpokeOut"])
    types["ListInternalRangesResponseIn"] = t.struct(
        {
            "internalRanges": t.array(t.proxy(renames["InternalRangeIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInternalRangesResponseIn"])
    types["ListInternalRangesResponseOut"] = t.struct(
        {
            "internalRanges": t.array(t.proxy(renames["InternalRangeOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInternalRangesResponseOut"])
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
    types["RoutingVPCIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["RoutingVPCIn"]
    )
    types["RoutingVPCOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "requiredForNewSiteToSiteDataTransferSpokes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutingVPCOut"])
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
    types["ListSpokesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "spokes": t.array(t.proxy(renames["SpokeIn"])).optional(),
        }
    ).named(renames["ListSpokesResponseIn"])
    types["ListSpokesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "spokes": t.array(t.proxy(renames["SpokeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSpokesResponseOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["LocationMetadataIn"] = t.struct(
        {"locationFeatures": t.array(t.string()).optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "locationFeatures": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["LinkedRouterApplianceInstancesIn"] = t.struct(
        {
            "siteToSiteDataTransfer": t.boolean().optional(),
            "instances": t.array(
                t.proxy(renames["RouterApplianceInstanceIn"])
            ).optional(),
        }
    ).named(renames["LinkedRouterApplianceInstancesIn"])
    types["LinkedRouterApplianceInstancesOut"] = t.struct(
        {
            "siteToSiteDataTransfer": t.boolean().optional(),
            "instances": t.array(
                t.proxy(renames["RouterApplianceInstanceOut"])
            ).optional(),
            "vpcNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedRouterApplianceInstancesOut"])
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
    types["LinkedVpnTunnelsIn"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
        }
    ).named(renames["LinkedVpnTunnelsIn"])
    types["LinkedVpnTunnelsOut"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "vpcNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedVpnTunnelsOut"])
    types["InternalRangeIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "peering": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "network": t.string().optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "ipCidrRange": t.string().optional(),
            "createTime": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "overlaps": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "usage": t.string().optional(),
        }
    ).named(renames["InternalRangeIn"])
    types["InternalRangeOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "users": t.array(t.string()).optional(),
            "peering": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "network": t.string().optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "ipCidrRange": t.string().optional(),
            "createTime": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "overlaps": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "usage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalRangeOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LinkedInterconnectAttachmentsIn"] = t.struct(
        {
            "siteToSiteDataTransfer": t.boolean().optional(),
            "uris": t.array(t.string()).optional(),
        }
    ).named(renames["LinkedInterconnectAttachmentsIn"])
    types["LinkedInterconnectAttachmentsOut"] = t.struct(
        {
            "vpcNetwork": t.string().optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "uris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedInterconnectAttachmentsOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = networkconnectivity.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = networkconnectivity.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = networkconnectivity.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = networkconnectivity.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = networkconnectivity.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalPolicyBasedRoutesGetIamPolicy"
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
        "projectsLocationsGlobalPolicyBasedRoutesSetIamPolicy"
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
        "projectsLocationsGlobalPolicyBasedRoutesTestIamPermissions"
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
    functions["projectsLocationsGlobalHubsGet"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsSetIamPolicy"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalHubsTestIamPermissions"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsDelete"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsList"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsCreate"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsGetIamPolicy"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsPatch"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesCreate"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesList"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesTestIamPermissions"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesPatch"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesGetIamPolicy"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesDelete"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesGet"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesSetIamPolicy"] = networkconnectivity.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesDelete"] = networkconnectivity.post(
        "v1/{parent}/internalRanges",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "internalRangeId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "peering": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "ipCidrRange": t.string().optional(),
                "createTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesGet"] = networkconnectivity.post(
        "v1/{parent}/internalRanges",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "internalRangeId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "peering": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "ipCidrRange": t.string().optional(),
                "createTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesPatch"] = networkconnectivity.post(
        "v1/{parent}/internalRanges",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "internalRangeId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "peering": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "ipCidrRange": t.string().optional(),
                "createTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesList"] = networkconnectivity.post(
        "v1/{parent}/internalRanges",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "internalRangeId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "peering": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "ipCidrRange": t.string().optional(),
                "createTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesCreate"] = networkconnectivity.post(
        "v1/{parent}/internalRanges",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "internalRangeId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "peering": t.string().optional(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "ipCidrRange": t.string().optional(),
                "createTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
    functions[
        "projectsLocationsServiceClassesTestIamPermissions"
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
    functions["projectsLocationsServiceClassesSetIamPolicy"] = networkconnectivity.get(
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
    functions["projectsLocationsServiceClassesGetIamPolicy"] = networkconnectivity.get(
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

    return Import(
        importer="networkconnectivity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
