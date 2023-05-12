from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_admob() -> Import:
    admob = HTTPRuntime("https://admob.googleapis.com/")

    renames = {
        "ErrorResponse": "_admob_1_ErrorResponse",
        "NetworkReportSpecSortConditionIn": "_admob_2_NetworkReportSpecSortConditionIn",
        "NetworkReportSpecSortConditionOut": "_admob_3_NetworkReportSpecSortConditionOut",
        "DateRangeIn": "_admob_4_DateRangeIn",
        "DateRangeOut": "_admob_5_DateRangeOut",
        "ListAdUnitsResponseIn": "_admob_6_ListAdUnitsResponseIn",
        "ListAdUnitsResponseOut": "_admob_7_ListAdUnitsResponseOut",
        "ListPublisherAccountsResponseIn": "_admob_8_ListPublisherAccountsResponseIn",
        "ListPublisherAccountsResponseOut": "_admob_9_ListPublisherAccountsResponseOut",
        "LocalizationSettingsIn": "_admob_10_LocalizationSettingsIn",
        "LocalizationSettingsOut": "_admob_11_LocalizationSettingsOut",
        "ReportFooterIn": "_admob_12_ReportFooterIn",
        "ReportFooterOut": "_admob_13_ReportFooterOut",
        "GenerateMediationReportRequestIn": "_admob_14_GenerateMediationReportRequestIn",
        "GenerateMediationReportRequestOut": "_admob_15_GenerateMediationReportRequestOut",
        "GenerateNetworkReportResponseIn": "_admob_16_GenerateNetworkReportResponseIn",
        "GenerateNetworkReportResponseOut": "_admob_17_GenerateNetworkReportResponseOut",
        "ListAppsResponseIn": "_admob_18_ListAppsResponseIn",
        "ListAppsResponseOut": "_admob_19_ListAppsResponseOut",
        "AppLinkedAppInfoIn": "_admob_20_AppLinkedAppInfoIn",
        "AppLinkedAppInfoOut": "_admob_21_AppLinkedAppInfoOut",
        "PublisherAccountIn": "_admob_22_PublisherAccountIn",
        "PublisherAccountOut": "_admob_23_PublisherAccountOut",
        "MediationReportSpecSortConditionIn": "_admob_24_MediationReportSpecSortConditionIn",
        "MediationReportSpecSortConditionOut": "_admob_25_MediationReportSpecSortConditionOut",
        "GenerateMediationReportResponseIn": "_admob_26_GenerateMediationReportResponseIn",
        "GenerateMediationReportResponseOut": "_admob_27_GenerateMediationReportResponseOut",
        "ReportHeaderIn": "_admob_28_ReportHeaderIn",
        "ReportHeaderOut": "_admob_29_ReportHeaderOut",
        "AppIn": "_admob_30_AppIn",
        "AppOut": "_admob_31_AppOut",
        "StringListIn": "_admob_32_StringListIn",
        "StringListOut": "_admob_33_StringListOut",
        "AppManualAppInfoIn": "_admob_34_AppManualAppInfoIn",
        "AppManualAppInfoOut": "_admob_35_AppManualAppInfoOut",
        "GenerateNetworkReportRequestIn": "_admob_36_GenerateNetworkReportRequestIn",
        "GenerateNetworkReportRequestOut": "_admob_37_GenerateNetworkReportRequestOut",
        "DateIn": "_admob_38_DateIn",
        "DateOut": "_admob_39_DateOut",
        "AdUnitIn": "_admob_40_AdUnitIn",
        "AdUnitOut": "_admob_41_AdUnitOut",
        "ReportWarningIn": "_admob_42_ReportWarningIn",
        "ReportWarningOut": "_admob_43_ReportWarningOut",
        "ReportRowMetricValueIn": "_admob_44_ReportRowMetricValueIn",
        "ReportRowMetricValueOut": "_admob_45_ReportRowMetricValueOut",
        "ReportRowIn": "_admob_46_ReportRowIn",
        "ReportRowOut": "_admob_47_ReportRowOut",
        "ReportRowDimensionValueIn": "_admob_48_ReportRowDimensionValueIn",
        "ReportRowDimensionValueOut": "_admob_49_ReportRowDimensionValueOut",
        "NetworkReportSpecIn": "_admob_50_NetworkReportSpecIn",
        "NetworkReportSpecOut": "_admob_51_NetworkReportSpecOut",
        "MediationReportSpecIn": "_admob_52_MediationReportSpecIn",
        "MediationReportSpecOut": "_admob_53_MediationReportSpecOut",
        "NetworkReportSpecDimensionFilterIn": "_admob_54_NetworkReportSpecDimensionFilterIn",
        "NetworkReportSpecDimensionFilterOut": "_admob_55_NetworkReportSpecDimensionFilterOut",
        "MediationReportSpecDimensionFilterIn": "_admob_56_MediationReportSpecDimensionFilterIn",
        "MediationReportSpecDimensionFilterOut": "_admob_57_MediationReportSpecDimensionFilterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NetworkReportSpecSortConditionIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "order": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionIn"])
    types["NetworkReportSpecSortConditionOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "order": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecSortConditionOut"])
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
    types["ListPublisherAccountsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "account": t.array(t.proxy(renames["PublisherAccountIn"])).optional(),
        }
    ).named(renames["ListPublisherAccountsResponseIn"])
    types["ListPublisherAccountsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "account": t.array(t.proxy(renames["PublisherAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPublisherAccountsResponseOut"])
    types["LocalizationSettingsIn"] = t.struct(
        {"currencyCode": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["LocalizationSettingsIn"])
    types["LocalizationSettingsOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizationSettingsOut"])
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
    types["GenerateMediationReportRequestIn"] = t.struct(
        {"reportSpec": t.proxy(renames["MediationReportSpecIn"]).optional()}
    ).named(renames["GenerateMediationReportRequestIn"])
    types["GenerateMediationReportRequestOut"] = t.struct(
        {
            "reportSpec": t.proxy(renames["MediationReportSpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateMediationReportRequestOut"])
    types["GenerateNetworkReportResponseIn"] = t.struct(
        {
            "header": t.proxy(renames["ReportHeaderIn"]).optional(),
            "footer": t.proxy(renames["ReportFooterIn"]).optional(),
            "row": t.proxy(renames["ReportRowIn"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseIn"])
    types["GenerateNetworkReportResponseOut"] = t.struct(
        {
            "header": t.proxy(renames["ReportHeaderOut"]).optional(),
            "footer": t.proxy(renames["ReportFooterOut"]).optional(),
            "row": t.proxy(renames["ReportRowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateNetworkReportResponseOut"])
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
    types["MediationReportSpecSortConditionIn"] = t.struct(
        {
            "order": t.string().optional(),
            "dimension": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["MediationReportSpecSortConditionIn"])
    types["MediationReportSpecSortConditionOut"] = t.struct(
        {
            "order": t.string().optional(),
            "dimension": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecSortConditionOut"])
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
    types["AppIn"] = t.struct(
        {
            "manualAppInfo": t.proxy(renames["AppManualAppInfoIn"]).optional(),
            "platform": t.string().optional(),
            "name": t.string().optional(),
            "appId": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoIn"]).optional(),
        }
    ).named(renames["AppIn"])
    types["AppOut"] = t.struct(
        {
            "manualAppInfo": t.proxy(renames["AppManualAppInfoOut"]).optional(),
            "platform": t.string().optional(),
            "appApprovalState": t.string().optional(),
            "name": t.string().optional(),
            "appId": t.string().optional(),
            "linkedAppInfo": t.proxy(renames["AppLinkedAppInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppOut"])
    types["StringListIn"] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames["StringListIn"]
    )
    types["StringListOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringListOut"])
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
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["AdUnitIn"] = t.struct(
        {
            "adFormat": t.string().optional(),
            "adUnitId": t.string().optional(),
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "adTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AdUnitIn"])
    types["AdUnitOut"] = t.struct(
        {
            "adFormat": t.string().optional(),
            "adUnitId": t.string().optional(),
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "adTypes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdUnitOut"])
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
    types["ReportRowMetricValueIn"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "microsValue": t.string().optional(),
        }
    ).named(renames["ReportRowMetricValueIn"])
    types["ReportRowMetricValueOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "microsValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowMetricValueOut"])
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
    types["ReportRowDimensionValueIn"] = t.struct(
        {"value": t.string().optional(), "displayLabel": t.string().optional()}
    ).named(renames["ReportRowDimensionValueIn"])
    types["ReportRowDimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "displayLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowDimensionValueOut"])
    types["NetworkReportSpecIn"] = t.struct(
        {
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterIn"])
            ).optional(),
            "timeZone": t.string().optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionIn"])
            ).optional(),
        }
    ).named(renames["NetworkReportSpecIn"])
    types["NetworkReportSpecOut"] = t.struct(
        {
            "dimensionFilters": t.array(
                t.proxy(renames["NetworkReportSpecDimensionFilterOut"])
            ).optional(),
            "timeZone": t.string().optional(),
            "maxReportRows": t.integer().optional(),
            "metrics": t.array(t.string()).optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "dimensions": t.array(t.string()).optional(),
            "sortConditions": t.array(
                t.proxy(renames["NetworkReportSpecSortConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkReportSpecOut"])
    types["MediationReportSpecIn"] = t.struct(
        {
            "maxReportRows": t.integer().optional(),
            "timeZone": t.string().optional(),
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionIn"])
            ).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterIn"])
            ).optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsIn"]
            ).optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["MediationReportSpecIn"])
    types["MediationReportSpecOut"] = t.struct(
        {
            "maxReportRows": t.integer().optional(),
            "timeZone": t.string().optional(),
            "sortConditions": t.array(
                t.proxy(renames["MediationReportSpecSortConditionOut"])
            ).optional(),
            "dimensionFilters": t.array(
                t.proxy(renames["MediationReportSpecDimensionFilterOut"])
            ).optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "localizationSettings": t.proxy(
                renames["LocalizationSettingsOut"]
            ).optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecOut"])
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
    types["MediationReportSpecDimensionFilterIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "matchesAny": t.proxy(renames["StringListIn"]).optional(),
        }
    ).named(renames["MediationReportSpecDimensionFilterIn"])
    types["MediationReportSpecDimensionFilterOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "matchesAny": t.proxy(renames["StringListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediationReportSpecDimensionFilterOut"])

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
    functions["accountsAdUnitsList"] = admob.get(
        "v1/{parent}/adUnits",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAdUnitsResponseOut"]),
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
