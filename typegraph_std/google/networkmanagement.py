from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_networkmanagement() -> Import:
    networkmanagement = HTTPRuntime("https://networkmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkmanagement_1_ErrorResponse",
        "DeliverInfoIn": "_networkmanagement_2_DeliverInfoIn",
        "DeliverInfoOut": "_networkmanagement_3_DeliverInfoOut",
        "CloudRunRevisionEndpointIn": "_networkmanagement_4_CloudRunRevisionEndpointIn",
        "CloudRunRevisionEndpointOut": "_networkmanagement_5_CloudRunRevisionEndpointOut",
        "ForwardInfoIn": "_networkmanagement_6_ForwardInfoIn",
        "ForwardInfoOut": "_networkmanagement_7_ForwardInfoOut",
        "DropInfoIn": "_networkmanagement_8_DropInfoIn",
        "DropInfoOut": "_networkmanagement_9_DropInfoOut",
        "SetIamPolicyRequestIn": "_networkmanagement_10_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkmanagement_11_SetIamPolicyRequestOut",
        "AppEngineVersionInfoIn": "_networkmanagement_12_AppEngineVersionInfoIn",
        "AppEngineVersionInfoOut": "_networkmanagement_13_AppEngineVersionInfoOut",
        "FirewallInfoIn": "_networkmanagement_14_FirewallInfoIn",
        "FirewallInfoOut": "_networkmanagement_15_FirewallInfoOut",
        "RerunConnectivityTestRequestIn": "_networkmanagement_16_RerunConnectivityTestRequestIn",
        "RerunConnectivityTestRequestOut": "_networkmanagement_17_RerunConnectivityTestRequestOut",
        "CloudFunctionInfoIn": "_networkmanagement_18_CloudFunctionInfoIn",
        "CloudFunctionInfoOut": "_networkmanagement_19_CloudFunctionInfoOut",
        "ConnectivityTestIn": "_networkmanagement_20_ConnectivityTestIn",
        "ConnectivityTestOut": "_networkmanagement_21_ConnectivityTestOut",
        "ReachabilityDetailsIn": "_networkmanagement_22_ReachabilityDetailsIn",
        "ReachabilityDetailsOut": "_networkmanagement_23_ReachabilityDetailsOut",
        "PolicyIn": "_networkmanagement_24_PolicyIn",
        "PolicyOut": "_networkmanagement_25_PolicyOut",
        "BindingIn": "_networkmanagement_26_BindingIn",
        "BindingOut": "_networkmanagement_27_BindingOut",
        "RouteInfoIn": "_networkmanagement_28_RouteInfoIn",
        "RouteInfoOut": "_networkmanagement_29_RouteInfoOut",
        "CloudFunctionEndpointIn": "_networkmanagement_30_CloudFunctionEndpointIn",
        "CloudFunctionEndpointOut": "_networkmanagement_31_CloudFunctionEndpointOut",
        "InstanceInfoIn": "_networkmanagement_32_InstanceInfoIn",
        "InstanceInfoOut": "_networkmanagement_33_InstanceInfoOut",
        "TraceIn": "_networkmanagement_34_TraceIn",
        "TraceOut": "_networkmanagement_35_TraceOut",
        "ListConnectivityTestsResponseIn": "_networkmanagement_36_ListConnectivityTestsResponseIn",
        "ListConnectivityTestsResponseOut": "_networkmanagement_37_ListConnectivityTestsResponseOut",
        "ExprIn": "_networkmanagement_38_ExprIn",
        "ExprOut": "_networkmanagement_39_ExprOut",
        "OperationMetadataIn": "_networkmanagement_40_OperationMetadataIn",
        "OperationMetadataOut": "_networkmanagement_41_OperationMetadataOut",
        "CancelOperationRequestIn": "_networkmanagement_42_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkmanagement_43_CancelOperationRequestOut",
        "LoadBalancerBackendIn": "_networkmanagement_44_LoadBalancerBackendIn",
        "LoadBalancerBackendOut": "_networkmanagement_45_LoadBalancerBackendOut",
        "CloudSQLInstanceInfoIn": "_networkmanagement_46_CloudSQLInstanceInfoIn",
        "CloudSQLInstanceInfoOut": "_networkmanagement_47_CloudSQLInstanceInfoOut",
        "AbortInfoIn": "_networkmanagement_48_AbortInfoIn",
        "AbortInfoOut": "_networkmanagement_49_AbortInfoOut",
        "EndpointIn": "_networkmanagement_50_EndpointIn",
        "EndpointOut": "_networkmanagement_51_EndpointOut",
        "LoadBalancerInfoIn": "_networkmanagement_52_LoadBalancerInfoIn",
        "LoadBalancerInfoOut": "_networkmanagement_53_LoadBalancerInfoOut",
        "ListOperationsResponseIn": "_networkmanagement_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkmanagement_55_ListOperationsResponseOut",
        "StatusIn": "_networkmanagement_56_StatusIn",
        "StatusOut": "_networkmanagement_57_StatusOut",
        "ListLocationsResponseIn": "_networkmanagement_58_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkmanagement_59_ListLocationsResponseOut",
        "LocationIn": "_networkmanagement_60_LocationIn",
        "LocationOut": "_networkmanagement_61_LocationOut",
        "EndpointInfoIn": "_networkmanagement_62_EndpointInfoIn",
        "EndpointInfoOut": "_networkmanagement_63_EndpointInfoOut",
        "GKEMasterInfoIn": "_networkmanagement_64_GKEMasterInfoIn",
        "GKEMasterInfoOut": "_networkmanagement_65_GKEMasterInfoOut",
        "NetworkInfoIn": "_networkmanagement_66_NetworkInfoIn",
        "NetworkInfoOut": "_networkmanagement_67_NetworkInfoOut",
        "EmptyIn": "_networkmanagement_68_EmptyIn",
        "EmptyOut": "_networkmanagement_69_EmptyOut",
        "TestIamPermissionsRequestIn": "_networkmanagement_70_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkmanagement_71_TestIamPermissionsRequestOut",
        "AppEngineVersionEndpointIn": "_networkmanagement_72_AppEngineVersionEndpointIn",
        "AppEngineVersionEndpointOut": "_networkmanagement_73_AppEngineVersionEndpointOut",
        "CloudRunRevisionInfoIn": "_networkmanagement_74_CloudRunRevisionInfoIn",
        "CloudRunRevisionInfoOut": "_networkmanagement_75_CloudRunRevisionInfoOut",
        "OperationIn": "_networkmanagement_76_OperationIn",
        "OperationOut": "_networkmanagement_77_OperationOut",
        "AuditConfigIn": "_networkmanagement_78_AuditConfigIn",
        "AuditConfigOut": "_networkmanagement_79_AuditConfigOut",
        "VpnGatewayInfoIn": "_networkmanagement_80_VpnGatewayInfoIn",
        "VpnGatewayInfoOut": "_networkmanagement_81_VpnGatewayInfoOut",
        "AuditLogConfigIn": "_networkmanagement_82_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkmanagement_83_AuditLogConfigOut",
        "TestIamPermissionsResponseIn": "_networkmanagement_84_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkmanagement_85_TestIamPermissionsResponseOut",
        "StepIn": "_networkmanagement_86_StepIn",
        "StepOut": "_networkmanagement_87_StepOut",
        "VpcConnectorInfoIn": "_networkmanagement_88_VpcConnectorInfoIn",
        "VpcConnectorInfoOut": "_networkmanagement_89_VpcConnectorInfoOut",
        "ForwardingRuleInfoIn": "_networkmanagement_90_ForwardingRuleInfoIn",
        "ForwardingRuleInfoOut": "_networkmanagement_91_ForwardingRuleInfoOut",
        "VpnTunnelInfoIn": "_networkmanagement_92_VpnTunnelInfoIn",
        "VpnTunnelInfoOut": "_networkmanagement_93_VpnTunnelInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["CloudRunRevisionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["CloudRunRevisionEndpointIn"])
    types["CloudRunRevisionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRevisionEndpointOut"])
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
    types["DropInfoIn"] = t.struct(
        {"resourceUri": t.string().optional(), "cause": t.string().optional()}
    ).named(renames["DropInfoIn"])
    types["DropInfoOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "cause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DropInfoOut"])
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
    types["AppEngineVersionInfoIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "uri": t.string().optional(),
            "runtime": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AppEngineVersionInfoIn"])
    types["AppEngineVersionInfoOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "uri": t.string().optional(),
            "runtime": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionInfoOut"])
    types["FirewallInfoIn"] = t.struct(
        {
            "action": t.string().optional(),
            "direction": t.string().optional(),
            "networkUri": t.string().optional(),
            "firewallRuleType": t.string().optional(),
            "priority": t.integer().optional(),
            "displayName": t.string().optional(),
            "targetTags": t.array(t.string()).optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "policy": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["FirewallInfoIn"])
    types["FirewallInfoOut"] = t.struct(
        {
            "action": t.string().optional(),
            "direction": t.string().optional(),
            "networkUri": t.string().optional(),
            "firewallRuleType": t.string().optional(),
            "priority": t.integer().optional(),
            "displayName": t.string().optional(),
            "targetTags": t.array(t.string()).optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "policy": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirewallInfoOut"])
    types["RerunConnectivityTestRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RerunConnectivityTestRequestIn"])
    types["RerunConnectivityTestRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RerunConnectivityTestRequestOut"])
    types["CloudFunctionInfoIn"] = t.struct(
        {
            "versionId": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["CloudFunctionInfoIn"])
    types["CloudFunctionInfoOut"] = t.struct(
        {
            "versionId": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudFunctionInfoOut"])
    types["ConnectivityTestIn"] = t.struct(
        {
            "relatedProjects": t.array(t.string()).optional(),
            "destination": t.proxy(renames["EndpointIn"]),
            "protocol": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["EndpointIn"]),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["ConnectivityTestIn"])
    types["ConnectivityTestOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "reachabilityDetails": t.proxy(
                renames["ReachabilityDetailsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "relatedProjects": t.array(t.string()).optional(),
            "destination": t.proxy(renames["EndpointOut"]),
            "displayName": t.string().optional(),
            "protocol": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "source": t.proxy(renames["EndpointOut"]),
            "description": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityTestOut"])
    types["ReachabilityDetailsIn"] = t.struct(
        {
            "traces": t.array(t.proxy(renames["TraceIn"])).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "verifyTime": t.string().optional(),
            "result": t.string().optional(),
        }
    ).named(renames["ReachabilityDetailsIn"])
    types["ReachabilityDetailsOut"] = t.struct(
        {
            "traces": t.array(t.proxy(renames["TraceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "verifyTime": t.string().optional(),
            "result": t.string().optional(),
        }
    ).named(renames["ReachabilityDetailsOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["RouteInfoIn"] = t.struct(
        {
            "destIpRange": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
            "nextHopType": t.string().optional(),
            "priority": t.integer().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "nextHop": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "routeType": t.string().optional(),
        }
    ).named(renames["RouteInfoIn"])
    types["RouteInfoOut"] = t.struct(
        {
            "destIpRange": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
            "nextHopType": t.string().optional(),
            "priority": t.integer().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "nextHop": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "routeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteInfoOut"])
    types["CloudFunctionEndpointIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["CloudFunctionEndpointIn"]
    )
    types["CloudFunctionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudFunctionEndpointOut"])
    types["InstanceInfoIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "displayName": t.string().optional(),
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "externalIp": t.string().optional(),
            "interface": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
        }
    ).named(renames["InstanceInfoIn"])
    types["InstanceInfoOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "displayName": t.string().optional(),
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "externalIp": t.string().optional(),
            "interface": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
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
    types["ListConnectivityTestsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["ConnectivityTestIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListConnectivityTestsResponseIn"])
    types["ListConnectivityTestsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["ConnectivityTestOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectivityTestsResponseOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["LoadBalancerBackendIn"] = t.struct(
        {
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "healthCheckFirewallState": t.string().optional(),
        }
    ).named(renames["LoadBalancerBackendIn"])
    types["LoadBalancerBackendOut"] = t.struct(
        {
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "healthCheckFirewallState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerBackendOut"])
    types["CloudSQLInstanceInfoIn"] = t.struct(
        {
            "internalIp": t.string().optional(),
            "displayName": t.string().optional(),
            "externalIp": t.string().optional(),
            "uri": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
        }
    ).named(renames["CloudSQLInstanceInfoIn"])
    types["CloudSQLInstanceInfoOut"] = t.struct(
        {
            "internalIp": t.string().optional(),
            "displayName": t.string().optional(),
            "externalIp": t.string().optional(),
            "uri": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSQLInstanceInfoOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "networkType": t.string().optional(),
            "projectId": t.string().optional(),
            "instance": t.string().optional(),
            "cloudSqlInstance": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointIn"]).optional(),
            "gkeMasterCluster": t.string().optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointIn"]
            ).optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointIn"]
            ).optional(),
            "network": t.string().optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "networkType": t.string().optional(),
            "projectId": t.string().optional(),
            "instance": t.string().optional(),
            "cloudSqlInstance": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointOut"]).optional(),
            "gkeMasterCluster": t.string().optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointOut"]
            ).optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointOut"]
            ).optional(),
            "network": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["LoadBalancerInfoIn"] = t.struct(
        {
            "backendUri": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "healthCheckUri": t.string().optional(),
            "backendType": t.string().optional(),
            "backends": t.array(t.proxy(renames["LoadBalancerBackendIn"])).optional(),
        }
    ).named(renames["LoadBalancerInfoIn"])
    types["LoadBalancerInfoOut"] = t.struct(
        {
            "backendUri": t.string().optional(),
            "loadBalancerType": t.string().optional(),
            "healthCheckUri": t.string().optional(),
            "backendType": t.string().optional(),
            "backends": t.array(t.proxy(renames["LoadBalancerBackendOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerInfoOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["EndpointInfoIn"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "protocol": t.string().optional(),
            "destinationNetworkUri": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "sourceIp": t.string().optional(),
            "destinationIp": t.string().optional(),
            "sourceNetworkUri": t.string().optional(),
        }
    ).named(renames["EndpointInfoIn"])
    types["EndpointInfoOut"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "protocol": t.string().optional(),
            "destinationNetworkUri": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "sourceIp": t.string().optional(),
            "destinationIp": t.string().optional(),
            "sourceNetworkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointInfoOut"])
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
    types["NetworkInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "matchedIpRange": t.string().optional(),
        }
    ).named(renames["NetworkInfoIn"])
    types["NetworkInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "matchedIpRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInfoOut"])
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
    types["AppEngineVersionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["AppEngineVersionEndpointIn"])
    types["AppEngineVersionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionEndpointOut"])
    types["CloudRunRevisionInfoIn"] = t.struct(
        {
            "serviceUri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["CloudRunRevisionInfoIn"])
    types["CloudRunRevisionInfoOut"] = t.struct(
        {
            "serviceUri": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRevisionInfoOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["VpnGatewayInfoIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "networkUri": t.string().optional(),
            "region": t.string().optional(),
            "uri": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["VpnGatewayInfoIn"])
    types["VpnGatewayInfoOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "networkUri": t.string().optional(),
            "region": t.string().optional(),
            "uri": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnGatewayInfoOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["StepIn"] = t.struct(
        {
            "description": t.string().optional(),
            "firewall": t.proxy(renames["FirewallInfoIn"]).optional(),
            "state": t.string().optional(),
            "causesDrop": t.boolean().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoIn"]).optional(),
            "network": t.proxy(renames["NetworkInfoIn"]).optional(),
            "instance": t.proxy(renames["InstanceInfoIn"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoIn"]).optional(),
            "endpoint": t.proxy(renames["EndpointInfoIn"]).optional(),
            "abort": t.proxy(renames["AbortInfoIn"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoIn"]).optional(),
            "route": t.proxy(renames["RouteInfoIn"]).optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoIn"]).optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoIn"]).optional(),
            "forward": t.proxy(renames["ForwardInfoIn"]).optional(),
            "drop": t.proxy(renames["DropInfoIn"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoIn"]).optional(),
            "projectId": t.string().optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoIn"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoIn"]).optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoIn"]).optional(),
            "deliver": t.proxy(renames["DeliverInfoIn"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoIn"]).optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "description": t.string().optional(),
            "firewall": t.proxy(renames["FirewallInfoOut"]).optional(),
            "state": t.string().optional(),
            "causesDrop": t.boolean().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoOut"]).optional(),
            "network": t.proxy(renames["NetworkInfoOut"]).optional(),
            "instance": t.proxy(renames["InstanceInfoOut"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoOut"]).optional(),
            "endpoint": t.proxy(renames["EndpointInfoOut"]).optional(),
            "abort": t.proxy(renames["AbortInfoOut"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoOut"]).optional(),
            "route": t.proxy(renames["RouteInfoOut"]).optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoOut"]).optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoOut"]).optional(),
            "forward": t.proxy(renames["ForwardInfoOut"]).optional(),
            "drop": t.proxy(renames["DropInfoOut"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoOut"]).optional(),
            "projectId": t.string().optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoOut"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoOut"]).optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoOut"]).optional(),
            "deliver": t.proxy(renames["DeliverInfoOut"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
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
    types["ForwardingRuleInfoIn"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "vip": t.string().optional(),
            "uri": t.string().optional(),
            "target": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "displayName": t.string().optional(),
            "matchedPortRange": t.string().optional(),
        }
    ).named(renames["ForwardingRuleInfoIn"])
    types["ForwardingRuleInfoOut"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "vip": t.string().optional(),
            "uri": t.string().optional(),
            "target": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "displayName": t.string().optional(),
            "matchedPortRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardingRuleInfoOut"])
    types["VpnTunnelInfoIn"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "remoteGatewayIp": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "displayName": t.string().optional(),
            "region": t.string().optional(),
            "routingType": t.string().optional(),
            "uri": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
        }
    ).named(renames["VpnTunnelInfoIn"])
    types["VpnTunnelInfoOut"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "remoteGatewayIp": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "displayName": t.string().optional(),
            "region": t.string().optional(),
            "routingType": t.string().optional(),
            "uri": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnTunnelInfoOut"])

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
    functions["projectsLocationsGlobalConnectivityTestsList"] = networkmanagement.post(
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
        "projectsLocationsGlobalConnectivityTestsDelete"
    ] = networkmanagement.post(
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
    functions["projectsLocationsGlobalConnectivityTestsRerun"] = networkmanagement.post(
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
    functions["projectsLocationsGlobalConnectivityTestsPatch"] = networkmanagement.post(
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
    functions["projectsLocationsGlobalConnectivityTestsGet"] = networkmanagement.post(
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
        "projectsLocationsGlobalConnectivityTestsGetIamPolicy"
    ] = networkmanagement.post(
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
        "projectsLocationsGlobalConnectivityTestsSetIamPolicy"
    ] = networkmanagement.post(
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
        "projectsLocationsGlobalConnectivityTestsCreate"
    ] = networkmanagement.post(
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
        "projectsLocationsGlobalConnectivityTestsTestIamPermissions"
    ] = networkmanagement.post(
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
    functions["projectsLocationsGlobalOperationsGet"] = networkmanagement.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsDelete"] = networkmanagement.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsCancel"] = networkmanagement.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsList"] = networkmanagement.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networkmanagement", renames=renames, types=types, functions=functions
    )
