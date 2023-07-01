from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_networkmanagement():
    networkmanagement = HTTPRuntime("https://networkmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkmanagement_1_ErrorResponse",
        "FirewallInfoIn": "_networkmanagement_2_FirewallInfoIn",
        "FirewallInfoOut": "_networkmanagement_3_FirewallInfoOut",
        "DropInfoIn": "_networkmanagement_4_DropInfoIn",
        "DropInfoOut": "_networkmanagement_5_DropInfoOut",
        "CloudSQLInstanceInfoIn": "_networkmanagement_6_CloudSQLInstanceInfoIn",
        "CloudSQLInstanceInfoOut": "_networkmanagement_7_CloudSQLInstanceInfoOut",
        "ListLocationsResponseIn": "_networkmanagement_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkmanagement_9_ListLocationsResponseOut",
        "ListOperationsResponseIn": "_networkmanagement_10_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkmanagement_11_ListOperationsResponseOut",
        "CancelOperationRequestIn": "_networkmanagement_12_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkmanagement_13_CancelOperationRequestOut",
        "CloudFunctionEndpointIn": "_networkmanagement_14_CloudFunctionEndpointIn",
        "CloudFunctionEndpointOut": "_networkmanagement_15_CloudFunctionEndpointOut",
        "SetIamPolicyRequestIn": "_networkmanagement_16_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkmanagement_17_SetIamPolicyRequestOut",
        "EmptyIn": "_networkmanagement_18_EmptyIn",
        "EmptyOut": "_networkmanagement_19_EmptyOut",
        "OperationIn": "_networkmanagement_20_OperationIn",
        "OperationOut": "_networkmanagement_21_OperationOut",
        "GoogleServiceInfoIn": "_networkmanagement_22_GoogleServiceInfoIn",
        "GoogleServiceInfoOut": "_networkmanagement_23_GoogleServiceInfoOut",
        "ForwardingRuleInfoIn": "_networkmanagement_24_ForwardingRuleInfoIn",
        "ForwardingRuleInfoOut": "_networkmanagement_25_ForwardingRuleInfoOut",
        "BindingIn": "_networkmanagement_26_BindingIn",
        "BindingOut": "_networkmanagement_27_BindingOut",
        "CloudRunRevisionEndpointIn": "_networkmanagement_28_CloudRunRevisionEndpointIn",
        "CloudRunRevisionEndpointOut": "_networkmanagement_29_CloudRunRevisionEndpointOut",
        "ConnectivityTestIn": "_networkmanagement_30_ConnectivityTestIn",
        "ConnectivityTestOut": "_networkmanagement_31_ConnectivityTestOut",
        "GKEMasterInfoIn": "_networkmanagement_32_GKEMasterInfoIn",
        "GKEMasterInfoOut": "_networkmanagement_33_GKEMasterInfoOut",
        "AbortInfoIn": "_networkmanagement_34_AbortInfoIn",
        "AbortInfoOut": "_networkmanagement_35_AbortInfoOut",
        "StatusIn": "_networkmanagement_36_StatusIn",
        "StatusOut": "_networkmanagement_37_StatusOut",
        "VpnTunnelInfoIn": "_networkmanagement_38_VpnTunnelInfoIn",
        "VpnTunnelInfoOut": "_networkmanagement_39_VpnTunnelInfoOut",
        "VpnGatewayInfoIn": "_networkmanagement_40_VpnGatewayInfoIn",
        "VpnGatewayInfoOut": "_networkmanagement_41_VpnGatewayInfoOut",
        "ExprIn": "_networkmanagement_42_ExprIn",
        "ExprOut": "_networkmanagement_43_ExprOut",
        "AppEngineVersionEndpointIn": "_networkmanagement_44_AppEngineVersionEndpointIn",
        "AppEngineVersionEndpointOut": "_networkmanagement_45_AppEngineVersionEndpointOut",
        "PolicyIn": "_networkmanagement_46_PolicyIn",
        "PolicyOut": "_networkmanagement_47_PolicyOut",
        "LocationIn": "_networkmanagement_48_LocationIn",
        "LocationOut": "_networkmanagement_49_LocationOut",
        "LoadBalancerBackendIn": "_networkmanagement_50_LoadBalancerBackendIn",
        "LoadBalancerBackendOut": "_networkmanagement_51_LoadBalancerBackendOut",
        "AuditLogConfigIn": "_networkmanagement_52_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkmanagement_53_AuditLogConfigOut",
        "RerunConnectivityTestRequestIn": "_networkmanagement_54_RerunConnectivityTestRequestIn",
        "RerunConnectivityTestRequestOut": "_networkmanagement_55_RerunConnectivityTestRequestOut",
        "TestIamPermissionsRequestIn": "_networkmanagement_56_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkmanagement_57_TestIamPermissionsRequestOut",
        "AuditConfigIn": "_networkmanagement_58_AuditConfigIn",
        "AuditConfigOut": "_networkmanagement_59_AuditConfigOut",
        "ForwardInfoIn": "_networkmanagement_60_ForwardInfoIn",
        "ForwardInfoOut": "_networkmanagement_61_ForwardInfoOut",
        "OperationMetadataIn": "_networkmanagement_62_OperationMetadataIn",
        "OperationMetadataOut": "_networkmanagement_63_OperationMetadataOut",
        "TraceIn": "_networkmanagement_64_TraceIn",
        "TraceOut": "_networkmanagement_65_TraceOut",
        "CloudRunRevisionInfoIn": "_networkmanagement_66_CloudRunRevisionInfoIn",
        "CloudRunRevisionInfoOut": "_networkmanagement_67_CloudRunRevisionInfoOut",
        "LoadBalancerInfoIn": "_networkmanagement_68_LoadBalancerInfoIn",
        "LoadBalancerInfoOut": "_networkmanagement_69_LoadBalancerInfoOut",
        "ReachabilityDetailsIn": "_networkmanagement_70_ReachabilityDetailsIn",
        "ReachabilityDetailsOut": "_networkmanagement_71_ReachabilityDetailsOut",
        "RouteInfoIn": "_networkmanagement_72_RouteInfoIn",
        "RouteInfoOut": "_networkmanagement_73_RouteInfoOut",
        "TestIamPermissionsResponseIn": "_networkmanagement_74_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkmanagement_75_TestIamPermissionsResponseOut",
        "InstanceInfoIn": "_networkmanagement_76_InstanceInfoIn",
        "InstanceInfoOut": "_networkmanagement_77_InstanceInfoOut",
        "EndpointIn": "_networkmanagement_78_EndpointIn",
        "EndpointOut": "_networkmanagement_79_EndpointOut",
        "CloudFunctionInfoIn": "_networkmanagement_80_CloudFunctionInfoIn",
        "CloudFunctionInfoOut": "_networkmanagement_81_CloudFunctionInfoOut",
        "StepIn": "_networkmanagement_82_StepIn",
        "StepOut": "_networkmanagement_83_StepOut",
        "ListConnectivityTestsResponseIn": "_networkmanagement_84_ListConnectivityTestsResponseIn",
        "ListConnectivityTestsResponseOut": "_networkmanagement_85_ListConnectivityTestsResponseOut",
        "EndpointInfoIn": "_networkmanagement_86_EndpointInfoIn",
        "EndpointInfoOut": "_networkmanagement_87_EndpointInfoOut",
        "AppEngineVersionInfoIn": "_networkmanagement_88_AppEngineVersionInfoIn",
        "AppEngineVersionInfoOut": "_networkmanagement_89_AppEngineVersionInfoOut",
        "DeliverInfoIn": "_networkmanagement_90_DeliverInfoIn",
        "DeliverInfoOut": "_networkmanagement_91_DeliverInfoOut",
        "VpcConnectorInfoIn": "_networkmanagement_92_VpcConnectorInfoIn",
        "VpcConnectorInfoOut": "_networkmanagement_93_VpcConnectorInfoOut",
        "NetworkInfoIn": "_networkmanagement_94_NetworkInfoIn",
        "NetworkInfoOut": "_networkmanagement_95_NetworkInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FirewallInfoIn"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "action": t.string().optional(),
            "priority": t.integer().optional(),
            "direction": t.string().optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "policy": t.string().optional(),
            "firewallRuleType": t.string().optional(),
            "targetTags": t.array(t.string()).optional(),
        }
    ).named(renames["FirewallInfoIn"])
    types["FirewallInfoOut"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "action": t.string().optional(),
            "priority": t.integer().optional(),
            "direction": t.string().optional(),
            "targetServiceAccounts": t.array(t.string()).optional(),
            "policy": t.string().optional(),
            "firewallRuleType": t.string().optional(),
            "targetTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirewallInfoOut"])
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
    types["CloudSQLInstanceInfoIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "region": t.string().optional(),
            "externalIp": t.string().optional(),
            "displayName": t.string().optional(),
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
        }
    ).named(renames["CloudSQLInstanceInfoIn"])
    types["CloudSQLInstanceInfoOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "region": t.string().optional(),
            "externalIp": t.string().optional(),
            "displayName": t.string().optional(),
            "internalIp": t.string().optional(),
            "networkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSQLInstanceInfoOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["CloudFunctionEndpointIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["CloudFunctionEndpointIn"]
    )
    types["CloudFunctionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudFunctionEndpointOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleServiceInfoIn"] = t.struct(
        {"sourceIp": t.string().optional(), "googleServiceType": t.string().optional()}
    ).named(renames["GoogleServiceInfoIn"])
    types["GoogleServiceInfoOut"] = t.struct(
        {
            "sourceIp": t.string().optional(),
            "googleServiceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleServiceInfoOut"])
    types["ForwardingRuleInfoIn"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "target": t.string().optional(),
            "matchedPortRange": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "vip": t.string().optional(),
        }
    ).named(renames["ForwardingRuleInfoIn"])
    types["ForwardingRuleInfoOut"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "matchedProtocol": t.string().optional(),
            "target": t.string().optional(),
            "matchedPortRange": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "vip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ForwardingRuleInfoOut"])
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
    types["CloudRunRevisionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["CloudRunRevisionEndpointIn"])
    types["CloudRunRevisionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRunRevisionEndpointOut"])
    types["ConnectivityTestIn"] = t.struct(
        {
            "description": t.string().optional(),
            "source": t.proxy(renames["EndpointIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destination": t.proxy(renames["EndpointIn"]),
            "protocol": t.string().optional(),
            "relatedProjects": t.array(t.string()).optional(),
            "name": t.string(),
        }
    ).named(renames["ConnectivityTestIn"])
    types["ConnectivityTestOut"] = t.struct(
        {
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "source": t.proxy(renames["EndpointOut"]),
            "reachabilityDetails": t.proxy(
                renames["ReachabilityDetailsOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "destination": t.proxy(renames["EndpointOut"]),
            "protocol": t.string().optional(),
            "relatedProjects": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityTestOut"])
    types["GKEMasterInfoIn"] = t.struct(
        {
            "clusterUri": t.string().optional(),
            "externalIp": t.string().optional(),
            "internalIp": t.string().optional(),
            "clusterNetworkUri": t.string().optional(),
        }
    ).named(renames["GKEMasterInfoIn"])
    types["GKEMasterInfoOut"] = t.struct(
        {
            "clusterUri": t.string().optional(),
            "externalIp": t.string().optional(),
            "internalIp": t.string().optional(),
            "clusterNetworkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GKEMasterInfoOut"])
    types["AbortInfoIn"] = t.struct(
        {
            "cause": t.string().optional(),
            "resourceUri": t.string().optional(),
            "projectsMissingPermission": t.array(t.string()).optional(),
        }
    ).named(renames["AbortInfoIn"])
    types["AbortInfoOut"] = t.struct(
        {
            "cause": t.string().optional(),
            "resourceUri": t.string().optional(),
            "projectsMissingPermission": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AbortInfoOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["VpnTunnelInfoIn"] = t.struct(
        {
            "remoteGatewayIp": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "region": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "uri": t.string().optional(),
            "routingType": t.string().optional(),
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
        }
    ).named(renames["VpnTunnelInfoIn"])
    types["VpnTunnelInfoOut"] = t.struct(
        {
            "remoteGatewayIp": t.string().optional(),
            "remoteGateway": t.string().optional(),
            "region": t.string().optional(),
            "sourceGatewayIp": t.string().optional(),
            "sourceGateway": t.string().optional(),
            "uri": t.string().optional(),
            "routingType": t.string().optional(),
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnTunnelInfoOut"])
    types["VpnGatewayInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "ipAddress": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
            "uri": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
        }
    ).named(renames["VpnGatewayInfoIn"])
    types["VpnGatewayInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "ipAddress": t.string().optional(),
            "vpnTunnelUri": t.string().optional(),
            "uri": t.string().optional(),
            "region": t.string().optional(),
            "networkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpnGatewayInfoOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["AppEngineVersionEndpointIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["AppEngineVersionEndpointIn"])
    types["AppEngineVersionEndpointOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionEndpointOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["LoadBalancerBackendIn"] = t.struct(
        {
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "healthCheckFirewallState": t.string().optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LoadBalancerBackendIn"])
    types["LoadBalancerBackendOut"] = t.struct(
        {
            "healthCheckAllowingFirewallRules": t.array(t.string()).optional(),
            "uri": t.string().optional(),
            "healthCheckFirewallState": t.string().optional(),
            "healthCheckBlockingFirewallRules": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerBackendOut"])
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
    types["RerunConnectivityTestRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RerunConnectivityTestRequestIn"])
    types["RerunConnectivityTestRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RerunConnectivityTestRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["LoadBalancerInfoIn"] = t.struct(
        {
            "loadBalancerType": t.string().optional(),
            "healthCheckUri": t.string().optional(),
            "backendUri": t.string().optional(),
            "backendType": t.string().optional(),
            "backends": t.array(t.proxy(renames["LoadBalancerBackendIn"])).optional(),
        }
    ).named(renames["LoadBalancerInfoIn"])
    types["LoadBalancerInfoOut"] = t.struct(
        {
            "loadBalancerType": t.string().optional(),
            "healthCheckUri": t.string().optional(),
            "backendUri": t.string().optional(),
            "backendType": t.string().optional(),
            "backends": t.array(t.proxy(renames["LoadBalancerBackendOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoadBalancerInfoOut"])
    types["ReachabilityDetailsIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "verifyTime": t.string().optional(),
            "result": t.string().optional(),
            "traces": t.array(t.proxy(renames["TraceIn"])).optional(),
        }
    ).named(renames["ReachabilityDetailsIn"])
    types["ReachabilityDetailsOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "verifyTime": t.string().optional(),
            "result": t.string().optional(),
            "traces": t.array(t.proxy(renames["TraceOut"])).optional(),
        }
    ).named(renames["ReachabilityDetailsOut"])
    types["RouteInfoIn"] = t.struct(
        {
            "nextHop": t.string().optional(),
            "routeType": t.string().optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "destIpRange": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "priority": t.integer().optional(),
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
            "uri": t.string().optional(),
            "nextHopType": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
        }
    ).named(renames["RouteInfoIn"])
    types["RouteInfoOut"] = t.struct(
        {
            "nextHop": t.string().optional(),
            "routeType": t.string().optional(),
            "srcPortRanges": t.array(t.string()).optional(),
            "destPortRanges": t.array(t.string()).optional(),
            "destIpRange": t.string().optional(),
            "srcIpRange": t.string().optional(),
            "instanceTags": t.array(t.string()).optional(),
            "priority": t.integer().optional(),
            "displayName": t.string().optional(),
            "networkUri": t.string().optional(),
            "uri": t.string().optional(),
            "nextHopType": t.string().optional(),
            "protocols": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteInfoOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["InstanceInfoIn"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "uri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "interface": t.string().optional(),
            "displayName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "externalIp": t.string().optional(),
        }
    ).named(renames["InstanceInfoIn"])
    types["InstanceInfoOut"] = t.struct(
        {
            "networkUri": t.string().optional(),
            "internalIp": t.string().optional(),
            "uri": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "interface": t.string().optional(),
            "displayName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "externalIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceInfoOut"])
    types["EndpointIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointIn"]
            ).optional(),
            "networkType": t.string().optional(),
            "cloudSqlInstance": t.string().optional(),
            "gkeMasterCluster": t.string().optional(),
            "instance": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointIn"]).optional(),
            "ipAddress": t.string().optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointIn"]
            ).optional(),
            "projectId": t.string().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "cloudRunRevision": t.proxy(
                renames["CloudRunRevisionEndpointOut"]
            ).optional(),
            "networkType": t.string().optional(),
            "cloudSqlInstance": t.string().optional(),
            "gkeMasterCluster": t.string().optional(),
            "instance": t.string().optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionEndpointOut"]).optional(),
            "ipAddress": t.string().optional(),
            "appEngineVersion": t.proxy(
                renames["AppEngineVersionEndpointOut"]
            ).optional(),
            "projectId": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["CloudFunctionInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "versionId": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["CloudFunctionInfoIn"])
    types["CloudFunctionInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "versionId": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudFunctionInfoOut"])
    types["StepIn"] = t.struct(
        {
            "deliver": t.proxy(renames["DeliverInfoIn"]).optional(),
            "instance": t.proxy(renames["InstanceInfoIn"]).optional(),
            "description": t.string().optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoIn"]).optional(),
            "causesDrop": t.boolean().optional(),
            "abort": t.proxy(renames["AbortInfoIn"]).optional(),
            "drop": t.proxy(renames["DropInfoIn"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoIn"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoIn"]).optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoIn"]).optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "network": t.proxy(renames["NetworkInfoIn"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoIn"]).optional(),
            "route": t.proxy(renames["RouteInfoIn"]).optional(),
            "firewall": t.proxy(renames["FirewallInfoIn"]).optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoIn"]).optional(),
            "googleService": t.proxy(renames["GoogleServiceInfoIn"]).optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoIn"]).optional(),
            "endpoint": t.proxy(renames["EndpointInfoIn"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoIn"]).optional(),
            "forward": t.proxy(renames["ForwardInfoIn"]).optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoIn"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoIn"]).optional(),
        }
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "deliver": t.proxy(renames["DeliverInfoOut"]).optional(),
            "instance": t.proxy(renames["InstanceInfoOut"]).optional(),
            "description": t.string().optional(),
            "loadBalancer": t.proxy(renames["LoadBalancerInfoOut"]).optional(),
            "causesDrop": t.boolean().optional(),
            "abort": t.proxy(renames["AbortInfoOut"]).optional(),
            "drop": t.proxy(renames["DropInfoOut"]).optional(),
            "forwardingRule": t.proxy(renames["ForwardingRuleInfoOut"]).optional(),
            "gkeMaster": t.proxy(renames["GKEMasterInfoOut"]).optional(),
            "cloudFunction": t.proxy(renames["CloudFunctionInfoOut"]).optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "network": t.proxy(renames["NetworkInfoOut"]).optional(),
            "vpnTunnel": t.proxy(renames["VpnTunnelInfoOut"]).optional(),
            "route": t.proxy(renames["RouteInfoOut"]).optional(),
            "firewall": t.proxy(renames["FirewallInfoOut"]).optional(),
            "vpnGateway": t.proxy(renames["VpnGatewayInfoOut"]).optional(),
            "googleService": t.proxy(renames["GoogleServiceInfoOut"]).optional(),
            "vpcConnector": t.proxy(renames["VpcConnectorInfoOut"]).optional(),
            "endpoint": t.proxy(renames["EndpointInfoOut"]).optional(),
            "cloudSqlInstance": t.proxy(renames["CloudSQLInstanceInfoOut"]).optional(),
            "forward": t.proxy(renames["ForwardInfoOut"]).optional(),
            "appEngineVersion": t.proxy(renames["AppEngineVersionInfoOut"]).optional(),
            "cloudRunRevision": t.proxy(renames["CloudRunRevisionInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
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
    types["EndpointInfoIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "sourceIp": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "destinationNetworkUri": t.string().optional(),
            "sourceNetworkUri": t.string().optional(),
        }
    ).named(renames["EndpointInfoIn"])
    types["EndpointInfoOut"] = t.struct(
        {
            "protocol": t.string().optional(),
            "sourceIp": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "destinationIp": t.string().optional(),
            "sourcePort": t.integer().optional(),
            "destinationNetworkUri": t.string().optional(),
            "sourceNetworkUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointInfoOut"])
    types["AppEngineVersionInfoIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "environment": t.string().optional(),
            "runtime": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["AppEngineVersionInfoIn"])
    types["AppEngineVersionInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "environment": t.string().optional(),
            "runtime": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineVersionInfoOut"])
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
    types["VpcConnectorInfoIn"] = t.struct(
        {
            "location": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["VpcConnectorInfoIn"])
    types["VpcConnectorInfoOut"] = t.struct(
        {
            "location": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcConnectorInfoOut"])
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
    functions["projectsLocationsGlobalOperationsGet"] = networkmanagement.delete(
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
    functions["projectsLocationsGlobalOperationsCancel"] = networkmanagement.delete(
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

    return Import(
        importer="networkmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
