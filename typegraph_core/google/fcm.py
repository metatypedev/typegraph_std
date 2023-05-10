from typegraph.runtimes.http import HTTPRuntime
from typegraph import TypeGraph
from typegraph import effects
from typegraph import t
from typegraph.importers.base.importer import Import


def import_fcm() -> Import:
    fcm = HTTPRuntime("https://fcm.googleapis.com/")

    renames = {
        "ErrorResponse": "_fcm_1_ErrorResponse",
        "FcmOptionsIn": "_fcm_2_FcmOptionsIn",
        "FcmOptionsOut": "_fcm_3_FcmOptionsOut",
        "SendMessageRequestIn": "_fcm_4_SendMessageRequestIn",
        "SendMessageRequestOut": "_fcm_5_SendMessageRequestOut",
        "NotificationIn": "_fcm_6_NotificationIn",
        "NotificationOut": "_fcm_7_NotificationOut",
        "WebpushConfigIn": "_fcm_8_WebpushConfigIn",
        "WebpushConfigOut": "_fcm_9_WebpushConfigOut",
        "MessageIn": "_fcm_10_MessageIn",
        "MessageOut": "_fcm_11_MessageOut",
        "ApnsConfigIn": "_fcm_12_ApnsConfigIn",
        "ApnsConfigOut": "_fcm_13_ApnsConfigOut",
        "ColorIn": "_fcm_14_ColorIn",
        "ColorOut": "_fcm_15_ColorOut",
        "AndroidConfigIn": "_fcm_16_AndroidConfigIn",
        "AndroidConfigOut": "_fcm_17_AndroidConfigOut",
        "LightSettingsIn": "_fcm_18_LightSettingsIn",
        "LightSettingsOut": "_fcm_19_LightSettingsOut",
        "AndroidNotificationIn": "_fcm_20_AndroidNotificationIn",
        "AndroidNotificationOut": "_fcm_21_AndroidNotificationOut",
        "AndroidFcmOptionsIn": "_fcm_22_AndroidFcmOptionsIn",
        "AndroidFcmOptionsOut": "_fcm_23_AndroidFcmOptionsOut",
        "ApnsFcmOptionsIn": "_fcm_24_ApnsFcmOptionsIn",
        "ApnsFcmOptionsOut": "_fcm_25_ApnsFcmOptionsOut",
        "WebpushFcmOptionsIn": "_fcm_26_WebpushFcmOptionsIn",
        "WebpushFcmOptionsOut": "_fcm_27_WebpushFcmOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FcmOptionsIn"] = t.struct({"analyticsLabel": t.string().optional()}).named(
        renames["FcmOptionsIn"]
    )
    types["FcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FcmOptionsOut"])
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
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsIn"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WebpushConfigIn"])
    types["WebpushConfigOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsOut"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpushConfigOut"])
    types["MessageIn"] = t.struct(
        {
            "notification": t.proxy(renames["NotificationIn"]).optional(),
            "name": t.string().optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsIn"]).optional(),
            "android": t.proxy(renames["AndroidConfigIn"]).optional(),
            "condition": t.string().optional(),
            "token": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "webpush": t.proxy(renames["WebpushConfigIn"]).optional(),
            "apns": t.proxy(renames["ApnsConfigIn"]).optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "notification": t.proxy(renames["NotificationOut"]).optional(),
            "name": t.string().optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsOut"]).optional(),
            "android": t.proxy(renames["AndroidConfigOut"]).optional(),
            "condition": t.string().optional(),
            "token": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "webpush": t.proxy(renames["WebpushConfigOut"]).optional(),
            "apns": t.proxy(renames["ApnsConfigOut"]).optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["ApnsConfigIn"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsIn"]).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApnsConfigIn"])
    types["ApnsConfigOut"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["ApnsFcmOptionsOut"]).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsConfigOut"])
    types["ColorIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["AndroidConfigIn"] = t.struct(
        {
            "ttl": t.string().optional(),
            "directBootOk": t.boolean().optional(),
            "restrictedPackageName": t.string().optional(),
            "priority": t.string().optional(),
            "notification": t.proxy(renames["AndroidNotificationIn"]).optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsIn"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "collapseKey": t.string().optional(),
        }
    ).named(renames["AndroidConfigIn"])
    types["AndroidConfigOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "directBootOk": t.boolean().optional(),
            "restrictedPackageName": t.string().optional(),
            "priority": t.string().optional(),
            "notification": t.proxy(renames["AndroidNotificationOut"]).optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsOut"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "collapseKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidConfigOut"])
    types["LightSettingsIn"] = t.struct(
        {
            "lightOnDuration": t.string(),
            "lightOffDuration": t.string(),
            "color": t.proxy(renames["ColorIn"]),
        }
    ).named(renames["LightSettingsIn"])
    types["LightSettingsOut"] = t.struct(
        {
            "lightOnDuration": t.string(),
            "lightOffDuration": t.string(),
            "color": t.proxy(renames["ColorOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LightSettingsOut"])
    types["AndroidNotificationIn"] = t.struct(
        {
            "proxy": t.string().optional(),
            "color": t.string().optional(),
            "image": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "sticky": t.boolean().optional(),
            "visibility": t.string().optional(),
            "title": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "lightSettings": t.proxy(renames["LightSettingsIn"]).optional(),
            "clickAction": t.string().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "titleLocKey": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "sound": t.string().optional(),
            "notificationCount": t.integer().optional(),
            "eventTime": t.string().optional(),
            "icon": t.string().optional(),
            "body": t.string().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "tag": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "ticker": t.string().optional(),
            "bodyLocKey": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "channelId": t.string().optional(),
        }
    ).named(renames["AndroidNotificationIn"])
    types["AndroidNotificationOut"] = t.struct(
        {
            "proxy": t.string().optional(),
            "color": t.string().optional(),
            "image": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "sticky": t.boolean().optional(),
            "visibility": t.string().optional(),
            "title": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "lightSettings": t.proxy(renames["LightSettingsOut"]).optional(),
            "clickAction": t.string().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "titleLocKey": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "sound": t.string().optional(),
            "notificationCount": t.integer().optional(),
            "eventTime": t.string().optional(),
            "icon": t.string().optional(),
            "body": t.string().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "tag": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "ticker": t.string().optional(),
            "bodyLocKey": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "channelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidNotificationOut"])
    types["AndroidFcmOptionsIn"] = t.struct(
        {"analyticsLabel": t.string().optional()}
    ).named(renames["AndroidFcmOptionsIn"])
    types["AndroidFcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidFcmOptionsOut"])
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
