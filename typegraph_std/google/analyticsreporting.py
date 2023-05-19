from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_analyticsreporting() -> Import:
    analyticsreporting = HTTPRuntime("https://analyticsreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsreporting_1_ErrorResponse",
        "PivotHeaderEntryIn": "_analyticsreporting_2_PivotHeaderEntryIn",
        "PivotHeaderEntryOut": "_analyticsreporting_3_PivotHeaderEntryOut",
        "TransactionDataIn": "_analyticsreporting_4_TransactionDataIn",
        "TransactionDataOut": "_analyticsreporting_5_TransactionDataOut",
        "DynamicSegmentIn": "_analyticsreporting_6_DynamicSegmentIn",
        "DynamicSegmentOut": "_analyticsreporting_7_DynamicSegmentOut",
        "MetricHeaderIn": "_analyticsreporting_8_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsreporting_9_MetricHeaderOut",
        "SimpleSegmentIn": "_analyticsreporting_10_SimpleSegmentIn",
        "SimpleSegmentOut": "_analyticsreporting_11_SimpleSegmentOut",
        "ReportDataIn": "_analyticsreporting_12_ReportDataIn",
        "ReportDataOut": "_analyticsreporting_13_ReportDataOut",
        "SegmentDefinitionIn": "_analyticsreporting_14_SegmentDefinitionIn",
        "SegmentDefinitionOut": "_analyticsreporting_15_SegmentDefinitionOut",
        "EcommerceDataIn": "_analyticsreporting_16_EcommerceDataIn",
        "EcommerceDataOut": "_analyticsreporting_17_EcommerceDataOut",
        "EventDataIn": "_analyticsreporting_18_EventDataIn",
        "EventDataOut": "_analyticsreporting_19_EventDataOut",
        "SegmentMetricFilterIn": "_analyticsreporting_20_SegmentMetricFilterIn",
        "SegmentMetricFilterOut": "_analyticsreporting_21_SegmentMetricFilterOut",
        "DateRangeIn": "_analyticsreporting_22_DateRangeIn",
        "DateRangeOut": "_analyticsreporting_23_DateRangeOut",
        "MetricHeaderEntryIn": "_analyticsreporting_24_MetricHeaderEntryIn",
        "MetricHeaderEntryOut": "_analyticsreporting_25_MetricHeaderEntryOut",
        "SegmentDimensionFilterIn": "_analyticsreporting_26_SegmentDimensionFilterIn",
        "SegmentDimensionFilterOut": "_analyticsreporting_27_SegmentDimensionFilterOut",
        "DimensionFilterIn": "_analyticsreporting_28_DimensionFilterIn",
        "DimensionFilterOut": "_analyticsreporting_29_DimensionFilterOut",
        "GetReportsResponseIn": "_analyticsreporting_30_GetReportsResponseIn",
        "GetReportsResponseOut": "_analyticsreporting_31_GetReportsResponseOut",
        "SegmentIn": "_analyticsreporting_32_SegmentIn",
        "SegmentOut": "_analyticsreporting_33_SegmentOut",
        "ReportIn": "_analyticsreporting_34_ReportIn",
        "ReportOut": "_analyticsreporting_35_ReportOut",
        "MetricFilterIn": "_analyticsreporting_36_MetricFilterIn",
        "MetricFilterOut": "_analyticsreporting_37_MetricFilterOut",
        "SegmentSequenceStepIn": "_analyticsreporting_38_SegmentSequenceStepIn",
        "SegmentSequenceStepOut": "_analyticsreporting_39_SegmentSequenceStepOut",
        "CohortGroupIn": "_analyticsreporting_40_CohortGroupIn",
        "CohortGroupOut": "_analyticsreporting_41_CohortGroupOut",
        "GoalSetDataIn": "_analyticsreporting_42_GoalSetDataIn",
        "GoalSetDataOut": "_analyticsreporting_43_GoalSetDataOut",
        "MetricIn": "_analyticsreporting_44_MetricIn",
        "MetricOut": "_analyticsreporting_45_MetricOut",
        "ReportRowIn": "_analyticsreporting_46_ReportRowIn",
        "ReportRowOut": "_analyticsreporting_47_ReportRowOut",
        "ActivityIn": "_analyticsreporting_48_ActivityIn",
        "ActivityOut": "_analyticsreporting_49_ActivityOut",
        "PivotValueRegionIn": "_analyticsreporting_50_PivotValueRegionIn",
        "PivotValueRegionOut": "_analyticsreporting_51_PivotValueRegionOut",
        "DimensionIn": "_analyticsreporting_52_DimensionIn",
        "DimensionOut": "_analyticsreporting_53_DimensionOut",
        "SearchUserActivityRequestIn": "_analyticsreporting_54_SearchUserActivityRequestIn",
        "SearchUserActivityRequestOut": "_analyticsreporting_55_SearchUserActivityRequestOut",
        "SegmentFilterIn": "_analyticsreporting_56_SegmentFilterIn",
        "SegmentFilterOut": "_analyticsreporting_57_SegmentFilterOut",
        "MetricFilterClauseIn": "_analyticsreporting_58_MetricFilterClauseIn",
        "MetricFilterClauseOut": "_analyticsreporting_59_MetricFilterClauseOut",
        "GetReportsRequestIn": "_analyticsreporting_60_GetReportsRequestIn",
        "GetReportsRequestOut": "_analyticsreporting_61_GetReportsRequestOut",
        "SegmentFilterClauseIn": "_analyticsreporting_62_SegmentFilterClauseIn",
        "SegmentFilterClauseOut": "_analyticsreporting_63_SegmentFilterClauseOut",
        "PageviewDataIn": "_analyticsreporting_64_PageviewDataIn",
        "PageviewDataOut": "_analyticsreporting_65_PageviewDataOut",
        "SearchUserActivityResponseIn": "_analyticsreporting_66_SearchUserActivityResponseIn",
        "SearchUserActivityResponseOut": "_analyticsreporting_67_SearchUserActivityResponseOut",
        "CustomDimensionIn": "_analyticsreporting_68_CustomDimensionIn",
        "CustomDimensionOut": "_analyticsreporting_69_CustomDimensionOut",
        "PivotHeaderIn": "_analyticsreporting_70_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsreporting_71_PivotHeaderOut",
        "ReportRequestIn": "_analyticsreporting_72_ReportRequestIn",
        "ReportRequestOut": "_analyticsreporting_73_ReportRequestOut",
        "GoalDataIn": "_analyticsreporting_74_GoalDataIn",
        "GoalDataOut": "_analyticsreporting_75_GoalDataOut",
        "DateRangeValuesIn": "_analyticsreporting_76_DateRangeValuesIn",
        "DateRangeValuesOut": "_analyticsreporting_77_DateRangeValuesOut",
        "ProductDataIn": "_analyticsreporting_78_ProductDataIn",
        "ProductDataOut": "_analyticsreporting_79_ProductDataOut",
        "OrderByIn": "_analyticsreporting_80_OrderByIn",
        "OrderByOut": "_analyticsreporting_81_OrderByOut",
        "UserIn": "_analyticsreporting_82_UserIn",
        "UserOut": "_analyticsreporting_83_UserOut",
        "ResourceQuotasRemainingIn": "_analyticsreporting_84_ResourceQuotasRemainingIn",
        "ResourceQuotasRemainingOut": "_analyticsreporting_85_ResourceQuotasRemainingOut",
        "DimensionFilterClauseIn": "_analyticsreporting_86_DimensionFilterClauseIn",
        "DimensionFilterClauseOut": "_analyticsreporting_87_DimensionFilterClauseOut",
        "UserActivitySessionIn": "_analyticsreporting_88_UserActivitySessionIn",
        "UserActivitySessionOut": "_analyticsreporting_89_UserActivitySessionOut",
        "OrFiltersForSegmentIn": "_analyticsreporting_90_OrFiltersForSegmentIn",
        "OrFiltersForSegmentOut": "_analyticsreporting_91_OrFiltersForSegmentOut",
        "SequenceSegmentIn": "_analyticsreporting_92_SequenceSegmentIn",
        "SequenceSegmentOut": "_analyticsreporting_93_SequenceSegmentOut",
        "ColumnHeaderIn": "_analyticsreporting_94_ColumnHeaderIn",
        "ColumnHeaderOut": "_analyticsreporting_95_ColumnHeaderOut",
        "CohortIn": "_analyticsreporting_96_CohortIn",
        "CohortOut": "_analyticsreporting_97_CohortOut",
        "ScreenviewDataIn": "_analyticsreporting_98_ScreenviewDataIn",
        "ScreenviewDataOut": "_analyticsreporting_99_ScreenviewDataOut",
        "PivotIn": "_analyticsreporting_100_PivotIn",
        "PivotOut": "_analyticsreporting_101_PivotOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PivotHeaderEntryIn"] = t.struct(
        {
            "metric": t.proxy(renames["MetricHeaderEntryIn"]).optional(),
            "dimensionNames": t.array(t.string()).optional(),
            "dimensionValues": t.array(t.string()).optional(),
        }
    ).named(renames["PivotHeaderEntryIn"])
    types["PivotHeaderEntryOut"] = t.struct(
        {
            "metric": t.proxy(renames["MetricHeaderEntryOut"]).optional(),
            "dimensionNames": t.array(t.string()).optional(),
            "dimensionValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotHeaderEntryOut"])
    types["TransactionDataIn"] = t.struct(
        {
            "transactionTax": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionShipping": t.number().optional(),
            "transactionRevenue": t.number().optional(),
        }
    ).named(renames["TransactionDataIn"])
    types["TransactionDataOut"] = t.struct(
        {
            "transactionTax": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionShipping": t.number().optional(),
            "transactionRevenue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionDataOut"])
    types["DynamicSegmentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sessionSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
            "userSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
        }
    ).named(renames["DynamicSegmentIn"])
    types["DynamicSegmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sessionSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "userSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicSegmentOut"])
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
    types["ReportDataIn"] = t.struct(
        {
            "isDataGolden": t.boolean().optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "dataLastRefreshed": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowIn"])).optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
            "emptyReason": t.string().optional(),
            "rowCount": t.integer().optional(),
            "maximums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
        }
    ).named(renames["ReportDataIn"])
    types["ReportDataOut"] = t.struct(
        {
            "isDataGolden": t.boolean().optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "dataLastRefreshed": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
            "emptyReason": t.string().optional(),
            "rowCount": t.integer().optional(),
            "maximums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportDataOut"])
    types["SegmentDefinitionIn"] = t.struct(
        {"segmentFilters": t.array(t.proxy(renames["SegmentFilterIn"])).optional()}
    ).named(renames["SegmentDefinitionIn"])
    types["SegmentDefinitionOut"] = t.struct(
        {
            "segmentFilters": t.array(t.proxy(renames["SegmentFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentDefinitionOut"])
    types["EcommerceDataIn"] = t.struct(
        {
            "ecommerceType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataIn"])).optional(),
            "transaction": t.proxy(renames["TransactionDataIn"]).optional(),
            "actionType": t.string().optional(),
        }
    ).named(renames["EcommerceDataIn"])
    types["EcommerceDataOut"] = t.struct(
        {
            "ecommerceType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataOut"])).optional(),
            "transaction": t.proxy(renames["TransactionDataOut"]).optional(),
            "actionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcommerceDataOut"])
    types["EventDataIn"] = t.struct(
        {
            "eventAction": t.string().optional(),
            "eventCount": t.string().optional(),
            "eventLabel": t.string().optional(),
            "eventCategory": t.string().optional(),
            "eventValue": t.string().optional(),
        }
    ).named(renames["EventDataIn"])
    types["EventDataOut"] = t.struct(
        {
            "eventAction": t.string().optional(),
            "eventCount": t.string().optional(),
            "eventLabel": t.string().optional(),
            "eventCategory": t.string().optional(),
            "eventValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDataOut"])
    types["SegmentMetricFilterIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "operator": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "metricName": t.string().optional(),
        }
    ).named(renames["SegmentMetricFilterIn"])
    types["SegmentMetricFilterOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "operator": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentMetricFilterOut"])
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
    types["MetricHeaderEntryIn"] = t.struct(
        {"name": t.string().optional(), "type": t.string().optional()}
    ).named(renames["MetricHeaderEntryIn"])
    types["MetricHeaderEntryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricHeaderEntryOut"])
    types["SegmentDimensionFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "expressions": t.array(t.string()).optional(),
            "maxComparisonValue": t.string().optional(),
            "minComparisonValue": t.string().optional(),
            "dimensionName": t.string().optional(),
        }
    ).named(renames["SegmentDimensionFilterIn"])
    types["SegmentDimensionFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "expressions": t.array(t.string()).optional(),
            "maxComparisonValue": t.string().optional(),
            "minComparisonValue": t.string().optional(),
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentDimensionFilterOut"])
    types["DimensionFilterIn"] = t.struct(
        {
            "not": t.boolean().optional(),
            "operator": t.string().optional(),
            "dimensionName": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "caseSensitive": t.boolean().optional(),
        }
    ).named(renames["DimensionFilterIn"])
    types["DimensionFilterOut"] = t.struct(
        {
            "not": t.boolean().optional(),
            "operator": t.string().optional(),
            "dimensionName": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "caseSensitive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionFilterOut"])
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
    types["SegmentIn"] = t.struct(
        {
            "dynamicSegment": t.proxy(renames["DynamicSegmentIn"]).optional(),
            "segmentId": t.string().optional(),
        }
    ).named(renames["SegmentIn"])
    types["SegmentOut"] = t.struct(
        {
            "dynamicSegment": t.proxy(renames["DynamicSegmentOut"]).optional(),
            "segmentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentOut"])
    types["ReportIn"] = t.struct(
        {
            "columnHeader": t.proxy(renames["ColumnHeaderIn"]).optional(),
            "data": t.proxy(renames["ReportDataIn"]).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "columnHeader": t.proxy(renames["ColumnHeaderOut"]).optional(),
            "data": t.proxy(renames["ReportDataOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["MetricFilterIn"] = t.struct(
        {
            "metricName": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "not": t.boolean().optional(),
            "operator": t.string().optional(),
        }
    ).named(renames["MetricFilterIn"])
    types["MetricFilterOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "not": t.boolean().optional(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricFilterOut"])
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
    types["CohortGroupIn"] = t.struct(
        {
            "cohorts": t.array(t.proxy(renames["CohortIn"])).optional(),
            "lifetimeValue": t.boolean().optional(),
        }
    ).named(renames["CohortGroupIn"])
    types["CohortGroupOut"] = t.struct(
        {
            "cohorts": t.array(t.proxy(renames["CohortOut"])).optional(),
            "lifetimeValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortGroupOut"])
    types["GoalSetDataIn"] = t.struct(
        {"goals": t.array(t.proxy(renames["GoalDataIn"])).optional()}
    ).named(renames["GoalSetDataIn"])
    types["GoalSetDataOut"] = t.struct(
        {
            "goals": t.array(t.proxy(renames["GoalDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalSetDataOut"])
    types["MetricIn"] = t.struct(
        {
            "alias": t.string().optional(),
            "expression": t.string().optional(),
            "formattingType": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "alias": t.string().optional(),
            "expression": t.string().optional(),
            "formattingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
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
    types["ActivityIn"] = t.struct(
        {
            "ecommerce": t.proxy(renames["EcommerceDataIn"]).optional(),
            "channelGrouping": t.string().optional(),
            "activityType": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionIn"])
            ).optional(),
            "campaign": t.string().optional(),
            "appview": t.proxy(renames["ScreenviewDataIn"]).optional(),
            "landingPagePath": t.string().optional(),
            "pageview": t.proxy(renames["PageviewDataIn"]).optional(),
            "hostname": t.string().optional(),
            "event": t.proxy(renames["EventDataIn"]).optional(),
            "goals": t.proxy(renames["GoalSetDataIn"]).optional(),
            "medium": t.string().optional(),
            "keyword": t.string().optional(),
            "activityTime": t.string().optional(),
            "source": t.string().optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "ecommerce": t.proxy(renames["EcommerceDataOut"]).optional(),
            "channelGrouping": t.string().optional(),
            "activityType": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionOut"])
            ).optional(),
            "campaign": t.string().optional(),
            "appview": t.proxy(renames["ScreenviewDataOut"]).optional(),
            "landingPagePath": t.string().optional(),
            "pageview": t.proxy(renames["PageviewDataOut"]).optional(),
            "hostname": t.string().optional(),
            "event": t.proxy(renames["EventDataOut"]).optional(),
            "goals": t.proxy(renames["GoalSetDataOut"]).optional(),
            "medium": t.string().optional(),
            "keyword": t.string().optional(),
            "activityTime": t.string().optional(),
            "source": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
    types["PivotValueRegionIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["PivotValueRegionIn"])
    types["PivotValueRegionOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueRegionOut"])
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
    types["SearchUserActivityRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "viewId": t.string(),
            "activityTypes": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "user": t.proxy(renames["UserIn"]),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["SearchUserActivityRequestIn"])
    types["SearchUserActivityRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "viewId": t.string(),
            "activityTypes": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "user": t.proxy(renames["UserOut"]),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityRequestOut"])
    types["SegmentFilterIn"] = t.struct(
        {
            "sequenceSegment": t.proxy(renames["SequenceSegmentIn"]).optional(),
            "simpleSegment": t.proxy(renames["SimpleSegmentIn"]).optional(),
            "not": t.boolean().optional(),
        }
    ).named(renames["SegmentFilterIn"])
    types["SegmentFilterOut"] = t.struct(
        {
            "sequenceSegment": t.proxy(renames["SequenceSegmentOut"]).optional(),
            "simpleSegment": t.proxy(renames["SimpleSegmentOut"]).optional(),
            "not": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentFilterOut"])
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
    types["SegmentFilterClauseIn"] = t.struct(
        {
            "not": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterIn"]).optional(),
            "metricFilter": t.proxy(renames["SegmentMetricFilterIn"]).optional(),
        }
    ).named(renames["SegmentFilterClauseIn"])
    types["SegmentFilterClauseOut"] = t.struct(
        {
            "not": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterOut"]).optional(),
            "metricFilter": t.proxy(renames["SegmentMetricFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentFilterClauseOut"])
    types["PageviewDataIn"] = t.struct(
        {"pageTitle": t.string().optional(), "pagePath": t.string().optional()}
    ).named(renames["PageviewDataIn"])
    types["PageviewDataOut"] = t.struct(
        {
            "pageTitle": t.string().optional(),
            "pagePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageviewDataOut"])
    types["SearchUserActivityResponseIn"] = t.struct(
        {
            "sessions": t.array(t.proxy(renames["UserActivitySessionIn"])).optional(),
            "totalRows": t.integer().optional(),
            "sampleRate": t.number().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchUserActivityResponseIn"])
    types["SearchUserActivityResponseOut"] = t.struct(
        {
            "sessions": t.array(t.proxy(renames["UserActivitySessionOut"])).optional(),
            "totalRows": t.integer().optional(),
            "sampleRate": t.number().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityResponseOut"])
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
    types["PivotHeaderIn"] = t.struct(
        {
            "totalPivotGroupsCount": t.integer().optional(),
            "pivotHeaderEntries": t.array(
                t.proxy(renames["PivotHeaderEntryIn"])
            ).optional(),
        }
    ).named(renames["PivotHeaderIn"])
    types["PivotHeaderOut"] = t.struct(
        {
            "totalPivotGroupsCount": t.integer().optional(),
            "pivotHeaderEntries": t.array(
                t.proxy(renames["PivotHeaderEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotHeaderOut"])
    types["ReportRequestIn"] = t.struct(
        {
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "cohortGroup": t.proxy(renames["CohortGroupIn"]).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseIn"])
            ).optional(),
            "hideTotals": t.boolean().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "segments": t.array(t.proxy(renames["SegmentIn"])).optional(),
            "viewId": t.string().optional(),
            "includeEmptyRows": t.boolean().optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseIn"])
            ).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "pageSize": t.integer().optional(),
            "samplingLevel": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "filtersExpression": t.string().optional(),
            "pageToken": t.string().optional(),
            "hideValueRanges": t.boolean().optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "cohortGroup": t.proxy(renames["CohortGroupOut"]).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseOut"])
            ).optional(),
            "hideTotals": t.boolean().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "segments": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "viewId": t.string().optional(),
            "includeEmptyRows": t.boolean().optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseOut"])
            ).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "pageSize": t.integer().optional(),
            "samplingLevel": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "filtersExpression": t.string().optional(),
            "pageToken": t.string().optional(),
            "hideValueRanges": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])
    types["GoalDataIn"] = t.struct(
        {
            "goalPreviousStep1": t.string().optional(),
            "goalCompletionLocation": t.string().optional(),
            "goalName": t.string().optional(),
            "goalPreviousStep3": t.string().optional(),
            "goalPreviousStep2": t.string().optional(),
            "goalValue": t.number().optional(),
            "goalCompletions": t.string().optional(),
            "goalIndex": t.integer().optional(),
        }
    ).named(renames["GoalDataIn"])
    types["GoalDataOut"] = t.struct(
        {
            "goalPreviousStep1": t.string().optional(),
            "goalCompletionLocation": t.string().optional(),
            "goalName": t.string().optional(),
            "goalPreviousStep3": t.string().optional(),
            "goalPreviousStep2": t.string().optional(),
            "goalValue": t.number().optional(),
            "goalCompletions": t.string().optional(),
            "goalIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalDataOut"])
    types["DateRangeValuesIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "pivotValueRegions": t.array(
                t.proxy(renames["PivotValueRegionIn"])
            ).optional(),
        }
    ).named(renames["DateRangeValuesIn"])
    types["DateRangeValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "pivotValueRegions": t.array(
                t.proxy(renames["PivotValueRegionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeValuesOut"])
    types["ProductDataIn"] = t.struct(
        {
            "productSku": t.string().optional(),
            "itemRevenue": t.number().optional(),
            "productQuantity": t.string().optional(),
            "productName": t.string().optional(),
        }
    ).named(renames["ProductDataIn"])
    types["ProductDataOut"] = t.struct(
        {
            "productSku": t.string().optional(),
            "itemRevenue": t.number().optional(),
            "productQuantity": t.string().optional(),
            "productName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDataOut"])
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
    types["ResourceQuotasRemainingIn"] = t.struct(
        {
            "dailyQuotaTokensRemaining": t.integer().optional(),
            "hourlyQuotaTokensRemaining": t.integer().optional(),
        }
    ).named(renames["ResourceQuotasRemainingIn"])
    types["ResourceQuotasRemainingOut"] = t.struct(
        {
            "dailyQuotaTokensRemaining": t.integer().optional(),
            "hourlyQuotaTokensRemaining": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceQuotasRemainingOut"])
    types["DimensionFilterClauseIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "filters": t.array(t.proxy(renames["DimensionFilterIn"])).optional(),
        }
    ).named(renames["DimensionFilterClauseIn"])
    types["DimensionFilterClauseOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "filters": t.array(t.proxy(renames["DimensionFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionFilterClauseOut"])
    types["UserActivitySessionIn"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["ActivityIn"])).optional(),
            "platform": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "dataSource": t.string().optional(),
            "sessionDate": t.string().optional(),
            "sessionId": t.string().optional(),
        }
    ).named(renames["UserActivitySessionIn"])
    types["UserActivitySessionOut"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["ActivityOut"])).optional(),
            "platform": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "dataSource": t.string().optional(),
            "sessionDate": t.string().optional(),
            "sessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserActivitySessionOut"])
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
    types["CohortIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["CohortIn"])
    types["CohortOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortOut"])
    types["ScreenviewDataIn"] = t.struct(
        {
            "screenName": t.string().optional(),
            "mobileDeviceBranding": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
            "appName": t.string().optional(),
        }
    ).named(renames["ScreenviewDataIn"])
    types["ScreenviewDataOut"] = t.struct(
        {
            "screenName": t.string().optional(),
            "mobileDeviceBranding": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
            "appName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenviewDataOut"])
    types["PivotIn"] = t.struct(
        {
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseIn"])
            ).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "startGroup": t.integer().optional(),
            "maxGroupCount": t.integer().optional(),
        }
    ).named(renames["PivotIn"])
    types["PivotOut"] = t.struct(
        {
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseOut"])
            ).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "startGroup": t.integer().optional(),
            "maxGroupCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOut"])

    functions = {}
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
    functions["userActivitySearch"] = analyticsreporting.post(
        "v4/userActivity:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "viewId": t.string(),
                "activityTypes": t.array(t.string()).optional(),
                "pageToken": t.string().optional(),
                "user": t.proxy(renames["UserIn"]),
                "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchUserActivityResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticsreporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
