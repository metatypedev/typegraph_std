from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_mybusinessnotifications():
    mybusinessnotifications = HTTPRuntime(
        "https://mybusinessnotifications.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessnotifications_1_ErrorResponse",
        "NotificationSettingIn": "_mybusinessnotifications_2_NotificationSettingIn",
        "NotificationSettingOut": "_mybusinessnotifications_3_NotificationSettingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NotificationSettingIn"] = t.struct(
        {
            "name": t.string(),
            "pubsubTopic": t.string().optional(),
            "notificationTypes": t.array(t.string()).optional(),
        }
    ).named(renames["NotificationSettingIn"])
    types["NotificationSettingOut"] = t.struct(
        {
            "name": t.string(),
            "pubsubTopic": t.string().optional(),
            "notificationTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationSettingOut"])

    functions = {}
    functions["accountsGetNotificationSetting"] = mybusinessnotifications.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "pubsubTopic": t.string().optional(),
                "notificationTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationSettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsUpdateNotificationSetting"] = mybusinessnotifications.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string(),
                "pubsubTopic": t.string().optional(),
                "notificationTypes": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationSettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessnotifications",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
