from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_admob() -> Import:
    admob = HTTPRuntime("https://admob.googleapis.com/")

    renames = {
        "ErrorResponse": "_admob_1_ErrorResponse",
        "AppManualAppInfoIn": "_admob_2_AppManualAppInfoIn",
        "AppManualAppInfoOut": "_admob_3_AppManualAppInfoOut",
        "GenerateMediationReportResponseIn": "_admob_4_GenerateMediationReportResponseIn",
        "GenerateMediationReportResponseOut": "_admob_5_GenerateMediationReportResponseOut",
        "PublisherAccountIn": "_admob_6_PublisherAccountIn",
        "PublisherAccountOut": "_admob_7_PublisherAccountOut",
        "DateRangeIn": "_admob_8_DateRangeIn",
        "DateRangeOut": "_admob_9_DateRangeOut",
        "ListPublisherAccountsResponseIn": "_admob_10_ListPublisherAccountsResponseIn",
        "ListPublisherAccountsResponseOut": "_admob_11_ListPublisherAccountsResponseOut",
        "AppIn": "_admob_12_AppIn",
        "AppOut": "_admob_13_AppOut",
        "ReportRowDimensionValueIn": "_admob_14_ReportRowDimensionValueIn",
        "ReportRowDimensionValueOut": "_admob_15_ReportRowDimensionValueOut",
        "ListAdUnitsResponseIn": "_admob_16_ListAdUnitsResponseIn",
        "ListAdUnitsResponseOut": "_admob_17_ListAdUnitsResponseOut",
        "ReportRowIn": "_admob_18_ReportRowIn",
        "ReportRowOut": "_admob_19_ReportRowOut",
        "DateIn": "_admob_20_DateIn",
        "DateOut": "_admob_21_DateOut",
        "NetworkReportSpecSortConditionIn": "_admob_22_NetworkReportSpecSortConditionIn",
        "NetworkReportSpecSortConditionOut": "_admob_23_NetworkReportSpecSortConditionOut",
        "NetworkReportSpecDimensionFilterIn": "_admob_24_NetworkReportSpecDimensionFilterIn",
        "NetworkReportSpecDimensionFilterOut": "_admob_25_NetworkReportSpecDimensionFilterOut",
        "AppLinkedAppInfoIn": "_admob_26_AppLinkedAppInfoIn",
        "AppLinkedAppInfoOut": "_admob_27_AppLinkedAppInfoOut",
        "GenerateNetworkReportRequestIn": "_admob_28_GenerateNetworkReportRequestIn",
        "GenerateNetworkReportRequestOut": "_admob_29_GenerateNetworkReportRequestOut",
        "NetworkReportSpecIn": "_admob_30_NetworkReportSpecIn",
        "NetworkReportSpecOut": "_admob_31_NetworkReportSpecOut",
        "MediationReportSpecIn": "_admob_32_MediationReportSpecIn",
        "MediationReportSpecOut": "_admob_33_MediationReportSpecOut",
        "LocalizationSettingsIn": "_admob_34_LocalizationSettingsIn",
        "LocalizationSettingsOut": "_admob_35_LocalizationSettingsOut",
        "AdUnitIn": "_admob_36_AdUnitIn",
        "AdUnitOut": "_admob_37_AdUnitOut",
        "GenerateMediationReportRequestIn": "_admob_38_GenerateMediationReportRequestIn",
        "GenerateMediationReportRequestOut": "_admob_39_GenerateMediationReportRequestOut",
        "MediationReportSpecDimensionFilterIn": "_admob_40_MediationReportSpecDimensionFilterIn",
        "MediationReportSpecDimensionFilterOut": "_admob_41_MediationReportSpecDimensionFilterOut",
        "ReportHeaderIn": "_admob_42_ReportHeaderIn",
        "ReportHeaderOut": "_admob_43_ReportHeaderOut",
        "ReportRowMetricValueIn": "_admob_44_ReportRowMetricValueIn",
        "ReportRowMetricValueOut": "_admob_45_ReportRowMetricValueOut",
        "MediationReportSpecSortConditionIn": "_admob_46_MediationReportSpecSortConditionIn",
        "MediationReportSpecSortConditionOut": "_admob_47_MediationReportSpecSortConditionOut",
        "ReportFooterIn": "_admob_48_ReportFooterIn",
        "ReportFooterOut": "_admob_49_ReportFooterOut",
        "GenerateNetworkReportResponseIn": "_admob_50_GenerateNetworkReportResponseIn",
        "GenerateNetworkReportResponseOut": "_admob_51_GenerateNetworkReportResponseOut",
        "ListAppsResponseIn": "_admob_52_ListAppsResponseIn",
        "ListAppsResponseOut": "_admob_53_ListAppsResponseOut",
        "StringListIn": "_admob_54_StringListIn",
        "StringListOut": "_admob_55_StringListOut",
        "ReportWarningIn": "_admob_56_ReportWarningIn",
        "ReportWarningOut": "_admob_57_ReportWarningOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AppManualAppInfoIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["AppManualAppInfoIn"])
    types["AppManualAppInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppManualAppInfoOut"])
    types["GenerateMediationReportResponseIn"] = t.struct(
        {
            "row": t.proxy(renames["ReportRowIn"]).optional(),
            "footer": t.proxy(renames["ReportFooterIn"]).optional(),
            "header": t.proxy(renames["ReportHeaderIn"]).optional(),
        }
    ).named(renames["GenerateMediationReportResponseIn"])
    types["GenerateMediationReportResponseOut"] = t.struct(
        {
            "row": t.proxy(renames["ReportRowOut"]).optional(),
            "footer": t.proxy(renames["ReportFooterOut"]).optional(),
            "header": t.proxy(renames["ReportHeaderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateMediationReportResponseOut"])
    types["PublisherAccountIn"] = t.struct(
        {
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
            "publisherId": t.string().optional(),
            "reportingTimeZone": t.string().optional(),
        }
    ).named(renames["PublisherAccountIn"])
    types["PublisherAccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
            "publisherId": t.string().optional(),
            "reportingTimeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherAccountOut"])
    types["DateRangeIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["ListPublisherAccountsResponseIn"] = t.struct(
        {
            "account": t.array(t.proxy(renames["PublisherAccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPublisherAccountsResponseIn"])
    types["ListPublisherAccountsResponseOut"] = t.struct(
        {
            "account": t.array(t.proxy(renames["PublisherAccountOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPublisherAccountsResponseOut"])
    types["AppIn"] = t.struct(
        {
            "manualAppInfo": t.proxy(renames["AppManualAppInfoIn"]).optional(),
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "platform": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoIn"]).optional(),
        }
    ).named(renames["AppIn"])
    types["AppOut"] = t.struct(
        {
            "appApprovalState": t.string().optional(),
            "manualAppInfo": t.proxy(renames["AppManualAppInfoOut"]).optional(),
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "platform": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppOut"])
    types["ReportRowDimensionValueIn"] = t.struct(
        {"displayLabel": t.string().optional(), "value": t.string().optional()}
    ).named(renames["ReportRowDimensionValueIn"])
    types["ReportRowDimensionValueOut"] = t.struct(
        {
            "displayLabel": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowDimensionValueOut"])
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
    types["ReportRowIn"] = t.struct(
        {
            "metricValues": t.struct({"_": t.string().optional()}).optional(),
            "dimensionValues": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ReportRowIn"])
    types["ReportRowOut"] = t.struct(
        {
            "metricValues": t.struct({"_": t.string().optional()}).optional(),
            "dimensionValues": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["NetworkReportSpecSortConditionIn"] = t.struct(
        {
            "order": t.string().optional(),
            "metric": t.string().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionIn"])
    types["NetworkReportSpecSortConditionOut"] = t.struct(
        {
            "order": t.string().optional(),
            "metric": t.string().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionOut"])
    types["NetworkReportSpecDimensionFilterIn"] = t.struct(
        {
            "matchesAny": t.proxy(renames["StringListIn"]).optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["NetworkReportSpecDimensionFilterIn"])
    types["NetworkReportSpecDimensionFilterOut"] = t.struct(
        {
            "matchesAny": t.proxy(renames["StringListOut"]).optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecDimensionFilterOut"])
    types["AppLinkedAppInfoIn"] = t.struct({"appStoreId": t.string().optional()}).named(
        renames["AppLinkedAppInfoIn"]
    )
    types["AppLinkedAppInfoOut"] = t.struct(
        {
            "appStoreId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppLinkedAppInfoOut"])
    types["GenerateNetworkReportRequestIn"] = t.struct(
        {"reportSpec": t.proxy(renames["NetworkReportSpecIn"]).optional()}
    ).named(renames["GenerateNetworkReportRequestIn"])
    types["GenerateNetworkReportRequestOut"] = t.struct(
        {
            "reportSpec": t.proxy(renames["NetworkReportSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateNetworkReportRequestOut"])
    types["NetworkReportSpecIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionIn"])
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterIn"])
            ).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "timeZone": t.string().optional(),
        }
    ).named(renames["NetworkReportSpecIn"])
    types["NetworkReportSpecOut"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionOut"])
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterOut"])
            ).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecOut"])
    types["MediationReportSpecIn"] = t.struct(
        {
            "maxReportRows": t.integer().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionIn"])
            ).optional(),
            "timeZone": t.string().optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterIn"])
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "metrics": t.array(t.string()).optional(),
        }
    ).named(renames["MediationReportSpecIn"])
    types["MediationReportSpecOut"] = t.struct(
        {
            "maxReportRows": t.integer().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionOut"])
            ).optional(),
            "timeZone": t.string().optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterOut"])
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecOut"])
    types["LocalizationSettingsIn"] = t.struct(
        {"languageCode": t.string().optional(), "currencyCode": t.string().optional()}
    ).named(renames["LocalizationSettingsIn"])
    types["LocalizationSettingsOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizationSettingsOut"])
    types["AdUnitIn"] = t.struct(
        {
            "adTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "adFormat": t.string().optional(),
            "adUnitId": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string().optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "adTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "adFormat": t.string().optional(),
            "adUnitId": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
    types["GenerateMediationReportRequestIn"] = t.struct(
        {"reportSpec": t.proxy(renames["MediationReportSpecIn"]).optional()}
    ).named(renames["GenerateMediationReportRequestIn"])
    types["GenerateMediationReportRequestOut"] = t.struct(
        {
            "reportSpec": t.proxy(renames["MediationReportSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateMediationReportRequestOut"])
    types["MediationReportSpecDimensionFilterIn"] = t.struct(
        {
            "matchesAny": t.proxy(renames["StringListIn"]).optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["MediationReportSpecDimensionFilterIn"])
    types["MediationReportSpecDimensionFilterOut"] = t.struct(
        {
            "matchesAny": t.proxy(renames["StringListOut"]).optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecDimensionFilterOut"])
    types["ReportHeaderIn"] = t.struct(
        {
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "reportingTimeZone": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["ReportHeaderIn"])
    types["ReportHeaderOut"] = t.struct(
        {
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "reportingTimeZone": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportHeaderOut"])
    types["ReportRowMetricValueIn"] = t.struct(
        {
            "integerValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "microsValue": t.string().optional(),
        }
    ).named(renames["ReportRowMetricValueIn"])
    types["ReportRowMetricValueOut"] = t.struct(
        {
            "integerValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "microsValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowMetricValueOut"])
    types["MediationReportSpecSortConditionIn"] = t.struct(
        {
            "order": t.string().optional(),
            "metric": t.string().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["MediationReportSpecSortConditionIn"])
    types["MediationReportSpecSortConditionOut"] = t.struct(
        {
            "order": t.string().optional(),
            "metric": t.string().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecSortConditionOut"])
    types["ReportFooterIn"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["ReportWarningIn"])).optional(),
            "matchingRowCount": t.string().optional(),
        }
    ).named(renames["ReportFooterIn"])
    types["ReportFooterOut"] = t.struct(
        {
            "warnings": t.array(t.proxy(renames["ReportWarningOut"])).optional(),
            "matchingRowCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportFooterOut"])
    types["GenerateNetworkReportResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ReportHeaderIn"]).optional(),
            "row": t.proxy(renames["ReportRowIn"]).optional(),
            "footer": t.proxy(renames["ReportFooterIn"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseIn"])
    types["GenerateNetworkReportResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ReportHeaderOut"]).optional(),
            "row": t.proxy(renames["ReportRowOut"]).optional(),
            "footer": t.proxy(renames["ReportFooterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseOut"])
    types["ListAppsResponseIn"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["AppIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAppsResponseIn"])
    types["ListAppsResponseOut"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["AppOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAppsResponseOut"])
    types["StringListIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["StringListIn"]
    )
    types["StringListOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
    types["ReportWarningIn"] = t.struct(
        {"description": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ReportWarningIn"])
    types["ReportWarningOut"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWarningOut"])

    functions = {}
    functions["accountsGet"] = admob.get(
        "v1/accounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsList"] = admob.get(
        "v1/accounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPublisherAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAppsList"] = admob.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsMediationReportGenerate"] = admob.post(
        "v1/{parent}/mediationReport:generate",
        t.struct(
            {
                "parent": t.string().optional(),
                "reportSpec": t.proxy(renames["MediationReportSpecIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateMediationReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAdUnitsList"] = admob.get(
        "v1/{parent}/adUnits",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsNetworkReportGenerate"] = admob.post(
        "v1/{parent}/networkReport:generate",
        t.struct(
            {
                "parent": t.string().optional(),
                "reportSpec": t.proxy(renames["NetworkReportSpecIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GenerateNetworkReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="admob", renames=renames, types=types, functions=functions)
