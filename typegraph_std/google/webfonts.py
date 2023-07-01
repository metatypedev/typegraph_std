from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_webfonts():
    webfonts = HTTPRuntime("https://webfonts.googleapis.com/")

    renames = {
        "ErrorResponse": "_webfonts_1_ErrorResponse",
        "AxisIn": "_webfonts_2_AxisIn",
        "AxisOut": "_webfonts_3_AxisOut",
        "WebfontIn": "_webfonts_4_WebfontIn",
        "WebfontOut": "_webfonts_5_WebfontOut",
        "WebfontListIn": "_webfonts_6_WebfontListIn",
        "WebfontListOut": "_webfonts_7_WebfontListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "kind": t.string().optional(),
            "menu": t.string().optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
            "axes": t.array(t.proxy(renames["AxisIn"])).optional(),
            "family": t.string().optional(),
            "category": t.string().optional(),
            "version": t.string().optional(),
            "subsets": t.array(t.string()).optional(),
            "variants": t.array(t.string()).optional(),
            "lastModified": t.string().optional(),
        }
    ).named(renames["WebfontIn"])
    types["WebfontOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "menu": t.string().optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
            "axes": t.array(t.proxy(renames["AxisOut"])).optional(),
            "family": t.string().optional(),
            "category": t.string().optional(),
            "version": t.string().optional(),
            "subsets": t.array(t.string()).optional(),
            "variants": t.array(t.string()).optional(),
            "lastModified": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebfontOut"])
    types["WebfontListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["WebfontIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["WebfontListIn"])
    types["WebfontListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["WebfontOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebfontListOut"])

    functions = {}
    functions["webfontsList"] = webfonts.get(
        "v1/webfonts",
        t.struct(
            {
                "capability": t.string().optional(),
                "sort": t.string().optional(),
                "subset": t.string().optional(),
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
