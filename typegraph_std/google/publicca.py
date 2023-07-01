from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_publicca():
    publicca = HTTPRuntime("https://publicca.googleapis.com/")

    renames = {
        "ErrorResponse": "_publicca_1_ErrorResponse",
        "ExternalAccountKeyIn": "_publicca_2_ExternalAccountKeyIn",
        "ExternalAccountKeyOut": "_publicca_3_ExternalAccountKeyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExternalAccountKeyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExternalAccountKeyIn"]
    )
    types["ExternalAccountKeyOut"] = t.struct(
        {
            "keyId": t.string().optional(),
            "name": t.string().optional(),
            "b64MacKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalAccountKeyOut"])

    functions = {}
    functions["projectsLocationsExternalAccountKeysCreate"] = publicca.post(
        "v1/{parent}/externalAccountKeys",
        t.struct(
            {
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExternalAccountKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="publicca", renames=renames, types=Box(types), functions=Box(functions)
    )
