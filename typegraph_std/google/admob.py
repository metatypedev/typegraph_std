from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_admob():
    admob = HTTPRuntime("https://admob.googleapis.com/")

    renames = {
        "ErrorResponse": "_admob_1_ErrorResponse",
        "MediationReportSpecIn": "_admob_2_MediationReportSpecIn",
        "MediationReportSpecOut": "_admob_3_MediationReportSpecOut",
        "GenerateMediationReportResponseIn": "_admob_4_GenerateMediationReportResponseIn",
        "GenerateMediationReportResponseOut": "_admob_5_GenerateMediationReportResponseOut",
        "GenerateMediationReportRequestIn": "_admob_6_GenerateMediationReportRequestIn",
        "GenerateMediationReportRequestOut": "_admob_7_GenerateMediationReportRequestOut",
        "DateRangeIn": "_admob_8_DateRangeIn",
        "DateRangeOut": "_admob_9_DateRangeOut",
        "StringListIn": "_admob_10_StringListIn",
        "StringListOut": "_admob_11_StringListOut",
        "ListAdUnitsResponseIn": "_admob_12_ListAdUnitsResponseIn",
        "ListAdUnitsResponseOut": "_admob_13_ListAdUnitsResponseOut",
        "LocalizationSettingsIn": "_admob_14_LocalizationSettingsIn",
        "LocalizationSettingsOut": "_admob_15_LocalizationSettingsOut",
        "DateIn": "_admob_16_DateIn",
        "DateOut": "_admob_17_DateOut",
        "MediationReportSpecDimensionFilterIn": "_admob_18_MediationReportSpecDimensionFilterIn",
        "MediationReportSpecDimensionFilterOut": "_admob_19_MediationReportSpecDimensionFilterOut",
        "MediationReportSpecSortConditionIn": "_admob_20_MediationReportSpecSortConditionIn",
        "MediationReportSpecSortConditionOut": "_admob_21_MediationReportSpecSortConditionOut",
        "AppIn": "_admob_22_AppIn",
        "AppOut": "_admob_23_AppOut",
        "ReportRowMetricValueIn": "_admob_24_ReportRowMetricValueIn",
        "ReportRowMetricValueOut": "_admob_25_ReportRowMetricValueOut",
        "NetworkReportSpecIn": "_admob_26_NetworkReportSpecIn",
        "NetworkReportSpecOut": "_admob_27_NetworkReportSpecOut",
        "AppManualAppInfoIn": "_admob_28_AppManualAppInfoIn",
        "AppManualAppInfoOut": "_admob_29_AppManualAppInfoOut",
        "ListPublisherAccountsResponseIn": "_admob_30_ListPublisherAccountsResponseIn",
        "ListPublisherAccountsResponseOut": "_admob_31_ListPublisherAccountsResponseOut",
        "ReportWarningIn": "_admob_32_ReportWarningIn",
        "ReportWarningOut": "_admob_33_ReportWarningOut",
        "GenerateNetworkReportRequestIn": "_admob_34_GenerateNetworkReportRequestIn",
        "GenerateNetworkReportRequestOut": "_admob_35_GenerateNetworkReportRequestOut",
        "PublisherAccountIn": "_admob_36_PublisherAccountIn",
        "PublisherAccountOut": "_admob_37_PublisherAccountOut",
        "NetworkReportSpecSortConditionIn": "_admob_38_NetworkReportSpecSortConditionIn",
        "NetworkReportSpecSortConditionOut": "_admob_39_NetworkReportSpecSortConditionOut",
        "GenerateNetworkReportResponseIn": "_admob_40_GenerateNetworkReportResponseIn",
        "GenerateNetworkReportResponseOut": "_admob_41_GenerateNetworkReportResponseOut",
        "ReportFooterIn": "_admob_42_ReportFooterIn",
        "ReportFooterOut": "_admob_43_ReportFooterOut",
        "NetworkReportSpecDimensionFilterIn": "_admob_44_NetworkReportSpecDimensionFilterIn",
        "NetworkReportSpecDimensionFilterOut": "_admob_45_NetworkReportSpecDimensionFilterOut",
        "ReportHeaderIn": "_admob_46_ReportHeaderIn",
        "ReportHeaderOut": "_admob_47_ReportHeaderOut",
        "AdUnitIn": "_admob_48_AdUnitIn",
        "AdUnitOut": "_admob_49_AdUnitOut",
        "AppLinkedAppInfoIn": "_admob_50_AppLinkedAppInfoIn",
        "AppLinkedAppInfoOut": "_admob_51_AppLinkedAppInfoOut",
        "ReportRowIn": "_admob_52_ReportRowIn",
        "ReportRowOut": "_admob_53_ReportRowOut",
        "ReportRowDimensionValueIn": "_admob_54_ReportRowDimensionValueIn",
        "ReportRowDimensionValueOut": "_admob_55_ReportRowDimensionValueOut",
        "ListAppsResponseIn": "_admob_56_ListAppsResponseIn",
        "ListAppsResponseOut": "_admob_57_ListAppsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MediationReportSpecIn"] = t.struct(
        {
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionIn"])
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "timeZone": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "maxReportRows": t.integer().optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterIn"])
            ).optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["MediationReportSpecIn"])
    types["MediationReportSpecOut"] = t.struct(
        {
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionOut"])
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "timeZone": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "maxReportRows": t.integer().optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterOut"])
            ).optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecOut"])
    types["GenerateMediationReportResponseIn"] = t.struct(
        {
            "footer": t.proxy(renames["ReportFooterIn"]).optional(),
            "header": t.proxy(renames["ReportHeaderIn"]).optional(),
            "row": t.proxy(renames["ReportRowIn"]).optional(),
        }
    ).named(renames["GenerateMediationReportResponseIn"])
    types["GenerateMediationReportResponseOut"] = t.struct(
        {
            "footer": t.proxy(renames["ReportFooterOut"]).optional(),
            "header": t.proxy(renames["ReportHeaderOut"]).optional(),
            "row": t.proxy(renames["ReportRowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateMediationReportResponseOut"])
    types["GenerateMediationReportRequestIn"] = t.struct(
        {"reportSpec": t.proxy(renames["MediationReportSpecIn"]).optional()}
    ).named(renames["GenerateMediationReportRequestIn"])
    types["GenerateMediationReportRequestOut"] = t.struct(
        {
            "reportSpec": t.proxy(renames["MediationReportSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateMediationReportRequestOut"])
    types["DateRangeIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["StringListIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["StringListIn"]
    )
    types["StringListOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
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
    types["AppIn"] = t.struct(
        {
            "name": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoIn"]).optional(),
            "manualAppInfo": t.proxy(renames["AppManualAppInfoIn"]).optional(),
            "appId": t.string().optional(),
            "platform": t.string().optional(),
        }
    ).named(renames["AppIn"])
    types["AppOut"] = t.struct(
        {
            "name": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoOut"]).optional(),
            "manualAppInfo": t.proxy(renames["AppManualAppInfoOut"]).optional(),
            "appId": t.string().optional(),
            "appApprovalState": t.string().optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppOut"])
    types["ReportRowMetricValueIn"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "microsValue": t.string().optional(),
            "integerValue": t.string().optional(),
        }
    ).named(renames["ReportRowMetricValueIn"])
    types["ReportRowMetricValueOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "microsValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowMetricValueOut"])
    types["NetworkReportSpecIn"] = t.struct(
        {
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionIn"])
            ).optional(),
            "timeZone": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "dimensions": t.array(t.string()).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterIn"])
            ).optional(),
        }
    ).named(renames["NetworkReportSpecIn"])
    types["NetworkReportSpecOut"] = t.struct(
        {
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionOut"])
            ).optional(),
            "timeZone": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "dimensions": t.array(t.string()).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecOut"])
    types["AppManualAppInfoIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["AppManualAppInfoIn"])
    types["AppManualAppInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppManualAppInfoOut"])
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
    types["ReportWarningIn"] = t.struct(
        {"type": t.string().optional(), "description": t.string().optional()}
    ).named(renames["ReportWarningIn"])
    types["ReportWarningOut"] = t.struct(
        {
            "type": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportWarningOut"])
    types["GenerateNetworkReportRequestIn"] = t.struct(
        {"reportSpec": t.proxy(renames["NetworkReportSpecIn"]).optional()}
    ).named(renames["GenerateNetworkReportRequestIn"])
    types["GenerateNetworkReportRequestOut"] = t.struct(
        {
            "reportSpec": t.proxy(renames["NetworkReportSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateNetworkReportRequestOut"])
    types["PublisherAccountIn"] = t.struct(
        {
            "reportingTimeZone": t.string().optional(),
            "currencyCode": t.string().optional(),
            "publisherId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PublisherAccountIn"])
    types["PublisherAccountOut"] = t.struct(
        {
            "reportingTimeZone": t.string().optional(),
            "currencyCode": t.string().optional(),
            "publisherId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherAccountOut"])
    types["NetworkReportSpecSortConditionIn"] = t.struct(
        {
            "order": t.string().optional(),
            "dimension": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionIn"])
    types["NetworkReportSpecSortConditionOut"] = t.struct(
        {
            "order": t.string().optional(),
            "dimension": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionOut"])
    types["GenerateNetworkReportResponseIn"] = t.struct(
        {
            "footer": t.proxy(renames["ReportFooterIn"]).optional(),
            "row": t.proxy(renames["ReportRowIn"]).optional(),
            "header": t.proxy(renames["ReportHeaderIn"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseIn"])
    types["GenerateNetworkReportResponseOut"] = t.struct(
        {
            "footer": t.proxy(renames["ReportFooterOut"]).optional(),
            "row": t.proxy(renames["ReportRowOut"]).optional(),
            "header": t.proxy(renames["ReportHeaderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseOut"])
    types["ReportFooterIn"] = t.struct(
        {
            "matchingRowCount": t.string().optional(),
            "warnings": t.array(t.proxy(renames["ReportWarningIn"])).optional(),
        }
    ).named(renames["ReportFooterIn"])
    types["ReportFooterOut"] = t.struct(
        {
            "matchingRowCount": t.string().optional(),
            "warnings": t.array(t.proxy(renames["ReportWarningOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportFooterOut"])
    types["NetworkReportSpecDimensionFilterIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "matchesAny": t.proxy(renames["StringListIn"]).optional(),
        }
    ).named(renames["NetworkReportSpecDimensionFilterIn"])
    types["NetworkReportSpecDimensionFilterOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "matchesAny": t.proxy(renames["StringListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecDimensionFilterOut"])
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
    types["AdUnitIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "adUnitId": t.string().optional(),
            "displayName": t.string().optional(),
            "adFormat": t.string().optional(),
            "adTypes": t.array(t.string()).optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "adUnitId": t.string().optional(),
            "displayName": t.string().optional(),
            "adFormat": t.string().optional(),
            "adTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
    types["AppLinkedAppInfoIn"] = t.struct({"appStoreId": t.string().optional()}).named(
        renames["AppLinkedAppInfoIn"]
    )
    types["AppLinkedAppInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "appStoreId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppLinkedAppInfoOut"])
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
    types["ListAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["AppIn"])).optional(),
        }
    ).named(renames["ListAppsResponseIn"])
    types["ListAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["AppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAppsResponseOut"])

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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
    functions["accountsAppsList"] = admob.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="admob", renames=renames, types=Box(types), functions=Box(functions)
    )
