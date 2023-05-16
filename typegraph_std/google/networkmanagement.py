from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_networkmanagement() -> Import:
    networkmanagement = HTTPRuntime("https://networkmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkmanagement_1_ErrorResponse",
        "EndpointIn": "_networkmanagement_2_EndpointIn",
        "EndpointOut": "_networkmanagement_3_EndpointOut",
        "AuditConfigIn": "_networkmanagement_4_AuditConfigIn",
        "AuditConfigOut": "_networkmanagement_5_AuditConfigOut",
        "CloudSQLInstanceInfoIn": "_networkmanagement_6_CloudSQLInstanceInfoIn",
        "CloudSQLInstanceInfoOut": "_networkmanagement_7_CloudSQLInstanceInfoOut",
        "AppEngineVersionInfoIn": "_networkmanagement_8_AppEngineVersionInfoIn",
        "AppEngineVersionInfoOut": "_networkmanagement_9_AppEngineVersionInfoOut",
        "VpcConnectorInfoIn": "_networkmanagement_10_VpcConnectorInfoIn",
        "VpcConnectorInfoOut": "_networkmanagement_11_VpcConnectorInfoOut",
        "AppEngineVersionEndpointIn": "_networkmanagement_12_AppEngineVersionEndpointIn",
        "AppEngineVersionEndpointOut": "_networkmanagement_13_AppEngineVersionEndpointOut",
        "ListConnectivityTestsResponseIn": "_networkmanagement_14_ListConnectivityTestsResponseIn",
        "ListConnectivityTestsResponseOut": "_networkmanagement_15_ListConnectivityTestsResponseOut",
        "AuditLogConfigIn": "_networkmanagement_16_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkmanagement_17_AuditLogConfigOut",
        "ExprIn": "_networkmanagement_18_ExprIn",
        "ExprOut": "_networkmanagement_19_ExprOut",
        "EmptyIn": "_networkmanagement_20_EmptyIn",
        "EmptyOut": "_networkmanagement_21_EmptyOut",
        "CancelOperationRequestIn": "_networkmanagement_22_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkmanagement_23_CancelOperationRequestOut",
        "BindingIn": "_networkmanagement_24_BindingIn",
        "BindingOut": "_networkmanagement_25_BindingOut",
        "CloudRunRevisionInfoIn": "_networkmanagement_26_CloudRunRevisionInfoIn",
        "CloudRunRevisionInfoOut": "_networkmanagement_27_CloudRunRevisionInfoOut",
        "TestIamPermissionsResponseIn": "_networkmanagement_28_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkmanagement_29_TestIamPermissionsResponseOut",
        "ReachabilityDetailsIn": "_networkmanagement_30_ReachabilityDetailsIn",
        "ReachabilityDetailsOut": "_networkmanagement_31_ReachabilityDetailsOut",
        "LocationIn": "_networkmanagement_32_LocationIn",
        "LocationOut": "_networkmanagement_33_LocationOut",
        "RerunConnectivityTestRequestIn": "_networkmanagement_34_RerunConnectivityTestRequestIn",
        "RerunConnectivityTestRequestOut": "_networkmanagement_35_RerunConnectivityTestRequestOut",
        "VpnGatewayInfoIn": "_networkmanagement_36_VpnGatewayInfoIn",
        "VpnGatewayInfoOut": "_networkmanagement_37_VpnGatewayInfoOut",
        "ForwardingRuleInfoIn": "_networkmanagement_38_ForwardingRuleInfoIn",
        "ForwardingRuleInfoOut": "_networkmanagement_39_ForwardingRuleInfoOut",
        "AbortInfoIn": "_networkmanagement_40_AbortInfoIn",
        "AbortInfoOut": "_networkmanagement_41_AbortInfoOut",
        "NetworkInfoIn": "_networkmanagement_42_NetworkInfoIn",
        "NetworkInfoOut": "_networkmanagement_43_NetworkInfoOut",
        "CloudFunctionEndpointIn": "_networkmanagement_44_CloudFunctionEndpointIn",
        "CloudFunctionEndpointOut": "_networkmanagement_45_CloudFunctionEndpointOut",
        "RouteInfoIn": "_networkmanagement_46_RouteInfoIn",
        "RouteInfoOut": "_networkmanagement_47_RouteInfoOut",
        "ListOperationsResponseIn": "_networkmanagement_48_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkmanagement_49_ListOperationsResponseOut",
        "ForwardInfoIn": "_networkmanagement_50_ForwardInfoIn",
        "ForwardInfoOut": "_networkmanagement_51_ForwardInfoOut",
        "OperationIn": "_networkmanagement_52_OperationIn",
        "OperationOut": "_networkmanagement_53_OperationOut",
        "InstanceInfoIn": "_networkmanagement_54_InstanceInfoIn",
        "InstanceInfoOut": "_networkmanagement_55_InstanceInfoOut",
        "DropInfoIn": "_networkmanagement_56_DropInfoIn",
        "DropInfoOut": "_networkmanagement_57_DropInfoOut",
        "VpnTunnelInfoIn": "_networkmanagement_58_VpnTunnelInfoIn",
        "VpnTunnelInfoOut": "_networkmanagement_59_VpnTunnelInfoOut",
        "LoadBalancerInfoIn": "_networkmanagement_60_LoadBalancerInfoIn",
        "LoadBalancerInfoOut": "_networkmanagement_61_LoadBalancerInfoOut",
        "CloudFunctionInfoIn": "_networkmanagement_62_CloudFunctionInfoIn",
        "CloudFunctionInfoOut": "_networkmanagement_63_CloudFunctionInfoOut",
        "OperationMetadataIn": "_networkmanagement_64_OperationMetadataIn",
        "OperationMetadataOut": "_networkmanagement_65_OperationMetadataOut",
        "CloudRunRevisionEndpointIn": "_networkmanagement_66_CloudRunRevisionEndpointIn",
        "CloudRunRevisionEndpointOut": "_networkmanagement_67_CloudRunRevisionEndpointOut",
        "GKEMasterInfoIn": "_networkmanagement_68_GKEMasterInfoIn",
        "GKEMasterInfoOut": "_networkmanagement_69_GKEMasterInfoOut",
        "DeliverInfoIn": "_networkmanagement_70_DeliverInfoIn",
        "DeliverInfoOut": "_networkmanagement_71_DeliverInfoOut",
        "FirewallInfoIn": "_networkmanagement_72_FirewallInfoIn",
        "FirewallInfoOut": "_networkmanagement_73_FirewallInfoOut",
        "TraceIn": "_networkmanagement_74_TraceIn",
        "TraceOut": "_networkmanagement_75_TraceOut",
        "SetIamPolicyRequestIn": "_networkmanagement_76_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkmanagement_77_SetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_networkmanagement_78_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkmanagement_79_TestIamPermissionsRequestOut",
        "ListLocationsResponseIn": "_networkmanagement_80_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkmanagement_81_ListLocationsResponseOut",
        "ConnectivityTestIn": "_networkmanagement_82_ConnectivityTestIn",
        "ConnectivityTestOut": "_networkmanagement_83_ConnectivityTestOut",
        "StepIn": "_networkmanagement_84_StepIn",
        "StepOut": "_networkmanagement_85_StepOut",
        "LoadBalancerBackendIn": "_networkmanagement_86_LoadBalancerBackendIn",
        "LoadBalancerBackendOut": "_networkmanagement_87_LoadBalancerBackendOut",
        "StatusIn": "_networkmanagement_88_StatusIn",
        "StatusOut": "_networkmanagement_89_StatusOut",
        "EndpointInfoIn": "_networkmanagement_90_EndpointInfoIn",
        "EndpointInfoOut": "_networkmanagement_91_EndpointInfoOut",
        "PolicyIn": "_networkmanagement_92_PolicyIn",
        "PolicyOut": "_networkmanagement_93_PolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EndpointIn"] = t.struct(
        {
            "cloudSqlInstance": t.string().optional(),
            "gkeMasterCluster": t.string().optional(),
            "network": t.string().optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointIn"]
            ).optional(),
            "port": t.integer().optional(),
            "instance": t.string().optional(),
            "projectId": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointIn"]).optional(),
            "ipAddress": t.string().optional(),
            "networkType": t.string().optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointIn"]
            ).optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "cloudSqlInstance": t.string().optional(),
            "gkeMasterCluster": t.string().optional(),
            "network": t.string().optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointOut"]
            ).optional(),
            "port": t.integer().optional(),
            "instance": t.string().optional(),
            "projectId": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointOut"]).optional(),
            "ipAddress": t.string().optional(),
            "networkType": t.string().optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["CloudSQLInstanceInfoIn"] = t.struct(
        {
            "region": t.string().optional(),
            "displayName": t.string().optional(),
            "externalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["CloudSQLInstanceInfoIn"])
    types["CloudSQLInstanceInfoOut"] = t.struct(
        {
            "region": t.string().optional(),
            "displayName": t.string().optional(),
            "externalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSQLInstanceInfoOut"])
    types["AppEngineVersionInfoIn"] = t.struct(
        {
            "runtime": t.string().optional(),
            "uri": t.string().optional(),
            "environment": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AppEngineVersionInfoIn"])
    types["AppEngineVersionInfoOut"] = t.struct(
        {
            "runtime": t.string().optional(),
            "uri": t.string().optional(),
            "environment": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionInfoOut"])
    types["VpcConnectorInfoIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["VpcConnectorInfoIn"])
    types["VpcConnectorInfoOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcConnectorInfoOut"])
    types["AppEngineVersionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["AppEngineVersionEndpointIn"])
    types["AppEngineVersionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionEndpointOut"])
    types["ListConnectivityTestsResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ConnectivityTestIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConnectivityTestsResponseIn"])
    types["ListConnectivityTestsResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ConnectivityTestOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectivityTestsResponseOut"])
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
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["CloudRunRevisionInfoIn"] = t.struct(
        {
            "location": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "serviceUri": t.string().optional(),
        }
    ).named(renames["CloudRunRevisionInfoIn"])
    types["CloudRunRevisionInfoOut"] = t.struct(
        {
            "location": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "serviceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRevisionInfoOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ReachabilityDetailsIn"] = t.struct(
        {
            "traces": t.array(t.proxy(renames["TraceIn"])).optional(),
            "verifyTime": t.string().optional(),
            "result": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ReachabilityDetailsIn"])
    types["ReachabilityDetailsOut"] = t.struct(
        {
            "traces": t.array(t.proxy(renames["TraceOut"])).optional(),
            "verifyTime": t.string().optional(),
            "result": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReachabilityDetailsOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RerunConnectivityTestRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RerunConnectivityTestRequestIn"])
    types["RerunConnectivityTestRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RerunConnectivityTestRequestOut"])
    types["VpnGatewayInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
            "region": t.string().optional(),
            "ipAddress": t.string().optional(),
            "uri": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
        }
    ).named(renames["VpnGatewayInfoIn"])
    types["VpnGatewayInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
            "region": t.string().optional(),
            "ipAddress": t.string().optional(),
            "uri": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnGatewayInfoOut"])
    types["ForwardingRuleInfoIn"] = t.struct(
        {
            "target": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "networkUri": t.string().optional(),
            "matchedPortRange": t.string().optional(),
            "vip": t.string().optional(),
        }
    ).named(renames["ForwardingRuleInfoIn"])
    types["ForwardingRuleInfoOut"] = t.struct(
        {
            "target": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "networkUri": t.string().optional(),
            "matchedPortRange": t.string().optional(),
            "vip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardingRuleInfoOut"])
    types["AbortInfoIn"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "cause": t.string().optional(),
            "projectsMissingPermission": t.array(t.string()).optional(),
        }
    ).named(renames["AbortInfoIn"])
    types["AbortInfoOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "cause": t.string().optional(),
            "projectsMissingPermission": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbortInfoOut"])
    types["NetworkInfoIn"] = t.struct(
        {
            "matchedIpRange": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["NetworkInfoIn"])
    types["NetworkInfoOut"] = t.struct(
        {
            "matchedIpRange": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInfoOut"])
    types["CloudFunctionEndpointIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["CloudFunctionEndpointIn"]
    )
    types["CloudFunctionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudFunctionEndpointOut"])
    types["RouteInfoIn"] = t.struct(
        {
            "priority": t.integer().optional(),
            "destIpRange": t.string().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "routeType": t.string().optional(),
            "networkUri": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "uri": t.string().optional(),
            "nextHop": t.string().optional(),
            "nextHopType": t.string().optional(),
        }
    ).named(renames["RouteInfoIn"])
    types["RouteInfoOut"] = t.struct(
        {
            "priority": t.integer().optional(),
            "destIpRange": t.string().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "routeType": t.string().optional(),
            "networkUri": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "uri": t.string().optional(),
            "nextHop": t.string().optional(),
            "nextHopType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteInfoOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ForwardInfoIn"] = t.struct(
        {"resourceUri": t.string().optional(), "target": t.string().optional()}
    ).named(renames["ForwardInfoIn"])
    types["ForwardInfoOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardInfoOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["InstanceInfoIn"] = t.struct(
        {
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "interface": t.string().optional(),
            "uri": t.string().optional(),
            "externalIp": t.string().optional(),
            "displayName": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["InstanceInfoIn"])
    types["InstanceInfoOut"] = t.struct(
        {
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "interface": t.string().optional(),
            "uri": t.string().optional(),
            "externalIp": t.string().optional(),
            "displayName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceInfoOut"])
    types["DropInfoIn"] = t.struct(
        {"cause": t.string().optional(), "resourceUri": t.string().optional()}
    ).named(renames["DropInfoIn"])
    types["DropInfoOut"] = t.struct(
        {
            "cause": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DropInfoOut"])
    types["VpnTunnelInfoIn"] = t.struct(
        {
            "region": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "remoteGatewayIp": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "routingType": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["VpnTunnelInfoIn"])
    types["VpnTunnelInfoOut"] = t.struct(
        {
            "region": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "remoteGatewayIp": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "routingType": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnTunnelInfoOut"])
    types["LoadBalancerInfoIn"] = t.struct(
        {
            "backends": t.array(t.proxy(renames["LoadBalancerBackendIn"])).optional(),
            "healthCheckUri": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "backendType": t.string().optional(),
            "backendUri": t.string().optional(),
        }
    ).named(renames["LoadBalancerInfoIn"])
    types["LoadBalancerInfoOut"] = t.struct(
        {
            "backends": t.array(t.proxy(renames["LoadBalancerBackendOut"])).optional(),
            "healthCheckUri": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "backendType": t.string().optional(),
            "backendUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerInfoOut"])
    types["CloudFunctionInfoIn"] = t.struct(
        {
            "versionId": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["CloudFunctionInfoIn"])
    types["CloudFunctionInfoOut"] = t.struct(
        {
            "versionId": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudFunctionInfoOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CloudRunRevisionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["CloudRunRevisionEndpointIn"])
    types["CloudRunRevisionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRevisionEndpointOut"])
    types["GKEMasterInfoIn"] = t.struct(
        {
            "clusterUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "externalIp": t.string().optional(),
            "clusterNetworkUri": t.string().optional(),
        }
    ).named(renames["GKEMasterInfoIn"])
    types["GKEMasterInfoOut"] = t.struct(
        {
            "clusterUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "externalIp": t.string().optional(),
            "clusterNetworkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GKEMasterInfoOut"])
    types["DeliverInfoIn"] = t.struct(
        {"target": t.string().optional(), "resourceUri": t.string().optional()}
    ).named(renames["DeliverInfoIn"])
    types["DeliverInfoOut"] = t.struct(
        {
            "target": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliverInfoOut"])
    types["FirewallInfoIn"] = t.struct(
        {
            "firewallRuleType": t.string().optional(),
            "priority": t.integer().optional(),
            "displayName": t.string().optional(),
            "action": t.string().optional(),
            "policy": t.string().optional(),
            "targetTags": t.array(t.string()).optional(),
            "direction": t.string().optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "networkUri": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["FirewallInfoIn"])
    types["FirewallInfoOut"] = t.struct(
        {
            "firewallRuleType": t.string().optional(),
            "priority": t.integer().optional(),
            "displayName": t.string().optional(),
            "action": t.string().optional(),
            "policy": t.string().optional(),
            "targetTags": t.array(t.string()).optional(),
            "direction": t.string().optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "networkUri": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirewallInfoOut"])
    types["TraceIn"] = t.struct(
        {
            "endpointInfo": t.proxy(renames["EndpointInfoIn"]).optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
        }
    ).named(renames["TraceIn"])
    types["TraceOut"] = t.struct(
        {
            "endpointInfo": t.proxy(renames["EndpointInfoOut"]).optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TraceOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["ConnectivityTestIn"] = t.struct(
        {
            "name": t.string(),
            "source": t.proxy(renames["EndpointIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destination": t.proxy(renames["EndpointIn"]),
            "protocol": t.string().optional(),
            "description": t.string().optional(),
            "relatedProjects": t.array(t.string()).optional(),
        }
    ).named(renames["ConnectivityTestIn"])
    types["ConnectivityTestOut"] = t.struct(
        {
            "name": t.string(),
            "updateTime": t.string().optional(),
            "source": t.proxy(renames["EndpointOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "reachabilityDetails": t.proxy(
                renames["ReachabilityDetailsOut"]
            ).optional(),
            "destination": t.proxy(renames["EndpointOut"]),
            "protocol": t.string().optional(),
            "description": t.string().optional(),
            "relatedProjects": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityTestOut"])
    types["StepIn"] = t.struct(
        {
            "description": t.string().optional(),
            "projectId": t.string().optional(),
            "network": t.proxy(renames["NetworkInfoIn"]).optional(),
            "firewall": t.proxy(renames["FirewallInfoIn"]).optional(),
            "abort": t.proxy(renames["AbortInfoIn"]).optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoIn"]).optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoIn"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoIn"]).optional(),
            "deliver": t.proxy(renames["DeliverInfoIn"]).optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoIn"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoIn"]).optional(),
            "drop": t.proxy(renames["DropInfoIn"]).optional(),
            "endpoint": t.proxy(renames["EndpointInfoIn"]).optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoIn"]).optional(),
            "causesDrop": t.boolean().optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoIn"]).optional(),
            "forward": t.proxy(renames["ForwardInfoIn"]).optional(),
            "route": t.proxy(renames["RouteInfoIn"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoIn"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoIn"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoIn"]).optional(),
            "instance": t.proxy(renames["InstanceInfoIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "description": t.string().optional(),
            "projectId": t.string().optional(),
            "network": t.proxy(renames["NetworkInfoOut"]).optional(),
            "firewall": t.proxy(renames["FirewallInfoOut"]).optional(),
            "abort": t.proxy(renames["AbortInfoOut"]).optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoOut"]).optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoOut"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoOut"]).optional(),
            "deliver": t.proxy(renames["DeliverInfoOut"]).optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoOut"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoOut"]).optional(),
            "drop": t.proxy(renames["DropInfoOut"]).optional(),
            "endpoint": t.proxy(renames["EndpointInfoOut"]).optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoOut"]).optional(),
            "causesDrop": t.boolean().optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoOut"]).optional(),
            "forward": t.proxy(renames["ForwardInfoOut"]).optional(),
            "route": t.proxy(renames["RouteInfoOut"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoOut"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoOut"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoOut"]).optional(),
            "instance": t.proxy(renames["InstanceInfoOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["LoadBalancerBackendIn"] = t.struct(
        {
            "healthCheckFirewallState": t.string().optional(),
            "displayName": t.string().optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["LoadBalancerBackendIn"])
    types["LoadBalancerBackendOut"] = t.struct(
        {
            "healthCheckFirewallState": t.string().optional(),
            "displayName": t.string().optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerBackendOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EndpointInfoIn"] = t.struct(
        {
            "sourcePort": t.integer().optional(),
            "destinationNetworkUri": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "sourceNetworkUri": t.string().optional(),
            "protocol": t.string().optional(),
            "sourceIp": t.string().optional(),
            "destinationIp": t.string().optional(),
        }
    ).named(renames["EndpointInfoIn"])
    types["EndpointInfoOut"] = t.struct(
        {
            "sourcePort": t.integer().optional(),
            "destinationNetworkUri": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "sourceNetworkUri": t.string().optional(),
            "protocol": t.string().optional(),
            "sourceIp": t.string().optional(),
            "destinationIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointInfoOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = networkmanagement.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = networkmanagement.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsGet"] = networkmanagement.post(
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
    functions["projectsLocationsGlobalOperationsList"] = networkmanagement.post(
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
    functions["projectsLocationsGlobalOperationsDelete"] = networkmanagement.post(
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
    functions["projectsLocationsGlobalOperationsCancel"] = networkmanagement.post(
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
    functions["projectsLocationsGlobalConnectivityTestsList"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalConnectivityTestsDelete"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalConnectivityTestsPatch"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalConnectivityTestsRerun"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalConnectivityTestsCreate"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsGetIamPolicy"
    ] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsTestIamPermissions"
    ] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsSetIamPolicy"
    ] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalConnectivityTestsGet"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConnectivityTestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networkmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
