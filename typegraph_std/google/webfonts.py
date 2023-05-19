from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_webfonts() -> Import:
    webfonts = HTTPRuntime("https://webfonts.googleapis.com/")

    renames = {
        "ErrorResponse": "_webfonts_1_ErrorResponse",
        "WebfontListIn": "_webfonts_2_WebfontListIn",
        "WebfontListOut": "_webfonts_3_WebfontListOut",
        "AxisIn": "_webfonts_4_AxisIn",
        "AxisOut": "_webfonts_5_AxisOut",
        "WebfontIn": "_webfonts_6_WebfontIn",
        "WebfontOut": "_webfonts_7_WebfontOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["WebfontListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["WebfontIn"])).optional(),
        }
    ).named(renames["WebfontListIn"])
    types["WebfontListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["WebfontOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebfontListOut"])
    types["AxisIn"] = t.struct(
        {
            "start": t.number().optional(),
            "end": t.number().optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["AxisIn"])
    types["AxisOut"] = t.struct(
        {
            "start": t.number().optional(),
            "end": t.number().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AxisOut"])
    types["WebfontIn"] = t.struct(
        {
            "variants": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
            "axes": t.array(t.proxy(renames["AxisIn"])).optional(),
            "version": t.string().optional(),
            "subsets": t.array(t.string()).optional(),
            "lastModified": t.string().optional(),
            "family": t.string().optional(),
            "kind": t.string().optional(),
            "menu": t.string().optional(),
        }
    ).named(renames["WebfontIn"])
    types["WebfontOut"] = t.struct(
        {
            "variants": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
            "axes": t.array(t.proxy(renames["AxisOut"])).optional(),
            "version": t.string().optional(),
            "subsets": t.array(t.string()).optional(),
            "lastModified": t.string().optional(),
            "family": t.string().optional(),
            "kind": t.string().optional(),
            "menu": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebfontOut"])

    functions = {}
    functions["webfontsList"] = webfonts.get(
        "v1/webfonts",
        t.struct(
            {
                "sort": t.string().optional(),
                "subset": t.string().optional(),
                "capability": t.string().optional(),
                "family": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebfontListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="webfonts", renames=renames, types=Box(types), functions=Box(functions)
    )
