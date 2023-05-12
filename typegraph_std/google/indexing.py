from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_indexing() -> Import:
    indexing = HTTPRuntime("https://indexing.googleapis.com/")

    renames = {
        "ErrorResponse": "_indexing_1_ErrorResponse",
        "UrlNotificationIn": "_indexing_2_UrlNotificationIn",
        "UrlNotificationOut": "_indexing_3_UrlNotificationOut",
        "PublishUrlNotificationResponseIn": "_indexing_4_PublishUrlNotificationResponseIn",
        "PublishUrlNotificationResponseOut": "_indexing_5_PublishUrlNotificationResponseOut",
        "UrlNotificationMetadataIn": "_indexing_6_UrlNotificationMetadataIn",
        "UrlNotificationMetadataOut": "_indexing_7_UrlNotificationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UrlNotificationIn"] = t.struct(
        {
            "url": t.string().optional(),
            "type": t.string().optional(),
            "notifyTime": t.string().optional(),
        }
    ).named(renames["UrlNotificationIn"])
    types["UrlNotificationOut"] = t.struct(
        {
            "url": t.string().optional(),
            "type": t.string().optional(),
            "notifyTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlNotificationOut"])
    types["PublishUrlNotificationResponseIn"] = t.struct(
        {
            "urlNotificationMetadata": t.proxy(
                renames["UrlNotificationMetadataIn"]
            ).optional()
        }
    ).named(renames["PublishUrlNotificationResponseIn"])
    types["PublishUrlNotificationResponseOut"] = t.struct(
        {
            "urlNotificationMetadata": t.proxy(
                renames["UrlNotificationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishUrlNotificationResponseOut"])
    types["UrlNotificationMetadataIn"] = t.struct(
        {
            "url": t.string().optional(),
            "latestUpdate": t.proxy(renames["UrlNotificationIn"]).optional(),
            "latestRemove": t.proxy(renames["UrlNotificationIn"]).optional(),
        }
    ).named(renames["UrlNotificationMetadataIn"])
    types["UrlNotificationMetadataOut"] = t.struct(
        {
            "url": t.string().optional(),
            "latestUpdate": t.proxy(renames["UrlNotificationOut"]).optional(),
            "latestRemove": t.proxy(renames["UrlNotificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlNotificationMetadataOut"])

    functions = {}
    functions["urlNotificationsPublish"] = indexing.get(
        "v3/urlNotifications/metadata",
        t.struct({"url": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UrlNotificationMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlNotificationsGetMetadata"] = indexing.get(
        "v3/urlNotifications/metadata",
        t.struct({"url": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UrlNotificationMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="indexing", renames=renames, types=Box(types), functions=Box(functions)
    )
