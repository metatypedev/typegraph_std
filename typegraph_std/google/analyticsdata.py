from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_analyticsdata() -> Import:
    analyticsdata = HTTPRuntime("https://analyticsdata.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsdata_1_ErrorResponse",
        "DimensionMetadataIn": "_analyticsdata_2_DimensionMetadataIn",
        "DimensionMetadataOut": "_analyticsdata_3_DimensionMetadataOut",
        "PivotSelectionIn": "_analyticsdata_4_PivotSelectionIn",
        "PivotSelectionOut": "_analyticsdata_5_PivotSelectionOut",
        "PivotDimensionHeaderIn": "_analyticsdata_6_PivotDimensionHeaderIn",
        "PivotDimensionHeaderOut": "_analyticsdata_7_PivotDimensionHeaderOut",
        "ConcatenateExpressionIn": "_analyticsdata_8_ConcatenateExpressionIn",
        "ConcatenateExpressionOut": "_analyticsdata_9_ConcatenateExpressionOut",
        "CheckCompatibilityResponseIn": "_analyticsdata_10_CheckCompatibilityResponseIn",
        "CheckCompatibilityResponseOut": "_analyticsdata_11_CheckCompatibilityResponseOut",
        "DimensionCompatibilityIn": "_analyticsdata_12_DimensionCompatibilityIn",
        "DimensionCompatibilityOut": "_analyticsdata_13_DimensionCompatibilityOut",
        "RunRealtimeReportRequestIn": "_analyticsdata_14_RunRealtimeReportRequestIn",
        "RunRealtimeReportRequestOut": "_analyticsdata_15_RunRealtimeReportRequestOut",
        "PivotIn": "_analyticsdata_16_PivotIn",
        "PivotOut": "_analyticsdata_17_PivotOut",
        "MetricHeaderIn": "_analyticsdata_18_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsdata_19_MetricHeaderOut",
        "RunPivotReportRequestIn": "_analyticsdata_20_RunPivotReportRequestIn",
        "RunPivotReportRequestOut": "_analyticsdata_21_RunPivotReportRequestOut",
        "DateRangeIn": "_analyticsdata_22_DateRangeIn",
        "DateRangeOut": "_analyticsdata_23_DateRangeOut",
        "BatchRunPivotReportsRequestIn": "_analyticsdata_24_BatchRunPivotReportsRequestIn",
        "BatchRunPivotReportsRequestOut": "_analyticsdata_25_BatchRunPivotReportsRequestOut",
        "RunRealtimeReportResponseIn": "_analyticsdata_26_RunRealtimeReportResponseIn",
        "RunRealtimeReportResponseOut": "_analyticsdata_27_RunRealtimeReportResponseOut",
        "ResponseMetaDataIn": "_analyticsdata_28_ResponseMetaDataIn",
        "ResponseMetaDataOut": "_analyticsdata_29_ResponseMetaDataOut",
        "MetricIn": "_analyticsdata_30_MetricIn",
        "MetricOut": "_analyticsdata_31_MetricOut",
        "DimensionExpressionIn": "_analyticsdata_32_DimensionExpressionIn",
        "DimensionExpressionOut": "_analyticsdata_33_DimensionExpressionOut",
        "PropertyQuotaIn": "_analyticsdata_34_PropertyQuotaIn",
        "PropertyQuotaOut": "_analyticsdata_35_PropertyQuotaOut",
        "NumericFilterIn": "_analyticsdata_36_NumericFilterIn",
        "NumericFilterOut": "_analyticsdata_37_NumericFilterOut",
        "MetricValueIn": "_analyticsdata_38_MetricValueIn",
        "MetricValueOut": "_analyticsdata_39_MetricValueOut",
        "MetricMetadataIn": "_analyticsdata_40_MetricMetadataIn",
        "MetricMetadataOut": "_analyticsdata_41_MetricMetadataOut",
        "CohortIn": "_analyticsdata_42_CohortIn",
        "CohortOut": "_analyticsdata_43_CohortOut",
        "CohortsRangeIn": "_analyticsdata_44_CohortsRangeIn",
        "CohortsRangeOut": "_analyticsdata_45_CohortsRangeOut",
        "SchemaRestrictionResponseIn": "_analyticsdata_46_SchemaRestrictionResponseIn",
        "SchemaRestrictionResponseOut": "_analyticsdata_47_SchemaRestrictionResponseOut",
        "MinuteRangeIn": "_analyticsdata_48_MinuteRangeIn",
        "MinuteRangeOut": "_analyticsdata_49_MinuteRangeOut",
        "OrderByIn": "_analyticsdata_50_OrderByIn",
        "OrderByOut": "_analyticsdata_51_OrderByOut",
        "CaseExpressionIn": "_analyticsdata_52_CaseExpressionIn",
        "CaseExpressionOut": "_analyticsdata_53_CaseExpressionOut",
        "PivotHeaderIn": "_analyticsdata_54_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsdata_55_PivotHeaderOut",
        "FilterExpressionIn": "_analyticsdata_56_FilterExpressionIn",
        "FilterExpressionOut": "_analyticsdata_57_FilterExpressionOut",
        "BatchRunReportsResponseIn": "_analyticsdata_58_BatchRunReportsResponseIn",
        "BatchRunReportsResponseOut": "_analyticsdata_59_BatchRunReportsResponseOut",
        "NumericValueIn": "_analyticsdata_60_NumericValueIn",
        "NumericValueOut": "_analyticsdata_61_NumericValueOut",
        "InListFilterIn": "_analyticsdata_62_InListFilterIn",
        "InListFilterOut": "_analyticsdata_63_InListFilterOut",
        "RunReportResponseIn": "_analyticsdata_64_RunReportResponseIn",
        "RunReportResponseOut": "_analyticsdata_65_RunReportResponseOut",
        "FilterIn": "_analyticsdata_66_FilterIn",
        "FilterOut": "_analyticsdata_67_FilterOut",
        "FilterExpressionListIn": "_analyticsdata_68_FilterExpressionListIn",
        "FilterExpressionListOut": "_analyticsdata_69_FilterExpressionListOut",
        "BetweenFilterIn": "_analyticsdata_70_BetweenFilterIn",
        "BetweenFilterOut": "_analyticsdata_71_BetweenFilterOut",
        "MetadataIn": "_analyticsdata_72_MetadataIn",
        "MetadataOut": "_analyticsdata_73_MetadataOut",
        "RowIn": "_analyticsdata_74_RowIn",
        "RowOut": "_analyticsdata_75_RowOut",
        "DimensionValueIn": "_analyticsdata_76_DimensionValueIn",
        "DimensionValueOut": "_analyticsdata_77_DimensionValueOut",
        "BatchRunReportsRequestIn": "_analyticsdata_78_BatchRunReportsRequestIn",
        "BatchRunReportsRequestOut": "_analyticsdata_79_BatchRunReportsRequestOut",
        "CohortSpecIn": "_analyticsdata_80_CohortSpecIn",
        "CohortSpecOut": "_analyticsdata_81_CohortSpecOut",
        "CohortReportSettingsIn": "_analyticsdata_82_CohortReportSettingsIn",
        "CohortReportSettingsOut": "_analyticsdata_83_CohortReportSettingsOut",
        "MetricCompatibilityIn": "_analyticsdata_84_MetricCompatibilityIn",
        "MetricCompatibilityOut": "_analyticsdata_85_MetricCompatibilityOut",
        "DimensionOrderByIn": "_analyticsdata_86_DimensionOrderByIn",
        "DimensionOrderByOut": "_analyticsdata_87_DimensionOrderByOut",
        "DimensionIn": "_analyticsdata_88_DimensionIn",
        "DimensionOut": "_analyticsdata_89_DimensionOut",
        "BatchRunPivotReportsResponseIn": "_analyticsdata_90_BatchRunPivotReportsResponseIn",
        "BatchRunPivotReportsResponseOut": "_analyticsdata_91_BatchRunPivotReportsResponseOut",
        "MetricOrderByIn": "_analyticsdata_92_MetricOrderByIn",
        "MetricOrderByOut": "_analyticsdata_93_MetricOrderByOut",
        "RunReportRequestIn": "_analyticsdata_94_RunReportRequestIn",
        "RunReportRequestOut": "_analyticsdata_95_RunReportRequestOut",
        "QuotaStatusIn": "_analyticsdata_96_QuotaStatusIn",
        "QuotaStatusOut": "_analyticsdata_97_QuotaStatusOut",
        "DimensionHeaderIn": "_analyticsdata_98_DimensionHeaderIn",
        "DimensionHeaderOut": "_analyticsdata_99_DimensionHeaderOut",
        "CheckCompatibilityRequestIn": "_analyticsdata_100_CheckCompatibilityRequestIn",
        "CheckCompatibilityRequestOut": "_analyticsdata_101_CheckCompatibilityRequestOut",
        "StringFilterIn": "_analyticsdata_102_StringFilterIn",
        "StringFilterOut": "_analyticsdata_103_StringFilterOut",
        "RunPivotReportResponseIn": "_analyticsdata_104_RunPivotReportResponseIn",
        "RunPivotReportResponseOut": "_analyticsdata_105_RunPivotReportResponseOut",
        "PivotOrderByIn": "_analyticsdata_106_PivotOrderByIn",
        "PivotOrderByOut": "_analyticsdata_107_PivotOrderByOut",
        "ActiveMetricRestrictionIn": "_analyticsdata_108_ActiveMetricRestrictionIn",
        "ActiveMetricRestrictionOut": "_analyticsdata_109_ActiveMetricRestrictionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DimensionMetadataIn"] = t.struct(
        {
            "category": t.string().optional(),
            "apiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "uiName": t.string().optional(),
            "description": t.string().optional(),
            "customDefinition": t.boolean().optional(),
        }
    ).named(renames["DimensionMetadataIn"])
    types["DimensionMetadataOut"] = t.struct(
        {
            "category": t.string().optional(),
            "apiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "uiName": t.string().optional(),
            "description": t.string().optional(),
            "customDefinition": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionMetadataOut"])
    types["PivotSelectionIn"] = t.struct(
        {
            "dimensionValue": t.string().optional(),
            "dimensionName": t.string().optional(),
        }
    ).named(renames["PivotSelectionIn"])
    types["PivotSelectionOut"] = t.struct(
        {
            "dimensionValue": t.string().optional(),
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotSelectionOut"])
    types["PivotDimensionHeaderIn"] = t.struct(
        {"dimensionValues": t.array(t.proxy(renames["DimensionValueIn"])).optional()}
    ).named(renames["PivotDimensionHeaderIn"])
    types["PivotDimensionHeaderOut"] = t.struct(
        {
            "dimensionValues": t.array(
                t.proxy(renames["DimensionValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotDimensionHeaderOut"])
    types["ConcatenateExpressionIn"] = t.struct(
        {
            "dimensionNames": t.array(t.string()).optional(),
            "delimiter": t.string().optional(),
        }
    ).named(renames["ConcatenateExpressionIn"])
    types["ConcatenateExpressionOut"] = t.struct(
        {
            "dimensionNames": t.array(t.string()).optional(),
            "delimiter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConcatenateExpressionOut"])
    types["CheckCompatibilityResponseIn"] = t.struct(
        {
            "metricCompatibilities": t.array(
                t.proxy(renames["MetricCompatibilityIn"])
            ).optional(),
            "dimensionCompatibilities": t.array(
                t.proxy(renames["DimensionCompatibilityIn"])
            ).optional(),
        }
    ).named(renames["CheckCompatibilityResponseIn"])
    types["CheckCompatibilityResponseOut"] = t.struct(
        {
            "metricCompatibilities": t.array(
                t.proxy(renames["MetricCompatibilityOut"])
            ).optional(),
            "dimensionCompatibilities": t.array(
                t.proxy(renames["DimensionCompatibilityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckCompatibilityResponseOut"])
    types["DimensionCompatibilityIn"] = t.struct(
        {
            "dimensionMetadata": t.proxy(renames["DimensionMetadataIn"]).optional(),
            "compatibility": t.string().optional(),
        }
    ).named(renames["DimensionCompatibilityIn"])
    types["DimensionCompatibilityOut"] = t.struct(
        {
            "dimensionMetadata": t.proxy(renames["DimensionMetadataOut"]).optional(),
            "compatibility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionCompatibilityOut"])
    types["RunRealtimeReportRequestIn"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "limit": t.string().optional(),
        }
    ).named(renames["RunRealtimeReportRequestIn"])
    types["RunRealtimeReportRequestOut"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeOut"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "limit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportRequestOut"])
    types["PivotIn"] = t.struct(
        {
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "fieldNames": t.array(t.string()).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
        }
    ).named(renames["PivotIn"])
    types["PivotOut"] = t.struct(
        {
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "fieldNames": t.array(t.string()).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOut"])
    types["MetricHeaderIn"] = t.struct(
        {"name": t.string().optional(), "type": t.string().optional()}
    ).named(renames["MetricHeaderIn"])
    types["MetricHeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricHeaderOut"])
    types["RunPivotReportRequestIn"] = t.struct(
        {
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "property": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "currencyCode": t.string().optional(),
            "keepEmptyRows": t.boolean().optional(),
        }
    ).named(renames["RunPivotReportRequestIn"])
    types["RunPivotReportRequestOut"] = t.struct(
        {
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "property": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "currencyCode": t.string().optional(),
            "keepEmptyRows": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportRequestOut"])
    types["DateRangeIn"] = t.struct(
        {
            "endDate": t.string().optional(),
            "name": t.string().optional(),
            "startDate": t.string().optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "endDate": t.string().optional(),
            "name": t.string().optional(),
            "startDate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["BatchRunPivotReportsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["RunPivotReportRequestIn"])).optional()}
    ).named(renames["BatchRunPivotReportsRequestIn"])
    types["BatchRunPivotReportsRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(renames["RunPivotReportRequestOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunPivotReportsRequestOut"])
    types["RunRealtimeReportResponseIn"] = t.struct(
        {
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
        }
    ).named(renames["RunRealtimeReportResponseIn"])
    types["RunRealtimeReportResponseOut"] = t.struct(
        {
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportResponseOut"])
    types["ResponseMetaDataIn"] = t.struct(
        {
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseIn"]
            ).optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
            "emptyReason": t.string().optional(),
            "timeZone": t.string().optional(),
            "currencyCode": t.string().optional(),
            "subjectToThresholding": t.boolean().optional(),
        }
    ).named(renames["ResponseMetaDataIn"])
    types["ResponseMetaDataOut"] = t.struct(
        {
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseOut"]
            ).optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
            "emptyReason": t.string().optional(),
            "timeZone": t.string().optional(),
            "currencyCode": t.string().optional(),
            "subjectToThresholding": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseMetaDataOut"])
    types["MetricIn"] = t.struct(
        {
            "name": t.string().optional(),
            "expression": t.string().optional(),
            "invisible": t.boolean().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "expression": t.string().optional(),
            "invisible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["DimensionExpressionIn"] = t.struct(
        {
            "lowerCase": t.proxy(renames["CaseExpressionIn"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionIn"]).optional(),
            "upperCase": t.proxy(renames["CaseExpressionIn"]).optional(),
        }
    ).named(renames["DimensionExpressionIn"])
    types["DimensionExpressionOut"] = t.struct(
        {
            "lowerCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionOut"]).optional(),
            "upperCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionExpressionOut"])
    types["PropertyQuotaIn"] = t.struct(
        {
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusIn"]).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusIn"]).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
        }
    ).named(renames["PropertyQuotaIn"])
    types["PropertyQuotaOut"] = t.struct(
        {
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusOut"]).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusOut"]).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyQuotaOut"])
    types["NumericFilterIn"] = t.struct(
        {
            "operation": t.string().optional(),
            "value": t.proxy(renames["NumericValueIn"]).optional(),
        }
    ).named(renames["NumericFilterIn"])
    types["NumericFilterOut"] = t.struct(
        {
            "operation": t.string().optional(),
            "value": t.proxy(renames["NumericValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NumericFilterOut"])
    types["MetricValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["MetricValueIn"]
    )
    types["MetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricValueOut"])
    types["MetricMetadataIn"] = t.struct(
        {
            "uiName": t.string().optional(),
            "customDefinition": t.boolean().optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "expression": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "category": t.string().optional(),
            "apiName": t.string().optional(),
        }
    ).named(renames["MetricMetadataIn"])
    types["MetricMetadataOut"] = t.struct(
        {
            "uiName": t.string().optional(),
            "customDefinition": t.boolean().optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "expression": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "category": t.string().optional(),
            "apiName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMetadataOut"])
    types["CohortIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["CohortIn"])
    types["CohortOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortOut"])
    types["CohortsRangeIn"] = t.struct(
        {
            "startOffset": t.integer().optional(),
            "endOffset": t.integer(),
            "granularity": t.string(),
        }
    ).named(renames["CohortsRangeIn"])
    types["CohortsRangeOut"] = t.struct(
        {
            "startOffset": t.integer().optional(),
            "endOffset": t.integer(),
            "granularity": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortsRangeOut"])
    types["SchemaRestrictionResponseIn"] = t.struct(
        {
            "activeMetricRestrictions": t.array(
                t.proxy(renames["ActiveMetricRestrictionIn"])
            ).optional()
        }
    ).named(renames["SchemaRestrictionResponseIn"])
    types["SchemaRestrictionResponseOut"] = t.struct(
        {
            "activeMetricRestrictions": t.array(
                t.proxy(renames["ActiveMetricRestrictionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaRestrictionResponseOut"])
    types["MinuteRangeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "startMinutesAgo": t.integer().optional(),
            "endMinutesAgo": t.integer().optional(),
        }
    ).named(renames["MinuteRangeIn"])
    types["MinuteRangeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "startMinutesAgo": t.integer().optional(),
            "endMinutesAgo": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinuteRangeOut"])
    types["OrderByIn"] = t.struct(
        {
            "desc": t.boolean().optional(),
            "pivot": t.proxy(renames["PivotOrderByIn"]).optional(),
            "dimension": t.proxy(renames["DimensionOrderByIn"]).optional(),
            "metric": t.proxy(renames["MetricOrderByIn"]).optional(),
        }
    ).named(renames["OrderByIn"])
    types["OrderByOut"] = t.struct(
        {
            "desc": t.boolean().optional(),
            "pivot": t.proxy(renames["PivotOrderByOut"]).optional(),
            "dimension": t.proxy(renames["DimensionOrderByOut"]).optional(),
            "metric": t.proxy(renames["MetricOrderByOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderByOut"])
    types["CaseExpressionIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["CaseExpressionIn"])
    types["CaseExpressionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseExpressionOut"])
    types["PivotHeaderIn"] = t.struct(
        {
            "rowCount": t.integer().optional(),
            "pivotDimensionHeaders": t.array(
                t.proxy(renames["PivotDimensionHeaderIn"])
            ).optional(),
        }
    ).named(renames["PivotHeaderIn"])
    types["PivotHeaderOut"] = t.struct(
        {
            "rowCount": t.integer().optional(),
            "pivotDimensionHeaders": t.array(
                t.proxy(renames["PivotDimensionHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotHeaderOut"])
    types["FilterExpressionIn"] = t.struct(
        {
            "notExpression": t.proxy(renames["FilterExpressionIn"]).optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "andGroup": t.proxy(renames["FilterExpressionListIn"]).optional(),
            "orGroup": t.proxy(renames["FilterExpressionListIn"]).optional(),
        }
    ).named(renames["FilterExpressionIn"])
    types["FilterExpressionOut"] = t.struct(
        {
            "notExpression": t.proxy(renames["FilterExpressionOut"]).optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "andGroup": t.proxy(renames["FilterExpressionListOut"]).optional(),
            "orGroup": t.proxy(renames["FilterExpressionListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionOut"])
    types["BatchRunReportsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "reports": t.array(t.proxy(renames["RunReportResponseIn"])).optional(),
        }
    ).named(renames["BatchRunReportsResponseIn"])
    types["BatchRunReportsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "reports": t.array(t.proxy(renames["RunReportResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunReportsResponseOut"])
    types["NumericValueIn"] = t.struct(
        {"doubleValue": t.number().optional(), "int64Value": t.string().optional()}
    ).named(renames["NumericValueIn"])
    types["NumericValueOut"] = t.struct(
        {
            "doubleValue": t.number().optional(),
            "int64Value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NumericValueOut"])
    types["InListFilterIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "caseSensitive": t.boolean().optional(),
        }
    ).named(renames["InListFilterIn"])
    types["InListFilterOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "caseSensitive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InListFilterOut"])
    types["RunReportResponseIn"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
            "rowCount": t.integer().optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "kind": t.string().optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
        }
    ).named(renames["RunReportResponseIn"])
    types["RunReportResponseOut"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "rowCount": t.integer().optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "kind": t.string().optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportResponseOut"])
    types["FilterIn"] = t.struct(
        {
            "numericFilter": t.proxy(renames["NumericFilterIn"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterIn"]).optional(),
            "fieldName": t.string().optional(),
            "inListFilter": t.proxy(renames["InListFilterIn"]).optional(),
            "stringFilter": t.proxy(renames["StringFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "numericFilter": t.proxy(renames["NumericFilterOut"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterOut"]).optional(),
            "fieldName": t.string().optional(),
            "inListFilter": t.proxy(renames["InListFilterOut"]).optional(),
            "stringFilter": t.proxy(renames["StringFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["FilterExpressionListIn"] = t.struct(
        {"expressions": t.array(t.proxy(renames["FilterExpressionIn"])).optional()}
    ).named(renames["FilterExpressionListIn"])
    types["FilterExpressionListOut"] = t.struct(
        {
            "expressions": t.array(t.proxy(renames["FilterExpressionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionListOut"])
    types["BetweenFilterIn"] = t.struct(
        {
            "toValue": t.proxy(renames["NumericValueIn"]).optional(),
            "fromValue": t.proxy(renames["NumericValueIn"]).optional(),
        }
    ).named(renames["BetweenFilterIn"])
    types["BetweenFilterOut"] = t.struct(
        {
            "toValue": t.proxy(renames["NumericValueOut"]).optional(),
            "fromValue": t.proxy(renames["NumericValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BetweenFilterOut"])
    types["MetadataIn"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionMetadataIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricMetadataIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionMetadataOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricMetadataOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["RowIn"] = t.struct(
        {
            "metricValues": t.array(t.proxy(renames["MetricValueIn"])).optional(),
            "dimensionValues": t.array(t.proxy(renames["DimensionValueIn"])).optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "metricValues": t.array(t.proxy(renames["MetricValueOut"])).optional(),
            "dimensionValues": t.array(
                t.proxy(renames["DimensionValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["DimensionValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DimensionValueIn"]
    )
    types["DimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueOut"])
    types["BatchRunReportsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["RunReportRequestIn"])).optional()}
    ).named(renames["BatchRunReportsRequestIn"])
    types["BatchRunReportsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RunReportRequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunReportsRequestOut"])
    types["CohortSpecIn"] = t.struct(
        {
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsIn"]
            ).optional(),
            "cohortsRange": t.proxy(renames["CohortsRangeIn"]).optional(),
            "cohorts": t.array(t.proxy(renames["CohortIn"])).optional(),
        }
    ).named(renames["CohortSpecIn"])
    types["CohortSpecOut"] = t.struct(
        {
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsOut"]
            ).optional(),
            "cohortsRange": t.proxy(renames["CohortsRangeOut"]).optional(),
            "cohorts": t.array(t.proxy(renames["CohortOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortSpecOut"])
    types["CohortReportSettingsIn"] = t.struct(
        {"accumulate": t.boolean().optional()}
    ).named(renames["CohortReportSettingsIn"])
    types["CohortReportSettingsOut"] = t.struct(
        {
            "accumulate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortReportSettingsOut"])
    types["MetricCompatibilityIn"] = t.struct(
        {
            "compatibility": t.string().optional(),
            "metricMetadata": t.proxy(renames["MetricMetadataIn"]).optional(),
        }
    ).named(renames["MetricCompatibilityIn"])
    types["MetricCompatibilityOut"] = t.struct(
        {
            "compatibility": t.string().optional(),
            "metricMetadata": t.proxy(renames["MetricMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricCompatibilityOut"])
    types["DimensionOrderByIn"] = t.struct(
        {"orderType": t.string().optional(), "dimensionName": t.string().optional()}
    ).named(renames["DimensionOrderByIn"])
    types["DimensionOrderByOut"] = t.struct(
        {
            "orderType": t.string().optional(),
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOrderByOut"])
    types["DimensionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dimensionExpression": t.proxy(renames["DimensionExpressionIn"]).optional(),
        }
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dimensionExpression": t.proxy(
                renames["DimensionExpressionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
    types["BatchRunPivotReportsResponseIn"] = t.struct(
        {
            "pivotReports": t.array(
                t.proxy(renames["RunPivotReportResponseIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BatchRunPivotReportsResponseIn"])
    types["BatchRunPivotReportsResponseOut"] = t.struct(
        {
            "pivotReports": t.array(
                t.proxy(renames["RunPivotReportResponseOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunPivotReportsResponseOut"])
    types["MetricOrderByIn"] = t.struct({"metricName": t.string().optional()}).named(
        renames["MetricOrderByIn"]
    )
    types["MetricOrderByOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOrderByOut"])
    types["RunReportRequestIn"] = t.struct(
        {
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "currencyCode": t.string().optional(),
            "keepEmptyRows": t.boolean().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "property": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
        }
    ).named(renames["RunReportRequestIn"])
    types["RunReportRequestOut"] = t.struct(
        {
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "currencyCode": t.string().optional(),
            "keepEmptyRows": t.boolean().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "property": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportRequestOut"])
    types["QuotaStatusIn"] = t.struct(
        {"consumed": t.integer().optional(), "remaining": t.integer().optional()}
    ).named(renames["QuotaStatusIn"])
    types["QuotaStatusOut"] = t.struct(
        {
            "consumed": t.integer().optional(),
            "remaining": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaStatusOut"])
    types["DimensionHeaderIn"] = t.struct({"name": t.string().optional()}).named(
        renames["DimensionHeaderIn"]
    )
    types["DimensionHeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionHeaderOut"])
    types["CheckCompatibilityRequestIn"] = t.struct(
        {
            "compatibilityFilter": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
        }
    ).named(renames["CheckCompatibilityRequestIn"])
    types["CheckCompatibilityRequestOut"] = t.struct(
        {
            "compatibilityFilter": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckCompatibilityRequestOut"])
    types["StringFilterIn"] = t.struct(
        {
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["StringFilterIn"])
    types["StringFilterOut"] = t.struct(
        {
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringFilterOut"])
    types["RunPivotReportResponseIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "aggregates": t.array(t.proxy(renames["RowIn"])).optional(),
            "kind": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderIn"])).optional(),
        }
    ).named(renames["RunPivotReportResponseIn"])
    types["RunPivotReportResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "aggregates": t.array(t.proxy(renames["RowOut"])).optional(),
            "kind": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportResponseOut"])
    types["PivotOrderByIn"] = t.struct(
        {
            "metricName": t.string().optional(),
            "pivotSelections": t.array(t.proxy(renames["PivotSelectionIn"])).optional(),
        }
    ).named(renames["PivotOrderByIn"])
    types["PivotOrderByOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "pivotSelections": t.array(
                t.proxy(renames["PivotSelectionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOrderByOut"])
    types["ActiveMetricRestrictionIn"] = t.struct(
        {
            "metricName": t.string().optional(),
            "restrictedMetricTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ActiveMetricRestrictionIn"])
    types["ActiveMetricRestrictionOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "restrictedMetricTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActiveMetricRestrictionOut"])

    functions = {}
    functions["propertiesRunReport"] = analyticsdata.post(
        "v1beta/{property}:batchRunPivotReports",
        t.struct(
            {
                "property": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["RunPivotReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRunPivotReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesBatchRunReports"] = analyticsdata.post(
        "v1beta/{property}:batchRunPivotReports",
        t.struct(
            {
                "property": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["RunPivotReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRunPivotReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCheckCompatibility"] = analyticsdata.post(
        "v1beta/{property}:batchRunPivotReports",
        t.struct(
            {
                "property": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["RunPivotReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRunPivotReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunRealtimeReport"] = analyticsdata.post(
        "v1beta/{property}:batchRunPivotReports",
        t.struct(
            {
                "property": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["RunPivotReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRunPivotReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunPivotReport"] = analyticsdata.post(
        "v1beta/{property}:batchRunPivotReports",
        t.struct(
            {
                "property": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["RunPivotReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRunPivotReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGetMetadata"] = analyticsdata.post(
        "v1beta/{property}:batchRunPivotReports",
        t.struct(
            {
                "property": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["RunPivotReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRunPivotReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesBatchRunPivotReports"] = analyticsdata.post(
        "v1beta/{property}:batchRunPivotReports",
        t.struct(
            {
                "property": t.string().optional(),
                "requests": t.array(
                    t.proxy(renames["RunPivotReportRequestIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchRunPivotReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticsdata",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
