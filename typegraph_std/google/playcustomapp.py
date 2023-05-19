from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_playcustomapp() -> Import:
    playcustomapp = HTTPRuntime("https://playcustomapp.googleapis.com/")

    renames = {
        "ErrorResponse": "_playcustomapp_1_ErrorResponse",
        "CustomAppIn": "_playcustomapp_2_CustomAppIn",
        "CustomAppOut": "_playcustomapp_3_CustomAppOut",
        "OrganizationIn": "_playcustomapp_4_OrganizationIn",
        "OrganizationOut": "_playcustomapp_5_OrganizationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CustomAppIn"] = t.struct(
        {
            "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
            "languageCode": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["CustomAppIn"])
    types["CustomAppOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "organizations": t.array(t.proxy(renames["OrganizationOut"])).optional(),
            "languageCode": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAppOut"])
    types["OrganizationIn"] = t.struct(
        {"organizationName": t.string().optional(), "organizationId": t.string()}
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "organizationName": t.string().optional(),
            "organizationId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])

    functions = {}
    functions["accountsCustomAppsCreate"] = playcustomapp.post(
        "playcustomapp/v1/accounts/{account}/customApps",
        t.struct(
            {
                "account": t.string().optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "languageCode": t.string().optional(),
                "title": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="playcustomapp",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
