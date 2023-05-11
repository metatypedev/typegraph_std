from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_iamcredentials() -> Import:
    iamcredentials = HTTPRuntime("https://iamcredentials.googleapis.com/")

    renames = {
        "ErrorResponse": "_iamcredentials_1_ErrorResponse",
        "SignBlobRequestIn": "_iamcredentials_2_SignBlobRequestIn",
        "SignBlobRequestOut": "_iamcredentials_3_SignBlobRequestOut",
        "GenerateAccessTokenRequestIn": "_iamcredentials_4_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_iamcredentials_5_GenerateAccessTokenRequestOut",
        "GenerateAccessTokenResponseIn": "_iamcredentials_6_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_iamcredentials_7_GenerateAccessTokenResponseOut",
        "GenerateIdTokenResponseIn": "_iamcredentials_8_GenerateIdTokenResponseIn",
        "GenerateIdTokenResponseOut": "_iamcredentials_9_GenerateIdTokenResponseOut",
        "SignJwtResponseIn": "_iamcredentials_10_SignJwtResponseIn",
        "SignJwtResponseOut": "_iamcredentials_11_SignJwtResponseOut",
        "SignJwtRequestIn": "_iamcredentials_12_SignJwtRequestIn",
        "SignJwtRequestOut": "_iamcredentials_13_SignJwtRequestOut",
        "SignBlobResponseIn": "_iamcredentials_14_SignBlobResponseIn",
        "SignBlobResponseOut": "_iamcredentials_15_SignBlobResponseOut",
        "GenerateIdTokenRequestIn": "_iamcredentials_16_GenerateIdTokenRequestIn",
        "GenerateIdTokenRequestOut": "_iamcredentials_17_GenerateIdTokenRequestOut",
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
            "scope": t.array(t.string()),
            "lifetime": t.string().optional(),
        }
    ).named(renames["GenerateAccessTokenRequestIn"])
    types["GenerateAccessTokenRequestOut"] = t.struct(
        {
            "delegates": t.array(t.string()).optional(),
            "scope": t.array(t.string()),
            "lifetime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenRequestOut"])
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
    types["GenerateIdTokenResponseIn"] = t.struct(
        {"token": t.string().optional()}
    ).named(renames["GenerateIdTokenResponseIn"])
    types["GenerateIdTokenResponseOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateIdTokenResponseOut"])
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
    types["SignBlobResponseIn"] = t.struct(
        {"signedBlob": t.string().optional(), "keyId": t.string().optional()}
    ).named(renames["SignBlobResponseIn"])
    types["SignBlobResponseOut"] = t.struct(
        {
            "signedBlob": t.string().optional(),
            "keyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignBlobResponseOut"])
    types["GenerateIdTokenRequestIn"] = t.struct(
        {
            "delegates": t.array(t.string()).optional(),
            "includeEmail": t.boolean().optional(),
            "audience": t.string(),
        }
    ).named(renames["GenerateIdTokenRequestIn"])
    types["GenerateIdTokenRequestOut"] = t.struct(
        {
            "delegates": t.array(t.string()).optional(),
            "includeEmail": t.boolean().optional(),
            "audience": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateIdTokenRequestOut"])

    functions = {}
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
        importer="iamcredentials", renames=renames, types=types, functions=functions
    )
