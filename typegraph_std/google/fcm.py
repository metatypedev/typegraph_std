from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_fcm() -> Import:
    fcm = HTTPRuntime("https://fcm.googleapis.com/")

    renames = {
        "ErrorResponse": "_fcm_1_ErrorResponse",
        "ApnsConfigIn": "_fcm_2_ApnsConfigIn",
        "ApnsConfigOut": "_fcm_3_ApnsConfigOut",
        "WebpushConfigIn": "_fcm_4_WebpushConfigIn",
        "WebpushConfigOut": "_fcm_5_WebpushConfigOut",
        "MessageIn": "_fcm_6_MessageIn",
        "MessageOut": "_fcm_7_MessageOut",
        "AndroidConfigIn": "_fcm_8_AndroidConfigIn",
        "AndroidConfigOut": "_fcm_9_AndroidConfigOut",
        "ApnsFcmOptionsIn": "_fcm_10_ApnsFcmOptionsIn",
        "ApnsFcmOptionsOut": "_fcm_11_ApnsFcmOptionsOut",
        "NotificationIn": "_fcm_12_NotificationIn",
        "NotificationOut": "_fcm_13_NotificationOut",
        "AndroidFcmOptionsIn": "_fcm_14_AndroidFcmOptionsIn",
        "AndroidFcmOptionsOut": "_fcm_15_AndroidFcmOptionsOut",
        "ColorIn": "_fcm_16_ColorIn",
        "ColorOut": "_fcm_17_ColorOut",
        "WebpushFcmOptionsIn": "_fcm_18_WebpushFcmOptionsIn",
        "WebpushFcmOptionsOut": "_fcm_19_WebpushFcmOptionsOut",
        "LightSettingsIn": "_fcm_20_LightSettingsIn",
        "LightSettingsOut": "_fcm_21_LightSettingsOut",
        "FcmOptionsIn": "_fcm_22_FcmOptionsIn",
        "FcmOptionsOut": "_fcm_23_FcmOptionsOut",
        "SendMessageRequestIn": "_fcm_24_SendMessageRequestIn",
        "SendMessageRequestOut": "_fcm_25_SendMessageRequestOut",
        "AndroidNotificationIn": "_fcm_26_AndroidNotificationIn",
        "AndroidNotificationOut": "_fcm_27_AndroidNotificationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["MessageIn"] = t.struct(
        {
            "apns": t.proxy(renames["ApnsConfigIn"]).optional(),
            "name": t.string().optional(),
            "token": t.string().optional(),
            "notification": t.proxy(renames["NotificationIn"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "topic": t.string().optional(),
            "condition": t.string().optional(),
            "android": t.proxy(renames["AndroidConfigIn"]).optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsIn"]).optional(),
            "webpush": t.proxy(renames["WebpushConfigIn"]).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "apns": t.proxy(renames["ApnsConfigOut"]).optional(),
            "name": t.string().optional(),
            "token": t.string().optional(),
            "notification": t.proxy(renames["NotificationOut"]).optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "topic": t.string().optional(),
            "condition": t.string().optional(),
            "android": t.proxy(renames["AndroidConfigOut"]).optional(),
            "fcmOptions": t.proxy(renames["FcmOptionsOut"]).optional(),
            "webpush": t.proxy(renames["WebpushConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["AndroidConfigIn"] = t.struct(
        {
            "ttl": t.string().optional(),
            "collapseKey": t.string().optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsIn"]).optional(),
            "restrictedPackageName": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.proxy(renames["AndroidNotificationIn"]).optional(),
            "directBootOk": t.boolean().optional(),
            "priority": t.string().optional(),
        }
    ).named(renames["AndroidConfigIn"])
    types["AndroidConfigOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "collapseKey": t.string().optional(),
            "fcmOptions": t.proxy(renames["AndroidFcmOptionsOut"]).optional(),
            "restrictedPackageName": t.string().optional(),
            "data": t.struct({"_": t.string().optional()}).optional(),
            "notification": t.proxy(renames["AndroidNotificationOut"]).optional(),
            "directBootOk": t.boolean().optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidConfigOut"])
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
    types["NotificationIn"] = t.struct(
        {
            "title": t.string().optional(),
            "image": t.string().optional(),
            "body": t.string().optional(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "image": t.string().optional(),
            "body": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
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
            "red": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "red": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
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
    types["LightSettingsIn"] = t.struct(
        {
            "lightOffDuration": t.string(),
            "color": t.proxy(renames["ColorIn"]),
            "lightOnDuration": t.string(),
        }
    ).named(renames["LightSettingsIn"])
    types["LightSettingsOut"] = t.struct(
        {
            "lightOffDuration": t.string(),
            "color": t.proxy(renames["ColorOut"]),
            "lightOnDuration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LightSettingsOut"])
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
    types["AndroidNotificationIn"] = t.struct(
        {
            "titleLocKey": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "eventTime": t.string().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "clickAction": t.string().optional(),
            "tag": t.string().optional(),
            "image": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "color": t.string().optional(),
            "visibility": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "channelId": t.string().optional(),
            "body": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "proxy": t.string().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "sound": t.string().optional(),
            "bodyLocKey": t.string().optional(),
            "ticker": t.string().optional(),
            "icon": t.string().optional(),
            "sticky": t.boolean().optional(),
            "notificationCount": t.integer().optional(),
            "lightSettings": t.proxy(renames["LightSettingsIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["AndroidNotificationIn"])
    types["AndroidNotificationOut"] = t.struct(
        {
            "titleLocKey": t.string().optional(),
            "notificationPriority": t.string().optional(),
            "bypassProxyNotification": t.boolean().optional(),
            "eventTime": t.string().optional(),
            "defaultVibrateTimings": t.boolean().optional(),
            "bodyLocArgs": t.array(t.string()).optional(),
            "clickAction": t.string().optional(),
            "tag": t.string().optional(),
            "image": t.string().optional(),
            "localOnly": t.boolean().optional(),
            "color": t.string().optional(),
            "visibility": t.string().optional(),
            "defaultSound": t.boolean().optional(),
            "defaultLightSettings": t.boolean().optional(),
            "channelId": t.string().optional(),
            "body": t.string().optional(),
            "titleLocArgs": t.array(t.string()).optional(),
            "proxy": t.string().optional(),
            "vibrateTimings": t.array(t.string()).optional(),
            "sound": t.string().optional(),
            "bodyLocKey": t.string().optional(),
            "ticker": t.string().optional(),
            "icon": t.string().optional(),
            "sticky": t.boolean().optional(),
            "notificationCount": t.integer().optional(),
            "lightSettings": t.proxy(renames["LightSettingsOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidNotificationOut"])

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
