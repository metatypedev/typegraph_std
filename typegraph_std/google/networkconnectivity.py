from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_networkconnectivity():
    networkconnectivity = HTTPRuntime("https://networkconnectivity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkconnectivity_1_ErrorResponse",
        "GoogleLongrunningListOperationsResponseIn": "_networkconnectivity_2_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_networkconnectivity_3_GoogleLongrunningListOperationsResponseOut",
        "SpokeTypeCountIn": "_networkconnectivity_4_SpokeTypeCountIn",
        "SpokeTypeCountOut": "_networkconnectivity_5_SpokeTypeCountOut",
        "ListRouteTablesResponseIn": "_networkconnectivity_6_ListRouteTablesResponseIn",
        "ListRouteTablesResponseOut": "_networkconnectivity_7_ListRouteTablesResponseOut",
        "ListServiceClassesResponseIn": "_networkconnectivity_8_ListServiceClassesResponseIn",
        "ListServiceClassesResponseOut": "_networkconnectivity_9_ListServiceClassesResponseOut",
        "ListLocationsResponseIn": "_networkconnectivity_10_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkconnectivity_11_ListLocationsResponseOut",
        "LinkedRouterApplianceInstancesIn": "_networkconnectivity_12_LinkedRouterApplianceInstancesIn",
        "LinkedRouterApplianceInstancesOut": "_networkconnectivity_13_LinkedRouterApplianceInstancesOut",
        "StateReasonIn": "_networkconnectivity_14_StateReasonIn",
        "StateReasonOut": "_networkconnectivity_15_StateReasonOut",
        "BindingIn": "_networkconnectivity_16_BindingIn",
        "BindingOut": "_networkconnectivity_17_BindingOut",
        "LocationIn": "_networkconnectivity_18_LocationIn",
        "LocationOut": "_networkconnectivity_19_LocationOut",
        "RoutingVPCIn": "_networkconnectivity_20_RoutingVPCIn",
        "RoutingVPCOut": "_networkconnectivity_21_RoutingVPCOut",
        "NextHopVpcNetworkIn": "_networkconnectivity_22_NextHopVpcNetworkIn",
        "NextHopVpcNetworkOut": "_networkconnectivity_23_NextHopVpcNetworkOut",
        "GoogleRpcStatusIn": "_networkconnectivity_24_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_networkconnectivity_25_GoogleRpcStatusOut",
        "ServiceClassIn": "_networkconnectivity_26_ServiceClassIn",
        "ServiceClassOut": "_networkconnectivity_27_ServiceClassOut",
        "PscConnectionIn": "_networkconnectivity_28_PscConnectionIn",
        "PscConnectionOut": "_networkconnectivity_29_PscConnectionOut",
        "SpokeSummaryIn": "_networkconnectivity_30_SpokeSummaryIn",
        "SpokeSummaryOut": "_networkconnectivity_31_SpokeSummaryOut",
        "OperationMetadataIn": "_networkconnectivity_32_OperationMetadataIn",
        "OperationMetadataOut": "_networkconnectivity_33_OperationMetadataOut",
        "RouteTableIn": "_networkconnectivity_34_RouteTableIn",
        "RouteTableOut": "_networkconnectivity_35_RouteTableOut",
        "ListServiceConnectionTokensResponseIn": "_networkconnectivity_36_ListServiceConnectionTokensResponseIn",
        "ListServiceConnectionTokensResponseOut": "_networkconnectivity_37_ListServiceConnectionTokensResponseOut",
        "RejectSpokeRequestIn": "_networkconnectivity_38_RejectSpokeRequestIn",
        "RejectSpokeRequestOut": "_networkconnectivity_39_RejectSpokeRequestOut",
        "ListRoutesResponseIn": "_networkconnectivity_40_ListRoutesResponseIn",
        "ListRoutesResponseOut": "_networkconnectivity_41_ListRoutesResponseOut",
        "ConsumerPscConfigIn": "_networkconnectivity_42_ConsumerPscConfigIn",
        "ConsumerPscConfigOut": "_networkconnectivity_43_ConsumerPscConfigOut",
        "SpokeStateCountIn": "_networkconnectivity_44_SpokeStateCountIn",
        "SpokeStateCountOut": "_networkconnectivity_45_SpokeStateCountOut",
        "SpokeStateReasonCountIn": "_networkconnectivity_46_SpokeStateReasonCountIn",
        "SpokeStateReasonCountOut": "_networkconnectivity_47_SpokeStateReasonCountOut",
        "ListInternalRangesResponseIn": "_networkconnectivity_48_ListInternalRangesResponseIn",
        "ListInternalRangesResponseOut": "_networkconnectivity_49_ListInternalRangesResponseOut",
        "ExprIn": "_networkconnectivity_50_ExprIn",
        "ExprOut": "_networkconnectivity_51_ExprOut",
        "ListHubSpokesResponseIn": "_networkconnectivity_52_ListHubSpokesResponseIn",
        "ListHubSpokesResponseOut": "_networkconnectivity_53_ListHubSpokesResponseOut",
        "ListSpokesResponseIn": "_networkconnectivity_54_ListSpokesResponseIn",
        "ListSpokesResponseOut": "_networkconnectivity_55_ListSpokesResponseOut",
        "PscConfigIn": "_networkconnectivity_56_PscConfigIn",
        "PscConfigOut": "_networkconnectivity_57_PscConfigOut",
        "InternalRangeIn": "_networkconnectivity_58_InternalRangeIn",
        "InternalRangeOut": "_networkconnectivity_59_InternalRangeOut",
        "SpokeIn": "_networkconnectivity_60_SpokeIn",
        "SpokeOut": "_networkconnectivity_61_SpokeOut",
        "SetIamPolicyRequestIn": "_networkconnectivity_62_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkconnectivity_63_SetIamPolicyRequestOut",
        "ListServiceConnectionPoliciesResponseIn": "_networkconnectivity_64_ListServiceConnectionPoliciesResponseIn",
        "ListServiceConnectionPoliciesResponseOut": "_networkconnectivity_65_ListServiceConnectionPoliciesResponseOut",
        "GoogleLongrunningCancelOperationRequestIn": "_networkconnectivity_66_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_networkconnectivity_67_GoogleLongrunningCancelOperationRequestOut",
        "EmptyIn": "_networkconnectivity_68_EmptyIn",
        "EmptyOut": "_networkconnectivity_69_EmptyOut",
        "TestIamPermissionsResponseIn": "_networkconnectivity_70_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkconnectivity_71_TestIamPermissionsResponseOut",
        "ServiceConnectionMapIn": "_networkconnectivity_72_ServiceConnectionMapIn",
        "ServiceConnectionMapOut": "_networkconnectivity_73_ServiceConnectionMapOut",
        "AcceptSpokeRequestIn": "_networkconnectivity_74_AcceptSpokeRequestIn",
        "AcceptSpokeRequestOut": "_networkconnectivity_75_AcceptSpokeRequestOut",
        "ServiceConnectionTokenIn": "_networkconnectivity_76_ServiceConnectionTokenIn",
        "ServiceConnectionTokenOut": "_networkconnectivity_77_ServiceConnectionTokenOut",
        "GoogleLongrunningOperationIn": "_networkconnectivity_78_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_networkconnectivity_79_GoogleLongrunningOperationOut",
        "LinkedVpcNetworkIn": "_networkconnectivity_80_LinkedVpcNetworkIn",
        "LinkedVpcNetworkOut": "_networkconnectivity_81_LinkedVpcNetworkOut",
        "HubIn": "_networkconnectivity_82_HubIn",
        "HubOut": "_networkconnectivity_83_HubOut",
        "ListServiceConnectionMapsResponseIn": "_networkconnectivity_84_ListServiceConnectionMapsResponseIn",
        "ListServiceConnectionMapsResponseOut": "_networkconnectivity_85_ListServiceConnectionMapsResponseOut",
        "LocationMetadataIn": "_networkconnectivity_86_LocationMetadataIn",
        "LocationMetadataOut": "_networkconnectivity_87_LocationMetadataOut",
        "TestIamPermissionsRequestIn": "_networkconnectivity_88_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkconnectivity_89_TestIamPermissionsRequestOut",
        "RouterApplianceInstanceIn": "_networkconnectivity_90_RouterApplianceInstanceIn",
        "RouterApplianceInstanceOut": "_networkconnectivity_91_RouterApplianceInstanceOut",
        "ListHubsResponseIn": "_networkconnectivity_92_ListHubsResponseIn",
        "ListHubsResponseOut": "_networkconnectivity_93_ListHubsResponseOut",
        "ProducerPscConfigIn": "_networkconnectivity_94_ProducerPscConfigIn",
        "ProducerPscConfigOut": "_networkconnectivity_95_ProducerPscConfigOut",
        "LinkedVpnTunnelsIn": "_networkconnectivity_96_LinkedVpnTunnelsIn",
        "LinkedVpnTunnelsOut": "_networkconnectivity_97_LinkedVpnTunnelsOut",
        "AuditConfigIn": "_networkconnectivity_98_AuditConfigIn",
        "AuditConfigOut": "_networkconnectivity_99_AuditConfigOut",
        "PolicyIn": "_networkconnectivity_100_PolicyIn",
        "PolicyOut": "_networkconnectivity_101_PolicyOut",
        "ConsumerPscConnectionIn": "_networkconnectivity_102_ConsumerPscConnectionIn",
        "ConsumerPscConnectionOut": "_networkconnectivity_103_ConsumerPscConnectionOut",
        "ServiceConnectionPolicyIn": "_networkconnectivity_104_ServiceConnectionPolicyIn",
        "ServiceConnectionPolicyOut": "_networkconnectivity_105_ServiceConnectionPolicyOut",
        "LinkedInterconnectAttachmentsIn": "_networkconnectivity_106_LinkedInterconnectAttachmentsIn",
        "LinkedInterconnectAttachmentsOut": "_networkconnectivity_107_LinkedInterconnectAttachmentsOut",
        "AuditLogConfigIn": "_networkconnectivity_108_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkconnectivity_109_AuditLogConfigOut",
        "RouteIn": "_networkconnectivity_110_RouteIn",
        "RouteOut": "_networkconnectivity_111_RouteOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SpokeTypeCountIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SpokeTypeCountIn"]
    )
    types["SpokeTypeCountOut"] = t.struct(
        {
            "count": t.string().optional(),
            "spokeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpokeTypeCountOut"])
    types["ListRouteTablesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "routeTables": t.array(t.proxy(renames["RouteTableIn"])).optional(),
        }
    ).named(renames["ListRouteTablesResponseIn"])
    types["ListRouteTablesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "routeTables": t.array(t.proxy(renames["RouteTableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRouteTablesResponseOut"])
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
    types["StateReasonIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "userDetails": t.string().optional(),
        }
    ).named(renames["StateReasonIn"])
    types["StateReasonOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "userDetails": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateReasonOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["NextHopVpcNetworkIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["NextHopVpcNetworkIn"]
    )
    types["NextHopVpcNetworkOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NextHopVpcNetworkOut"])
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
    types["ServiceClassIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ServiceClassIn"])
    types["ServiceClassOut"] = t.struct(
        {
            "serviceClass": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "serviceConnectionMaps": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceClassOut"])
    types["PscConnectionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "consumerForwardingRule": t.string().optional(),
            "errorType": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "consumerTargetProject": t.string().optional(),
            "gceOperation": t.string().optional(),
            "consumerAddress": t.string().optional(),
            "pscConnectionId": t.string().optional(),
        }
    ).named(renames["PscConnectionIn"])
    types["PscConnectionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "consumerForwardingRule": t.string().optional(),
            "errorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "consumerTargetProject": t.string().optional(),
            "gceOperation": t.string().optional(),
            "consumerAddress": t.string().optional(),
            "pscConnectionId": t.string().optional(),
        }
    ).named(renames["PscConnectionOut"])
    types["SpokeSummaryIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SpokeSummaryIn"]
    )
    types["SpokeSummaryOut"] = t.struct(
        {
            "spokeStateReasonCounts": t.array(
                t.proxy(renames["SpokeStateReasonCountOut"])
            ).optional(),
            "spokeStateCounts": t.array(
                t.proxy(renames["SpokeStateCountOut"])
            ).optional(),
            "spokeTypeCounts": t.array(
                t.proxy(renames["SpokeTypeCountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpokeSummaryOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["RouteTableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RouteTableIn"])
    types["RouteTableOut"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteTableOut"])
    types["ListServiceConnectionTokensResponseIn"] = t.struct(
        {
            "serviceConnectionTokens": t.array(
                t.proxy(renames["ServiceConnectionTokenIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListServiceConnectionTokensResponseIn"])
    types["ListServiceConnectionTokensResponseOut"] = t.struct(
        {
            "serviceConnectionTokens": t.array(
                t.proxy(renames["ServiceConnectionTokenOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConnectionTokensResponseOut"])
    types["RejectSpokeRequestIn"] = t.struct(
        {"details": t.string().optional(), "requestId": t.string().optional()}
    ).named(renames["RejectSpokeRequestIn"])
    types["RejectSpokeRequestOut"] = t.struct(
        {
            "details": t.string().optional(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RejectSpokeRequestOut"])
    types["ListRoutesResponseIn"] = t.struct(
        {
            "routes": t.array(t.proxy(renames["RouteIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListRoutesResponseIn"])
    types["ListRoutesResponseOut"] = t.struct(
        {
            "routes": t.array(t.proxy(renames["RouteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRoutesResponseOut"])
    types["ConsumerPscConfigIn"] = t.struct(
        {
            "disableGlobalAccess": t.boolean().optional(),
            "project": t.string().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["ConsumerPscConfigIn"])
    types["ConsumerPscConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "disableGlobalAccess": t.boolean().optional(),
            "project": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerPscConfigOut"])
    types["SpokeStateCountIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SpokeStateCountIn"]
    )
    types["SpokeStateCountOut"] = t.struct(
        {
            "count": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpokeStateCountOut"])
    types["SpokeStateReasonCountIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SpokeStateReasonCountIn"]
    )
    types["SpokeStateReasonCountOut"] = t.struct(
        {
            "count": t.string().optional(),
            "stateReasonCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpokeStateReasonCountOut"])
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
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ListHubSpokesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "spokes": t.array(t.proxy(renames["SpokeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListHubSpokesResponseIn"])
    types["ListHubSpokesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "spokes": t.array(t.proxy(renames["SpokeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHubSpokesResponseOut"])
    types["ListSpokesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "spokes": t.array(t.proxy(renames["SpokeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSpokesResponseIn"])
    types["ListSpokesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "spokes": t.array(t.proxy(renames["SpokeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSpokesResponseOut"])
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
    types["InternalRangeIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "description": t.string().optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "overlaps": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "peering": t.string().optional(),
            "name": t.string().optional(),
            "usage": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
        }
    ).named(renames["InternalRangeIn"])
    types["InternalRangeOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "description": t.string().optional(),
            "targetCidrRange": t.array(t.string()).optional(),
            "overlaps": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "prefixLength": t.integer().optional(),
            "peering": t.string().optional(),
            "name": t.string().optional(),
            "usage": t.string().optional(),
            "users": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InternalRangeOut"])
    types["SpokeIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "hub": t.string().optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesIn"]
            ).optional(),
            "linkedVpcNetwork": t.proxy(renames["LinkedVpcNetworkIn"]).optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsIn"]
            ).optional(),
            "description": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsIn"]).optional(),
        }
    ).named(renames["SpokeIn"])
    types["SpokeOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reasons": t.array(t.proxy(renames["StateReasonOut"])).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "hub": t.string().optional(),
            "updateTime": t.string().optional(),
            "linkedRouterApplianceInstances": t.proxy(
                renames["LinkedRouterApplianceInstancesOut"]
            ).optional(),
            "linkedVpcNetwork": t.proxy(renames["LinkedVpcNetworkOut"]).optional(),
            "uniqueId": t.string().optional(),
            "linkedInterconnectAttachments": t.proxy(
                renames["LinkedInterconnectAttachmentsOut"]
            ).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "spokeType": t.string().optional(),
            "linkedVpnTunnels": t.proxy(renames["LinkedVpnTunnelsOut"]).optional(),
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
    types["ListServiceConnectionPoliciesResponseIn"] = t.struct(
        {
            "serviceConnectionPolicies": t.array(
                t.proxy(renames["ServiceConnectionPolicyIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServiceConnectionPoliciesResponseIn"])
    types["ListServiceConnectionPoliciesResponseOut"] = t.struct(
        {
            "serviceConnectionPolicies": t.array(
                t.proxy(renames["ServiceConnectionPolicyOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConnectionPoliciesResponseOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ServiceConnectionMapIn"] = t.struct(
        {
            "description": t.string().optional(),
            "consumerPscConfigs": t.array(
                t.proxy(renames["ConsumerPscConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "producerPscConfigs": t.array(
                t.proxy(renames["ProducerPscConfigIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "token": t.string().optional(),
            "serviceClass": t.string().optional(),
        }
    ).named(renames["ServiceConnectionMapIn"])
    types["ServiceConnectionMapOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "consumerPscConnections": t.array(
                t.proxy(renames["ConsumerPscConnectionOut"])
            ).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "consumerPscConfigs": t.array(
                t.proxy(renames["ConsumerPscConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "producerPscConfigs": t.array(
                t.proxy(renames["ProducerPscConfigOut"])
            ).optional(),
            "infrastructure": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "token": t.string().optional(),
            "serviceClass": t.string().optional(),
            "serviceClassUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConnectionMapOut"])
    types["AcceptSpokeRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["AcceptSpokeRequestIn"])
    types["AcceptSpokeRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceptSpokeRequestOut"])
    types["ServiceConnectionTokenIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ServiceConnectionTokenIn"])
    types["ServiceConnectionTokenOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "expireTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "token": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConnectionTokenOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["LinkedVpcNetworkIn"] = t.struct(
        {"uri": t.string(), "excludeExportRanges": t.array(t.string()).optional()}
    ).named(renames["LinkedVpcNetworkIn"])
    types["LinkedVpcNetworkOut"] = t.struct(
        {
            "uri": t.string(),
            "excludeExportRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedVpcNetworkOut"])
    types["HubIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["HubIn"])
    types["HubOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "spokeSummary": t.proxy(renames["SpokeSummaryOut"]).optional(),
            "routeTables": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "routingVpcs": t.array(t.proxy(renames["RoutingVPCOut"])).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HubOut"])
    types["ListServiceConnectionMapsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceConnectionMaps": t.array(
                t.proxy(renames["ServiceConnectionMapIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListServiceConnectionMapsResponseIn"])
    types["ListServiceConnectionMapsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceConnectionMaps": t.array(
                t.proxy(renames["ServiceConnectionMapOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConnectionMapsResponseOut"])
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
    types["ProducerPscConfigIn"] = t.struct(
        {"serviceAttachmentUri": t.string().optional()}
    ).named(renames["ProducerPscConfigIn"])
    types["ProducerPscConfigOut"] = t.struct(
        {
            "serviceAttachmentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProducerPscConfigOut"])
    types["LinkedVpnTunnelsIn"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
        }
    ).named(renames["LinkedVpnTunnelsIn"])
    types["LinkedVpnTunnelsOut"] = t.struct(
        {
            "uris": t.array(t.string()).optional(),
            "vpcNetwork": t.string().optional(),
            "siteToSiteDataTransfer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkedVpnTunnelsOut"])
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
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ConsumerPscConnectionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "errorType": t.string().optional(),
            "forwardingRule": t.string().optional(),
            "ip": t.string().optional(),
            "project": t.string().optional(),
            "serviceAttachmentUri": t.string().optional(),
            "gceOperation": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "network": t.string().optional(),
            "pscConnectionId": t.string().optional(),
        }
    ).named(renames["ConsumerPscConnectionIn"])
    types["ConsumerPscConnectionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "errorType": t.string().optional(),
            "forwardingRule": t.string().optional(),
            "ip": t.string().optional(),
            "project": t.string().optional(),
            "serviceAttachmentUri": t.string().optional(),
            "gceOperation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "network": t.string().optional(),
            "pscConnectionId": t.string().optional(),
        }
    ).named(renames["ConsumerPscConnectionOut"])
    types["ServiceConnectionPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pscConfig": t.proxy(renames["PscConfigIn"]).optional(),
            "network": t.string().optional(),
            "serviceClass": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ServiceConnectionPolicyIn"])
    types["ServiceConnectionPolicyOut"] = t.struct(
        {
            "pscConnections": t.array(t.proxy(renames["PscConnectionOut"])).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "pscConfig": t.proxy(renames["PscConfigOut"]).optional(),
            "network": t.string().optional(),
            "infrastructure": t.string().optional(),
            "serviceClass": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConnectionPolicyOut"])
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
    types["RouteIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nextHopVpcNetwork": t.proxy(renames["NextHopVpcNetworkIn"]).optional(),
            "description": t.string().optional(),
            "spoke": t.string().optional(),
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nextHopVpcNetwork": t.proxy(renames["NextHopVpcNetworkOut"]).optional(),
            "description": t.string().optional(),
            "spoke": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])

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
        "projectsLocationsServiceConnectionTokensDelete"
    ] = networkconnectivity.get(
        "v1/{parent}/serviceConnectionTokens",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceConnectionTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionTokensGet"] = networkconnectivity.get(
        "v1/{parent}/serviceConnectionTokens",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceConnectionTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionTokensCreate"
    ] = networkconnectivity.get(
        "v1/{parent}/serviceConnectionTokens",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceConnectionTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionTokensList"] = networkconnectivity.get(
        "v1/{parent}/serviceConnectionTokens",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceConnectionTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsSetIamPolicy"
    ] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionMapsList"] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionMapsGet"] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsGetIamPolicy"
    ] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsTestIamPermissions"
    ] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceConnectionMapsPatch"] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsDelete"
    ] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionMapsCreate"
    ] = networkconnectivity.post(
        "v1/{parent}/serviceConnectionMaps",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceConnectionMapId": t.string().optional(),
                "description": t.string().optional(),
                "consumerPscConfigs": t.array(
                    t.proxy(renames["ConsumerPscConfigIn"])
                ).optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "producerPscConfigs": t.array(
                    t.proxy(renames["ProducerPscConfigIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "serviceClass": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceClassesSetIamPolicy"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceClassesDelete"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceClassesList"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceClassesGet"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceClassesTestIamPermissions"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceClassesGetIamPolicy"
    ] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceClassesPatch"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsDelete"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalHubsTestIamPermissions"
    ] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsSetIamPolicy"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsGet"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsGetIamPolicy"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsList"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsPatch"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsListSpokes"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsCreate"] = networkconnectivity.post(
        "v1/{parent}/hubs",
        t.struct(
            {
                "hubId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "routingVpcs": t.array(t.proxy(renames["RoutingVPCIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsRouteTablesList"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RouteTableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalHubsRouteTablesGet"] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RouteTableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalHubsRouteTablesRoutesList"
    ] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalHubsRouteTablesRoutesGet"
    ] = networkconnectivity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalHubsGroupsGetIamPolicy"
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
        "projectsLocationsGlobalHubsGroupsSetIamPolicy"
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
        "projectsLocationsGlobalHubsGroupsTestIamPermissions"
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
    ] = networkconnectivity.get(
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
    functions[
        "projectsLocationsGlobalPolicyBasedRoutesTestIamPermissions"
    ] = networkconnectivity.get(
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
    functions[
        "projectsLocationsGlobalPolicyBasedRoutesGetIamPolicy"
    ] = networkconnectivity.get(
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
    functions["projectsLocationsOperationsList"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesGet"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "description": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "peering": t.string().optional(),
                "usage": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesList"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "description": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "peering": t.string().optional(),
                "usage": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesDelete"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "description": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "peering": t.string().optional(),
                "usage": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesCreate"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "description": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "peering": t.string().optional(),
                "usage": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInternalRangesPatch"] = networkconnectivity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "createTime": t.string().optional(),
                "ipCidrRange": t.string().optional(),
                "description": t.string().optional(),
                "targetCidrRange": t.array(t.string()).optional(),
                "overlaps": t.array(t.string()).optional(),
                "updateTime": t.string().optional(),
                "prefixLength": t.integer().optional(),
                "peering": t.string().optional(),
                "usage": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesList"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesPatch"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesTestIamPermissions"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesReject"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesGet"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesCreate"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesAccept"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesSetIamPolicy"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesGetIamPolicy"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSpokesDelete"] = networkconnectivity.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceConnectionPoliciesPatch"
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
        "projectsLocationsServiceConnectionPoliciesList"
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
        "projectsLocationsServiceConnectionPoliciesDelete"
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
        "projectsLocationsServiceConnectionPoliciesCreate"
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
        "projectsLocationsServiceConnectionPoliciesGet"
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

    return Import(
        importer="networkconnectivity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
