from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_kgsearch():
    kgsearch = HTTPRuntime("https://kgsearch.googleapis.com/")

    renames = {
        "ErrorResponse": "_kgsearch_1_ErrorResponse",
        "SearchResponseIn": "_kgsearch_2_SearchResponseIn",
        "SearchResponseOut": "_kgsearch_3_SearchResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SearchResponseIn"] = t.struct(
        {
            "@context": t.struct({"_": t.string().optional()}).optional(),
            "@type": t.struct({"_": t.string().optional()}).optional(),
            "itemListElement": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "@context": t.struct({"_": t.string().optional()}).optional(),
            "@type": t.struct({"_": t.string().optional()}).optional(),
            "itemListElement": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])

    functions = {}
    functions["entitiesSearch"] = kgsearch.get(
        "v1/entities:search",
        t.struct(
            {
                "prefix": t.boolean().optional(),
                "limit": t.integer().optional(),
                "indent": t.boolean().optional(),
                "ids": t.string().optional(),
                "query": t.string().optional(),
                "types": t.string().optional(),
                "languages": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="kgsearch", renames=renames, types=Box(types), functions=Box(functions)
    )
