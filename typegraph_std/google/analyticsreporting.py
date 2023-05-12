from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_analyticsreporting() -> Import:
    analyticsreporting = HTTPRuntime("https://analyticsreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsreporting_1_ErrorResponse",
        "SegmentSequenceStepIn": "_analyticsreporting_2_SegmentSequenceStepIn",
        "SegmentSequenceStepOut": "_analyticsreporting_3_SegmentSequenceStepOut",
        "SearchUserActivityResponseIn": "_analyticsreporting_4_SearchUserActivityResponseIn",
        "SearchUserActivityResponseOut": "_analyticsreporting_5_SearchUserActivityResponseOut",
        "PivotIn": "_analyticsreporting_6_PivotIn",
        "PivotOut": "_analyticsreporting_7_PivotOut",
        "EcommerceDataIn": "_analyticsreporting_8_EcommerceDataIn",
        "EcommerceDataOut": "_analyticsreporting_9_EcommerceDataOut",
        "TransactionDataIn": "_analyticsreporting_10_TransactionDataIn",
        "TransactionDataOut": "_analyticsreporting_11_TransactionDataOut",
        "SegmentDefinitionIn": "_analyticsreporting_12_SegmentDefinitionIn",
        "SegmentDefinitionOut": "_analyticsreporting_13_SegmentDefinitionOut",
        "UserIn": "_analyticsreporting_14_UserIn",
        "UserOut": "_analyticsreporting_15_UserOut",
        "DimensionIn": "_analyticsreporting_16_DimensionIn",
        "DimensionOut": "_analyticsreporting_17_DimensionOut",
        "UserActivitySessionIn": "_analyticsreporting_18_UserActivitySessionIn",
        "UserActivitySessionOut": "_analyticsreporting_19_UserActivitySessionOut",
        "ActivityIn": "_analyticsreporting_20_ActivityIn",
        "ActivityOut": "_analyticsreporting_21_ActivityOut",
        "MetricFilterIn": "_analyticsreporting_22_MetricFilterIn",
        "MetricFilterOut": "_analyticsreporting_23_MetricFilterOut",
        "PivotValueRegionIn": "_analyticsreporting_24_PivotValueRegionIn",
        "PivotValueRegionOut": "_analyticsreporting_25_PivotValueRegionOut",
        "ReportIn": "_analyticsreporting_26_ReportIn",
        "ReportOut": "_analyticsreporting_27_ReportOut",
        "GetReportsResponseIn": "_analyticsreporting_28_GetReportsResponseIn",
        "GetReportsResponseOut": "_analyticsreporting_29_GetReportsResponseOut",
        "CohortGroupIn": "_analyticsreporting_30_CohortGroupIn",
        "CohortGroupOut": "_analyticsreporting_31_CohortGroupOut",
        "PivotHeaderIn": "_analyticsreporting_32_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsreporting_33_PivotHeaderOut",
        "GetReportsRequestIn": "_analyticsreporting_34_GetReportsRequestIn",
        "GetReportsRequestOut": "_analyticsreporting_35_GetReportsRequestOut",
        "CustomDimensionIn": "_analyticsreporting_36_CustomDimensionIn",
        "CustomDimensionOut": "_analyticsreporting_37_CustomDimensionOut",
        "MetricFilterClauseIn": "_analyticsreporting_38_MetricFilterClauseIn",
        "MetricFilterClauseOut": "_analyticsreporting_39_MetricFilterClauseOut",
        "ColumnHeaderIn": "_analyticsreporting_40_ColumnHeaderIn",
        "ColumnHeaderOut": "_analyticsreporting_41_ColumnHeaderOut",
        "ScreenviewDataIn": "_analyticsreporting_42_ScreenviewDataIn",
        "ScreenviewDataOut": "_analyticsreporting_43_ScreenviewDataOut",
        "DateRangeValuesIn": "_analyticsreporting_44_DateRangeValuesIn",
        "DateRangeValuesOut": "_analyticsreporting_45_DateRangeValuesOut",
        "ReportRowIn": "_analyticsreporting_46_ReportRowIn",
        "ReportRowOut": "_analyticsreporting_47_ReportRowOut",
        "ProductDataIn": "_analyticsreporting_48_ProductDataIn",
        "ProductDataOut": "_analyticsreporting_49_ProductDataOut",
        "SequenceSegmentIn": "_analyticsreporting_50_SequenceSegmentIn",
        "SequenceSegmentOut": "_analyticsreporting_51_SequenceSegmentOut",
        "SegmentMetricFilterIn": "_analyticsreporting_52_SegmentMetricFilterIn",
        "SegmentMetricFilterOut": "_analyticsreporting_53_SegmentMetricFilterOut",
        "PageviewDataIn": "_analyticsreporting_54_PageviewDataIn",
        "PageviewDataOut": "_analyticsreporting_55_PageviewDataOut",
        "CohortIn": "_analyticsreporting_56_CohortIn",
        "CohortOut": "_analyticsreporting_57_CohortOut",
        "SimpleSegmentIn": "_analyticsreporting_58_SimpleSegmentIn",
        "SimpleSegmentOut": "_analyticsreporting_59_SimpleSegmentOut",
        "ResourceQuotasRemainingIn": "_analyticsreporting_60_ResourceQuotasRemainingIn",
        "ResourceQuotasRemainingOut": "_analyticsreporting_61_ResourceQuotasRemainingOut",
        "SearchUserActivityRequestIn": "_analyticsreporting_62_SearchUserActivityRequestIn",
        "SearchUserActivityRequestOut": "_analyticsreporting_63_SearchUserActivityRequestOut",
        "MetricHeaderIn": "_analyticsreporting_64_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsreporting_65_MetricHeaderOut",
        "OrderByIn": "_analyticsreporting_66_OrderByIn",
        "OrderByOut": "_analyticsreporting_67_OrderByOut",
        "DateRangeIn": "_analyticsreporting_68_DateRangeIn",
        "DateRangeOut": "_analyticsreporting_69_DateRangeOut",
        "GoalSetDataIn": "_analyticsreporting_70_GoalSetDataIn",
        "GoalSetDataOut": "_analyticsreporting_71_GoalSetDataOut",
        "DynamicSegmentIn": "_analyticsreporting_72_DynamicSegmentIn",
        "DynamicSegmentOut": "_analyticsreporting_73_DynamicSegmentOut",
        "OrFiltersForSegmentIn": "_analyticsreporting_74_OrFiltersForSegmentIn",
        "OrFiltersForSegmentOut": "_analyticsreporting_75_OrFiltersForSegmentOut",
        "SegmentDimensionFilterIn": "_analyticsreporting_76_SegmentDimensionFilterIn",
        "SegmentDimensionFilterOut": "_analyticsreporting_77_SegmentDimensionFilterOut",
        "DimensionFilterClauseIn": "_analyticsreporting_78_DimensionFilterClauseIn",
        "DimensionFilterClauseOut": "_analyticsreporting_79_DimensionFilterClauseOut",
        "MetricIn": "_analyticsreporting_80_MetricIn",
        "MetricOut": "_analyticsreporting_81_MetricOut",
        "SegmentFilterIn": "_analyticsreporting_82_SegmentFilterIn",
        "SegmentFilterOut": "_analyticsreporting_83_SegmentFilterOut",
        "ReportDataIn": "_analyticsreporting_84_ReportDataIn",
        "ReportDataOut": "_analyticsreporting_85_ReportDataOut",
        "EventDataIn": "_analyticsreporting_86_EventDataIn",
        "EventDataOut": "_analyticsreporting_87_EventDataOut",
        "DimensionFilterIn": "_analyticsreporting_88_DimensionFilterIn",
        "DimensionFilterOut": "_analyticsreporting_89_DimensionFilterOut",
        "SegmentIn": "_analyticsreporting_90_SegmentIn",
        "SegmentOut": "_analyticsreporting_91_SegmentOut",
        "GoalDataIn": "_analyticsreporting_92_GoalDataIn",
        "GoalDataOut": "_analyticsreporting_93_GoalDataOut",
        "PivotHeaderEntryIn": "_analyticsreporting_94_PivotHeaderEntryIn",
        "PivotHeaderEntryOut": "_analyticsreporting_95_PivotHeaderEntryOut",
        "ReportRequestIn": "_analyticsreporting_96_ReportRequestIn",
        "ReportRequestOut": "_analyticsreporting_97_ReportRequestOut",
        "SegmentFilterClauseIn": "_analyticsreporting_98_SegmentFilterClauseIn",
        "SegmentFilterClauseOut": "_analyticsreporting_99_SegmentFilterClauseOut",
        "MetricHeaderEntryIn": "_analyticsreporting_100_MetricHeaderEntryIn",
        "MetricHeaderEntryOut": "_analyticsreporting_101_MetricHeaderEntryOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SegmentSequenceStepIn"] = t.struct(
        {
            "orFiltersForSegment": t.array(
                t.proxy(renames["OrFiltersForSegmentIn"])
            ).optional(),
            "matchType": t.string().optional(),
        }
    ).named(renames["SegmentSequenceStepIn"])
    types["SegmentSequenceStepOut"] = t.struct(
        {
            "orFiltersForSegment": t.array(
                t.proxy(renames["OrFiltersForSegmentOut"])
            ).optional(),
            "matchType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentSequenceStepOut"])
    types["SearchUserActivityResponseIn"] = t.struct(
        {
            "sampleRate": t.number().optional(),
            "nextPageToken": t.string().optional(),
            "totalRows": t.integer().optional(),
            "sessions": t.array(t.proxy(renames["UserActivitySessionIn"])).optional(),
        }
    ).named(renames["SearchUserActivityResponseIn"])
    types["SearchUserActivityResponseOut"] = t.struct(
        {
            "sampleRate": t.number().optional(),
            "nextPageToken": t.string().optional(),
            "totalRows": t.integer().optional(),
            "sessions": t.array(t.proxy(renames["UserActivitySessionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityResponseOut"])
    types["PivotIn"] = t.struct(
        {
            "maxGroupCount": t.integer().optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseIn"])
            ).optional(),
            "startGroup": t.integer().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["PivotIn"])
    types["PivotOut"] = t.struct(
        {
            "maxGroupCount": t.integer().optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseOut"])
            ).optional(),
            "startGroup": t.integer().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOut"])
    types["EcommerceDataIn"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionDataIn"]).optional(),
            "ecommerceType": t.string().optional(),
            "actionType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataIn"])).optional(),
        }
    ).named(renames["EcommerceDataIn"])
    types["EcommerceDataOut"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionDataOut"]).optional(),
            "ecommerceType": t.string().optional(),
            "actionType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcommerceDataOut"])
    types["TransactionDataIn"] = t.struct(
        {
            "transactionRevenue": t.number().optional(),
            "transactionTax": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionShipping": t.number().optional(),
        }
    ).named(renames["TransactionDataIn"])
    types["TransactionDataOut"] = t.struct(
        {
            "transactionRevenue": t.number().optional(),
            "transactionTax": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionShipping": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionDataOut"])
    types["SegmentDefinitionIn"] = t.struct(
        {"segmentFilters": t.array(t.proxy(renames["SegmentFilterIn"])).optional()}
    ).named(renames["SegmentDefinitionIn"])
    types["SegmentDefinitionOut"] = t.struct(
        {
            "segmentFilters": t.array(t.proxy(renames["SegmentFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentDefinitionOut"])
    types["UserIn"] = t.struct(
        {"userId": t.string().optional(), "type": t.string().optional()}
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["DimensionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "histogramBuckets": t.array(t.string()).optional(),
        }
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "histogramBuckets": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
    types["UserActivitySessionIn"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["ActivityIn"])).optional(),
            "sessionDate": t.string().optional(),
            "sessionId": t.string().optional(),
            "dataSource": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "platform": t.string().optional(),
        }
    ).named(renames["UserActivitySessionIn"])
    types["UserActivitySessionOut"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["ActivityOut"])).optional(),
            "sessionDate": t.string().optional(),
            "sessionId": t.string().optional(),
            "dataSource": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserActivitySessionOut"])
    types["ActivityIn"] = t.struct(
        {
            "pageview": t.proxy(renames["PageviewDataIn"]).optional(),
            "appview": t.proxy(renames["ScreenviewDataIn"]).optional(),
            "medium": t.string().optional(),
            "source": t.string().optional(),
            "landingPagePath": t.string().optional(),
            "activityTime": t.string().optional(),
            "ecommerce": t.proxy(renames["EcommerceDataIn"]).optional(),
            "event": t.proxy(renames["EventDataIn"]).optional(),
            "goals": t.proxy(renames["GoalSetDataIn"]).optional(),
            "channelGrouping": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionIn"])
            ).optional(),
            "hostname": t.string().optional(),
            "keyword": t.string().optional(),
            "campaign": t.string().optional(),
            "activityType": t.string().optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "pageview": t.proxy(renames["PageviewDataOut"]).optional(),
            "appview": t.proxy(renames["ScreenviewDataOut"]).optional(),
            "medium": t.string().optional(),
            "source": t.string().optional(),
            "landingPagePath": t.string().optional(),
            "activityTime": t.string().optional(),
            "ecommerce": t.proxy(renames["EcommerceDataOut"]).optional(),
            "event": t.proxy(renames["EventDataOut"]).optional(),
            "goals": t.proxy(renames["GoalSetDataOut"]).optional(),
            "channelGrouping": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionOut"])
            ).optional(),
            "hostname": t.string().optional(),
            "keyword": t.string().optional(),
            "campaign": t.string().optional(),
            "activityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
    types["MetricFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "not": t.boolean().optional(),
            "comparisonValue": t.string().optional(),
            "metricName": t.string().optional(),
        }
    ).named(renames["MetricFilterIn"])
    types["MetricFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "not": t.boolean().optional(),
            "comparisonValue": t.string().optional(),
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricFilterOut"])
    types["PivotValueRegionIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["PivotValueRegionIn"])
    types["PivotValueRegionOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueRegionOut"])
    types["ReportIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "data": t.proxy(renames["ReportDataIn"]).optional(),
            "columnHeader": t.proxy(renames["ColumnHeaderIn"]).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "data": t.proxy(renames["ReportDataOut"]).optional(),
            "columnHeader": t.proxy(renames["ColumnHeaderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["GetReportsResponseIn"] = t.struct(
        {
            "resourceQuotasRemaining": t.proxy(
                renames["ResourceQuotasRemainingIn"]
            ).optional(),
            "queryCost": t.integer().optional(),
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
        }
    ).named(renames["GetReportsResponseIn"])
    types["GetReportsResponseOut"] = t.struct(
        {
            "resourceQuotasRemaining": t.proxy(
                renames["ResourceQuotasRemainingOut"]
            ).optional(),
            "queryCost": t.integer().optional(),
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReportsResponseOut"])
    types["CohortGroupIn"] = t.struct(
        {
            "lifetimeValue": t.boolean().optional(),
            "cohorts": t.array(t.proxy(renames["CohortIn"])).optional(),
        }
    ).named(renames["CohortGroupIn"])
    types["CohortGroupOut"] = t.struct(
        {
            "lifetimeValue": t.boolean().optional(),
            "cohorts": t.array(t.proxy(renames["CohortOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortGroupOut"])
    types["PivotHeaderIn"] = t.struct(
        {
            "pivotHeaderEntries": t.array(
                t.proxy(renames["PivotHeaderEntryIn"])
            ).optional(),
            "totalPivotGroupsCount": t.integer().optional(),
        }
    ).named(renames["PivotHeaderIn"])
    types["PivotHeaderOut"] = t.struct(
        {
            "pivotHeaderEntries": t.array(
                t.proxy(renames["PivotHeaderEntryOut"])
            ).optional(),
            "totalPivotGroupsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotHeaderOut"])
    types["GetReportsRequestIn"] = t.struct(
        {
            "reportRequests": t.array(t.proxy(renames["ReportRequestIn"])).optional(),
            "useResourceQuotas": t.boolean().optional(),
        }
    ).named(renames["GetReportsRequestIn"])
    types["GetReportsRequestOut"] = t.struct(
        {
            "reportRequests": t.array(t.proxy(renames["ReportRequestOut"])).optional(),
            "useResourceQuotas": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReportsRequestOut"])
    types["CustomDimensionIn"] = t.struct(
        {"value": t.string().optional(), "index": t.integer().optional()}
    ).named(renames["CustomDimensionIn"])
    types["CustomDimensionOut"] = t.struct(
        {
            "value": t.string().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDimensionOut"])
    types["MetricFilterClauseIn"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["MetricFilterIn"])).optional(),
            "operator": t.string().optional(),
        }
    ).named(renames["MetricFilterClauseIn"])
    types["MetricFilterClauseOut"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["MetricFilterOut"])).optional(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricFilterClauseOut"])
    types["ColumnHeaderIn"] = t.struct(
        {
            "metricHeader": t.proxy(renames["MetricHeaderIn"]).optional(),
            "dimensions": t.array(t.string()).optional(),
        }
    ).named(renames["ColumnHeaderIn"])
    types["ColumnHeaderOut"] = t.struct(
        {
            "metricHeader": t.proxy(renames["MetricHeaderOut"]).optional(),
            "dimensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnHeaderOut"])
    types["ScreenviewDataIn"] = t.struct(
        {
            "mobileDeviceBranding": t.string().optional(),
            "screenName": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
            "appName": t.string().optional(),
        }
    ).named(renames["ScreenviewDataIn"])
    types["ScreenviewDataOut"] = t.struct(
        {
            "mobileDeviceBranding": t.string().optional(),
            "screenName": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
            "appName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenviewDataOut"])
    types["DateRangeValuesIn"] = t.struct(
        {
            "pivotValueRegions": t.array(
                t.proxy(renames["PivotValueRegionIn"])
            ).optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["DateRangeValuesIn"])
    types["DateRangeValuesOut"] = t.struct(
        {
            "pivotValueRegions": t.array(
                t.proxy(renames["PivotValueRegionOut"])
            ).optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeValuesOut"])
    types["ReportRowIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "dimensions": t.array(t.string()).optional(),
        }
    ).named(renames["ReportRowIn"])
    types["ReportRowOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "dimensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowOut"])
    types["ProductDataIn"] = t.struct(
        {
            "productQuantity": t.string().optional(),
            "productName": t.string().optional(),
            "productSku": t.string().optional(),
            "itemRevenue": t.number().optional(),
        }
    ).named(renames["ProductDataIn"])
    types["ProductDataOut"] = t.struct(
        {
            "productQuantity": t.string().optional(),
            "productName": t.string().optional(),
            "productSku": t.string().optional(),
            "itemRevenue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDataOut"])
    types["SequenceSegmentIn"] = t.struct(
        {
            "segmentSequenceSteps": t.array(
                t.proxy(renames["SegmentSequenceStepIn"])
            ).optional(),
            "firstStepShouldMatchFirstHit": t.boolean().optional(),
        }
    ).named(renames["SequenceSegmentIn"])
    types["SequenceSegmentOut"] = t.struct(
        {
            "segmentSequenceSteps": t.array(
                t.proxy(renames["SegmentSequenceStepOut"])
            ).optional(),
            "firstStepShouldMatchFirstHit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SequenceSegmentOut"])
    types["SegmentMetricFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "scope": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "metricName": t.string().optional(),
        }
    ).named(renames["SegmentMetricFilterIn"])
    types["SegmentMetricFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "scope": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentMetricFilterOut"])
    types["PageviewDataIn"] = t.struct(
        {"pagePath": t.string().optional(), "pageTitle": t.string().optional()}
    ).named(renames["PageviewDataIn"])
    types["PageviewDataOut"] = t.struct(
        {
            "pagePath": t.string().optional(),
            "pageTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageviewDataOut"])
    types["CohortIn"] = t.struct(
        {
            "type": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CohortIn"])
    types["CohortOut"] = t.struct(
        {
            "type": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortOut"])
    types["SimpleSegmentIn"] = t.struct(
        {
            "orFiltersForSegment": t.array(
                t.proxy(renames["OrFiltersForSegmentIn"])
            ).optional()
        }
    ).named(renames["SimpleSegmentIn"])
    types["SimpleSegmentOut"] = t.struct(
        {
            "orFiltersForSegment": t.array(
                t.proxy(renames["OrFiltersForSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleSegmentOut"])
    types["ResourceQuotasRemainingIn"] = t.struct(
        {
            "hourlyQuotaTokensRemaining": t.integer().optional(),
            "dailyQuotaTokensRemaining": t.integer().optional(),
        }
    ).named(renames["ResourceQuotasRemainingIn"])
    types["ResourceQuotasRemainingOut"] = t.struct(
        {
            "hourlyQuotaTokensRemaining": t.integer().optional(),
            "dailyQuotaTokensRemaining": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceQuotasRemainingOut"])
    types["SearchUserActivityRequestIn"] = t.struct(
        {
            "viewId": t.string(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "user": t.proxy(renames["UserIn"]),
            "activityTypes": t.array(t.string()).optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["SearchUserActivityRequestIn"])
    types["SearchUserActivityRequestOut"] = t.struct(
        {
            "viewId": t.string(),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "user": t.proxy(renames["UserOut"]),
            "activityTypes": t.array(t.string()).optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityRequestOut"])
    types["MetricHeaderIn"] = t.struct(
        {
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderIn"])).optional(),
            "metricHeaderEntries": t.array(
                t.proxy(renames["MetricHeaderEntryIn"])
            ).optional(),
        }
    ).named(renames["MetricHeaderIn"])
    types["MetricHeaderOut"] = t.struct(
        {
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderOut"])).optional(),
            "metricHeaderEntries": t.array(
                t.proxy(renames["MetricHeaderEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricHeaderOut"])
    types["OrderByIn"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "orderType": t.string().optional(),
            "sortOrder": t.string().optional(),
        }
    ).named(renames["OrderByIn"])
    types["OrderByOut"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "orderType": t.string().optional(),
            "sortOrder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderByOut"])
    types["DateRangeIn"] = t.struct(
        {"startDate": t.string().optional(), "endDate": t.string().optional()}
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["GoalSetDataIn"] = t.struct(
        {"goals": t.array(t.proxy(renames["GoalDataIn"])).optional()}
    ).named(renames["GoalSetDataIn"])
    types["GoalSetDataOut"] = t.struct(
        {
            "goals": t.array(t.proxy(renames["GoalDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalSetDataOut"])
    types["DynamicSegmentIn"] = t.struct(
        {
            "sessionSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
            "userSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DynamicSegmentIn"])
    types["DynamicSegmentOut"] = t.struct(
        {
            "sessionSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "userSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicSegmentOut"])
    types["OrFiltersForSegmentIn"] = t.struct(
        {
            "segmentFilterClauses": t.array(
                t.proxy(renames["SegmentFilterClauseIn"])
            ).optional()
        }
    ).named(renames["OrFiltersForSegmentIn"])
    types["OrFiltersForSegmentOut"] = t.struct(
        {
            "segmentFilterClauses": t.array(
                t.proxy(renames["SegmentFilterClauseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrFiltersForSegmentOut"])
    types["SegmentDimensionFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "maxComparisonValue": t.string().optional(),
            "minComparisonValue": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "dimensionName": t.string().optional(),
        }
    ).named(renames["SegmentDimensionFilterIn"])
    types["SegmentDimensionFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "maxComparisonValue": t.string().optional(),
            "minComparisonValue": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentDimensionFilterOut"])
    types["DimensionFilterClauseIn"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["DimensionFilterIn"])).optional(),
            "operator": t.string().optional(),
        }
    ).named(renames["DimensionFilterClauseIn"])
    types["DimensionFilterClauseOut"] = t.struct(
        {
            "filters": t.array(t.proxy(renames["DimensionFilterOut"])).optional(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionFilterClauseOut"])
    types["MetricIn"] = t.struct(
        {
            "formattingType": t.string().optional(),
            "alias": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "formattingType": t.string().optional(),
            "alias": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["SegmentFilterIn"] = t.struct(
        {
            "not": t.boolean().optional(),
            "sequenceSegment": t.proxy(renames["SequenceSegmentIn"]).optional(),
            "simpleSegment": t.proxy(renames["SimpleSegmentIn"]).optional(),
        }
    ).named(renames["SegmentFilterIn"])
    types["SegmentFilterOut"] = t.struct(
        {
            "not": t.boolean().optional(),
            "sequenceSegment": t.proxy(renames["SequenceSegmentOut"]).optional(),
            "simpleSegment": t.proxy(renames["SimpleSegmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentFilterOut"])
    types["ReportDataIn"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "isDataGolden": t.boolean().optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "rowCount": t.integer().optional(),
            "dataLastRefreshed": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowIn"])).optional(),
            "emptyReason": t.string().optional(),
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
        }
    ).named(renames["ReportDataIn"])
    types["ReportDataOut"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "isDataGolden": t.boolean().optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "rowCount": t.integer().optional(),
            "dataLastRefreshed": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "emptyReason": t.string().optional(),
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportDataOut"])
    types["EventDataIn"] = t.struct(
        {
            "eventCategory": t.string().optional(),
            "eventAction": t.string().optional(),
            "eventCount": t.string().optional(),
            "eventValue": t.string().optional(),
            "eventLabel": t.string().optional(),
        }
    ).named(renames["EventDataIn"])
    types["EventDataOut"] = t.struct(
        {
            "eventCategory": t.string().optional(),
            "eventAction": t.string().optional(),
            "eventCount": t.string().optional(),
            "eventValue": t.string().optional(),
            "eventLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDataOut"])
    types["DimensionFilterIn"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "expressions": t.array(t.string()).optional(),
            "not": t.boolean().optional(),
            "operator": t.string().optional(),
        }
    ).named(renames["DimensionFilterIn"])
    types["DimensionFilterOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "expressions": t.array(t.string()).optional(),
            "not": t.boolean().optional(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionFilterOut"])
    types["SegmentIn"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "dynamicSegment": t.proxy(renames["DynamicSegmentIn"]).optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "segmentId": t.string().optional(),
            "dynamicSegment": t.proxy(renames["DynamicSegmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["GoalDataIn"] = t.struct(
        {
            "goalValue": t.number().optional(),
            "goalIndex": t.integer().optional(),
            "goalCompletions": t.string().optional(),
            "goalPreviousStep1": t.string().optional(),
            "goalPreviousStep2": t.string().optional(),
            "goalCompletionLocation": t.string().optional(),
            "goalPreviousStep3": t.string().optional(),
            "goalName": t.string().optional(),
        }
    ).named(renames["GoalDataIn"])
    types["GoalDataOut"] = t.struct(
        {
            "goalValue": t.number().optional(),
            "goalIndex": t.integer().optional(),
            "goalCompletions": t.string().optional(),
            "goalPreviousStep1": t.string().optional(),
            "goalPreviousStep2": t.string().optional(),
            "goalCompletionLocation": t.string().optional(),
            "goalPreviousStep3": t.string().optional(),
            "goalName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalDataOut"])
    types["PivotHeaderEntryIn"] = t.struct(
        {
            "metric": t.proxy(renames["MetricHeaderEntryIn"]).optional(),
            "dimensionValues": t.array(t.string()).optional(),
            "dimensionNames": t.array(t.string()).optional(),
        }
    ).named(renames["PivotHeaderEntryIn"])
    types["PivotHeaderEntryOut"] = t.struct(
        {
            "metric": t.proxy(renames["MetricHeaderEntryOut"]).optional(),
            "dimensionValues": t.array(t.string()).optional(),
            "dimensionNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotHeaderEntryOut"])
    types["ReportRequestIn"] = t.struct(
        {
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "viewId": t.string().optional(),
            "hideValueRanges": t.boolean().optional(),
            "includeEmptyRows": t.boolean().optional(),
            "samplingLevel": t.string().optional(),
            "hideTotals": t.boolean().optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseIn"])
            ).optional(),
            "pageSize": t.integer().optional(),
            "filtersExpression": t.string().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "cohortGroup": t.proxy(renames["CohortGroupIn"]).optional(),
            "segments": t.array(t.proxy(renames["SegmentIn"])).optional(),
            "pageToken": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseIn"])
            ).optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "viewId": t.string().optional(),
            "hideValueRanges": t.boolean().optional(),
            "includeEmptyRows": t.boolean().optional(),
            "samplingLevel": t.string().optional(),
            "hideTotals": t.boolean().optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseOut"])
            ).optional(),
            "pageSize": t.integer().optional(),
            "filtersExpression": t.string().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "cohortGroup": t.proxy(renames["CohortGroupOut"]).optional(),
            "segments": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "pageToken": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])
    types["SegmentFilterClauseIn"] = t.struct(
        {
            "metricFilter": t.proxy(renames["SegmentMetricFilterIn"]).optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterIn"]).optional(),
            "not": t.boolean().optional(),
        }
    ).named(renames["SegmentFilterClauseIn"])
    types["SegmentFilterClauseOut"] = t.struct(
        {
            "metricFilter": t.proxy(renames["SegmentMetricFilterOut"]).optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterOut"]).optional(),
            "not": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentFilterClauseOut"])
    types["MetricHeaderEntryIn"] = t.struct(
        {"type": t.string().optional(), "name": t.string().optional()}
    ).named(renames["MetricHeaderEntryIn"])
    types["MetricHeaderEntryOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricHeaderEntryOut"])

    functions = {}
    functions["userActivitySearch"] = analyticsreporting.post(
        "v4/userActivity:search",
        t.struct(
            {
                "viewId": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "user": t.proxy(renames["UserIn"]),
                "activityTypes": t.array(t.string()).optional(),
                "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchUserActivityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportsBatchGet"] = analyticsreporting.post(
        "v4/reports:batchGet",
        t.struct(
            {
                "reportRequests": t.array(
                    t.proxy(renames["ReportRequestIn"])
                ).optional(),
                "useResourceQuotas": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticsreporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
