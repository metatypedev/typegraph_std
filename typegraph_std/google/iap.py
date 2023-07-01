from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_iap():
    iap = HTTPRuntime("https://iap.googleapis.com/")

    renames = {
        "ErrorResponse": "_iap_1_ErrorResponse",
        "AccessSettingsIn": "_iap_2_AccessSettingsIn",
        "AccessSettingsOut": "_iap_3_AccessSettingsOut",
        "SetIamPolicyRequestIn": "_iap_4_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_iap_5_SetIamPolicyRequestOut",
        "ListTunnelDestGroupsResponseIn": "_iap_6_ListTunnelDestGroupsResponseIn",
        "ListTunnelDestGroupsResponseOut": "_iap_7_ListTunnelDestGroupsResponseOut",
        "TestIamPermissionsResponseIn": "_iap_8_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_iap_9_TestIamPermissionsResponseOut",
        "ListIdentityAwareProxyClientsResponseIn": "_iap_10_ListIdentityAwareProxyClientsResponseIn",
        "ListIdentityAwareProxyClientsResponseOut": "_iap_11_ListIdentityAwareProxyClientsResponseOut",
        "ApplicationSettingsIn": "_iap_12_ApplicationSettingsIn",
        "ApplicationSettingsOut": "_iap_13_ApplicationSettingsOut",
        "PolicyIn": "_iap_14_PolicyIn",
        "PolicyOut": "_iap_15_PolicyOut",
        "OAuthSettingsIn": "_iap_16_OAuthSettingsIn",
        "OAuthSettingsOut": "_iap_17_OAuthSettingsOut",
        "CsmSettingsIn": "_iap_18_CsmSettingsIn",
        "CsmSettingsOut": "_iap_19_CsmSettingsOut",
        "CorsSettingsIn": "_iap_20_CorsSettingsIn",
        "CorsSettingsOut": "_iap_21_CorsSettingsOut",
        "BindingIn": "_iap_22_BindingIn",
        "BindingOut": "_iap_23_BindingOut",
        "ReauthSettingsIn": "_iap_24_ReauthSettingsIn",
        "ReauthSettingsOut": "_iap_25_ReauthSettingsOut",
        "AttributePropagationSettingsIn": "_iap_26_AttributePropagationSettingsIn",
        "AttributePropagationSettingsOut": "_iap_27_AttributePropagationSettingsOut",
        "GetIamPolicyRequestIn": "_iap_28_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_iap_29_GetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_iap_30_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_iap_31_TestIamPermissionsRequestOut",
        "EmptyIn": "_iap_32_EmptyIn",
        "EmptyOut": "_iap_33_EmptyOut",
        "ValidateIapAttributeExpressionResponseIn": "_iap_34_ValidateIapAttributeExpressionResponseIn",
        "ValidateIapAttributeExpressionResponseOut": "_iap_35_ValidateIapAttributeExpressionResponseOut",
        "PolicyNameIn": "_iap_36_PolicyNameIn",
        "PolicyNameOut": "_iap_37_PolicyNameOut",
        "AccessDeniedPageSettingsIn": "_iap_38_AccessDeniedPageSettingsIn",
        "AccessDeniedPageSettingsOut": "_iap_39_AccessDeniedPageSettingsOut",
        "ExprIn": "_iap_40_ExprIn",
        "ExprOut": "_iap_41_ExprOut",
        "BrandIn": "_iap_42_BrandIn",
        "BrandOut": "_iap_43_BrandOut",
        "IdentityAwareProxyClientIn": "_iap_44_IdentityAwareProxyClientIn",
        "IdentityAwareProxyClientOut": "_iap_45_IdentityAwareProxyClientOut",
        "PolicyDelegationSettingsIn": "_iap_46_PolicyDelegationSettingsIn",
        "PolicyDelegationSettingsOut": "_iap_47_PolicyDelegationSettingsOut",
        "ResourceIn": "_iap_48_ResourceIn",
        "ResourceOut": "_iap_49_ResourceOut",
        "GcipSettingsIn": "_iap_50_GcipSettingsIn",
        "GcipSettingsOut": "_iap_51_GcipSettingsOut",
        "ListBrandsResponseIn": "_iap_52_ListBrandsResponseIn",
        "ListBrandsResponseOut": "_iap_53_ListBrandsResponseOut",
        "IapSettingsIn": "_iap_54_IapSettingsIn",
        "IapSettingsOut": "_iap_55_IapSettingsOut",
        "GetPolicyOptionsIn": "_iap_56_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_iap_57_GetPolicyOptionsOut",
        "ResetIdentityAwareProxyClientSecretRequestIn": "_iap_58_ResetIdentityAwareProxyClientSecretRequestIn",
        "ResetIdentityAwareProxyClientSecretRequestOut": "_iap_59_ResetIdentityAwareProxyClientSecretRequestOut",
        "AllowedDomainsSettingsIn": "_iap_60_AllowedDomainsSettingsIn",
        "AllowedDomainsSettingsOut": "_iap_61_AllowedDomainsSettingsOut",
        "TunnelDestGroupIn": "_iap_62_TunnelDestGroupIn",
        "TunnelDestGroupOut": "_iap_63_TunnelDestGroupOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AccessSettingsIn"] = t.struct(
        {
            "corsSettings": t.proxy(renames["CorsSettingsIn"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsIn"]).optional(),
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsIn"]
            ).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsIn"]
            ).optional(),
            "gcipSettings": t.proxy(renames["GcipSettingsIn"]).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsIn"]).optional(),
        }
    ).named(renames["AccessSettingsIn"])
    types["AccessSettingsOut"] = t.struct(
        {
            "corsSettings": t.proxy(renames["CorsSettingsOut"]).optional(),
            "oauthSettings": t.proxy(renames["OAuthSettingsOut"]).optional(),
            "policyDelegationSettings": t.proxy(
                renames["PolicyDelegationSettingsOut"]
            ).optional(),
            "allowedDomainsSettings": t.proxy(
                renames["AllowedDomainsSettingsOut"]
            ).optional(),
            "gcipSettings": t.proxy(renames["GcipSettingsOut"]).optional(),
            "reauthSettings": t.proxy(renames["ReauthSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSettingsOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["OAuthSettingsIn"] = t.struct({"loginHint": t.string().optional()}).named(
        renames["OAuthSettingsIn"]
    )
    types["OAuthSettingsOut"] = t.struct(
        {
            "loginHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthSettingsOut"])
    types["CsmSettingsIn"] = t.struct({"rctokenAud": t.string().optional()}).named(
        renames["CsmSettingsIn"]
    )
    types["CsmSettingsOut"] = t.struct(
        {
            "rctokenAud": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsmSettingsOut"])
    types["CorsSettingsIn"] = t.struct(
        {"allowHttpOptions": t.boolean().optional()}
    ).named(renames["CorsSettingsIn"])
    types["CorsSettingsOut"] = t.struct(
        {
            "allowHttpOptions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorsSettingsOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ReauthSettingsIn"] = t.struct(
        {
            "method": t.string().optional(),
            "policyType": t.string().optional(),
            "maxAge": t.string().optional(),
        }
    ).named(renames["ReauthSettingsIn"])
    types["ReauthSettingsOut"] = t.struct(
        {
            "method": t.string().optional(),
            "policyType": t.string().optional(),
            "maxAge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReauthSettingsOut"])
    types["AttributePropagationSettingsIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "outputCredentials": t.array(t.string()).optional(),
            "enable": t.boolean().optional(),
        }
    ).named(renames["AttributePropagationSettingsIn"])
    types["AttributePropagationSettingsOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "outputCredentials": t.array(t.string()).optional(),
            "enable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributePropagationSettingsOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ValidateIapAttributeExpressionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ValidateIapAttributeExpressionResponseIn"])
    types["ValidateIapAttributeExpressionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateIapAttributeExpressionResponseOut"])
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
    types["AccessDeniedPageSettingsIn"] = t.struct(
        {
            "accessDeniedPageUri": t.string().optional(),
            "remediationTokenGenerationEnabled": t.boolean().optional(),
            "generateTroubleshootingUri": t.boolean().optional(),
        }
    ).named(renames["AccessDeniedPageSettingsIn"])
    types["AccessDeniedPageSettingsOut"] = t.struct(
        {
            "accessDeniedPageUri": t.string().optional(),
            "remediationTokenGenerationEnabled": t.boolean().optional(),
            "generateTroubleshootingUri": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessDeniedPageSettingsOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
            "supportEmail": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BrandOut"])
    types["IdentityAwareProxyClientIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["IdentityAwareProxyClientIn"])
    types["IdentityAwareProxyClientOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityAwareProxyClientOut"])
    types["PolicyDelegationSettingsIn"] = t.struct(
        {
            "iamPermission": t.string().optional(),
            "iamServiceName": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameIn"]).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
        }
    ).named(renames["PolicyDelegationSettingsIn"])
    types["PolicyDelegationSettingsOut"] = t.struct(
        {
            "iamPermission": t.string().optional(),
            "iamServiceName": t.string().optional(),
            "policyName": t.proxy(renames["PolicyNameOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyDelegationSettingsOut"])
    types["ResourceIn"] = t.struct(
        {
            "type": t.string().optional(),
            "service": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "service": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["GcipSettingsIn"] = t.struct(
        {
            "loginPageUri": t.string().optional(),
            "tenantIds": t.array(t.string()).optional(),
        }
    ).named(renames["GcipSettingsIn"])
    types["GcipSettingsOut"] = t.struct(
        {
            "loginPageUri": t.string().optional(),
            "tenantIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcipSettingsOut"])
    types["ListBrandsResponseIn"] = t.struct(
        {"brands": t.array(t.proxy(renames["BrandIn"])).optional()}
    ).named(renames["ListBrandsResponseIn"])
    types["ListBrandsResponseOut"] = t.struct(
        {
            "brands": t.array(t.proxy(renames["BrandOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBrandsResponseOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["ResetIdentityAwareProxyClientSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestIn"])
    types["ResetIdentityAwareProxyClientSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetIdentityAwareProxyClientSecretRequestOut"])
    types["AllowedDomainsSettingsIn"] = t.struct(
        {"domains": t.array(t.string()).optional(), "enable": t.boolean().optional()}
    ).named(renames["AllowedDomainsSettingsIn"])
    types["AllowedDomainsSettingsOut"] = t.struct(
        {
            "domains": t.array(t.string()).optional(),
            "enable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedDomainsSettingsOut"])
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

    functions = {}
    functions["v1GetIamPolicy"] = iap.get(
        "v1/{name}:iapSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IapSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1ValidateAttributeExpression"] = iap.get(
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
    functions["v1UpdateIapSettings"] = iap.get(
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
    functions["v1GetIapSettings"] = iap.get(
        "v1/{name}:iapSettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IapSettingsOut"]),
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
    functions["projectsBrandsList"] = iap.get(
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
    functions["projectsIap_tunnelLocationsDestGroupsCreate"] = iap.get(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTunnelDestGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsGet"] = iap.get(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTunnelDestGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsDelete"] = iap.get(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTunnelDestGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsPatch"] = iap.get(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTunnelDestGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIap_tunnelLocationsDestGroupsList"] = iap.get(
        "v1/{parent}/destGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTunnelDestGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="iap", renames=renames, types=Box(types), functions=Box(functions)
    )
