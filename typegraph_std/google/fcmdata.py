from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_fcmdata():
    fcmdata = HTTPRuntime("https://fcmdata.googleapis.com/")

    renames = {
        "ErrorResponse": "_fcmdata_1_ErrorResponse",
        "GoogleFirebaseFcmDataV1beta1MessageInsightPercentsIn": "_fcmdata_2_GoogleFirebaseFcmDataV1beta1MessageInsightPercentsIn",
        "GoogleFirebaseFcmDataV1beta1MessageInsightPercentsOut": "_fcmdata_3_GoogleFirebaseFcmDataV1beta1MessageInsightPercentsOut",
        "GoogleTypeDateIn": "_fcmdata_4_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_fcmdata_5_GoogleTypeDateOut",
        "GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsIn": "_fcmdata_6_GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsIn",
        "GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsOut": "_fcmdata_7_GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsOut",
        "GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataIn": "_fcmdata_8_GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataIn",
        "GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataOut": "_fcmdata_9_GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataOut",
        "GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseIn": "_fcmdata_10_GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseIn",
        "GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseOut": "_fcmdata_11_GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseOut",
        "GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsIn": "_fcmdata_12_GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsIn",
        "GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsOut": "_fcmdata_13_GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsOut",
        "GoogleFirebaseFcmDataV1beta1DataIn": "_fcmdata_14_GoogleFirebaseFcmDataV1beta1DataIn",
        "GoogleFirebaseFcmDataV1beta1DataOut": "_fcmdata_15_GoogleFirebaseFcmDataV1beta1DataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleFirebaseFcmDataV1beta1MessageInsightPercentsIn"] = t.struct(
        {"priorityLowered": t.number().optional()}
    ).named(renames["GoogleFirebaseFcmDataV1beta1MessageInsightPercentsIn"])
    types["GoogleFirebaseFcmDataV1beta1MessageInsightPercentsOut"] = t.struct(
        {
            "priorityLowered": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1MessageInsightPercentsOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsIn"] = t.struct(
        {
            "droppedTooManyPendingMessages": t.number().optional(),
            "pending": t.number().optional(),
            "droppedDeviceInactive": t.number().optional(),
            "droppedAppForceStopped": t.number().optional(),
            "delivered": t.number().optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsIn"])
    types["GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsOut"] = t.struct(
        {
            "droppedTooManyPendingMessages": t.number().optional(),
            "pending": t.number().optional(),
            "droppedDeviceInactive": t.number().optional(),
            "droppedAppForceStopped": t.number().optional(),
            "delivered": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsOut"])
    types["GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "data": t.proxy(renames["GoogleFirebaseFcmDataV1beta1DataIn"]).optional(),
            "date": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "analyticsLabel": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataIn"])
    types["GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataOut"] = t.struct(
        {
            "appId": t.string().optional(),
            "data": t.proxy(renames["GoogleFirebaseFcmDataV1beta1DataOut"]).optional(),
            "date": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "analyticsLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataOut"])
    types["GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseIn"] = t.struct(
        {
            "androidDeliveryData": t.array(
                t.proxy(renames["GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseIn"])
    types["GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseOut"] = t.struct(
        {
            "androidDeliveryData": t.array(
                t.proxy(renames["GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseOut"])
    types["GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsIn"] = t.struct(
        {
            "delayedMessageThrottled": t.number().optional(),
            "delayedUserStopped": t.number().optional(),
            "delayedDeviceDoze": t.number().optional(),
            "deliveredNoDelay": t.number().optional(),
            "delayedDeviceOffline": t.number().optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsIn"])
    types["GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsOut"] = t.struct(
        {
            "delayedMessageThrottled": t.number().optional(),
            "delayedUserStopped": t.number().optional(),
            "delayedDeviceDoze": t.number().optional(),
            "deliveredNoDelay": t.number().optional(),
            "delayedDeviceOffline": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsOut"])
    types["GoogleFirebaseFcmDataV1beta1DataIn"] = t.struct(
        {
            "countMessagesAccepted": t.string().optional(),
            "deliveryPerformancePercents": t.proxy(
                renames["GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsIn"]
            ).optional(),
            "messageInsightPercents": t.proxy(
                renames["GoogleFirebaseFcmDataV1beta1MessageInsightPercentsIn"]
            ).optional(),
            "messageOutcomePercents": t.proxy(
                renames["GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1DataIn"])
    types["GoogleFirebaseFcmDataV1beta1DataOut"] = t.struct(
        {
            "countMessagesAccepted": t.string().optional(),
            "deliveryPerformancePercents": t.proxy(
                renames["GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsOut"]
            ).optional(),
            "messageInsightPercents": t.proxy(
                renames["GoogleFirebaseFcmDataV1beta1MessageInsightPercentsOut"]
            ).optional(),
            "messageOutcomePercents": t.proxy(
                renames["GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseFcmDataV1beta1DataOut"])

    functions = {}
    functions["projectsAndroidAppsDeliveryDataList"] = fcmdata.get(
        "v1beta1/{parent}/deliveryData",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="fcmdata", renames=renames, types=Box(types), functions=Box(functions)
    )
