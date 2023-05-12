from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_fcm() -> Import:
    fcm = HTTPRuntime("https://fcm.googleapis.com/")

    renames = {
        "ErrorResponse": "_fcm_1_ErrorResponse",
        "WebpushFcmOptionsIn": "_fcm_2_WebpushFcmOptionsIn",
        "WebpushFcmOptionsOut": "_fcm_3_WebpushFcmOptionsOut",
        "AndroidNotificationIn": "_fcm_4_AndroidNotificationIn",
        "AndroidNotificationOut": "_fcm_5_AndroidNotificationOut",
        "FcmOptionsIn": "_fcm_6_FcmOptionsIn",
        "FcmOptionsOut": "_fcm_7_FcmOptionsOut",
        "ApnsFcmOptionsIn": "_fcm_8_ApnsFcmOptionsIn",
        "ApnsFcmOptionsOut": "_fcm_9_ApnsFcmOptionsOut",
        "WebpushConfigIn": "_fcm_10_WebpushConfigIn",
        "WebpushConfigOut": "_fcm_11_WebpushConfigOut",
        "ApnsConfigIn": "_fcm_12_ApnsConfigIn",
        "ApnsConfigOut": "_fcm_13_ApnsConfigOut",
        "AndroidConfigIn": "_fcm_14_AndroidConfigIn",
        "AndroidConfigOut": "_fcm_15_AndroidConfigOut",
        "AndroidFcmOptionsIn": "_fcm_16_AndroidFcmOptionsIn",
        "AndroidFcmOptionsOut": "_fcm_17_AndroidFcmOptionsOut",
        "SendMessageRequestIn": "_fcm_18_SendMessageRequestIn",
        "SendMessageRequestOut": "_fcm_19_SendMessageRequestOut",
        "LightSettingsIn": "_fcm_20_LightSettingsIn",
        "LightSettingsOut": "_fcm_21_LightSettingsOut",
        "NotificationIn": "_fcm_22_NotificationIn",
        "NotificationOut": "_fcm_23_NotificationOut",
        "MessageIn": "_fcm_24_MessageIn",
        "MessageOut": "_fcm_25_MessageOut",
        "ColorIn": "_fcm_26_ColorIn",
        "ColorOut": "_fcm_27_ColorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["WebpushFcmOptionsIn"] = t.struct(
        {"analyticsLabel": t.string().optional(), "link": t.string().optional()}
    ).named(renames["WebpushFcmOptionsIn"])
    types["WebpushFcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpushFcmOptionsOut"])
    types["AndroidNotificationIn"] = t.struct(
        {
            "vibrateTimings": t.array(t.string()).optional(),
            "ticker": t.string().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "color": t.string().optional(),
            "visibility": t.string().optional(),
            "sticky": t.boolean().optional(),
            "titleLocKey": t.string().optional(),
            "proxy": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "channelId": t.string().optional(),
            "title": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "lightSettings": t.proxy(renames["LightSettingsIn"]).optional(),
            "clickAction": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "icon": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "bodyLocKey": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "eventTime": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "sound": t.string().optional(),
            "image": t.string().optional(),
            "tag": t.string().optional(),
            "notificationCount": t.integer().optional(),
            "body": t.string().optional(),
        }
    ).named(renames["AndroidNotificationIn"])
    types["AndroidNotificationOut"] = t.struct(
        {
            "vibrateTimings": t.array(t.string()).optional(),
            "ticker": t.string().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "color": t.string().optional(),
            "visibility": t.string().optional(),
            "sticky": t.boolean().optional(),
            "titleLocKey": t.string().optional(),
            "proxy": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "channelId": t.string().optional(),
            "title": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "lightSettings": t.proxy(renames["LightSettingsOut"]).optional(),
            "clickAction": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "icon": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "bodyLocKey": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "eventTime": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "sound": t.string().optional(),
            "image": t.string().optional(),
            "tag": t.string().optional(),
            "notificationCount": t.integer().optional(),
            "body": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidNotificationOut"])
    types["FcmOptionsIn"] = t.struct({"analyticsLabel": t.string().optional()}).named(
        renames["FcmOptionsIn"]
    )
    types["FcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FcmOptionsOut"])
    types["ApnsFcmOptionsIn"] = t.struct(
        {"analyticsLabel": t.string().optional(), "image": t.string().optional()}
    ).named(renames["ApnsFcmOptionsIn"])
    types["ApnsFcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsFcmOptionsOut"])
    types["WebpushConfigIn"] = t.struct(
        {
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsIn"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WebpushConfigIn"])
    types["WebpushConfigOut"] = t.struct(
        {
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsOut"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpushConfigOut"])
    types["ApnsConfigIn"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsIn"]).optional(),
        }
    ).named(renames["ApnsConfigIn"])
    types["ApnsConfigOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsConfigOut"])
    types["AndroidConfigIn"] = t.struct(
        {
            "directBootOk": t.boolean().optional(),
            "restrictedPackageName": t.string().optional(),
            "priority": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.proxy(renames["AndroidNotificationIn"]).optional(),
            "ttl": t.string().optional(),
            "collapseKey": t.string().optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsIn"]).optional(),
        }
    ).named(renames["AndroidConfigIn"])
    types["AndroidConfigOut"] = t.struct(
        {
            "directBootOk": t.boolean().optional(),
            "restrictedPackageName": t.string().optional(),
            "priority": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.proxy(renames["AndroidNotificationOut"]).optional(),
            "ttl": t.string().optional(),
            "collapseKey": t.string().optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidConfigOut"])
    types["AndroidFcmOptionsIn"] = t.struct(
        {"analyticsLabel": t.string().optional()}
    ).named(renames["AndroidFcmOptionsIn"])
    types["AndroidFcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidFcmOptionsOut"])
    types["SendMessageRequestIn"] = t.struct(
        {
            "message": t.proxy(renames["MessageIn"]),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["SendMessageRequestIn"])
    types["SendMessageRequestOut"] = t.struct(
        {
            "message": t.proxy(renames["MessageOut"]),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SendMessageRequestOut"])
    types["LightSettingsIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]),
            "lightOffDuration": t.string(),
            "lightOnDuration": t.string(),
        }
    ).named(renames["LightSettingsIn"])
    types["LightSettingsOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]),
            "lightOffDuration": t.string(),
            "lightOnDuration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LightSettingsOut"])
    types["NotificationIn"] = t.struct(
        {
            "body": t.string().optional(),
            "title": t.string().optional(),
            "image": t.string().optional(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "body": t.string().optional(),
            "title": t.string().optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["MessageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsIn"]).optional(),
            "condition": t.string().optional(),
            "android": t.proxy(renames["AndroidConfigIn"]).optional(),
            "topic": t.string().optional(),
            "token": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "webpush": t.proxy(renames["WebpushConfigIn"]).optional(),
            "apns": t.proxy(renames["ApnsConfigIn"]).optional(),
            "notification": t.proxy(renames["NotificationIn"]).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsOut"]).optional(),
            "condition": t.string().optional(),
            "android": t.proxy(renames["AndroidConfigOut"]).optional(),
            "topic": t.string().optional(),
            "token": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "webpush": t.proxy(renames["WebpushConfigOut"]).optional(),
            "apns": t.proxy(renames["ApnsConfigOut"]).optional(),
            "notification": t.proxy(renames["NotificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["ColorIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])

    functions = {}
    functions["projectsMessagesSend"] = fcm.post(
        "v1/{parent}/messages:send",
        t.struct(
            {
                "parent": t.string(),
                "message": t.proxy(renames["MessageIn"]),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="fcm", renames=renames, types=Box(types), functions=Box(functions)
    )
