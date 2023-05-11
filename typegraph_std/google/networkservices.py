from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_networkservices() -> Import:
    networkservices = HTTPRuntime("https://networkservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkservices_1_ErrorResponse",
        "TlsRouteRouteMatchIn": "_networkservices_2_TlsRouteRouteMatchIn",
        "TlsRouteRouteMatchOut": "_networkservices_3_TlsRouteRouteMatchOut",
        "HttpRouteRouteActionIn": "_networkservices_4_HttpRouteRouteActionIn",
        "HttpRouteRouteActionOut": "_networkservices_5_HttpRouteRouteActionOut",
        "EmptyIn": "_networkservices_6_EmptyIn",
        "EmptyOut": "_networkservices_7_EmptyOut",
        "TcpRouteIn": "_networkservices_8_TcpRouteIn",
        "TcpRouteOut": "_networkservices_9_TcpRouteOut",
        "HttpRouteFaultInjectionPolicyAbortIn": "_networkservices_10_HttpRouteFaultInjectionPolicyAbortIn",
        "HttpRouteFaultInjectionPolicyAbortOut": "_networkservices_11_HttpRouteFaultInjectionPolicyAbortOut",
        "TcpRouteRouteDestinationIn": "_networkservices_12_TcpRouteRouteDestinationIn",
        "TcpRouteRouteDestinationOut": "_networkservices_13_TcpRouteRouteDestinationOut",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsIn": "_networkservices_14_EndpointMatcherMetadataLabelMatcherMetadataLabelsIn",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsOut": "_networkservices_15_EndpointMatcherMetadataLabelMatcherMetadataLabelsOut",
        "BindingIn": "_networkservices_16_BindingIn",
        "BindingOut": "_networkservices_17_BindingOut",
        "HttpRouteHeaderModifierIn": "_networkservices_18_HttpRouteHeaderModifierIn",
        "HttpRouteHeaderModifierOut": "_networkservices_19_HttpRouteHeaderModifierOut",
        "GatewayIn": "_networkservices_20_GatewayIn",
        "GatewayOut": "_networkservices_21_GatewayOut",
        "SetIamPolicyRequestIn": "_networkservices_22_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkservices_23_SetIamPolicyRequestOut",
        "PolicyIn": "_networkservices_24_PolicyIn",
        "PolicyOut": "_networkservices_25_PolicyOut",
        "AuditConfigIn": "_networkservices_26_AuditConfigIn",
        "AuditConfigOut": "_networkservices_27_AuditConfigOut",
        "MeshIn": "_networkservices_28_MeshIn",
        "MeshOut": "_networkservices_29_MeshOut",
        "GrpcRouteRouteRuleIn": "_networkservices_30_GrpcRouteRouteRuleIn",
        "GrpcRouteRouteRuleOut": "_networkservices_31_GrpcRouteRouteRuleOut",
        "GrpcRouteMethodMatchIn": "_networkservices_32_GrpcRouteMethodMatchIn",
        "GrpcRouteMethodMatchOut": "_networkservices_33_GrpcRouteMethodMatchOut",
        "TlsRouteIn": "_networkservices_34_TlsRouteIn",
        "TlsRouteOut": "_networkservices_35_TlsRouteOut",
        "AuditLogConfigIn": "_networkservices_36_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkservices_37_AuditLogConfigOut",
        "TlsRouteRouteActionIn": "_networkservices_38_TlsRouteRouteActionIn",
        "TlsRouteRouteActionOut": "_networkservices_39_TlsRouteRouteActionOut",
        "GrpcRouteRouteMatchIn": "_networkservices_40_GrpcRouteRouteMatchIn",
        "GrpcRouteRouteMatchOut": "_networkservices_41_GrpcRouteRouteMatchOut",
        "TcpRouteRouteMatchIn": "_networkservices_42_TcpRouteRouteMatchIn",
        "TcpRouteRouteMatchOut": "_networkservices_43_TcpRouteRouteMatchOut",
        "GrpcRouteIn": "_networkservices_44_GrpcRouteIn",
        "GrpcRouteOut": "_networkservices_45_GrpcRouteOut",
        "GrpcRouteRetryPolicyIn": "_networkservices_46_GrpcRouteRetryPolicyIn",
        "GrpcRouteRetryPolicyOut": "_networkservices_47_GrpcRouteRetryPolicyOut",
        "HttpRouteIn": "_networkservices_48_HttpRouteIn",
        "HttpRouteOut": "_networkservices_49_HttpRouteOut",
        "HttpRouteRedirectIn": "_networkservices_50_HttpRouteRedirectIn",
        "HttpRouteRedirectOut": "_networkservices_51_HttpRouteRedirectOut",
        "TestIamPermissionsRequestIn": "_networkservices_52_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkservices_53_TestIamPermissionsRequestOut",
        "ListGrpcRoutesResponseIn": "_networkservices_54_ListGrpcRoutesResponseIn",
        "ListGrpcRoutesResponseOut": "_networkservices_55_ListGrpcRoutesResponseOut",
        "LocationIn": "_networkservices_56_LocationIn",
        "LocationOut": "_networkservices_57_LocationOut",
        "GrpcRouteRouteActionIn": "_networkservices_58_GrpcRouteRouteActionIn",
        "GrpcRouteRouteActionOut": "_networkservices_59_GrpcRouteRouteActionOut",
        "HttpRouteFaultInjectionPolicyIn": "_networkservices_60_HttpRouteFaultInjectionPolicyIn",
        "HttpRouteFaultInjectionPolicyOut": "_networkservices_61_HttpRouteFaultInjectionPolicyOut",
        "ListMeshesResponseIn": "_networkservices_62_ListMeshesResponseIn",
        "ListMeshesResponseOut": "_networkservices_63_ListMeshesResponseOut",
        "GrpcRouteFaultInjectionPolicyAbortIn": "_networkservices_64_GrpcRouteFaultInjectionPolicyAbortIn",
        "GrpcRouteFaultInjectionPolicyAbortOut": "_networkservices_65_GrpcRouteFaultInjectionPolicyAbortOut",
        "ListLocationsResponseIn": "_networkservices_66_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkservices_67_ListLocationsResponseOut",
        "ListTlsRoutesResponseIn": "_networkservices_68_ListTlsRoutesResponseIn",
        "ListTlsRoutesResponseOut": "_networkservices_69_ListTlsRoutesResponseOut",
        "TlsRouteRouteDestinationIn": "_networkservices_70_TlsRouteRouteDestinationIn",
        "TlsRouteRouteDestinationOut": "_networkservices_71_TlsRouteRouteDestinationOut",
        "HttpRouteURLRewriteIn": "_networkservices_72_HttpRouteURLRewriteIn",
        "HttpRouteURLRewriteOut": "_networkservices_73_HttpRouteURLRewriteOut",
        "HttpRouteFaultInjectionPolicyDelayIn": "_networkservices_74_HttpRouteFaultInjectionPolicyDelayIn",
        "HttpRouteFaultInjectionPolicyDelayOut": "_networkservices_75_HttpRouteFaultInjectionPolicyDelayOut",
        "EndpointPolicyIn": "_networkservices_76_EndpointPolicyIn",
        "EndpointPolicyOut": "_networkservices_77_EndpointPolicyOut",
        "StatusIn": "_networkservices_78_StatusIn",
        "StatusOut": "_networkservices_79_StatusOut",
        "ListOperationsResponseIn": "_networkservices_80_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkservices_81_ListOperationsResponseOut",
        "HttpRouteRequestMirrorPolicyIn": "_networkservices_82_HttpRouteRequestMirrorPolicyIn",
        "HttpRouteRequestMirrorPolicyOut": "_networkservices_83_HttpRouteRequestMirrorPolicyOut",
        "TestIamPermissionsResponseIn": "_networkservices_84_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkservices_85_TestIamPermissionsResponseOut",
        "HttpRouteDestinationIn": "_networkservices_86_HttpRouteDestinationIn",
        "HttpRouteDestinationOut": "_networkservices_87_HttpRouteDestinationOut",
        "ListGatewaysResponseIn": "_networkservices_88_ListGatewaysResponseIn",
        "ListGatewaysResponseOut": "_networkservices_89_ListGatewaysResponseOut",
        "OperationIn": "_networkservices_90_OperationIn",
        "OperationOut": "_networkservices_91_OperationOut",
        "TcpRouteRouteRuleIn": "_networkservices_92_TcpRouteRouteRuleIn",
        "TcpRouteRouteRuleOut": "_networkservices_93_TcpRouteRouteRuleOut",
        "ListEndpointPoliciesResponseIn": "_networkservices_94_ListEndpointPoliciesResponseIn",
        "ListEndpointPoliciesResponseOut": "_networkservices_95_ListEndpointPoliciesResponseOut",
        "HttpRouteQueryParameterMatchIn": "_networkservices_96_HttpRouteQueryParameterMatchIn",
        "HttpRouteQueryParameterMatchOut": "_networkservices_97_HttpRouteQueryParameterMatchOut",
        "HttpRouteRetryPolicyIn": "_networkservices_98_HttpRouteRetryPolicyIn",
        "HttpRouteRetryPolicyOut": "_networkservices_99_HttpRouteRetryPolicyOut",
        "HttpRouteRouteRuleIn": "_networkservices_100_HttpRouteRouteRuleIn",
        "HttpRouteRouteRuleOut": "_networkservices_101_HttpRouteRouteRuleOut",
        "TlsRouteRouteRuleIn": "_networkservices_102_TlsRouteRouteRuleIn",
        "TlsRouteRouteRuleOut": "_networkservices_103_TlsRouteRouteRuleOut",
        "ListTcpRoutesResponseIn": "_networkservices_104_ListTcpRoutesResponseIn",
        "ListTcpRoutesResponseOut": "_networkservices_105_ListTcpRoutesResponseOut",
        "CancelOperationRequestIn": "_networkservices_106_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkservices_107_CancelOperationRequestOut",
        "ExprIn": "_networkservices_108_ExprIn",
        "ExprOut": "_networkservices_109_ExprOut",
        "EndpointMatcherMetadataLabelMatcherIn": "_networkservices_110_EndpointMatcherMetadataLabelMatcherIn",
        "EndpointMatcherMetadataLabelMatcherOut": "_networkservices_111_EndpointMatcherMetadataLabelMatcherOut",
        "GrpcRouteFaultInjectionPolicyIn": "_networkservices_112_GrpcRouteFaultInjectionPolicyIn",
        "GrpcRouteFaultInjectionPolicyOut": "_networkservices_113_GrpcRouteFaultInjectionPolicyOut",
        "TcpRouteRouteActionIn": "_networkservices_114_TcpRouteRouteActionIn",
        "TcpRouteRouteActionOut": "_networkservices_115_TcpRouteRouteActionOut",
        "HttpRouteCorsPolicyIn": "_networkservices_116_HttpRouteCorsPolicyIn",
        "HttpRouteCorsPolicyOut": "_networkservices_117_HttpRouteCorsPolicyOut",
        "ListHttpRoutesResponseIn": "_networkservices_118_ListHttpRoutesResponseIn",
        "ListHttpRoutesResponseOut": "_networkservices_119_ListHttpRoutesResponseOut",
        "GrpcRouteHeaderMatchIn": "_networkservices_120_GrpcRouteHeaderMatchIn",
        "GrpcRouteHeaderMatchOut": "_networkservices_121_GrpcRouteHeaderMatchOut",
        "OperationMetadataIn": "_networkservices_122_OperationMetadataIn",
        "OperationMetadataOut": "_networkservices_123_OperationMetadataOut",
        "ListServiceBindingsResponseIn": "_networkservices_124_ListServiceBindingsResponseIn",
        "ListServiceBindingsResponseOut": "_networkservices_125_ListServiceBindingsResponseOut",
        "HttpRouteRouteMatchIn": "_networkservices_126_HttpRouteRouteMatchIn",
        "HttpRouteRouteMatchOut": "_networkservices_127_HttpRouteRouteMatchOut",
        "GrpcRouteDestinationIn": "_networkservices_128_GrpcRouteDestinationIn",
        "GrpcRouteDestinationOut": "_networkservices_129_GrpcRouteDestinationOut",
        "HttpRouteHeaderMatchIntegerRangeIn": "_networkservices_130_HttpRouteHeaderMatchIntegerRangeIn",
        "HttpRouteHeaderMatchIntegerRangeOut": "_networkservices_131_HttpRouteHeaderMatchIntegerRangeOut",
        "GrpcRouteFaultInjectionPolicyDelayIn": "_networkservices_132_GrpcRouteFaultInjectionPolicyDelayIn",
        "GrpcRouteFaultInjectionPolicyDelayOut": "_networkservices_133_GrpcRouteFaultInjectionPolicyDelayOut",
        "TrafficPortSelectorIn": "_networkservices_134_TrafficPortSelectorIn",
        "TrafficPortSelectorOut": "_networkservices_135_TrafficPortSelectorOut",
        "HttpRouteHeaderMatchIn": "_networkservices_136_HttpRouteHeaderMatchIn",
        "HttpRouteHeaderMatchOut": "_networkservices_137_HttpRouteHeaderMatchOut",
        "EndpointMatcherIn": "_networkservices_138_EndpointMatcherIn",
        "EndpointMatcherOut": "_networkservices_139_EndpointMatcherOut",
        "ServiceBindingIn": "_networkservices_140_ServiceBindingIn",
        "ServiceBindingOut": "_networkservices_141_ServiceBindingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TlsRouteRouteMatchIn"] = t.struct(
        {
            "alpn": t.array(t.string()).optional(),
            "sniHost": t.array(t.string()).optional(),
        }
    ).named(renames["TlsRouteRouteMatchIn"])
    types["TlsRouteRouteMatchOut"] = t.struct(
        {
            "alpn": t.array(t.string()).optional(),
            "sniHost": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteMatchOut"])
    types["HttpRouteRouteActionIn"] = t.struct(
        {
            "timeout": t.string().optional(),
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationIn"])
            ).optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectIn"]).optional(),
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyIn"]).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteIn"]).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyIn"]).optional(),
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyIn"]
            ).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyIn"]
            ).optional(),
        }
    ).named(renames["HttpRouteRouteActionIn"])
    types["HttpRouteRouteActionOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationOut"])
            ).optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectOut"]).optional(),
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyOut"]).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteOut"]).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyOut"]).optional(),
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyOut"]
            ).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteActionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TcpRouteIn"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
            "gateways": t.array(t.string()).optional(),
            "meshes": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TcpRouteIn"])
    types["TcpRouteOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleOut"])),
            "updateTime": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "meshes": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteOut"])
    types["HttpRouteFaultInjectionPolicyAbortIn"] = t.struct(
        {"percentage": t.integer().optional(), "httpStatus": t.integer().optional()}
    ).named(renames["HttpRouteFaultInjectionPolicyAbortIn"])
    types["HttpRouteFaultInjectionPolicyAbortOut"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "httpStatus": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyAbortOut"])
    types["TcpRouteRouteDestinationIn"] = t.struct(
        {"serviceName": t.string(), "weight": t.integer().optional()}
    ).named(renames["TcpRouteRouteDestinationIn"])
    types["TcpRouteRouteDestinationOut"] = t.struct(
        {
            "serviceName": t.string(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteRouteDestinationOut"])
    types["EndpointMatcherMetadataLabelMatcherMetadataLabelsIn"] = t.struct(
        {"labelName": t.string(), "labelValue": t.string()}
    ).named(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsIn"])
    types["EndpointMatcherMetadataLabelMatcherMetadataLabelsOut"] = t.struct(
        {
            "labelName": t.string(),
            "labelValue": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsOut"])
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
    types["HttpRouteHeaderModifierIn"] = t.struct(
        {
            "set": t.struct({"_": t.string().optional()}).optional(),
            "add": t.struct({"_": t.string().optional()}).optional(),
            "remove": t.array(t.string()).optional(),
        }
    ).named(renames["HttpRouteHeaderModifierIn"])
    types["HttpRouteHeaderModifierOut"] = t.struct(
        {
            "set": t.struct({"_": t.string().optional()}).optional(),
            "add": t.struct({"_": t.string().optional()}).optional(),
            "remove": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderModifierOut"])
    types["GatewayIn"] = t.struct(
        {
            "addresses": t.array(t.string()).optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "ports": t.array(t.integer()),
            "type": t.string().optional(),
            "serverTlsPolicy": t.string().optional(),
            "scope": t.string().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GatewayIn"])
    types["GatewayOut"] = t.struct(
        {
            "addresses": t.array(t.string()).optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "ports": t.array(t.integer()),
            "type": t.string().optional(),
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "createTime": t.string().optional(),
            "serverTlsPolicy": t.string().optional(),
            "scope": t.string().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
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
    types["MeshIn"] = t.struct(
        {
            "interceptionPort": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["MeshIn"])
    types["MeshOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "interceptionPort": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshOut"])
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
    types["GrpcRouteMethodMatchIn"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "grpcMethod": t.string(),
            "grpcService": t.string(),
            "type": t.string().optional(),
        }
    ).named(renames["GrpcRouteMethodMatchIn"])
    types["GrpcRouteMethodMatchOut"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "grpcMethod": t.string(),
            "grpcService": t.string(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteMethodMatchOut"])
    types["TlsRouteIn"] = t.struct(
        {
            "gateways": t.array(t.string()).optional(),
            "name": t.string(),
            "meshes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
        }
    ).named(renames["TlsRouteIn"])
    types["TlsRouteOut"] = t.struct(
        {
            "gateways": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "meshes": t.array(t.string()).optional(),
            "selfLink": t.string().optional(),
            "description": t.string().optional(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleOut"])),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteOut"])
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
    types["TlsRouteRouteActionIn"] = t.struct(
        {"destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationIn"]))}
    ).named(renames["TlsRouteRouteActionIn"])
    types["TlsRouteRouteActionOut"] = t.struct(
        {
            "destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteActionOut"])
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
    types["GrpcRouteIn"] = t.struct(
        {
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "meshes": t.array(t.string()).optional(),
            "hostnames": t.array(t.string()),
            "name": t.string(),
        }
    ).named(renames["GrpcRouteIn"])
    types["GrpcRouteOut"] = t.struct(
        {
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleOut"])),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "selfLink": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "hostnames": t.array(t.string()),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteOut"])
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
    types["HttpRouteIn"] = t.struct(
        {
            "gateways": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "meshes": t.array(t.string()).optional(),
            "name": t.string(),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
            "hostnames": t.array(t.string()),
        }
    ).named(renames["HttpRouteIn"])
    types["HttpRouteOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "name": t.string(),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleOut"])),
            "hostnames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteOut"])
    types["HttpRouteRedirectIn"] = t.struct(
        {
            "hostRedirect": t.string().optional(),
            "pathRedirect": t.string().optional(),
            "stripQuery": t.boolean().optional(),
            "responseCode": t.string().optional(),
            "prefixRewrite": t.string().optional(),
            "httpsRedirect": t.boolean().optional(),
            "portRedirect": t.integer().optional(),
        }
    ).named(renames["HttpRouteRedirectIn"])
    types["HttpRouteRedirectOut"] = t.struct(
        {
            "hostRedirect": t.string().optional(),
            "pathRedirect": t.string().optional(),
            "stripQuery": t.boolean().optional(),
            "responseCode": t.string().optional(),
            "prefixRewrite": t.string().optional(),
            "httpsRedirect": t.boolean().optional(),
            "portRedirect": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRedirectOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GrpcRouteRouteActionIn"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["GrpcRouteDestinationIn"])
            ).optional(),
            "timeout": t.string().optional(),
            "retryPolicy": t.proxy(renames["GrpcRouteRetryPolicyIn"]).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyIn"]
            ).optional(),
        }
    ).named(renames["GrpcRouteRouteActionIn"])
    types["GrpcRouteRouteActionOut"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["GrpcRouteDestinationOut"])
            ).optional(),
            "timeout": t.string().optional(),
            "retryPolicy": t.proxy(renames["GrpcRouteRetryPolicyOut"]).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRouteActionOut"])
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
    types["GrpcRouteFaultInjectionPolicyAbortIn"] = t.struct(
        {"httpStatus": t.integer().optional(), "percentage": t.integer().optional()}
    ).named(renames["GrpcRouteFaultInjectionPolicyAbortIn"])
    types["GrpcRouteFaultInjectionPolicyAbortOut"] = t.struct(
        {
            "httpStatus": t.integer().optional(),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyAbortOut"])
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
    types["ListTlsRoutesResponseIn"] = t.struct(
        {
            "tlsRoutes": t.array(t.proxy(renames["TlsRouteIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTlsRoutesResponseIn"])
    types["ListTlsRoutesResponseOut"] = t.struct(
        {
            "tlsRoutes": t.array(t.proxy(renames["TlsRouteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTlsRoutesResponseOut"])
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
    types["EndpointPolicyIn"] = t.struct(
        {
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trafficPortSelector": t.proxy(renames["TrafficPortSelectorIn"]).optional(),
            "clientTlsPolicy": t.string().optional(),
            "description": t.string().optional(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
            "authorizationPolicy": t.string().optional(),
            "name": t.string(),
            "serverTlsPolicy": t.string().optional(),
        }
    ).named(renames["EndpointPolicyIn"])
    types["EndpointPolicyOut"] = t.struct(
        {
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trafficPortSelector": t.proxy(
                renames["TrafficPortSelectorOut"]
            ).optional(),
            "clientTlsPolicy": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherOut"]),
            "createTime": t.string().optional(),
            "authorizationPolicy": t.string().optional(),
            "name": t.string(),
            "serverTlsPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointPolicyOut"])
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
    types["HttpRouteRequestMirrorPolicyIn"] = t.struct(
        {"destination": t.proxy(renames["HttpRouteDestinationIn"]).optional()}
    ).named(renames["HttpRouteRequestMirrorPolicyIn"])
    types["HttpRouteRequestMirrorPolicyOut"] = t.struct(
        {
            "destination": t.proxy(renames["HttpRouteDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRequestMirrorPolicyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["HttpRouteDestinationIn"] = t.struct(
        {"serviceName": t.string().optional(), "weight": t.integer().optional()}
    ).named(renames["HttpRouteDestinationIn"])
    types["HttpRouteDestinationOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "weight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteDestinationOut"])
    types["ListGatewaysResponseIn"] = t.struct(
        {
            "gateways": t.array(t.proxy(renames["GatewayIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGatewaysResponseIn"])
    types["ListGatewaysResponseOut"] = t.struct(
        {
            "gateways": t.array(t.proxy(renames["GatewayOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaysResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["TcpRouteRouteRuleIn"] = t.struct(
        {
            "action": t.proxy(renames["TcpRouteRouteActionIn"]),
            "matches": t.array(t.proxy(renames["TcpRouteRouteMatchIn"])).optional(),
        }
    ).named(renames["TcpRouteRouteRuleIn"])
    types["TcpRouteRouteRuleOut"] = t.struct(
        {
            "action": t.proxy(renames["TcpRouteRouteActionOut"]),
            "matches": t.array(t.proxy(renames["TcpRouteRouteMatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteRouteRuleOut"])
    types["ListEndpointPoliciesResponseIn"] = t.struct(
        {
            "endpointPolicies": t.array(
                t.proxy(renames["EndpointPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEndpointPoliciesResponseIn"])
    types["ListEndpointPoliciesResponseOut"] = t.struct(
        {
            "endpointPolicies": t.array(
                t.proxy(renames["EndpointPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEndpointPoliciesResponseOut"])
    types["HttpRouteQueryParameterMatchIn"] = t.struct(
        {
            "regexMatch": t.string().optional(),
            "exactMatch": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "queryParameter": t.string().optional(),
        }
    ).named(renames["HttpRouteQueryParameterMatchIn"])
    types["HttpRouteQueryParameterMatchOut"] = t.struct(
        {
            "regexMatch": t.string().optional(),
            "exactMatch": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "queryParameter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteQueryParameterMatchOut"])
    types["HttpRouteRetryPolicyIn"] = t.struct(
        {
            "retryConditions": t.array(t.string()).optional(),
            "numRetries": t.integer().optional(),
            "perTryTimeout": t.string().optional(),
        }
    ).named(renames["HttpRouteRetryPolicyIn"])
    types["HttpRouteRetryPolicyOut"] = t.struct(
        {
            "retryConditions": t.array(t.string()).optional(),
            "numRetries": t.integer().optional(),
            "perTryTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRetryPolicyOut"])
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
    types["TlsRouteRouteRuleIn"] = t.struct(
        {
            "matches": t.array(t.proxy(renames["TlsRouteRouteMatchIn"])),
            "action": t.proxy(renames["TlsRouteRouteActionIn"]),
        }
    ).named(renames["TlsRouteRouteRuleIn"])
    types["TlsRouteRouteRuleOut"] = t.struct(
        {
            "matches": t.array(t.proxy(renames["TlsRouteRouteMatchOut"])),
            "action": t.proxy(renames["TlsRouteRouteActionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteRuleOut"])
    types["ListTcpRoutesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tcpRoutes": t.array(t.proxy(renames["TcpRouteIn"])).optional(),
        }
    ).named(renames["ListTcpRoutesResponseIn"])
    types["ListTcpRoutesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tcpRoutes": t.array(t.proxy(renames["TcpRouteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTcpRoutesResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EndpointMatcherMetadataLabelMatcherIn"] = t.struct(
        {
            "metadataLabels": t.array(
                t.proxy(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsIn"])
            ).optional(),
            "metadataLabelMatchCriteria": t.string().optional(),
        }
    ).named(renames["EndpointMatcherMetadataLabelMatcherIn"])
    types["EndpointMatcherMetadataLabelMatcherOut"] = t.struct(
        {
            "metadataLabels": t.array(
                t.proxy(renames["EndpointMatcherMetadataLabelMatcherMetadataLabelsOut"])
            ).optional(),
            "metadataLabelMatchCriteria": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointMatcherMetadataLabelMatcherOut"])
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
    types["HttpRouteCorsPolicyIn"] = t.struct(
        {
            "allowMethods": t.array(t.string()).optional(),
            "maxAge": t.string().optional(),
            "allowCredentials": t.boolean().optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowHeaders": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "exposeHeaders": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
        }
    ).named(renames["HttpRouteCorsPolicyIn"])
    types["HttpRouteCorsPolicyOut"] = t.struct(
        {
            "allowMethods": t.array(t.string()).optional(),
            "maxAge": t.string().optional(),
            "allowCredentials": t.boolean().optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowHeaders": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "exposeHeaders": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteCorsPolicyOut"])
    types["ListHttpRoutesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "httpRoutes": t.array(t.proxy(renames["HttpRouteIn"])).optional(),
        }
    ).named(renames["ListHttpRoutesResponseIn"])
    types["ListHttpRoutesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "httpRoutes": t.array(t.proxy(renames["HttpRouteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHttpRoutesResponseOut"])
    types["GrpcRouteHeaderMatchIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string(), "key": t.string()}
    ).named(renames["GrpcRouteHeaderMatchIn"])
    types["GrpcRouteHeaderMatchOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string(),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteHeaderMatchOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListServiceBindingsResponseIn"] = t.struct(
        {
            "serviceBindings": t.array(t.proxy(renames["ServiceBindingIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServiceBindingsResponseIn"])
    types["ListServiceBindingsResponseOut"] = t.struct(
        {
            "serviceBindings": t.array(
                t.proxy(renames["ServiceBindingOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceBindingsResponseOut"])
    types["HttpRouteRouteMatchIn"] = t.struct(
        {
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchIn"])).optional(),
            "prefixMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchIn"])
            ).optional(),
            "fullPathMatch": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
        }
    ).named(renames["HttpRouteRouteMatchIn"])
    types["HttpRouteRouteMatchOut"] = t.struct(
        {
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchOut"])).optional(),
            "prefixMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchOut"])
            ).optional(),
            "fullPathMatch": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteMatchOut"])
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
    types["GrpcRouteFaultInjectionPolicyDelayIn"] = t.struct(
        {"percentage": t.integer().optional(), "fixedDelay": t.string().optional()}
    ).named(renames["GrpcRouteFaultInjectionPolicyDelayIn"])
    types["GrpcRouteFaultInjectionPolicyDelayOut"] = t.struct(
        {
            "percentage": t.integer().optional(),
            "fixedDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyDelayOut"])
    types["TrafficPortSelectorIn"] = t.struct(
        {"ports": t.array(t.string()).optional()}
    ).named(renames["TrafficPortSelectorIn"])
    types["TrafficPortSelectorOut"] = t.struct(
        {
            "ports": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficPortSelectorOut"])
    types["HttpRouteHeaderMatchIn"] = t.struct(
        {
            "header": t.string().optional(),
            "regexMatch": t.string().optional(),
            "prefixMatch": t.string().optional(),
            "suffixMatch": t.string().optional(),
            "invertMatch": t.boolean().optional(),
            "presentMatch": t.boolean().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeIn"]
            ).optional(),
            "exactMatch": t.string().optional(),
        }
    ).named(renames["HttpRouteHeaderMatchIn"])
    types["HttpRouteHeaderMatchOut"] = t.struct(
        {
            "header": t.string().optional(),
            "regexMatch": t.string().optional(),
            "prefixMatch": t.string().optional(),
            "suffixMatch": t.string().optional(),
            "invertMatch": t.boolean().optional(),
            "presentMatch": t.boolean().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeOut"]
            ).optional(),
            "exactMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderMatchOut"])
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
    types["ServiceBindingIn"] = t.struct(
        {
            "description": t.string().optional(),
            "service": t.string(),
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ServiceBindingIn"])
    types["ServiceBindingOut"] = t.struct(
        {
            "description": t.string().optional(),
            "service": t.string(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceBindingOut"])

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
    functions["projectsLocationsEdgeCacheKeysetsGetIamPolicy"] = networkservices.post(
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
    functions[
        "projectsLocationsEdgeCacheKeysetsTestIamPermissions"
    ] = networkservices.post(
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
    functions["projectsLocationsEdgeCacheKeysetsSetIamPolicy"] = networkservices.post(
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
    functions["projectsLocationsTlsRoutesDelete"] = networkservices.post(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "tlsRouteId": t.string(),
                "parent": t.string(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesList"] = networkservices.post(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "tlsRouteId": t.string(),
                "parent": t.string(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesGet"] = networkservices.post(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "tlsRouteId": t.string(),
                "parent": t.string(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesPatch"] = networkservices.post(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "tlsRouteId": t.string(),
                "parent": t.string(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesCreate"] = networkservices.post(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "tlsRouteId": t.string(),
                "parent": t.string(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesPatch"] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesDelete"] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesGet"] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesSetIamPolicy"] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesList"] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesGetIamPolicy"] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEndpointPoliciesTestIamPermissions"
    ] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesCreate"] = networkservices.post(
        "v1/{parent}/endpointPolicies",
        t.struct(
            {
                "parent": t.string(),
                "endpointPolicyId": t.string(),
                "type": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "authorizationPolicy": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsGatewaysSetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysDelete"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysGetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysTestIamPermissions"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysCreate"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysPatch"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysList"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsGetIamPolicy"] = networkservices.get(
        "v1/{parent}/serviceBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsSetIamPolicy"] = networkservices.get(
        "v1/{parent}/serviceBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsGet"] = networkservices.get(
        "v1/{parent}/serviceBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServiceBindingsTestIamPermissions"
    ] = networkservices.get(
        "v1/{parent}/serviceBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsCreate"] = networkservices.get(
        "v1/{parent}/serviceBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsDelete"] = networkservices.get(
        "v1/{parent}/serviceBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServiceBindingsList"] = networkservices.get(
        "v1/{parent}/serviceBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceBindingsResponseOut"]),
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
    functions["projectsLocationsHttpRoutesList"] = networkservices.get(
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
    functions["projectsLocationsTcpRoutesPatch"] = networkservices.post(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "tcpRouteId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "gateways": t.array(t.string()).optional(),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesDelete"] = networkservices.post(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "tcpRouteId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "gateways": t.array(t.string()).optional(),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesGet"] = networkservices.post(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "tcpRouteId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "gateways": t.array(t.string()).optional(),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesList"] = networkservices.post(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "tcpRouteId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "gateways": t.array(t.string()).optional(),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTcpRoutesCreate"] = networkservices.post(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "tcpRouteId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "gateways": t.array(t.string()).optional(),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsGrpcRoutesDelete"] = networkservices.get(
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
    functions["projectsLocationsMeshesTestIamPermissions"] = networkservices.get(
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
    functions["projectsLocationsMeshesSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsMeshesList"] = networkservices.get(
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
    functions["projectsLocationsEdgeCacheServicesSetIamPolicy"] = networkservices.get(
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
        "projectsLocationsEdgeCacheServicesTestIamPermissions"
    ] = networkservices.get(
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
    functions["projectsLocationsEdgeCacheServicesGetIamPolicy"] = networkservices.get(
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
        "projectsLocationsEdgeCacheOriginsTestIamPermissions"
    ] = networkservices.post(
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
    functions["projectsLocationsEdgeCacheOriginsGetIamPolicy"] = networkservices.post(
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
    functions["projectsLocationsEdgeCacheOriginsSetIamPolicy"] = networkservices.post(
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

    return Import(
        importer="networkservices", renames=renames, types=types, functions=functions
    )
