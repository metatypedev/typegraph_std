from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_iamcredentials():
    iamcredentials = HTTPRuntime("https://iamcredentials.googleapis.com/")

    renames = {
        "ErrorResponse": "_iamcredentials_1_ErrorResponse",
        "SignBlobRequestIn": "_iamcredentials_2_SignBlobRequestIn",
        "SignBlobRequestOut": "_iamcredentials_3_SignBlobRequestOut",
        "GenerateAccessTokenRequestIn": "_iamcredentials_4_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_iamcredentials_5_GenerateAccessTokenRequestOut",
        "GenerateIdTokenResponseIn": "_iamcredentials_6_GenerateIdTokenResponseIn",
        "GenerateIdTokenResponseOut": "_iamcredentials_7_GenerateIdTokenResponseOut",
        "GenerateIdTokenRequestIn": "_iamcredentials_8_GenerateIdTokenRequestIn",
        "GenerateIdTokenRequestOut": "_iamcredentials_9_GenerateIdTokenRequestOut",
        "GenerateAccessTokenResponseIn": "_iamcredentials_10_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_iamcredentials_11_GenerateAccessTokenResponseOut",
        "SignJwtRequestIn": "_iamcredentials_12_SignJwtRequestIn",
        "SignJwtRequestOut": "_iamcredentials_13_SignJwtRequestOut",
        "SignJwtResponseIn": "_iamcredentials_14_SignJwtResponseIn",
        "SignJwtResponseOut": "_iamcredentials_15_SignJwtResponseOut",
        "SignBlobResponseIn": "_iamcredentials_16_SignBlobResponseIn",
        "SignBlobResponseOut": "_iamcredentials_17_SignBlobResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GenerateAccessTokenRequestIn"] = t.struct(
        {
            "delegates": t.array(t.string()).optional(),
            "lifetime": t.string().optional(),
            "scope": t.array(t.string()),
        }
    ).named(renames["GenerateAccessTokenRequestIn"])
    types["GenerateAccessTokenRequestOut"] = t.struct(
        {
            "delegates": t.array(t.string()).optional(),
            "lifetime": t.string().optional(),
            "scope": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenRequestOut"])
    types["GenerateIdTokenResponseIn"] = t.struct(
        {"token": t.string().optional()}
    ).named(renames["GenerateIdTokenResponseIn"])
    types["GenerateIdTokenResponseOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateIdTokenResponseOut"])
    types["GenerateIdTokenRequestIn"] = t.struct(
        {
            "audience": t.string(),
            "includeEmail": t.boolean().optional(),
            "delegates": t.array(t.string()).optional(),
        }
    ).named(renames["GenerateIdTokenRequestIn"])
    types["GenerateIdTokenRequestOut"] = t.struct(
        {
            "audience": t.string(),
            "includeEmail": t.boolean().optional(),
            "delegates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateIdTokenRequestOut"])
    types["GenerateAccessTokenResponseIn"] = t.struct(
        {"accessToken": t.string().optional(), "expireTime": t.string().optional()}
    ).named(renames["GenerateAccessTokenResponseIn"])
    types["GenerateAccessTokenResponseOut"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenResponseOut"])
    types["SignJwtRequestIn"] = t.struct(
        {"delegates": t.array(t.string()).optional(), "payload": t.string()}
    ).named(renames["SignJwtRequestIn"])
    types["SignJwtRequestOut"] = t.struct(
        {
            "delegates": t.array(t.string()).optional(),
            "payload": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignJwtRequestOut"])
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

    functions = {}
    functions["projectsServiceAccountsGenerateIdToken"] = iamcredentials.post(
        "v1/{name}:signJwt",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignJwtResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsSignBlob"] = iamcredentials.post(
        "v1/{name}:signJwt",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignJwtResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsGenerateAccessToken"] = iamcredentials.post(
        "v1/{name}:signJwt",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignJwtResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsSignJwt"] = iamcredentials.post(
        "v1/{name}:signJwt",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignJwtResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="iamcredentials",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
