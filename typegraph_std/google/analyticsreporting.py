from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_analyticsreporting() -> Import:
    analyticsreporting = HTTPRuntime("https://analyticsreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsreporting_1_ErrorResponse",
        "DateRangeValuesIn": "_analyticsreporting_2_DateRangeValuesIn",
        "DateRangeValuesOut": "_analyticsreporting_3_DateRangeValuesOut",
        "SearchUserActivityResponseIn": "_analyticsreporting_4_SearchUserActivityResponseIn",
        "SearchUserActivityResponseOut": "_analyticsreporting_5_SearchUserActivityResponseOut",
        "SimpleSegmentIn": "_analyticsreporting_6_SimpleSegmentIn",
        "SimpleSegmentOut": "_analyticsreporting_7_SimpleSegmentOut",
        "DateRangeIn": "_analyticsreporting_8_DateRangeIn",
        "DateRangeOut": "_analyticsreporting_9_DateRangeOut",
        "DimensionFilterClauseIn": "_analyticsreporting_10_DimensionFilterClauseIn",
        "DimensionFilterClauseOut": "_analyticsreporting_11_DimensionFilterClauseOut",
        "MetricFilterIn": "_analyticsreporting_12_MetricFilterIn",
        "MetricFilterOut": "_analyticsreporting_13_MetricFilterOut",
        "GoalSetDataIn": "_analyticsreporting_14_GoalSetDataIn",
        "GoalSetDataOut": "_analyticsreporting_15_GoalSetDataOut",
        "ScreenviewDataIn": "_analyticsreporting_16_ScreenviewDataIn",
        "ScreenviewDataOut": "_analyticsreporting_17_ScreenviewDataOut",
        "PivotHeaderIn": "_analyticsreporting_18_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsreporting_19_PivotHeaderOut",
        "DimensionIn": "_analyticsreporting_20_DimensionIn",
        "DimensionOut": "_analyticsreporting_21_DimensionOut",
        "MetricFilterClauseIn": "_analyticsreporting_22_MetricFilterClauseIn",
        "MetricFilterClauseOut": "_analyticsreporting_23_MetricFilterClauseOut",
        "ResourceQuotasRemainingIn": "_analyticsreporting_24_ResourceQuotasRemainingIn",
        "ResourceQuotasRemainingOut": "_analyticsreporting_25_ResourceQuotasRemainingOut",
        "SegmentDimensionFilterIn": "_analyticsreporting_26_SegmentDimensionFilterIn",
        "SegmentDimensionFilterOut": "_analyticsreporting_27_SegmentDimensionFilterOut",
        "SegmentMetricFilterIn": "_analyticsreporting_28_SegmentMetricFilterIn",
        "SegmentMetricFilterOut": "_analyticsreporting_29_SegmentMetricFilterOut",
        "ProductDataIn": "_analyticsreporting_30_ProductDataIn",
        "ProductDataOut": "_analyticsreporting_31_ProductDataOut",
        "PivotIn": "_analyticsreporting_32_PivotIn",
        "PivotOut": "_analyticsreporting_33_PivotOut",
        "CustomDimensionIn": "_analyticsreporting_34_CustomDimensionIn",
        "CustomDimensionOut": "_analyticsreporting_35_CustomDimensionOut",
        "TransactionDataIn": "_analyticsreporting_36_TransactionDataIn",
        "TransactionDataOut": "_analyticsreporting_37_TransactionDataOut",
        "SequenceSegmentIn": "_analyticsreporting_38_SequenceSegmentIn",
        "SequenceSegmentOut": "_analyticsreporting_39_SequenceSegmentOut",
        "SegmentIn": "_analyticsreporting_40_SegmentIn",
        "SegmentOut": "_analyticsreporting_41_SegmentOut",
        "SegmentFilterClauseIn": "_analyticsreporting_42_SegmentFilterClauseIn",
        "SegmentFilterClauseOut": "_analyticsreporting_43_SegmentFilterClauseOut",
        "EcommerceDataIn": "_analyticsreporting_44_EcommerceDataIn",
        "EcommerceDataOut": "_analyticsreporting_45_EcommerceDataOut",
        "OrderByIn": "_analyticsreporting_46_OrderByIn",
        "OrderByOut": "_analyticsreporting_47_OrderByOut",
        "SegmentSequenceStepIn": "_analyticsreporting_48_SegmentSequenceStepIn",
        "SegmentSequenceStepOut": "_analyticsreporting_49_SegmentSequenceStepOut",
        "CohortIn": "_analyticsreporting_50_CohortIn",
        "CohortOut": "_analyticsreporting_51_CohortOut",
        "ReportRowIn": "_analyticsreporting_52_ReportRowIn",
        "ReportRowOut": "_analyticsreporting_53_ReportRowOut",
        "PivotValueRegionIn": "_analyticsreporting_54_PivotValueRegionIn",
        "PivotValueRegionOut": "_analyticsreporting_55_PivotValueRegionOut",
        "SegmentFilterIn": "_analyticsreporting_56_SegmentFilterIn",
        "SegmentFilterOut": "_analyticsreporting_57_SegmentFilterOut",
        "MetricHeaderIn": "_analyticsreporting_58_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsreporting_59_MetricHeaderOut",
        "ReportIn": "_analyticsreporting_60_ReportIn",
        "ReportOut": "_analyticsreporting_61_ReportOut",
        "ReportDataIn": "_analyticsreporting_62_ReportDataIn",
        "ReportDataOut": "_analyticsreporting_63_ReportDataOut",
        "PivotHeaderEntryIn": "_analyticsreporting_64_PivotHeaderEntryIn",
        "PivotHeaderEntryOut": "_analyticsreporting_65_PivotHeaderEntryOut",
        "GetReportsRequestIn": "_analyticsreporting_66_GetReportsRequestIn",
        "GetReportsRequestOut": "_analyticsreporting_67_GetReportsRequestOut",
        "ColumnHeaderIn": "_analyticsreporting_68_ColumnHeaderIn",
        "ColumnHeaderOut": "_analyticsreporting_69_ColumnHeaderOut",
        "ReportRequestIn": "_analyticsreporting_70_ReportRequestIn",
        "ReportRequestOut": "_analyticsreporting_71_ReportRequestOut",
        "OrFiltersForSegmentIn": "_analyticsreporting_72_OrFiltersForSegmentIn",
        "OrFiltersForSegmentOut": "_analyticsreporting_73_OrFiltersForSegmentOut",
        "GetReportsResponseIn": "_analyticsreporting_74_GetReportsResponseIn",
        "GetReportsResponseOut": "_analyticsreporting_75_GetReportsResponseOut",
        "EventDataIn": "_analyticsreporting_76_EventDataIn",
        "EventDataOut": "_analyticsreporting_77_EventDataOut",
        "PageviewDataIn": "_analyticsreporting_78_PageviewDataIn",
        "PageviewDataOut": "_analyticsreporting_79_PageviewDataOut",
        "MetricHeaderEntryIn": "_analyticsreporting_80_MetricHeaderEntryIn",
        "MetricHeaderEntryOut": "_analyticsreporting_81_MetricHeaderEntryOut",
        "UserActivitySessionIn": "_analyticsreporting_82_UserActivitySessionIn",
        "UserActivitySessionOut": "_analyticsreporting_83_UserActivitySessionOut",
        "MetricIn": "_analyticsreporting_84_MetricIn",
        "MetricOut": "_analyticsreporting_85_MetricOut",
        "CohortGroupIn": "_analyticsreporting_86_CohortGroupIn",
        "CohortGroupOut": "_analyticsreporting_87_CohortGroupOut",
        "ActivityIn": "_analyticsreporting_88_ActivityIn",
        "ActivityOut": "_analyticsreporting_89_ActivityOut",
        "GoalDataIn": "_analyticsreporting_90_GoalDataIn",
        "GoalDataOut": "_analyticsreporting_91_GoalDataOut",
        "DimensionFilterIn": "_analyticsreporting_92_DimensionFilterIn",
        "DimensionFilterOut": "_analyticsreporting_93_DimensionFilterOut",
        "SegmentDefinitionIn": "_analyticsreporting_94_SegmentDefinitionIn",
        "SegmentDefinitionOut": "_analyticsreporting_95_SegmentDefinitionOut",
        "UserIn": "_analyticsreporting_96_UserIn",
        "UserOut": "_analyticsreporting_97_UserOut",
        "DynamicSegmentIn": "_analyticsreporting_98_DynamicSegmentIn",
        "DynamicSegmentOut": "_analyticsreporting_99_DynamicSegmentOut",
        "SearchUserActivityRequestIn": "_analyticsreporting_100_SearchUserActivityRequestIn",
        "SearchUserActivityRequestOut": "_analyticsreporting_101_SearchUserActivityRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SearchUserActivityResponseIn"] = t.struct(
        {
            "totalRows": t.integer().optional(),
            "sessions": t.array(t.proxy(renames["UserActivitySessionIn"])).optional(),
            "sampleRate": t.number().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchUserActivityResponseIn"])
    types["SearchUserActivityResponseOut"] = t.struct(
        {
            "totalRows": t.integer().optional(),
            "sessions": t.array(t.proxy(renames["UserActivitySessionOut"])).optional(),
            "sampleRate": t.number().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityResponseOut"])
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
    types["DateRangeIn"] = t.struct(
        {"endDate": t.string().optional(), "startDate": t.string().optional()}
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
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
    types["MetricFilterIn"] = t.struct(
        {
            "metricName": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "operator": t.string().optional(),
            "not": t.boolean().optional(),
        }
    ).named(renames["MetricFilterIn"])
    types["MetricFilterOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "operator": t.string().optional(),
            "not": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricFilterOut"])
    types["GoalSetDataIn"] = t.struct(
        {"goals": t.array(t.proxy(renames["GoalDataIn"])).optional()}
    ).named(renames["GoalSetDataIn"])
    types["GoalSetDataOut"] = t.struct(
        {
            "goals": t.array(t.proxy(renames["GoalDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalSetDataOut"])
    types["ScreenviewDataIn"] = t.struct(
        {
            "screenName": t.string().optional(),
            "appName": t.string().optional(),
            "mobileDeviceBranding": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
        }
    ).named(renames["ScreenviewDataIn"])
    types["ScreenviewDataOut"] = t.struct(
        {
            "screenName": t.string().optional(),
            "appName": t.string().optional(),
            "mobileDeviceBranding": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenviewDataOut"])
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
    types["DimensionIn"] = t.struct(
        {
            "histogramBuckets": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "histogramBuckets": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
    types["MetricFilterClauseIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "filters": t.array(t.proxy(renames["MetricFilterIn"])).optional(),
        }
    ).named(renames["MetricFilterClauseIn"])
    types["MetricFilterClauseOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "filters": t.array(t.proxy(renames["MetricFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricFilterClauseOut"])
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
    types["SegmentDimensionFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "minComparisonValue": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "dimensionName": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
        }
    ).named(renames["SegmentDimensionFilterIn"])
    types["SegmentDimensionFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "minComparisonValue": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "dimensionName": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentDimensionFilterOut"])
    types["SegmentMetricFilterIn"] = t.struct(
        {
            "comparisonValue": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "scope": t.string().optional(),
            "operator": t.string().optional(),
            "metricName": t.string().optional(),
        }
    ).named(renames["SegmentMetricFilterIn"])
    types["SegmentMetricFilterOut"] = t.struct(
        {
            "comparisonValue": t.string().optional(),
            "maxComparisonValue": t.string().optional(),
            "scope": t.string().optional(),
            "operator": t.string().optional(),
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentMetricFilterOut"])
    types["ProductDataIn"] = t.struct(
        {
            "productQuantity": t.string().optional(),
            "itemRevenue": t.number().optional(),
            "productName": t.string().optional(),
            "productSku": t.string().optional(),
        }
    ).named(renames["ProductDataIn"])
    types["ProductDataOut"] = t.struct(
        {
            "productQuantity": t.string().optional(),
            "itemRevenue": t.number().optional(),
            "productName": t.string().optional(),
            "productSku": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDataOut"])
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
    types["TransactionDataIn"] = t.struct(
        {
            "transactionTax": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionRevenue": t.number().optional(),
            "transactionShipping": t.number().optional(),
        }
    ).named(renames["TransactionDataIn"])
    types["TransactionDataOut"] = t.struct(
        {
            "transactionTax": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionRevenue": t.number().optional(),
            "transactionShipping": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionDataOut"])
    types["SequenceSegmentIn"] = t.struct(
        {
            "firstStepShouldMatchFirstHit": t.boolean().optional(),
            "segmentSequenceSteps": t.array(
                t.proxy(renames["SegmentSequenceStepIn"])
            ).optional(),
        }
    ).named(renames["SequenceSegmentIn"])
    types["SequenceSegmentOut"] = t.struct(
        {
            "firstStepShouldMatchFirstHit": t.boolean().optional(),
            "segmentSequenceSteps": t.array(
                t.proxy(renames["SegmentSequenceStepOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SequenceSegmentOut"])
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
    types["SegmentFilterClauseIn"] = t.struct(
        {
            "metricFilter": t.proxy(renames["SegmentMetricFilterIn"]).optional(),
            "not": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterIn"]).optional(),
        }
    ).named(renames["SegmentFilterClauseIn"])
    types["SegmentFilterClauseOut"] = t.struct(
        {
            "metricFilter": t.proxy(renames["SegmentMetricFilterOut"]).optional(),
            "not": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentFilterClauseOut"])
    types["EcommerceDataIn"] = t.struct(
        {
            "actionType": t.string().optional(),
            "ecommerceType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataIn"])).optional(),
            "transaction": t.proxy(renames["TransactionDataIn"]).optional(),
        }
    ).named(renames["EcommerceDataIn"])
    types["EcommerceDataOut"] = t.struct(
        {
            "actionType": t.string().optional(),
            "ecommerceType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataOut"])).optional(),
            "transaction": t.proxy(renames["TransactionDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcommerceDataOut"])
    types["OrderByIn"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "fieldName": t.string().optional(),
            "orderType": t.string().optional(),
        }
    ).named(renames["OrderByIn"])
    types["OrderByOut"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "fieldName": t.string().optional(),
            "orderType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderByOut"])
    types["SegmentSequenceStepIn"] = t.struct(
        {
            "matchType": t.string().optional(),
            "orFiltersForSegment": t.array(
                t.proxy(renames["OrFiltersForSegmentIn"])
            ).optional(),
        }
    ).named(renames["SegmentSequenceStepIn"])
    types["SegmentSequenceStepOut"] = t.struct(
        {
            "matchType": t.string().optional(),
            "orFiltersForSegment": t.array(
                t.proxy(renames["OrFiltersForSegmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentSequenceStepOut"])
    types["CohortIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CohortIn"])
    types["CohortOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortOut"])
    types["ReportRowIn"] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
        }
    ).named(renames["ReportRowIn"])
    types["ReportRowOut"] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRowOut"])
    types["PivotValueRegionIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["PivotValueRegionIn"])
    types["PivotValueRegionOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueRegionOut"])
    types["SegmentFilterIn"] = t.struct(
        {
            "not": t.boolean().optional(),
            "simpleSegment": t.proxy(renames["SimpleSegmentIn"]).optional(),
            "sequenceSegment": t.proxy(renames["SequenceSegmentIn"]).optional(),
        }
    ).named(renames["SegmentFilterIn"])
    types["SegmentFilterOut"] = t.struct(
        {
            "not": t.boolean().optional(),
            "simpleSegment": t.proxy(renames["SimpleSegmentOut"]).optional(),
            "sequenceSegment": t.proxy(renames["SequenceSegmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentFilterOut"])
    types["MetricHeaderIn"] = t.struct(
        {
            "metricHeaderEntries": t.array(
                t.proxy(renames["MetricHeaderEntryIn"])
            ).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderIn"])).optional(),
        }
    ).named(renames["MetricHeaderIn"])
    types["MetricHeaderOut"] = t.struct(
        {
            "metricHeaderEntries": t.array(
                t.proxy(renames["MetricHeaderEntryOut"])
            ).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricHeaderOut"])
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
    types["ReportDataIn"] = t.struct(
        {
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "maximums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "dataLastRefreshed": t.string().optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
            "rows": t.array(t.proxy(renames["ReportRowIn"])).optional(),
            "emptyReason": t.string().optional(),
            "rowCount": t.integer().optional(),
            "isDataGolden": t.boolean().optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
        }
    ).named(renames["ReportDataIn"])
    types["ReportDataOut"] = t.struct(
        {
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "maximums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "dataLastRefreshed": t.string().optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
            "rows": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "emptyReason": t.string().optional(),
            "rowCount": t.integer().optional(),
            "isDataGolden": t.boolean().optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportDataOut"])
    types["PivotHeaderEntryIn"] = t.struct(
        {
            "dimensionNames": t.array(t.string()).optional(),
            "metric": t.proxy(renames["MetricHeaderEntryIn"]).optional(),
            "dimensionValues": t.array(t.string()).optional(),
        }
    ).named(renames["PivotHeaderEntryIn"])
    types["PivotHeaderEntryOut"] = t.struct(
        {
            "dimensionNames": t.array(t.string()).optional(),
            "metric": t.proxy(renames["MetricHeaderEntryOut"]).optional(),
            "dimensionValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotHeaderEntryOut"])
    types["GetReportsRequestIn"] = t.struct(
        {
            "useResourceQuotas": t.boolean().optional(),
            "reportRequests": t.array(t.proxy(renames["ReportRequestIn"])).optional(),
        }
    ).named(renames["GetReportsRequestIn"])
    types["GetReportsRequestOut"] = t.struct(
        {
            "useResourceQuotas": t.boolean().optional(),
            "reportRequests": t.array(t.proxy(renames["ReportRequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReportsRequestOut"])
    types["ColumnHeaderIn"] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "metricHeader": t.proxy(renames["MetricHeaderIn"]).optional(),
        }
    ).named(renames["ColumnHeaderIn"])
    types["ColumnHeaderOut"] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "metricHeader": t.proxy(renames["MetricHeaderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnHeaderOut"])
    types["ReportRequestIn"] = t.struct(
        {
            "hideTotals": t.boolean().optional(),
            "filtersExpression": t.string().optional(),
            "cohortGroup": t.proxy(renames["CohortGroupIn"]).optional(),
            "samplingLevel": t.string().optional(),
            "segments": t.array(t.proxy(renames["SegmentIn"])).optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "hideValueRanges": t.boolean().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "viewId": t.string().optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseIn"])
            ).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "includeEmptyRows": t.boolean().optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseIn"])
            ).optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "hideTotals": t.boolean().optional(),
            "filtersExpression": t.string().optional(),
            "cohortGroup": t.proxy(renames["CohortGroupOut"]).optional(),
            "samplingLevel": t.string().optional(),
            "segments": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "hideValueRanges": t.boolean().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "viewId": t.string().optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseOut"])
            ).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "includeEmptyRows": t.boolean().optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])
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
    types["GetReportsResponseIn"] = t.struct(
        {
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
            "resourceQuotasRemaining": t.proxy(
                renames["ResourceQuotasRemainingIn"]
            ).optional(),
            "queryCost": t.integer().optional(),
        }
    ).named(renames["GetReportsResponseIn"])
    types["GetReportsResponseOut"] = t.struct(
        {
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "resourceQuotasRemaining": t.proxy(
                renames["ResourceQuotasRemainingOut"]
            ).optional(),
            "queryCost": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReportsResponseOut"])
    types["EventDataIn"] = t.struct(
        {
            "eventCount": t.string().optional(),
            "eventLabel": t.string().optional(),
            "eventValue": t.string().optional(),
            "eventAction": t.string().optional(),
            "eventCategory": t.string().optional(),
        }
    ).named(renames["EventDataIn"])
    types["EventDataOut"] = t.struct(
        {
            "eventCount": t.string().optional(),
            "eventLabel": t.string().optional(),
            "eventValue": t.string().optional(),
            "eventAction": t.string().optional(),
            "eventCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDataOut"])
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
    types["UserActivitySessionIn"] = t.struct(
        {
            "platform": t.string().optional(),
            "sessionDate": t.string().optional(),
            "dataSource": t.string().optional(),
            "sessionId": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "activities": t.array(t.proxy(renames["ActivityIn"])).optional(),
        }
    ).named(renames["UserActivitySessionIn"])
    types["UserActivitySessionOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "sessionDate": t.string().optional(),
            "dataSource": t.string().optional(),
            "sessionId": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "activities": t.array(t.proxy(renames["ActivityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserActivitySessionOut"])
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
    types["ActivityIn"] = t.struct(
        {
            "keyword": t.string().optional(),
            "landingPagePath": t.string().optional(),
            "activityType": t.string().optional(),
            "medium": t.string().optional(),
            "pageview": t.proxy(renames["PageviewDataIn"]).optional(),
            "source": t.string().optional(),
            "appview": t.proxy(renames["ScreenviewDataIn"]).optional(),
            "ecommerce": t.proxy(renames["EcommerceDataIn"]).optional(),
            "event": t.proxy(renames["EventDataIn"]).optional(),
            "goals": t.proxy(renames["GoalSetDataIn"]).optional(),
            "hostname": t.string().optional(),
            "channelGrouping": t.string().optional(),
            "campaign": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionIn"])
            ).optional(),
            "activityTime": t.string().optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "keyword": t.string().optional(),
            "landingPagePath": t.string().optional(),
            "activityType": t.string().optional(),
            "medium": t.string().optional(),
            "pageview": t.proxy(renames["PageviewDataOut"]).optional(),
            "source": t.string().optional(),
            "appview": t.proxy(renames["ScreenviewDataOut"]).optional(),
            "ecommerce": t.proxy(renames["EcommerceDataOut"]).optional(),
            "event": t.proxy(renames["EventDataOut"]).optional(),
            "goals": t.proxy(renames["GoalSetDataOut"]).optional(),
            "hostname": t.string().optional(),
            "channelGrouping": t.string().optional(),
            "campaign": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionOut"])
            ).optional(),
            "activityTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
    types["GoalDataIn"] = t.struct(
        {
            "goalCompletionLocation": t.string().optional(),
            "goalPreviousStep1": t.string().optional(),
            "goalCompletions": t.string().optional(),
            "goalIndex": t.integer().optional(),
            "goalPreviousStep2": t.string().optional(),
            "goalName": t.string().optional(),
            "goalValue": t.number().optional(),
            "goalPreviousStep3": t.string().optional(),
        }
    ).named(renames["GoalDataIn"])
    types["GoalDataOut"] = t.struct(
        {
            "goalCompletionLocation": t.string().optional(),
            "goalPreviousStep1": t.string().optional(),
            "goalCompletions": t.string().optional(),
            "goalIndex": t.integer().optional(),
            "goalPreviousStep2": t.string().optional(),
            "goalName": t.string().optional(),
            "goalValue": t.number().optional(),
            "goalPreviousStep3": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalDataOut"])
    types["DimensionFilterIn"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "operator": t.string().optional(),
            "dimensionName": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "not": t.boolean().optional(),
        }
    ).named(renames["DimensionFilterIn"])
    types["DimensionFilterOut"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "operator": t.string().optional(),
            "dimensionName": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "not": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionFilterOut"])
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
    types["DynamicSegmentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "userSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
            "sessionSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
        }
    ).named(renames["DynamicSegmentIn"])
    types["DynamicSegmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "userSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "sessionSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicSegmentOut"])
    types["SearchUserActivityRequestIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "pageToken": t.string().optional(),
            "viewId": t.string(),
            "user": t.proxy(renames["UserIn"]),
            "pageSize": t.integer().optional(),
            "activityTypes": t.array(t.string()).optional(),
        }
    ).named(renames["SearchUserActivityRequestIn"])
    types["SearchUserActivityRequestOut"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "pageToken": t.string().optional(),
            "viewId": t.string(),
            "user": t.proxy(renames["UserOut"]),
            "pageSize": t.integer().optional(),
            "activityTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityRequestOut"])

    functions = {}
    functions["userActivitySearch"] = analyticsreporting.post(
        "v4/userActivity:search",
        t.struct(
            {
                "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                "pageToken": t.string().optional(),
                "viewId": t.string(),
                "user": t.proxy(renames["UserIn"]),
                "pageSize": t.integer().optional(),
                "activityTypes": t.array(t.string()).optional(),
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
                "useResourceQuotas": t.boolean().optional(),
                "reportRequests": t.array(
                    t.proxy(renames["ReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticsreporting", renames=renames, types=types, functions=functions
    )
