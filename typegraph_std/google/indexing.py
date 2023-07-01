from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_indexing():
    indexing = HTTPRuntime("https://indexing.googleapis.com/")

    renames = {
        "ErrorResponse": "_indexing_1_ErrorResponse",
        "PublishUrlNotificationResponseIn": "_indexing_2_PublishUrlNotificationResponseIn",
        "PublishUrlNotificationResponseOut": "_indexing_3_PublishUrlNotificationResponseOut",
        "UrlNotificationIn": "_indexing_4_UrlNotificationIn",
        "UrlNotificationOut": "_indexing_5_UrlNotificationOut",
        "UrlNotificationMetadataIn": "_indexing_6_UrlNotificationMetadataIn",
        "UrlNotificationMetadataOut": "_indexing_7_UrlNotificationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["UrlNotificationIn"] = t.struct(
        {
            "notifyTime": t.string().optional(),
            "type": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["UrlNotificationIn"])
    types["UrlNotificationOut"] = t.struct(
        {
            "notifyTime": t.string().optional(),
            "type": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlNotificationOut"])
    types["UrlNotificationMetadataIn"] = t.struct(
        {
            "latestUpdate": t.proxy(renames["UrlNotificationIn"]).optional(),
            "latestRemove": t.proxy(renames["UrlNotificationIn"]).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["UrlNotificationMetadataIn"])
    types["UrlNotificationMetadataOut"] = t.struct(
        {
            "latestUpdate": t.proxy(renames["UrlNotificationOut"]).optional(),
            "latestRemove": t.proxy(renames["UrlNotificationOut"]).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlNotificationMetadataOut"])

    functions = {}
    functions["urlNotificationsGetMetadata"] = indexing.post(
        "v3/urlNotifications:publish",
        t.struct(
            {
                "notifyTime": t.string().optional(),
                "type": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishUrlNotificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["urlNotificationsPublish"] = indexing.post(
        "v3/urlNotifications:publish",
        t.struct(
            {
                "notifyTime": t.string().optional(),
                "type": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishUrlNotificationResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="indexing", renames=renames, types=Box(types), functions=Box(functions)
    )
