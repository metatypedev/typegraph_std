from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_networkservices() -> Import:
    networkservices = HTTPRuntime("https://networkservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkservices_1_ErrorResponse",
        "LocationIn": "_networkservices_2_LocationIn",
        "LocationOut": "_networkservices_3_LocationOut",
        "GatewayIn": "_networkservices_4_GatewayIn",
        "GatewayOut": "_networkservices_5_GatewayOut",
        "HttpRouteRouteActionIn": "_networkservices_6_HttpRouteRouteActionIn",
        "HttpRouteRouteActionOut": "_networkservices_7_HttpRouteRouteActionOut",
        "TlsRouteRouteMatchIn": "_networkservices_8_TlsRouteRouteMatchIn",
        "TlsRouteRouteMatchOut": "_networkservices_9_TlsRouteRouteMatchOut",
        "AuditConfigIn": "_networkservices_10_AuditConfigIn",
        "AuditConfigOut": "_networkservices_11_AuditConfigOut",
        "ListGrpcRoutesResponseIn": "_networkservices_12_ListGrpcRoutesResponseIn",
        "ListGrpcRoutesResponseOut": "_networkservices_13_ListGrpcRoutesResponseOut",
        "SetIamPolicyRequestIn": "_networkservices_14_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkservices_15_SetIamPolicyRequestOut",
        "ListHttpRoutesResponseIn": "_networkservices_16_ListHttpRoutesResponseIn",
        "ListHttpRoutesResponseOut": "_networkservices_17_ListHttpRoutesResponseOut",
        "TcpRouteIn": "_networkservices_18_TcpRouteIn",
        "TcpRouteOut": "_networkservices_19_TcpRouteOut",
        "EmptyIn": "_networkservices_20_EmptyIn",
        "EmptyOut": "_networkservices_21_EmptyOut",
        "TlsRouteIn": "_networkservices_22_TlsRouteIn",
        "TlsRouteOut": "_networkservices_23_TlsRouteOut",
        "BindingIn": "_networkservices_24_BindingIn",
        "BindingOut": "_networkservices_25_BindingOut",
        "GrpcRouteIn": "_networkservices_26_GrpcRouteIn",
        "GrpcRouteOut": "_networkservices_27_GrpcRouteOut",
        "HttpRouteHeaderMatchIntegerRangeIn": "_networkservices_28_HttpRouteHeaderMatchIntegerRangeIn",
        "HttpRouteHeaderMatchIntegerRangeOut": "_networkservices_29_HttpRouteHeaderMatchIntegerRangeOut",
        "GrpcRouteRetryPolicyIn": "_networkservices_30_GrpcRouteRetryPolicyIn",
        "GrpcRouteRetryPolicyOut": "_networkservices_31_GrpcRouteRetryPolicyOut",
        "HttpRouteURLRewriteIn": "_networkservices_32_HttpRouteURLRewriteIn",
        "HttpRouteURLRewriteOut": "_networkservices_33_HttpRouteURLRewriteOut",
        "TestIamPermissionsRequestIn": "_networkservices_34_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkservices_35_TestIamPermissionsRequestOut",
        "GrpcRouteMethodMatchIn": "_networkservices_36_GrpcRouteMethodMatchIn",
        "GrpcRouteMethodMatchOut": "_networkservices_37_GrpcRouteMethodMatchOut",
        "HttpRouteFaultInjectionPolicyDelayIn": "_networkservices_38_HttpRouteFaultInjectionPolicyDelayIn",
        "HttpRouteFaultInjectionPolicyDelayOut": "_networkservices_39_HttpRouteFaultInjectionPolicyDelayOut",
        "ListTcpRoutesResponseIn": "_networkservices_40_ListTcpRoutesResponseIn",
        "ListTcpRoutesResponseOut": "_networkservices_41_ListTcpRoutesResponseOut",
        "HttpRouteIn": "_networkservices_42_HttpRouteIn",
        "HttpRouteOut": "_networkservices_43_HttpRouteOut",
        "HttpRouteRouteMatchIn": "_networkservices_44_HttpRouteRouteMatchIn",
        "HttpRouteRouteMatchOut": "_networkservices_45_HttpRouteRouteMatchOut",
        "ListLocationsResponseIn": "_networkservices_46_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkservices_47_ListLocationsResponseOut",
        "ServiceBindingIn": "_networkservices_48_ServiceBindingIn",
        "ServiceBindingOut": "_networkservices_49_ServiceBindingOut",
        "GrpcRouteFaultInjectionPolicyAbortIn": "_networkservices_50_GrpcRouteFaultInjectionPolicyAbortIn",
        "GrpcRouteFaultInjectionPolicyAbortOut": "_networkservices_51_GrpcRouteFaultInjectionPolicyAbortOut",
        "MeshIn": "_networkservices_52_MeshIn",
        "MeshOut": "_networkservices_53_MeshOut",
        "HttpRouteHeaderMatchIn": "_networkservices_54_HttpRouteHeaderMatchIn",
        "HttpRouteHeaderMatchOut": "_networkservices_55_HttpRouteHeaderMatchOut",
        "HttpRouteQueryParameterMatchIn": "_networkservices_56_HttpRouteQueryParameterMatchIn",
        "HttpRouteQueryParameterMatchOut": "_networkservices_57_HttpRouteQueryParameterMatchOut",
        "ExprIn": "_networkservices_58_ExprIn",
        "ExprOut": "_networkservices_59_ExprOut",
        "HttpRouteCorsPolicyIn": "_networkservices_60_HttpRouteCorsPolicyIn",
        "HttpRouteCorsPolicyOut": "_networkservices_61_HttpRouteCorsPolicyOut",
        "ListServiceBindingsResponseIn": "_networkservices_62_ListServiceBindingsResponseIn",
        "ListServiceBindingsResponseOut": "_networkservices_63_ListServiceBindingsResponseOut",
        "PolicyIn": "_networkservices_64_PolicyIn",
        "PolicyOut": "_networkservices_65_PolicyOut",
        "TlsRouteRouteRuleIn": "_networkservices_66_TlsRouteRouteRuleIn",
        "TlsRouteRouteRuleOut": "_networkservices_67_TlsRouteRouteRuleOut",
        "ListGatewaysResponseIn": "_networkservices_68_ListGatewaysResponseIn",
        "ListGatewaysResponseOut": "_networkservices_69_ListGatewaysResponseOut",
        "TlsRouteRouteDestinationIn": "_networkservices_70_TlsRouteRouteDestinationIn",
        "TlsRouteRouteDestinationOut": "_networkservices_71_TlsRouteRouteDestinationOut",
        "ListMeshesResponseIn": "_networkservices_72_ListMeshesResponseIn",
        "ListMeshesResponseOut": "_networkservices_73_ListMeshesResponseOut",
        "GrpcRouteFaultInjectionPolicyIn": "_networkservices_74_GrpcRouteFaultInjectionPolicyIn",
        "GrpcRouteFaultInjectionPolicyOut": "_networkservices_75_GrpcRouteFaultInjectionPolicyOut",
        "TcpRouteRouteMatchIn": "_networkservices_76_TcpRouteRouteMatchIn",
        "TcpRouteRouteMatchOut": "_networkservices_77_TcpRouteRouteMatchOut",
        "EndpointMatcherIn": "_networkservices_78_EndpointMatcherIn",
        "EndpointMatcherOut": "_networkservices_79_EndpointMatcherOut",
        "ListTlsRoutesResponseIn": "_networkservices_80_ListTlsRoutesResponseIn",
        "ListTlsRoutesResponseOut": "_networkservices_81_ListTlsRoutesResponseOut",
        "TestIamPermissionsResponseIn": "_networkservices_82_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkservices_83_TestIamPermissionsResponseOut",
        "EndpointMatcherMetadataLabelMatcherIn": "_networkservices_84_EndpointMatcherMetadataLabelMatcherIn",
        "EndpointMatcherMetadataLabelMatcherOut": "_networkservices_85_EndpointMatcherMetadataLabelMatcherOut",
        "HttpRouteDestinationIn": "_networkservices_86_HttpRouteDestinationIn",
        "HttpRouteDestinationOut": "_networkservices_87_HttpRouteDestinationOut",
        "HttpRouteRouteRuleIn": "_networkservices_88_HttpRouteRouteRuleIn",
        "HttpRouteRouteRuleOut": "_networkservices_89_HttpRouteRouteRuleOut",
        "StatusIn": "_networkservices_90_StatusIn",
        "StatusOut": "_networkservices_91_StatusOut",
        "GrpcRouteRouteActionIn": "_networkservices_92_GrpcRouteRouteActionIn",
        "GrpcRouteRouteActionOut": "_networkservices_93_GrpcRouteRouteActionOut",
        "GrpcRouteFaultInjectionPolicyDelayIn": "_networkservices_94_GrpcRouteFaultInjectionPolicyDelayIn",
        "GrpcRouteFaultInjectionPolicyDelayOut": "_networkservices_95_GrpcRouteFaultInjectionPolicyDelayOut",
        "TcpRouteRouteActionIn": "_networkservices_96_TcpRouteRouteActionIn",
        "TcpRouteRouteActionOut": "_networkservices_97_TcpRouteRouteActionOut",
        "ListEndpointPoliciesResponseIn": "_networkservices_98_ListEndpointPoliciesResponseIn",
        "ListEndpointPoliciesResponseOut": "_networkservices_99_ListEndpointPoliciesResponseOut",
        "HttpRouteFaultInjectionPolicyAbortIn": "_networkservices_100_HttpRouteFaultInjectionPolicyAbortIn",
        "HttpRouteFaultInjectionPolicyAbortOut": "_networkservices_101_HttpRouteFaultInjectionPolicyAbortOut",
        "GrpcRouteHeaderMatchIn": "_networkservices_102_GrpcRouteHeaderMatchIn",
        "GrpcRouteHeaderMatchOut": "_networkservices_103_GrpcRouteHeaderMatchOut",
        "OperationMetadataIn": "_networkservices_104_OperationMetadataIn",
        "OperationMetadataOut": "_networkservices_105_OperationMetadataOut",
        "GrpcRouteDestinationIn": "_networkservices_106_GrpcRouteDestinationIn",
        "GrpcRouteDestinationOut": "_networkservices_107_GrpcRouteDestinationOut",
        "TlsRouteRouteActionIn": "_networkservices_108_TlsRouteRouteActionIn",
        "TlsRouteRouteActionOut": "_networkservices_109_TlsRouteRouteActionOut",
        "AuditLogConfigIn": "_networkservices_110_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkservices_111_AuditLogConfigOut",
        "TcpRouteRouteRuleIn": "_networkservices_112_TcpRouteRouteRuleIn",
        "TcpRouteRouteRuleOut": "_networkservices_113_TcpRouteRouteRuleOut",
        "ListOperationsResponseIn": "_networkservices_114_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkservices_115_ListOperationsResponseOut",
        "GrpcRouteRouteRuleIn": "_networkservices_116_GrpcRouteRouteRuleIn",
        "GrpcRouteRouteRuleOut": "_networkservices_117_GrpcRouteRouteRuleOut",
        "GrpcRouteRouteMatchIn": "_networkservices_118_GrpcRouteRouteMatchIn",
        "GrpcRouteRouteMatchOut": "_networkservices_119_GrpcRouteRouteMatchOut",
        "EndpointPolicyIn": "_networkservices_120_EndpointPolicyIn",
        "EndpointPolicyOut": "_networkservices_121_EndpointPolicyOut",
        "HttpRouteRedirectIn": "_networkservices_122_HttpRouteRedirectIn",
        "HttpRouteRedirectOut": "_networkservices_123_HttpRouteRedirectOut",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsIn": "_networkservices_124_EndpointMatcherMetadataLabelMatcherMetadataLabelsIn",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsOut": "_networkservices_125_EndpointMatcherMetadataLabelMatcherMetadataLabelsOut",
        "HttpRouteHeaderModifierIn": "_networkservices_126_HttpRouteHeaderModifierIn",
        "HttpRouteHeaderModifierOut": "_networkservices_127_HttpRouteHeaderModifierOut",
        "HttpRouteRetryPolicyIn": "_networkservices_128_HttpRouteRetryPolicyIn",
        "HttpRouteRetryPolicyOut": "_networkservices_129_HttpRouteRetryPolicyOut",
        "TcpRouteRouteDestinationIn": "_networkservices_130_TcpRouteRouteDestinationIn",
        "TcpRouteRouteDestinationOut": "_networkservices_131_TcpRouteRouteDestinationOut",
        "HttpRouteRequestMirrorPolicyIn": "_networkservices_132_HttpRouteRequestMirrorPolicyIn",
        "HttpRouteRequestMirrorPolicyOut": "_networkservices_133_HttpRouteRequestMirrorPolicyOut",
        "OperationIn": "_networkservices_134_OperationIn",
        "OperationOut": "_networkservices_135_OperationOut",
        "TrafficPortSelectorIn": "_networkservices_136_TrafficPortSelectorIn",
        "TrafficPortSelectorOut": "_networkservices_137_TrafficPortSelectorOut",
        "CancelOperationRequestIn": "_networkservices_138_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkservices_139_CancelOperationRequestOut",
        "HttpRouteFaultInjectionPolicyIn": "_networkservices_140_HttpRouteFaultInjectionPolicyIn",
        "HttpRouteFaultInjectionPolicyOut": "_networkservices_141_HttpRouteFaultInjectionPolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GatewayIn"] = t.struct(
        {
            "network": t.string().optional(),
            "serverTlsPolicy": t.string().optional(),
            "description": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "ports": t.array(t.integer()),
            "name": t.string(),
            "addresses": t.array(t.string()).optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["GatewayIn"])
    types["GatewayOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "network": t.string().optional(),
            "serverTlsPolicy": t.string().optional(),
            "description": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "createTime": t.string().optional(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "ports": t.array(t.integer()),
            "name": t.string(),
            "addresses": t.array(t.string()).optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayOut"])
    types["HttpRouteRouteActionIn"] = t.struct(
        {
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyIn"]).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyIn"]).optional(),
            "timeout": t.string().optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectIn"]).optional(),
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteIn"]).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyIn"]
            ).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyIn"]
            ).optional(),
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationIn"])
            ).optional(),
        }
    ).named(renames["HttpRouteRouteActionIn"])
    types["HttpRouteRouteActionOut"] = t.struct(
        {
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyOut"]).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyOut"]).optional(),
            "timeout": t.string().optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectOut"]).optional(),
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteOut"]).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyOut"]
            ).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyOut"]
            ).optional(),
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteActionOut"])
    types["TlsRouteRouteMatchIn"] = t.struct(
        {
            "sniHost": t.array(t.string()).optional(),
            "alpn": t.array(t.string()).optional(),
        }
    ).named(renames["TlsRouteRouteMatchIn"])
    types["TlsRouteRouteMatchOut"] = t.struct(
        {
            "sniHost": t.array(t.string()).optional(),
            "alpn": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteMatchOut"])
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
    types["ListGrpcRoutesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "grpcRoutes": t.array(t.proxy(renames["GrpcRouteIn"])).optional(),
        }
    ).named(renames["ListGrpcRoutesResponseIn"])
    types["ListGrpcRoutesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "grpcRoutes": t.array(t.proxy(renames["GrpcRouteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGrpcRoutesResponseOut"])
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
    types["ListHttpRoutesResponseIn"] = t.struct(
        {
            "httpRoutes": t.array(t.proxy(renames["HttpRouteIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListHttpRoutesResponseIn"])
    types["ListHttpRoutesResponseOut"] = t.struct(
        {
            "httpRoutes": t.array(t.proxy(renames["HttpRouteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHttpRoutesResponseOut"])
    types["TcpRouteIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string(),
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "meshes": t.array(t.string()).optional(),
        }
    ).named(renames["TcpRouteIn"])
    types["TcpRouteOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "gateways": t.array(t.string()).optional(),
            "selfLink": t.string().optional(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleOut"])),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "meshes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TlsRouteIn"] = t.struct(
        {
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
            "name": t.string(),
            "description": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
        }
    ).named(renames["TlsRouteIn"])
    types["TlsRouteOut"] = t.struct(
        {
            "gateways": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleOut"])),
            "name": t.string(),
            "description": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteOut"])
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
    types["GrpcRouteIn"] = t.struct(
        {
            "meshes": t.array(t.string()).optional(),
            "gateways": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
            "hostnames": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GrpcRouteIn"])
    types["GrpcRouteOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "selfLink": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleOut"])),
            "hostnames": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteOut"])
    types["HttpRouteHeaderMatchIntegerRangeIn"] = t.struct(
        {"end": t.integer().optional(), "start": t.integer().optional()}
    ).named(renames["HttpRouteHeaderMatchIntegerRangeIn"])
    types["HttpRouteHeaderMatchIntegerRangeOut"] = t.struct(
        {
            "end": t.integer().optional(),
            "start": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderMatchIntegerRangeOut"])
    types["GrpcRouteRetryPolicyIn"] = t.struct(
        {
            "retryConditions": t.array(t.string()).optional(),
            "numRetries": t.integer().optional(),
        }
    ).named(renames["GrpcRouteRetryPolicyIn"])
    types["GrpcRouteRetryPolicyOut"] = t.struct(
        {
            "retryConditions": t.array(t.string()).optional(),
            "numRetries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRetryPolicyOut"])
    types["HttpRouteURLRewriteIn"] = t.struct(
        {
            "pathPrefixRewrite": t.string().optional(),
            "hostRewrite": t.string().optional(),
        }
    ).named(renames["HttpRouteURLRewriteIn"])
    types["HttpRouteURLRewriteOut"] = t.struct(
        {
            "pathPrefixRewrite": t.string().optional(),
            "hostRewrite": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteURLRewriteOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GrpcRouteMethodMatchIn"] = t.struct(
        {
            "grpcMethod": t.string(),
            "type": t.string().optional(),
            "grpcService": t.string(),
            "caseSensitive": t.boolean().optional(),
        }
    ).named(renames["GrpcRouteMethodMatchIn"])
    types["GrpcRouteMethodMatchOut"] = t.struct(
        {
            "grpcMethod": t.string(),
            "type": t.string().optional(),
            "grpcService": t.string(),
            "caseSensitive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteMethodMatchOut"])
    types["HttpRouteFaultInjectionPolicyDelayIn"] = t.struct(
        {"percentage": t.integer().optional(), "fixedDelay": t.string().optional()}
    ).named(renames["HttpRouteFaultInjectionPolicyDelayIn"])
    types["HttpRouteFaultInjectionPolicyDelayOut"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "fixedDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyDelayOut"])
    types["ListTcpRoutesResponseIn"] = t.struct(
        {
            "tcpRoutes": t.array(t.proxy(renames["TcpRouteIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTcpRoutesResponseIn"])
    types["ListTcpRoutesResponseOut"] = t.struct(
        {
            "tcpRoutes": t.array(t.proxy(renames["TcpRouteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTcpRoutesResponseOut"])
    types["HttpRouteIn"] = t.struct(
        {
            "description": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
            "name": t.string(),
            "hostnames": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HttpRouteIn"])
    types["HttpRouteOut"] = t.struct(
        {
            "description": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleOut"])),
            "selfLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "hostnames": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteOut"])
    types["HttpRouteRouteMatchIn"] = t.struct(
        {
            "ignoreCase": t.boolean().optional(),
            "regexMatch": t.string().optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchIn"])
            ).optional(),
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchIn"])).optional(),
            "prefixMatch": t.string().optional(),
            "fullPathMatch": t.string().optional(),
        }
    ).named(renames["HttpRouteRouteMatchIn"])
    types["HttpRouteRouteMatchOut"] = t.struct(
        {
            "ignoreCase": t.boolean().optional(),
            "regexMatch": t.string().optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchOut"])
            ).optional(),
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchOut"])).optional(),
            "prefixMatch": t.string().optional(),
            "fullPathMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteMatchOut"])
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
    types["ServiceBindingIn"] = t.struct(
        {
            "service": t.string(),
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ServiceBindingIn"])
    types["ServiceBindingOut"] = t.struct(
        {
            "service": t.string(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceBindingOut"])
    types["GrpcRouteFaultInjectionPolicyAbortIn"] = t.struct(
        {"percentage": t.integer().optional(), "httpStatus": t.integer().optional()}
    ).named(renames["GrpcRouteFaultInjectionPolicyAbortIn"])
    types["GrpcRouteFaultInjectionPolicyAbortOut"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "httpStatus": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyAbortOut"])
    types["MeshIn"] = t.struct(
        {
            "name": t.string(),
            "interceptionPort": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MeshIn"])
    types["MeshOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "name": t.string(),
            "interceptionPort": t.integer().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshOut"])
    types["HttpRouteHeaderMatchIn"] = t.struct(
        {
            "prefixMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "exactMatch": t.string().optional(),
            "header": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "suffixMatch": t.string().optional(),
            "invertMatch": t.boolean().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeIn"]
            ).optional(),
        }
    ).named(renames["HttpRouteHeaderMatchIn"])
    types["HttpRouteHeaderMatchOut"] = t.struct(
        {
            "prefixMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "exactMatch": t.string().optional(),
            "header": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "suffixMatch": t.string().optional(),
            "invertMatch": t.boolean().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderMatchOut"])
    types["HttpRouteQueryParameterMatchIn"] = t.struct(
        {
            "regexMatch": t.string().optional(),
            "queryParameter": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "exactMatch": t.string().optional(),
        }
    ).named(renames["HttpRouteQueryParameterMatchIn"])
    types["HttpRouteQueryParameterMatchOut"] = t.struct(
        {
            "regexMatch": t.string().optional(),
            "queryParameter": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "exactMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteQueryParameterMatchOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["HttpRouteCorsPolicyIn"] = t.struct(
        {
            "allowHeaders": t.array(t.string()).optional(),
            "allowMethods": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
            "allowCredentials": t.boolean().optional(),
            "maxAge": t.string().optional(),
            "exposeHeaders": t.array(t.string()).optional(),
        }
    ).named(renames["HttpRouteCorsPolicyIn"])
    types["HttpRouteCorsPolicyOut"] = t.struct(
        {
            "allowHeaders": t.array(t.string()).optional(),
            "allowMethods": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
            "allowCredentials": t.boolean().optional(),
            "maxAge": t.string().optional(),
            "exposeHeaders": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteCorsPolicyOut"])
    types["ListServiceBindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceBindings": t.array(t.proxy(renames["ServiceBindingIn"])).optional(),
        }
    ).named(renames["ListServiceBindingsResponseIn"])
    types["ListServiceBindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceBindings": t.array(
                t.proxy(renames["ServiceBindingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceBindingsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TlsRouteRouteRuleIn"] = t.struct(
        {
            "action": t.proxy(renames["TlsRouteRouteActionIn"]),
            "matches": t.array(t.proxy(renames["TlsRouteRouteMatchIn"])),
        }
    ).named(renames["TlsRouteRouteRuleIn"])
    types["TlsRouteRouteRuleOut"] = t.struct(
        {
            "action": t.proxy(renames["TlsRouteRouteActionOut"]),
            "matches": t.array(t.proxy(renames["TlsRouteRouteMatchOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteRuleOut"])
    types["ListGatewaysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gateways": t.array(t.proxy(renames["GatewayIn"])).optional(),
        }
    ).named(renames["ListGatewaysResponseIn"])
    types["ListGatewaysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gateways": t.array(t.proxy(renames["GatewayOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaysResponseOut"])
    types["TlsRouteRouteDestinationIn"] = t.struct(
        {"weight": t.integer().optional(), "serviceName": t.string()}
    ).named(renames["TlsRouteRouteDestinationIn"])
    types["TlsRouteRouteDestinationOut"] = t.struct(
        {
            "weight": t.integer().optional(),
            "serviceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteDestinationOut"])
    types["ListMeshesResponseIn"] = t.struct(
        {
            "meshes": t.array(t.proxy(renames["MeshIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMeshesResponseIn"])
    types["ListMeshesResponseOut"] = t.struct(
        {
            "meshes": t.array(t.proxy(renames["MeshOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMeshesResponseOut"])
    types["GrpcRouteFaultInjectionPolicyIn"] = t.struct(
        {
            "delay": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyDelayIn"]
            ).optional(),
            "abort": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyAbortIn"]
            ).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyIn"])
    types["GrpcRouteFaultInjectionPolicyOut"] = t.struct(
        {
            "delay": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyDelayOut"]
            ).optional(),
            "abort": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyAbortOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyOut"])
    types["TcpRouteRouteMatchIn"] = t.struct(
        {"port": t.string(), "address": t.string()}
    ).named(renames["TcpRouteRouteMatchIn"])
    types["TcpRouteRouteMatchOut"] = t.struct(
        {
            "port": t.string(),
            "address": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteRouteMatchOut"])
    types["EndpointMatcherIn"] = t.struct(
        {
            "metadataLabelMatcher": t.proxy(
                renames["EndpointMatcherMetadataLabelMatcherIn"]
            ).optional()
        }
    ).named(renames["EndpointMatcherIn"])
    types["EndpointMatcherOut"] = t.struct(
        {
            "metadataLabelMatcher": t.proxy(
                renames["EndpointMatcherMetadataLabelMatcherOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointMatcherOut"])
    types["ListTlsRoutesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tlsRoutes": t.array(t.proxy(renames["TlsRouteIn"])).optional(),
        }
    ).named(renames["ListTlsRoutesResponseIn"])
    types["ListTlsRoutesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tlsRoutes": t.array(t.proxy(renames["TlsRouteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTlsRoutesResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["EndpointMatcherMetadataLabelMatcherIn"] = t.struct(
        {
            "metadataLabelMatchCriteria": t.string().optional(),
            "metadataLabels": t.array(
                t.proxy(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsIn"])
            ).optional(),
        }
    ).named(renames["EndpointMatcherMetadataLabelMatcherIn"])
    types["EndpointMatcherMetadataLabelMatcherOut"] = t.struct(
        {
            "metadataLabelMatchCriteria": t.string().optional(),
            "metadataLabels": t.array(
                t.proxy(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointMatcherMetadataLabelMatcherOut"])
    types["HttpRouteDestinationIn"] = t.struct(
        {"weight": t.integer().optional(), "serviceName": t.string().optional()}
    ).named(renames["HttpRouteDestinationIn"])
    types["HttpRouteDestinationOut"] = t.struct(
        {
            "weight": t.integer().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteDestinationOut"])
    types["HttpRouteRouteRuleIn"] = t.struct(
        {
            "action": t.proxy(renames["HttpRouteRouteActionIn"]).optional(),
            "matches": t.array(t.proxy(renames["HttpRouteRouteMatchIn"])).optional(),
        }
    ).named(renames["HttpRouteRouteRuleIn"])
    types["HttpRouteRouteRuleOut"] = t.struct(
        {
            "action": t.proxy(renames["HttpRouteRouteActionOut"]).optional(),
            "matches": t.array(t.proxy(renames["HttpRouteRouteMatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteRuleOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GrpcRouteRouteActionIn"] = t.struct(
        {
            "retryPolicy": t.proxy(renames["GrpcRouteRetryPolicyIn"]).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyIn"]
            ).optional(),
            "destinations": t.array(
                t.proxy(renames["GrpcRouteDestinationIn"])
            ).optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["GrpcRouteRouteActionIn"])
    types["GrpcRouteRouteActionOut"] = t.struct(
        {
            "retryPolicy": t.proxy(renames["GrpcRouteRetryPolicyOut"]).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyOut"]
            ).optional(),
            "destinations": t.array(
                t.proxy(renames["GrpcRouteDestinationOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRouteActionOut"])
    types["GrpcRouteFaultInjectionPolicyDelayIn"] = t.struct(
        {"fixedDelay": t.string().optional(), "percentage": t.integer().optional()}
    ).named(renames["GrpcRouteFaultInjectionPolicyDelayIn"])
    types["GrpcRouteFaultInjectionPolicyDelayOut"] = t.struct(
        {
            "fixedDelay": t.string().optional(),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyDelayOut"])
    types["TcpRouteRouteActionIn"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["TcpRouteRouteDestinationIn"])
            ).optional(),
            "originalDestination": t.boolean().optional(),
        }
    ).named(renames["TcpRouteRouteActionIn"])
    types["TcpRouteRouteActionOut"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["TcpRouteRouteDestinationOut"])
            ).optional(),
            "originalDestination": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteRouteActionOut"])
    types["ListEndpointPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "endpointPolicies": t.array(
                t.proxy(renames["EndpointPolicyIn"])
            ).optional(),
        }
    ).named(renames["ListEndpointPoliciesResponseIn"])
    types["ListEndpointPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "endpointPolicies": t.array(
                t.proxy(renames["EndpointPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEndpointPoliciesResponseOut"])
    types["HttpRouteFaultInjectionPolicyAbortIn"] = t.struct(
        {"httpStatus": t.integer().optional(), "percentage": t.integer().optional()}
    ).named(renames["HttpRouteFaultInjectionPolicyAbortIn"])
    types["HttpRouteFaultInjectionPolicyAbortOut"] = t.struct(
        {
            "httpStatus": t.integer().optional(),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyAbortOut"])
    types["GrpcRouteHeaderMatchIn"] = t.struct(
        {"key": t.string(), "value": t.string(), "type": t.string().optional()}
    ).named(renames["GrpcRouteHeaderMatchIn"])
    types["GrpcRouteHeaderMatchOut"] = t.struct(
        {
            "key": t.string(),
            "value": t.string(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteHeaderMatchOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GrpcRouteDestinationIn"] = t.struct(
        {"serviceName": t.string(), "weight": t.integer().optional()}
    ).named(renames["GrpcRouteDestinationIn"])
    types["GrpcRouteDestinationOut"] = t.struct(
        {
            "serviceName": t.string(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteDestinationOut"])
    types["TlsRouteRouteActionIn"] = t.struct(
        {"destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationIn"]))}
    ).named(renames["TlsRouteRouteActionIn"])
    types["TlsRouteRouteActionOut"] = t.struct(
        {
            "destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteActionOut"])
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
    types["TcpRouteRouteRuleIn"] = t.struct(
        {
            "matches": t.array(t.proxy(renames["TcpRouteRouteMatchIn"])).optional(),
            "action": t.proxy(renames["TcpRouteRouteActionIn"]),
        }
    ).named(renames["TcpRouteRouteRuleIn"])
    types["TcpRouteRouteRuleOut"] = t.struct(
        {
            "matches": t.array(t.proxy(renames["TcpRouteRouteMatchOut"])).optional(),
            "action": t.proxy(renames["TcpRouteRouteActionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteRouteRuleOut"])
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
    types["GrpcRouteRouteRuleIn"] = t.struct(
        {
            "action": t.proxy(renames["GrpcRouteRouteActionIn"]),
            "matches": t.array(t.proxy(renames["GrpcRouteRouteMatchIn"])).optional(),
        }
    ).named(renames["GrpcRouteRouteRuleIn"])
    types["GrpcRouteRouteRuleOut"] = t.struct(
        {
            "action": t.proxy(renames["GrpcRouteRouteActionOut"]),
            "matches": t.array(t.proxy(renames["GrpcRouteRouteMatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRouteRuleOut"])
    types["GrpcRouteRouteMatchIn"] = t.struct(
        {
            "headers": t.array(t.proxy(renames["GrpcRouteHeaderMatchIn"])).optional(),
            "method": t.proxy(renames["GrpcRouteMethodMatchIn"]).optional(),
        }
    ).named(renames["GrpcRouteRouteMatchIn"])
    types["GrpcRouteRouteMatchOut"] = t.struct(
        {
            "headers": t.array(t.proxy(renames["GrpcRouteHeaderMatchOut"])).optional(),
            "method": t.proxy(renames["GrpcRouteMethodMatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRouteMatchOut"])
    types["EndpointPolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "trafficPortSelector": t.proxy(renames["TrafficPortSelectorIn"]).optional(),
            "authorizationPolicy": t.string().optional(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
            "clientTlsPolicy": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "serverTlsPolicy": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["EndpointPolicyIn"])
    types["EndpointPolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "trafficPortSelector": t.proxy(
                renames["TrafficPortSelectorOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "authorizationPolicy": t.string().optional(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherOut"]),
            "clientTlsPolicy": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "serverTlsPolicy": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointPolicyOut"])
    types["HttpRouteRedirectIn"] = t.struct(
        {
            "stripQuery": t.boolean().optional(),
            "httpsRedirect": t.boolean().optional(),
            "pathRedirect": t.string().optional(),
            "responseCode": t.string().optional(),
            "portRedirect": t.integer().optional(),
            "prefixRewrite": t.string().optional(),
            "hostRedirect": t.string().optional(),
        }
    ).named(renames["HttpRouteRedirectIn"])
    types["HttpRouteRedirectOut"] = t.struct(
        {
            "stripQuery": t.boolean().optional(),
            "httpsRedirect": t.boolean().optional(),
            "pathRedirect": t.string().optional(),
            "responseCode": t.string().optional(),
            "portRedirect": t.integer().optional(),
            "prefixRewrite": t.string().optional(),
            "hostRedirect": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRedirectOut"])
    types["EndpointMatcherMetadataLabelMatcherMetadataLabelsIn"] = t.struct(
        {"labelValue": t.string(), "labelName": t.string()}
    ).named(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsIn"])
    types["EndpointMatcherMetadataLabelMatcherMetadataLabelsOut"] = t.struct(
        {
            "labelValue": t.string(),
            "labelName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsOut"])
    types["HttpRouteHeaderModifierIn"] = t.struct(
        {
            "remove": t.array(t.string()).optional(),
            "add": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HttpRouteHeaderModifierIn"])
    types["HttpRouteHeaderModifierOut"] = t.struct(
        {
            "remove": t.array(t.string()).optional(),
            "add": t.struct({"_": t.string().optional()}).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderModifierOut"])
    types["HttpRouteRetryPolicyIn"] = t.struct(
        {
            "numRetries": t.integer().optional(),
            "retryConditions": t.array(t.string()).optional(),
            "perTryTimeout": t.string().optional(),
        }
    ).named(renames["HttpRouteRetryPolicyIn"])
    types["HttpRouteRetryPolicyOut"] = t.struct(
        {
            "numRetries": t.integer().optional(),
            "retryConditions": t.array(t.string()).optional(),
            "perTryTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRetryPolicyOut"])
    types["TcpRouteRouteDestinationIn"] = t.struct(
        {"weight": t.integer().optional(), "serviceName": t.string()}
    ).named(renames["TcpRouteRouteDestinationIn"])
    types["TcpRouteRouteDestinationOut"] = t.struct(
        {
            "weight": t.integer().optional(),
            "serviceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteRouteDestinationOut"])
    types["HttpRouteRequestMirrorPolicyIn"] = t.struct(
        {"destination": t.proxy(renames["HttpRouteDestinationIn"]).optional()}
    ).named(renames["HttpRouteRequestMirrorPolicyIn"])
    types["HttpRouteRequestMirrorPolicyOut"] = t.struct(
        {
            "destination": t.proxy(renames["HttpRouteDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRequestMirrorPolicyOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["TrafficPortSelectorIn"] = t.struct(
        {"ports": t.array(t.string()).optional()}
    ).named(renames["TrafficPortSelectorIn"])
    types["TrafficPortSelectorOut"] = t.struct(
        {
            "ports": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficPortSelectorOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["HttpRouteFaultInjectionPolicyIn"] = t.struct(
        {
            "delay": t.proxy(
                renames["HttpRouteFaultInjectionPolicyDelayIn"]
            ).optional(),
            "abort": t.proxy(
                renames["HttpRouteFaultInjectionPolicyAbortIn"]
            ).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyIn"])
    types["HttpRouteFaultInjectionPolicyOut"] = t.struct(
        {
            "delay": t.proxy(
                renames["HttpRouteFaultInjectionPolicyDelayOut"]
            ).optional(),
            "abort": t.proxy(
                renames["HttpRouteFaultInjectionPolicyAbortOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyOut"])

    functions = {}
    functions["projectsLocationsList"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsDelete"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsGetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsCreate"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsSetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsList"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceBindingsTestIamPermissions"
    ] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysGetIamPolicy"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysPatch"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysTestIamPermissions"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysGet"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysCreate"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysList"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysSetIamPolicy"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysDelete"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEdgeCacheServicesSetIamPolicy"] = networkservices.post(
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
    functions["projectsLocationsEdgeCacheServicesGetIamPolicy"] = networkservices.post(
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
        "projectsLocationsEdgeCacheServicesTestIamPermissions"
    ] = networkservices.post(
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
    functions["projectsLocationsOperationsList"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesDelete"] = networkservices.get(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTcpRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesGet"] = networkservices.get(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTcpRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesCreate"] = networkservices.get(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTcpRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesPatch"] = networkservices.get(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTcpRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesList"] = networkservices.get(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTcpRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesList"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesGet"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesCreate"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesPatch"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesDelete"] = networkservices.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesDelete"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GrpcRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesPatch"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GrpcRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesCreate"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GrpcRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesList"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GrpcRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GrpcRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesSetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesGetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesCreate"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesDelete"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesPatch"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesList"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesTestIamPermissions"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MeshOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesList"] = networkservices.get(
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
    functions["projectsLocationsEndpointPoliciesSetIamPolicy"] = networkservices.get(
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
        "projectsLocationsEndpointPoliciesTestIamPermissions"
    ] = networkservices.get(
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
    functions["projectsLocationsEndpointPoliciesDelete"] = networkservices.get(
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
    functions["projectsLocationsEndpointPoliciesPatch"] = networkservices.get(
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
    functions["projectsLocationsEndpointPoliciesCreate"] = networkservices.get(
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
    functions["projectsLocationsEndpointPoliciesGet"] = networkservices.get(
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
    functions["projectsLocationsEndpointPoliciesGetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsEdgeCacheKeysetsGetIamPolicy"] = networkservices.post(
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
    functions["projectsLocationsEdgeCacheKeysetsSetIamPolicy"] = networkservices.post(
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
        "projectsLocationsEdgeCacheKeysetsTestIamPermissions"
    ] = networkservices.post(
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
    functions["projectsLocationsEdgeCacheOriginsGetIamPolicy"] = networkservices.post(
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
        "projectsLocationsEdgeCacheOriginsTestIamPermissions"
    ] = networkservices.post(
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
    functions["projectsLocationsEdgeCacheOriginsSetIamPolicy"] = networkservices.post(
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
    functions["projectsLocationsHttpRoutesList"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesPatch"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesCreate"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesDelete"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpRouteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networkservices",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
