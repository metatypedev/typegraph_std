from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_networkservices() -> Import:
    networkservices = HTTPRuntime("https://networkservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_networkservices_1_ErrorResponse",
        "HttpRouteRedirectIn": "_networkservices_2_HttpRouteRedirectIn",
        "HttpRouteRedirectOut": "_networkservices_3_HttpRouteRedirectOut",
        "GrpcRouteDestinationIn": "_networkservices_4_GrpcRouteDestinationIn",
        "GrpcRouteDestinationOut": "_networkservices_5_GrpcRouteDestinationOut",
        "ListGatewaysResponseIn": "_networkservices_6_ListGatewaysResponseIn",
        "ListGatewaysResponseOut": "_networkservices_7_ListGatewaysResponseOut",
        "TcpRouteIn": "_networkservices_8_TcpRouteIn",
        "TcpRouteOut": "_networkservices_9_TcpRouteOut",
        "EmptyIn": "_networkservices_10_EmptyIn",
        "EmptyOut": "_networkservices_11_EmptyOut",
        "MeshIn": "_networkservices_12_MeshIn",
        "MeshOut": "_networkservices_13_MeshOut",
        "SetIamPolicyRequestIn": "_networkservices_14_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_networkservices_15_SetIamPolicyRequestOut",
        "HttpRouteRouteRuleIn": "_networkservices_16_HttpRouteRouteRuleIn",
        "HttpRouteRouteRuleOut": "_networkservices_17_HttpRouteRouteRuleOut",
        "OperationIn": "_networkservices_18_OperationIn",
        "OperationOut": "_networkservices_19_OperationOut",
        "HttpRouteHeaderMatchIn": "_networkservices_20_HttpRouteHeaderMatchIn",
        "HttpRouteHeaderMatchOut": "_networkservices_21_HttpRouteHeaderMatchOut",
        "ListLocationsResponseIn": "_networkservices_22_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networkservices_23_ListLocationsResponseOut",
        "HttpRouteRequestMirrorPolicyIn": "_networkservices_24_HttpRouteRequestMirrorPolicyIn",
        "HttpRouteRequestMirrorPolicyOut": "_networkservices_25_HttpRouteRequestMirrorPolicyOut",
        "HttpRouteCorsPolicyIn": "_networkservices_26_HttpRouteCorsPolicyIn",
        "HttpRouteCorsPolicyOut": "_networkservices_27_HttpRouteCorsPolicyOut",
        "HttpRouteRouteMatchIn": "_networkservices_28_HttpRouteRouteMatchIn",
        "HttpRouteRouteMatchOut": "_networkservices_29_HttpRouteRouteMatchOut",
        "GrpcRouteFaultInjectionPolicyAbortIn": "_networkservices_30_GrpcRouteFaultInjectionPolicyAbortIn",
        "GrpcRouteFaultInjectionPolicyAbortOut": "_networkservices_31_GrpcRouteFaultInjectionPolicyAbortOut",
        "ListServiceBindingsResponseIn": "_networkservices_32_ListServiceBindingsResponseIn",
        "ListServiceBindingsResponseOut": "_networkservices_33_ListServiceBindingsResponseOut",
        "TestIamPermissionsRequestIn": "_networkservices_34_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_networkservices_35_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_networkservices_36_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_networkservices_37_TestIamPermissionsResponseOut",
        "HttpRouteHeaderMatchIntegerRangeIn": "_networkservices_38_HttpRouteHeaderMatchIntegerRangeIn",
        "HttpRouteHeaderMatchIntegerRangeOut": "_networkservices_39_HttpRouteHeaderMatchIntegerRangeOut",
        "HttpRouteDestinationIn": "_networkservices_40_HttpRouteDestinationIn",
        "HttpRouteDestinationOut": "_networkservices_41_HttpRouteDestinationOut",
        "TlsRouteRouteActionIn": "_networkservices_42_TlsRouteRouteActionIn",
        "TlsRouteRouteActionOut": "_networkservices_43_TlsRouteRouteActionOut",
        "TcpRouteRouteRuleIn": "_networkservices_44_TcpRouteRouteRuleIn",
        "TcpRouteRouteRuleOut": "_networkservices_45_TcpRouteRouteRuleOut",
        "HttpRouteQueryParameterMatchIn": "_networkservices_46_HttpRouteQueryParameterMatchIn",
        "HttpRouteQueryParameterMatchOut": "_networkservices_47_HttpRouteQueryParameterMatchOut",
        "GrpcRouteIn": "_networkservices_48_GrpcRouteIn",
        "GrpcRouteOut": "_networkservices_49_GrpcRouteOut",
        "GrpcRouteHeaderMatchIn": "_networkservices_50_GrpcRouteHeaderMatchIn",
        "GrpcRouteHeaderMatchOut": "_networkservices_51_GrpcRouteHeaderMatchOut",
        "AuditConfigIn": "_networkservices_52_AuditConfigIn",
        "AuditConfigOut": "_networkservices_53_AuditConfigOut",
        "GatewayIn": "_networkservices_54_GatewayIn",
        "GatewayOut": "_networkservices_55_GatewayOut",
        "HttpRouteFaultInjectionPolicyAbortIn": "_networkservices_56_HttpRouteFaultInjectionPolicyAbortIn",
        "HttpRouteFaultInjectionPolicyAbortOut": "_networkservices_57_HttpRouteFaultInjectionPolicyAbortOut",
        "ListEndpointPoliciesResponseIn": "_networkservices_58_ListEndpointPoliciesResponseIn",
        "ListEndpointPoliciesResponseOut": "_networkservices_59_ListEndpointPoliciesResponseOut",
        "TcpRouteRouteMatchIn": "_networkservices_60_TcpRouteRouteMatchIn",
        "TcpRouteRouteMatchOut": "_networkservices_61_TcpRouteRouteMatchOut",
        "CancelOperationRequestIn": "_networkservices_62_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networkservices_63_CancelOperationRequestOut",
        "ServiceBindingIn": "_networkservices_64_ServiceBindingIn",
        "ServiceBindingOut": "_networkservices_65_ServiceBindingOut",
        "TlsRouteRouteDestinationIn": "_networkservices_66_TlsRouteRouteDestinationIn",
        "TlsRouteRouteDestinationOut": "_networkservices_67_TlsRouteRouteDestinationOut",
        "GrpcRouteRouteMatchIn": "_networkservices_68_GrpcRouteRouteMatchIn",
        "GrpcRouteRouteMatchOut": "_networkservices_69_GrpcRouteRouteMatchOut",
        "GrpcRouteRouteRuleIn": "_networkservices_70_GrpcRouteRouteRuleIn",
        "GrpcRouteRouteRuleOut": "_networkservices_71_GrpcRouteRouteRuleOut",
        "EndpointMatcherMetadataLabelMatcherIn": "_networkservices_72_EndpointMatcherMetadataLabelMatcherIn",
        "EndpointMatcherMetadataLabelMatcherOut": "_networkservices_73_EndpointMatcherMetadataLabelMatcherOut",
        "TlsRouteRouteMatchIn": "_networkservices_74_TlsRouteRouteMatchIn",
        "TlsRouteRouteMatchOut": "_networkservices_75_TlsRouteRouteMatchOut",
        "GrpcRouteFaultInjectionPolicyIn": "_networkservices_76_GrpcRouteFaultInjectionPolicyIn",
        "GrpcRouteFaultInjectionPolicyOut": "_networkservices_77_GrpcRouteFaultInjectionPolicyOut",
        "GrpcRouteFaultInjectionPolicyDelayIn": "_networkservices_78_GrpcRouteFaultInjectionPolicyDelayIn",
        "GrpcRouteFaultInjectionPolicyDelayOut": "_networkservices_79_GrpcRouteFaultInjectionPolicyDelayOut",
        "GrpcRouteRetryPolicyIn": "_networkservices_80_GrpcRouteRetryPolicyIn",
        "GrpcRouteRetryPolicyOut": "_networkservices_81_GrpcRouteRetryPolicyOut",
        "GrpcRouteRouteActionIn": "_networkservices_82_GrpcRouteRouteActionIn",
        "GrpcRouteRouteActionOut": "_networkservices_83_GrpcRouteRouteActionOut",
        "TcpRouteRouteDestinationIn": "_networkservices_84_TcpRouteRouteDestinationIn",
        "TcpRouteRouteDestinationOut": "_networkservices_85_TcpRouteRouteDestinationOut",
        "StatusIn": "_networkservices_86_StatusIn",
        "StatusOut": "_networkservices_87_StatusOut",
        "ListTlsRoutesResponseIn": "_networkservices_88_ListTlsRoutesResponseIn",
        "ListTlsRoutesResponseOut": "_networkservices_89_ListTlsRoutesResponseOut",
        "OperationMetadataIn": "_networkservices_90_OperationMetadataIn",
        "OperationMetadataOut": "_networkservices_91_OperationMetadataOut",
        "TcpRouteRouteActionIn": "_networkservices_92_TcpRouteRouteActionIn",
        "TcpRouteRouteActionOut": "_networkservices_93_TcpRouteRouteActionOut",
        "HttpRouteRouteActionIn": "_networkservices_94_HttpRouteRouteActionIn",
        "HttpRouteRouteActionOut": "_networkservices_95_HttpRouteRouteActionOut",
        "LocationIn": "_networkservices_96_LocationIn",
        "LocationOut": "_networkservices_97_LocationOut",
        "HttpRouteRetryPolicyIn": "_networkservices_98_HttpRouteRetryPolicyIn",
        "HttpRouteRetryPolicyOut": "_networkservices_99_HttpRouteRetryPolicyOut",
        "PolicyIn": "_networkservices_100_PolicyIn",
        "PolicyOut": "_networkservices_101_PolicyOut",
        "HttpRouteHeaderModifierIn": "_networkservices_102_HttpRouteHeaderModifierIn",
        "HttpRouteHeaderModifierOut": "_networkservices_103_HttpRouteHeaderModifierOut",
        "ListOperationsResponseIn": "_networkservices_104_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networkservices_105_ListOperationsResponseOut",
        "AuditLogConfigIn": "_networkservices_106_AuditLogConfigIn",
        "AuditLogConfigOut": "_networkservices_107_AuditLogConfigOut",
        "HttpRouteIn": "_networkservices_108_HttpRouteIn",
        "HttpRouteOut": "_networkservices_109_HttpRouteOut",
        "ListTcpRoutesResponseIn": "_networkservices_110_ListTcpRoutesResponseIn",
        "ListTcpRoutesResponseOut": "_networkservices_111_ListTcpRoutesResponseOut",
        "GrpcRouteMethodMatchIn": "_networkservices_112_GrpcRouteMethodMatchIn",
        "GrpcRouteMethodMatchOut": "_networkservices_113_GrpcRouteMethodMatchOut",
        "TrafficPortSelectorIn": "_networkservices_114_TrafficPortSelectorIn",
        "TrafficPortSelectorOut": "_networkservices_115_TrafficPortSelectorOut",
        "ListHttpRoutesResponseIn": "_networkservices_116_ListHttpRoutesResponseIn",
        "ListHttpRoutesResponseOut": "_networkservices_117_ListHttpRoutesResponseOut",
        "HttpRouteFaultInjectionPolicyIn": "_networkservices_118_HttpRouteFaultInjectionPolicyIn",
        "HttpRouteFaultInjectionPolicyOut": "_networkservices_119_HttpRouteFaultInjectionPolicyOut",
        "EndpointMatcherIn": "_networkservices_120_EndpointMatcherIn",
        "EndpointMatcherOut": "_networkservices_121_EndpointMatcherOut",
        "HttpRouteURLRewriteIn": "_networkservices_122_HttpRouteURLRewriteIn",
        "HttpRouteURLRewriteOut": "_networkservices_123_HttpRouteURLRewriteOut",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsIn": "_networkservices_124_EndpointMatcherMetadataLabelMatcherMetadataLabelsIn",
        "EndpointMatcherMetadataLabelMatcherMetadataLabelsOut": "_networkservices_125_EndpointMatcherMetadataLabelMatcherMetadataLabelsOut",
        "HttpRouteFaultInjectionPolicyDelayIn": "_networkservices_126_HttpRouteFaultInjectionPolicyDelayIn",
        "HttpRouteFaultInjectionPolicyDelayOut": "_networkservices_127_HttpRouteFaultInjectionPolicyDelayOut",
        "TlsRouteIn": "_networkservices_128_TlsRouteIn",
        "TlsRouteOut": "_networkservices_129_TlsRouteOut",
        "TlsRouteRouteRuleIn": "_networkservices_130_TlsRouteRouteRuleIn",
        "TlsRouteRouteRuleOut": "_networkservices_131_TlsRouteRouteRuleOut",
        "BindingIn": "_networkservices_132_BindingIn",
        "BindingOut": "_networkservices_133_BindingOut",
        "ListGrpcRoutesResponseIn": "_networkservices_134_ListGrpcRoutesResponseIn",
        "ListGrpcRoutesResponseOut": "_networkservices_135_ListGrpcRoutesResponseOut",
        "EndpointPolicyIn": "_networkservices_136_EndpointPolicyIn",
        "EndpointPolicyOut": "_networkservices_137_EndpointPolicyOut",
        "ListMeshesResponseIn": "_networkservices_138_ListMeshesResponseIn",
        "ListMeshesResponseOut": "_networkservices_139_ListMeshesResponseOut",
        "ExprIn": "_networkservices_140_ExprIn",
        "ExprOut": "_networkservices_141_ExprOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HttpRouteRedirectIn"] = t.struct(
        {
            "responseCode": t.string().optional(),
            "portRedirect": t.integer().optional(),
            "prefixRewrite": t.string().optional(),
            "httpsRedirect": t.boolean().optional(),
            "hostRedirect": t.string().optional(),
            "pathRedirect": t.string().optional(),
            "stripQuery": t.boolean().optional(),
        }
    ).named(renames["HttpRouteRedirectIn"])
    types["HttpRouteRedirectOut"] = t.struct(
        {
            "responseCode": t.string().optional(),
            "portRedirect": t.integer().optional(),
            "prefixRewrite": t.string().optional(),
            "httpsRedirect": t.boolean().optional(),
            "hostRedirect": t.string().optional(),
            "pathRedirect": t.string().optional(),
            "stripQuery": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRedirectOut"])
    types["GrpcRouteDestinationIn"] = t.struct(
        {"weight": t.integer().optional(), "serviceName": t.string()}
    ).named(renames["GrpcRouteDestinationIn"])
    types["GrpcRouteDestinationOut"] = t.struct(
        {
            "weight": t.integer().optional(),
            "serviceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteDestinationOut"])
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
    types["TcpRouteIn"] = t.struct(
        {
            "name": t.string(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "meshes": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TcpRouteIn"])
    types["TcpRouteOut"] = t.struct(
        {
            "name": t.string(),
            "rules": t.array(t.proxy(renames["TcpRouteRouteRuleOut"])),
            "description": t.string().optional(),
            "selfLink": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MeshIn"] = t.struct(
        {
            "interceptionPort": t.integer().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MeshIn"])
    types["MeshOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "interceptionPort": t.integer().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "selfLink": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MeshOut"])
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
    types["HttpRouteRouteRuleIn"] = t.struct(
        {
            "matches": t.array(t.proxy(renames["HttpRouteRouteMatchIn"])).optional(),
            "action": t.proxy(renames["HttpRouteRouteActionIn"]).optional(),
        }
    ).named(renames["HttpRouteRouteRuleIn"])
    types["HttpRouteRouteRuleOut"] = t.struct(
        {
            "matches": t.array(t.proxy(renames["HttpRouteRouteMatchOut"])).optional(),
            "action": t.proxy(renames["HttpRouteRouteActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteRuleOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["HttpRouteHeaderMatchIn"] = t.struct(
        {
            "exactMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "suffixMatch": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "header": t.string().optional(),
            "invertMatch": t.boolean().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeIn"]
            ).optional(),
            "prefixMatch": t.string().optional(),
        }
    ).named(renames["HttpRouteHeaderMatchIn"])
    types["HttpRouteHeaderMatchOut"] = t.struct(
        {
            "exactMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "suffixMatch": t.string().optional(),
            "presentMatch": t.boolean().optional(),
            "header": t.string().optional(),
            "invertMatch": t.boolean().optional(),
            "rangeMatch": t.proxy(
                renames["HttpRouteHeaderMatchIntegerRangeOut"]
            ).optional(),
            "prefixMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderMatchOut"])
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
    types["HttpRouteRequestMirrorPolicyIn"] = t.struct(
        {"destination": t.proxy(renames["HttpRouteDestinationIn"]).optional()}
    ).named(renames["HttpRouteRequestMirrorPolicyIn"])
    types["HttpRouteRequestMirrorPolicyOut"] = t.struct(
        {
            "destination": t.proxy(renames["HttpRouteDestinationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRequestMirrorPolicyOut"])
    types["HttpRouteCorsPolicyIn"] = t.struct(
        {
            "exposeHeaders": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
            "allowMethods": t.array(t.string()).optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowCredentials": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "maxAge": t.string().optional(),
            "allowHeaders": t.array(t.string()).optional(),
        }
    ).named(renames["HttpRouteCorsPolicyIn"])
    types["HttpRouteCorsPolicyOut"] = t.struct(
        {
            "exposeHeaders": t.array(t.string()).optional(),
            "allowOrigins": t.array(t.string()).optional(),
            "allowMethods": t.array(t.string()).optional(),
            "allowOriginRegexes": t.array(t.string()).optional(),
            "allowCredentials": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "maxAge": t.string().optional(),
            "allowHeaders": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteCorsPolicyOut"])
    types["HttpRouteRouteMatchIn"] = t.struct(
        {
            "fullPathMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
            "prefixMatch": t.string().optional(),
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchIn"])).optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchIn"])
            ).optional(),
        }
    ).named(renames["HttpRouteRouteMatchIn"])
    types["HttpRouteRouteMatchOut"] = t.struct(
        {
            "fullPathMatch": t.string().optional(),
            "regexMatch": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
            "prefixMatch": t.string().optional(),
            "headers": t.array(t.proxy(renames["HttpRouteHeaderMatchOut"])).optional(),
            "queryParameters": t.array(
                t.proxy(renames["HttpRouteQueryParameterMatchOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteMatchOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["TlsRouteRouteActionIn"] = t.struct(
        {"destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationIn"]))}
    ).named(renames["TlsRouteRouteActionIn"])
    types["TlsRouteRouteActionOut"] = t.struct(
        {
            "destinations": t.array(t.proxy(renames["TlsRouteRouteDestinationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteRouteActionOut"])
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
    types["GrpcRouteIn"] = t.struct(
        {
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
            "meshes": t.array(t.string()).optional(),
            "name": t.string(),
            "hostnames": t.array(t.string()),
        }
    ).named(renames["GrpcRouteIn"])
    types["GrpcRouteOut"] = t.struct(
        {
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleOut"])),
            "meshes": t.array(t.string()).optional(),
            "selfLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "hostnames": t.array(t.string()),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteOut"])
    types["GrpcRouteHeaderMatchIn"] = t.struct(
        {"type": t.string().optional(), "key": t.string(), "value": t.string()}
    ).named(renames["GrpcRouteHeaderMatchIn"])
    types["GrpcRouteHeaderMatchOut"] = t.struct(
        {
            "type": t.string().optional(),
            "key": t.string(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteHeaderMatchOut"])
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
    types["GatewayIn"] = t.struct(
        {
            "network": t.string().optional(),
            "scope": t.string().optional(),
            "ports": t.array(t.integer()),
            "name": t.string(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "addresses": t.array(t.string()).optional(),
            "serverTlsPolicy": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "description": t.string().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["GatewayIn"])
    types["GatewayOut"] = t.struct(
        {
            "network": t.string().optional(),
            "selfLink": t.string().optional(),
            "scope": t.string().optional(),
            "ports": t.array(t.integer()),
            "name": t.string(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "certificateUrls": t.array(t.string()).optional(),
            "addresses": t.array(t.string()).optional(),
            "serverTlsPolicy": t.string().optional(),
            "gatewaySecurityPolicy": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewayOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ServiceBindingIn"] = t.struct(
        {
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "service": t.string(),
        }
    ).named(renames["ServiceBindingIn"])
    types["ServiceBindingOut"] = t.struct(
        {
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "service": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceBindingOut"])
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
    types["GrpcRouteRouteMatchIn"] = t.struct(
        {
            "method": t.proxy(renames["GrpcRouteMethodMatchIn"]).optional(),
            "headers": t.array(t.proxy(renames["GrpcRouteHeaderMatchIn"])).optional(),
        }
    ).named(renames["GrpcRouteRouteMatchIn"])
    types["GrpcRouteRouteMatchOut"] = t.struct(
        {
            "method": t.proxy(renames["GrpcRouteMethodMatchOut"]).optional(),
            "headers": t.array(t.proxy(renames["GrpcRouteHeaderMatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteRouteMatchOut"])
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
    types["GrpcRouteFaultInjectionPolicyIn"] = t.struct(
        {
            "abort": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyAbortIn"]
            ).optional(),
            "delay": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyDelayIn"]
            ).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyIn"])
    types["GrpcRouteFaultInjectionPolicyOut"] = t.struct(
        {
            "abort": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyAbortOut"]
            ).optional(),
            "delay": t.proxy(
                renames["GrpcRouteFaultInjectionPolicyDelayOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteFaultInjectionPolicyOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["TcpRouteRouteActionIn"] = t.struct(
        {
            "originalDestination": t.boolean().optional(),
            "destinations": t.array(
                t.proxy(renames["TcpRouteRouteDestinationIn"])
            ).optional(),
        }
    ).named(renames["TcpRouteRouteActionIn"])
    types["TcpRouteRouteActionOut"] = t.struct(
        {
            "originalDestination": t.boolean().optional(),
            "destinations": t.array(
                t.proxy(renames["TcpRouteRouteDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TcpRouteRouteActionOut"])
    types["HttpRouteRouteActionIn"] = t.struct(
        {
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationIn"])
            ).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyIn"]).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteIn"]).optional(),
            "timeout": t.string().optional(),
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierIn"]
            ).optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectIn"]).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyIn"]
            ).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyIn"]).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyIn"]
            ).optional(),
        }
    ).named(renames["HttpRouteRouteActionIn"])
    types["HttpRouteRouteActionOut"] = t.struct(
        {
            "requestHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "destinations": t.array(
                t.proxy(renames["HttpRouteDestinationOut"])
            ).optional(),
            "corsPolicy": t.proxy(renames["HttpRouteCorsPolicyOut"]).optional(),
            "urlRewrite": t.proxy(renames["HttpRouteURLRewriteOut"]).optional(),
            "timeout": t.string().optional(),
            "responseHeaderModifier": t.proxy(
                renames["HttpRouteHeaderModifierOut"]
            ).optional(),
            "redirect": t.proxy(renames["HttpRouteRedirectOut"]).optional(),
            "faultInjectionPolicy": t.proxy(
                renames["HttpRouteFaultInjectionPolicyOut"]
            ).optional(),
            "retryPolicy": t.proxy(renames["HttpRouteRetryPolicyOut"]).optional(),
            "requestMirrorPolicy": t.proxy(
                renames["HttpRouteRequestMirrorPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRouteActionOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["HttpRouteRetryPolicyIn"] = t.struct(
        {
            "perTryTimeout": t.string().optional(),
            "retryConditions": t.array(t.string()).optional(),
            "numRetries": t.integer().optional(),
        }
    ).named(renames["HttpRouteRetryPolicyIn"])
    types["HttpRouteRetryPolicyOut"] = t.struct(
        {
            "perTryTimeout": t.string().optional(),
            "retryConditions": t.array(t.string()).optional(),
            "numRetries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteRetryPolicyOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["HttpRouteHeaderModifierIn"] = t.struct(
        {
            "remove": t.array(t.string()).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "add": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HttpRouteHeaderModifierIn"])
    types["HttpRouteHeaderModifierOut"] = t.struct(
        {
            "remove": t.array(t.string()).optional(),
            "set": t.struct({"_": t.string().optional()}).optional(),
            "add": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteHeaderModifierOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
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
    types["HttpRouteIn"] = t.struct(
        {
            "meshes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "hostnames": t.array(t.string()),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleIn"])),
        }
    ).named(renames["HttpRouteIn"])
    types["HttpRouteOut"] = t.struct(
        {
            "meshes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "gateways": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "selfLink": t.string().optional(),
            "hostnames": t.array(t.string()),
            "rules": t.array(t.proxy(renames["HttpRouteRouteRuleOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRouteOut"])
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
    types["GrpcRouteMethodMatchIn"] = t.struct(
        {
            "grpcService": t.string(),
            "grpcMethod": t.string(),
            "caseSensitive": t.boolean().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GrpcRouteMethodMatchIn"])
    types["GrpcRouteMethodMatchOut"] = t.struct(
        {
            "grpcService": t.string(),
            "grpcMethod": t.string(),
            "caseSensitive": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GrpcRouteMethodMatchOut"])
    types["TrafficPortSelectorIn"] = t.struct(
        {"ports": t.array(t.string()).optional()}
    ).named(renames["TrafficPortSelectorIn"])
    types["TrafficPortSelectorOut"] = t.struct(
        {
            "ports": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficPortSelectorOut"])
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
    types["TlsRouteIn"] = t.struct(
        {
            "meshes": t.array(t.string()).optional(),
            "gateways": t.array(t.string()).optional(),
            "name": t.string(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
            "description": t.string().optional(),
        }
    ).named(renames["TlsRouteIn"])
    types["TlsRouteOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "meshes": t.array(t.string()).optional(),
            "gateways": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "rules": t.array(t.proxy(renames["TlsRouteRouteRuleOut"])),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsRouteOut"])
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
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["EndpointPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherIn"]),
            "trafficPortSelector": t.proxy(renames["TrafficPortSelectorIn"]).optional(),
            "description": t.string().optional(),
            "serverTlsPolicy": t.string().optional(),
            "clientTlsPolicy": t.string().optional(),
            "authorizationPolicy": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["EndpointPolicyIn"])
    types["EndpointPolicyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string(),
            "endpointMatcher": t.proxy(renames["EndpointMatcherOut"]),
            "trafficPortSelector": t.proxy(
                renames["TrafficPortSelectorOut"]
            ).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "serverTlsPolicy": t.string().optional(),
            "clientTlsPolicy": t.string().optional(),
            "authorizationPolicy": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointPolicyOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])

    functions = {}
    functions["projectsLocationsGet"] = networkservices.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsServiceBindingsSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsServiceBindingsGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceBindingOut"]),
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
    functions["projectsLocationsEndpointPoliciesDelete"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEndpointPoliciesTestIamPermissions"
    ] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesCreate"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesGetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesPatch"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesList"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesSetIamPolicy"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointPoliciesGet"] = networkservices.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointPolicyOut"]),
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
                "description": t.string().optional(),
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
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "description": t.string().optional(),
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
    functions["projectsLocationsTcpRoutesPatch"] = networkservices.post(
        "v1/{parent}/tcpRoutes",
        t.struct(
            {
                "tcpRouteId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "description": t.string().optional(),
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
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "description": t.string().optional(),
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
                "rules": t.array(t.proxy(renames["TcpRouteRouteRuleIn"])),
                "description": t.string().optional(),
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
    functions["projectsLocationsGrpcRoutesList"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesGet"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesDelete"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesCreate"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGrpcRoutesPatch"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "gateways": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "rules": t.array(t.proxy(renames["GrpcRouteRouteRuleIn"])),
                "meshes": t.array(t.string()).optional(),
                "hostnames": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsOperationsList"] = networkservices.delete(
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
    functions["projectsLocationsHttpRoutesDelete"] = networkservices.get(
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
    functions["projectsLocationsHttpRoutesPatch"] = networkservices.get(
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
    functions["projectsLocationsTlsRoutesList"] = networkservices.post(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "tlsRouteId": t.string(),
                "parent": t.string(),
                "meshes": t.array(t.string()).optional(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "description": t.string().optional(),
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
                "meshes": t.array(t.string()).optional(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "description": t.string().optional(),
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
                "meshes": t.array(t.string()).optional(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsRoutesDelete"] = networkservices.post(
        "v1/{parent}/tlsRoutes",
        t.struct(
            {
                "tlsRouteId": t.string(),
                "parent": t.string(),
                "meshes": t.array(t.string()).optional(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "description": t.string().optional(),
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
                "meshes": t.array(t.string()).optional(),
                "gateways": t.array(t.string()).optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["TlsRouteRouteRuleIn"])),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEdgeCacheOriginsSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsEdgeCacheOriginsGetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsGatewaysTestIamPermissions"] = networkservices.get(
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
    functions["projectsLocationsGatewaysCreate"] = networkservices.get(
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
    functions["projectsLocationsGatewaysDelete"] = networkservices.get(
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
    functions["projectsLocationsGatewaysSetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsGatewaysGet"] = networkservices.get(
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
    functions["projectsLocationsGatewaysList"] = networkservices.get(
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
    functions["projectsLocationsGatewaysPatch"] = networkservices.get(
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
    functions["projectsLocationsGatewaysGetIamPolicy"] = networkservices.get(
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
    functions["projectsLocationsMeshesCreate"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesList"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesGetIamPolicy"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesTestIamPermissions"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesDelete"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesSetIamPolicy"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesGet"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsMeshesPatch"] = networkservices.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "interceptionPort": t.integer().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networkservices",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
