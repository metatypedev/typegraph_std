from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_fcm():
    fcm = HTTPRuntime("https://fcm.googleapis.com/")

    renames = {
        "ErrorResponse": "_fcm_1_ErrorResponse",
        "ApnsFcmOptionsIn": "_fcm_2_ApnsFcmOptionsIn",
        "ApnsFcmOptionsOut": "_fcm_3_ApnsFcmOptionsOut",
        "ColorIn": "_fcm_4_ColorIn",
        "ColorOut": "_fcm_5_ColorOut",
        "FcmOptionsIn": "_fcm_6_FcmOptionsIn",
        "FcmOptionsOut": "_fcm_7_FcmOptionsOut",
        "NotificationIn": "_fcm_8_NotificationIn",
        "NotificationOut": "_fcm_9_NotificationOut",
        "LightSettingsIn": "_fcm_10_LightSettingsIn",
        "LightSettingsOut": "_fcm_11_LightSettingsOut",
        "AndroidNotificationIn": "_fcm_12_AndroidNotificationIn",
        "AndroidNotificationOut": "_fcm_13_AndroidNotificationOut",
        "SendMessageRequestIn": "_fcm_14_SendMessageRequestIn",
        "SendMessageRequestOut": "_fcm_15_SendMessageRequestOut",
        "WebpushConfigIn": "_fcm_16_WebpushConfigIn",
        "WebpushConfigOut": "_fcm_17_WebpushConfigOut",
        "AndroidFcmOptionsIn": "_fcm_18_AndroidFcmOptionsIn",
        "AndroidFcmOptionsOut": "_fcm_19_AndroidFcmOptionsOut",
        "MessageIn": "_fcm_20_MessageIn",
        "MessageOut": "_fcm_21_MessageOut",
        "AndroidConfigIn": "_fcm_22_AndroidConfigIn",
        "AndroidConfigOut": "_fcm_23_AndroidConfigOut",
        "WebpushFcmOptionsIn": "_fcm_24_WebpushFcmOptionsIn",
        "WebpushFcmOptionsOut": "_fcm_25_WebpushFcmOptionsOut",
        "ApnsConfigIn": "_fcm_26_ApnsConfigIn",
        "ApnsConfigOut": "_fcm_27_ApnsConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ApnsFcmOptionsIn"] = t.struct(
        {"image": t.string().optional(), "analyticsLabel": t.string().optional()}
    ).named(renames["ApnsFcmOptionsIn"])
    types["ApnsFcmOptionsOut"] = t.struct(
        {
            "image": t.string().optional(),
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApnsFcmOptionsOut"])
    types["ColorIn"] = t.struct(
        {
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["FcmOptionsIn"] = t.struct({"analyticsLabel": t.string().optional()}).named(
        renames["FcmOptionsIn"]
    )
    types["FcmOptionsOut"] = t.struct(
        {
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FcmOptionsOut"])
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
    types["AndroidNotificationIn"] = t.struct(
        {
            "sticky": t.boolean().optional(),
            "bodyLocKey": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "eventTime": t.string().optional(),
            "channelId": t.string().optional(),
            "sound": t.string().optional(),
            "image": t.string().optional(),
            "icon": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "ticker": t.string().optional(),
            "proxy": t.string().optional(),
            "titleLocKey": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "title": t.string().optional(),
            "clickAction": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "notificationCount": t.integer().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "tag": t.string().optional(),
            "visibility": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "body": t.string().optional(),
            "color": t.string().optional(),
            "lightSettings": t.proxy(renames["LightSettingsIn"]).optional(),
            "vibrateTimings": t.array(t.string()).optional(),
        }
    ).named(renames["AndroidNotificationIn"])
    types["AndroidNotificationOut"] = t.struct(
        {
            "sticky": t.boolean().optional(),
            "bodyLocKey": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "eventTime": t.string().optional(),
            "channelId": t.string().optional(),
            "sound": t.string().optional(),
            "image": t.string().optional(),
            "icon": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "ticker": t.string().optional(),
            "proxy": t.string().optional(),
            "titleLocKey": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "title": t.string().optional(),
            "clickAction": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "notificationCount": t.integer().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "tag": t.string().optional(),
            "visibility": t.string().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "body": t.string().optional(),
            "color": t.string().optional(),
            "lightSettings": t.proxy(renames["LightSettingsOut"]).optional(),
            "vibrateTimings": t.array(t.string()).optional(),
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
    types["WebpushConfigIn"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsIn"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WebpushConfigIn"])
    types["WebpushConfigOut"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["WebpushFcmOptionsOut"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.struct({"_": t.string().optional()}).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebpushConfigOut"])
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
            "topic": t.string().optional(),
            "name": t.string().optional(),
            "condition": t.string().optional(),
            "apns": t.proxy(renames["ApnsConfigIn"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.proxy(renames["NotificationIn"]).optional(),
            "webpush": t.proxy(renames["WebpushConfigIn"]).optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsIn"]).optional(),
            "android": t.proxy(renames["AndroidConfigIn"]).optional(),
            "token": t.string().optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "name": t.string().optional(),
            "condition": t.string().optional(),
            "apns": t.proxy(renames["ApnsConfigOut"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.proxy(renames["NotificationOut"]).optional(),
            "webpush": t.proxy(renames["WebpushConfigOut"]).optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsOut"]).optional(),
            "android": t.proxy(renames["AndroidConfigOut"]).optional(),
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["AndroidConfigIn"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsIn"]).optional(),
            "priority": t.string().optional(),
            "ttl": t.string().optional(),
            "collapseKey": t.string().optional(),
            "notification": t.proxy(renames["AndroidNotificationIn"]).optional(),
            "directBootOk": t.boolean().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "restrictedPackageName": t.string().optional(),
        }
    ).named(renames["AndroidConfigIn"])
    types["AndroidConfigOut"] = t.struct(
        {
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsOut"]).optional(),
            "priority": t.string().optional(),
            "ttl": t.string().optional(),
            "collapseKey": t.string().optional(),
            "notification": t.proxy(renames["AndroidNotificationOut"]).optional(),
            "directBootOk": t.boolean().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "restrictedPackageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidConfigOut"])
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
