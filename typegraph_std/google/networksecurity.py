from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_networksecurity() -> Import:
    networksecurity = HTTPRuntime("https://networksecurity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networksecurity_1_ErrorResponse",
        "RuleIn": "_networksecurity_2_RuleIn",
        "RuleOut": "_networksecurity_3_RuleOut",
        "MTLSPolicyIn": "_networksecurity_4_MTLSPolicyIn",
        "MTLSPolicyOut": "_networksecurity_5_MTLSPolicyOut",
        "UrlListIn": "_networksecurity_6_UrlListIn",
        "UrlListOut": "_networksecurity_7_UrlListOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_networksecurity_8_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_networksecurity_9_GoogleIamV1TestIamPermissionsResponseOut",
        "LocationIn": "_networksecurity_10_LocationIn",
        "LocationOut": "_networksecurity_11_LocationOut",
        "ClientTlsPolicyIn": "_networksecurity_12_ClientTlsPolicyIn",
        "ClientTlsPolicyOut": "_networksecurity_13_ClientTlsPolicyOut",
        "HttpHeaderMatchIn": "_networksecurity_14_HttpHeaderMatchIn",
        "HttpHeaderMatchOut": "_networksecurity_15_HttpHeaderMatchOut",
        "EmptyIn": "_networksecurity_16_EmptyIn",
        "EmptyOut": "_networksecurity_17_EmptyOut",
        "GoogleIamV1AuditConfigIn": "_networksecurity_18_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_networksecurity_19_GoogleIamV1AuditConfigOut",
        "OperationIn": "_networksecurity_20_OperationIn",
        "OperationOut": "_networksecurity_21_OperationOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_networksecurity_22_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_networksecurity_23_GoogleIamV1SetIamPolicyRequestOut",
        "ListGatewaySecurityPolicyRulesResponseIn": "_networksecurity_24_ListGatewaySecurityPolicyRulesResponseIn",
        "ListGatewaySecurityPolicyRulesResponseOut": "_networksecurity_25_ListGatewaySecurityPolicyRulesResponseOut",
        "ListServerTlsPoliciesResponseIn": "_networksecurity_26_ListServerTlsPoliciesResponseIn",
        "ListServerTlsPoliciesResponseOut": "_networksecurity_27_ListServerTlsPoliciesResponseOut",
        "SourceIn": "_networksecurity_28_SourceIn",
        "SourceOut": "_networksecurity_29_SourceOut",
        "GoogleCloudNetworksecurityV1GrpcEndpointIn": "_networksecurity_30_GoogleCloudNetworksecurityV1GrpcEndpointIn",
        "GoogleCloudNetworksecurityV1GrpcEndpointOut": "_networksecurity_31_GoogleCloudNetworksecurityV1GrpcEndpointOut",
        "ListGatewaySecurityPoliciesResponseIn": "_networksecurity_32_ListGatewaySecurityPoliciesResponseIn",
        "ListGatewaySecurityPoliciesResponseOut": "_networksecurity_33_ListGatewaySecurityPoliciesResponseOut",
        "AuthorizationPolicyIn": "_networksecurity_34_AuthorizationPolicyIn",
        "AuthorizationPolicyOut": "_networksecurity_35_AuthorizationPolicyOut",
        "StatusIn": "_networksecurity_36_StatusIn",
        "StatusOut": "_networksecurity_37_StatusOut",
        "ListClientTlsPoliciesResponseIn": "_networksecurity_38_ListClientTlsPoliciesResponseIn",
        "ListClientTlsPoliciesResponseOut": "_networksecurity_39_ListClientTlsPoliciesResponseOut",
        "CertificateProviderInstanceIn": "_networksecurity_40_CertificateProviderInstanceIn",
        "CertificateProviderInstanceOut": "_networksecurity_41_CertificateProviderInstanceOut",
        "DestinationIn": "_networksecurity_42_DestinationIn",
        "DestinationOut": "_networksecurity_43_DestinationOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_networksecurity_44_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_networksecurity_45_GoogleIamV1TestIamPermissionsRequestOut",
        "CancelOperationRequestIn": "_networksecurity_46_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networksecurity_47_CancelOperationRequestOut",
        "ListOperationsResponseIn": "_networksecurity_48_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networksecurity_49_ListOperationsResponseOut",
        "GoogleIamV1BindingIn": "_networksecurity_50_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_networksecurity_51_GoogleIamV1BindingOut",
        "ListTlsInspectionPoliciesResponseIn": "_networksecurity_52_ListTlsInspectionPoliciesResponseIn",
        "ListTlsInspectionPoliciesResponseOut": "_networksecurity_53_ListTlsInspectionPoliciesResponseOut",
        "GatewaySecurityPolicyRuleIn": "_networksecurity_54_GatewaySecurityPolicyRuleIn",
        "GatewaySecurityPolicyRuleOut": "_networksecurity_55_GatewaySecurityPolicyRuleOut",
        "ServerTlsPolicyIn": "_networksecurity_56_ServerTlsPolicyIn",
        "ServerTlsPolicyOut": "_networksecurity_57_ServerTlsPolicyOut",
        "ListAuthorizationPoliciesResponseIn": "_networksecurity_58_ListAuthorizationPoliciesResponseIn",
        "ListAuthorizationPoliciesResponseOut": "_networksecurity_59_ListAuthorizationPoliciesResponseOut",
        "TlsInspectionPolicyIn": "_networksecurity_60_TlsInspectionPolicyIn",
        "TlsInspectionPolicyOut": "_networksecurity_61_TlsInspectionPolicyOut",
        "ValidationCAIn": "_networksecurity_62_ValidationCAIn",
        "ValidationCAOut": "_networksecurity_63_ValidationCAOut",
        "ListUrlListsResponseIn": "_networksecurity_64_ListUrlListsResponseIn",
        "ListUrlListsResponseOut": "_networksecurity_65_ListUrlListsResponseOut",
        "ListLocationsResponseIn": "_networksecurity_66_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networksecurity_67_ListLocationsResponseOut",
        "OperationMetadataIn": "_networksecurity_68_OperationMetadataIn",
        "OperationMetadataOut": "_networksecurity_69_OperationMetadataOut",
        "GoogleCloudNetworksecurityV1CertificateProviderIn": "_networksecurity_70_GoogleCloudNetworksecurityV1CertificateProviderIn",
        "GoogleCloudNetworksecurityV1CertificateProviderOut": "_networksecurity_71_GoogleCloudNetworksecurityV1CertificateProviderOut",
        "GatewaySecurityPolicyIn": "_networksecurity_72_GatewaySecurityPolicyIn",
        "GatewaySecurityPolicyOut": "_networksecurity_73_GatewaySecurityPolicyOut",
        "ExprIn": "_networksecurity_74_ExprIn",
        "ExprOut": "_networksecurity_75_ExprOut",
        "GoogleIamV1PolicyIn": "_networksecurity_76_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_networksecurity_77_GoogleIamV1PolicyOut",
        "GoogleIamV1AuditLogConfigIn": "_networksecurity_78_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_networksecurity_79_GoogleIamV1AuditLogConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RuleIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "destinations": t.array(t.proxy(renames["DestinationIn"])).optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "destinations": t.array(t.proxy(renames["DestinationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["MTLSPolicyIn"] = t.struct(
        {
            "clientValidationTrustConfig": t.string().optional(),
            "clientValidationMode": t.string().optional(),
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAIn"])),
        }
    ).named(renames["MTLSPolicyIn"])
    types["MTLSPolicyOut"] = t.struct(
        {
            "clientValidationTrustConfig": t.string().optional(),
            "clientValidationMode": t.string().optional(),
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MTLSPolicyOut"])
    types["UrlListIn"] = t.struct(
        {
            "name": t.string(),
            "values": t.array(t.string()),
            "description": t.string().optional(),
        }
    ).named(renames["UrlListIn"])
    types["UrlListOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string(),
            "values": t.array(t.string()),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlListOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
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
    types["ClientTlsPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAIn"])
            ).optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
            "sni": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["ClientTlsPolicyIn"])
    types["ClientTlsPolicyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAOut"])
            ).optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "sni": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientTlsPolicyOut"])
    types["HttpHeaderMatchIn"] = t.struct(
        {"regexMatch": t.string(), "headerName": t.string()}
    ).named(renames["HttpHeaderMatchIn"])
    types["HttpHeaderMatchOut"] = t.struct(
        {
            "regexMatch": t.string(),
            "headerName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpHeaderMatchOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["ListGatewaySecurityPolicyRulesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleIn"])
            ).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseIn"])
    types["ListGatewaySecurityPolicyRulesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseOut"])
    types["ListServerTlsPoliciesResponseIn"] = t.struct(
        {
            "serverTlsPolicies": t.array(
                t.proxy(renames["ServerTlsPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServerTlsPoliciesResponseIn"])
    types["ListServerTlsPoliciesResponseOut"] = t.struct(
        {
            "serverTlsPolicies": t.array(
                t.proxy(renames["ServerTlsPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServerTlsPoliciesResponseOut"])
    types["SourceIn"] = t.struct(
        {
            "principals": t.array(t.string()).optional(),
            "ipBlocks": t.array(t.string()).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "principals": t.array(t.string()).optional(),
            "ipBlocks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["GoogleCloudNetworksecurityV1GrpcEndpointIn"] = t.struct(
        {"targetUri": t.string()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"])
    types["GoogleCloudNetworksecurityV1GrpcEndpointOut"] = t.struct(
        {"targetUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"])
    types["ListGatewaySecurityPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gatewaySecurityPolicies": t.array(
                t.proxy(renames["GatewaySecurityPolicyIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListGatewaySecurityPoliciesResponseIn"])
    types["ListGatewaySecurityPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gatewaySecurityPolicies": t.array(
                t.proxy(renames["GatewaySecurityPolicyOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaySecurityPoliciesResponseOut"])
    types["AuthorizationPolicyIn"] = t.struct(
        {
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AuthorizationPolicyIn"])
    types["AuthorizationPolicyOut"] = t.struct(
        {
            "name": t.string(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationPolicyOut"])
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
    types["ListClientTlsPoliciesResponseIn"] = t.struct(
        {
            "clientTlsPolicies": t.array(
                t.proxy(renames["ClientTlsPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListClientTlsPoliciesResponseIn"])
    types["ListClientTlsPoliciesResponseOut"] = t.struct(
        {
            "clientTlsPolicies": t.array(
                t.proxy(renames["ClientTlsPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientTlsPoliciesResponseOut"])
    types["CertificateProviderInstanceIn"] = t.struct(
        {"pluginInstance": t.string()}
    ).named(renames["CertificateProviderInstanceIn"])
    types["CertificateProviderInstanceOut"] = t.struct(
        {
            "pluginInstance": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateProviderInstanceOut"])
    types["DestinationIn"] = t.struct(
        {
            "ports": t.array(t.integer()),
            "methods": t.array(t.string()).optional(),
            "hosts": t.array(t.string()),
            "httpHeaderMatch": t.proxy(renames["HttpHeaderMatchIn"]).optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "ports": t.array(t.integer()),
            "methods": t.array(t.string()).optional(),
            "hosts": t.array(t.string()),
            "httpHeaderMatch": t.proxy(renames["HttpHeaderMatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["ListTlsInspectionPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "tlsInspectionPolicies": t.array(
                t.proxy(renames["TlsInspectionPolicyIn"])
            ).optional(),
        }
    ).named(renames["ListTlsInspectionPoliciesResponseIn"])
    types["ListTlsInspectionPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "tlsInspectionPolicies": t.array(
                t.proxy(renames["TlsInspectionPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTlsInspectionPoliciesResponseOut"])
    types["GatewaySecurityPolicyRuleIn"] = t.struct(
        {
            "priority": t.integer(),
            "enabled": t.boolean(),
            "basicProfile": t.string(),
            "applicationMatcher": t.string().optional(),
            "description": t.string().optional(),
            "sessionMatcher": t.string(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "name": t.string(),
        }
    ).named(renames["GatewaySecurityPolicyRuleIn"])
    types["GatewaySecurityPolicyRuleOut"] = t.struct(
        {
            "priority": t.integer(),
            "enabled": t.boolean(),
            "createTime": t.string().optional(),
            "basicProfile": t.string(),
            "applicationMatcher": t.string().optional(),
            "description": t.string().optional(),
            "sessionMatcher": t.string(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyRuleOut"])
    types["ServerTlsPolicyIn"] = t.struct(
        {
            "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
            "allowOpen": t.boolean().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
        }
    ).named(renames["ServerTlsPolicyIn"])
    types["ServerTlsPolicyOut"] = t.struct(
        {
            "mtlsPolicy": t.proxy(renames["MTLSPolicyOut"]).optional(),
            "allowOpen": t.boolean().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerTlsPolicyOut"])
    types["ListAuthorizationPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "authorizationPolicies": t.array(
                t.proxy(renames["AuthorizationPolicyIn"])
            ).optional(),
        }
    ).named(renames["ListAuthorizationPoliciesResponseIn"])
    types["ListAuthorizationPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "authorizationPolicies": t.array(
                t.proxy(renames["AuthorizationPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuthorizationPoliciesResponseOut"])
    types["TlsInspectionPolicyIn"] = t.struct(
        {"caPool": t.string(), "name": t.string(), "description": t.string().optional()}
    ).named(renames["TlsInspectionPolicyIn"])
    types["TlsInspectionPolicyOut"] = t.struct(
        {
            "caPool": t.string(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsInspectionPolicyOut"])
    types["ValidationCAIn"] = t.struct(
        {
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceIn"]
            ).optional(),
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"]
            ).optional(),
        }
    ).named(renames["ValidationCAIn"])
    types["ValidationCAOut"] = t.struct(
        {
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceOut"]
            ).optional(),
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCAOut"])
    types["ListUrlListsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "urlLists": t.array(t.proxy(renames["UrlListIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUrlListsResponseIn"])
    types["ListUrlListsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "urlLists": t.array(t.proxy(renames["UrlListOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUrlListsResponseOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GoogleCloudNetworksecurityV1CertificateProviderIn"] = t.struct(
        {
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceIn"]
            ).optional(),
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudNetworksecurityV1CertificateProviderIn"])
    types["GoogleCloudNetworksecurityV1CertificateProviderOut"] = t.struct(
        {
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceOut"]
            ).optional(),
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudNetworksecurityV1CertificateProviderOut"])
    types["GatewaySecurityPolicyIn"] = t.struct(
        {
            "name": t.string(),
            "tlsInspectionPolicy": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GatewaySecurityPolicyIn"])
    types["GatewaySecurityPolicyOut"] = t.struct(
        {
            "name": t.string(),
            "tlsInspectionPolicy": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])

    functions = {}
    functions["projectsLocationsList"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesList"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesCreate"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesDelete"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesGet"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesSetIamPolicy"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesGetIamPolicy"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesPatch"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClientTlsPoliciesTestIamPermissions"
    ] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesDelete"] = networksecurity.post(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "gatewaySecurityPolicyId": t.string(),
                "name": t.string(),
                "tlsInspectionPolicy": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesList"] = networksecurity.post(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "gatewaySecurityPolicyId": t.string(),
                "name": t.string(),
                "tlsInspectionPolicy": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesPatch"] = networksecurity.post(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "gatewaySecurityPolicyId": t.string(),
                "name": t.string(),
                "tlsInspectionPolicy": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesGet"] = networksecurity.post(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "gatewaySecurityPolicyId": t.string(),
                "name": t.string(),
                "tlsInspectionPolicy": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesCreate"] = networksecurity.post(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "gatewaySecurityPolicyId": t.string(),
                "name": t.string(),
                "tlsInspectionPolicy": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesPatch"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewaySecurityPolicyRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesList"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewaySecurityPolicyRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesDelete"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewaySecurityPolicyRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesCreate"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewaySecurityPolicyRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesRulesGet"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GatewaySecurityPolicyRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesList"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TlsInspectionPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesPatch"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TlsInspectionPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesDelete"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TlsInspectionPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesCreate"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TlsInspectionPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesGet"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TlsInspectionPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesGetIamPolicy"
    ] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesPatch"] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesSetIamPolicy"
    ] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesGet"] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesList"] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesDelete"] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesTestIamPermissions"
    ] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesCreate"] = networksecurity.post(
        "v1/{parent}/authorizationPolicies",
        t.struct(
            {
                "authorizationPolicyId": t.string(),
                "parent": t.string(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "action": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesDelete"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesGet"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesCreate"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesSetIamPolicy"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesGetIamPolicy"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesPatch"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesList"] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServerTlsPoliciesTestIamPermissions"
    ] = networksecurity.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "values": t.array(t.string()),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsDelete"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "values": t.array(t.string()),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsGet"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "values": t.array(t.string()),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsList"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "values": t.array(t.string()),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsPatch"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "values": t.array(t.string()),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networksecurity", renames=renames, types=types, functions=functions
    )
