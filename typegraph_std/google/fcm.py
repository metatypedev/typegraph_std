from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_fcm() -> Import:
    fcm = HTTPRuntime("https://fcm.googleapis.com/")

    renames = {
        "ErrorResponse": "_fcm_1_ErrorResponse",
        "WebpushFcmOptionsIn": "_fcm_2_WebpushFcmOptionsIn",
        "WebpushFcmOptionsOut": "_fcm_3_WebpushFcmOptionsOut",
        "WebpushConfigIn": "_fcm_4_WebpushConfigIn",
        "WebpushConfigOut": "_fcm_5_WebpushConfigOut",
        "AndroidConfigIn": "_fcm_6_AndroidConfigIn",
        "AndroidConfigOut": "_fcm_7_AndroidConfigOut",
        "FcmOptionsIn": "_fcm_8_FcmOptionsIn",
        "FcmOptionsOut": "_fcm_9_FcmOptionsOut",
        "ApnsConfigIn": "_fcm_10_ApnsConfigIn",
        "ApnsConfigOut": "_fcm_11_ApnsConfigOut",
        "AndroidFcmOptionsIn": "_fcm_12_AndroidFcmOptionsIn",
        "AndroidFcmOptionsOut": "_fcm_13_AndroidFcmOptionsOut",
        "ColorIn": "_fcm_14_ColorIn",
        "ColorOut": "_fcm_15_ColorOut",
        "LightSettingsIn": "_fcm_16_LightSettingsIn",
        "LightSettingsOut": "_fcm_17_LightSettingsOut",
        "SendMessageRequestIn": "_fcm_18_SendMessageRequestIn",
        "SendMessageRequestOut": "_fcm_19_SendMessageRequestOut",
        "AndroidNotificationIn": "_fcm_20_AndroidNotificationIn",
        "AndroidNotificationOut": "_fcm_21_AndroidNotificationOut",
        "ApnsFcmOptionsIn": "_fcm_22_ApnsFcmOptionsIn",
        "ApnsFcmOptionsOut": "_fcm_23_ApnsFcmOptionsOut",
        "MessageIn": "_fcm_24_MessageIn",
        "MessageOut": "_fcm_25_MessageOut",
        "NotificationIn": "_fcm_26_NotificationIn",
        "NotificationOut": "_fcm_27_NotificationOut",
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
    types["WebpushConfigIn"] = t.struct(
        {
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsIn"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WebpushConfigIn"])
    types["WebpushConfigOut"] = t.struct(
        {
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsOut"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpushConfigOut"])
    types["AndroidConfigIn"] = t.struct(
        {
            "restrictedPackageName": t.string().optional(),
            "directBootOk": t.boolean().optional(),
            "priority": t.string().optional(),
            "ttl": t.string().optional(),
            "notification": t.proxy(renames["AndroidNotificationIn"]).optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsIn"]).optional(),
            "collapseKey": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AndroidConfigIn"])
    types["AndroidConfigOut"] = t.struct(
        {
            "restrictedPackageName": t.string().optional(),
            "directBootOk": t.boolean().optional(),
            "priority": t.string().optional(),
            "ttl": t.string().optional(),
            "notification": t.proxy(renames["AndroidNotificationOut"]).optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsOut"]).optional(),
            "collapseKey": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidConfigOut"])
    types["FcmOptionsIn"] = t.struct({"analyticsLabel": t.string().optional()}).named(
        renames["FcmOptionsIn"]
    )
    types["FcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FcmOptionsOut"])
    types["ApnsConfigIn"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsIn"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApnsConfigIn"])
    types["ApnsConfigOut"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsOut"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsConfigOut"])
    types["AndroidFcmOptionsIn"] = t.struct(
        {"analyticsLabel": t.string().optional()}
    ).named(renames["AndroidFcmOptionsIn"])
    types["AndroidFcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidFcmOptionsOut"])
    types["ColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["LightSettingsIn"] = t.struct(
        {
            "lightOnDuration": t.string(),
            "color": t.proxy(renames["ColorIn"]),
            "lightOffDuration": t.string(),
        }
    ).named(renames["LightSettingsIn"])
    types["LightSettingsOut"] = t.struct(
        {
            "lightOnDuration": t.string(),
            "color": t.proxy(renames["ColorOut"]),
            "lightOffDuration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LightSettingsOut"])
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
    types["AndroidNotificationIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "color": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "notificationCount": t.integer().optional(),
            "body": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "bodyLocKey": t.string().optional(),
            "eventTime": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "sticky": t.boolean().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "channelId": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "visibility": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "ticker": t.string().optional(),
            "image": t.string().optional(),
            "lightSettings": t.proxy(renames["LightSettingsIn"]).optional(),
            "proxy": t.string().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "localOnly": t.boolean().optional(),
            "icon": t.string().optional(),
            "clickAction": t.string().optional(),
            "titleLocKey": t.string().optional(),
            "sound": t.string().optional(),
        }
    ).named(renames["AndroidNotificationIn"])
    types["AndroidNotificationOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "color": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "notificationCount": t.integer().optional(),
            "body": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "bodyLocKey": t.string().optional(),
            "eventTime": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "sticky": t.boolean().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "channelId": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "visibility": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "ticker": t.string().optional(),
            "image": t.string().optional(),
            "lightSettings": t.proxy(renames["LightSettingsOut"]).optional(),
            "proxy": t.string().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "localOnly": t.boolean().optional(),
            "icon": t.string().optional(),
            "clickAction": t.string().optional(),
            "titleLocKey": t.string().optional(),
            "sound": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidNotificationOut"])
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
    types["MessageIn"] = t.struct(
        {
            "token": t.string().optional(),
            "android": t.proxy(renames["AndroidConfigIn"]).optional(),
            "name": t.string().optional(),
            "webpush": t.proxy(renames["WebpushConfigIn"]).optional(),
            "condition": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "apns": t.proxy(renames["ApnsConfigIn"]).optional(),
            "notification": t.proxy(renames["NotificationIn"]).optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsIn"]).optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "token": t.string().optional(),
            "android": t.proxy(renames["AndroidConfigOut"]).optional(),
            "name": t.string().optional(),
            "webpush": t.proxy(renames["WebpushConfigOut"]).optional(),
            "condition": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "apns": t.proxy(renames["ApnsConfigOut"]).optional(),
            "notification": t.proxy(renames["NotificationOut"]).optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsOut"]).optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
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

    return Import(importer="fcm", renames=renames, types=types, functions=functions)
