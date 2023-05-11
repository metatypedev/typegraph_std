from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_sts() -> Import:
    sts = HTTPRuntime("https://sts.googleapis.com/")

    renames = {
        "ErrorResponse": "_sts_1_ErrorResponse",
        "GoogleIdentityStsV1IntrospectTokenRequestIn": "_sts_2_GoogleIdentityStsV1IntrospectTokenRequestIn",
        "GoogleIdentityStsV1IntrospectTokenRequestOut": "_sts_3_GoogleIdentityStsV1IntrospectTokenRequestOut",
        "GoogleIdentityStsV1betaAccessBoundaryRuleIn": "_sts_4_GoogleIdentityStsV1betaAccessBoundaryRuleIn",
        "GoogleIdentityStsV1betaAccessBoundaryRuleOut": "_sts_5_GoogleIdentityStsV1betaAccessBoundaryRuleOut",
        "GoogleIamV1BindingIn": "_sts_6_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_sts_7_GoogleIamV1BindingOut",
        "GoogleIdentityStsV1ExchangeTokenResponseIn": "_sts_8_GoogleIdentityStsV1ExchangeTokenResponseIn",
        "GoogleIdentityStsV1ExchangeTokenResponseOut": "_sts_9_GoogleIdentityStsV1ExchangeTokenResponseOut",
        "GoogleIdentityStsV1ExchangeTokenRequestIn": "_sts_10_GoogleIdentityStsV1ExchangeTokenRequestIn",
        "GoogleIdentityStsV1ExchangeTokenRequestOut": "_sts_11_GoogleIdentityStsV1ExchangeTokenRequestOut",
        "GoogleIdentityStsV1ExchangeOauthTokenResponseIn": "_sts_12_GoogleIdentityStsV1ExchangeOauthTokenResponseIn",
        "GoogleIdentityStsV1ExchangeOauthTokenResponseOut": "_sts_13_GoogleIdentityStsV1ExchangeOauthTokenResponseOut",
        "GoogleIdentityStsV1AccessBoundaryRuleIn": "_sts_14_GoogleIdentityStsV1AccessBoundaryRuleIn",
        "GoogleIdentityStsV1AccessBoundaryRuleOut": "_sts_15_GoogleIdentityStsV1AccessBoundaryRuleOut",
        "GoogleIdentityStsV1AccessBoundaryIn": "_sts_16_GoogleIdentityStsV1AccessBoundaryIn",
        "GoogleIdentityStsV1AccessBoundaryOut": "_sts_17_GoogleIdentityStsV1AccessBoundaryOut",
        "GoogleIdentityStsV1ExchangeOauthTokenRequestIn": "_sts_18_GoogleIdentityStsV1ExchangeOauthTokenRequestIn",
        "GoogleIdentityStsV1ExchangeOauthTokenRequestOut": "_sts_19_GoogleIdentityStsV1ExchangeOauthTokenRequestOut",
        "GoogleTypeExprIn": "_sts_20_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_sts_21_GoogleTypeExprOut",
        "GoogleIdentityStsV1IntrospectTokenResponseIn": "_sts_22_GoogleIdentityStsV1IntrospectTokenResponseIn",
        "GoogleIdentityStsV1IntrospectTokenResponseOut": "_sts_23_GoogleIdentityStsV1IntrospectTokenResponseOut",
        "GoogleIdentityStsV1OptionsIn": "_sts_24_GoogleIdentityStsV1OptionsIn",
        "GoogleIdentityStsV1OptionsOut": "_sts_25_GoogleIdentityStsV1OptionsOut",
        "GoogleIdentityStsV1betaAccessBoundaryIn": "_sts_26_GoogleIdentityStsV1betaAccessBoundaryIn",
        "GoogleIdentityStsV1betaAccessBoundaryOut": "_sts_27_GoogleIdentityStsV1betaAccessBoundaryOut",
        "GoogleIdentityStsV1betaOptionsIn": "_sts_28_GoogleIdentityStsV1betaOptionsIn",
        "GoogleIdentityStsV1betaOptionsOut": "_sts_29_GoogleIdentityStsV1betaOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleIdentityStsV1IntrospectTokenRequestIn"] = t.struct(
        {"tokenTypeHint": t.string().optional(), "token": t.string()}
    ).named(renames["GoogleIdentityStsV1IntrospectTokenRequestIn"])
    types["GoogleIdentityStsV1IntrospectTokenRequestOut"] = t.struct(
        {
            "tokenTypeHint": t.string().optional(),
            "token": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenRequestOut"])
    types["GoogleIdentityStsV1betaAccessBoundaryRuleIn"] = t.struct(
        {
            "availablePermissions": t.array(t.string()).optional(),
            "availabilityCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "availableResource": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaAccessBoundaryRuleIn"])
    types["GoogleIdentityStsV1betaAccessBoundaryRuleOut"] = t.struct(
        {
            "availablePermissions": t.array(t.string()).optional(),
            "availabilityCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "availableResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaAccessBoundaryRuleOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleIdentityStsV1ExchangeTokenResponseIn"] = t.struct(
        {
            "token_type": t.string().optional(),
            "issued_token_type": t.string().optional(),
            "access_token": t.string().optional(),
            "expires_in": t.integer().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenResponseIn"])
    types["GoogleIdentityStsV1ExchangeTokenResponseOut"] = t.struct(
        {
            "token_type": t.string().optional(),
            "issued_token_type": t.string().optional(),
            "access_token": t.string().optional(),
            "expires_in": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenResponseOut"])
    types["GoogleIdentityStsV1ExchangeTokenRequestIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "subjectTokenType": t.string(),
            "subjectToken": t.string(),
            "requestedTokenType": t.string(),
            "grantType": t.string(),
            "options": t.string().optional(),
            "audience": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenRequestIn"])
    types["GoogleIdentityStsV1ExchangeTokenRequestOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "subjectTokenType": t.string(),
            "subjectToken": t.string(),
            "requestedTokenType": t.string(),
            "grantType": t.string(),
            "options": t.string().optional(),
            "audience": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenRequestOut"])
    types["GoogleIdentityStsV1ExchangeOauthTokenResponseIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "access_token": t.string().optional(),
            "expires_in": t.integer().optional(),
            "id_token": t.string().optional(),
            "token_type": t.string().optional(),
            "refresh_token": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenResponseIn"])
    types["GoogleIdentityStsV1ExchangeOauthTokenResponseOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "access_token": t.string().optional(),
            "expires_in": t.integer().optional(),
            "id_token": t.string().optional(),
            "token_type": t.string().optional(),
            "refresh_token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenResponseOut"])
    types["GoogleIdentityStsV1AccessBoundaryRuleIn"] = t.struct(
        {
            "availabilityCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "availablePermissions": t.array(t.string()).optional(),
            "availableResource": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1AccessBoundaryRuleIn"])
    types["GoogleIdentityStsV1AccessBoundaryRuleOut"] = t.struct(
        {
            "availabilityCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "availablePermissions": t.array(t.string()).optional(),
            "availableResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1AccessBoundaryRuleOut"])
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
    types["GoogleIdentityStsV1ExchangeOauthTokenRequestIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "clientId": t.string().optional(),
            "codeVerifier": t.string().optional(),
            "redirectUri": t.string().optional(),
            "refreshToken": t.string().optional(),
            "code": t.string().optional(),
            "grantType": t.string(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenRequestIn"])
    types["GoogleIdentityStsV1ExchangeOauthTokenRequestOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "clientId": t.string().optional(),
            "codeVerifier": t.string().optional(),
            "redirectUri": t.string().optional(),
            "refreshToken": t.string().optional(),
            "code": t.string().optional(),
            "grantType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenRequestOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleIdentityStsV1IntrospectTokenResponseIn"] = t.struct(
        {
            "exp": t.string().optional(),
            "scope": t.string().optional(),
            "active": t.boolean().optional(),
            "sub": t.string().optional(),
            "username": t.string().optional(),
            "iss": t.string().optional(),
            "iat": t.string().optional(),
            "client_id": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenResponseIn"])
    types["GoogleIdentityStsV1IntrospectTokenResponseOut"] = t.struct(
        {
            "exp": t.string().optional(),
            "scope": t.string().optional(),
            "active": t.boolean().optional(),
            "sub": t.string().optional(),
            "username": t.string().optional(),
            "iss": t.string().optional(),
            "iat": t.string().optional(),
            "client_id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"])
    types["GoogleIdentityStsV1OptionsIn"] = t.struct(
        {
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1AccessBoundaryIn"]
            ).optional(),
            "userProject": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIdentityStsV1OptionsIn"])
    types["GoogleIdentityStsV1OptionsOut"] = t.struct(
        {
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1AccessBoundaryOut"]
            ).optional(),
            "userProject": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1OptionsOut"])
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
    types["GoogleIdentityStsV1betaOptionsIn"] = t.struct(
        {
            "userProject": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1betaAccessBoundaryIn"]
            ).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaOptionsIn"])
    types["GoogleIdentityStsV1betaOptionsOut"] = t.struct(
        {
            "userProject": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "accessBoundary": t.proxy(
                renames["GoogleIdentityStsV1betaAccessBoundaryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1betaOptionsOut"])

    functions = {}
    functions["v1Token"] = sts.post(
        "v1/introspect",
        t.struct(
            {
                "tokenTypeHint": t.string().optional(),
                "token": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1Oauthtoken"] = sts.post(
        "v1/introspect",
        t.struct(
            {
                "tokenTypeHint": t.string().optional(),
                "token": t.string(),
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
                "tokenTypeHint": t.string().optional(),
                "token": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="sts", renames=renames, types=types, functions=functions)
