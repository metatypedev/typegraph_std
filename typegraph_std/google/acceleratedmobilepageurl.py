from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_acceleratedmobilepageurl():
    acceleratedmobilepageurl = HTTPRuntime(
        "https://acceleratedmobilepageurl.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_acceleratedmobilepageurl_1_ErrorResponse",
        "BatchGetAmpUrlsResponseIn": "_acceleratedmobilepageurl_2_BatchGetAmpUrlsResponseIn",
        "BatchGetAmpUrlsResponseOut": "_acceleratedmobilepageurl_3_BatchGetAmpUrlsResponseOut",
        "BatchGetAmpUrlsRequestIn": "_acceleratedmobilepageurl_4_BatchGetAmpUrlsRequestIn",
        "BatchGetAmpUrlsRequestOut": "_acceleratedmobilepageurl_5_BatchGetAmpUrlsRequestOut",
        "AmpUrlIn": "_acceleratedmobilepageurl_6_AmpUrlIn",
        "AmpUrlOut": "_acceleratedmobilepageurl_7_AmpUrlOut",
        "AmpUrlErrorIn": "_acceleratedmobilepageurl_8_AmpUrlErrorIn",
        "AmpUrlErrorOut": "_acceleratedmobilepageurl_9_AmpUrlErrorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BatchGetAmpUrlsResponseIn"] = t.struct(
        {
            "urlErrors": t.array(t.proxy(renames["AmpUrlErrorIn"])).optional(),
            "ampUrls": t.array(t.proxy(renames["AmpUrlIn"])).optional(),
        }
    ).named(renames["BatchGetAmpUrlsResponseIn"])
    types["BatchGetAmpUrlsResponseOut"] = t.struct(
        {
            "urlErrors": t.array(t.proxy(renames["AmpUrlErrorOut"])).optional(),
            "ampUrls": t.array(t.proxy(renames["AmpUrlOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAmpUrlsResponseOut"])
    types["BatchGetAmpUrlsRequestIn"] = t.struct(
        {
            "lookupStrategy": t.string().optional(),
            "urls": t.array(t.string()).optional(),
        }
    ).named(renames["BatchGetAmpUrlsRequestIn"])
    types["BatchGetAmpUrlsRequestOut"] = t.struct(
        {
            "lookupStrategy": t.string().optional(),
            "urls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetAmpUrlsRequestOut"])
    types["AmpUrlIn"] = t.struct(
        {
            "originalUrl": t.string().optional(),
            "cdnAmpUrl": t.string().optional(),
            "ampUrl": t.string().optional(),
        }
    ).named(renames["AmpUrlIn"])
    types["AmpUrlOut"] = t.struct(
        {
            "originalUrl": t.string().optional(),
            "cdnAmpUrl": t.string().optional(),
            "ampUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AmpUrlOut"])
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

    functions = {}
    functions["ampUrlsBatchGet"] = acceleratedmobilepageurl.post(
        "v1/ampUrls:batchGet",
        t.struct(
            {
                "lookupStrategy": t.string().optional(),
                "urls": t.array(t.string()).optional(),
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
        types=Box(types),
        functions=Box(functions),
    )
