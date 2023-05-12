from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_iamcredentials() -> Import:
    iamcredentials = HTTPRuntime("https://iamcredentials.googleapis.com/")

    renames = {
        "ErrorResponse": "_iamcredentials_1_ErrorResponse",
        "SignJwtRequestIn": "_iamcredentials_2_SignJwtRequestIn",
        "SignJwtRequestOut": "_iamcredentials_3_SignJwtRequestOut",
        "GenerateIdTokenRequestIn": "_iamcredentials_4_GenerateIdTokenRequestIn",
        "GenerateIdTokenRequestOut": "_iamcredentials_5_GenerateIdTokenRequestOut",
        "GenerateIdTokenResponseIn": "_iamcredentials_6_GenerateIdTokenResponseIn",
        "GenerateIdTokenResponseOut": "_iamcredentials_7_GenerateIdTokenResponseOut",
        "GenerateAccessTokenRequestIn": "_iamcredentials_8_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_iamcredentials_9_GenerateAccessTokenRequestOut",
        "SignJwtResponseIn": "_iamcredentials_10_SignJwtResponseIn",
        "SignJwtResponseOut": "_iamcredentials_11_SignJwtResponseOut",
        "SignBlobResponseIn": "_iamcredentials_12_SignBlobResponseIn",
        "SignBlobResponseOut": "_iamcredentials_13_SignBlobResponseOut",
        "SignBlobRequestIn": "_iamcredentials_14_SignBlobRequestIn",
        "SignBlobRequestOut": "_iamcredentials_15_SignBlobRequestOut",
        "GenerateAccessTokenResponseIn": "_iamcredentials_16_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_iamcredentials_17_GenerateAccessTokenResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SignJwtRequestIn"] = t.struct(
        {"payload": t.string(), "delegates": t.array(t.string()).optional()}
    ).named(renames["SignJwtRequestIn"])
    types["SignJwtRequestOut"] = t.struct(
        {
            "payload": t.string(),
            "delegates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignJwtRequestOut"])
    types["GenerateIdTokenRequestIn"] = t.struct(
        {
            "includeEmail": t.boolean().optional(),
            "delegates": t.array(t.string()).optional(),
            "audience": t.string(),
        }
    ).named(renames["GenerateIdTokenRequestIn"])
    types["GenerateIdTokenRequestOut"] = t.struct(
        {
            "includeEmail": t.boolean().optional(),
            "delegates": t.array(t.string()).optional(),
            "audience": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateIdTokenRequestOut"])
    types["GenerateIdTokenResponseIn"] = t.struct(
        {"token": t.string().optional()}
    ).named(renames["GenerateIdTokenResponseIn"])
    types["GenerateIdTokenResponseOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateIdTokenResponseOut"])
    types["GenerateAccessTokenRequestIn"] = t.struct(
        {
            "scope": t.array(t.string()),
            "lifetime": t.string().optional(),
            "delegates": t.array(t.string()).optional(),
        }
    ).named(renames["GenerateAccessTokenRequestIn"])
    types["GenerateAccessTokenRequestOut"] = t.struct(
        {
            "scope": t.array(t.string()),
            "lifetime": t.string().optional(),
            "delegates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenRequestOut"])
    types["SignJwtResponseIn"] = t.struct(
        {"keyId": t.string().optional(), "signedJwt": t.string().optional()}
    ).named(renames["SignJwtResponseIn"])
    types["SignJwtResponseOut"] = t.struct(
        {
            "keyId": t.string().optional(),
            "signedJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignJwtResponseOut"])
    types["SignBlobResponseIn"] = t.struct(
        {"keyId": t.string().optional(), "signedBlob": t.string().optional()}
    ).named(renames["SignBlobResponseIn"])
    types["SignBlobResponseOut"] = t.struct(
        {
            "keyId": t.string().optional(),
            "signedBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignBlobResponseOut"])
    types["SignBlobRequestIn"] = t.struct(
        {"payload": t.string(), "delegates": t.array(t.string()).optional()}
    ).named(renames["SignBlobRequestIn"])
    types["SignBlobRequestOut"] = t.struct(
        {
            "payload": t.string(),
            "delegates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignBlobRequestOut"])
    types["GenerateAccessTokenResponseIn"] = t.struct(
        {"expireTime": t.string().optional(), "accessToken": t.string().optional()}
    ).named(renames["GenerateAccessTokenResponseIn"])
    types["GenerateAccessTokenResponseOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "accessToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenResponseOut"])

    functions = {}
    functions["projectsServiceAccountsGenerateIdToken"] = iamcredentials.post(
        "v1/{name}:generateAccessToken",
        t.struct(
            {
                "name": t.string(),
                "scope": t.array(t.string()),
                "lifetime": t.string().optional(),
                "delegates": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateAccessTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsSignBlob"] = iamcredentials.post(
        "v1/{name}:generateAccessToken",
        t.struct(
            {
                "name": t.string(),
                "scope": t.array(t.string()),
                "lifetime": t.string().optional(),
                "delegates": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateAccessTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsSignJwt"] = iamcredentials.post(
        "v1/{name}:generateAccessToken",
        t.struct(
            {
                "name": t.string(),
                "scope": t.array(t.string()),
                "lifetime": t.string().optional(),
                "delegates": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateAccessTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsGenerateAccessToken"] = iamcredentials.post(
        "v1/{name}:generateAccessToken",
        t.struct(
            {
                "name": t.string(),
                "scope": t.array(t.string()),
                "lifetime": t.string().optional(),
                "delegates": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateAccessTokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="iamcredentials",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
