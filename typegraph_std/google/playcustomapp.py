from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_playcustomapp():
    playcustomapp = HTTPRuntime("https://playcustomapp.googleapis.com/")

    renames = {
        "ErrorResponse": "_playcustomapp_1_ErrorResponse",
        "OrganizationIn": "_playcustomapp_2_OrganizationIn",
        "OrganizationOut": "_playcustomapp_3_OrganizationOut",
        "CustomAppIn": "_playcustomapp_4_CustomAppIn",
        "CustomAppOut": "_playcustomapp_5_CustomAppOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OrganizationIn"] = t.struct(
        {"organizationId": t.string(), "organizationName": t.string().optional()}
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "organizationId": t.string(),
            "organizationName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["CustomAppIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["CustomAppIn"])
    types["CustomAppOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "languageCode": t.string().optional(),
            "organizations": t.array(t.proxy(renames["OrganizationOut"])).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAppOut"])

    functions = {}
    functions["accountsCustomAppsCreate"] = playcustomapp.post(
        "playcustomapp/v1/accounts/{account}/customApps",
        t.struct(
            {
                "account": t.string().optional(),
                "languageCode": t.string().optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
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
