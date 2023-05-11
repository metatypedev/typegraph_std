from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_webfonts() -> Import:
    webfonts = HTTPRuntime("https://webfonts.googleapis.com/")

    renames = {
        "ErrorResponse": "_webfonts_1_ErrorResponse",
        "WebfontIn": "_webfonts_2_WebfontIn",
        "WebfontOut": "_webfonts_3_WebfontOut",
        "AxisIn": "_webfonts_4_AxisIn",
        "AxisOut": "_webfonts_5_AxisOut",
        "WebfontListIn": "_webfonts_6_WebfontListIn",
        "WebfontListOut": "_webfonts_7_WebfontListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["WebfontIn"] = t.struct(
        {
            "menu": t.string().optional(),
            "lastModified": t.string().optional(),
            "subsets": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "axes": t.array(t.proxy(renames["AxisIn"])).optional(),
            "category": t.string().optional(),
            "kind": t.string().optional(),
            "variants": t.array(t.string()).optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
            "family": t.string().optional(),
        }
    ).named(renames["WebfontIn"])
    types["WebfontOut"] = t.struct(
        {
            "menu": t.string().optional(),
            "lastModified": t.string().optional(),
            "subsets": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "axes": t.array(t.proxy(renames["AxisOut"])).optional(),
            "category": t.string().optional(),
            "kind": t.string().optional(),
            "variants": t.array(t.string()).optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
            "family": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebfontOut"])
    types["AxisIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "start": t.number().optional(),
            "end": t.number().optional(),
        }
    ).named(renames["AxisIn"])
    types["AxisOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "start": t.number().optional(),
            "end": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AxisOut"])
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
                "subset": t.string().optional(),
                "family": t.string().optional(),
                "capability": t.string().optional(),
                "sort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebfontListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="webfonts", renames=renames, types=types, functions=functions
    )
