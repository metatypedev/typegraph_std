from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_networksecurity() -> Import:
    networksecurity = HTTPRuntime("https://networksecurity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networksecurity_1_ErrorResponse",
        "ValidationCAIn": "_networksecurity_2_ValidationCAIn",
        "ValidationCAOut": "_networksecurity_3_ValidationCAOut",
        "ListServerTlsPoliciesResponseIn": "_networksecurity_4_ListServerTlsPoliciesResponseIn",
        "ListServerTlsPoliciesResponseOut": "_networksecurity_5_ListServerTlsPoliciesResponseOut",
        "OperationMetadataIn": "_networksecurity_6_OperationMetadataIn",
        "OperationMetadataOut": "_networksecurity_7_OperationMetadataOut",
        "ListTlsInspectionPoliciesResponseIn": "_networksecurity_8_ListTlsInspectionPoliciesResponseIn",
        "ListTlsInspectionPoliciesResponseOut": "_networksecurity_9_ListTlsInspectionPoliciesResponseOut",
        "MTLSPolicyIn": "_networksecurity_10_MTLSPolicyIn",
        "MTLSPolicyOut": "_networksecurity_11_MTLSPolicyOut",
        "ListGatewaySecurityPoliciesResponseIn": "_networksecurity_12_ListGatewaySecurityPoliciesResponseIn",
        "ListGatewaySecurityPoliciesResponseOut": "_networksecurity_13_ListGatewaySecurityPoliciesResponseOut",
        "SourceIn": "_networksecurity_14_SourceIn",
        "SourceOut": "_networksecurity_15_SourceOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_networksecurity_16_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_networksecurity_17_GoogleIamV1SetIamPolicyRequestOut",
        "CancelOperationRequestIn": "_networksecurity_18_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networksecurity_19_CancelOperationRequestOut",
        "ListLocationsResponseIn": "_networksecurity_20_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networksecurity_21_ListLocationsResponseOut",
        "GoogleCloudNetworksecurityV1CertificateProviderIn": "_networksecurity_22_GoogleCloudNetworksecurityV1CertificateProviderIn",
        "GoogleCloudNetworksecurityV1CertificateProviderOut": "_networksecurity_23_GoogleCloudNetworksecurityV1CertificateProviderOut",
        "TlsInspectionPolicyIn": "_networksecurity_24_TlsInspectionPolicyIn",
        "TlsInspectionPolicyOut": "_networksecurity_25_TlsInspectionPolicyOut",
        "ListClientTlsPoliciesResponseIn": "_networksecurity_26_ListClientTlsPoliciesResponseIn",
        "ListClientTlsPoliciesResponseOut": "_networksecurity_27_ListClientTlsPoliciesResponseOut",
        "AuthorizationPolicyIn": "_networksecurity_28_AuthorizationPolicyIn",
        "AuthorizationPolicyOut": "_networksecurity_29_AuthorizationPolicyOut",
        "ClientTlsPolicyIn": "_networksecurity_30_ClientTlsPolicyIn",
        "ClientTlsPolicyOut": "_networksecurity_31_ClientTlsPolicyOut",
        "UrlListIn": "_networksecurity_32_UrlListIn",
        "UrlListOut": "_networksecurity_33_UrlListOut",
        "ListAuthorizationPoliciesResponseIn": "_networksecurity_34_ListAuthorizationPoliciesResponseIn",
        "ListAuthorizationPoliciesResponseOut": "_networksecurity_35_ListAuthorizationPoliciesResponseOut",
        "EmptyIn": "_networksecurity_36_EmptyIn",
        "EmptyOut": "_networksecurity_37_EmptyOut",
        "ExprIn": "_networksecurity_38_ExprIn",
        "ExprOut": "_networksecurity_39_ExprOut",
        "LocationIn": "_networksecurity_40_LocationIn",
        "LocationOut": "_networksecurity_41_LocationOut",
        "ListGatewaySecurityPolicyRulesResponseIn": "_networksecurity_42_ListGatewaySecurityPolicyRulesResponseIn",
        "ListGatewaySecurityPolicyRulesResponseOut": "_networksecurity_43_ListGatewaySecurityPolicyRulesResponseOut",
        "DestinationIn": "_networksecurity_44_DestinationIn",
        "DestinationOut": "_networksecurity_45_DestinationOut",
        "StatusIn": "_networksecurity_46_StatusIn",
        "StatusOut": "_networksecurity_47_StatusOut",
        "GatewaySecurityPolicyRuleIn": "_networksecurity_48_GatewaySecurityPolicyRuleIn",
        "GatewaySecurityPolicyRuleOut": "_networksecurity_49_GatewaySecurityPolicyRuleOut",
        "ServerTlsPolicyIn": "_networksecurity_50_ServerTlsPolicyIn",
        "ServerTlsPolicyOut": "_networksecurity_51_ServerTlsPolicyOut",
        "HttpHeaderMatchIn": "_networksecurity_52_HttpHeaderMatchIn",
        "HttpHeaderMatchOut": "_networksecurity_53_HttpHeaderMatchOut",
        "GoogleIamV1BindingIn": "_networksecurity_54_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_networksecurity_55_GoogleIamV1BindingOut",
        "GoogleCloudNetworksecurityV1GrpcEndpointIn": "_networksecurity_56_GoogleCloudNetworksecurityV1GrpcEndpointIn",
        "GoogleCloudNetworksecurityV1GrpcEndpointOut": "_networksecurity_57_GoogleCloudNetworksecurityV1GrpcEndpointOut",
        "GoogleIamV1AuditLogConfigIn": "_networksecurity_58_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_networksecurity_59_GoogleIamV1AuditLogConfigOut",
        "ListOperationsResponseIn": "_networksecurity_60_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networksecurity_61_ListOperationsResponseOut",
        "OperationIn": "_networksecurity_62_OperationIn",
        "OperationOut": "_networksecurity_63_OperationOut",
        "GoogleIamV1PolicyIn": "_networksecurity_64_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_networksecurity_65_GoogleIamV1PolicyOut",
        "RuleIn": "_networksecurity_66_RuleIn",
        "RuleOut": "_networksecurity_67_RuleOut",
        "ListUrlListsResponseIn": "_networksecurity_68_ListUrlListsResponseIn",
        "ListUrlListsResponseOut": "_networksecurity_69_ListUrlListsResponseOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_networksecurity_70_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_networksecurity_71_GoogleIamV1TestIamPermissionsResponseOut",
        "CertificateProviderInstanceIn": "_networksecurity_72_CertificateProviderInstanceIn",
        "CertificateProviderInstanceOut": "_networksecurity_73_CertificateProviderInstanceOut",
        "GatewaySecurityPolicyIn": "_networksecurity_74_GatewaySecurityPolicyIn",
        "GatewaySecurityPolicyOut": "_networksecurity_75_GatewaySecurityPolicyOut",
        "GoogleIamV1AuditConfigIn": "_networksecurity_76_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_networksecurity_77_GoogleIamV1AuditConfigOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_networksecurity_78_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_networksecurity_79_GoogleIamV1TestIamPermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ValidationCAIn"] = t.struct(
        {
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"]
            ).optional(),
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceIn"]
            ).optional(),
        }
    ).named(renames["ValidationCAIn"])
    types["ValidationCAOut"] = t.struct(
        {
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"]
            ).optional(),
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidationCAOut"])
    types["ListServerTlsPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serverTlsPolicies": t.array(
                t.proxy(renames["ServerTlsPolicyIn"])
            ).optional(),
        }
    ).named(renames["ListServerTlsPoliciesResponseIn"])
    types["ListServerTlsPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serverTlsPolicies": t.array(
                t.proxy(renames["ServerTlsPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServerTlsPoliciesResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListTlsInspectionPoliciesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "tlsInspectionPolicies": t.array(
                t.proxy(renames["TlsInspectionPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTlsInspectionPoliciesResponseIn"])
    types["ListTlsInspectionPoliciesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "tlsInspectionPolicies": t.array(
                t.proxy(renames["TlsInspectionPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTlsInspectionPoliciesResponseOut"])
    types["MTLSPolicyIn"] = t.struct(
        {
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAIn"])),
            "clientValidationTrustConfig": t.string().optional(),
            "clientValidationMode": t.string().optional(),
        }
    ).named(renames["MTLSPolicyIn"])
    types["MTLSPolicyOut"] = t.struct(
        {
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAOut"])),
            "clientValidationTrustConfig": t.string().optional(),
            "clientValidationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MTLSPolicyOut"])
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
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["TlsInspectionPolicyIn"] = t.struct(
        {"name": t.string(), "caPool": t.string(), "description": t.string().optional()}
    ).named(renames["TlsInspectionPolicyIn"])
    types["TlsInspectionPolicyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "caPool": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TlsInspectionPolicyOut"])
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
    types["AuthorizationPolicyIn"] = t.struct(
        {
            "name": t.string(),
            "action": t.string(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuthorizationPolicyIn"])
    types["AuthorizationPolicyOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string(),
            "action": t.string(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationPolicyOut"])
    types["ClientTlsPolicyIn"] = t.struct(
        {
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAIn"])
            ).optional(),
            "name": t.string(),
            "sni": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ClientTlsPolicyIn"])
    types["ClientTlsPolicyOut"] = t.struct(
        {
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "sni": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientTlsPolicyOut"])
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
            "name": t.string(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "values": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlListOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListGatewaySecurityPolicyRulesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseIn"])
    types["ListGatewaySecurityPolicyRulesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseOut"])
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
    types["GatewaySecurityPolicyRuleIn"] = t.struct(
        {
            "applicationMatcher": t.string().optional(),
            "enabled": t.boolean(),
            "name": t.string(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "sessionMatcher": t.string(),
            "description": t.string().optional(),
            "basicProfile": t.string(),
            "priority": t.integer(),
        }
    ).named(renames["GatewaySecurityPolicyRuleIn"])
    types["GatewaySecurityPolicyRuleOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "applicationMatcher": t.string().optional(),
            "enabled": t.boolean(),
            "name": t.string(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "sessionMatcher": t.string(),
            "description": t.string().optional(),
            "basicProfile": t.string(),
            "priority": t.integer(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyRuleOut"])
    types["ServerTlsPolicyIn"] = t.struct(
        {
            "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
            "description": t.string().optional(),
            "allowOpen": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
            "name": t.string(),
        }
    ).named(renames["ServerTlsPolicyIn"])
    types["ServerTlsPolicyOut"] = t.struct(
        {
            "mtlsPolicy": t.proxy(renames["MTLSPolicyOut"]).optional(),
            "description": t.string().optional(),
            "allowOpen": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerTlsPolicyOut"])
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
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudNetworksecurityV1GrpcEndpointIn"] = t.struct(
        {"targetUri": t.string()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"])
    types["GoogleCloudNetworksecurityV1GrpcEndpointOut"] = t.struct(
        {"targetUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"])
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
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["RuleIn"] = t.struct(
        {
            "destinations": t.array(t.proxy(renames["DestinationIn"])).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "destinations": t.array(t.proxy(renames["DestinationOut"])).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["ListUrlListsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "urlLists": t.array(t.proxy(renames["UrlListIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListUrlListsResponseIn"])
    types["ListUrlListsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "urlLists": t.array(t.proxy(renames["UrlListOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUrlListsResponseOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["CertificateProviderInstanceIn"] = t.struct(
        {"pluginInstance": t.string()}
    ).named(renames["CertificateProviderInstanceIn"])
    types["CertificateProviderInstanceOut"] = t.struct(
        {
            "pluginInstance": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateProviderInstanceOut"])
    types["GatewaySecurityPolicyIn"] = t.struct(
        {
            "name": t.string(),
            "tlsInspectionPolicy": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GatewaySecurityPolicyIn"])
    types["GatewaySecurityPolicyOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string(),
            "tlsInspectionPolicy": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyOut"])
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
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])

    functions = {}
    functions["projectsLocationsGet"] = networksecurity.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesCreate"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesPatch"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesDelete"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesSetIamPolicy"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesTestIamPermissions"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesList"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesGetIamPolicy"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesGet"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizationPolicyOut"]),
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
    functions["projectsLocationsTlsInspectionPoliciesCreate"] = networksecurity.get(
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
    functions["projectsLocationsTlsInspectionPoliciesList"] = networksecurity.get(
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
    functions["projectsLocationsUrlListsGet"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
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
                "updateMask": t.string().optional(),
                "name": t.string(),
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
                "updateMask": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "values": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
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
                "updateMask": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "values": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesCreate"] = networksecurity.get(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGatewaySecurityPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesPatch"] = networksecurity.get(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGatewaySecurityPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesDelete"] = networksecurity.get(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGatewaySecurityPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesGet"] = networksecurity.get(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGatewaySecurityPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesList"] = networksecurity.get(
        "v1/{parent}/gatewaySecurityPolicies",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGatewaySecurityPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesPatch"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesList"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesCreate"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesGet"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesRulesDelete"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsOperationsList"] = networksecurity.delete(
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
    functions["projectsLocationsOperationsDelete"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsClientTlsPoliciesCreate"] = networksecurity.delete(
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
    functions["projectsLocationsClientTlsPoliciesPatch"] = networksecurity.delete(
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
    functions["projectsLocationsClientTlsPoliciesList"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
    functions["projectsLocationsClientTlsPoliciesDelete"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesSetIamPolicy"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesCreate"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesDelete"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesGet"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsServerTlsPoliciesTestIamPermissions"
    ] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesList"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesPatch"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesGetIamPolicy"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="networksecurity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
