from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_admob() -> Import:
    admob = HTTPRuntime("https://admob.googleapis.com/")

    renames = {
        "ErrorResponse": "_admob_1_ErrorResponse",
        "ReportFooterIn": "_admob_2_ReportFooterIn",
        "ReportFooterOut": "_admob_3_ReportFooterOut",
        "ListAdUnitsResponseIn": "_admob_4_ListAdUnitsResponseIn",
        "ListAdUnitsResponseOut": "_admob_5_ListAdUnitsResponseOut",
        "ReportRowIn": "_admob_6_ReportRowIn",
        "ReportRowOut": "_admob_7_ReportRowOut",
        "AppManualAppInfoIn": "_admob_8_AppManualAppInfoIn",
        "AppManualAppInfoOut": "_admob_9_AppManualAppInfoOut",
        "GenerateNetworkReportRequestIn": "_admob_10_GenerateNetworkReportRequestIn",
        "GenerateNetworkReportRequestOut": "_admob_11_GenerateNetworkReportRequestOut",
        "GenerateMediationReportResponseIn": "_admob_12_GenerateMediationReportResponseIn",
        "GenerateMediationReportResponseOut": "_admob_13_GenerateMediationReportResponseOut",
        "AppIn": "_admob_14_AppIn",
        "AppOut": "_admob_15_AppOut",
        "MediationReportSpecIn": "_admob_16_MediationReportSpecIn",
        "MediationReportSpecOut": "_admob_17_MediationReportSpecOut",
        "ListPublisherAccountsResponseIn": "_admob_18_ListPublisherAccountsResponseIn",
        "ListPublisherAccountsResponseOut": "_admob_19_ListPublisherAccountsResponseOut",
        "LocalizationSettingsIn": "_admob_20_LocalizationSettingsIn",
        "LocalizationSettingsOut": "_admob_21_LocalizationSettingsOut",
        "MediationReportSpecSortConditionIn": "_admob_22_MediationReportSpecSortConditionIn",
        "MediationReportSpecSortConditionOut": "_admob_23_MediationReportSpecSortConditionOut",
        "NetworkReportSpecDimensionFilterIn": "_admob_24_NetworkReportSpecDimensionFilterIn",
        "NetworkReportSpecDimensionFilterOut": "_admob_25_NetworkReportSpecDimensionFilterOut",
        "NetworkReportSpecSortConditionIn": "_admob_26_NetworkReportSpecSortConditionIn",
        "NetworkReportSpecSortConditionOut": "_admob_27_NetworkReportSpecSortConditionOut",
        "ListAppsResponseIn": "_admob_28_ListAppsResponseIn",
        "ListAppsResponseOut": "_admob_29_ListAppsResponseOut",
        "PublisherAccountIn": "_admob_30_PublisherAccountIn",
        "PublisherAccountOut": "_admob_31_PublisherAccountOut",
        "DateRangeIn": "_admob_32_DateRangeIn",
        "DateRangeOut": "_admob_33_DateRangeOut",
        "AdUnitIn": "_admob_34_AdUnitIn",
        "AdUnitOut": "_admob_35_AdUnitOut",
        "GenerateNetworkReportResponseIn": "_admob_36_GenerateNetworkReportResponseIn",
        "GenerateNetworkReportResponseOut": "_admob_37_GenerateNetworkReportResponseOut",
        "MediationReportSpecDimensionFilterIn": "_admob_38_MediationReportSpecDimensionFilterIn",
        "MediationReportSpecDimensionFilterOut": "_admob_39_MediationReportSpecDimensionFilterOut",
        "ReportRowMetricValueIn": "_admob_40_ReportRowMetricValueIn",
        "ReportRowMetricValueOut": "_admob_41_ReportRowMetricValueOut",
        "DateIn": "_admob_42_DateIn",
        "DateOut": "_admob_43_DateOut",
        "ReportHeaderIn": "_admob_44_ReportHeaderIn",
        "ReportHeaderOut": "_admob_45_ReportHeaderOut",
        "StringListIn": "_admob_46_StringListIn",
        "StringListOut": "_admob_47_StringListOut",
        "GenerateMediationReportRequestIn": "_admob_48_GenerateMediationReportRequestIn",
        "GenerateMediationReportRequestOut": "_admob_49_GenerateMediationReportRequestOut",
        "ReportRowDimensionValueIn": "_admob_50_ReportRowDimensionValueIn",
        "ReportRowDimensionValueOut": "_admob_51_ReportRowDimensionValueOut",
        "NetworkReportSpecIn": "_admob_52_NetworkReportSpecIn",
        "NetworkReportSpecOut": "_admob_53_NetworkReportSpecOut",
        "AppLinkedAppInfoIn": "_admob_54_AppLinkedAppInfoIn",
        "AppLinkedAppInfoOut": "_admob_55_AppLinkedAppInfoOut",
        "ReportWarningIn": "_admob_56_ReportWarningIn",
        "ReportWarningOut": "_admob_57_ReportWarningOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ReportRowIn"] = t.struct(
        {
            "dimensionValues": t.struct({"_": t.string().optional()}).optional(),
            "metricValues": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ReportRowIn"])
    types["ReportRowOut"] = t.struct(
        {
            "dimensionValues": t.struct({"_": t.string().optional()}).optional(),
            "metricValues": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowOut"])
    types["AppManualAppInfoIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["AppManualAppInfoIn"])
    types["AppManualAppInfoOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppManualAppInfoOut"])
    types["GenerateNetworkReportRequestIn"] = t.struct(
        {"reportSpec": t.proxy(renames["NetworkReportSpecIn"]).optional()}
    ).named(renames["GenerateNetworkReportRequestIn"])
    types["GenerateNetworkReportRequestOut"] = t.struct(
        {
            "reportSpec": t.proxy(renames["NetworkReportSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateNetworkReportRequestOut"])
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
    types["AppIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "manualAppInfo": t.proxy(renames["AppManualAppInfoIn"]).optional(),
            "name": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoIn"]).optional(),
            "platform": t.string().optional(),
        }
    ).named(renames["AppIn"])
    types["AppOut"] = t.struct(
        {
            "appId": t.string().optional(),
            "appApprovalState": t.string().optional(),
            "manualAppInfo": t.proxy(renames["AppManualAppInfoOut"]).optional(),
            "name": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoOut"]).optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppOut"])
    types["MediationReportSpecIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "timeZone": t.string().optional(),
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionIn"])
            ).optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterIn"])
            ).optional(),
        }
    ).named(renames["MediationReportSpecIn"])
    types["MediationReportSpecOut"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionOut"])
            ).optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecOut"])
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
    types["MediationReportSpecSortConditionIn"] = t.struct(
        {
            "metric": t.string().optional(),
            "dimension": t.string().optional(),
            "order": t.string().optional(),
        }
    ).named(renames["MediationReportSpecSortConditionIn"])
    types["MediationReportSpecSortConditionOut"] = t.struct(
        {
            "metric": t.string().optional(),
            "dimension": t.string().optional(),
            "order": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecSortConditionOut"])
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
    types["NetworkReportSpecSortConditionIn"] = t.struct(
        {
            "metric": t.string().optional(),
            "order": t.string().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionIn"])
    types["NetworkReportSpecSortConditionOut"] = t.struct(
        {
            "metric": t.string().optional(),
            "order": t.string().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionOut"])
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
    types["PublisherAccountIn"] = t.struct(
        {
            "publisherId": t.string().optional(),
            "reportingTimeZone": t.string().optional(),
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["PublisherAccountIn"])
    types["PublisherAccountOut"] = t.struct(
        {
            "publisherId": t.string().optional(),
            "reportingTimeZone": t.string().optional(),
            "name": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublisherAccountOut"])
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
    types["AdUnitIn"] = t.struct(
        {
            "adTypes": t.array(t.string()).optional(),
            "adUnitId": t.string().optional(),
            "appId": t.string().optional(),
            "adFormat": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "adTypes": t.array(t.string()).optional(),
            "adUnitId": t.string().optional(),
            "appId": t.string().optional(),
            "adFormat": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
    types["GenerateNetworkReportResponseIn"] = t.struct(
        {
            "footer": t.proxy(renames["ReportFooterIn"]).optional(),
            "header": t.proxy(renames["ReportHeaderIn"]).optional(),
            "row": t.proxy(renames["ReportRowIn"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseIn"])
    types["GenerateNetworkReportResponseOut"] = t.struct(
        {
            "footer": t.proxy(renames["ReportFooterOut"]).optional(),
            "header": t.proxy(renames["ReportHeaderOut"]).optional(),
            "row": t.proxy(renames["ReportRowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseOut"])
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
    types["ReportRowMetricValueIn"] = t.struct(
        {
            "microsValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "doubleValue": t.number().optional(),
        }
    ).named(renames["ReportRowMetricValueIn"])
    types["ReportRowMetricValueOut"] = t.struct(
        {
            "microsValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowMetricValueOut"])
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
    types["ReportHeaderIn"] = t.struct(
        {
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "reportingTimeZone": t.string().optional(),
        }
    ).named(renames["ReportHeaderIn"])
    types["ReportHeaderOut"] = t.struct(
        {
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "reportingTimeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportHeaderOut"])
    types["StringListIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["StringListIn"]
    )
    types["StringListOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
    types["GenerateMediationReportRequestIn"] = t.struct(
        {"reportSpec": t.proxy(renames["MediationReportSpecIn"]).optional()}
    ).named(renames["GenerateMediationReportRequestIn"])
    types["GenerateMediationReportRequestOut"] = t.struct(
        {
            "reportSpec": t.proxy(renames["MediationReportSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateMediationReportRequestOut"])
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
    types["NetworkReportSpecIn"] = t.struct(
        {
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterIn"])
            ).optional(),
            "maxReportRows": t.integer().optional(),
            "timeZone": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "dimensions": t.array(t.string()).optional(),
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionIn"])
            ).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "metrics": t.array(t.string()).optional(),
        }
    ).named(renames["NetworkReportSpecIn"])
    types["NetworkReportSpecOut"] = t.struct(
        {
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterOut"])
            ).optional(),
            "maxReportRows": t.integer().optional(),
            "timeZone": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "dimensions": t.array(t.string()).optional(),
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionOut"])
            ).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecOut"])
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
    functions["accountsAppsList"] = admob.get(
        "v1/{parent}/apps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppsResponseOut"]),
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

    return Import(
        importer="admob", renames=renames, types=Box(types), functions=Box(functions)
    )
