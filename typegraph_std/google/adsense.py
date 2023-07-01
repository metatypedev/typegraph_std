from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_adsense():
    adsense = HTTPRuntime("https://adsense.googleapis.com/")

    renames = {
        "ErrorResponse": "_adsense_1_ErrorResponse",
        "ListAlertsResponseIn": "_adsense_2_ListAlertsResponseIn",
        "ListAlertsResponseOut": "_adsense_3_ListAlertsResponseOut",
        "CustomChannelIn": "_adsense_4_CustomChannelIn",
        "CustomChannelOut": "_adsense_5_CustomChannelOut",
        "ListCustomChannelsResponseIn": "_adsense_6_ListCustomChannelsResponseIn",
        "ListCustomChannelsResponseOut": "_adsense_7_ListCustomChannelsResponseOut",
        "ReportResultIn": "_adsense_8_ReportResultIn",
        "ReportResultOut": "_adsense_9_ReportResultOut",
        "PaymentIn": "_adsense_10_PaymentIn",
        "PaymentOut": "_adsense_11_PaymentOut",
        "ListLinkedAdUnitsResponseIn": "_adsense_12_ListLinkedAdUnitsResponseIn",
        "ListLinkedAdUnitsResponseOut": "_adsense_13_ListLinkedAdUnitsResponseOut",
        "ListChildAccountsResponseIn": "_adsense_14_ListChildAccountsResponseIn",
        "ListChildAccountsResponseOut": "_adsense_15_ListChildAccountsResponseOut",
        "ListAdClientsResponseIn": "_adsense_16_ListAdClientsResponseIn",
        "ListAdClientsResponseOut": "_adsense_17_ListAdClientsResponseOut",
        "SiteIn": "_adsense_18_SiteIn",
        "SiteOut": "_adsense_19_SiteOut",
        "ListPaymentsResponseIn": "_adsense_20_ListPaymentsResponseIn",
        "ListPaymentsResponseOut": "_adsense_21_ListPaymentsResponseOut",
        "AlertIn": "_adsense_22_AlertIn",
        "AlertOut": "_adsense_23_AlertOut",
        "ListUrlChannelsResponseIn": "_adsense_24_ListUrlChannelsResponseIn",
        "ListUrlChannelsResponseOut": "_adsense_25_ListUrlChannelsResponseOut",
        "ListAccountsResponseIn": "_adsense_26_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_adsense_27_ListAccountsResponseOut",
        "TimeZoneIn": "_adsense_28_TimeZoneIn",
        "TimeZoneOut": "_adsense_29_TimeZoneOut",
        "DateIn": "_adsense_30_DateIn",
        "DateOut": "_adsense_31_DateOut",
        "UrlChannelIn": "_adsense_32_UrlChannelIn",
        "UrlChannelOut": "_adsense_33_UrlChannelOut",
        "AccountIn": "_adsense_34_AccountIn",
        "AccountOut": "_adsense_35_AccountOut",
        "AdUnitAdCodeIn": "_adsense_36_AdUnitAdCodeIn",
        "AdUnitAdCodeOut": "_adsense_37_AdUnitAdCodeOut",
        "HttpBodyIn": "_adsense_38_HttpBodyIn",
        "HttpBodyOut": "_adsense_39_HttpBodyOut",
        "HeaderIn": "_adsense_40_HeaderIn",
        "HeaderOut": "_adsense_41_HeaderOut",
        "SavedReportIn": "_adsense_42_SavedReportIn",
        "SavedReportOut": "_adsense_43_SavedReportOut",
        "CellIn": "_adsense_44_CellIn",
        "CellOut": "_adsense_45_CellOut",
        "ListAdUnitsResponseIn": "_adsense_46_ListAdUnitsResponseIn",
        "ListAdUnitsResponseOut": "_adsense_47_ListAdUnitsResponseOut",
        "ListLinkedCustomChannelsResponseIn": "_adsense_48_ListLinkedCustomChannelsResponseIn",
        "ListLinkedCustomChannelsResponseOut": "_adsense_49_ListLinkedCustomChannelsResponseOut",
        "AdBlockingRecoveryTagIn": "_adsense_50_AdBlockingRecoveryTagIn",
        "AdBlockingRecoveryTagOut": "_adsense_51_AdBlockingRecoveryTagOut",
        "AdClientAdCodeIn": "_adsense_52_AdClientAdCodeIn",
        "AdClientAdCodeOut": "_adsense_53_AdClientAdCodeOut",
        "AdUnitIn": "_adsense_54_AdUnitIn",
        "AdUnitOut": "_adsense_55_AdUnitOut",
        "EmptyIn": "_adsense_56_EmptyIn",
        "EmptyOut": "_adsense_57_EmptyOut",
        "ListSitesResponseIn": "_adsense_58_ListSitesResponseIn",
        "ListSitesResponseOut": "_adsense_59_ListSitesResponseOut",
        "ListSavedReportsResponseIn": "_adsense_60_ListSavedReportsResponseIn",
        "ListSavedReportsResponseOut": "_adsense_61_ListSavedReportsResponseOut",
        "RowIn": "_adsense_62_RowIn",
        "RowOut": "_adsense_63_RowOut",
        "ContentAdsSettingsIn": "_adsense_64_ContentAdsSettingsIn",
        "ContentAdsSettingsOut": "_adsense_65_ContentAdsSettingsOut",
        "AdClientIn": "_adsense_66_AdClientIn",
        "AdClientOut": "_adsense_67_AdClientOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListAlertsResponseIn"] = t.struct(
        {"alerts": t.array(t.proxy(renames["AlertIn"])).optional()}
    ).named(renames["ListAlertsResponseIn"])
    types["ListAlertsResponseOut"] = t.struct(
        {
            "alerts": t.array(t.proxy(renames["AlertOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertsResponseOut"])
    types["CustomChannelIn"] = t.struct(
        {"displayName": t.string(), "active": t.boolean().optional()}
    ).named(renames["CustomChannelIn"])
    types["CustomChannelOut"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string().optional(),
            "reportingDimensionId": t.string().optional(),
            "active": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelOut"])
    types["ListCustomChannelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customChannels": t.array(t.proxy(renames["CustomChannelIn"])).optional(),
        }
    ).named(renames["ListCustomChannelsResponseIn"])
    types["ListCustomChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customChannels": t.array(t.proxy(renames["CustomChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomChannelsResponseOut"])
    types["ReportResultIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]),
            "headers": t.array(t.proxy(renames["HeaderIn"])).optional(),
            "averages": t.proxy(renames["RowIn"]).optional(),
            "totals": t.proxy(renames["RowIn"]).optional(),
            "totalMatchedRows": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "endDate": t.proxy(renames["DateIn"]),
            "warnings": t.array(t.string()).optional(),
        }
    ).named(renames["ReportResultIn"])
    types["ReportResultOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]),
            "headers": t.array(t.proxy(renames["HeaderOut"])).optional(),
            "averages": t.proxy(renames["RowOut"]).optional(),
            "totals": t.proxy(renames["RowOut"]).optional(),
            "totalMatchedRows": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "endDate": t.proxy(renames["DateOut"]),
            "warnings": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportResultOut"])
    types["PaymentIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PaymentIn"]
    )
    types["PaymentOut"] = t.struct(
        {
            "amount": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentOut"])
    types["ListLinkedAdUnitsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "adUnits": t.array(t.proxy(renames["AdUnitIn"])).optional(),
        }
    ).named(renames["ListLinkedAdUnitsResponseIn"])
    types["ListLinkedAdUnitsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "adUnits": t.array(t.proxy(renames["AdUnitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLinkedAdUnitsResponseOut"])
    types["ListChildAccountsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountIn"])).optional(),
        }
    ).named(renames["ListChildAccountsResponseIn"])
    types["ListChildAccountsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListChildAccountsResponseOut"])
    types["ListAdClientsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "adClients": t.array(t.proxy(renames["AdClientIn"])).optional(),
        }
    ).named(renames["ListAdClientsResponseIn"])
    types["ListAdClientsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "adClients": t.array(t.proxy(renames["AdClientOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAdClientsResponseOut"])
    types["SiteIn"] = t.struct(
        {"domain": t.string().optional(), "autoAdsEnabled": t.boolean().optional()}
    ).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "state": t.string().optional(),
            "reportingDimensionId": t.string().optional(),
            "name": t.string().optional(),
            "autoAdsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
    types["ListPaymentsResponseIn"] = t.struct(
        {"payments": t.array(t.proxy(renames["PaymentIn"])).optional()}
    ).named(renames["ListPaymentsResponseIn"])
    types["ListPaymentsResponseOut"] = t.struct(
        {
            "payments": t.array(t.proxy(renames["PaymentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPaymentsResponseOut"])
    types["AlertIn"] = t.struct({"_": t.string().optional()}).named(renames["AlertIn"])
    types["AlertOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertOut"])
    types["ListUrlChannelsResponseIn"] = t.struct(
        {
            "urlChannels": t.array(t.proxy(renames["UrlChannelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUrlChannelsResponseIn"])
    types["ListUrlChannelsResponseOut"] = t.struct(
        {
            "urlChannels": t.array(t.proxy(renames["UrlChannelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUrlChannelsResponseOut"])
    types["ListAccountsResponseIn"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["AccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAccountsResponseIn"])
    types["ListAccountsResponseOut"] = t.struct(
        {
            "accounts": t.array(t.proxy(renames["AccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountsResponseOut"])
    types["TimeZoneIn"] = t.struct(
        {"version": t.string().optional(), "id": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "version": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["UrlChannelIn"] = t.struct({"uriPattern": t.string().optional()}).named(
        renames["UrlChannelIn"]
    )
    types["UrlChannelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "reportingDimensionId": t.string().optional(),
            "uriPattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelOut"])
    types["AccountIn"] = t.struct(
        {"timeZone": t.proxy(renames["TimeZoneIn"]).optional()}
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "pendingTasks": t.array(t.string()).optional(),
            "premium": t.boolean().optional(),
            "state": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
    types["AdUnitAdCodeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdUnitAdCodeIn"]
    )
    types["AdUnitAdCodeOut"] = t.struct(
        {
            "adCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitAdCodeOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["HeaderIn"] = t.struct(
        {"name": t.string(), "currencyCode": t.string().optional(), "type": t.string()}
    ).named(renames["HeaderIn"])
    types["HeaderOut"] = t.struct(
        {
            "name": t.string(),
            "currencyCode": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeaderOut"])
    types["SavedReportIn"] = t.struct({"title": t.string().optional()}).named(
        renames["SavedReportIn"]
    )
    types["SavedReportOut"] = t.struct(
        {
            "name": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedReportOut"])
    types["CellIn"] = t.struct({"value": t.string().optional()}).named(
        renames["CellIn"]
    )
    types["CellOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellOut"])
    types["ListAdUnitsResponseIn"] = t.struct(
        {
            "adUnits": t.array(t.proxy(renames["AdUnitIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAdUnitsResponseIn"])
    types["ListAdUnitsResponseOut"] = t.struct(
        {
            "adUnits": t.array(t.proxy(renames["AdUnitOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAdUnitsResponseOut"])
    types["ListLinkedCustomChannelsResponseIn"] = t.struct(
        {
            "customChannels": t.array(t.proxy(renames["CustomChannelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLinkedCustomChannelsResponseIn"])
    types["ListLinkedCustomChannelsResponseOut"] = t.struct(
        {
            "customChannels": t.array(t.proxy(renames["CustomChannelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLinkedCustomChannelsResponseOut"])
    types["AdBlockingRecoveryTagIn"] = t.struct(
        {"tag": t.string().optional(), "errorProtectionCode": t.string().optional()}
    ).named(renames["AdBlockingRecoveryTagIn"])
    types["AdBlockingRecoveryTagOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "errorProtectionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBlockingRecoveryTagOut"])
    types["AdClientAdCodeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdClientAdCodeIn"]
    )
    types["AdClientAdCodeOut"] = t.struct(
        {
            "adCode": t.string().optional(),
            "ampBody": t.string().optional(),
            "ampHead": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientAdCodeOut"])
    types["AdUnitIn"] = t.struct(
        {
            "state": t.string(),
            "displayName": t.string(),
            "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "state": t.string(),
            "reportingDimensionId": t.string().optional(),
            "displayName": t.string(),
            "contentAdsSettings": t.proxy(renames["ContentAdsSettingsOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListSitesResponseIn"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSitesResponseIn"])
    types["ListSitesResponseOut"] = t.struct(
        {
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSitesResponseOut"])
    types["ListSavedReportsResponseIn"] = t.struct(
        {
            "savedReports": t.array(t.proxy(renames["SavedReportIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSavedReportsResponseIn"])
    types["ListSavedReportsResponseOut"] = t.struct(
        {
            "savedReports": t.array(t.proxy(renames["SavedReportOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSavedReportsResponseOut"])
    types["RowIn"] = t.struct(
        {"cells": t.array(t.proxy(renames["CellIn"])).optional()}
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "cells": t.array(t.proxy(renames["CellOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["ContentAdsSettingsIn"] = t.struct(
        {"type": t.string(), "size": t.string()}
    ).named(renames["ContentAdsSettingsIn"])
    types["ContentAdsSettingsOut"] = t.struct(
        {
            "type": t.string(),
            "size": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentAdsSettingsOut"])
    types["AdClientIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdClientIn"]
    )
    types["AdClientOut"] = t.struct(
        {
            "state": t.string().optional(),
            "productCode": t.string().optional(),
            "reportingDimensionId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientOut"])

    functions = {}
    functions["accountsList"] = adsense.get(
        "v2/{name}/adBlockingRecoveryTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdBlockingRecoveryTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsListChildAccounts"] = adsense.get(
        "v2/{name}/adBlockingRecoveryTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdBlockingRecoveryTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGet"] = adsense.get(
        "v2/{name}/adBlockingRecoveryTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdBlockingRecoveryTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsGetAdBlockingRecoveryTag"] = adsense.get(
        "v2/{name}/adBlockingRecoveryTag",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdBlockingRecoveryTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsPaymentsList"] = adsense.get(
        "v2/{parent}/payments",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListPaymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsGet"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsList"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsGetAdcode"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsGet"] = adsense.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "displayName": t.string(),
                "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsGetAdcode"] = adsense.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "displayName": t.string(),
                "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsList"] = adsense.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "displayName": t.string(),
                "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsListLinkedCustomChannels"] = adsense.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "displayName": t.string(),
                "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsCreate"] = adsense.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "displayName": t.string(),
                "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsPatch"] = adsense.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "displayName": t.string(),
                "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AdUnitOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsCreate"] = adsense.get(
        "v2/{parent}:listLinkedAdUnits",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinkedAdUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsDelete"] = adsense.get(
        "v2/{parent}:listLinkedAdUnits",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinkedAdUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsPatch"] = adsense.get(
        "v2/{parent}:listLinkedAdUnits",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinkedAdUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsList"] = adsense.get(
        "v2/{parent}:listLinkedAdUnits",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinkedAdUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsGet"] = adsense.get(
        "v2/{parent}:listLinkedAdUnits",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinkedAdUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsListLinkedAdUnits"] = adsense.get(
        "v2/{parent}:listLinkedAdUnits",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLinkedAdUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsUrlchannelsList"] = adsense.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UrlChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsUrlchannelsGet"] = adsense.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UrlChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAlertsList"] = adsense.get(
        "v2/{parent}/alerts",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGetSaved"] = adsense.get(
        "v2/{account}/reports:generateCsv",
        t.struct(
            {
                "endDate.year": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "orderBy": t.string().optional(),
                "startDate.day": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "limit": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
                "languageCode": t.string().optional(),
                "endDate.day": t.integer().optional(),
                "metrics": t.string(),
                "dateRange": t.string().optional(),
                "dimensions": t.string().optional(),
                "account": t.string(),
                "filters": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGenerate"] = adsense.get(
        "v2/{account}/reports:generateCsv",
        t.struct(
            {
                "endDate.year": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "orderBy": t.string().optional(),
                "startDate.day": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "limit": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
                "languageCode": t.string().optional(),
                "endDate.day": t.integer().optional(),
                "metrics": t.string(),
                "dateRange": t.string().optional(),
                "dimensions": t.string().optional(),
                "account": t.string(),
                "filters": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGenerateCsv"] = adsense.get(
        "v2/{account}/reports:generateCsv",
        t.struct(
            {
                "endDate.year": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "orderBy": t.string().optional(),
                "startDate.day": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "limit": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
                "languageCode": t.string().optional(),
                "endDate.day": t.integer().optional(),
                "metrics": t.string(),
                "dateRange": t.string().optional(),
                "dimensions": t.string().optional(),
                "account": t.string(),
                "filters": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsSavedGenerate"] = adsense.get(
        "v2/{name}/saved:generateCsv",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "dateRange": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
                "name": t.string(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "startDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsSavedList"] = adsense.get(
        "v2/{name}/saved:generateCsv",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "dateRange": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
                "name": t.string(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "startDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsSavedGenerateCsv"] = adsense.get(
        "v2/{name}/saved:generateCsv",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "dateRange": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
                "name": t.string(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "startDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsSitesList"] = adsense.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsSitesGet"] = adsense.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SiteOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="adsense", renames=renames, types=Box(types), functions=Box(functions)
    )
