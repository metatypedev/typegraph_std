from typegraph import effects
from typegraph import t
from typegraph.importers.base.importer import Import
from typegraph import TypeGraph
from typegraph.runtimes.http import HTTPRuntime


def import_fcm() -> Import:
    fcm = HTTPRuntime("https://fcm.googleapis.com/")

    renames = {
        "ErrorResponse": "_fcm_1_ErrorResponse",
        "ColorIn": "_fcm_2_ColorIn",
        "ColorOut": "_fcm_3_ColorOut",
        "NotificationIn": "_fcm_4_NotificationIn",
        "NotificationOut": "_fcm_5_NotificationOut",
        "WebpushConfigIn": "_fcm_6_WebpushConfigIn",
        "WebpushConfigOut": "_fcm_7_WebpushConfigOut",
        "ApnsFcmOptionsIn": "_fcm_8_ApnsFcmOptionsIn",
        "ApnsFcmOptionsOut": "_fcm_9_ApnsFcmOptionsOut",
        "ApnsConfigIn": "_fcm_10_ApnsConfigIn",
        "ApnsConfigOut": "_fcm_11_ApnsConfigOut",
        "WebpushFcmOptionsIn": "_fcm_12_WebpushFcmOptionsIn",
        "WebpushFcmOptionsOut": "_fcm_13_WebpushFcmOptionsOut",
        "FcmOptionsIn": "_fcm_14_FcmOptionsIn",
        "FcmOptionsOut": "_fcm_15_FcmOptionsOut",
        "LightSettingsIn": "_fcm_16_LightSettingsIn",
        "LightSettingsOut": "_fcm_17_LightSettingsOut",
        "AndroidConfigIn": "_fcm_18_AndroidConfigIn",
        "AndroidConfigOut": "_fcm_19_AndroidConfigOut",
        "AndroidFcmOptionsIn": "_fcm_20_AndroidFcmOptionsIn",
        "AndroidFcmOptionsOut": "_fcm_21_AndroidFcmOptionsOut",
        "MessageIn": "_fcm_22_MessageIn",
        "MessageOut": "_fcm_23_MessageOut",
        "AndroidNotificationIn": "_fcm_24_AndroidNotificationIn",
        "AndroidNotificationOut": "_fcm_25_AndroidNotificationOut",
        "SendMessageRequestIn": "_fcm_26_SendMessageRequestIn",
        "SendMessageRequestOut": "_fcm_27_SendMessageRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["NotificationIn"] = t.struct(
        {
            "title": t.string().optional(),
            "body": t.string().optional(),
            "image": t.string().optional(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "body": t.string().optional(),
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["WebpushConfigIn"] = t.struct(
        {
            "data": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsIn"]).optional(),
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WebpushConfigIn"])
    types["WebpushConfigOut"] = t.struct(
        {
            "data": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsOut"]).optional(),
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpushConfigOut"])
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
    types["ApnsConfigIn"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsIn"]).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApnsConfigIn"])
    types["ApnsConfigOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsOut"]).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsConfigOut"])
    types["WebpushFcmOptionsIn"] = t.struct(
        {"link": t.string().optional(), "analyticsLabel": t.string().optional()}
    ).named(renames["WebpushFcmOptionsIn"])
    types["WebpushFcmOptionsOut"] = t.struct(
        {
            "link": t.string().optional(),
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpushFcmOptionsOut"])
    types["FcmOptionsIn"] = t.struct({"analyticsLabel": t.string().optional()}).named(
        renames["FcmOptionsIn"]
    )
    types["FcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FcmOptionsOut"])
    types["LightSettingsIn"] = t.struct(
        {
            "color": t.proxy(renames["ColorIn"]),
            "lightOnDuration": t.string(),
            "lightOffDuration": t.string(),
        }
    ).named(renames["LightSettingsIn"])
    types["LightSettingsOut"] = t.struct(
        {
            "color": t.proxy(renames["ColorOut"]),
            "lightOnDuration": t.string(),
            "lightOffDuration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LightSettingsOut"])
    types["AndroidConfigIn"] = t.struct(
        {
            "notification": t.proxy(renames["AndroidNotificationIn"]).optional(),
            "priority": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "collapseKey": t.string().optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsIn"]).optional(),
            "ttl": t.string().optional(),
            "restrictedPackageName": t.string().optional(),
            "directBootOk": t.boolean().optional(),
        }
    ).named(renames["AndroidConfigIn"])
    types["AndroidConfigOut"] = t.struct(
        {
            "notification": t.proxy(renames["AndroidNotificationOut"]).optional(),
            "priority": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "collapseKey": t.string().optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsOut"]).optional(),
            "ttl": t.string().optional(),
            "restrictedPackageName": t.string().optional(),
            "directBootOk": t.boolean().optional(),
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
    types["MessageIn"] = t.struct(
        {
            "apns": t.proxy(renames["ApnsConfigIn"]).optional(),
            "webpush": t.proxy(renames["WebpushConfigIn"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "topic": t.string().optional(),
            "condition": t.string().optional(),
            "name": t.string().optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsIn"]).optional(),
            "android": t.proxy(renames["AndroidConfigIn"]).optional(),
            "token": t.string().optional(),
            "notification": t.proxy(renames["NotificationIn"]).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "apns": t.proxy(renames["ApnsConfigOut"]).optional(),
            "webpush": t.proxy(renames["WebpushConfigOut"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "topic": t.string().optional(),
            "condition": t.string().optional(),
            "name": t.string().optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsOut"]).optional(),
            "android": t.proxy(renames["AndroidConfigOut"]).optional(),
            "token": t.string().optional(),
            "notification": t.proxy(renames["NotificationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["AndroidNotificationIn"] = t.struct(
        {
            "image": t.string().optional(),
            "lightSettings": t.proxy(renames["LightSettingsIn"]).optional(),
            "eventTime": t.string().optional(),
            "visibility": t.string().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "icon": t.string().optional(),
            "ticker": t.string().optional(),
            "sound": t.string().optional(),
            "tag": t.string().optional(),
            "color": t.string().optional(),
            "channelId": t.string().optional(),
            "notificationCount": t.integer().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "proxy": t.string().optional(),
            "body": t.string().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "clickAction": t.string().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "localOnly": t.boolean().optional(),
            "bodyLocKey": t.string().optional(),
            "titleLocKey": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "notificationPriority": t.string().optional(),
            "sticky": t.boolean().optional(),
        }
    ).named(renames["AndroidNotificationIn"])
    types["AndroidNotificationOut"] = t.struct(
        {
            "image": t.string().optional(),
            "lightSettings": t.proxy(renames["LightSettingsOut"]).optional(),
            "eventTime": t.string().optional(),
            "visibility": t.string().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "icon": t.string().optional(),
            "ticker": t.string().optional(),
            "sound": t.string().optional(),
            "tag": t.string().optional(),
            "color": t.string().optional(),
            "channelId": t.string().optional(),
            "notificationCount": t.integer().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "proxy": t.string().optional(),
            "body": t.string().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "clickAction": t.string().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "localOnly": t.boolean().optional(),
            "bodyLocKey": t.string().optional(),
            "titleLocKey": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "notificationPriority": t.string().optional(),
            "sticky": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidNotificationOut"])
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
