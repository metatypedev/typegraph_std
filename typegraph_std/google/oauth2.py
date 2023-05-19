from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_oauth2() -> Import:
    oauth2 = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_oauth2_1_ErrorResponse",
        "TokeninfoIn": "_oauth2_2_TokeninfoIn",
        "TokeninfoOut": "_oauth2_3_TokeninfoOut",
        "UserinfoIn": "_oauth2_4_UserinfoIn",
        "UserinfoOut": "_oauth2_5_UserinfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TokeninfoIn"] = t.struct(
        {
            "audience": t.string().optional(),
            "email": t.string().optional(),
            "expires_in": t.integer().optional(),
            "issued_to": t.string().optional(),
            "scope": t.string().optional(),
            "user_id": t.string().optional(),
            "verified_email": t.boolean().optional(),
        }
    ).named(renames["TokeninfoIn"])
    types["TokeninfoOut"] = t.struct(
        {
            "audience": t.string().optional(),
            "email": t.string().optional(),
            "expires_in": t.integer().optional(),
            "issued_to": t.string().optional(),
            "scope": t.string().optional(),
            "user_id": t.string().optional(),
            "verified_email": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokeninfoOut"])
    types["UserinfoIn"] = t.struct(
        {
            "email": t.string().optional(),
            "family_name": t.string().optional(),
            "gender": t.string().optional(),
            "given_name": t.string().optional(),
            "hd": t.string().optional(),
            "id": t.string().optional(),
            "link": t.string().optional(),
            "locale": t.string().optional(),
            "name": t.string().optional(),
            "picture": t.string().optional(),
            "verified_email": t.boolean().optional(),
        }
    ).named(renames["UserinfoIn"])
    types["UserinfoOut"] = t.struct(
        {
            "email": t.string().optional(),
            "family_name": t.string().optional(),
            "gender": t.string().optional(),
            "given_name": t.string().optional(),
            "hd": t.string().optional(),
            "id": t.string().optional(),
            "link": t.string().optional(),
            "locale": t.string().optional(),
            "name": t.string().optional(),
            "picture": t.string().optional(),
            "verified_email": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserinfoOut"])

    functions = {}
    functions["Tokeninfo"] = oauth2.post(
        "oauth2/v2/tokeninfo",
        t.struct(
            {
                "access_token": t.string(),
                "id_token": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TokeninfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userinfoGet"] = oauth2.get(
        "oauth2/v2/userinfo",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["UserinfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userinfoV2MeGet"] = oauth2.get(
        "userinfo/v2/me",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["UserinfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="oauth2", renames=renames, types=Box(types), functions=Box(functions)
    )
