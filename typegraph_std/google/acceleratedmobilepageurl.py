from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_acceleratedmobilepageurl() -> Import:
    acceleratedmobilepageurl = HTTPRuntime(
        "https://acceleratedmobilepageurl.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_acceleratedmobilepageurl_1_ErrorResponse",
        "AmpUrlErrorIn": "_acceleratedmobilepageurl_2_AmpUrlErrorIn",
        "AmpUrlErrorOut": "_acceleratedmobilepageurl_3_AmpUrlErrorOut",
        "BatchGetAmpUrlsResponseIn": "_acceleratedmobilepageurl_4_BatchGetAmpUrlsResponseIn",
        "BatchGetAmpUrlsResponseOut": "_acceleratedmobilepageurl_5_BatchGetAmpUrlsResponseOut",
        "BatchGetAmpUrlsRequestIn": "_acceleratedmobilepageurl_6_BatchGetAmpUrlsRequestIn",
        "BatchGetAmpUrlsRequestOut": "_acceleratedmobilepageurl_7_BatchGetAmpUrlsRequestOut",
        "AmpUrlIn": "_acceleratedmobilepageurl_8_AmpUrlIn",
        "AmpUrlOut": "_acceleratedmobilepageurl_9_AmpUrlOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AmpUrlErrorIn"] = t.struct(
        {
            "originalUrl": t.string().optional(),
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["AmpUrlErrorIn"])
    types["AmpUrlErrorOut"] = t.struct(
        {
            "originalUrl": t.string().optional(),
            "errorCode": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmpUrlErrorOut"])
    types["BatchGetAmpUrlsResponseIn"] = t.struct(
        {
            "ampUrls": t.array(t.proxy(renames["AmpUrlIn"])).optional(),
            "urlErrors": t.array(t.proxy(renames["AmpUrlErrorIn"])).optional(),
        }
    ).named(renames["BatchGetAmpUrlsResponseIn"])
    types["BatchGetAmpUrlsResponseOut"] = t.struct(
        {
            "ampUrls": t.array(t.proxy(renames["AmpUrlOut"])).optional(),
            "urlErrors": t.array(t.proxy(renames["AmpUrlErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAmpUrlsResponseOut"])
    types["BatchGetAmpUrlsRequestIn"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "lookupStrategy": t.string().optional(),
        }
    ).named(renames["BatchGetAmpUrlsRequestIn"])
    types["BatchGetAmpUrlsRequestOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "lookupStrategy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAmpUrlsRequestOut"])
    types["AmpUrlIn"] = t.struct(
        {
            "cdnAmpUrl": t.string().optional(),
            "ampUrl": t.string().optional(),
            "originalUrl": t.string().optional(),
        }
    ).named(renames["AmpUrlIn"])
    types["AmpUrlOut"] = t.struct(
        {
            "cdnAmpUrl": t.string().optional(),
            "ampUrl": t.string().optional(),
            "originalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmpUrlOut"])

    functions = {}
    functions["ampUrlsBatchGet"] = acceleratedmobilepageurl.post(
        "v1/ampUrls:batchGet",
        t.struct(
            {
                "urls": t.array(t.string()).optional(),
                "lookupStrategy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetAmpUrlsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="acceleratedmobilepageurl",
        renames=renames,
        types=types,
        functions=functions,
    )
