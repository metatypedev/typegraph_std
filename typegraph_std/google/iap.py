from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_iap() -> Import:
    iap = HTTPRuntime("https://iap.googleapis.com/")

    renames = {
        "ErrorResponse": "_iap_1_ErrorResponse",
        "PolicyIn": "_iap_2_PolicyIn",
        "PolicyOut": "_iap_3_PolicyOut",
        "GetPolicyOptionsIn": "_iap_4_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_iap_5_GetPolicyOptionsOut",
        "ListBrandsResponseIn": "_iap_6_ListBrandsResponseIn",
        "ListBrandsResponseOut": "_iap_7_ListBrandsResponseOut",
        "AccessSettingsIn": "_iap_8_AccessSettingsIn",
        "AccessSettingsOut": "_iap_9_AccessSettingsOut",
        "ListTunnelDestGroupsResponseIn": "_iap_10_ListTunnelDestGroupsResponseIn",
        "ListTunnelDestGroupsResponseOut": "_iap_11_ListTunnelDestGroupsResponseOut",
        "TunnelDestGroupIn": "_iap_12_TunnelDestGroupIn",
        "TunnelDestGroupOut": "_iap_13_TunnelDestGroupOut",
        "AccessDeniedPageSettingsIn": "_iap_14_AccessDeniedPageSettingsIn",
        "AccessDeniedPageSettingsOut": "_iap_15_AccessDeniedPageSettingsOut",
        "CsmSettingsIn": "_iap_16_CsmSettingsIn",
        "CsmSettingsOut": "_iap_17_CsmSettingsOut",
        "SetIamPolicyRequestIn": "_iap_18_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_iap_19_SetIamPolicyRequestOut",
        "PolicyNameIn": "_iap_20_PolicyNameIn",
        "PolicyNameOut": "_iap_21_PolicyNameOut",
        "CorsSettingsIn": "_iap_22_CorsSettingsIn",
        "CorsSettingsOut": "_iap_23_CorsSettingsOut",
        "OAuthSettingsIn": "_iap_24_OAuthSettingsIn",
        "OAuthSettingsOut": "_iap_25_OAuthSettingsOut",
        "BrandIn": "_iap_26_BrandIn",
        "BrandOut": "_iap_27_BrandOut",
        "AllowedDomainsSettingsIn": "_iap_28_AllowedDomainsSettingsIn",
        "AllowedDomainsSettingsOut": "_iap_29_AllowedDomainsSettingsOut",
        "ReauthSettingsIn": "_iap_30_ReauthSettingsIn",
        "ReauthSettingsOut": "_iap_31_ReauthSettingsOut",
        "EmptyIn": "_iap_32_EmptyIn",
        "EmptyOut": "_iap_33_EmptyOut",
        "IapSettingsIn": "_iap_34_IapSettingsIn",
        "IapSettingsOut": "_iap_35_IapSettingsOut",
        "BindingIn": "_iap_36_BindingIn",
        "BindingOut": "_iap_37_BindingOut",
        "ListIdentityAwareProxyClientsResponseIn": "_iap_38_ListIdentityAwareProxyClientsResponseIn",
        "ListIdentityAwareProxyClientsResponseOut": "_iap_39_ListIdentityAwareProxyClientsResponseOut",
        "AttributePropagationSettingsIn": "_iap_40_AttributePropagationSettingsIn",
        "AttributePropagationSettingsOut": "_iap_41_AttributePropagationSettingsOut",
        "TestIamPermissionsRequestIn": "_iap_42_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_iap_43_TestIamPermissionsRequestOut",
        "ApplicationSettingsIn": "_iap_44_ApplicationSettingsIn",
        "ApplicationSettingsOut": "_iap_45_ApplicationSettingsOut",
        "TestIamPermissionsResponseIn": "_iap_46_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_iap_47_TestIamPermissionsResponseOut",
        "ExprIn": "_iap_48_ExprIn",
        "ExprOut": "_iap_49_ExprOut",
        "PolicyDelegationSettingsIn": "_iap_50_PolicyDelegationSettingsIn",
        "PolicyDelegationSettingsOut": "_iap_51_PolicyDelegationSettingsOut",
        "GetIamPolicyRequestIn": "_iap_52_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_iap_53_GetIamPolicyRequestOut",
        "ResetIdentityAwareProxyClientSecretRequestIn": "_iap_54_ResetIdentityAwareProxyClientSecretRequestIn",
        "ResetIdentityAwareProxyClientSecretRequestOut": "_iap_55_ResetIdentityAwareProxyClientSecretRequestOut",
        "GcipSettingsIn": "_iap_56_GcipSettingsIn",
        "GcipSettingsOut": "_iap_57_GcipSettingsOut",
        "IdentityAwareProxyClientIn": "_iap_58_IdentityAwareProxyClientIn",
        "IdentityAwareProxyClientOut": "_iap_59_IdentityAwareProxyClientOut",
        "ResourceIn": "_iap_60_ResourceIn",
        "ResourceOut": "_iap_61_ResourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["ListBrandsResponseIn"] = t.struct(
        {"brands": t.array(t.proxy(renames["BrandIn"])).optional()}
    ).named(renames["ListBrandsResponseIn"])
    types["ListBrandsResponseOut"] = t.struct(
        {
            "brands": t.array(t.proxy(renames["BrandOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBrandsResponseOut"])
    types["AccessSettingsIn"] = t.struct(
        {
            "gcipSettings": t.proxy(renames["GcipSettingsIn"]).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsIn"]
            ).optional(),
            "corsSettings": t.proxy(renames["CorsSettingsIn"]).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsIn"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsIn"]).optional(),
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsIn"]
            ).optional(),
        }
    ).named(renames["AccessSettingsIn"])
    types["AccessSettingsOut"] = t.struct(
        {
            "gcipSettings": t.proxy(renames["GcipSettingsOut"]).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsOut"]
            ).optional(),
            "corsSettings": t.proxy(renames["CorsSettingsOut"]).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsOut"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsOut"]).optional(),
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSettingsOut"])
    types["ListTunnelDestGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tunnelDestGroups": t.array(
                t.proxy(renames["TunnelDestGroupIn"])
            ).optional(),
        }
    ).named(renames["ListTunnelDestGroupsResponseIn"])
    types["ListTunnelDestGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tunnelDestGroups": t.array(
                t.proxy(renames["TunnelDestGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTunnelDestGroupsResponseOut"])
    types["TunnelDestGroupIn"] = t.struct(
        {
            "cidrs": t.array(t.string()).optional(),
            "name": t.string(),
            "fqdns": t.array(t.string()).optional(),
        }
    ).named(renames["TunnelDestGroupIn"])
    types["TunnelDestGroupOut"] = t.struct(
        {
            "cidrs": t.array(t.string()).optional(),
            "name": t.string(),
            "fqdns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TunnelDestGroupOut"])
    types["AccessDeniedPageSettingsIn"] = t.struct(
        {
            "accessDeniedPageUri": t.string().optional(),
            "generateTroubleshootingUri": t.boolean().optional(),
            "remediationTokenGenerationEnabled": t.boolean().optional(),
        }
    ).named(renames["AccessDeniedPageSettingsIn"])
    types["AccessDeniedPageSettingsOut"] = t.struct(
        {
            "accessDeniedPageUri": t.string().optional(),
            "generateTroubleshootingUri": t.boolean().optional(),
            "remediationTokenGenerationEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessDeniedPageSettingsOut"])
    types["CsmSettingsIn"] = t.struct({"rctokenAud": t.string().optional()}).named(
        renames["CsmSettingsIn"]
    )
    types["CsmSettingsOut"] = t.struct(
        {
            "rctokenAud": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsmSettingsOut"])
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
            "id": t.string().optional(),
            "type": t.string().optional(),
            "region": t.string().optional(),
        }
    ).named(renames["PolicyNameIn"])
    types["PolicyNameOut"] = t.struct(
        {
            "id": t.string().optional(),
            "type": t.string().optional(),
            "region": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyNameOut"])
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
    types["BrandIn"] = t.struct(
        {
            "supportEmail": t.string().optional(),
            "applicationTitle": t.string().optional(),
        }
    ).named(renames["BrandIn"])
    types["BrandOut"] = t.struct(
        {
            "supportEmail": t.string().optional(),
            "name": t.string().optional(),
            "orgInternalOnly": t.boolean().optional(),
            "applicationTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrandOut"])
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
    types["ReauthSettingsIn"] = t.struct(
        {
            "maxAge": t.string().optional(),
            "policyType": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["ReauthSettingsIn"])
    types["ReauthSettingsOut"] = t.struct(
        {
            "maxAge": t.string().optional(),
            "policyType": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReauthSettingsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["IapSettingsIn"] = t.struct(
        {
            "applicationSettings": t.proxy(renames["ApplicationSettingsIn"]).optional(),
            "name": t.string(),
            "accessSettings": t.proxy(renames["AccessSettingsIn"]).optional(),
        }
    ).named(renames["IapSettingsIn"])
    types["IapSettingsOut"] = t.struct(
        {
            "applicationSettings": t.proxy(
                renames["ApplicationSettingsOut"]
            ).optional(),
            "name": t.string(),
            "accessSettings": t.proxy(renames["AccessSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapSettingsOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["AttributePropagationSettingsIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "enable": t.boolean().optional(),
            "outputCredentials": t.array(t.string()).optional(),
        }
    ).named(renames["AttributePropagationSettingsIn"])
    types["AttributePropagationSettingsOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "enable": t.boolean().optional(),
            "outputCredentials": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributePropagationSettingsOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ApplicationSettingsIn"] = t.struct(
        {
            "attributePropagationSettings": t.proxy(
                renames["AttributePropagationSettingsIn"]
            ).optional(),
            "csmSettings": t.proxy(renames["CsmSettingsIn"]).optional(),
            "cookieDomain": t.string().optional(),
            "accessDeniedPageSettings": t.proxy(
                renames["AccessDeniedPageSettingsIn"]
            ).optional(),
        }
    ).named(renames["ApplicationSettingsIn"])
    types["ApplicationSettingsOut"] = t.struct(
        {
            "attributePropagationSettings": t.proxy(
                renames["AttributePropagationSettingsOut"]
            ).optional(),
            "csmSettings": t.proxy(renames["CsmSettingsOut"]).optional(),
            "cookieDomain": t.string().optional(),
            "accessDeniedPageSettings": t.proxy(
                renames["AccessDeniedPageSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationSettingsOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["PolicyDelegationSettingsIn"] = t.struct(
        {
            "iamPermission": t.string().optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "iamServiceName": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameIn"]).optional(),
        }
    ).named(renames["PolicyDelegationSettingsIn"])
    types["PolicyDelegationSettingsOut"] = t.struct(
        {
            "iamPermission": t.string().optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "iamServiceName": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyDelegationSettingsOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ResetIdentityAwareProxyClientSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestIn"])
    types["ResetIdentityAwareProxyClientSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestOut"])
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
    types["IdentityAwareProxyClientIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["IdentityAwareProxyClientIn"])
    types["IdentityAwareProxyClientOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityAwareProxyClientOut"])
    types["ResourceIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "service": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])

    functions = {}
    functions["projectsIap_tunnelLocationsDestGroupsList"] = iap.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsPatch"] = iap.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsGet"] = iap.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsCreate"] = iap.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsDelete"] = iap.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsList"] = iap.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BrandOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsCreate"] = iap.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BrandOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsGet"] = iap.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BrandOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsList"] = iap.post(
        "v1/{name}:resetSecret",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IdentityAwareProxyClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsGet"] = iap.post(
        "v1/{name}:resetSecret",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IdentityAwareProxyClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsCreate"] = iap.post(
        "v1/{name}:resetSecret",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IdentityAwareProxyClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsDelete"] = iap.post(
        "v1/{name}:resetSecret",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IdentityAwareProxyClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBrandsIdentityAwareProxyClientsResetSecret"] = iap.post(
        "v1/{name}:resetSecret",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IdentityAwareProxyClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetIapSettings"] = iap.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1TestIamPermissions"] = iap.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1SetIamPolicy"] = iap.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1UpdateIapSettings"] = iap.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetIamPolicy"] = iap.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="iap", renames=renames, types=Box(types), functions=Box(functions)
    )
