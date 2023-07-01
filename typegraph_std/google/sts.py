from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_sts():
    sts = HTTPRuntime("https://sts.googleapis.com/")

    renames = {
        "ErrorResponse": "_sts_1_ErrorResponse",
        "GoogleIdentityStsV1betaAccessBoundaryIn": "_sts_2_GoogleIdentityStsV1betaAccessBoundaryIn",
        "GoogleIdentityStsV1betaAccessBoundaryOut": "_sts_3_GoogleIdentityStsV1betaAccessBoundaryOut",
        "GoogleTypeExprIn": "_sts_4_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_sts_5_GoogleTypeExprOut",
        "GoogleIdentityStsV1AccessBoundaryRuleIn": "_sts_6_GoogleIdentityStsV1AccessBoundaryRuleIn",
        "GoogleIdentityStsV1AccessBoundaryRuleOut": "_sts_7_GoogleIdentityStsV1AccessBoundaryRuleOut",
        "GoogleIamV1BindingIn": "_sts_8_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_sts_9_GoogleIamV1BindingOut",
        "GoogleIdentityStsV1AccessBoundaryIn": "_sts_10_GoogleIdentityStsV1AccessBoundaryIn",
        "GoogleIdentityStsV1AccessBoundaryOut": "_sts_11_GoogleIdentityStsV1AccessBoundaryOut",
        "GoogleIdentityStsV1IntrospectTokenRequestIn": "_sts_12_GoogleIdentityStsV1IntrospectTokenRequestIn",
        "GoogleIdentityStsV1IntrospectTokenRequestOut": "_sts_13_GoogleIdentityStsV1IntrospectTokenRequestOut",
        "GoogleIdentityStsV1IntrospectTokenResponseIn": "_sts_14_GoogleIdentityStsV1IntrospectTokenResponseIn",
        "GoogleIdentityStsV1IntrospectTokenResponseOut": "_sts_15_GoogleIdentityStsV1IntrospectTokenResponseOut",
        "GoogleIdentityStsV1betaAccessBoundaryRuleIn": "_sts_16_GoogleIdentityStsV1betaAccessBoundaryRuleIn",
        "GoogleIdentityStsV1betaAccessBoundaryRuleOut": "_sts_17_GoogleIdentityStsV1betaAccessBoundaryRuleOut",
        "GoogleIdentityStsV1ExchangeTokenRequestIn": "_sts_18_GoogleIdentityStsV1ExchangeTokenRequestIn",
        "GoogleIdentityStsV1ExchangeTokenRequestOut": "_sts_19_GoogleIdentityStsV1ExchangeTokenRequestOut",
        "GoogleIdentityStsV1betaOptionsIn": "_sts_20_GoogleIdentityStsV1betaOptionsIn",
        "GoogleIdentityStsV1betaOptionsOut": "_sts_21_GoogleIdentityStsV1betaOptionsOut",
        "GoogleIdentityStsV1ExchangeOauthTokenResponseIn": "_sts_22_GoogleIdentityStsV1ExchangeOauthTokenResponseIn",
        "GoogleIdentityStsV1ExchangeOauthTokenResponseOut": "_sts_23_GoogleIdentityStsV1ExchangeOauthTokenResponseOut",
        "GoogleIdentityStsV1ExchangeTokenResponseIn": "_sts_24_GoogleIdentityStsV1ExchangeTokenResponseIn",
        "GoogleIdentityStsV1ExchangeTokenResponseOut": "_sts_25_GoogleIdentityStsV1ExchangeTokenResponseOut",
        "GoogleIdentityStsV1ExchangeOauthTokenRequestIn": "_sts_26_GoogleIdentityStsV1ExchangeOauthTokenRequestIn",
        "GoogleIdentityStsV1ExchangeOauthTokenRequestOut": "_sts_27_GoogleIdentityStsV1ExchangeOauthTokenRequestOut",
        "GoogleIdentityStsV1OptionsIn": "_sts_28_GoogleIdentityStsV1OptionsIn",
        "GoogleIdentityStsV1OptionsOut": "_sts_29_GoogleIdentityStsV1OptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleIdentityStsV1betaAccessBoundaryIn"] = t.struct(
        {
            "accessBoundaryRules": t.array(
                t.proxy(renames["GoogleIdentityStsV1betaAccessBoundaryRuleIn"])
            ).optional()
        }
    ).named(renames["GoogleIdentityStsV1betaAccessBoundaryIn"])
    types["GoogleIdentityStsV1betaAccessBoundaryOut"] = t.struct(
        {
            "accessBoundaryRules": t.array(
                t.proxy(renames["GoogleIdentityStsV1betaAccessBoundaryRuleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaAccessBoundaryOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleIdentityStsV1AccessBoundaryRuleIn"] = t.struct(
        {
            "availablePermissions": t.array(t.string()).optional(),
            "availableResource": t.string().optional(),
            "availabilityCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1AccessBoundaryRuleIn"])
    types["GoogleIdentityStsV1AccessBoundaryRuleOut"] = t.struct(
        {
            "availablePermissions": t.array(t.string()).optional(),
            "availableResource": t.string().optional(),
            "availabilityCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1AccessBoundaryRuleOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleIdentityStsV1AccessBoundaryIn"] = t.struct(
        {
            "accessBoundaryRules": t.array(
                t.proxy(renames["GoogleIdentityStsV1AccessBoundaryRuleIn"])
            ).optional()
        }
    ).named(renames["GoogleIdentityStsV1AccessBoundaryIn"])
    types["GoogleIdentityStsV1AccessBoundaryOut"] = t.struct(
        {
            "accessBoundaryRules": t.array(
                t.proxy(renames["GoogleIdentityStsV1AccessBoundaryRuleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1AccessBoundaryOut"])
    types["GoogleIdentityStsV1IntrospectTokenRequestIn"] = t.struct(
        {"token": t.string(), "tokenTypeHint": t.string().optional()}
    ).named(renames["GoogleIdentityStsV1IntrospectTokenRequestIn"])
    types["GoogleIdentityStsV1IntrospectTokenRequestOut"] = t.struct(
        {
            "token": t.string(),
            "tokenTypeHint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenRequestOut"])
    types["GoogleIdentityStsV1IntrospectTokenResponseIn"] = t.struct(
        {
            "active": t.boolean().optional(),
            "sub": t.string().optional(),
            "client_id": t.string().optional(),
            "scope": t.string().optional(),
            "iss": t.string().optional(),
            "iat": t.string().optional(),
            "exp": t.string().optional(),
            "username": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenResponseIn"])
    types["GoogleIdentityStsV1IntrospectTokenResponseOut"] = t.struct(
        {
            "active": t.boolean().optional(),
            "sub": t.string().optional(),
            "client_id": t.string().optional(),
            "scope": t.string().optional(),
            "iss": t.string().optional(),
            "iat": t.string().optional(),
            "exp": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"])
    types["GoogleIdentityStsV1betaAccessBoundaryRuleIn"] = t.struct(
        {
            "availabilityCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "availableResource": t.string().optional(),
            "availablePermissions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaAccessBoundaryRuleIn"])
    types["GoogleIdentityStsV1betaAccessBoundaryRuleOut"] = t.struct(
        {
            "availabilityCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "availableResource": t.string().optional(),
            "availablePermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaAccessBoundaryRuleOut"])
    types["GoogleIdentityStsV1ExchangeTokenRequestIn"] = t.struct(
        {
            "grantType": t.string(),
            "requestedTokenType": t.string(),
            "scope": t.string().optional(),
            "audience": t.string().optional(),
            "options": t.string().optional(),
            "subjectToken": t.string(),
            "subjectTokenType": t.string(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenRequestIn"])
    types["GoogleIdentityStsV1ExchangeTokenRequestOut"] = t.struct(
        {
            "grantType": t.string(),
            "requestedTokenType": t.string(),
            "scope": t.string().optional(),
            "audience": t.string().optional(),
            "options": t.string().optional(),
            "subjectToken": t.string(),
            "subjectTokenType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenRequestOut"])
    types["GoogleIdentityStsV1betaOptionsIn"] = t.struct(
        {
            "audiences": t.array(t.string()).optional(),
            "userProject": t.string().optional(),
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1betaAccessBoundaryIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaOptionsIn"])
    types["GoogleIdentityStsV1betaOptionsOut"] = t.struct(
        {
            "audiences": t.array(t.string()).optional(),
            "userProject": t.string().optional(),
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1betaAccessBoundaryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaOptionsOut"])
    types["GoogleIdentityStsV1ExchangeOauthTokenResponseIn"] = t.struct(
        {
            "refresh_token": t.string().optional(),
            "expires_in": t.integer().optional(),
            "scope": t.string().optional(),
            "id_token": t.string().optional(),
            "access_token": t.string().optional(),
            "token_type": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenResponseIn"])
    types["GoogleIdentityStsV1ExchangeOauthTokenResponseOut"] = t.struct(
        {
            "refresh_token": t.string().optional(),
            "expires_in": t.integer().optional(),
            "scope": t.string().optional(),
            "id_token": t.string().optional(),
            "access_token": t.string().optional(),
            "token_type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenResponseOut"])
    types["GoogleIdentityStsV1ExchangeTokenResponseIn"] = t.struct(
        {
            "issued_token_type": t.string().optional(),
            "expires_in": t.integer().optional(),
            "token_type": t.string().optional(),
            "access_token": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenResponseIn"])
    types["GoogleIdentityStsV1ExchangeTokenResponseOut"] = t.struct(
        {
            "issued_token_type": t.string().optional(),
            "expires_in": t.integer().optional(),
            "token_type": t.string().optional(),
            "access_token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenResponseOut"])
    types["GoogleIdentityStsV1ExchangeOauthTokenRequestIn"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "redirectUri": t.string().optional(),
            "clientId": t.string().optional(),
            "codeVerifier": t.string().optional(),
            "code": t.string().optional(),
            "grantType": t.string(),
            "scope": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenRequestIn"])
    types["GoogleIdentityStsV1ExchangeOauthTokenRequestOut"] = t.struct(
        {
            "refreshToken": t.string().optional(),
            "redirectUri": t.string().optional(),
            "clientId": t.string().optional(),
            "codeVerifier": t.string().optional(),
            "code": t.string().optional(),
            "grantType": t.string(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenRequestOut"])
    types["GoogleIdentityStsV1OptionsIn"] = t.struct(
        {
            "audiences": t.array(t.string()).optional(),
            "userProject": t.string().optional(),
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1AccessBoundaryIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityStsV1OptionsIn"])
    types["GoogleIdentityStsV1OptionsOut"] = t.struct(
        {
            "audiences": t.array(t.string()).optional(),
            "userProject": t.string().optional(),
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1AccessBoundaryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1OptionsOut"])

    functions = {}
    functions["v1Oauthtoken"] = sts.post(
        "v1/introspect",
        t.struct(
            {
                "token": t.string(),
                "tokenTypeHint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1Token"] = sts.post(
        "v1/introspect",
        t.struct(
            {
                "token": t.string(),
                "tokenTypeHint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1Introspect"] = sts.post(
        "v1/introspect",
        t.struct(
            {
                "token": t.string(),
                "tokenTypeHint": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sts", renames=renames, types=Box(types), functions=Box(functions)
    )
