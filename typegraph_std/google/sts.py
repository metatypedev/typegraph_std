from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_sts() -> Import:
    sts = HTTPRuntime("https://sts.googleapis.com/")

    renames = {
        "ErrorResponse": "_sts_1_ErrorResponse",
        "GoogleIamV1BindingIn": "_sts_2_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_sts_3_GoogleIamV1BindingOut",
        "GoogleIdentityStsV1betaAccessBoundaryRuleIn": "_sts_4_GoogleIdentityStsV1betaAccessBoundaryRuleIn",
        "GoogleIdentityStsV1betaAccessBoundaryRuleOut": "_sts_5_GoogleIdentityStsV1betaAccessBoundaryRuleOut",
        "GoogleIdentityStsV1IntrospectTokenRequestIn": "_sts_6_GoogleIdentityStsV1IntrospectTokenRequestIn",
        "GoogleIdentityStsV1IntrospectTokenRequestOut": "_sts_7_GoogleIdentityStsV1IntrospectTokenRequestOut",
        "GoogleIdentityStsV1ExchangeOauthTokenResponseIn": "_sts_8_GoogleIdentityStsV1ExchangeOauthTokenResponseIn",
        "GoogleIdentityStsV1ExchangeOauthTokenResponseOut": "_sts_9_GoogleIdentityStsV1ExchangeOauthTokenResponseOut",
        "GoogleIdentityStsV1betaAccessBoundaryIn": "_sts_10_GoogleIdentityStsV1betaAccessBoundaryIn",
        "GoogleIdentityStsV1betaAccessBoundaryOut": "_sts_11_GoogleIdentityStsV1betaAccessBoundaryOut",
        "GoogleIdentityStsV1ExchangeTokenRequestIn": "_sts_12_GoogleIdentityStsV1ExchangeTokenRequestIn",
        "GoogleIdentityStsV1ExchangeTokenRequestOut": "_sts_13_GoogleIdentityStsV1ExchangeTokenRequestOut",
        "GoogleIdentityStsV1ExchangeOauthTokenRequestIn": "_sts_14_GoogleIdentityStsV1ExchangeOauthTokenRequestIn",
        "GoogleIdentityStsV1ExchangeOauthTokenRequestOut": "_sts_15_GoogleIdentityStsV1ExchangeOauthTokenRequestOut",
        "GoogleIdentityStsV1ExchangeTokenResponseIn": "_sts_16_GoogleIdentityStsV1ExchangeTokenResponseIn",
        "GoogleIdentityStsV1ExchangeTokenResponseOut": "_sts_17_GoogleIdentityStsV1ExchangeTokenResponseOut",
        "GoogleTypeExprIn": "_sts_18_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_sts_19_GoogleTypeExprOut",
        "GoogleIdentityStsV1IntrospectTokenResponseIn": "_sts_20_GoogleIdentityStsV1IntrospectTokenResponseIn",
        "GoogleIdentityStsV1IntrospectTokenResponseOut": "_sts_21_GoogleIdentityStsV1IntrospectTokenResponseOut",
        "GoogleIdentityStsV1betaOptionsIn": "_sts_22_GoogleIdentityStsV1betaOptionsIn",
        "GoogleIdentityStsV1betaOptionsOut": "_sts_23_GoogleIdentityStsV1betaOptionsOut",
        "GoogleIdentityStsV1AccessBoundaryRuleIn": "_sts_24_GoogleIdentityStsV1AccessBoundaryRuleIn",
        "GoogleIdentityStsV1AccessBoundaryRuleOut": "_sts_25_GoogleIdentityStsV1AccessBoundaryRuleOut",
        "GoogleIdentityStsV1AccessBoundaryIn": "_sts_26_GoogleIdentityStsV1AccessBoundaryIn",
        "GoogleIdentityStsV1AccessBoundaryOut": "_sts_27_GoogleIdentityStsV1AccessBoundaryOut",
        "GoogleIdentityStsV1OptionsIn": "_sts_28_GoogleIdentityStsV1OptionsIn",
        "GoogleIdentityStsV1OptionsOut": "_sts_29_GoogleIdentityStsV1OptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
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
    types["GoogleIdentityStsV1ExchangeOauthTokenResponseIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "refresh_token": t.string().optional(),
            "id_token": t.string().optional(),
            "access_token": t.string().optional(),
            "expires_in": t.integer().optional(),
            "token_type": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenResponseIn"])
    types["GoogleIdentityStsV1ExchangeOauthTokenResponseOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "refresh_token": t.string().optional(),
            "id_token": t.string().optional(),
            "access_token": t.string().optional(),
            "expires_in": t.integer().optional(),
            "token_type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenResponseOut"])
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
    types["GoogleIdentityStsV1ExchangeTokenRequestIn"] = t.struct(
        {
            "options": t.string().optional(),
            "scope": t.string().optional(),
            "grantType": t.string(),
            "subjectTokenType": t.string(),
            "requestedTokenType": t.string(),
            "audience": t.string().optional(),
            "subjectToken": t.string(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenRequestIn"])
    types["GoogleIdentityStsV1ExchangeTokenRequestOut"] = t.struct(
        {
            "options": t.string().optional(),
            "scope": t.string().optional(),
            "grantType": t.string(),
            "subjectTokenType": t.string(),
            "requestedTokenType": t.string(),
            "audience": t.string().optional(),
            "subjectToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenRequestOut"])
    types["GoogleIdentityStsV1ExchangeOauthTokenRequestIn"] = t.struct(
        {
            "codeVerifier": t.string().optional(),
            "grantType": t.string(),
            "clientId": t.string().optional(),
            "code": t.string().optional(),
            "redirectUri": t.string().optional(),
            "refreshToken": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenRequestIn"])
    types["GoogleIdentityStsV1ExchangeOauthTokenRequestOut"] = t.struct(
        {
            "codeVerifier": t.string().optional(),
            "grantType": t.string(),
            "clientId": t.string().optional(),
            "code": t.string().optional(),
            "redirectUri": t.string().optional(),
            "refreshToken": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeOauthTokenRequestOut"])
    types["GoogleIdentityStsV1ExchangeTokenResponseIn"] = t.struct(
        {
            "access_token": t.string().optional(),
            "issued_token_type": t.string().optional(),
            "expires_in": t.integer().optional(),
            "token_type": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenResponseIn"])
    types["GoogleIdentityStsV1ExchangeTokenResponseOut"] = t.struct(
        {
            "access_token": t.string().optional(),
            "issued_token_type": t.string().optional(),
            "expires_in": t.integer().optional(),
            "token_type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1ExchangeTokenResponseOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleIdentityStsV1IntrospectTokenResponseIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "iss": t.string().optional(),
            "active": t.boolean().optional(),
            "client_id": t.string().optional(),
            "sub": t.string().optional(),
            "username": t.string().optional(),
            "exp": t.string().optional(),
            "iat": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenResponseIn"])
    types["GoogleIdentityStsV1IntrospectTokenResponseOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "iss": t.string().optional(),
            "active": t.boolean().optional(),
            "client_id": t.string().optional(),
            "sub": t.string().optional(),
            "username": t.string().optional(),
            "exp": t.string().optional(),
            "iat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIdentityStsV1IntrospectTokenResponseOut"])
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
    types["GoogleIdentityStsV1AccessBoundaryRuleIn"] = t.struct(
        {
            "availablePermissions": t.array(t.string()).optional(),
            "availabilityCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "availableResource": t.string().optional(),
        }
    ).named(renames["GoogleIdentityStsV1AccessBoundaryRuleIn"])
    types["GoogleIdentityStsV1AccessBoundaryRuleOut"] = t.struct(
        {
            "availablePermissions": t.array(t.string()).optional(),
            "availabilityCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
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

    functions = {}
    functions["v1Introspect"] = sts.post(
        "v1/token",
        t.struct(
            {
                "options": t.string().optional(),
                "scope": t.string().optional(),
                "grantType": t.string(),
                "subjectTokenType": t.string(),
                "requestedTokenType": t.string(),
                "audience": t.string().optional(),
                "subjectToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1ExchangeTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1Oauthtoken"] = sts.post(
        "v1/token",
        t.struct(
            {
                "options": t.string().optional(),
                "scope": t.string().optional(),
                "grantType": t.string(),
                "subjectTokenType": t.string(),
                "requestedTokenType": t.string(),
                "audience": t.string().optional(),
                "subjectToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1ExchangeTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1Token"] = sts.post(
        "v1/token",
        t.struct(
            {
                "options": t.string().optional(),
                "scope": t.string().optional(),
                "grantType": t.string(),
                "subjectTokenType": t.string(),
                "requestedTokenType": t.string(),
                "audience": t.string().optional(),
                "subjectToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIdentityStsV1ExchangeTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sts", renames=renames, types=Box(types), functions=Box(functions)
    )
