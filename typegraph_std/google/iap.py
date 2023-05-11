from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_iap() -> Import:
    iap = HTTPRuntime("https://iap.googleapis.com/")

    renames = {
        "ErrorResponse": "_iap_1_ErrorResponse",
        "CorsSettingsIn": "_iap_2_CorsSettingsIn",
        "CorsSettingsOut": "_iap_3_CorsSettingsOut",
        "OAuthSettingsIn": "_iap_4_OAuthSettingsIn",
        "OAuthSettingsOut": "_iap_5_OAuthSettingsOut",
        "TestIamPermissionsRequestIn": "_iap_6_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_iap_7_TestIamPermissionsRequestOut",
        "ReauthSettingsIn": "_iap_8_ReauthSettingsIn",
        "ReauthSettingsOut": "_iap_9_ReauthSettingsOut",
        "AttributePropagationSettingsIn": "_iap_10_AttributePropagationSettingsIn",
        "AttributePropagationSettingsOut": "_iap_11_AttributePropagationSettingsOut",
        "ListIdentityAwareProxyClientsResponseIn": "_iap_12_ListIdentityAwareProxyClientsResponseIn",
        "ListIdentityAwareProxyClientsResponseOut": "_iap_13_ListIdentityAwareProxyClientsResponseOut",
        "AllowedDomainsSettingsIn": "_iap_14_AllowedDomainsSettingsIn",
        "AllowedDomainsSettingsOut": "_iap_15_AllowedDomainsSettingsOut",
        "AccessDeniedPageSettingsIn": "_iap_16_AccessDeniedPageSettingsIn",
        "AccessDeniedPageSettingsOut": "_iap_17_AccessDeniedPageSettingsOut",
        "IdentityAwareProxyClientIn": "_iap_18_IdentityAwareProxyClientIn",
        "IdentityAwareProxyClientOut": "_iap_19_IdentityAwareProxyClientOut",
        "GetIamPolicyRequestIn": "_iap_20_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_iap_21_GetIamPolicyRequestOut",
        "EmptyIn": "_iap_22_EmptyIn",
        "EmptyOut": "_iap_23_EmptyOut",
        "BrandIn": "_iap_24_BrandIn",
        "BrandOut": "_iap_25_BrandOut",
        "CsmSettingsIn": "_iap_26_CsmSettingsIn",
        "CsmSettingsOut": "_iap_27_CsmSettingsOut",
        "PolicyDelegationSettingsIn": "_iap_28_PolicyDelegationSettingsIn",
        "PolicyDelegationSettingsOut": "_iap_29_PolicyDelegationSettingsOut",
        "AccessSettingsIn": "_iap_30_AccessSettingsIn",
        "AccessSettingsOut": "_iap_31_AccessSettingsOut",
        "GcipSettingsIn": "_iap_32_GcipSettingsIn",
        "GcipSettingsOut": "_iap_33_GcipSettingsOut",
        "ApplicationSettingsIn": "_iap_34_ApplicationSettingsIn",
        "ApplicationSettingsOut": "_iap_35_ApplicationSettingsOut",
        "TunnelDestGroupIn": "_iap_36_TunnelDestGroupIn",
        "TunnelDestGroupOut": "_iap_37_TunnelDestGroupOut",
        "ExprIn": "_iap_38_ExprIn",
        "ExprOut": "_iap_39_ExprOut",
        "TestIamPermissionsResponseIn": "_iap_40_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_iap_41_TestIamPermissionsResponseOut",
        "PolicyIn": "_iap_42_PolicyIn",
        "PolicyOut": "_iap_43_PolicyOut",
        "ResourceIn": "_iap_44_ResourceIn",
        "ResourceOut": "_iap_45_ResourceOut",
        "GetPolicyOptionsIn": "_iap_46_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_iap_47_GetPolicyOptionsOut",
        "BindingIn": "_iap_48_BindingIn",
        "BindingOut": "_iap_49_BindingOut",
        "IapSettingsIn": "_iap_50_IapSettingsIn",
        "IapSettingsOut": "_iap_51_IapSettingsOut",
        "ListTunnelDestGroupsResponseIn": "_iap_52_ListTunnelDestGroupsResponseIn",
        "ListTunnelDestGroupsResponseOut": "_iap_53_ListTunnelDestGroupsResponseOut",
        "ResetIdentityAwareProxyClientSecretRequestIn": "_iap_54_ResetIdentityAwareProxyClientSecretRequestIn",
        "ResetIdentityAwareProxyClientSecretRequestOut": "_iap_55_ResetIdentityAwareProxyClientSecretRequestOut",
        "SetIamPolicyRequestIn": "_iap_56_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_iap_57_SetIamPolicyRequestOut",
        "PolicyNameIn": "_iap_58_PolicyNameIn",
        "PolicyNameOut": "_iap_59_PolicyNameOut",
        "ListBrandsResponseIn": "_iap_60_ListBrandsResponseIn",
        "ListBrandsResponseOut": "_iap_61_ListBrandsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CorsSettingsIn"] = t.struct(
        {"allowHttpOptions": t.boolean().optional()}
    ).named(renames["CorsSettingsIn"])
    types["CorsSettingsOut"] = t.struct(
        {
            "allowHttpOptions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorsSettingsOut"])
    types["OAuthSettingsIn"] = t.struct({"loginHint": t.string().optional()}).named(
        renames["OAuthSettingsIn"]
    )
    types["OAuthSettingsOut"] = t.struct(
        {
            "loginHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthSettingsOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ReauthSettingsIn"] = t.struct(
        {
            "method": t.string().optional(),
            "maxAge": t.string().optional(),
            "policyType": t.string().optional(),
        }
    ).named(renames["ReauthSettingsIn"])
    types["ReauthSettingsOut"] = t.struct(
        {
            "method": t.string().optional(),
            "maxAge": t.string().optional(),
            "policyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReauthSettingsOut"])
    types["AttributePropagationSettingsIn"] = t.struct(
        {
            "enable": t.boolean().optional(),
            "outputCredentials": t.array(t.string()).optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["AttributePropagationSettingsIn"])
    types["AttributePropagationSettingsOut"] = t.struct(
        {
            "enable": t.boolean().optional(),
            "outputCredentials": t.array(t.string()).optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributePropagationSettingsOut"])
    types["ListIdentityAwareProxyClientsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "identityAwareProxyClients": t.array(
                t.proxy(renames["IdentityAwareProxyClientIn"])
            ).optional(),
        }
    ).named(renames["ListIdentityAwareProxyClientsResponseIn"])
    types["ListIdentityAwareProxyClientsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "identityAwareProxyClients": t.array(
                t.proxy(renames["IdentityAwareProxyClientOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListIdentityAwareProxyClientsResponseOut"])
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
    types["AccessDeniedPageSettingsIn"] = t.struct(
        {
            "remediationTokenGenerationEnabled": t.boolean().optional(),
            "generateTroubleshootingUri": t.boolean().optional(),
            "accessDeniedPageUri": t.string().optional(),
        }
    ).named(renames["AccessDeniedPageSettingsIn"])
    types["AccessDeniedPageSettingsOut"] = t.struct(
        {
            "remediationTokenGenerationEnabled": t.boolean().optional(),
            "generateTroubleshootingUri": t.boolean().optional(),
            "accessDeniedPageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessDeniedPageSettingsOut"])
    types["IdentityAwareProxyClientIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["IdentityAwareProxyClientIn"])
    types["IdentityAwareProxyClientOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "secret": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityAwareProxyClientOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BrandIn"] = t.struct(
        {
            "applicationTitle": t.string().optional(),
            "supportEmail": t.string().optional(),
        }
    ).named(renames["BrandIn"])
    types["BrandOut"] = t.struct(
        {
            "applicationTitle": t.string().optional(),
            "orgInternalOnly": t.boolean().optional(),
            "name": t.string().optional(),
            "supportEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrandOut"])
    types["CsmSettingsIn"] = t.struct({"rctokenAud": t.string().optional()}).named(
        renames["CsmSettingsIn"]
    )
    types["CsmSettingsOut"] = t.struct(
        {
            "rctokenAud": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsmSettingsOut"])
    types["PolicyDelegationSettingsIn"] = t.struct(
        {
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "iamServiceName": t.string().optional(),
            "iamPermission": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameIn"]).optional(),
        }
    ).named(renames["PolicyDelegationSettingsIn"])
    types["PolicyDelegationSettingsOut"] = t.struct(
        {
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "iamServiceName": t.string().optional(),
            "iamPermission": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyDelegationSettingsOut"])
    types["AccessSettingsIn"] = t.struct(
        {
            "gcipSettings": t.proxy(renames["GcipSettingsIn"]).optional(),
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsIn"]
            ).optional(),
            "corsSettings": t.proxy(renames["CorsSettingsIn"]).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsIn"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsIn"]).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsIn"]
            ).optional(),
        }
    ).named(renames["AccessSettingsIn"])
    types["AccessSettingsOut"] = t.struct(
        {
            "gcipSettings": t.proxy(renames["GcipSettingsOut"]).optional(),
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsOut"]
            ).optional(),
            "corsSettings": t.proxy(renames["CorsSettingsOut"]).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsOut"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsOut"]).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSettingsOut"])
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
            "accessDeniedPageSettings": t.proxy(
                renames["AccessDeniedPageSettingsIn"]
            ).optional(),
            "csmSettings": t.proxy(renames["CsmSettingsIn"]).optional(),
        }
    ).named(renames["ApplicationSettingsIn"])
    types["ApplicationSettingsOut"] = t.struct(
        {
            "cookieDomain": t.string().optional(),
            "attributePropagationSettings": t.proxy(
                renames["AttributePropagationSettingsOut"]
            ).optional(),
            "accessDeniedPageSettings": t.proxy(
                renames["AccessDeniedPageSettingsOut"]
            ).optional(),
            "csmSettings": t.proxy(renames["CsmSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationSettingsOut"])
    types["TunnelDestGroupIn"] = t.struct(
        {
            "fqdns": t.array(t.string()).optional(),
            "name": t.string(),
            "cidrs": t.array(t.string()).optional(),
        }
    ).named(renames["TunnelDestGroupIn"])
    types["TunnelDestGroupOut"] = t.struct(
        {
            "fqdns": t.array(t.string()).optional(),
            "name": t.string(),
            "cidrs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TunnelDestGroupOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ResourceIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "service": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "service": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["IapSettingsIn"] = t.struct(
        {
            "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
            "applicationSettings": t.proxy(renames["ApplicationSettingsIn"]).optional(),
            "name": t.string(),
        }
    ).named(renames["IapSettingsIn"])
    types["IapSettingsOut"] = t.struct(
        {
            "accessSettings": t.proxy(renames["AccessSettingsOut"]).optional(),
            "applicationSettings": t.proxy(
                renames["ApplicationSettingsOut"]
            ).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapSettingsOut"])
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
    types["ResetIdentityAwareProxyClientSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestIn"])
    types["ResetIdentityAwareProxyClientSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["PolicyNameIn"] = t.struct(
        {
            "region": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PolicyNameIn"])
    types["PolicyNameOut"] = t.struct(
        {
            "region": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyNameOut"])
    types["ListBrandsResponseIn"] = t.struct(
        {"brands": t.array(t.proxy(renames["BrandIn"])).optional()}
    ).named(renames["ListBrandsResponseIn"])
    types["ListBrandsResponseOut"] = t.struct(
        {
            "brands": t.array(t.proxy(renames["BrandOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBrandsResponseOut"])

    functions = {}
    functions["v1UpdateIapSettings"] = iap.get(
        "v1/{name}:iapSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SetIamPolicy"] = iap.get(
        "v1/{name}:iapSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1TestIamPermissions"] = iap.get(
        "v1/{name}:iapSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetIamPolicy"] = iap.get(
        "v1/{name}:iapSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetIapSettings"] = iap.get(
        "v1/{name}:iapSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsCreate"] = iap.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsList"] = iap.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsGet"] = iap.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsDelete"] = iap.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsPatch"] = iap.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "fqdns": t.array(t.string()).optional(),
                "cidrs": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TunnelDestGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsCreate"] = iap.get(
        "v1/{parent}/brands",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListBrandsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsGet"] = iap.get(
        "v1/{parent}/brands",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListBrandsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsList"] = iap.get(
        "v1/{parent}/brands",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListBrandsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsCreate"] = iap.get(
        "v1/{parent}/identityAwareProxyClients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdentityAwareProxyClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsDelete"] = iap.get(
        "v1/{parent}/identityAwareProxyClients",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdentityAwareProxyClientsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="iap", renames=renames, types=types, functions=functions)
