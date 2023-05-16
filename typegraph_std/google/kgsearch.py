from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_kgsearch() -> Import:
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
            "itemListElement": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "@context": t.struct({"_": t.string().optional()}).optional(),
            "@type": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "itemListElement": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "@context": t.struct({"_": t.string().optional()}).optional(),
            "@type": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])

    functions = {}
    functions["entitiesSearch"] = kgsearch.get(
        "v1/entities:search",
        t.struct(
            {
                "ids": t.string().optional(),
                "prefix": t.boolean().optional(),
                "limit": t.integer().optional(),
                "languages": t.string().optional(),
                "indent": t.boolean().optional(),
                "query": t.string().optional(),
                "types": t.string().optional(),
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
