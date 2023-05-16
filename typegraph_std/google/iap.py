from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_iap() -> Import:
    iap = HTTPRuntime("https://iap.googleapis.com/")

    renames = {
        "ErrorResponse": "_iap_1_ErrorResponse",
        "ExprIn": "_iap_2_ExprIn",
        "ExprOut": "_iap_3_ExprOut",
        "ListIdentityAwareProxyClientsResponseIn": "_iap_4_ListIdentityAwareProxyClientsResponseIn",
        "ListIdentityAwareProxyClientsResponseOut": "_iap_5_ListIdentityAwareProxyClientsResponseOut",
        "ReauthSettingsIn": "_iap_6_ReauthSettingsIn",
        "ReauthSettingsOut": "_iap_7_ReauthSettingsOut",
        "AllowedDomainsSettingsIn": "_iap_8_AllowedDomainsSettingsIn",
        "AllowedDomainsSettingsOut": "_iap_9_AllowedDomainsSettingsOut",
        "PolicyNameIn": "_iap_10_PolicyNameIn",
        "PolicyNameOut": "_iap_11_PolicyNameOut",
        "AccessDeniedPageSettingsIn": "_iap_12_AccessDeniedPageSettingsIn",
        "AccessDeniedPageSettingsOut": "_iap_13_AccessDeniedPageSettingsOut",
        "TestIamPermissionsResponseIn": "_iap_14_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_iap_15_TestIamPermissionsResponseOut",
        "GetPolicyOptionsIn": "_iap_16_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_iap_17_GetPolicyOptionsOut",
        "IapSettingsIn": "_iap_18_IapSettingsIn",
        "IapSettingsOut": "_iap_19_IapSettingsOut",
        "CsmSettingsIn": "_iap_20_CsmSettingsIn",
        "CsmSettingsOut": "_iap_21_CsmSettingsOut",
        "ListBrandsResponseIn": "_iap_22_ListBrandsResponseIn",
        "ListBrandsResponseOut": "_iap_23_ListBrandsResponseOut",
        "PolicyIn": "_iap_24_PolicyIn",
        "PolicyOut": "_iap_25_PolicyOut",
        "EmptyIn": "_iap_26_EmptyIn",
        "EmptyOut": "_iap_27_EmptyOut",
        "OAuthSettingsIn": "_iap_28_OAuthSettingsIn",
        "OAuthSettingsOut": "_iap_29_OAuthSettingsOut",
        "ResourceIn": "_iap_30_ResourceIn",
        "ResourceOut": "_iap_31_ResourceOut",
        "TunnelDestGroupIn": "_iap_32_TunnelDestGroupIn",
        "TunnelDestGroupOut": "_iap_33_TunnelDestGroupOut",
        "TestIamPermissionsRequestIn": "_iap_34_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_iap_35_TestIamPermissionsRequestOut",
        "CorsSettingsIn": "_iap_36_CorsSettingsIn",
        "CorsSettingsOut": "_iap_37_CorsSettingsOut",
        "ListTunnelDestGroupsResponseIn": "_iap_38_ListTunnelDestGroupsResponseIn",
        "ListTunnelDestGroupsResponseOut": "_iap_39_ListTunnelDestGroupsResponseOut",
        "SetIamPolicyRequestIn": "_iap_40_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_iap_41_SetIamPolicyRequestOut",
        "GetIamPolicyRequestIn": "_iap_42_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_iap_43_GetIamPolicyRequestOut",
        "IdentityAwareProxyClientIn": "_iap_44_IdentityAwareProxyClientIn",
        "IdentityAwareProxyClientOut": "_iap_45_IdentityAwareProxyClientOut",
        "GcipSettingsIn": "_iap_46_GcipSettingsIn",
        "GcipSettingsOut": "_iap_47_GcipSettingsOut",
        "ApplicationSettingsIn": "_iap_48_ApplicationSettingsIn",
        "ApplicationSettingsOut": "_iap_49_ApplicationSettingsOut",
        "AttributePropagationSettingsIn": "_iap_50_AttributePropagationSettingsIn",
        "AttributePropagationSettingsOut": "_iap_51_AttributePropagationSettingsOut",
        "BindingIn": "_iap_52_BindingIn",
        "BindingOut": "_iap_53_BindingOut",
        "AccessSettingsIn": "_iap_54_AccessSettingsIn",
        "AccessSettingsOut": "_iap_55_AccessSettingsOut",
        "ResetIdentityAwareProxyClientSecretRequestIn": "_iap_56_ResetIdentityAwareProxyClientSecretRequestIn",
        "ResetIdentityAwareProxyClientSecretRequestOut": "_iap_57_ResetIdentityAwareProxyClientSecretRequestOut",
        "PolicyDelegationSettingsIn": "_iap_58_PolicyDelegationSettingsIn",
        "PolicyDelegationSettingsOut": "_iap_59_PolicyDelegationSettingsOut",
        "BrandIn": "_iap_60_BrandIn",
        "BrandOut": "_iap_61_BrandOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListIdentityAwareProxyClientsResponseIn"] = t.struct(
        {
            "identityAwareProxyClients": t.array(
                t.proxy(renames["IdentityAwareProxyClientIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListIdentityAwareProxyClientsResponseIn"])
    types["ListIdentityAwareProxyClientsResponseOut"] = t.struct(
        {
            "identityAwareProxyClients": t.array(
                t.proxy(renames["IdentityAwareProxyClientOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListIdentityAwareProxyClientsResponseOut"])
    types["ReauthSettingsIn"] = t.struct(
        {
            "policyType": t.string().optional(),
            "method": t.string().optional(),
            "maxAge": t.string().optional(),
        }
    ).named(renames["ReauthSettingsIn"])
    types["ReauthSettingsOut"] = t.struct(
        {
            "policyType": t.string().optional(),
            "method": t.string().optional(),
            "maxAge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReauthSettingsOut"])
    types["AllowedDomainsSettingsIn"] = t.struct(
        {"enable": t.boolean().optional(), "domains": t.array(t.string()).optional()}
    ).named(renames["AllowedDomainsSettingsIn"])
    types["AllowedDomainsSettingsOut"] = t.struct(
        {
            "enable": t.boolean().optional(),
            "domains": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedDomainsSettingsOut"])
    types["PolicyNameIn"] = t.struct(
        {
            "region": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PolicyNameIn"])
    types["PolicyNameOut"] = t.struct(
        {
            "region": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyNameOut"])
    types["AccessDeniedPageSettingsIn"] = t.struct(
        {
            "generateTroubleshootingUri": t.boolean().optional(),
            "remediationTokenGenerationEnabled": t.boolean().optional(),
            "accessDeniedPageUri": t.string().optional(),
        }
    ).named(renames["AccessDeniedPageSettingsIn"])
    types["AccessDeniedPageSettingsOut"] = t.struct(
        {
            "generateTroubleshootingUri": t.boolean().optional(),
            "remediationTokenGenerationEnabled": t.boolean().optional(),
            "accessDeniedPageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessDeniedPageSettingsOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["IapSettingsIn"] = t.struct(
        {
            "name": t.string(),
            "applicationSettings": t.proxy(renames["ApplicationSettingsIn"]).optional(),
            "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
        }
    ).named(renames["IapSettingsIn"])
    types["IapSettingsOut"] = t.struct(
        {
            "name": t.string(),
            "applicationSettings": t.proxy(
                renames["ApplicationSettingsOut"]
            ).optional(),
            "accessSettings": t.proxy(renames["AccessSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapSettingsOut"])
    types["CsmSettingsIn"] = t.struct({"rctokenAud": t.string().optional()}).named(
        renames["CsmSettingsIn"]
    )
    types["CsmSettingsOut"] = t.struct(
        {
            "rctokenAud": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsmSettingsOut"])
    types["ListBrandsResponseIn"] = t.struct(
        {"brands": t.array(t.proxy(renames["BrandIn"])).optional()}
    ).named(renames["ListBrandsResponseIn"])
    types["ListBrandsResponseOut"] = t.struct(
        {
            "brands": t.array(t.proxy(renames["BrandOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBrandsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OAuthSettingsIn"] = t.struct({"loginHint": t.string().optional()}).named(
        renames["OAuthSettingsIn"]
    )
    types["OAuthSettingsOut"] = t.struct(
        {
            "loginHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthSettingsOut"])
    types["ResourceIn"] = t.struct(
        {
            "service": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "service": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["TunnelDestGroupIn"] = t.struct(
        {
            "fqdns": t.array(t.string()).optional(),
            "cidrs": t.array(t.string()).optional(),
            "name": t.string(),
        }
    ).named(renames["TunnelDestGroupIn"])
    types["TunnelDestGroupOut"] = t.struct(
        {
            "fqdns": t.array(t.string()).optional(),
            "cidrs": t.array(t.string()).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TunnelDestGroupOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["CorsSettingsIn"] = t.struct(
        {"allowHttpOptions": t.boolean().optional()}
    ).named(renames["CorsSettingsIn"])
    types["CorsSettingsOut"] = t.struct(
        {
            "allowHttpOptions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorsSettingsOut"])
    types["ListTunnelDestGroupsResponseIn"] = t.struct(
        {
            "tunnelDestGroups": t.array(
                t.proxy(renames["TunnelDestGroupIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTunnelDestGroupsResponseIn"])
    types["ListTunnelDestGroupsResponseOut"] = t.struct(
        {
            "tunnelDestGroups": t.array(
                t.proxy(renames["TunnelDestGroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTunnelDestGroupsResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["IdentityAwareProxyClientIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["IdentityAwareProxyClientIn"])
    types["IdentityAwareProxyClientOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityAwareProxyClientOut"])
    types["GcipSettingsIn"] = t.struct(
        {
            "tenantIds": t.array(t.string()).optional(),
            "loginPageUri": t.string().optional(),
        }
    ).named(renames["GcipSettingsIn"])
    types["GcipSettingsOut"] = t.struct(
        {
            "tenantIds": t.array(t.string()).optional(),
            "loginPageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcipSettingsOut"])
    types["ApplicationSettingsIn"] = t.struct(
        {
            "cookieDomain": t.string().optional(),
            "attributePropagationSettings": t.proxy(
                renames["AttributePropagationSettingsIn"]
            ).optional(),
            "csmSettings": t.proxy(renames["CsmSettingsIn"]).optional(),
            "accessDeniedPageSettings": t.proxy(
                renames["AccessDeniedPageSettingsIn"]
            ).optional(),
        }
    ).named(renames["ApplicationSettingsIn"])
    types["ApplicationSettingsOut"] = t.struct(
        {
            "cookieDomain": t.string().optional(),
            "attributePropagationSettings": t.proxy(
                renames["AttributePropagationSettingsOut"]
            ).optional(),
            "csmSettings": t.proxy(renames["CsmSettingsOut"]).optional(),
            "accessDeniedPageSettings": t.proxy(
                renames["AccessDeniedPageSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationSettingsOut"])
    types["AttributePropagationSettingsIn"] = t.struct(
        {
            "outputCredentials": t.array(t.string()).optional(),
            "expression": t.string().optional(),
            "enable": t.boolean().optional(),
        }
    ).named(renames["AttributePropagationSettingsIn"])
    types["AttributePropagationSettingsOut"] = t.struct(
        {
            "outputCredentials": t.array(t.string()).optional(),
            "expression": t.string().optional(),
            "enable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributePropagationSettingsOut"])
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
    types["AccessSettingsIn"] = t.struct(
        {
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsIn"]
            ).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsIn"]).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsIn"]
            ).optional(),
            "corsSettings": t.proxy(renames["CorsSettingsIn"]).optional(),
            "gcipSettings": t.proxy(renames["GcipSettingsIn"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsIn"]).optional(),
        }
    ).named(renames["AccessSettingsIn"])
    types["AccessSettingsOut"] = t.struct(
        {
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsOut"]
            ).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsOut"]).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsOut"]
            ).optional(),
            "corsSettings": t.proxy(renames["CorsSettingsOut"]).optional(),
            "gcipSettings": t.proxy(renames["GcipSettingsOut"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSettingsOut"])
    types["ResetIdentityAwareProxyClientSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestIn"])
    types["ResetIdentityAwareProxyClientSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestOut"])
    types["PolicyDelegationSettingsIn"] = t.struct(
        {
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "iamServiceName": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameIn"]).optional(),
            "iamPermission": t.string().optional(),
        }
    ).named(renames["PolicyDelegationSettingsIn"])
    types["PolicyDelegationSettingsOut"] = t.struct(
        {
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "iamServiceName": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameOut"]).optional(),
            "iamPermission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyDelegationSettingsOut"])
    types["BrandIn"] = t.struct(
        {
            "supportEmail": t.string().optional(),
            "applicationTitle": t.string().optional(),
        }
    ).named(renames["BrandIn"])
    types["BrandOut"] = t.struct(
        {
            "supportEmail": t.string().optional(),
            "orgInternalOnly": t.boolean().optional(),
            "applicationTitle": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrandOut"])

    functions = {}
    functions["v1GetIamPolicy"] = iap.patch(
        "v1/{name}:iapSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "applicationSettings": t.proxy(
                    renames["ApplicationSettingsIn"]
                ).optional(),
                "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1TestIamPermissions"] = iap.patch(
        "v1/{name}:iapSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "applicationSettings": t.proxy(
                    renames["ApplicationSettingsIn"]
                ).optional(),
                "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SetIamPolicy"] = iap.patch(
        "v1/{name}:iapSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "applicationSettings": t.proxy(
                    renames["ApplicationSettingsIn"]
                ).optional(),
                "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetIapSettings"] = iap.patch(
        "v1/{name}:iapSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "applicationSettings": t.proxy(
                    renames["ApplicationSettingsIn"]
                ).optional(),
                "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1UpdateIapSettings"] = iap.patch(
        "v1/{name}:iapSettings",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "applicationSettings": t.proxy(
                    renames["ApplicationSettingsIn"]
                ).optional(),
                "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsGet"] = iap.post(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "tunnelDestGroupId": t.string(),
                "parent": t.string(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsPatch"] = iap.post(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "tunnelDestGroupId": t.string(),
                "parent": t.string(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsDelete"] = iap.post(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "tunnelDestGroupId": t.string(),
                "parent": t.string(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsList"] = iap.post(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "tunnelDestGroupId": t.string(),
                "parent": t.string(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsCreate"] = iap.post(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "tunnelDestGroupId": t.string(),
                "parent": t.string(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsGet"] = iap.post(
        "v1/{parent}/brands",
        t.struct(
            {
                "parent": t.string(),
                "supportEmail": t.string().optional(),
                "applicationTitle": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BrandOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsList"] = iap.post(
        "v1/{parent}/brands",
        t.struct(
            {
                "parent": t.string(),
                "supportEmail": t.string().optional(),
                "applicationTitle": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BrandOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsCreate"] = iap.post(
        "v1/{parent}/brands",
        t.struct(
            {
                "parent": t.string(),
                "supportEmail": t.string().optional(),
                "applicationTitle": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BrandOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsDelete"] = iap.get(
        "v1/{parent}/identityAwareProxyClients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdentityAwareProxyClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsGet"] = iap.get(
        "v1/{parent}/identityAwareProxyClients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdentityAwareProxyClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsCreate"] = iap.get(
        "v1/{parent}/identityAwareProxyClients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdentityAwareProxyClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsResetSecret"] = iap.get(
        "v1/{parent}/identityAwareProxyClients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdentityAwareProxyClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsList"] = iap.get(
        "v1/{parent}/identityAwareProxyClients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdentityAwareProxyClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="iap", renames=renames, types=Box(types), functions=Box(functions)
    )
