from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinessnotifications() -> Import:
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
            "notificationTypes": t.array(t.string()).optional(),
            "pubsubTopic": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["NotificationSettingIn"])
    types["NotificationSettingOut"] = t.struct(
        {
            "notificationTypes": t.array(t.string()).optional(),
            "pubsubTopic": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationSettingOut"])

    functions = {}
    functions["accountsGetNotificationSetting"] = mybusinessnotifications.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "notificationTypes": t.array(t.string()).optional(),
                "pubsubTopic": t.string().optional(),
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
                "name": t.string(),
                "updateMask": t.string(),
                "notificationTypes": t.array(t.string()).optional(),
                "pubsubTopic": t.string().optional(),
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
