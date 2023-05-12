from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_networkmanagement() -> Import:
    networkmanagement = HTTPRuntime("https://networkmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkmanagement_1_ErrorResponse",
        "LoadBalancerBackendIn": "_networkmanagement_2_LoadBalancerBackendIn",
        "LoadBalancerBackendOut": "_networkmanagement_3_LoadBalancerBackendOut",
        "AbortInfoIn": "_networkmanagement_4_AbortInfoIn",
        "AbortInfoOut": "_networkmanagement_5_AbortInfoOut",
        "ListLocationsResponseIn": "_networkmanagement_6_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkmanagement_7_ListLocationsResponseOut",
        "TestIamPermissionsRequestIn": "_networkmanagement_8_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkmanagement_9_TestIamPermissionsRequestOut",
        "VpnGatewayInfoIn": "_networkmanagement_10_VpnGatewayInfoIn",
        "VpnGatewayInfoOut": "_networkmanagement_11_VpnGatewayInfoOut",
        "BindingIn": "_networkmanagement_12_BindingIn",
        "BindingOut": "_networkmanagement_13_BindingOut",
        "ForwardInfoIn": "_networkmanagement_14_ForwardInfoIn",
        "ForwardInfoOut": "_networkmanagement_15_ForwardInfoOut",
        "ForwardingRuleInfoIn": "_networkmanagement_16_ForwardingRuleInfoIn",
        "ForwardingRuleInfoOut": "_networkmanagement_17_ForwardingRuleInfoOut",
        "InstanceInfoIn": "_networkmanagement_18_InstanceInfoIn",
        "InstanceInfoOut": "_networkmanagement_19_InstanceInfoOut",
        "TraceIn": "_networkmanagement_20_TraceIn",
        "TraceOut": "_networkmanagement_21_TraceOut",
        "LoadBalancerInfoIn": "_networkmanagement_22_LoadBalancerInfoIn",
        "LoadBalancerInfoOut": "_networkmanagement_23_LoadBalancerInfoOut",
        "AppEngineVersionEndpointIn": "_networkmanagement_24_AppEngineVersionEndpointIn",
        "AppEngineVersionEndpointOut": "_networkmanagement_25_AppEngineVersionEndpointOut",
        "NetworkInfoIn": "_networkmanagement_26_NetworkInfoIn",
        "NetworkInfoOut": "_networkmanagement_27_NetworkInfoOut",
        "VpcConnectorInfoIn": "_networkmanagement_28_VpcConnectorInfoIn",
        "VpcConnectorInfoOut": "_networkmanagement_29_VpcConnectorInfoOut",
        "EndpointInfoIn": "_networkmanagement_30_EndpointInfoIn",
        "EndpointInfoOut": "_networkmanagement_31_EndpointInfoOut",
        "AppEngineVersionInfoIn": "_networkmanagement_32_AppEngineVersionInfoIn",
        "AppEngineVersionInfoOut": "_networkmanagement_33_AppEngineVersionInfoOut",
        "ListOperationsResponseIn": "_networkmanagement_34_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkmanagement_35_ListOperationsResponseOut",
        "ConnectivityTestIn": "_networkmanagement_36_ConnectivityTestIn",
        "ConnectivityTestOut": "_networkmanagement_37_ConnectivityTestOut",
        "CloudRunRevisionInfoIn": "_networkmanagement_38_CloudRunRevisionInfoIn",
        "CloudRunRevisionInfoOut": "_networkmanagement_39_CloudRunRevisionInfoOut",
        "SetIamPolicyRequestIn": "_networkmanagement_40_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkmanagement_41_SetIamPolicyRequestOut",
        "RerunConnectivityTestRequestIn": "_networkmanagement_42_RerunConnectivityTestRequestIn",
        "RerunConnectivityTestRequestOut": "_networkmanagement_43_RerunConnectivityTestRequestOut",
        "CloudFunctionEndpointIn": "_networkmanagement_44_CloudFunctionEndpointIn",
        "CloudFunctionEndpointOut": "_networkmanagement_45_CloudFunctionEndpointOut",
        "LocationIn": "_networkmanagement_46_LocationIn",
        "LocationOut": "_networkmanagement_47_LocationOut",
        "TestIamPermissionsResponseIn": "_networkmanagement_48_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkmanagement_49_TestIamPermissionsResponseOut",
        "EndpointIn": "_networkmanagement_50_EndpointIn",
        "EndpointOut": "_networkmanagement_51_EndpointOut",
        "VpnTunnelInfoIn": "_networkmanagement_52_VpnTunnelInfoIn",
        "VpnTunnelInfoOut": "_networkmanagement_53_VpnTunnelInfoOut",
        "OperationIn": "_networkmanagement_54_OperationIn",
        "OperationOut": "_networkmanagement_55_OperationOut",
        "ExprIn": "_networkmanagement_56_ExprIn",
        "ExprOut": "_networkmanagement_57_ExprOut",
        "CloudFunctionInfoIn": "_networkmanagement_58_CloudFunctionInfoIn",
        "CloudFunctionInfoOut": "_networkmanagement_59_CloudFunctionInfoOut",
        "CloudRunRevisionEndpointIn": "_networkmanagement_60_CloudRunRevisionEndpointIn",
        "CloudRunRevisionEndpointOut": "_networkmanagement_61_CloudRunRevisionEndpointOut",
        "ListConnectivityTestsResponseIn": "_networkmanagement_62_ListConnectivityTestsResponseIn",
        "ListConnectivityTestsResponseOut": "_networkmanagement_63_ListConnectivityTestsResponseOut",
        "DeliverInfoIn": "_networkmanagement_64_DeliverInfoIn",
        "DeliverInfoOut": "_networkmanagement_65_DeliverInfoOut",
        "PolicyIn": "_networkmanagement_66_PolicyIn",
        "PolicyOut": "_networkmanagement_67_PolicyOut",
        "FirewallInfoIn": "_networkmanagement_68_FirewallInfoIn",
        "FirewallInfoOut": "_networkmanagement_69_FirewallInfoOut",
        "StepIn": "_networkmanagement_70_StepIn",
        "StepOut": "_networkmanagement_71_StepOut",
        "CloudSQLInstanceInfoIn": "_networkmanagement_72_CloudSQLInstanceInfoIn",
        "CloudSQLInstanceInfoOut": "_networkmanagement_73_CloudSQLInstanceInfoOut",
        "StatusIn": "_networkmanagement_74_StatusIn",
        "StatusOut": "_networkmanagement_75_StatusOut",
        "AuditConfigIn": "_networkmanagement_76_AuditConfigIn",
        "AuditConfigOut": "_networkmanagement_77_AuditConfigOut",
        "GKEMasterInfoIn": "_networkmanagement_78_GKEMasterInfoIn",
        "GKEMasterInfoOut": "_networkmanagement_79_GKEMasterInfoOut",
        "DropInfoIn": "_networkmanagement_80_DropInfoIn",
        "DropInfoOut": "_networkmanagement_81_DropInfoOut",
        "AuditLogConfigIn": "_networkmanagement_82_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkmanagement_83_AuditLogConfigOut",
        "OperationMetadataIn": "_networkmanagement_84_OperationMetadataIn",
        "OperationMetadataOut": "_networkmanagement_85_OperationMetadataOut",
        "RouteInfoIn": "_networkmanagement_86_RouteInfoIn",
        "RouteInfoOut": "_networkmanagement_87_RouteInfoOut",
        "CancelOperationRequestIn": "_networkmanagement_88_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkmanagement_89_CancelOperationRequestOut",
        "ReachabilityDetailsIn": "_networkmanagement_90_ReachabilityDetailsIn",
        "ReachabilityDetailsOut": "_networkmanagement_91_ReachabilityDetailsOut",
        "EmptyIn": "_networkmanagement_92_EmptyIn",
        "EmptyOut": "_networkmanagement_93_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LoadBalancerBackendIn"] = t.struct(
        {
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "healthCheckFirewallState": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["LoadBalancerBackendIn"])
    types["LoadBalancerBackendOut"] = t.struct(
        {
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "healthCheckFirewallState": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerBackendOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["VpnGatewayInfoIn"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "ipAddress": t.string().optional(),
            "region": t.string().optional(),
        }
    ).named(renames["VpnGatewayInfoIn"])
    types["VpnGatewayInfoOut"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "ipAddress": t.string().optional(),
            "region": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnGatewayInfoOut"])
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
    types["ForwardInfoIn"] = t.struct(
        {"target": t.string().optional(), "resourceUri": t.string().optional()}
    ).named(renames["ForwardInfoIn"])
    types["ForwardInfoOut"] = t.struct(
        {
            "target": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardInfoOut"])
    types["ForwardingRuleInfoIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "matchedPortRange": t.string().optional(),
            "target": t.string().optional(),
            "displayName": t.string().optional(),
            "vip": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "networkUri": t.string().optional(),
        }
    ).named(renames["ForwardingRuleInfoIn"])
    types["ForwardingRuleInfoOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "matchedPortRange": t.string().optional(),
            "target": t.string().optional(),
            "displayName": t.string().optional(),
            "vip": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "networkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardingRuleInfoOut"])
    types["InstanceInfoIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "interface": t.string().optional(),
            "externalIp": t.string().optional(),
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["InstanceInfoIn"])
    types["InstanceInfoOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "interface": t.string().optional(),
            "externalIp": t.string().optional(),
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceInfoOut"])
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
    types["LoadBalancerInfoIn"] = t.struct(
        {
            "backendUri": t.string().optional(),
            "backends": t.array(t.proxy(renames["LoadBalancerBackendIn"])).optional(),
            "healthCheckUri": t.string().optional(),
            "backendType": t.string().optional(),
            "loadBalancerType": t.string().optional(),
        }
    ).named(renames["LoadBalancerInfoIn"])
    types["LoadBalancerInfoOut"] = t.struct(
        {
            "backendUri": t.string().optional(),
            "backends": t.array(t.proxy(renames["LoadBalancerBackendOut"])).optional(),
            "healthCheckUri": t.string().optional(),
            "backendType": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerInfoOut"])
    types["AppEngineVersionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["AppEngineVersionEndpointIn"])
    types["AppEngineVersionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionEndpointOut"])
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
    types["VpcConnectorInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["VpcConnectorInfoIn"])
    types["VpcConnectorInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcConnectorInfoOut"])
    types["EndpointInfoIn"] = t.struct(
        {
            "sourceIp": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "sourceNetworkUri": t.string().optional(),
            "destinationNetworkUri": t.string().optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["EndpointInfoIn"])
    types["EndpointInfoOut"] = t.struct(
        {
            "sourceIp": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "sourceNetworkUri": t.string().optional(),
            "destinationNetworkUri": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointInfoOut"])
    types["AppEngineVersionInfoIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "runtime": t.string().optional(),
        }
    ).named(renames["AppEngineVersionInfoIn"])
    types["AppEngineVersionInfoOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "runtime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionInfoOut"])
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
    types["ConnectivityTestIn"] = t.struct(
        {
            "name": t.string(),
            "destination": t.proxy(renames["EndpointIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["EndpointIn"]),
            "relatedProjects": t.array(t.string()).optional(),
            "protocol": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ConnectivityTestIn"])
    types["ConnectivityTestOut"] = t.struct(
        {
            "reachabilityDetails": t.proxy(
                renames["ReachabilityDetailsOut"]
            ).optional(),
            "name": t.string(),
            "destination": t.proxy(renames["EndpointOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["EndpointOut"]),
            "relatedProjects": t.array(t.string()).optional(),
            "protocol": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityTestOut"])
    types["CloudRunRevisionInfoIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "serviceUri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["CloudRunRevisionInfoIn"])
    types["CloudRunRevisionInfoOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "serviceUri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRevisionInfoOut"])
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
    types["RerunConnectivityTestRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RerunConnectivityTestRequestIn"])
    types["RerunConnectivityTestRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RerunConnectivityTestRequestOut"])
    types["CloudFunctionEndpointIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["CloudFunctionEndpointIn"]
    )
    types["CloudFunctionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudFunctionEndpointOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["EndpointIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "cloudSqlInstance": t.string().optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointIn"]
            ).optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointIn"]
            ).optional(),
            "instance": t.string().optional(),
            "ipAddress": t.string().optional(),
            "gkeMasterCluster": t.string().optional(),
            "networkType": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointIn"]).optional(),
            "port": t.integer().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "cloudSqlInstance": t.string().optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointOut"]
            ).optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointOut"]
            ).optional(),
            "instance": t.string().optional(),
            "ipAddress": t.string().optional(),
            "gkeMasterCluster": t.string().optional(),
            "networkType": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointOut"]).optional(),
            "port": t.integer().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["VpnTunnelInfoIn"] = t.struct(
        {
            "remoteGatewayIp": t.string().optional(),
            "routingType": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["VpnTunnelInfoIn"])
    types["VpnTunnelInfoOut"] = t.struct(
        {
            "remoteGatewayIp": t.string().optional(),
            "routingType": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnTunnelInfoOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["CloudRunRevisionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["CloudRunRevisionEndpointIn"])
    types["CloudRunRevisionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRevisionEndpointOut"])
    types["ListConnectivityTestsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "resources": t.array(t.proxy(renames["ConnectivityTestIn"])).optional(),
        }
    ).named(renames["ListConnectivityTestsResponseIn"])
    types["ListConnectivityTestsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "resources": t.array(t.proxy(renames["ConnectivityTestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectivityTestsResponseOut"])
    types["DeliverInfoIn"] = t.struct(
        {"resourceUri": t.string().optional(), "target": t.string().optional()}
    ).named(renames["DeliverInfoIn"])
    types["DeliverInfoOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliverInfoOut"])
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
    types["FirewallInfoIn"] = t.struct(
        {
            "targetTags": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "direction": t.string().optional(),
            "uri": t.string().optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "policy": t.string().optional(),
            "priority": t.integer().optional(),
            "firewallRuleType": t.string().optional(),
        }
    ).named(renames["FirewallInfoIn"])
    types["FirewallInfoOut"] = t.struct(
        {
            "targetTags": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "direction": t.string().optional(),
            "uri": t.string().optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "policy": t.string().optional(),
            "priority": t.integer().optional(),
            "firewallRuleType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirewallInfoOut"])
    types["StepIn"] = t.struct(
        {
            "endpoint": t.proxy(renames["EndpointInfoIn"]).optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoIn"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoIn"]).optional(),
            "abort": t.proxy(renames["AbortInfoIn"]).optional(),
            "causesDrop": t.boolean().optional(),
            "projectId": t.string().optional(),
            "drop": t.proxy(renames["DropInfoIn"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoIn"]).optional(),
            "network": t.proxy(renames["NetworkInfoIn"]).optional(),
            "deliver": t.proxy(renames["DeliverInfoIn"]).optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoIn"]).optional(),
            "description": t.string().optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoIn"]).optional(),
            "firewall": t.proxy(renames["FirewallInfoIn"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoIn"]).optional(),
            "forward": t.proxy(renames["ForwardInfoIn"]).optional(),
            "route": t.proxy(renames["RouteInfoIn"]).optional(),
            "state": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoIn"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoIn"]).optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoIn"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoIn"]).optional(),
            "instance": t.proxy(renames["InstanceInfoIn"]).optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "endpoint": t.proxy(renames["EndpointInfoOut"]).optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoOut"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoOut"]).optional(),
            "abort": t.proxy(renames["AbortInfoOut"]).optional(),
            "causesDrop": t.boolean().optional(),
            "projectId": t.string().optional(),
            "drop": t.proxy(renames["DropInfoOut"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoOut"]).optional(),
            "network": t.proxy(renames["NetworkInfoOut"]).optional(),
            "deliver": t.proxy(renames["DeliverInfoOut"]).optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoOut"]).optional(),
            "description": t.string().optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoOut"]).optional(),
            "firewall": t.proxy(renames["FirewallInfoOut"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoOut"]).optional(),
            "forward": t.proxy(renames["ForwardInfoOut"]).optional(),
            "route": t.proxy(renames["RouteInfoOut"]).optional(),
            "state": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoOut"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoOut"]).optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoOut"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoOut"]).optional(),
            "instance": t.proxy(renames["InstanceInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["CloudSQLInstanceInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "internalIp": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
            "externalIp": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["CloudSQLInstanceInfoIn"])
    types["CloudSQLInstanceInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "internalIp": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
            "externalIp": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSQLInstanceInfoOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["GKEMasterInfoIn"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "clusterUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "clusterNetworkUri": t.string().optional(),
        }
    ).named(renames["GKEMasterInfoIn"])
    types["GKEMasterInfoOut"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "clusterUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "clusterNetworkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GKEMasterInfoOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "target": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["RouteInfoIn"] = t.struct(
        {
            "destIpRange": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "routeType": t.string().optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "priority": t.integer().optional(),
            "nextHop": t.string().optional(),
            "nextHopType": t.string().optional(),
        }
    ).named(renames["RouteInfoIn"])
    types["RouteInfoOut"] = t.struct(
        {
            "destIpRange": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "routeType": t.string().optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "priority": t.integer().optional(),
            "nextHop": t.string().optional(),
            "nextHopType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteInfoOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ReachabilityDetailsIn"] = t.struct(
        {
            "verifyTime": t.string().optional(),
            "traces": t.array(t.proxy(renames["TraceIn"])).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "result": t.string().optional(),
        }
    ).named(renames["ReachabilityDetailsIn"])
    types["ReachabilityDetailsOut"] = t.struct(
        {
            "verifyTime": t.string().optional(),
            "traces": t.array(t.proxy(renames["TraceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "result": t.string().optional(),
        }
    ).named(renames["ReachabilityDetailsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["projectsLocationsList"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = networkmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsCancel"] = networkmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsList"] = networkmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsGet"] = networkmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsDelete"] = networkmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalConnectivityTestsGet"] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsDelete"
    ] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsSetIamPolicy"
    ] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsCreate"
    ] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalConnectivityTestsList"] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsRerun"
    ] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsTestIamPermissions"
    ] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsGetIamPolicy"
    ] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalConnectivityTestsPatch"
    ] = networkmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "destination": t.proxy(renames["EndpointIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "source": t.proxy(renames["EndpointIn"]),
                "relatedProjects": t.array(t.string()).optional(),
                "protocol": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networkmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
