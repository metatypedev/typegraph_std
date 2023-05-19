from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_iamcredentials() -> Import:
    iamcredentials = HTTPRuntime("https://iamcredentials.googleapis.com/")

    renames = {
        "ErrorResponse": "_iamcredentials_1_ErrorResponse",
        "SignJwtResponseIn": "_iamcredentials_2_SignJwtResponseIn",
        "SignJwtResponseOut": "_iamcredentials_3_SignJwtResponseOut",
        "SignBlobResponseIn": "_iamcredentials_4_SignBlobResponseIn",
        "SignBlobResponseOut": "_iamcredentials_5_SignBlobResponseOut",
        "GenerateIdTokenResponseIn": "_iamcredentials_6_GenerateIdTokenResponseIn",
        "GenerateIdTokenResponseOut": "_iamcredentials_7_GenerateIdTokenResponseOut",
        "SignBlobRequestIn": "_iamcredentials_8_SignBlobRequestIn",
        "SignBlobRequestOut": "_iamcredentials_9_SignBlobRequestOut",
        "SignJwtRequestIn": "_iamcredentials_10_SignJwtRequestIn",
        "SignJwtRequestOut": "_iamcredentials_11_SignJwtRequestOut",
        "GenerateAccessTokenRequestIn": "_iamcredentials_12_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_iamcredentials_13_GenerateAccessTokenRequestOut",
        "GenerateIdTokenRequestIn": "_iamcredentials_14_GenerateIdTokenRequestIn",
        "GenerateIdTokenRequestOut": "_iamcredentials_15_GenerateIdTokenRequestOut",
        "GenerateAccessTokenResponseIn": "_iamcredentials_16_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_iamcredentials_17_GenerateAccessTokenResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SignJwtResponseIn"] = t.struct(
        {"signedJwt": t.string().optional(), "keyId": t.string().optional()}
    ).named(renames["SignJwtResponseIn"])
    types["SignJwtResponseOut"] = t.struct(
        {
            "signedJwt": t.string().optional(),
            "keyId": t.string().optional(),
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
    types["GenerateIdTokenResponseIn"] = t.struct(
        {"token": t.string().optional()}
    ).named(renames["GenerateIdTokenResponseIn"])
    types["GenerateIdTokenResponseOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateIdTokenResponseOut"])
    types["SignBlobRequestIn"] = t.struct(
        {"delegates": t.array(t.string()).optional(), "payload": t.string()}
    ).named(renames["SignBlobRequestIn"])
    types["SignBlobRequestOut"] = t.struct(
        {
            "delegates": t.array(t.string()).optional(),
            "payload": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignBlobRequestOut"])
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
    types["GenerateAccessTokenRequestIn"] = t.struct(
        {
            "lifetime": t.string().optional(),
            "delegates": t.array(t.string()).optional(),
            "scope": t.array(t.string()),
        }
    ).named(renames["GenerateAccessTokenRequestIn"])
    types["GenerateAccessTokenRequestOut"] = t.struct(
        {
            "lifetime": t.string().optional(),
            "delegates": t.array(t.string()).optional(),
            "scope": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenRequestOut"])
    types["GenerateIdTokenRequestIn"] = t.struct(
        {
            "includeEmail": t.boolean().optional(),
            "audience": t.string(),
            "delegates": t.array(t.string()).optional(),
        }
    ).named(renames["GenerateIdTokenRequestIn"])
    types["GenerateIdTokenRequestOut"] = t.struct(
        {
            "includeEmail": t.boolean().optional(),
            "audience": t.string(),
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

    functions = {}
    functions["projectsServiceAccountsGenerateAccessToken"] = iamcredentials.post(
        "v1/{name}:signBlob",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignBlobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsSignJwt"] = iamcredentials.post(
        "v1/{name}:signBlob",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignBlobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsGenerateIdToken"] = iamcredentials.post(
        "v1/{name}:signBlob",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignBlobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountsSignBlob"] = iamcredentials.post(
        "v1/{name}:signBlob",
        t.struct(
            {
                "name": t.string(),
                "delegates": t.array(t.string()).optional(),
                "payload": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignBlobResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="iamcredentials",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
