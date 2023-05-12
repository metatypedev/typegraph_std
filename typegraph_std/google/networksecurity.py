from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_networksecurity() -> Import:
    networksecurity = HTTPRuntime("https://networksecurity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networksecurity_1_ErrorResponse",
        "DestinationIn": "_networksecurity_2_DestinationIn",
        "DestinationOut": "_networksecurity_3_DestinationOut",
        "UrlListIn": "_networksecurity_4_UrlListIn",
        "UrlListOut": "_networksecurity_5_UrlListOut",
        "LocationIn": "_networksecurity_6_LocationIn",
        "LocationOut": "_networksecurity_7_LocationOut",
        "GoogleCloudNetworksecurityV1CertificateProviderIn": "_networksecurity_8_GoogleCloudNetworksecurityV1CertificateProviderIn",
        "GoogleCloudNetworksecurityV1CertificateProviderOut": "_networksecurity_9_GoogleCloudNetworksecurityV1CertificateProviderOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_networksecurity_10_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_networksecurity_11_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudNetworksecurityV1GrpcEndpointIn": "_networksecurity_12_GoogleCloudNetworksecurityV1GrpcEndpointIn",
        "GoogleCloudNetworksecurityV1GrpcEndpointOut": "_networksecurity_13_GoogleCloudNetworksecurityV1GrpcEndpointOut",
        "ListClientTlsPoliciesResponseIn": "_networksecurity_14_ListClientTlsPoliciesResponseIn",
        "ListClientTlsPoliciesResponseOut": "_networksecurity_15_ListClientTlsPoliciesResponseOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_networksecurity_16_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_networksecurity_17_GoogleIamV1SetIamPolicyRequestOut",
        "ListLocationsResponseIn": "_networksecurity_18_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networksecurity_19_ListLocationsResponseOut",
        "TlsInspectionPolicyIn": "_networksecurity_20_TlsInspectionPolicyIn",
        "TlsInspectionPolicyOut": "_networksecurity_21_TlsInspectionPolicyOut",
        "ClientTlsPolicyIn": "_networksecurity_22_ClientTlsPolicyIn",
        "ClientTlsPolicyOut": "_networksecurity_23_ClientTlsPolicyOut",
        "CancelOperationRequestIn": "_networksecurity_24_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networksecurity_25_CancelOperationRequestOut",
        "ListTlsInspectionPoliciesResponseIn": "_networksecurity_26_ListTlsInspectionPoliciesResponseIn",
        "ListTlsInspectionPoliciesResponseOut": "_networksecurity_27_ListTlsInspectionPoliciesResponseOut",
        "MTLSPolicyIn": "_networksecurity_28_MTLSPolicyIn",
        "MTLSPolicyOut": "_networksecurity_29_MTLSPolicyOut",
        "ListUrlListsResponseIn": "_networksecurity_30_ListUrlListsResponseIn",
        "ListUrlListsResponseOut": "_networksecurity_31_ListUrlListsResponseOut",
        "HttpHeaderMatchIn": "_networksecurity_32_HttpHeaderMatchIn",
        "HttpHeaderMatchOut": "_networksecurity_33_HttpHeaderMatchOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_networksecurity_34_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_networksecurity_35_GoogleIamV1TestIamPermissionsResponseOut",
        "ServerTlsPolicyIn": "_networksecurity_36_ServerTlsPolicyIn",
        "ServerTlsPolicyOut": "_networksecurity_37_ServerTlsPolicyOut",
        "GoogleIamV1BindingIn": "_networksecurity_38_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_networksecurity_39_GoogleIamV1BindingOut",
        "GoogleIamV1AuditLogConfigIn": "_networksecurity_40_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_networksecurity_41_GoogleIamV1AuditLogConfigOut",
        "ExprIn": "_networksecurity_42_ExprIn",
        "ExprOut": "_networksecurity_43_ExprOut",
        "GatewaySecurityPolicyRuleIn": "_networksecurity_44_GatewaySecurityPolicyRuleIn",
        "GatewaySecurityPolicyRuleOut": "_networksecurity_45_GatewaySecurityPolicyRuleOut",
        "GatewaySecurityPolicyIn": "_networksecurity_46_GatewaySecurityPolicyIn",
        "GatewaySecurityPolicyOut": "_networksecurity_47_GatewaySecurityPolicyOut",
        "ListGatewaySecurityPolicyRulesResponseIn": "_networksecurity_48_ListGatewaySecurityPolicyRulesResponseIn",
        "ListGatewaySecurityPolicyRulesResponseOut": "_networksecurity_49_ListGatewaySecurityPolicyRulesResponseOut",
        "ListOperationsResponseIn": "_networksecurity_50_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networksecurity_51_ListOperationsResponseOut",
        "OperationIn": "_networksecurity_52_OperationIn",
        "OperationOut": "_networksecurity_53_OperationOut",
        "ListServerTlsPoliciesResponseIn": "_networksecurity_54_ListServerTlsPoliciesResponseIn",
        "ListServerTlsPoliciesResponseOut": "_networksecurity_55_ListServerTlsPoliciesResponseOut",
        "ValidationCAIn": "_networksecurity_56_ValidationCAIn",
        "ValidationCAOut": "_networksecurity_57_ValidationCAOut",
        "ListAuthorizationPoliciesResponseIn": "_networksecurity_58_ListAuthorizationPoliciesResponseIn",
        "ListAuthorizationPoliciesResponseOut": "_networksecurity_59_ListAuthorizationPoliciesResponseOut",
        "ListGatewaySecurityPoliciesResponseIn": "_networksecurity_60_ListGatewaySecurityPoliciesResponseIn",
        "ListGatewaySecurityPoliciesResponseOut": "_networksecurity_61_ListGatewaySecurityPoliciesResponseOut",
        "EmptyIn": "_networksecurity_62_EmptyIn",
        "EmptyOut": "_networksecurity_63_EmptyOut",
        "GoogleIamV1AuditConfigIn": "_networksecurity_64_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_networksecurity_65_GoogleIamV1AuditConfigOut",
        "AuthorizationPolicyIn": "_networksecurity_66_AuthorizationPolicyIn",
        "AuthorizationPolicyOut": "_networksecurity_67_AuthorizationPolicyOut",
        "CertificateProviderInstanceIn": "_networksecurity_68_CertificateProviderInstanceIn",
        "CertificateProviderInstanceOut": "_networksecurity_69_CertificateProviderInstanceOut",
        "GoogleIamV1PolicyIn": "_networksecurity_70_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_networksecurity_71_GoogleIamV1PolicyOut",
        "OperationMetadataIn": "_networksecurity_72_OperationMetadataIn",
        "OperationMetadataOut": "_networksecurity_73_OperationMetadataOut",
        "SourceIn": "_networksecurity_74_SourceIn",
        "SourceOut": "_networksecurity_75_SourceOut",
        "StatusIn": "_networksecurity_76_StatusIn",
        "StatusOut": "_networksecurity_77_StatusOut",
        "RuleIn": "_networksecurity_78_RuleIn",
        "RuleOut": "_networksecurity_79_RuleOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DestinationIn"] = t.struct(
        {
            "hosts": t.array(t.string()),
            "httpHeaderMatch": t.proxy(renames["HttpHeaderMatchIn"]).optional(),
            "ports": t.array(t.integer()),
            "methods": t.array(t.string()).optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "hosts": t.array(t.string()),
            "httpHeaderMatch": t.proxy(renames["HttpHeaderMatchOut"]).optional(),
            "ports": t.array(t.integer()),
            "methods": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
    types["UrlListIn"] = t.struct(
        {
            "name": t.string(),
            "description": t.string().optional(),
            "values": t.array(t.string()),
        }
    ).named(renames["UrlListIn"])
    types["UrlListOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlListOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudNetworksecurityV1GrpcEndpointIn"] = t.struct(
        {"targetUri": t.string()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"])
    types["GoogleCloudNetworksecurityV1GrpcEndpointOut"] = t.struct(
        {"targetUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"])
    types["ListClientTlsPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clientTlsPolicies": t.array(
                t.proxy(renames["ClientTlsPolicyIn"])
            ).optional(),
        }
    ).named(renames["ListClientTlsPoliciesResponseIn"])
    types["ListClientTlsPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clientTlsPolicies": t.array(
                t.proxy(renames["ClientTlsPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClientTlsPoliciesResponseOut"])
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
    types["TlsInspectionPolicyIn"] = t.struct(
        {"caPool": t.string(), "description": t.string().optional(), "name": t.string()}
    ).named(renames["TlsInspectionPolicyIn"])
    types["TlsInspectionPolicyOut"] = t.struct(
        {
            "caPool": t.string(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsInspectionPolicyOut"])
    types["ClientTlsPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
            "sni": t.string().optional(),
            "name": t.string(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAIn"])
            ).optional(),
        }
    ).named(renames["ClientTlsPolicyIn"])
    types["ClientTlsPolicyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "sni": t.string().optional(),
            "name": t.string(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientTlsPolicyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListTlsInspectionPoliciesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "tlsInspectionPolicies": t.array(
                t.proxy(renames["TlsInspectionPolicyIn"])
            ).optional(),
        }
    ).named(renames["ListTlsInspectionPoliciesResponseIn"])
    types["ListTlsInspectionPoliciesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "tlsInspectionPolicies": t.array(
                t.proxy(renames["TlsInspectionPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTlsInspectionPoliciesResponseOut"])
    types["MTLSPolicyIn"] = t.struct(
        {
            "clientValidationMode": t.string().optional(),
            "clientValidationTrustConfig": t.string().optional(),
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAIn"])),
        }
    ).named(renames["MTLSPolicyIn"])
    types["MTLSPolicyOut"] = t.struct(
        {
            "clientValidationMode": t.string().optional(),
            "clientValidationTrustConfig": t.string().optional(),
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MTLSPolicyOut"])
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
    types["HttpHeaderMatchIn"] = t.struct(
        {"headerName": t.string(), "regexMatch": t.string()}
    ).named(renames["HttpHeaderMatchIn"])
    types["HttpHeaderMatchOut"] = t.struct(
        {
            "headerName": t.string(),
            "regexMatch": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpHeaderMatchOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["ServerTlsPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "allowOpen": t.boolean().optional(),
            "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
            "name": t.string(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ServerTlsPolicyIn"])
    types["ServerTlsPolicyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "allowOpen": t.boolean().optional(),
            "mtlsPolicy": t.proxy(renames["MTLSPolicyOut"]).optional(),
            "name": t.string(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerTlsPolicyOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["GatewaySecurityPolicyRuleIn"] = t.struct(
        {
            "basicProfile": t.string(),
            "priority": t.integer(),
            "sessionMatcher": t.string(),
            "name": t.string(),
            "applicationMatcher": t.string().optional(),
            "enabled": t.boolean(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GatewaySecurityPolicyRuleIn"])
    types["GatewaySecurityPolicyRuleOut"] = t.struct(
        {
            "basicProfile": t.string(),
            "priority": t.integer(),
            "sessionMatcher": t.string(),
            "name": t.string(),
            "applicationMatcher": t.string().optional(),
            "updateTime": t.string().optional(),
            "enabled": t.boolean(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyRuleOut"])
    types["GatewaySecurityPolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "tlsInspectionPolicy": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["GatewaySecurityPolicyIn"])
    types["GatewaySecurityPolicyOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "tlsInspectionPolicy": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyOut"])
    types["ListGatewaySecurityPolicyRulesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleIn"])
            ).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseIn"])
    types["ListGatewaySecurityPolicyRulesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseOut"])
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ListAuthorizationPoliciesResponseIn"] = t.struct(
        {
            "authorizationPolicies": t.array(
                t.proxy(renames["AuthorizationPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAuthorizationPoliciesResponseIn"])
    types["ListAuthorizationPoliciesResponseOut"] = t.struct(
        {
            "authorizationPolicies": t.array(
                t.proxy(renames["AuthorizationPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuthorizationPoliciesResponseOut"])
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
    types["AuthorizationPolicyIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "action": t.string(),
            "name": t.string(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuthorizationPolicyIn"])
    types["AuthorizationPolicyOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "action": t.string(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationPolicyOut"])
    types["CertificateProviderInstanceIn"] = t.struct(
        {"pluginInstance": t.string()}
    ).named(renames["CertificateProviderInstanceIn"])
    types["CertificateProviderInstanceOut"] = t.struct(
        {
            "pluginInstance": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateProviderInstanceOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = networksecurity.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = networksecurity.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "values": t.array(t.string()),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "values": t.array(t.string()),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "values": t.array(t.string()),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "values": t.array(t.string()),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "values": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesGet"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServerTlsPoliciesTestIamPermissions"
    ] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesGetIamPolicy"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesList"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesDelete"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesSetIamPolicy"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesPatch"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "allowOpen": t.boolean().optional(),
                "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
                "serverCertificate": t.proxy(
                    renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesGet"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesDelete"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesList"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesGetIamPolicy"
    ] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesSetIamPolicy"
    ] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesTestIamPermissions"
    ] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesPatch"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
                "action": t.string(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesGet"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "caPool": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesDelete"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "caPool": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesList"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "caPool": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "caPool": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesPatch"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "caPool": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClientTlsPoliciesTestIamPermissions"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesGet"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClientTlsPoliciesGetIamPolicy"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesList"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClientTlsPoliciesSetIamPolicy"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesCreate"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesPatch"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesDelete"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesDelete"] = networksecurity.post(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "gatewaySecurityPolicyId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "tlsInspectionPolicy": t.string().optional(),
                "name": t.string(),
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
                "gatewaySecurityPolicyId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "tlsInspectionPolicy": t.string().optional(),
                "name": t.string(),
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
                "gatewaySecurityPolicyId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "tlsInspectionPolicy": t.string().optional(),
                "name": t.string(),
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
                "gatewaySecurityPolicyId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "tlsInspectionPolicy": t.string().optional(),
                "name": t.string(),
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
                "gatewaySecurityPolicyId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "tlsInspectionPolicy": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesList"
    ] = networksecurity.post(
        "v1/{parent}/rules",
        t.struct(
            {
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "parent": t.string(),
                "basicProfile": t.string(),
                "priority": t.integer(),
                "sessionMatcher": t.string(),
                "name": t.string(),
                "applicationMatcher": t.string().optional(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesDelete"
    ] = networksecurity.post(
        "v1/{parent}/rules",
        t.struct(
            {
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "parent": t.string(),
                "basicProfile": t.string(),
                "priority": t.integer(),
                "sessionMatcher": t.string(),
                "name": t.string(),
                "applicationMatcher": t.string().optional(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesGet"
    ] = networksecurity.post(
        "v1/{parent}/rules",
        t.struct(
            {
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "parent": t.string(),
                "basicProfile": t.string(),
                "priority": t.integer(),
                "sessionMatcher": t.string(),
                "name": t.string(),
                "applicationMatcher": t.string().optional(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
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
    ] = networksecurity.post(
        "v1/{parent}/rules",
        t.struct(
            {
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "parent": t.string(),
                "basicProfile": t.string(),
                "priority": t.integer(),
                "sessionMatcher": t.string(),
                "name": t.string(),
                "applicationMatcher": t.string().optional(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesCreate"
    ] = networksecurity.post(
        "v1/{parent}/rules",
        t.struct(
            {
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "parent": t.string(),
                "basicProfile": t.string(),
                "priority": t.integer(),
                "sessionMatcher": t.string(),
                "name": t.string(),
                "applicationMatcher": t.string().optional(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networksecurity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
