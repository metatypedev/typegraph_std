from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_siteVerification():
    siteVerification = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_siteVerification_1_ErrorResponse",
        "SiteVerificationWebResourceListResponseIn": "_siteVerification_2_SiteVerificationWebResourceListResponseIn",
        "SiteVerificationWebResourceListResponseOut": "_siteVerification_3_SiteVerificationWebResourceListResponseOut",
        "SiteVerificationWebResourceGettokenRequestIn": "_siteVerification_4_SiteVerificationWebResourceGettokenRequestIn",
        "SiteVerificationWebResourceGettokenRequestOut": "_siteVerification_5_SiteVerificationWebResourceGettokenRequestOut",
        "SiteVerificationWebResourceResourceIn": "_siteVerification_6_SiteVerificationWebResourceResourceIn",
        "SiteVerificationWebResourceResourceOut": "_siteVerification_7_SiteVerificationWebResourceResourceOut",
        "SiteVerificationWebResourceGettokenResponseIn": "_siteVerification_8_SiteVerificationWebResourceGettokenResponseIn",
        "SiteVerificationWebResourceGettokenResponseOut": "_siteVerification_9_SiteVerificationWebResourceGettokenResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SiteVerificationWebResourceListResponseIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["SiteVerificationWebResourceResourceIn"])
            ).optional()
        }
    ).named(renames["SiteVerificationWebResourceListResponseIn"])
    types["SiteVerificationWebResourceListResponseOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["SiteVerificationWebResourceResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteVerificationWebResourceListResponseOut"])
    types["SiteVerificationWebResourceGettokenRequestIn"] = t.struct(
        {
            "verificationMethod": t.string().optional(),
            "site": t.struct(
                {"type": t.string().optional(), "identifier": t.string().optional()}
            ).optional(),
        }
    ).named(renames["SiteVerificationWebResourceGettokenRequestIn"])
    types["SiteVerificationWebResourceGettokenRequestOut"] = t.struct(
        {
            "verificationMethod": t.string().optional(),
            "site": t.struct(
                {"type": t.string().optional(), "identifier": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteVerificationWebResourceGettokenRequestOut"])
    types["SiteVerificationWebResourceResourceIn"] = t.struct(
        {
            "id": t.string().optional(),
            "site": t.struct(
                {"type": t.string().optional(), "identifier": t.string().optional()}
            ).optional(),
            "owners": t.array(t.string()).optional(),
        }
    ).named(renames["SiteVerificationWebResourceResourceIn"])
    types["SiteVerificationWebResourceResourceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "site": t.struct(
                {"type": t.string().optional(), "identifier": t.string().optional()}
            ).optional(),
            "owners": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteVerificationWebResourceResourceOut"])
    types["SiteVerificationWebResourceGettokenResponseIn"] = t.struct(
        {"token": t.string().optional(), "method": t.string().optional()}
    ).named(renames["SiteVerificationWebResourceGettokenResponseIn"])
    types["SiteVerificationWebResourceGettokenResponseOut"] = t.struct(
        {
            "token": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteVerificationWebResourceGettokenResponseOut"])

    functions = {}
    functions["webResourceGet"] = siteVerification.post(
        "token",
        t.struct(
            {
                "verificationMethod": t.string().optional(),
                "site": t.struct(
                    {"type": t.string().optional(), "identifier": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteVerificationWebResourceGettokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webResourceDelete"] = siteVerification.post(
        "token",
        t.struct(
            {
                "verificationMethod": t.string().optional(),
                "site": t.struct(
                    {"type": t.string().optional(), "identifier": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteVerificationWebResourceGettokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webResourceUpdate"] = siteVerification.post(
        "token",
        t.struct(
            {
                "verificationMethod": t.string().optional(),
                "site": t.struct(
                    {"type": t.string().optional(), "identifier": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteVerificationWebResourceGettokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webResourceInsert"] = siteVerification.post(
        "token",
        t.struct(
            {
                "verificationMethod": t.string().optional(),
                "site": t.struct(
                    {"type": t.string().optional(), "identifier": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteVerificationWebResourceGettokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webResourcePatch"] = siteVerification.post(
        "token",
        t.struct(
            {
                "verificationMethod": t.string().optional(),
                "site": t.struct(
                    {"type": t.string().optional(), "identifier": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteVerificationWebResourceGettokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webResourceList"] = siteVerification.post(
        "token",
        t.struct(
            {
                "verificationMethod": t.string().optional(),
                "site": t.struct(
                    {"type": t.string().optional(), "identifier": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteVerificationWebResourceGettokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webResourceGetToken"] = siteVerification.post(
        "token",
        t.struct(
            {
                "verificationMethod": t.string().optional(),
                "site": t.struct(
                    {"type": t.string().optional(), "identifier": t.string().optional()}
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SiteVerificationWebResourceGettokenResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="siteVerification",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
