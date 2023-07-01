from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_networksecurity():
    networksecurity = HTTPRuntime("https://networksecurity.googleapis.com/")

    renames = {
        "ErrorResponse": "_networksecurity_1_ErrorResponse",
        "GatewaySecurityPolicyRuleIn": "_networksecurity_2_GatewaySecurityPolicyRuleIn",
        "GatewaySecurityPolicyRuleOut": "_networksecurity_3_GatewaySecurityPolicyRuleOut",
        "MTLSPolicyIn": "_networksecurity_4_MTLSPolicyIn",
        "MTLSPolicyOut": "_networksecurity_5_MTLSPolicyOut",
        "ListAddressGroupReferencesResponseAddressGroupReferenceIn": "_networksecurity_6_ListAddressGroupReferencesResponseAddressGroupReferenceIn",
        "ListAddressGroupReferencesResponseAddressGroupReferenceOut": "_networksecurity_7_ListAddressGroupReferencesResponseAddressGroupReferenceOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_networksecurity_8_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_networksecurity_9_GoogleIamV1SetIamPolicyRequestOut",
        "TlsInspectionPolicyIn": "_networksecurity_10_TlsInspectionPolicyIn",
        "TlsInspectionPolicyOut": "_networksecurity_11_TlsInspectionPolicyOut",
        "ListAddressGroupReferencesResponseIn": "_networksecurity_12_ListAddressGroupReferencesResponseIn",
        "ListAddressGroupReferencesResponseOut": "_networksecurity_13_ListAddressGroupReferencesResponseOut",
        "ListOperationsResponseIn": "_networksecurity_14_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_networksecurity_15_ListOperationsResponseOut",
        "AddressGroupIn": "_networksecurity_16_AddressGroupIn",
        "AddressGroupOut": "_networksecurity_17_AddressGroupOut",
        "GoogleIamV1AuditLogConfigIn": "_networksecurity_18_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_networksecurity_19_GoogleIamV1AuditLogConfigOut",
        "UrlListIn": "_networksecurity_20_UrlListIn",
        "UrlListOut": "_networksecurity_21_UrlListOut",
        "LocationIn": "_networksecurity_22_LocationIn",
        "LocationOut": "_networksecurity_23_LocationOut",
        "DestinationIn": "_networksecurity_24_DestinationIn",
        "DestinationOut": "_networksecurity_25_DestinationOut",
        "GoogleIamV1PolicyIn": "_networksecurity_26_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_networksecurity_27_GoogleIamV1PolicyOut",
        "CancelOperationRequestIn": "_networksecurity_28_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_networksecurity_29_CancelOperationRequestOut",
        "CertificateProviderInstanceIn": "_networksecurity_30_CertificateProviderInstanceIn",
        "CertificateProviderInstanceOut": "_networksecurity_31_CertificateProviderInstanceOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_networksecurity_32_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_networksecurity_33_GoogleIamV1TestIamPermissionsResponseOut",
        "ListGatewaySecurityPoliciesResponseIn": "_networksecurity_34_ListGatewaySecurityPoliciesResponseIn",
        "ListGatewaySecurityPoliciesResponseOut": "_networksecurity_35_ListGatewaySecurityPoliciesResponseOut",
        "CloneAddressGroupItemsRequestIn": "_networksecurity_36_CloneAddressGroupItemsRequestIn",
        "CloneAddressGroupItemsRequestOut": "_networksecurity_37_CloneAddressGroupItemsRequestOut",
        "RuleIn": "_networksecurity_38_RuleIn",
        "RuleOut": "_networksecurity_39_RuleOut",
        "HttpHeaderMatchIn": "_networksecurity_40_HttpHeaderMatchIn",
        "HttpHeaderMatchOut": "_networksecurity_41_HttpHeaderMatchOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_networksecurity_42_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_networksecurity_43_GoogleIamV1TestIamPermissionsRequestOut",
        "ListUrlListsResponseIn": "_networksecurity_44_ListUrlListsResponseIn",
        "ListUrlListsResponseOut": "_networksecurity_45_ListUrlListsResponseOut",
        "SourceIn": "_networksecurity_46_SourceIn",
        "SourceOut": "_networksecurity_47_SourceOut",
        "ListClientTlsPoliciesResponseIn": "_networksecurity_48_ListClientTlsPoliciesResponseIn",
        "ListClientTlsPoliciesResponseOut": "_networksecurity_49_ListClientTlsPoliciesResponseOut",
        "ExprIn": "_networksecurity_50_ExprIn",
        "ExprOut": "_networksecurity_51_ExprOut",
        "ListTlsInspectionPoliciesResponseIn": "_networksecurity_52_ListTlsInspectionPoliciesResponseIn",
        "ListTlsInspectionPoliciesResponseOut": "_networksecurity_53_ListTlsInspectionPoliciesResponseOut",
        "GoogleCloudNetworksecurityV1CertificateProviderIn": "_networksecurity_54_GoogleCloudNetworksecurityV1CertificateProviderIn",
        "GoogleCloudNetworksecurityV1CertificateProviderOut": "_networksecurity_55_GoogleCloudNetworksecurityV1CertificateProviderOut",
        "ListServerTlsPoliciesResponseIn": "_networksecurity_56_ListServerTlsPoliciesResponseIn",
        "ListServerTlsPoliciesResponseOut": "_networksecurity_57_ListServerTlsPoliciesResponseOut",
        "OperationIn": "_networksecurity_58_OperationIn",
        "OperationOut": "_networksecurity_59_OperationOut",
        "GatewaySecurityPolicyIn": "_networksecurity_60_GatewaySecurityPolicyIn",
        "GatewaySecurityPolicyOut": "_networksecurity_61_GatewaySecurityPolicyOut",
        "ListAddressGroupsResponseIn": "_networksecurity_62_ListAddressGroupsResponseIn",
        "ListAddressGroupsResponseOut": "_networksecurity_63_ListAddressGroupsResponseOut",
        "RemoveAddressGroupItemsRequestIn": "_networksecurity_64_RemoveAddressGroupItemsRequestIn",
        "RemoveAddressGroupItemsRequestOut": "_networksecurity_65_RemoveAddressGroupItemsRequestOut",
        "ClientTlsPolicyIn": "_networksecurity_66_ClientTlsPolicyIn",
        "ClientTlsPolicyOut": "_networksecurity_67_ClientTlsPolicyOut",
        "ListGatewaySecurityPolicyRulesResponseIn": "_networksecurity_68_ListGatewaySecurityPolicyRulesResponseIn",
        "ListGatewaySecurityPolicyRulesResponseOut": "_networksecurity_69_ListGatewaySecurityPolicyRulesResponseOut",
        "GoogleIamV1BindingIn": "_networksecurity_70_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_networksecurity_71_GoogleIamV1BindingOut",
        "GoogleCloudNetworksecurityV1GrpcEndpointIn": "_networksecurity_72_GoogleCloudNetworksecurityV1GrpcEndpointIn",
        "GoogleCloudNetworksecurityV1GrpcEndpointOut": "_networksecurity_73_GoogleCloudNetworksecurityV1GrpcEndpointOut",
        "AddAddressGroupItemsRequestIn": "_networksecurity_74_AddAddressGroupItemsRequestIn",
        "AddAddressGroupItemsRequestOut": "_networksecurity_75_AddAddressGroupItemsRequestOut",
        "ServerTlsPolicyIn": "_networksecurity_76_ServerTlsPolicyIn",
        "ServerTlsPolicyOut": "_networksecurity_77_ServerTlsPolicyOut",
        "AuthorizationPolicyIn": "_networksecurity_78_AuthorizationPolicyIn",
        "AuthorizationPolicyOut": "_networksecurity_79_AuthorizationPolicyOut",
        "EmptyIn": "_networksecurity_80_EmptyIn",
        "EmptyOut": "_networksecurity_81_EmptyOut",
        "StatusIn": "_networksecurity_82_StatusIn",
        "StatusOut": "_networksecurity_83_StatusOut",
        "ListAuthorizationPoliciesResponseIn": "_networksecurity_84_ListAuthorizationPoliciesResponseIn",
        "ListAuthorizationPoliciesResponseOut": "_networksecurity_85_ListAuthorizationPoliciesResponseOut",
        "ListLocationsResponseIn": "_networksecurity_86_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_networksecurity_87_ListLocationsResponseOut",
        "OperationMetadataIn": "_networksecurity_88_OperationMetadataIn",
        "OperationMetadataOut": "_networksecurity_89_OperationMetadataOut",
        "ValidationCAIn": "_networksecurity_90_ValidationCAIn",
        "ValidationCAOut": "_networksecurity_91_ValidationCAOut",
        "GoogleIamV1AuditConfigIn": "_networksecurity_92_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_networksecurity_93_GoogleIamV1AuditConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GatewaySecurityPolicyRuleIn"] = t.struct(
        {
            "basicProfile": t.string(),
            "enabled": t.boolean(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "sessionMatcher": t.string(),
            "applicationMatcher": t.string().optional(),
            "description": t.string().optional(),
            "priority": t.integer(),
            "name": t.string(),
        }
    ).named(renames["GatewaySecurityPolicyRuleIn"])
    types["GatewaySecurityPolicyRuleOut"] = t.struct(
        {
            "basicProfile": t.string(),
            "createTime": t.string().optional(),
            "enabled": t.boolean(),
            "tlsInspectionEnabled": t.boolean().optional(),
            "sessionMatcher": t.string(),
            "applicationMatcher": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "priority": t.integer(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyRuleOut"])
    types["MTLSPolicyIn"] = t.struct(
        {
            "clientValidationMode": t.string().optional(),
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAIn"])),
            "clientValidationTrustConfig": t.string().optional(),
        }
    ).named(renames["MTLSPolicyIn"])
    types["MTLSPolicyOut"] = t.struct(
        {
            "clientValidationMode": t.string().optional(),
            "clientValidationCa": t.array(t.proxy(renames["ValidationCAOut"])),
            "clientValidationTrustConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MTLSPolicyOut"])
    types["ListAddressGroupReferencesResponseAddressGroupReferenceIn"] = t.struct(
        {
            "firewallPolicy": t.string().optional(),
            "rulePriority": t.integer().optional(),
        }
    ).named(renames["ListAddressGroupReferencesResponseAddressGroupReferenceIn"])
    types["ListAddressGroupReferencesResponseAddressGroupReferenceOut"] = t.struct(
        {
            "firewallPolicy": t.string().optional(),
            "rulePriority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAddressGroupReferencesResponseAddressGroupReferenceOut"])
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
    types["ListAddressGroupReferencesResponseIn"] = t.struct(
        {
            "addressGroupReferences": t.array(
                t.proxy(
                    renames["ListAddressGroupReferencesResponseAddressGroupReferenceIn"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAddressGroupReferencesResponseIn"])
    types["ListAddressGroupReferencesResponseOut"] = t.struct(
        {
            "addressGroupReferences": t.array(
                t.proxy(
                    renames[
                        "ListAddressGroupReferencesResponseAddressGroupReferenceOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAddressGroupReferencesResponseOut"])
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
    types["AddressGroupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "items": t.array(t.string()).optional(),
            "type": t.string(),
            "capacity": t.integer(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["AddressGroupIn"])
    types["AddressGroupOut"] = t.struct(
        {
            "description": t.string().optional(),
            "items": t.array(t.string()).optional(),
            "type": t.string(),
            "capacity": t.integer(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "selfLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressGroupOut"])
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
    types["UrlListIn"] = t.struct(
        {
            "values": t.array(t.string()),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["UrlListIn"])
    types["UrlListOut"] = t.struct(
        {
            "values": t.array(t.string()),
            "description": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlListOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DestinationIn"] = t.struct(
        {
            "methods": t.array(t.string()).optional(),
            "hosts": t.array(t.string()),
            "ports": t.array(t.integer()),
            "httpHeaderMatch": t.proxy(renames["HttpHeaderMatchIn"]).optional(),
        }
    ).named(renames["DestinationIn"])
    types["DestinationOut"] = t.struct(
        {
            "methods": t.array(t.string()).optional(),
            "hosts": t.array(t.string()),
            "ports": t.array(t.integer()),
            "httpHeaderMatch": t.proxy(renames["HttpHeaderMatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["CertificateProviderInstanceIn"] = t.struct(
        {"pluginInstance": t.string()}
    ).named(renames["CertificateProviderInstanceIn"])
    types["CertificateProviderInstanceOut"] = t.struct(
        {
            "pluginInstance": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateProviderInstanceOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["ListGatewaySecurityPoliciesResponseIn"] = t.struct(
        {
            "gatewaySecurityPolicies": t.array(
                t.proxy(renames["GatewaySecurityPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListGatewaySecurityPoliciesResponseIn"])
    types["ListGatewaySecurityPoliciesResponseOut"] = t.struct(
        {
            "gatewaySecurityPolicies": t.array(
                t.proxy(renames["GatewaySecurityPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaySecurityPoliciesResponseOut"])
    types["CloneAddressGroupItemsRequestIn"] = t.struct(
        {"sourceAddressGroup": t.string(), "requestId": t.string().optional()}
    ).named(renames["CloneAddressGroupItemsRequestIn"])
    types["CloneAddressGroupItemsRequestOut"] = t.struct(
        {
            "sourceAddressGroup": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneAddressGroupItemsRequestOut"])
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
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
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
    types["SourceIn"] = t.struct(
        {
            "ipBlocks": t.array(t.string()).optional(),
            "principals": t.array(t.string()).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "ipBlocks": t.array(t.string()).optional(),
            "principals": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["GoogleCloudNetworksecurityV1CertificateProviderIn"] = t.struct(
        {
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"]
            ).optional(),
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudNetworksecurityV1CertificateProviderIn"])
    types["GoogleCloudNetworksecurityV1CertificateProviderOut"] = t.struct(
        {
            "grpcEndpoint": t.proxy(
                renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"]
            ).optional(),
            "certificateProviderInstance": t.proxy(
                renames["CertificateProviderInstanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudNetworksecurityV1CertificateProviderOut"])
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
    types["GatewaySecurityPolicyIn"] = t.struct(
        {
            "tlsInspectionPolicy": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["GatewaySecurityPolicyIn"])
    types["GatewaySecurityPolicyOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "tlsInspectionPolicy": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GatewaySecurityPolicyOut"])
    types["ListAddressGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "addressGroups": t.array(t.proxy(renames["AddressGroupIn"])).optional(),
        }
    ).named(renames["ListAddressGroupsResponseIn"])
    types["ListAddressGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "addressGroups": t.array(t.proxy(renames["AddressGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAddressGroupsResponseOut"])
    types["RemoveAddressGroupItemsRequestIn"] = t.struct(
        {"items": t.array(t.string()), "requestId": t.string().optional()}
    ).named(renames["RemoveAddressGroupItemsRequestIn"])
    types["RemoveAddressGroupItemsRequestOut"] = t.struct(
        {
            "items": t.array(t.string()),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAddressGroupItemsRequestOut"])
    types["ClientTlsPolicyIn"] = t.struct(
        {
            "sni": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAIn"])
            ).optional(),
            "description": t.string().optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
            "name": t.string(),
        }
    ).named(renames["ClientTlsPolicyIn"])
    types["ClientTlsPolicyOut"] = t.struct(
        {
            "sni": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverValidationCa": t.array(
                t.proxy(renames["ValidationCAOut"])
            ).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "clientCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientTlsPolicyOut"])
    types["ListGatewaySecurityPolicyRulesResponseIn"] = t.struct(
        {
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseIn"])
    types["ListGatewaySecurityPolicyRulesResponseOut"] = t.struct(
        {
            "gatewaySecurityPolicyRules": t.array(
                t.proxy(renames["GatewaySecurityPolicyRuleOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGatewaySecurityPolicyRulesResponseOut"])
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
    types["GoogleCloudNetworksecurityV1GrpcEndpointIn"] = t.struct(
        {"targetUri": t.string()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointIn"])
    types["GoogleCloudNetworksecurityV1GrpcEndpointOut"] = t.struct(
        {"targetUri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudNetworksecurityV1GrpcEndpointOut"])
    types["AddAddressGroupItemsRequestIn"] = t.struct(
        {"requestId": t.string().optional(), "items": t.array(t.string())}
    ).named(renames["AddAddressGroupItemsRequestIn"])
    types["AddAddressGroupItemsRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "items": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddAddressGroupItemsRequestOut"])
    types["ServerTlsPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderIn"]
            ).optional(),
            "mtlsPolicy": t.proxy(renames["MTLSPolicyIn"]).optional(),
            "description": t.string().optional(),
            "allowOpen": t.boolean().optional(),
            "name": t.string(),
        }
    ).named(renames["ServerTlsPolicyIn"])
    types["ServerTlsPolicyOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serverCertificate": t.proxy(
                renames["GoogleCloudNetworksecurityV1CertificateProviderOut"]
            ).optional(),
            "mtlsPolicy": t.proxy(renames["MTLSPolicyOut"]).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "allowOpen": t.boolean().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerTlsPolicyOut"])
    types["AuthorizationPolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "action": t.string(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
        }
    ).named(renames["AuthorizationPolicyIn"])
    types["AuthorizationPolicyOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "action": t.string(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationPolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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

    functions = {}
    functions["organizationsLocationsAddressGroupsCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsAddressGroupsGet"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsAddressGroupsList"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsAddressGroupsDelete"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsAddressGroupsCloneItems"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsAddressGroupsAddItems"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsAddressGroupsListReferences"
    ] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsAddressGroupsRemoveItems"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsAddressGroupsPatch"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "items": t.array(t.string()).optional(),
                "type": t.string(),
                "capacity": t.integer(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsList"] = networksecurity.post(
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
    functions["organizationsLocationsOperationsGet"] = networksecurity.post(
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
    functions["organizationsLocationsOperationsDelete"] = networksecurity.post(
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
    functions["organizationsLocationsOperationsCancel"] = networksecurity.post(
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
    functions["projectsLocationsClientTlsPoliciesList"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesGetIamPolicy"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesCreate"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesPatch"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesDelete"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClientTlsPoliciesTestIamPermissions"
    ] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesSetIamPolicy"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientTlsPoliciesGet"] = networksecurity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ClientTlsPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTlsInspectionPoliciesCreate"] = networksecurity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
                "caPool": t.string(),
                "description": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string().optional(),
                "caPool": t.string(),
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
    functions["projectsLocationsAddressGroupsListReferences"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsCloneItems"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsPatch"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsRemoveItems"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsGetIamPolicy"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsGet"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsList"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsDelete"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsAddItems"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsSetIamPolicy"] = networksecurity.post(
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
    functions["projectsLocationsAddressGroupsCreate"] = networksecurity.post(
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
        "projectsLocationsAddressGroupsTestIamPermissions"
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
    functions["projectsLocationsGatewaySecurityPoliciesPatch"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesCreate"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesList"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaySecurityPoliciesGet"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGatewaySecurityPoliciesDelete"
    ] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
                "parent": t.string(),
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "basicProfile": t.string(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "sessionMatcher": t.string(),
                "applicationMatcher": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer(),
                "name": t.string(),
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
                "parent": t.string(),
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "basicProfile": t.string(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "sessionMatcher": t.string(),
                "applicationMatcher": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer(),
                "name": t.string(),
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
                "parent": t.string(),
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "basicProfile": t.string(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "sessionMatcher": t.string(),
                "applicationMatcher": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer(),
                "name": t.string(),
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
                "parent": t.string(),
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "basicProfile": t.string(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "sessionMatcher": t.string(),
                "applicationMatcher": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer(),
                "name": t.string(),
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
                "parent": t.string(),
                "gatewaySecurityPolicyRuleId": t.string().optional(),
                "basicProfile": t.string(),
                "enabled": t.boolean(),
                "tlsInspectionEnabled": t.boolean().optional(),
                "sessionMatcher": t.string(),
                "applicationMatcher": t.string().optional(),
                "description": t.string().optional(),
                "priority": t.integer(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesCreate"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesSetIamPolicy"
    ] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesPatch"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesGet"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesTestIamPermissions"
    ] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesDelete"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAuthorizationPoliciesList"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsAuthorizationPoliciesGetIamPolicy"
    ] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsServerTlsPoliciesSetIamPolicy"] = networksecurity.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsList"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsGet"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsCreate"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsPatch"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUrlListsDelete"] = networksecurity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
