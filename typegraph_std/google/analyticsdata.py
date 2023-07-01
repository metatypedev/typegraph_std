from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_analyticsdata():
    analyticsdata = HTTPRuntime("https://analyticsdata.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsdata_1_ErrorResponse",
        "MinuteRangeIn": "_analyticsdata_2_MinuteRangeIn",
        "MinuteRangeOut": "_analyticsdata_3_MinuteRangeOut",
        "RowIn": "_analyticsdata_4_RowIn",
        "RowOut": "_analyticsdata_5_RowOut",
        "PivotHeaderIn": "_analyticsdata_6_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsdata_7_PivotHeaderOut",
        "DimensionValueIn": "_analyticsdata_8_DimensionValueIn",
        "DimensionValueOut": "_analyticsdata_9_DimensionValueOut",
        "QuotaStatusIn": "_analyticsdata_10_QuotaStatusIn",
        "QuotaStatusOut": "_analyticsdata_11_QuotaStatusOut",
        "FilterExpressionListIn": "_analyticsdata_12_FilterExpressionListIn",
        "FilterExpressionListOut": "_analyticsdata_13_FilterExpressionListOut",
        "ResponseMetaDataIn": "_analyticsdata_14_ResponseMetaDataIn",
        "ResponseMetaDataOut": "_analyticsdata_15_ResponseMetaDataOut",
        "PivotIn": "_analyticsdata_16_PivotIn",
        "PivotOut": "_analyticsdata_17_PivotOut",
        "MetricMetadataIn": "_analyticsdata_18_MetricMetadataIn",
        "MetricMetadataOut": "_analyticsdata_19_MetricMetadataOut",
        "CheckCompatibilityRequestIn": "_analyticsdata_20_CheckCompatibilityRequestIn",
        "CheckCompatibilityRequestOut": "_analyticsdata_21_CheckCompatibilityRequestOut",
        "CohortIn": "_analyticsdata_22_CohortIn",
        "CohortOut": "_analyticsdata_23_CohortOut",
        "MetricCompatibilityIn": "_analyticsdata_24_MetricCompatibilityIn",
        "MetricCompatibilityOut": "_analyticsdata_25_MetricCompatibilityOut",
        "MetricValueIn": "_analyticsdata_26_MetricValueIn",
        "MetricValueOut": "_analyticsdata_27_MetricValueOut",
        "PropertyQuotaIn": "_analyticsdata_28_PropertyQuotaIn",
        "PropertyQuotaOut": "_analyticsdata_29_PropertyQuotaOut",
        "PivotOrderByIn": "_analyticsdata_30_PivotOrderByIn",
        "PivotOrderByOut": "_analyticsdata_31_PivotOrderByOut",
        "BetweenFilterIn": "_analyticsdata_32_BetweenFilterIn",
        "BetweenFilterOut": "_analyticsdata_33_BetweenFilterOut",
        "MetricIn": "_analyticsdata_34_MetricIn",
        "MetricOut": "_analyticsdata_35_MetricOut",
        "CohortReportSettingsIn": "_analyticsdata_36_CohortReportSettingsIn",
        "CohortReportSettingsOut": "_analyticsdata_37_CohortReportSettingsOut",
        "RunRealtimeReportResponseIn": "_analyticsdata_38_RunRealtimeReportResponseIn",
        "RunRealtimeReportResponseOut": "_analyticsdata_39_RunRealtimeReportResponseOut",
        "BatchRunReportsResponseIn": "_analyticsdata_40_BatchRunReportsResponseIn",
        "BatchRunReportsResponseOut": "_analyticsdata_41_BatchRunReportsResponseOut",
        "BatchRunReportsRequestIn": "_analyticsdata_42_BatchRunReportsRequestIn",
        "BatchRunReportsRequestOut": "_analyticsdata_43_BatchRunReportsRequestOut",
        "RunPivotReportResponseIn": "_analyticsdata_44_RunPivotReportResponseIn",
        "RunPivotReportResponseOut": "_analyticsdata_45_RunPivotReportResponseOut",
        "PivotSelectionIn": "_analyticsdata_46_PivotSelectionIn",
        "PivotSelectionOut": "_analyticsdata_47_PivotSelectionOut",
        "RunReportResponseIn": "_analyticsdata_48_RunReportResponseIn",
        "RunReportResponseOut": "_analyticsdata_49_RunReportResponseOut",
        "DimensionMetadataIn": "_analyticsdata_50_DimensionMetadataIn",
        "DimensionMetadataOut": "_analyticsdata_51_DimensionMetadataOut",
        "CohortsRangeIn": "_analyticsdata_52_CohortsRangeIn",
        "CohortsRangeOut": "_analyticsdata_53_CohortsRangeOut",
        "RunPivotReportRequestIn": "_analyticsdata_54_RunPivotReportRequestIn",
        "RunPivotReportRequestOut": "_analyticsdata_55_RunPivotReportRequestOut",
        "DimensionCompatibilityIn": "_analyticsdata_56_DimensionCompatibilityIn",
        "DimensionCompatibilityOut": "_analyticsdata_57_DimensionCompatibilityOut",
        "OrderByIn": "_analyticsdata_58_OrderByIn",
        "OrderByOut": "_analyticsdata_59_OrderByOut",
        "MetricHeaderIn": "_analyticsdata_60_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsdata_61_MetricHeaderOut",
        "DimensionHeaderIn": "_analyticsdata_62_DimensionHeaderIn",
        "DimensionHeaderOut": "_analyticsdata_63_DimensionHeaderOut",
        "RunReportRequestIn": "_analyticsdata_64_RunReportRequestIn",
        "RunReportRequestOut": "_analyticsdata_65_RunReportRequestOut",
        "CohortSpecIn": "_analyticsdata_66_CohortSpecIn",
        "CohortSpecOut": "_analyticsdata_67_CohortSpecOut",
        "ConcatenateExpressionIn": "_analyticsdata_68_ConcatenateExpressionIn",
        "ConcatenateExpressionOut": "_analyticsdata_69_ConcatenateExpressionOut",
        "DimensionExpressionIn": "_analyticsdata_70_DimensionExpressionIn",
        "DimensionExpressionOut": "_analyticsdata_71_DimensionExpressionOut",
        "ActiveMetricRestrictionIn": "_analyticsdata_72_ActiveMetricRestrictionIn",
        "ActiveMetricRestrictionOut": "_analyticsdata_73_ActiveMetricRestrictionOut",
        "NumericFilterIn": "_analyticsdata_74_NumericFilterIn",
        "NumericFilterOut": "_analyticsdata_75_NumericFilterOut",
        "BatchRunPivotReportsResponseIn": "_analyticsdata_76_BatchRunPivotReportsResponseIn",
        "BatchRunPivotReportsResponseOut": "_analyticsdata_77_BatchRunPivotReportsResponseOut",
        "BatchRunPivotReportsRequestIn": "_analyticsdata_78_BatchRunPivotReportsRequestIn",
        "BatchRunPivotReportsRequestOut": "_analyticsdata_79_BatchRunPivotReportsRequestOut",
        "StringFilterIn": "_analyticsdata_80_StringFilterIn",
        "StringFilterOut": "_analyticsdata_81_StringFilterOut",
        "FilterExpressionIn": "_analyticsdata_82_FilterExpressionIn",
        "FilterExpressionOut": "_analyticsdata_83_FilterExpressionOut",
        "SchemaRestrictionResponseIn": "_analyticsdata_84_SchemaRestrictionResponseIn",
        "SchemaRestrictionResponseOut": "_analyticsdata_85_SchemaRestrictionResponseOut",
        "InListFilterIn": "_analyticsdata_86_InListFilterIn",
        "InListFilterOut": "_analyticsdata_87_InListFilterOut",
        "MetadataIn": "_analyticsdata_88_MetadataIn",
        "MetadataOut": "_analyticsdata_89_MetadataOut",
        "MetricOrderByIn": "_analyticsdata_90_MetricOrderByIn",
        "MetricOrderByOut": "_analyticsdata_91_MetricOrderByOut",
        "DimensionIn": "_analyticsdata_92_DimensionIn",
        "DimensionOut": "_analyticsdata_93_DimensionOut",
        "PivotDimensionHeaderIn": "_analyticsdata_94_PivotDimensionHeaderIn",
        "PivotDimensionHeaderOut": "_analyticsdata_95_PivotDimensionHeaderOut",
        "CaseExpressionIn": "_analyticsdata_96_CaseExpressionIn",
        "CaseExpressionOut": "_analyticsdata_97_CaseExpressionOut",
        "FilterIn": "_analyticsdata_98_FilterIn",
        "FilterOut": "_analyticsdata_99_FilterOut",
        "NumericValueIn": "_analyticsdata_100_NumericValueIn",
        "NumericValueOut": "_analyticsdata_101_NumericValueOut",
        "DateRangeIn": "_analyticsdata_102_DateRangeIn",
        "DateRangeOut": "_analyticsdata_103_DateRangeOut",
        "DimensionOrderByIn": "_analyticsdata_104_DimensionOrderByIn",
        "DimensionOrderByOut": "_analyticsdata_105_DimensionOrderByOut",
        "CheckCompatibilityResponseIn": "_analyticsdata_106_CheckCompatibilityResponseIn",
        "CheckCompatibilityResponseOut": "_analyticsdata_107_CheckCompatibilityResponseOut",
        "RunRealtimeReportRequestIn": "_analyticsdata_108_RunRealtimeReportRequestIn",
        "RunRealtimeReportRequestOut": "_analyticsdata_109_RunRealtimeReportRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MinuteRangeIn"] = t.struct(
        {
            "startMinutesAgo": t.integer().optional(),
            "name": t.string().optional(),
            "endMinutesAgo": t.integer().optional(),
        }
    ).named(renames["MinuteRangeIn"])
    types["MinuteRangeOut"] = t.struct(
        {
            "startMinutesAgo": t.integer().optional(),
            "name": t.string().optional(),
            "endMinutesAgo": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinuteRangeOut"])
    types["RowIn"] = t.struct(
        {
            "dimensionValues": t.array(t.proxy(renames["DimensionValueIn"])).optional(),
            "metricValues": t.array(t.proxy(renames["MetricValueIn"])).optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "dimensionValues": t.array(
                t.proxy(renames["DimensionValueOut"])
            ).optional(),
            "metricValues": t.array(t.proxy(renames["MetricValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
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
    types["DimensionValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DimensionValueIn"]
    )
    types["DimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueOut"])
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
    types["FilterExpressionListIn"] = t.struct(
        {"expressions": t.array(t.proxy(renames["FilterExpressionIn"])).optional()}
    ).named(renames["FilterExpressionListIn"])
    types["FilterExpressionListOut"] = t.struct(
        {
            "expressions": t.array(t.proxy(renames["FilterExpressionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionListOut"])
    types["ResponseMetaDataIn"] = t.struct(
        {
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseIn"]
            ).optional(),
            "timeZone": t.string().optional(),
            "emptyReason": t.string().optional(),
            "currencyCode": t.string().optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
            "subjectToThresholding": t.boolean().optional(),
        }
    ).named(renames["ResponseMetaDataIn"])
    types["ResponseMetaDataOut"] = t.struct(
        {
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "emptyReason": t.string().optional(),
            "currencyCode": t.string().optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
            "subjectToThresholding": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseMetaDataOut"])
    types["PivotIn"] = t.struct(
        {
            "fieldNames": t.array(t.string()).optional(),
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
        }
    ).named(renames["PivotIn"])
    types["PivotOut"] = t.struct(
        {
            "fieldNames": t.array(t.string()).optional(),
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOut"])
    types["MetricMetadataIn"] = t.struct(
        {
            "customDefinition": t.boolean().optional(),
            "uiName": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "apiName": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["MetricMetadataIn"])
    types["MetricMetadataOut"] = t.struct(
        {
            "customDefinition": t.boolean().optional(),
            "uiName": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "apiName": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMetadataOut"])
    types["CheckCompatibilityRequestIn"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "compatibilityFilter": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
        }
    ).named(renames["CheckCompatibilityRequestIn"])
    types["CheckCompatibilityRequestOut"] = t.struct(
        {
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "compatibilityFilter": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckCompatibilityRequestOut"])
    types["CohortIn"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
            "name": t.string().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["CohortIn"])
    types["CohortOut"] = t.struct(
        {
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "name": t.string().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortOut"])
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
    types["MetricValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["MetricValueIn"]
    )
    types["MetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricValueOut"])
    types["PropertyQuotaIn"] = t.struct(
        {
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusIn"]).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusIn"]).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
        }
    ).named(renames["PropertyQuotaIn"])
    types["PropertyQuotaOut"] = t.struct(
        {
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusOut"]).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusOut"]).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyQuotaOut"])
    types["PivotOrderByIn"] = t.struct(
        {
            "pivotSelections": t.array(t.proxy(renames["PivotSelectionIn"])).optional(),
            "metricName": t.string().optional(),
        }
    ).named(renames["PivotOrderByIn"])
    types["PivotOrderByOut"] = t.struct(
        {
            "pivotSelections": t.array(
                t.proxy(renames["PivotSelectionOut"])
            ).optional(),
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOrderByOut"])
    types["BetweenFilterIn"] = t.struct(
        {
            "fromValue": t.proxy(renames["NumericValueIn"]).optional(),
            "toValue": t.proxy(renames["NumericValueIn"]).optional(),
        }
    ).named(renames["BetweenFilterIn"])
    types["BetweenFilterOut"] = t.struct(
        {
            "fromValue": t.proxy(renames["NumericValueOut"]).optional(),
            "toValue": t.proxy(renames["NumericValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BetweenFilterOut"])
    types["MetricIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "invisible": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "invisible": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["CohortReportSettingsIn"] = t.struct(
        {"accumulate": t.boolean().optional()}
    ).named(renames["CohortReportSettingsIn"])
    types["CohortReportSettingsOut"] = t.struct(
        {
            "accumulate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortReportSettingsOut"])
    types["RunRealtimeReportResponseIn"] = t.struct(
        {
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "kind": t.string().optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
        }
    ).named(renames["RunRealtimeReportResponseIn"])
    types["RunRealtimeReportResponseOut"] = t.struct(
        {
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "kind": t.string().optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "rowCount": t.integer().optional(),
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportResponseOut"])
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
    types["BatchRunReportsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["RunReportRequestIn"])).optional()}
    ).named(renames["BatchRunReportsRequestIn"])
    types["BatchRunReportsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RunReportRequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunReportsRequestOut"])
    types["RunPivotReportResponseIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
            "kind": t.string().optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderIn"])).optional(),
            "aggregates": t.array(t.proxy(renames["RowIn"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
        }
    ).named(renames["RunPivotReportResponseIn"])
    types["RunPivotReportResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "kind": t.string().optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderOut"])).optional(),
            "aggregates": t.array(t.proxy(renames["RowOut"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportResponseOut"])
    types["PivotSelectionIn"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "dimensionValue": t.string().optional(),
        }
    ).named(renames["PivotSelectionIn"])
    types["PivotSelectionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "dimensionValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotSelectionOut"])
    types["RunReportResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "rowCount": t.integer().optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
        }
    ).named(renames["RunReportResponseIn"])
    types["RunReportResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "rowCount": t.integer().optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportResponseOut"])
    types["DimensionMetadataIn"] = t.struct(
        {
            "customDefinition": t.boolean().optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "apiName": t.string().optional(),
            "uiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
        }
    ).named(renames["DimensionMetadataIn"])
    types["DimensionMetadataOut"] = t.struct(
        {
            "customDefinition": t.boolean().optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "apiName": t.string().optional(),
            "uiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionMetadataOut"])
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
    types["RunPivotReportRequestIn"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "currencyCode": t.string().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "property": t.string().optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["RunPivotReportRequestIn"])
    types["RunPivotReportRequestOut"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "currencyCode": t.string().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "property": t.string().optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportRequestOut"])
    types["DimensionCompatibilityIn"] = t.struct(
        {
            "compatibility": t.string().optional(),
            "dimensionMetadata": t.proxy(renames["DimensionMetadataIn"]).optional(),
        }
    ).named(renames["DimensionCompatibilityIn"])
    types["DimensionCompatibilityOut"] = t.struct(
        {
            "compatibility": t.string().optional(),
            "dimensionMetadata": t.proxy(renames["DimensionMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionCompatibilityOut"])
    types["OrderByIn"] = t.struct(
        {
            "metric": t.proxy(renames["MetricOrderByIn"]).optional(),
            "desc": t.boolean().optional(),
            "dimension": t.proxy(renames["DimensionOrderByIn"]).optional(),
            "pivot": t.proxy(renames["PivotOrderByIn"]).optional(),
        }
    ).named(renames["OrderByIn"])
    types["OrderByOut"] = t.struct(
        {
            "metric": t.proxy(renames["MetricOrderByOut"]).optional(),
            "desc": t.boolean().optional(),
            "dimension": t.proxy(renames["DimensionOrderByOut"]).optional(),
            "pivot": t.proxy(renames["PivotOrderByOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderByOut"])
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
    types["DimensionHeaderIn"] = t.struct({"name": t.string().optional()}).named(
        renames["DimensionHeaderIn"]
    )
    types["DimensionHeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionHeaderOut"])
    types["RunReportRequestIn"] = t.struct(
        {
            "metricAggregations": t.array(t.string()).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "offset": t.string().optional(),
            "limit": t.string().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "currencyCode": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "property": t.string().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "returnPropertyQuota": t.boolean().optional(),
        }
    ).named(renames["RunReportRequestIn"])
    types["RunReportRequestOut"] = t.struct(
        {
            "metricAggregations": t.array(t.string()).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "offset": t.string().optional(),
            "limit": t.string().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "currencyCode": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "property": t.string().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportRequestOut"])
    types["CohortSpecIn"] = t.struct(
        {
            "cohorts": t.array(t.proxy(renames["CohortIn"])).optional(),
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsIn"]
            ).optional(),
            "cohortsRange": t.proxy(renames["CohortsRangeIn"]).optional(),
        }
    ).named(renames["CohortSpecIn"])
    types["CohortSpecOut"] = t.struct(
        {
            "cohorts": t.array(t.proxy(renames["CohortOut"])).optional(),
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsOut"]
            ).optional(),
            "cohortsRange": t.proxy(renames["CohortsRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortSpecOut"])
    types["ConcatenateExpressionIn"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "dimensionNames": t.array(t.string()).optional(),
        }
    ).named(renames["ConcatenateExpressionIn"])
    types["ConcatenateExpressionOut"] = t.struct(
        {
            "delimiter": t.string().optional(),
            "dimensionNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConcatenateExpressionOut"])
    types["DimensionExpressionIn"] = t.struct(
        {
            "upperCase": t.proxy(renames["CaseExpressionIn"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionIn"]).optional(),
            "lowerCase": t.proxy(renames["CaseExpressionIn"]).optional(),
        }
    ).named(renames["DimensionExpressionIn"])
    types["DimensionExpressionOut"] = t.struct(
        {
            "upperCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionOut"]).optional(),
            "lowerCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionExpressionOut"])
    types["ActiveMetricRestrictionIn"] = t.struct(
        {
            "restrictedMetricTypes": t.array(t.string()).optional(),
            "metricName": t.string().optional(),
        }
    ).named(renames["ActiveMetricRestrictionIn"])
    types["ActiveMetricRestrictionOut"] = t.struct(
        {
            "restrictedMetricTypes": t.array(t.string()).optional(),
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActiveMetricRestrictionOut"])
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
    types["BatchRunPivotReportsResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "pivotReports": t.array(
                t.proxy(renames["RunPivotReportResponseIn"])
            ).optional(),
        }
    ).named(renames["BatchRunPivotReportsResponseIn"])
    types["BatchRunPivotReportsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "pivotReports": t.array(
                t.proxy(renames["RunPivotReportResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunPivotReportsResponseOut"])
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
    types["StringFilterIn"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "matchType": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["StringFilterIn"])
    types["StringFilterOut"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "matchType": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringFilterOut"])
    types["FilterExpressionIn"] = t.struct(
        {
            "andGroup": t.proxy(renames["FilterExpressionListIn"]).optional(),
            "notExpression": t.proxy(renames["FilterExpressionIn"]).optional(),
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "orGroup": t.proxy(renames["FilterExpressionListIn"]).optional(),
        }
    ).named(renames["FilterExpressionIn"])
    types["FilterExpressionOut"] = t.struct(
        {
            "andGroup": t.proxy(renames["FilterExpressionListOut"]).optional(),
            "notExpression": t.proxy(renames["FilterExpressionOut"]).optional(),
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "orGroup": t.proxy(renames["FilterExpressionListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionOut"])
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
    types["InListFilterIn"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["InListFilterIn"])
    types["InListFilterOut"] = t.struct(
        {
            "caseSensitive": t.boolean().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InListFilterOut"])
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
    types["MetricOrderByIn"] = t.struct({"metricName": t.string().optional()}).named(
        renames["MetricOrderByIn"]
    )
    types["MetricOrderByOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOrderByOut"])
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
    types["CaseExpressionIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["CaseExpressionIn"])
    types["CaseExpressionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseExpressionOut"])
    types["FilterIn"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "stringFilter": t.proxy(renames["StringFilterIn"]).optional(),
            "inListFilter": t.proxy(renames["InListFilterIn"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterIn"]).optional(),
            "numericFilter": t.proxy(renames["NumericFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "stringFilter": t.proxy(renames["StringFilterOut"]).optional(),
            "inListFilter": t.proxy(renames["InListFilterOut"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterOut"]).optional(),
            "numericFilter": t.proxy(renames["NumericFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
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
    types["DateRangeIn"] = t.struct(
        {
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "endDate": t.string().optional(),
            "startDate": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
    types["DimensionOrderByIn"] = t.struct(
        {"dimensionName": t.string().optional(), "orderType": t.string().optional()}
    ).named(renames["DimensionOrderByIn"])
    types["DimensionOrderByOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "orderType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOrderByOut"])
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
    types["RunRealtimeReportRequestIn"] = t.struct(
        {
            "metricAggregations": t.array(t.string()).optional(),
            "limit": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
        }
    ).named(renames["RunRealtimeReportRequestIn"])
    types["RunRealtimeReportRequestOut"] = t.struct(
        {
            "metricAggregations": t.array(t.string()).optional(),
            "limit": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportRequestOut"])

    functions = {}
    functions["propertiesGetMetadata"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "limit": t.string().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesBatchRunReports"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "limit": t.string().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesBatchRunPivotReports"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "limit": t.string().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunReport"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "limit": t.string().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesCheckCompatibility"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "limit": t.string().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunPivotReport"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "limit": t.string().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesRunRealtimeReport"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "limit": t.string().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="analyticsdata",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
