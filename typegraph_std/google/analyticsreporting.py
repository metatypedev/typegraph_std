from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_analyticsreporting():
    analyticsreporting = HTTPRuntime("https://analyticsreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsreporting_1_ErrorResponse",
        "SegmentFilterIn": "_analyticsreporting_2_SegmentFilterIn",
        "SegmentFilterOut": "_analyticsreporting_3_SegmentFilterOut",
        "MetricFilterIn": "_analyticsreporting_4_MetricFilterIn",
        "MetricFilterOut": "_analyticsreporting_5_MetricFilterOut",
        "DateRangeIn": "_analyticsreporting_6_DateRangeIn",
        "DateRangeOut": "_analyticsreporting_7_DateRangeOut",
        "PageviewDataIn": "_analyticsreporting_8_PageviewDataIn",
        "PageviewDataOut": "_analyticsreporting_9_PageviewDataOut",
        "ActivityIn": "_analyticsreporting_10_ActivityIn",
        "ActivityOut": "_analyticsreporting_11_ActivityOut",
        "ColumnHeaderIn": "_analyticsreporting_12_ColumnHeaderIn",
        "ColumnHeaderOut": "_analyticsreporting_13_ColumnHeaderOut",
        "SegmentFilterClauseIn": "_analyticsreporting_14_SegmentFilterClauseIn",
        "SegmentFilterClauseOut": "_analyticsreporting_15_SegmentFilterClauseOut",
        "GoalSetDataIn": "_analyticsreporting_16_GoalSetDataIn",
        "GoalSetDataOut": "_analyticsreporting_17_GoalSetDataOut",
        "ReportRowIn": "_analyticsreporting_18_ReportRowIn",
        "ReportRowOut": "_analyticsreporting_19_ReportRowOut",
        "CohortGroupIn": "_analyticsreporting_20_CohortGroupIn",
        "CohortGroupOut": "_analyticsreporting_21_CohortGroupOut",
        "MetricHeaderEntryIn": "_analyticsreporting_22_MetricHeaderEntryIn",
        "MetricHeaderEntryOut": "_analyticsreporting_23_MetricHeaderEntryOut",
        "TransactionDataIn": "_analyticsreporting_24_TransactionDataIn",
        "TransactionDataOut": "_analyticsreporting_25_TransactionDataOut",
        "SequenceSegmentIn": "_analyticsreporting_26_SequenceSegmentIn",
        "SequenceSegmentOut": "_analyticsreporting_27_SequenceSegmentOut",
        "PivotHeaderEntryIn": "_analyticsreporting_28_PivotHeaderEntryIn",
        "PivotHeaderEntryOut": "_analyticsreporting_29_PivotHeaderEntryOut",
        "EcommerceDataIn": "_analyticsreporting_30_EcommerceDataIn",
        "EcommerceDataOut": "_analyticsreporting_31_EcommerceDataOut",
        "GoalDataIn": "_analyticsreporting_32_GoalDataIn",
        "GoalDataOut": "_analyticsreporting_33_GoalDataOut",
        "SegmentDimensionFilterIn": "_analyticsreporting_34_SegmentDimensionFilterIn",
        "SegmentDimensionFilterOut": "_analyticsreporting_35_SegmentDimensionFilterOut",
        "DateRangeValuesIn": "_analyticsreporting_36_DateRangeValuesIn",
        "DateRangeValuesOut": "_analyticsreporting_37_DateRangeValuesOut",
        "ResourceQuotasRemainingIn": "_analyticsreporting_38_ResourceQuotasRemainingIn",
        "ResourceQuotasRemainingOut": "_analyticsreporting_39_ResourceQuotasRemainingOut",
        "MetricFilterClauseIn": "_analyticsreporting_40_MetricFilterClauseIn",
        "MetricFilterClauseOut": "_analyticsreporting_41_MetricFilterClauseOut",
        "ProductDataIn": "_analyticsreporting_42_ProductDataIn",
        "ProductDataOut": "_analyticsreporting_43_ProductDataOut",
        "PivotValueRegionIn": "_analyticsreporting_44_PivotValueRegionIn",
        "PivotValueRegionOut": "_analyticsreporting_45_PivotValueRegionOut",
        "SearchUserActivityResponseIn": "_analyticsreporting_46_SearchUserActivityResponseIn",
        "SearchUserActivityResponseOut": "_analyticsreporting_47_SearchUserActivityResponseOut",
        "SegmentIn": "_analyticsreporting_48_SegmentIn",
        "SegmentOut": "_analyticsreporting_49_SegmentOut",
        "ReportIn": "_analyticsreporting_50_ReportIn",
        "ReportOut": "_analyticsreporting_51_ReportOut",
        "CustomDimensionIn": "_analyticsreporting_52_CustomDimensionIn",
        "CustomDimensionOut": "_analyticsreporting_53_CustomDimensionOut",
        "EventDataIn": "_analyticsreporting_54_EventDataIn",
        "EventDataOut": "_analyticsreporting_55_EventDataOut",
        "UserActivitySessionIn": "_analyticsreporting_56_UserActivitySessionIn",
        "UserActivitySessionOut": "_analyticsreporting_57_UserActivitySessionOut",
        "DimensionFilterIn": "_analyticsreporting_58_DimensionFilterIn",
        "DimensionFilterOut": "_analyticsreporting_59_DimensionFilterOut",
        "GetReportsRequestIn": "_analyticsreporting_60_GetReportsRequestIn",
        "GetReportsRequestOut": "_analyticsreporting_61_GetReportsRequestOut",
        "SimpleSegmentIn": "_analyticsreporting_62_SimpleSegmentIn",
        "SimpleSegmentOut": "_analyticsreporting_63_SimpleSegmentOut",
        "DimensionFilterClauseIn": "_analyticsreporting_64_DimensionFilterClauseIn",
        "DimensionFilterClauseOut": "_analyticsreporting_65_DimensionFilterClauseOut",
        "OrderByIn": "_analyticsreporting_66_OrderByIn",
        "OrderByOut": "_analyticsreporting_67_OrderByOut",
        "ScreenviewDataIn": "_analyticsreporting_68_ScreenviewDataIn",
        "ScreenviewDataOut": "_analyticsreporting_69_ScreenviewDataOut",
        "MetricHeaderIn": "_analyticsreporting_70_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsreporting_71_MetricHeaderOut",
        "PivotHeaderIn": "_analyticsreporting_72_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsreporting_73_PivotHeaderOut",
        "DimensionIn": "_analyticsreporting_74_DimensionIn",
        "DimensionOut": "_analyticsreporting_75_DimensionOut",
        "DynamicSegmentIn": "_analyticsreporting_76_DynamicSegmentIn",
        "DynamicSegmentOut": "_analyticsreporting_77_DynamicSegmentOut",
        "UserIn": "_analyticsreporting_78_UserIn",
        "UserOut": "_analyticsreporting_79_UserOut",
        "ReportDataIn": "_analyticsreporting_80_ReportDataIn",
        "ReportDataOut": "_analyticsreporting_81_ReportDataOut",
        "SearchUserActivityRequestIn": "_analyticsreporting_82_SearchUserActivityRequestIn",
        "SearchUserActivityRequestOut": "_analyticsreporting_83_SearchUserActivityRequestOut",
        "MetricIn": "_analyticsreporting_84_MetricIn",
        "MetricOut": "_analyticsreporting_85_MetricOut",
        "ReportRequestIn": "_analyticsreporting_86_ReportRequestIn",
        "ReportRequestOut": "_analyticsreporting_87_ReportRequestOut",
        "GetReportsResponseIn": "_analyticsreporting_88_GetReportsResponseIn",
        "GetReportsResponseOut": "_analyticsreporting_89_GetReportsResponseOut",
        "SegmentDefinitionIn": "_analyticsreporting_90_SegmentDefinitionIn",
        "SegmentDefinitionOut": "_analyticsreporting_91_SegmentDefinitionOut",
        "PivotIn": "_analyticsreporting_92_PivotIn",
        "PivotOut": "_analyticsreporting_93_PivotOut",
        "OrFiltersForSegmentIn": "_analyticsreporting_94_OrFiltersForSegmentIn",
        "OrFiltersForSegmentOut": "_analyticsreporting_95_OrFiltersForSegmentOut",
        "SegmentSequenceStepIn": "_analyticsreporting_96_SegmentSequenceStepIn",
        "SegmentSequenceStepOut": "_analyticsreporting_97_SegmentSequenceStepOut",
        "CohortIn": "_analyticsreporting_98_CohortIn",
        "CohortOut": "_analyticsreporting_99_CohortOut",
        "SegmentMetricFilterIn": "_analyticsreporting_100_SegmentMetricFilterIn",
        "SegmentMetricFilterOut": "_analyticsreporting_101_SegmentMetricFilterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["MetricFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "not": t.boolean().optional(),
            "metricName": t.string().optional(),
            "comparisonValue": t.string().optional(),
        }
    ).named(renames["MetricFilterIn"])
    types["MetricFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "not": t.boolean().optional(),
            "metricName": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricFilterOut"])
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
    types["ActivityIn"] = t.struct(
        {
            "event": t.proxy(renames["EventDataIn"]).optional(),
            "channelGrouping": t.string().optional(),
            "appview": t.proxy(renames["ScreenviewDataIn"]).optional(),
            "landingPagePath": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionIn"])
            ).optional(),
            "campaign": t.string().optional(),
            "activityType": t.string().optional(),
            "keyword": t.string().optional(),
            "pageview": t.proxy(renames["PageviewDataIn"]).optional(),
            "goals": t.proxy(renames["GoalSetDataIn"]).optional(),
            "activityTime": t.string().optional(),
            "hostname": t.string().optional(),
            "ecommerce": t.proxy(renames["EcommerceDataIn"]).optional(),
            "source": t.string().optional(),
            "medium": t.string().optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "event": t.proxy(renames["EventDataOut"]).optional(),
            "channelGrouping": t.string().optional(),
            "appview": t.proxy(renames["ScreenviewDataOut"]).optional(),
            "landingPagePath": t.string().optional(),
            "customDimension": t.array(
                t.proxy(renames["CustomDimensionOut"])
            ).optional(),
            "campaign": t.string().optional(),
            "activityType": t.string().optional(),
            "keyword": t.string().optional(),
            "pageview": t.proxy(renames["PageviewDataOut"]).optional(),
            "goals": t.proxy(renames["GoalSetDataOut"]).optional(),
            "activityTime": t.string().optional(),
            "hostname": t.string().optional(),
            "ecommerce": t.proxy(renames["EcommerceDataOut"]).optional(),
            "source": t.string().optional(),
            "medium": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
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
    types["SegmentFilterClauseIn"] = t.struct(
        {
            "not": t.boolean().optional(),
            "metricFilter": t.proxy(renames["SegmentMetricFilterIn"]).optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterIn"]).optional(),
        }
    ).named(renames["SegmentFilterClauseIn"])
    types["SegmentFilterClauseOut"] = t.struct(
        {
            "not": t.boolean().optional(),
            "metricFilter": t.proxy(renames["SegmentMetricFilterOut"]).optional(),
            "dimensionFilter": t.proxy(renames["SegmentDimensionFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentFilterClauseOut"])
    types["GoalSetDataIn"] = t.struct(
        {"goals": t.array(t.proxy(renames["GoalDataIn"])).optional()}
    ).named(renames["GoalSetDataIn"])
    types["GoalSetDataOut"] = t.struct(
        {
            "goals": t.array(t.proxy(renames["GoalDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalSetDataOut"])
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
    types["TransactionDataIn"] = t.struct(
        {
            "transactionRevenue": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionTax": t.number().optional(),
            "transactionShipping": t.number().optional(),
        }
    ).named(renames["TransactionDataIn"])
    types["TransactionDataOut"] = t.struct(
        {
            "transactionRevenue": t.number().optional(),
            "transactionId": t.string().optional(),
            "transactionTax": t.number().optional(),
            "transactionShipping": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionDataOut"])
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
    types["PivotHeaderEntryIn"] = t.struct(
        {
            "dimensionValues": t.array(t.string()).optional(),
            "dimensionNames": t.array(t.string()).optional(),
            "metric": t.proxy(renames["MetricHeaderEntryIn"]).optional(),
        }
    ).named(renames["PivotHeaderEntryIn"])
    types["PivotHeaderEntryOut"] = t.struct(
        {
            "dimensionValues": t.array(t.string()).optional(),
            "dimensionNames": t.array(t.string()).optional(),
            "metric": t.proxy(renames["MetricHeaderEntryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotHeaderEntryOut"])
    types["EcommerceDataIn"] = t.struct(
        {
            "ecommerceType": t.string().optional(),
            "actionType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataIn"])).optional(),
            "transaction": t.proxy(renames["TransactionDataIn"]).optional(),
        }
    ).named(renames["EcommerceDataIn"])
    types["EcommerceDataOut"] = t.struct(
        {
            "ecommerceType": t.string().optional(),
            "actionType": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductDataOut"])).optional(),
            "transaction": t.proxy(renames["TransactionDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcommerceDataOut"])
    types["GoalDataIn"] = t.struct(
        {
            "goalPreviousStep2": t.string().optional(),
            "goalName": t.string().optional(),
            "goalIndex": t.integer().optional(),
            "goalCompletions": t.string().optional(),
            "goalCompletionLocation": t.string().optional(),
            "goalValue": t.number().optional(),
            "goalPreviousStep3": t.string().optional(),
            "goalPreviousStep1": t.string().optional(),
        }
    ).named(renames["GoalDataIn"])
    types["GoalDataOut"] = t.struct(
        {
            "goalPreviousStep2": t.string().optional(),
            "goalName": t.string().optional(),
            "goalIndex": t.integer().optional(),
            "goalCompletions": t.string().optional(),
            "goalCompletionLocation": t.string().optional(),
            "goalValue": t.number().optional(),
            "goalPreviousStep3": t.string().optional(),
            "goalPreviousStep1": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoalDataOut"])
    types["SegmentDimensionFilterIn"] = t.struct(
        {
            "maxComparisonValue": t.string().optional(),
            "operator": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "expressions": t.array(t.string()).optional(),
            "dimensionName": t.string().optional(),
            "minComparisonValue": t.string().optional(),
        }
    ).named(renames["SegmentDimensionFilterIn"])
    types["SegmentDimensionFilterOut"] = t.struct(
        {
            "maxComparisonValue": t.string().optional(),
            "operator": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "expressions": t.array(t.string()).optional(),
            "dimensionName": t.string().optional(),
            "minComparisonValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentDimensionFilterOut"])
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
    types["ProductDataIn"] = t.struct(
        {
            "itemRevenue": t.number().optional(),
            "productSku": t.string().optional(),
            "productName": t.string().optional(),
            "productQuantity": t.string().optional(),
        }
    ).named(renames["ProductDataIn"])
    types["ProductDataOut"] = t.struct(
        {
            "itemRevenue": t.number().optional(),
            "productSku": t.string().optional(),
            "productName": t.string().optional(),
            "productQuantity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDataOut"])
    types["PivotValueRegionIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["PivotValueRegionIn"])
    types["PivotValueRegionOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotValueRegionOut"])
    types["SearchUserActivityResponseIn"] = t.struct(
        {
            "totalRows": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "sampleRate": t.number().optional(),
            "sessions": t.array(t.proxy(renames["UserActivitySessionIn"])).optional(),
        }
    ).named(renames["SearchUserActivityResponseIn"])
    types["SearchUserActivityResponseOut"] = t.struct(
        {
            "totalRows": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "sampleRate": t.number().optional(),
            "sessions": t.array(t.proxy(renames["UserActivitySessionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityResponseOut"])
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
    types["EventDataIn"] = t.struct(
        {
            "eventCategory": t.string().optional(),
            "eventCount": t.string().optional(),
            "eventAction": t.string().optional(),
            "eventValue": t.string().optional(),
            "eventLabel": t.string().optional(),
        }
    ).named(renames["EventDataIn"])
    types["EventDataOut"] = t.struct(
        {
            "eventCategory": t.string().optional(),
            "eventCount": t.string().optional(),
            "eventAction": t.string().optional(),
            "eventValue": t.string().optional(),
            "eventLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDataOut"])
    types["UserActivitySessionIn"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["ActivityIn"])).optional(),
            "platform": t.string().optional(),
            "dataSource": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "sessionDate": t.string().optional(),
            "sessionId": t.string().optional(),
        }
    ).named(renames["UserActivitySessionIn"])
    types["UserActivitySessionOut"] = t.struct(
        {
            "activities": t.array(t.proxy(renames["ActivityOut"])).optional(),
            "platform": t.string().optional(),
            "dataSource": t.string().optional(),
            "deviceCategory": t.string().optional(),
            "sessionDate": t.string().optional(),
            "sessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserActivitySessionOut"])
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
    types["OrderByIn"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "orderType": t.string().optional(),
            "fieldName": t.string().optional(),
        }
    ).named(renames["OrderByIn"])
    types["OrderByOut"] = t.struct(
        {
            "sortOrder": t.string().optional(),
            "orderType": t.string().optional(),
            "fieldName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderByOut"])
    types["ScreenviewDataIn"] = t.struct(
        {
            "screenName": t.string().optional(),
            "mobileDeviceBranding": t.string().optional(),
            "appName": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
        }
    ).named(renames["ScreenviewDataIn"])
    types["ScreenviewDataOut"] = t.struct(
        {
            "screenName": t.string().optional(),
            "mobileDeviceBranding": t.string().optional(),
            "appName": t.string().optional(),
            "mobileDeviceModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScreenviewDataOut"])
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
    types["DynamicSegmentIn"] = t.struct(
        {
            "userSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
            "name": t.string().optional(),
            "sessionSegment": t.proxy(renames["SegmentDefinitionIn"]).optional(),
        }
    ).named(renames["DynamicSegmentIn"])
    types["DynamicSegmentOut"] = t.struct(
        {
            "userSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "name": t.string().optional(),
            "sessionSegment": t.proxy(renames["SegmentDefinitionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicSegmentOut"])
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
    types["ReportDataIn"] = t.struct(
        {
            "emptyReason": t.string().optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
            "dataLastRefreshed": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowIn"])).optional(),
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "maximums": t.array(t.proxy(renames["DateRangeValuesIn"])).optional(),
            "isDataGolden": t.boolean().optional(),
            "rowCount": t.integer().optional(),
        }
    ).named(renames["ReportDataIn"])
    types["ReportDataOut"] = t.struct(
        {
            "emptyReason": t.string().optional(),
            "totals": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "samplesReadCounts": t.array(t.string()).optional(),
            "dataLastRefreshed": t.string().optional(),
            "rows": t.array(t.proxy(renames["ReportRowOut"])).optional(),
            "samplingSpaceSizes": t.array(t.string()).optional(),
            "minimums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "maximums": t.array(t.proxy(renames["DateRangeValuesOut"])).optional(),
            "isDataGolden": t.boolean().optional(),
            "rowCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportDataOut"])
    types["SearchUserActivityRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "activityTypes": t.array(t.string()).optional(),
            "user": t.proxy(renames["UserIn"]),
            "pageSize": t.integer().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "viewId": t.string(),
        }
    ).named(renames["SearchUserActivityRequestIn"])
    types["SearchUserActivityRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "activityTypes": t.array(t.string()).optional(),
            "user": t.proxy(renames["UserOut"]),
            "pageSize": t.integer().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "viewId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchUserActivityRequestOut"])
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
    types["ReportRequestIn"] = t.struct(
        {
            "filtersExpression": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "includeEmptyRows": t.boolean().optional(),
            "cohortGroup": t.proxy(renames["CohortGroupIn"]).optional(),
            "pageToken": t.string().optional(),
            "viewId": t.string().optional(),
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseIn"])
            ).optional(),
            "hideValueRanges": t.boolean().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "hideTotals": t.boolean().optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseIn"])
            ).optional(),
            "segments": t.array(t.proxy(renames["SegmentIn"])).optional(),
            "samplingLevel": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "filtersExpression": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "includeEmptyRows": t.boolean().optional(),
            "cohortGroup": t.proxy(renames["CohortGroupOut"]).optional(),
            "pageToken": t.string().optional(),
            "viewId": t.string().optional(),
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "metricFilterClauses": t.array(
                t.proxy(renames["MetricFilterClauseOut"])
            ).optional(),
            "hideValueRanges": t.boolean().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "hideTotals": t.boolean().optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseOut"])
            ).optional(),
            "segments": t.array(t.proxy(renames["SegmentOut"])).optional(),
            "samplingLevel": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])
    types["GetReportsResponseIn"] = t.struct(
        {
            "resourceQuotasRemaining": t.proxy(
                renames["ResourceQuotasRemainingIn"]
            ).optional(),
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
            "queryCost": t.integer().optional(),
        }
    ).named(renames["GetReportsResponseIn"])
    types["GetReportsResponseOut"] = t.struct(
        {
            "resourceQuotasRemaining": t.proxy(
                renames["ResourceQuotasRemainingOut"]
            ).optional(),
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "queryCost": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReportsResponseOut"])
    types["SegmentDefinitionIn"] = t.struct(
        {"segmentFilters": t.array(t.proxy(renames["SegmentFilterIn"])).optional()}
    ).named(renames["SegmentDefinitionIn"])
    types["SegmentDefinitionOut"] = t.struct(
        {
            "segmentFilters": t.array(t.proxy(renames["SegmentFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentDefinitionOut"])
    types["PivotIn"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseIn"])
            ).optional(),
            "startGroup": t.integer().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "maxGroupCount": t.integer().optional(),
        }
    ).named(renames["PivotIn"])
    types["PivotOut"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "dimensionFilterClauses": t.array(
                t.proxy(renames["DimensionFilterClauseOut"])
            ).optional(),
            "startGroup": t.integer().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "maxGroupCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOut"])
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
    types["SegmentMetricFilterIn"] = t.struct(
        {
            "maxComparisonValue": t.string().optional(),
            "scope": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "operator": t.string().optional(),
            "metricName": t.string().optional(),
        }
    ).named(renames["SegmentMetricFilterIn"])
    types["SegmentMetricFilterOut"] = t.struct(
        {
            "maxComparisonValue": t.string().optional(),
            "scope": t.string().optional(),
            "comparisonValue": t.string().optional(),
            "operator": t.string().optional(),
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SegmentMetricFilterOut"])

    functions = {}
    functions["userActivitySearch"] = analyticsreporting.post(
        "v4/userActivity:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "activityTypes": t.array(t.string()).optional(),
                "user": t.proxy(renames["UserIn"]),
                "pageSize": t.integer().optional(),
                "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
                "viewId": t.string(),
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
