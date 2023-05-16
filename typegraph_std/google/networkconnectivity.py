from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_networkconnectivity() -> Import:
    networkconnectivity = HTTPRuntime("https://networkconnectivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkconnectivity_1_ErrorResponse",
        "TestIamPermissionsResponseIn": "_networkconnectivity_2_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkconnectivity_3_TestIamPermissionsResponseOut",
        "GoogleLongrunningCancelOperationRequestIn": "_networkconnectivity_4_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_networkconnectivity_5_GoogleLongrunningCancelOperationRequestOut",
        "ServiceClassIn": "_networkconnectivity_6_ServiceClassIn",
        "ServiceClassOut": "_networkconnectivity_7_ServiceClassOut",
        "GoogleLongrunningOperationIn": "_networkconnectivity_8_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_networkconnectivity_9_GoogleLongrunningOperationOut",
        "ConsumerPscConnectionIn": "_networkconnectivity_10_ConsumerPscConnectionIn",
        "ConsumerPscConnectionOut": "_networkconnectivity_11_ConsumerPscConnectionOut",
        "PscConfigIn": "_networkconnectivity_12_PscConfigIn",
        "PscConfigOut": "_networkconnectivity_13_PscConfigOut",
        "ProducerPscConfigIn": "_networkconnectivity_14_ProducerPscConfigIn",
        "ProducerPscConfigOut": "_networkconnectivity_15_ProducerPscConfigOut",
        "ListInternalRangesResponseIn": "_networkconnectivity_16_ListInternalRangesResponseIn",
        "ListInternalRangesResponseOut": "_networkconnectivity_17_ListInternalRangesResponseOut",
        "ListSpokesResponseIn": "_networkconnectivity_18_ListSpokesResponseIn",
        "ListSpokesResponseOut": "_networkconnectivity_19_ListSpokesResponseOut",
        "RoutingVPCIn": "_networkconnectivity_20_RoutingVPCIn",
        "RoutingVPCOut": "_networkconnectivity_21_RoutingVPCOut",
        "ListServiceConnectionTokensResponseIn": "_networkconnectivity_22_ListServiceConnectionTokensResponseIn",
        "ListServiceConnectionTokensResponseOut": "_networkconnectivity_23_ListServiceConnectionTokensResponseOut",
        "ListHubsResponseIn": "_networkconnectivity_24_ListHubsResponseIn",
        "ListHubsResponseOut": "_networkconnectivity_25_ListHubsResponseOut",
        "PolicyIn": "_networkconnectivity_26_PolicyIn",
        "PolicyOut": "_networkconnectivity_27_PolicyOut",
        "AuditConfigIn": "_networkconnectivity_28_AuditConfigIn",
        "AuditConfigOut": "_networkconnectivity_29_AuditConfigOut",
        "RouterApplianceInstanceIn": "_networkconnectivity_30_RouterApplianceInstanceIn",
        "RouterApplianceInstanceOut": "_networkconnectivity_31_RouterApplianceInstanceOut",
        "ServiceConnectionPolicyIn": "_networkconnectivity_32_ServiceConnectionPolicyIn",
        "ServiceConnectionPolicyOut": "_networkconnectivity_33_ServiceConnectionPolicyOut",
        "GoogleLongrunningListOperationsResponseIn": "_networkconnectivity_34_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_networkconnectivity_35_GoogleLongrunningListOperationsResponseOut",
        "ServiceConnectionTokenIn": "_networkconnectivity_36_ServiceConnectionTokenIn",
        "ServiceConnectionTokenOut": "_networkconnectivity_37_ServiceConnectionTokenOut",
        "LocationIn": "_networkconnectivity_38_LocationIn",
        "LocationOut": "_networkconnectivity_39_LocationOut",
        "ListServiceConnectionMapsResponseIn": "_networkconnectivity_40_ListServiceConnectionMapsResponseIn",
        "ListServiceConnectionMapsResponseOut": "_networkconnectivity_41_ListServiceConnectionMapsResponseOut",
        "SpokeIn": "_networkconnectivity_42_SpokeIn",
        "SpokeOut": "_networkconnectivity_43_SpokeOut",
        "ServiceConnectionMapIn": "_networkconnectivity_44_ServiceConnectionMapIn",
        "ServiceConnectionMapOut": "_networkconnectivity_45_ServiceConnectionMapOut",
        "TestIamPermissionsRequestIn": "_networkconnectivity_46_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkconnectivity_47_TestIamPermissionsRequestOut",
        "EmptyIn": "_networkconnectivity_48_EmptyIn",
        "EmptyOut": "_networkconnectivity_49_EmptyOut",
        "SetIamPolicyRequestIn": "_networkconnectivity_50_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkconnectivity_51_SetIamPolicyRequestOut",
        "ListLocationsResponseIn": "_networkconnectivity_52_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkconnectivity_53_ListLocationsResponseOut",
        "InternalRangeIn": "_networkconnectivity_54_InternalRangeIn",
        "InternalRangeOut": "_networkconnectivity_55_InternalRangeOut",
        "LinkedVpnTunnelsIn": "_networkconnectivity_56_LinkedVpnTunnelsIn",
        "LinkedVpnTunnelsOut": "_networkconnectivity_57_LinkedVpnTunnelsOut",
        "LocationMetadataIn": "_networkconnectivity_58_LocationMetadataIn",
        "LocationMetadataOut": "_networkconnectivity_59_LocationMetadataOut",
        "LinkedRouterApplianceInstancesIn": "_networkconnectivity_60_LinkedRouterApplianceInstancesIn",
        "LinkedRouterApplianceInstancesOut": "_networkconnectivity_61_LinkedRouterApplianceInstancesOut",
        "BindingIn": "_networkconnectivity_62_BindingIn",
        "BindingOut": "_networkconnectivity_63_BindingOut",
        "ListServiceClassesResponseIn": "_networkconnectivity_64_ListServiceClassesResponseIn",
        "ListServiceClassesResponseOut": "_networkconnectivity_65_ListServiceClassesResponseOut",
        "ConsumerPscConfigIn": "_networkconnectivity_66_ConsumerPscConfigIn",
        "ConsumerPscConfigOut": "_networkconnectivity_67_ConsumerPscConfigOut",
        "PscConnectionIn": "_networkconnectivity_68_PscConnectionIn",
        "PscConnectionOut": "_networkconnectivity_69_PscConnectionOut",
        "GoogleRpcStatusIn": "_networkconnectivity_70_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_networkconnectivity_71_GoogleRpcStatusOut",
        "AuditLogConfigIn": "_networkconnectivity_72_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkconnectivity_73_AuditLogConfigOut",
        "LinkedInterconnectAttachmentsIn": "_networkconnectivity_74_LinkedInterconnectAttachmentsIn",
        "LinkedInterconnectAttachmentsOut": "_networkconnectivity_75_LinkedInterconnectAttachmentsOut",
        "OperationMetadataIn": "_networkconnectivity_76_OperationMetadataIn",
        "OperationMetadataOut": "_networkconnectivity_77_OperationMetadataOut",
        "ListServiceConnectionPoliciesResponseIn": "_networkconnectivity_78_ListServiceConnectionPoliciesResponseIn",
        "ListServiceConnectionPoliciesResponseOut": "_networkconnectivity_79_ListServiceConnectionPoliciesResponseOut",
        "ExprIn": "_networkconnectivity_80_ExprIn",
        "ExprOut": "_networkconnectivity_81_ExprOut",
        "HubIn": "_networkconnectivity_82_HubIn",
        "HubOut": "_networkconnectivity_83_HubOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["ServiceClassIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceClassIn"])
    types["ServiceClassOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "serviceClass": t.string().optional(),
            "serviceConnectionMaps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceClassOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["ConsumerPscConnectionIn"] = t.struct(
        {
            "serviceAttachmentUri": t.string().optional(),
            "ip": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "errorType": t.string().optional(),
            "forwardingRule": t.string().optional(),
            "gceOperation": t.string().optional(),
            "state": t.string().optional(),
            "network": t.string().optional(),
            "pscConnectionId": t.string().optional(),
        }
    ).named(renames["ConsumerPscConnectionIn"])
    types["ConsumerPscConnectionOut"] = t.struct(
        {
            "serviceAttachmentUri": t.string().optional(),
            "ip": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "errorType": t.string().optional(),
            "forwardingRule": t.string().optional(),
            "gceOperation": t.string().optional(),
            "state": t.string().optional(),
            "network": t.string().optional(),
            "pscConnectionId": t.string().optional(),
        }
    ).named(renames["ConsumerPscConnectionOut"])
    types["PscConfigIn"] = t.struct(
        {"limit": t.string().optional(), "subnetworks": t.array(t.string()).optional()}
    ).named(renames["PscConfigIn"])
    types["PscConfigOut"] = t.struct(
        {
            "limit": t.string().optional(),
            "subnetworks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PscConfigOut"])
    types["ProducerPscConfigIn"] = t.struct(
        {"serviceAttachmentUri": t.string().optional()}
    ).named(renames["ProducerPscConfigIn"])
    types["ProducerPscConfigOut"] = t.struct(
        {
            "serviceAttachmentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProducerPscConfigOut"])
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
    types["ListServiceConnectionTokensResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "serviceConnectionTokens": t.array(
                t.proxy(renames["ServiceConnectionTokenIn"])
            ).optional(),
        }
    ).named(renames["ListServiceConnectionTokensResponseIn"])
    types["ListServiceConnectionTokensResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "serviceConnectionTokens": t.array(
                t.proxy(renames["ServiceConnectionTokenOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConnectionTokensResponseOut"])
    types["ListHubsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "hubs": t.array(t.proxy(renames["HubIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListHubsResponseIn"])
    types["ListHubsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "hubs": t.array(t.proxy(renames["HubOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHubsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["RouterApplianceInstanceIn"] = t.struct(
        {"ipAddress": t.string().optional(), "virtualMachine": t.string().optional()}
    ).named(renames["RouterApplianceInstanceIn"])
    types["RouterApplianceInstanceOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "virtualMachine": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouterApplianceInstanceOut"])
    types["ServiceConnectionPolicyIn"] = t.struct(
        {
            "network": t.string().optional(),
            "pscConfig": t.proxy(renames["PscConfigIn"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "serviceClass": t.string().optional(),
        }
    ).named(renames["ServiceConnectionPolicyIn"])
    types["ServiceConnectionPolicyOut"] = t.struct(
        {
            "network": t.string().optional(),
            "pscConfig": t.proxy(renames["PscConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "infrastructure": t.string().optional(),
            "pscConnections": t.array(t.proxy(renames["PscConnectionOut"])).optional(),
            "updateTime": t.string().optional(),
            "serviceClass": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConnectionPolicyOut"])
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
    types["ServiceConnectionTokenIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ServiceConnectionTokenIn"])
    types["ServiceConnectionTokenOut"] = t.struct(
        {
            "token": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "expireTime": t.string().optional(),
            "network": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConnectionTokenOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListServiceConnectionMapsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "serviceConnectionMaps": t.array(
                t.proxy(renames["ServiceConnectionMapIn"])
            ).optional(),
        }
    ).named(renames["ListServiceConnectionMapsResponseIn"])
    types["ListServiceConnectionMapsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "serviceConnectionMaps": t.array(
                t.proxy(renames["ServiceConnectionMapOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConnectionMapsResponseOut"])
    types["SpokeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsIn"]
            ).optional(),
            "hub": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["SpokeIn"])
    types["SpokeOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsOut"]
            ).optional(),
            "hub": t.string().optional(),
            "createTime": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsOut"]).optional(),
            "uniqueId": t.string().optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpokeOut"])
    types["ServiceConnectionMapIn"] = t.struct(
        {
            "consumerPscConfigs": t.array(
                t.proxy(renames["ConsumerPscConfigIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "serviceClass": t.string().optional(),
            "token": t.string().optional(),
            "producerPscConfigs": t.array(
                t.proxy(renames["ProducerPscConfigIn"])
            ).optional(),
        }
    ).named(renames["ServiceConnectionMapIn"])
    types["ServiceConnectionMapOut"] = t.struct(
        {
            "serviceClassUri": t.string().optional(),
            "consumerPscConfigs": t.array(
                t.proxy(renames["ConsumerPscConfigOut"])
            ).optional(),
            "consumerPscConnections": t.array(
                t.proxy(renames["ConsumerPscConnectionOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "serviceClass": t.string().optional(),
            "token": t.string().optional(),
            "producerPscConfigs": t.array(
                t.proxy(renames["ProducerPscConfigOut"])
            ).optional(),
            "infrastructure": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConnectionMapOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["InternalRangeIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "peering": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "usage": t.string().optional(),
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "network": t.string().optional(),
            "overlaps": t.array(t.string()).optional(),
        }
    ).named(renames["InternalRangeIn"])
    types["InternalRangeOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "peering": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "users": t.array(t.string()).optional(),
            "usage": t.string().optional(),
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "network": t.string().optional(),
            "overlaps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalRangeOut"])
    types["LinkedVpnTunnelsIn"] = t.struct(
        {
            "siteToSiteDataTransfer": t.boolean().optional(),
            "uris": t.array(t.string()).optional(),
        }
    ).named(renames["LinkedVpnTunnelsIn"])
    types["LinkedVpnTunnelsOut"] = t.struct(
        {
            "vpcNetwork": t.string().optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "uris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedVpnTunnelsOut"])
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
            "instances": t.array(
                t.proxy(renames["RouterApplianceInstanceIn"])
            ).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
        }
    ).named(renames["LinkedRouterApplianceInstancesIn"])
    types["LinkedRouterApplianceInstancesOut"] = t.struct(
        {
            "instances": t.array(
                t.proxy(renames["RouterApplianceInstanceOut"])
            ).optional(),
            "vpcNetwork": t.string().optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedRouterApplianceInstancesOut"])
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
    types["ListServiceClassesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "serviceClasses": t.array(t.proxy(renames["ServiceClassIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServiceClassesResponseIn"])
    types["ListServiceClassesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "serviceClasses": t.array(t.proxy(renames["ServiceClassOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceClassesResponseOut"])
    types["ConsumerPscConfigIn"] = t.struct(
        {
            "project": t.string().optional(),
            "disableGlobalAccess": t.boolean().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["ConsumerPscConfigIn"])
    types["ConsumerPscConfigOut"] = t.struct(
        {
            "project": t.string().optional(),
            "disableGlobalAccess": t.boolean().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerPscConfigOut"])
    types["PscConnectionIn"] = t.struct(
        {
            "consumerAddress": t.string().optional(),
            "pscConnectionId": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "state": t.string().optional(),
            "errorType": t.string().optional(),
            "consumerForwardingRule": t.string().optional(),
            "gceOperation": t.string().optional(),
            "consumerTargetProject": t.string().optional(),
        }
    ).named(renames["PscConnectionIn"])
    types["PscConnectionOut"] = t.struct(
        {
            "consumerAddress": t.string().optional(),
            "pscConnectionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "errorType": t.string().optional(),
            "consumerForwardingRule": t.string().optional(),
            "gceOperation": t.string().optional(),
            "consumerTargetProject": t.string().optional(),
        }
    ).named(renames["PscConnectionOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["LinkedInterconnectAttachmentsIn"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
        }
    ).named(renames["LinkedInterconnectAttachmentsIn"])
    types["LinkedInterconnectAttachmentsOut"] = t.struct(
        {
            "vpcNetwork": t.string().optional(),
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedInterconnectAttachmentsOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListServiceConnectionPoliciesResponseIn"] = t.struct(
        {
            "serviceConnectionPolicies": t.array(
                t.proxy(renames["ServiceConnectionPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListServiceConnectionPoliciesResponseIn"])
    types["ListServiceConnectionPoliciesResponseOut"] = t.struct(
        {
            "serviceConnectionPolicies": t.array(
                t.proxy(renames["ServiceConnectionPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConnectionPoliciesResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["HubIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["HubIn"])
    types["HubOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "routingVpcs": t.array(t.proxy(renames["RoutingVPCOut"])).optional(),
            "description": t.string().optional(),
            "uniqueId": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HubOut"])

    functions = {}
    functions["projectsLocationsList"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionPoliciesGet"
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
    functions[
        "projectsLocationsServiceConnectionPoliciesPatch"
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
    functions[
        "projectsLocationsServiceConnectionPoliciesSetIamPolicy"
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
    functions[
        "projectsLocationsServiceConnectionPoliciesGetIamPolicy"
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
    functions[
        "projectsLocationsServiceConnectionPoliciesCreate"
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
    functions[
        "projectsLocationsServiceConnectionPoliciesList"
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
    functions[
        "projectsLocationsServiceConnectionPoliciesTestIamPermissions"
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
    functions[
        "projectsLocationsServiceConnectionPoliciesDelete"
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
    functions["projectsLocationsGlobalHubsCreate"] = networkconnectivity.post(
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
    functions["projectsLocationsGlobalHubsDelete"] = networkconnectivity.post(
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
    functions["projectsLocationsGlobalHubsGet"] = networkconnectivity.post(
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
    functions["projectsLocationsGlobalHubsPatch"] = networkconnectivity.post(
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
    functions["projectsLocationsGlobalHubsGetIamPolicy"] = networkconnectivity.post(
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
    functions[
        "projectsLocationsGlobalHubsTestIamPermissions"
    ] = networkconnectivity.post(
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
    functions["projectsLocationsGlobalHubsList"] = networkconnectivity.post(
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
    functions["projectsLocationsGlobalHubsSetIamPolicy"] = networkconnectivity.post(
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
    functions["projectsLocationsOperationsDelete"] = networkconnectivity.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = networkconnectivity.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = networkconnectivity.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = networkconnectivity.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionTokensDelete"
    ] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceConnectionTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionTokensList"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceConnectionTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionTokensCreate"
    ] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceConnectionTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionTokensGet"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceConnectionTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesGet"] = networkconnectivity.post(
        "v1/{parent}/internalRanges",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "internalRangeId": t.string().optional(),
                "createTime": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "peering": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "name": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "network": t.string().optional(),
                "overlaps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesDelete"] = networkconnectivity.post(
        "v1/{parent}/internalRanges",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "internalRangeId": t.string().optional(),
                "createTime": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "peering": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "name": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "network": t.string().optional(),
                "overlaps": t.array(t.string()).optional(),
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
                "requestId": t.string().optional(),
                "parent": t.string(),
                "internalRangeId": t.string().optional(),
                "createTime": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "peering": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "name": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "network": t.string().optional(),
                "overlaps": t.array(t.string()).optional(),
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
                "requestId": t.string().optional(),
                "parent": t.string(),
                "internalRangeId": t.string().optional(),
                "createTime": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "peering": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "name": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "network": t.string().optional(),
                "overlaps": t.array(t.string()).optional(),
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
                "requestId": t.string().optional(),
                "parent": t.string(),
                "internalRangeId": t.string().optional(),
                "createTime": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "peering": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "usage": t.string().optional(),
                "name": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "network": t.string().optional(),
                "overlaps": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceClassesGet"] = networkconnectivity.post(
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
    functions["projectsLocationsServiceClassesCreate"] = networkconnectivity.post(
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
    functions["projectsLocationsServiceClassesDelete"] = networkconnectivity.post(
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
    functions["projectsLocationsServiceClassesGetIamPolicy"] = networkconnectivity.post(
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
    functions[
        "projectsLocationsServiceClassesTestIamPermissions"
    ] = networkconnectivity.post(
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
    functions["projectsLocationsServiceClassesList"] = networkconnectivity.post(
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
    functions["projectsLocationsServiceClassesPatch"] = networkconnectivity.post(
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
    functions["projectsLocationsServiceClassesSetIamPolicy"] = networkconnectivity.post(
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
    functions["projectsLocationsServiceConnectionMapsGet"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsCreate"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsTestIamPermissions"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsSetIamPolicy"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsGetIamPolicy"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsDelete"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionMapsList"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsPatch"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "serviceClass": t.string().optional(),
                "token": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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

    return Import(
        importer="networkconnectivity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
