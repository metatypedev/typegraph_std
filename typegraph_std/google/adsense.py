from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_adsense() -> Import:
    adsense = HTTPRuntime("https://adsense.googleapis.com/")

    renames = {
        "ErrorResponse": "_adsense_1_ErrorResponse",
        "AdUnitAdCodeIn": "_adsense_2_AdUnitAdCodeIn",
        "AdUnitAdCodeOut": "_adsense_3_AdUnitAdCodeOut",
        "HttpBodyIn": "_adsense_4_HttpBodyIn",
        "HttpBodyOut": "_adsense_5_HttpBodyOut",
        "ListCustomChannelsResponseIn": "_adsense_6_ListCustomChannelsResponseIn",
        "ListCustomChannelsResponseOut": "_adsense_7_ListCustomChannelsResponseOut",
        "DateIn": "_adsense_8_DateIn",
        "DateOut": "_adsense_9_DateOut",
        "ListAccountsResponseIn": "_adsense_10_ListAccountsResponseIn",
        "ListAccountsResponseOut": "_adsense_11_ListAccountsResponseOut",
        "CustomChannelIn": "_adsense_12_CustomChannelIn",
        "CustomChannelOut": "_adsense_13_CustomChannelOut",
        "ListPaymentsResponseIn": "_adsense_14_ListPaymentsResponseIn",
        "ListPaymentsResponseOut": "_adsense_15_ListPaymentsResponseOut",
        "AdUnitIn": "_adsense_16_AdUnitIn",
        "AdUnitOut": "_adsense_17_AdUnitOut",
        "SiteIn": "_adsense_18_SiteIn",
        "SiteOut": "_adsense_19_SiteOut",
        "ListAlertsResponseIn": "_adsense_20_ListAlertsResponseIn",
        "ListAlertsResponseOut": "_adsense_21_ListAlertsResponseOut",
        "HeaderIn": "_adsense_22_HeaderIn",
        "HeaderOut": "_adsense_23_HeaderOut",
        "ListAdClientsResponseIn": "_adsense_24_ListAdClientsResponseIn",
        "ListAdClientsResponseOut": "_adsense_25_ListAdClientsResponseOut",
        "RowIn": "_adsense_26_RowIn",
        "RowOut": "_adsense_27_RowOut",
        "PaymentIn": "_adsense_28_PaymentIn",
        "PaymentOut": "_adsense_29_PaymentOut",
        "SavedReportIn": "_adsense_30_SavedReportIn",
        "SavedReportOut": "_adsense_31_SavedReportOut",
        "AlertIn": "_adsense_32_AlertIn",
        "AlertOut": "_adsense_33_AlertOut",
        "AccountIn": "_adsense_34_AccountIn",
        "AccountOut": "_adsense_35_AccountOut",
        "ListSavedReportsResponseIn": "_adsense_36_ListSavedReportsResponseIn",
        "ListSavedReportsResponseOut": "_adsense_37_ListSavedReportsResponseOut",
        "AdClientIn": "_adsense_38_AdClientIn",
        "AdClientOut": "_adsense_39_AdClientOut",
        "ContentAdsSettingsIn": "_adsense_40_ContentAdsSettingsIn",
        "ContentAdsSettingsOut": "_adsense_41_ContentAdsSettingsOut",
        "ListLinkedCustomChannelsResponseIn": "_adsense_42_ListLinkedCustomChannelsResponseIn",
        "ListLinkedCustomChannelsResponseOut": "_adsense_43_ListLinkedCustomChannelsResponseOut",
        "ReportResultIn": "_adsense_44_ReportResultIn",
        "ReportResultOut": "_adsense_45_ReportResultOut",
        "EmptyIn": "_adsense_46_EmptyIn",
        "EmptyOut": "_adsense_47_EmptyOut",
        "TimeZoneIn": "_adsense_48_TimeZoneIn",
        "TimeZoneOut": "_adsense_49_TimeZoneOut",
        "UrlChannelIn": "_adsense_50_UrlChannelIn",
        "UrlChannelOut": "_adsense_51_UrlChannelOut",
        "AdBlockingRecoveryTagIn": "_adsense_52_AdBlockingRecoveryTagIn",
        "AdBlockingRecoveryTagOut": "_adsense_53_AdBlockingRecoveryTagOut",
        "ListChildAccountsResponseIn": "_adsense_54_ListChildAccountsResponseIn",
        "ListChildAccountsResponseOut": "_adsense_55_ListChildAccountsResponseOut",
        "ListUrlChannelsResponseIn": "_adsense_56_ListUrlChannelsResponseIn",
        "ListUrlChannelsResponseOut": "_adsense_57_ListUrlChannelsResponseOut",
        "AdClientAdCodeIn": "_adsense_58_AdClientAdCodeIn",
        "AdClientAdCodeOut": "_adsense_59_AdClientAdCodeOut",
        "ListLinkedAdUnitsResponseIn": "_adsense_60_ListLinkedAdUnitsResponseIn",
        "ListLinkedAdUnitsResponseOut": "_adsense_61_ListLinkedAdUnitsResponseOut",
        "ListAdUnitsResponseIn": "_adsense_62_ListAdUnitsResponseIn",
        "ListAdUnitsResponseOut": "_adsense_63_ListAdUnitsResponseOut",
        "CellIn": "_adsense_64_CellIn",
        "CellOut": "_adsense_65_CellOut",
        "ListSitesResponseIn": "_adsense_66_ListSitesResponseIn",
        "ListSitesResponseOut": "_adsense_67_ListSitesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListCustomChannelsResponseIn"] = t.struct(
        {
            "customChannels": t.array(t.proxy(renames["CustomChannelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCustomChannelsResponseIn"])
    types["ListCustomChannelsResponseOut"] = t.struct(
        {
            "customChannels": t.array(t.proxy(renames["CustomChannelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomChannelsResponseOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ListAccountsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountIn"])).optional(),
        }
    ).named(renames["ListAccountsResponseIn"])
    types["ListAccountsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accounts": t.array(t.proxy(renames["AccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccountsResponseOut"])
    types["CustomChannelIn"] = t.struct(
        {"active": t.boolean().optional(), "displayName": t.string()}
    ).named(renames["CustomChannelIn"])
    types["CustomChannelOut"] = t.struct(
        {
            "reportingDimensionId": t.string().optional(),
            "active": t.boolean().optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomChannelOut"])
    types["ListPaymentsResponseIn"] = t.struct(
        {"payments": t.array(t.proxy(renames["PaymentIn"])).optional()}
    ).named(renames["ListPaymentsResponseIn"])
    types["ListPaymentsResponseOut"] = t.struct(
        {
            "payments": t.array(t.proxy(renames["PaymentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPaymentsResponseOut"])
    types["AdUnitIn"] = t.struct(
        {
            "state": t.string().optional(),
            "contentAdsSettings": t.proxy(renames["ContentAdsSettingsIn"]),
            "displayName": t.string(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "name": t.string().optional(),
            "reportingDimensionId": t.string().optional(),
            "state": t.string().optional(),
            "contentAdsSettings": t.proxy(renames["ContentAdsSettingsOut"]),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
    types["SiteIn"] = t.struct(
        {"autoAdsEnabled": t.boolean().optional(), "domain": t.string().optional()}
    ).named(renames["SiteIn"])
    types["SiteOut"] = t.struct(
        {
            "autoAdsEnabled": t.boolean().optional(),
            "state": t.string().optional(),
            "reportingDimensionId": t.string().optional(),
            "name": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SiteOut"])
    types["ListAlertsResponseIn"] = t.struct(
        {"alerts": t.array(t.proxy(renames["AlertIn"])).optional()}
    ).named(renames["ListAlertsResponseIn"])
    types["ListAlertsResponseOut"] = t.struct(
        {
            "alerts": t.array(t.proxy(renames["AlertOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAlertsResponseOut"])
    types["HeaderIn"] = t.struct(
        {"currencyCode": t.string().optional(), "name": t.string(), "type": t.string()}
    ).named(renames["HeaderIn"])
    types["HeaderOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "name": t.string(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeaderOut"])
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
    types["RowIn"] = t.struct(
        {"cells": t.array(t.proxy(renames["CellIn"])).optional()}
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "cells": t.array(t.proxy(renames["CellOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["PaymentIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PaymentIn"]
    )
    types["PaymentOut"] = t.struct(
        {
            "amount": t.string().optional(),
            "name": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentOut"])
    types["SavedReportIn"] = t.struct({"title": t.string().optional()}).named(
        renames["SavedReportIn"]
    )
    types["SavedReportOut"] = t.struct(
        {
            "title": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedReportOut"])
    types["AlertIn"] = t.struct({"_": t.string().optional()}).named(renames["AlertIn"])
    types["AlertOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlertOut"])
    types["AccountIn"] = t.struct(
        {"timeZone": t.proxy(renames["TimeZoneIn"]).optional()}
    ).named(renames["AccountIn"])
    types["AccountOut"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "state": t.string().optional(),
            "premium": t.boolean().optional(),
            "pendingTasks": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccountOut"])
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
    types["ListLinkedCustomChannelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customChannels": t.array(t.proxy(renames["CustomChannelIn"])).optional(),
        }
    ).named(renames["ListLinkedCustomChannelsResponseIn"])
    types["ListLinkedCustomChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customChannels": t.array(t.proxy(renames["CustomChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLinkedCustomChannelsResponseOut"])
    types["ReportResultIn"] = t.struct(
        {
            "totals": t.proxy(renames["RowIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]),
            "averages": t.proxy(renames["RowIn"]).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "totalMatchedRows": t.string().optional(),
            "startDate": t.proxy(renames["DateIn"]),
            "headers": t.array(t.proxy(renames["HeaderIn"])).optional(),
            "warnings": t.array(t.string()).optional(),
        }
    ).named(renames["ReportResultIn"])
    types["ReportResultOut"] = t.struct(
        {
            "totals": t.proxy(renames["RowOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]),
            "averages": t.proxy(renames["RowOut"]).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "totalMatchedRows": t.string().optional(),
            "startDate": t.proxy(renames["DateOut"]),
            "headers": t.array(t.proxy(renames["HeaderOut"])).optional(),
            "warnings": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportResultOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["UrlChannelIn"] = t.struct({"uriPattern": t.string().optional()}).named(
        renames["UrlChannelIn"]
    )
    types["UrlChannelOut"] = t.struct(
        {
            "uriPattern": t.string().optional(),
            "name": t.string().optional(),
            "reportingDimensionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlChannelOut"])
    types["AdBlockingRecoveryTagIn"] = t.struct(
        {"errorProtectionCode": t.string().optional(), "tag": t.string().optional()}
    ).named(renames["AdBlockingRecoveryTagIn"])
    types["AdBlockingRecoveryTagOut"] = t.struct(
        {
            "errorProtectionCode": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdBlockingRecoveryTagOut"])
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
    types["ListUrlChannelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "urlChannels": t.array(t.proxy(renames["UrlChannelIn"])).optional(),
        }
    ).named(renames["ListUrlChannelsResponseIn"])
    types["ListUrlChannelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "urlChannels": t.array(t.proxy(renames["UrlChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUrlChannelsResponseOut"])
    types["AdClientAdCodeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdClientAdCodeIn"]
    )
    types["AdClientAdCodeOut"] = t.struct(
        {
            "ampHead": t.string().optional(),
            "adCode": t.string().optional(),
            "ampBody": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdClientAdCodeOut"])
    types["ListLinkedAdUnitsResponseIn"] = t.struct(
        {
            "adUnits": t.array(t.proxy(renames["AdUnitIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLinkedAdUnitsResponseIn"])
    types["ListLinkedAdUnitsResponseOut"] = t.struct(
        {
            "adUnits": t.array(t.proxy(renames["AdUnitOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLinkedAdUnitsResponseOut"])
    types["ListAdUnitsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "adUnits": t.array(t.proxy(renames["AdUnitIn"])).optional(),
        }
    ).named(renames["ListAdUnitsResponseIn"])
    types["ListAdUnitsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "adUnits": t.array(t.proxy(renames["AdUnitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAdUnitsResponseOut"])
    types["CellIn"] = t.struct({"value": t.string().optional()}).named(
        renames["CellIn"]
    )
    types["CellOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CellOut"])
    types["ListSitesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sites": t.array(t.proxy(renames["SiteIn"])).optional(),
        }
    ).named(renames["ListSitesResponseIn"])
    types["ListSitesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sites": t.array(t.proxy(renames["SiteOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSitesResponseOut"])

    functions = {}
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
    functions["accountsList"] = adsense.get(
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
    functions["accountsReportsGenerateCsv"] = adsense.get(
        "v2/{name}/saved",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SavedReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGenerate"] = adsense.get(
        "v2/{name}/saved",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SavedReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsGetSaved"] = adsense.get(
        "v2/{name}/saved",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SavedReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsReportsSavedGenerate"] = adsense.get(
        "v2/{name}/saved:generateCsv",
        t.struct(
            {
                "dateRange": t.string().optional(),
                "endDate.month": t.integer().optional(),
                "name": t.string(),
                "currencyCode": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "languageCode": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
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
                "dateRange": t.string().optional(),
                "endDate.month": t.integer().optional(),
                "name": t.string(),
                "currencyCode": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "languageCode": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
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
                "dateRange": t.string().optional(),
                "endDate.month": t.integer().optional(),
                "name": t.string(),
                "currencyCode": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "languageCode": t.string().optional(),
                "reportingTimeZone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsSitesGet"] = adsense.get(
        "v2/{parent}/sites",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsSitesList"] = adsense.get(
        "v2/{parent}/sites",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSitesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAlertsList"] = adsense.get(
        "v2/{parent}/alerts",
        t.struct(
            {
                "parent": t.string(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAlertsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsGetAdcode"] = adsense.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsList"] = adsense.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsGet"] = adsense.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdClientOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsDelete"] = adsense.post(
        "v2/{parent}/customchannels",
        t.struct(
            {
                "parent": t.string(),
                "active": t.boolean().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsList"] = adsense.post(
        "v2/{parent}/customchannels",
        t.struct(
            {
                "parent": t.string(),
                "active": t.boolean().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsListLinkedAdUnits"] = adsense.post(
        "v2/{parent}/customchannels",
        t.struct(
            {
                "parent": t.string(),
                "active": t.boolean().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsGet"] = adsense.post(
        "v2/{parent}/customchannels",
        t.struct(
            {
                "parent": t.string(),
                "active": t.boolean().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsPatch"] = adsense.post(
        "v2/{parent}/customchannels",
        t.struct(
            {
                "parent": t.string(),
                "active": t.boolean().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsCustomchannelsCreate"] = adsense.post(
        "v2/{parent}/customchannels",
        t.struct(
            {
                "parent": t.string(),
                "active": t.boolean().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsListLinkedCustomChannels"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdUnitAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsList"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdUnitAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsCreate"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdUnitAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsGet"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdUnitAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsPatch"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdUnitAdCodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdclientsAdunitsGetAdcode"] = adsense.get(
        "v2/{name}/adcode",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AdUnitAdCodeOut"]),
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

    return Import(
        importer="adsense", renames=renames, types=Box(types), functions=Box(functions)
    )
