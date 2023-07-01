from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_networkservices():
    networkservices = HTTPRuntime("https://networkservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkservices_1_ErrorResponse",
        "ListOperationsResponseIn": "_networkservices_2_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkservices_3_ListOperationsResponseOut",
        "PolicyIn": "_networkservices_4_PolicyIn",
        "PolicyOut": "_networkservices_5_PolicyOut",
        "ListEndpointPoliciesResponseIn": "_networkservices_6_ListEndpointPoliciesResponseIn",
        "ListEndpointPoliciesResponseOut": "_networkservices_7_ListEndpointPoliciesResponseOut",
        "ListTlsRoutesResponseIn": "_networkservices_8_ListTlsRoutesResponseIn",
        "ListTlsRoutesResponseOut": "_networkservices_9_ListTlsRoutesResponseOut",
        "TlsRouteRouteActionIn": "_networkservices_10_TlsRouteRouteActionIn",
        "TlsRouteRouteActionOut": "_networkservices_11_TlsRouteRouteActionOut",
        "TlsRouteRouteDestinationIn": "_networkservices_12_TlsRouteRouteDestinationIn",
        "TlsRouteRouteDestinationOut": "_networkservices_13_TlsRouteRouteDestinationOut",
        "GrpcRouteDestinationIn": "_networkservices_14_GrpcRouteDestinationIn",
        "GrpcRouteDestinationOut": "_networkservices_15_GrpcRouteDestinationOut",
        "HttpRouteURLRewriteIn": "_networkservices_16_HttpRouteURLRewriteIn",
        "HttpRouteURLRewriteOut": "_networkservices_17_HttpRouteURLRewriteOut",
        "HttpRouteRedirectIn": "_networkservices_18_HttpRouteRedirectIn",
        "HttpRouteRedirectOut": "_networkservices_19_HttpRouteRedirectOut",
        "TcpRouteRouteRuleIn": "_networkservices_20_TcpRouteRouteRuleIn",
        "TcpRouteRouteRuleOut": "_networkservices_21_TcpRouteRouteRuleOut",
        "ListHttpRoutesResponseIn": "_networkservices_22_ListHttpRoutesResponseIn",
        "ListHttpRoutesResponseOut": "_networkservices_23_ListHttpRoutesResponseOut",
        "TcpRouteIn": "_networkservices_24_TcpRouteIn",
        "TcpRouteOut": "_networkservices_25_TcpRouteOut",
        "AuditConfigIn": "_networkservices_26_AuditConfigIn",
        "AuditConfigOut": "_networkservices_27_AuditConfigOut",
        "TcpRouteRouteActionIn": "_networkservices_28_TcpRouteRouteActionIn",
        "TcpRouteRouteActionOut": "_networkservices_29_TcpRouteRouteActionOut",
        "TcpRouteRouteDestinationIn": "_networkservices_30_TcpRouteRouteDestinationIn",
        "TcpRouteRouteDestinationOut": "_networkservices_31_TcpRouteRouteDestinationOut",
        "GrpcRouteFaultInjectionPolicyAbortIn": "_networkservices_32_GrpcRouteFaultInjectionPolicyAbortIn",
        "GrpcRouteFaultInjectionPolicyAbortOut": "_networkservices_33_GrpcRouteFaultInjectionPolicyAbortOut",
        "ServiceBindingIn": "_networkservices_34_ServiceBindingIn",
        "ServiceBindingOut": "_networkservices_35_ServiceBindingOut",
        "CancelOperationRequestIn": "_networkservices_36_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkservices_37_CancelOperationRequestOut",
        "MeshIn": "_networkservices_38_MeshIn",
        "MeshOut": "_networkservices_39_MeshOut",
        "GrpcRouteRouteMatchIn": "_networkservices_40_GrpcRouteRouteMatchIn",
        "GrpcRouteRouteMatchOut": "_networkservices_41_GrpcRouteRouteMatchOut",
        "HttpRouteFaultInjectionPolicyDelayIn": "_networkservices_42_HttpRouteFaultInjectionPolicyDelayIn",
        "HttpRouteFaultInjectionPolicyDelayOut": "_networkservices_43_HttpRouteFaultInjectionPolicyDelayOut",
        "HttpRouteRouteRuleIn": "_networkservices_44_HttpRouteRouteRuleIn",
        "HttpRouteRouteRuleOut": "_networkservices_45_HttpRouteRouteRuleOut",
        "HttpRouteCorsPolicyIn": "_networkservices_46_HttpRouteCorsPolicyIn",
        "HttpRouteCorsPolicyOut": "_networkservices_47_HttpRouteCorsPolicyOut",
        "GrpcRouteRouteActionIn": "_networkservices_48_GrpcRouteRouteActionIn",
        "GrpcRouteRouteActionOut": "_networkservices_49_GrpcRouteRouteActionOut",
        "EndpointMatcherIn": "_networkservices_50_EndpointMatcherIn",
        "EndpointMatcherOut": "_networkservices_51_EndpointMatcherOut",
        "TlsRouteRouteMatchIn": "_networkservices_52_TlsRouteRouteMatchIn",
        "TlsRouteRouteMatchOut": "_networkservices_53_TlsRouteRouteMatchOut",
        "GrpcRouteFaultInjectionPolicyIn": "_networkservices_54_GrpcRouteFaultInjectionPolicyIn",
        "GrpcRouteFaultInjectionPolicyOut": "_networkservices_55_GrpcRouteFaultInjectionPolicyOut",
        "TlsRouteRouteRuleIn": "_networkservices_56_TlsRouteRouteRuleIn",
        "TlsRouteRouteRuleOut": "_networkservices_57_TlsRouteRouteRuleOut",
        "GrpcRouteHeaderMatchIn": "_networkservices_58_GrpcRouteHeaderMatchIn",
        "GrpcRouteHeaderMatchOut": "_networkservices_59_GrpcRouteHeaderMatchOut",
        "HttpRouteHeaderMatchIntegerRangeIn": "_networkservices_60_HttpRouteHeaderMatchIntegerRangeIn",
        "HttpRouteHeaderMatchIntegerRangeOut": "_networkservices_61_HttpRouteHeaderMatchIntegerRangeOut",
        "GrpcRouteFaultInjectionPolicyDelayIn": "_networkservices_62_GrpcRouteFaultInjectionPolicyDelayIn",
        "GrpcRouteFaultInjectionPolicyDelayOut": "_networkservices_63_GrpcRouteFaultInjectionPolicyDelayOut",
        "ListLocationsResponseIn": "_networkservices_64_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkservices_65_ListLocationsResponseOut",
        "OperationIn": "_networkservices_66_OperationIn",
        "OperationOut": "_networkservices_67_OperationOut",
        "ListMeshesResponseIn": "_networkservices_68_ListMeshesResponseIn",
        "ListMeshesResponseOut": "_networkservices_69_ListMeshesResponseOut",
        "GrpcRouteIn": "_networkservices_70_GrpcRouteIn",
        "GrpcRouteOut": "_networkservices_71_GrpcRouteOut",
        "GrpcRouteRetryPolicyIn": "_networkservices_72_GrpcRouteRetryPolicyIn",
        "GrpcRouteRetryPolicyOut": "_networkservices_73_GrpcRouteRetryPolicyOut",
        "GrpcRouteRouteRuleIn": "_networkservices_74_GrpcRouteRouteRuleIn",
        "GrpcRouteRouteRuleOut": "_networkservices_75_GrpcRouteRouteRuleOut",
        "GrpcRouteMethodMatchIn": "_networkservices_76_GrpcRouteMethodMatchIn",
        "GrpcRouteMethodMatchOut": "_networkservices_77_GrpcRouteMethodMatchOut",
        "ListGrpcRoutesResponseIn": "_networkservices_78_ListGrpcRoutesResponseIn",
        "ListGrpcRoutesResponseOut": "_networkservices_79_ListGrpcRoutesResponseOut",
        "TestIamPermissionsRequestIn": "_networkservices_80_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkservices_81_TestIamPermissionsRequestOut",
        "HttpRouteDestinationIn": "_networkservices_82_HttpRouteDestinationIn",
        "HttpRouteDestinationOut": "_networkservices_83_HttpRouteDestinationOut",
        "SetIamPolicyRequestIn": "_networkservices_84_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkservices_85_SetIamPolicyRequestOut",
        "LocationIn": "_networkservices_86_LocationIn",
        "LocationOut": "_networkservices_87_LocationOut",
        "HttpRouteFaultInjectionPolicyIn": "_networkservices_88_HttpRouteFaultInjectionPolicyIn",
        "HttpRouteFaultInjectionPolicyOut": "_networkservices_89_HttpRouteFaultInjectionPolicyOut",
        "TcpRouteRouteMatchIn": "_networkservices_90_TcpRouteRouteMatchIn",
        "TcpRouteRouteMatchOut": "_networkservices_91_TcpRouteRouteMatchOut",
        "HttpRouteHeaderMatchIn": "_networkservices_92_HttpRouteHeaderMatchIn",
        "HttpRouteHeaderMatchOut": "_networkservices_93_HttpRouteHeaderMatchOut",
        "TestIamPermissionsResponseIn": "_networkservices_94_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkservices_95_TestIamPermissionsResponseOut",
        "OperationMetadataIn": "_networkservices_96_OperationMetadataIn",
        "OperationMetadataOut": "_networkservices_97_OperationMetadataOut",
        "StatusIn": "_networkservices_98_StatusIn",
        "StatusOut": "_networkservices_99_StatusOut",
        "EmptyIn": "_networkservices_100_EmptyIn",
        "EmptyOut": "_networkservices_101_EmptyOut",
        "EndpointMatcherMetadataLabelMatcherIn": "_networkservices_102_EndpointMatcherMetadataLabelMatcherIn",
        "EndpointMatcherMetadataLabelMatcherOut": "_networkservices_103_EndpointMatcherMetadataLabelMatcherOut",
        "ListTcpRoutesResponseIn": "_networkservices_104_ListTcpRoutesResponseIn",
        "ListTcpRoutesResponseOut": "_networkservices_105_ListTcpRoutesResponseOut",
        "GatewayIn": "_networkservices_106_GatewayIn",
        "GatewayOut": "_networkservices_107_GatewayOut",
        "ListServiceBindingsResponseIn": "_networkservices_108_ListServiceBindingsResponseIn",
        "ListServiceBindingsResponseOut": "_networkservices_109_ListServiceBindingsResponseOut",
        "HttpRouteRetryPolicyIn": "_networkservices_110_HttpRouteRetryPolicyIn",
        "HttpRouteRetryPolicyOut": "_networkservices_111_HttpRouteRetryPolicyOut",
        "TrafficPortSelectorIn": "_networkservices_112_TrafficPortSelectorIn",
        "TrafficPortSelectorOut": "_networkservices_113_TrafficPortSelectorOut",
        "ListGatewaysResponseIn": "_networkservices_114_ListGatewaysResponseIn",
        "ListGatewaysResponseOut": "_networkservices_115_ListGatewaysResponseOut",
        "EndpointPolicyIn": "_networkservices_116_EndpointPolicyIn",
        "EndpointPolicyOut": "_networkservices_117_EndpointPolicyOut",
        "AuditLogConfigIn": "_networkservices_118_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkservices_119_AuditLogConfigOut",
        "BindingIn": "_networkservices_120_BindingIn",
        "BindingOut": "_networkservices_121_BindingOut",
        "HttpRouteRequestMirrorPolicyIn": "_networkservices_122_HttpRouteRequestMirrorPolicyIn",
        "HttpRouteRequestMirrorPolicyOut": "_networkservices_123_HttpRouteRequestMirrorPolicyOut",
        "HttpRouteRouteActionIn": "_networkservices_124_HttpRouteRouteActionIn",
        "HttpRouteRouteActionOut": "_networkservices_125_HttpRouteRouteActionOut",
        "HttpRouteIn": "_networkservices_126_HttpRouteIn",
        "HttpRouteOut": "_networkservices_127_HttpRouteOut",
        "HttpRouteHeaderModifierIn": "_networkservices_128_HttpRouteHeaderModifierIn",
        "HttpRouteHeaderModifierOut": "_networkservices_129_HttpRouteHeaderModifierOut",
        "TlsRouteIn": "_networkservices_130_TlsRouteIn",
        "TlsRouteOut": "_networkservices_131_TlsRouteOut",
        "HttpRouteQueryParameterMatchIn": "_networkservices_132_HttpRouteQueryParameterMatchIn",
        "HttpRouteQueryParameterMatchOut": "_networkservices_133_HttpRouteQueryParameterMatchOut",
        "HttpRouteRouteMatchIn": "_networkservices_134_HttpRouteRouteMatchIn",
        "HttpRouteRouteMatchOut": "_networkservices_135_HttpRouteRouteMatchOut",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsIn": "_networkservices_136_EndpointMatcherMetadataLabelMatcherMetadataLabelsIn",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsOut": "_networkservices_137_EndpointMatcherMetadataLabelMatcherMetadataLabelsOut",
        "ExprIn": "_networkservices_138_ExprIn",
        "ExprOut": "_networkservices_139_ExprOut",
        "HttpRouteFaultInjectionPolicyAbortIn": "_networkservices_140_HttpRouteFaultInjectionPolicyAbortIn",
        "HttpRouteFaultInjectionPolicyAbortOut": "_networkservices_141_HttpRouteFaultInjectionPolicyAbortOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TlsRouteRouteActionIn"] = t.struct(
        {"destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationIn"]))}
    ).named(renames["TlsRouteRouteActionIn"])
    types["TlsRouteRouteActionOut"] = t.struct(
        {
            "destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteActionOut"])
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
    types["HttpRouteRedirectIn"] = t.struct(
        {
            "httpsRedirect": t.boolean().optional(),
            "stripQuery": t.boolean().optional(),
            "hostRedirect": t.string().optional(),
            "pathRedirect": t.string().optional(),
            "portRedirect": t.integer().optional(),
            "responseCode": t.string().optional(),
            "prefixRewrite": t.string().optional(),
        }
    ).named(renames["HttpRouteRedirectIn"])
    types["HttpRouteRedirectOut"] = t.struct(
        {
            "httpsRedirect": t.boolean().optional(),
            "stripQuery": t.boolean().optional(),
            "hostRedirect": t.string().optional(),
            "pathRedirect": t.string().optional(),
            "portRedirect": t.integer().optional(),
            "responseCode": t.string().optional(),
            "prefixRewrite": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRedirectOut"])
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
    types["TcpRouteIn"] = t.struct(
        {
            "name": t.string(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
            "meshes": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
        }
    ).named(renames["TcpRouteIn"])
    types["TcpRouteOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleOut"])),
            "meshes": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteOut"])
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
    types["ServiceBindingIn"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "service": t.string(),
        }
    ).named(renames["ServiceBindingIn"])
    types["ServiceBindingOut"] = t.struct(
        {
            "name": t.string(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceId": t.string().optional(),
            "service": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceBindingOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["MeshIn"] = t.struct(
        {
            "interceptionPort": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["MeshIn"])
    types["MeshOut"] = t.struct(
        {
            "interceptionPort": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshOut"])
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
    types["HttpRouteFaultInjectionPolicyDelayIn"] = t.struct(
        {"fixedDelay": t.string().optional(), "percentage": t.integer().optional()}
    ).named(renames["HttpRouteFaultInjectionPolicyDelayIn"])
    types["HttpRouteFaultInjectionPolicyDelayOut"] = t.struct(
        {
            "fixedDelay": t.string().optional(),
            "percentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyDelayOut"])
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
    types["HttpRouteCorsPolicyIn"] = t.struct(
        {
            "allowMethods": t.array(t.string()).optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowHeaders": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "exposeHeaders": t.array(t.string()).optional(),
            "allowCredentials": t.boolean().optional(),
            "maxAge": t.string().optional(),
        }
    ).named(renames["HttpRouteCorsPolicyIn"])
    types["HttpRouteCorsPolicyOut"] = t.struct(
        {
            "allowMethods": t.array(t.string()).optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowHeaders": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
            "disabled": t.boolean().optional(),
            "exposeHeaders": t.array(t.string()).optional(),
            "allowCredentials": t.boolean().optional(),
            "maxAge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteCorsPolicyOut"])
    types["GrpcRouteRouteActionIn"] = t.struct(
        {
            "faultInjectionPolicy": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyIn"]
            ).optional(),
            "timeout": t.string().optional(),
            "retryPolicy": t.proxy(renames["GrpcRouteRetryPolicyIn"]).optional(),
            "destinations": t.array(
                t.proxy(renames["GrpcRouteDestinationIn"])
            ).optional(),
        }
    ).named(renames["GrpcRouteRouteActionIn"])
    types["GrpcRouteRouteActionOut"] = t.struct(
        {
            "faultInjectionPolicy": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyOut"]
            ).optional(),
            "timeout": t.string().optional(),
            "retryPolicy": t.proxy(renames["GrpcRouteRetryPolicyOut"]).optional(),
            "destinations": t.array(
                t.proxy(renames["GrpcRouteDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRouteActionOut"])
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
    types["HttpRouteHeaderMatchIntegerRangeIn"] = t.struct(
        {"start": t.integer().optional(), "end": t.integer().optional()}
    ).named(renames["HttpRouteHeaderMatchIntegerRangeIn"])
    types["HttpRouteHeaderMatchIntegerRangeOut"] = t.struct(
        {
            "start": t.integer().optional(),
            "end": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderMatchIntegerRangeOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListMeshesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "meshes": t.array(t.proxy(renames["MeshIn"])).optional(),
        }
    ).named(renames["ListMeshesResponseIn"])
    types["ListMeshesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "meshes": t.array(t.proxy(renames["MeshOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMeshesResponseOut"])
    types["GrpcRouteIn"] = t.struct(
        {
            "gateways": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "meshes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
            "hostnames": t.array(t.string()),
        }
    ).named(renames["GrpcRouteIn"])
    types["GrpcRouteOut"] = t.struct(
        {
            "gateways": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "meshes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "selfLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleOut"])),
            "hostnames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteOut"])
    types["GrpcRouteRetryPolicyIn"] = t.struct(
        {
            "numRetries": t.integer().optional(),
            "retryConditions": t.array(t.string()).optional(),
        }
    ).named(renames["GrpcRouteRetryPolicyIn"])
    types["GrpcRouteRetryPolicyOut"] = t.struct(
        {
            "numRetries": t.integer().optional(),
            "retryConditions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRetryPolicyOut"])
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
            "grpcService": t.string(),
            "grpcMethod": t.string(),
            "type": t.string().optional(),
        }
    ).named(renames["GrpcRouteMethodMatchIn"])
    types["GrpcRouteMethodMatchOut"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "grpcService": t.string(),
            "grpcMethod": t.string(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteMethodMatchOut"])
    types["ListGrpcRoutesResponseIn"] = t.struct(
        {
            "grpcRoutes": t.array(t.proxy(renames["GrpcRouteIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGrpcRoutesResponseIn"])
    types["ListGrpcRoutesResponseOut"] = t.struct(
        {
            "grpcRoutes": t.array(t.proxy(renames["GrpcRouteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGrpcRoutesResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["HttpRouteFaultInjectionPolicyIn"] = t.struct(
        {
            "abort": t.proxy(
                renames["HttpRouteFaultInjectionPolicyAbortIn"]
            ).optional(),
            "delay": t.proxy(
                renames["HttpRouteFaultInjectionPolicyDelayIn"]
            ).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyIn"])
    types["HttpRouteFaultInjectionPolicyOut"] = t.struct(
        {
            "abort": t.proxy(
                renames["HttpRouteFaultInjectionPolicyAbortOut"]
            ).optional(),
            "delay": t.proxy(
                renames["HttpRouteFaultInjectionPolicyDelayOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteFaultInjectionPolicyOut"])
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
    types["HttpRouteHeaderMatchIn"] = t.struct(
        {
            "invertMatch": t.boolean().optional(),
            "presentMatch": t.boolean().optional(),
            "header": t.string().optional(),
            "exactMatch": t.string().optional(),
            "prefixMatch": t.string().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeIn"]
            ).optional(),
            "suffixMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
        }
    ).named(renames["HttpRouteHeaderMatchIn"])
    types["HttpRouteHeaderMatchOut"] = t.struct(
        {
            "invertMatch": t.boolean().optional(),
            "presentMatch": t.boolean().optional(),
            "header": t.string().optional(),
            "exactMatch": t.string().optional(),
            "prefixMatch": t.string().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeOut"]
            ).optional(),
            "suffixMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderMatchOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["GatewayIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "ports": t.array(t.integer()),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverTlsPolicy": t.string().optional(),
            "addresses": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "network": t.string().optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "name": t.string(),
        }
    ).named(renames["GatewayIn"])
    types["GatewayOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "ports": t.array(t.integer()),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverTlsPolicy": t.string().optional(),
            "addresses": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "updateTime": t.string().optional(),
            "network": t.string().optional(),
            "createTime": t.string().optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "selfLink": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayOut"])
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
    types["HttpRouteRetryPolicyIn"] = t.struct(
        {
            "retryConditions": t.array(t.string()).optional(),
            "perTryTimeout": t.string().optional(),
            "numRetries": t.integer().optional(),
        }
    ).named(renames["HttpRouteRetryPolicyIn"])
    types["HttpRouteRetryPolicyOut"] = t.struct(
        {
            "retryConditions": t.array(t.string()).optional(),
            "perTryTimeout": t.string().optional(),
            "numRetries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRetryPolicyOut"])
    types["TrafficPortSelectorIn"] = t.struct(
        {"ports": t.array(t.string()).optional()}
    ).named(renames["TrafficPortSelectorIn"])
    types["TrafficPortSelectorOut"] = t.struct(
        {
            "ports": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficPortSelectorOut"])
    types["ListGatewaysResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "gateways": t.array(t.proxy(renames["GatewayIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGatewaysResponseIn"])
    types["ListGatewaysResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "gateways": t.array(t.proxy(renames["GatewayOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaysResponseOut"])
    types["EndpointPolicyIn"] = t.struct(
        {
            "serverTlsPolicy": t.string().optional(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trafficPortSelector": t.proxy(renames["TrafficPortSelectorIn"]).optional(),
            "authorizationPolicy": t.string().optional(),
            "clientTlsPolicy": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "type": t.string(),
        }
    ).named(renames["EndpointPolicyIn"])
    types["EndpointPolicyOut"] = t.struct(
        {
            "serverTlsPolicy": t.string().optional(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trafficPortSelector": t.proxy(
                renames["TrafficPortSelectorOut"]
            ).optional(),
            "authorizationPolicy": t.string().optional(),
            "clientTlsPolicy": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointPolicyOut"])
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
    types["HttpRouteRequestMirrorPolicyIn"] = t.struct(
        {"destination": t.proxy(renames["HttpRouteDestinationIn"]).optional()}
    ).named(renames["HttpRouteRequestMirrorPolicyIn"])
    types["HttpRouteRequestMirrorPolicyOut"] = t.struct(
        {
            "destination": t.proxy(renames["HttpRouteDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRequestMirrorPolicyOut"])
    types["HttpRouteRouteActionIn"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationIn"])
            ).optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectIn"]).optional(),
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyIn"]
            ).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyIn"]).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteIn"]).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyIn"]
            ).optional(),
            "timeout": t.string().optional(),
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyIn"]).optional(),
        }
    ).named(renames["HttpRouteRouteActionIn"])
    types["HttpRouteRouteActionOut"] = t.struct(
        {
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationOut"])
            ).optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectOut"]).optional(),
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyOut"]
            ).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyOut"]).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteOut"]).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyOut"]
            ).optional(),
            "timeout": t.string().optional(),
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteActionOut"])
    types["HttpRouteIn"] = t.struct(
        {
            "hostnames": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
            "name": t.string(),
            "description": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
        }
    ).named(renames["HttpRouteIn"])
    types["HttpRouteOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "hostnames": t.array(t.string()),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "selfLink": t.string().optional(),
            "createTime": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleOut"])),
            "name": t.string(),
            "description": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteOut"])
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
    types["TlsRouteIn"] = t.struct(
        {
            "name": t.string(),
            "meshes": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
        }
    ).named(renames["TlsRouteIn"])
    types["TlsRouteOut"] = t.struct(
        {
            "name": t.string(),
            "updateTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleOut"])),
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteOut"])
    types["HttpRouteQueryParameterMatchIn"] = t.struct(
        {
            "presentMatch": t.boolean().optional(),
            "exactMatch": t.string().optional(),
            "queryParameter": t.string().optional(),
            "regexMatch": t.string().optional(),
        }
    ).named(renames["HttpRouteQueryParameterMatchIn"])
    types["HttpRouteQueryParameterMatchOut"] = t.struct(
        {
            "presentMatch": t.boolean().optional(),
            "exactMatch": t.string().optional(),
            "queryParameter": t.string().optional(),
            "regexMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteQueryParameterMatchOut"])
    types["HttpRouteRouteMatchIn"] = t.struct(
        {
            "regexMatch": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
            "prefixMatch": t.string().optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchIn"])
            ).optional(),
            "fullPathMatch": t.string().optional(),
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchIn"])).optional(),
        }
    ).named(renames["HttpRouteRouteMatchIn"])
    types["HttpRouteRouteMatchOut"] = t.struct(
        {
            "regexMatch": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
            "prefixMatch": t.string().optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchOut"])
            ).optional(),
            "fullPathMatch": t.string().optional(),
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteMatchOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = networkservices.get(
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
    functions["projectsLocationsList"] = networkservices.get(
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
    functions["projectsLocationsTcpRoutesDelete"] = networkservices.post(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "tcpRouteId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
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
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
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
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
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
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesDelete"] = networkservices.get(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTlsRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesPatch"] = networkservices.get(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTlsRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesCreate"] = networkservices.get(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTlsRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesGet"] = networkservices.get(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTlsRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesList"] = networkservices.get(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTlsRoutesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesList"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesDelete"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesGet"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesGetIamPolicy"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesCreate"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesSetIamPolicy"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEndpointPoliciesTestIamPermissions"
    ] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesPatch"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "serverTlsPolicy": t.string().optional(),
                "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "trafficPortSelector": t.proxy(
                    renames["TrafficPortSelectorIn"]
                ).optional(),
                "authorizationPolicy": t.string().optional(),
                "clientTlsPolicy": t.string().optional(),
                "description": t.string().optional(),
                "type": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysList"] = networkservices.post(
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
    functions["projectsLocationsGatewaysGet"] = networkservices.post(
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
    functions["projectsLocationsGatewaysDelete"] = networkservices.post(
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
    functions["projectsLocationsGatewaysPatch"] = networkservices.post(
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
    functions["projectsLocationsGatewaysCreate"] = networkservices.post(
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
    functions["projectsLocationsGatewaysSetIamPolicy"] = networkservices.post(
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
    functions["projectsLocationsGatewaysGetIamPolicy"] = networkservices.post(
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
    functions["projectsLocationsGatewaysTestIamPermissions"] = networkservices.post(
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
    functions["projectsLocationsGrpcRoutesDelete"] = networkservices.post(
        "v1/{parent}/grpcRoutes",
        t.struct(
            {
                "parent": t.string(),
                "grpcRouteId": t.string(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesPatch"] = networkservices.post(
        "v1/{parent}/grpcRoutes",
        t.struct(
            {
                "parent": t.string(),
                "grpcRouteId": t.string(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesList"] = networkservices.post(
        "v1/{parent}/grpcRoutes",
        t.struct(
            {
                "parent": t.string(),
                "grpcRouteId": t.string(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesGet"] = networkservices.post(
        "v1/{parent}/grpcRoutes",
        t.struct(
            {
                "parent": t.string(),
                "grpcRouteId": t.string(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesCreate"] = networkservices.post(
        "v1/{parent}/grpcRoutes",
        t.struct(
            {
                "parent": t.string(),
                "grpcRouteId": t.string(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "meshes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = networkservices.post(
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
    functions["projectsLocationsOperationsGet"] = networkservices.post(
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
    functions["projectsLocationsOperationsList"] = networkservices.post(
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
    functions["projectsLocationsOperationsCancel"] = networkservices.post(
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
    functions["projectsLocationsServiceBindingsCreate"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
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
    functions["projectsLocationsServiceBindingsSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsServiceBindingsList"] = networkservices.get(
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
    functions["projectsLocationsServiceBindingsGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEdgeCacheKeysetsTestIamPermissions"
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
    functions["projectsLocationsEdgeCacheKeysetsSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsEdgeCacheKeysetsGetIamPolicy"] = networkservices.get(
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEdgeCacheServicesSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsEdgeCacheServicesGetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsMeshesSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsMeshesDelete"] = networkservices.get(
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
    functions["projectsLocationsMeshesList"] = networkservices.get(
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
    functions["projectsLocationsMeshesTestIamPermissions"] = networkservices.get(
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
    functions["projectsLocationsMeshesGet"] = networkservices.get(
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
    functions["projectsLocationsMeshesCreate"] = networkservices.get(
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
    functions["projectsLocationsMeshesPatch"] = networkservices.get(
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
    functions["projectsLocationsMeshesGetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsHttpRoutesGet"] = networkservices.post(
        "v1/{parent}/httpRoutes",
        t.struct(
            {
                "parent": t.string(),
                "httpRouteId": t.string(),
                "hostnames": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gateways": t.array(t.string()).optional(),
                "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
                "name": t.string(),
                "description": t.string().optional(),
                "meshes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesDelete"] = networkservices.post(
        "v1/{parent}/httpRoutes",
        t.struct(
            {
                "parent": t.string(),
                "httpRouteId": t.string(),
                "hostnames": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gateways": t.array(t.string()).optional(),
                "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
                "name": t.string(),
                "description": t.string().optional(),
                "meshes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesList"] = networkservices.post(
        "v1/{parent}/httpRoutes",
        t.struct(
            {
                "parent": t.string(),
                "httpRouteId": t.string(),
                "hostnames": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gateways": t.array(t.string()).optional(),
                "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
                "name": t.string(),
                "description": t.string().optional(),
                "meshes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesPatch"] = networkservices.post(
        "v1/{parent}/httpRoutes",
        t.struct(
            {
                "parent": t.string(),
                "httpRouteId": t.string(),
                "hostnames": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gateways": t.array(t.string()).optional(),
                "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
                "name": t.string(),
                "description": t.string().optional(),
                "meshes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsHttpRoutesCreate"] = networkservices.post(
        "v1/{parent}/httpRoutes",
        t.struct(
            {
                "parent": t.string(),
                "httpRouteId": t.string(),
                "hostnames": t.array(t.string()),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gateways": t.array(t.string()).optional(),
                "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
                "name": t.string(),
                "description": t.string().optional(),
                "meshes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEdgeCacheOriginsSetIamPolicy"] = networkservices.post(
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
        "projectsLocationsEdgeCacheOriginsTestIamPermissions"
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

    return Import(
        importer="networkservices",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
