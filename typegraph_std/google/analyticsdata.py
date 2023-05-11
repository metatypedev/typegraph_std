from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_analyticsdata() -> Import:
    analyticsdata = HTTPRuntime("https://analyticsdata.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsdata_1_ErrorResponse",
        "MetricValueIn": "_analyticsdata_2_MetricValueIn",
        "MetricValueOut": "_analyticsdata_3_MetricValueOut",
        "PivotSelectionIn": "_analyticsdata_4_PivotSelectionIn",
        "PivotSelectionOut": "_analyticsdata_5_PivotSelectionOut",
        "CohortIn": "_analyticsdata_6_CohortIn",
        "CohortOut": "_analyticsdata_7_CohortOut",
        "DimensionMetadataIn": "_analyticsdata_8_DimensionMetadataIn",
        "DimensionMetadataOut": "_analyticsdata_9_DimensionMetadataOut",
        "ResponseMetaDataIn": "_analyticsdata_10_ResponseMetaDataIn",
        "ResponseMetaDataOut": "_analyticsdata_11_ResponseMetaDataOut",
        "DimensionExpressionIn": "_analyticsdata_12_DimensionExpressionIn",
        "DimensionExpressionOut": "_analyticsdata_13_DimensionExpressionOut",
        "RunRealtimeReportResponseIn": "_analyticsdata_14_RunRealtimeReportResponseIn",
        "RunRealtimeReportResponseOut": "_analyticsdata_15_RunRealtimeReportResponseOut",
        "SchemaRestrictionResponseIn": "_analyticsdata_16_SchemaRestrictionResponseIn",
        "SchemaRestrictionResponseOut": "_analyticsdata_17_SchemaRestrictionResponseOut",
        "BetweenFilterIn": "_analyticsdata_18_BetweenFilterIn",
        "BetweenFilterOut": "_analyticsdata_19_BetweenFilterOut",
        "MetricIn": "_analyticsdata_20_MetricIn",
        "MetricOut": "_analyticsdata_21_MetricOut",
        "NumericFilterIn": "_analyticsdata_22_NumericFilterIn",
        "NumericFilterOut": "_analyticsdata_23_NumericFilterOut",
        "RunReportResponseIn": "_analyticsdata_24_RunReportResponseIn",
        "RunReportResponseOut": "_analyticsdata_25_RunReportResponseOut",
        "FilterExpressionListIn": "_analyticsdata_26_FilterExpressionListIn",
        "FilterExpressionListOut": "_analyticsdata_27_FilterExpressionListOut",
        "CheckCompatibilityResponseIn": "_analyticsdata_28_CheckCompatibilityResponseIn",
        "CheckCompatibilityResponseOut": "_analyticsdata_29_CheckCompatibilityResponseOut",
        "MetricOrderByIn": "_analyticsdata_30_MetricOrderByIn",
        "MetricOrderByOut": "_analyticsdata_31_MetricOrderByOut",
        "RunPivotReportRequestIn": "_analyticsdata_32_RunPivotReportRequestIn",
        "RunPivotReportRequestOut": "_analyticsdata_33_RunPivotReportRequestOut",
        "CheckCompatibilityRequestIn": "_analyticsdata_34_CheckCompatibilityRequestIn",
        "CheckCompatibilityRequestOut": "_analyticsdata_35_CheckCompatibilityRequestOut",
        "MetricMetadataIn": "_analyticsdata_36_MetricMetadataIn",
        "MetricMetadataOut": "_analyticsdata_37_MetricMetadataOut",
        "DimensionValueIn": "_analyticsdata_38_DimensionValueIn",
        "DimensionValueOut": "_analyticsdata_39_DimensionValueOut",
        "RunRealtimeReportRequestIn": "_analyticsdata_40_RunRealtimeReportRequestIn",
        "RunRealtimeReportRequestOut": "_analyticsdata_41_RunRealtimeReportRequestOut",
        "RowIn": "_analyticsdata_42_RowIn",
        "RowOut": "_analyticsdata_43_RowOut",
        "RunPivotReportResponseIn": "_analyticsdata_44_RunPivotReportResponseIn",
        "RunPivotReportResponseOut": "_analyticsdata_45_RunPivotReportResponseOut",
        "OrderByIn": "_analyticsdata_46_OrderByIn",
        "OrderByOut": "_analyticsdata_47_OrderByOut",
        "FilterExpressionIn": "_analyticsdata_48_FilterExpressionIn",
        "FilterExpressionOut": "_analyticsdata_49_FilterExpressionOut",
        "CohortSpecIn": "_analyticsdata_50_CohortSpecIn",
        "CohortSpecOut": "_analyticsdata_51_CohortSpecOut",
        "PivotDimensionHeaderIn": "_analyticsdata_52_PivotDimensionHeaderIn",
        "PivotDimensionHeaderOut": "_analyticsdata_53_PivotDimensionHeaderOut",
        "ConcatenateExpressionIn": "_analyticsdata_54_ConcatenateExpressionIn",
        "ConcatenateExpressionOut": "_analyticsdata_55_ConcatenateExpressionOut",
        "MinuteRangeIn": "_analyticsdata_56_MinuteRangeIn",
        "MinuteRangeOut": "_analyticsdata_57_MinuteRangeOut",
        "FilterIn": "_analyticsdata_58_FilterIn",
        "FilterOut": "_analyticsdata_59_FilterOut",
        "MetadataIn": "_analyticsdata_60_MetadataIn",
        "MetadataOut": "_analyticsdata_61_MetadataOut",
        "RunReportRequestIn": "_analyticsdata_62_RunReportRequestIn",
        "RunReportRequestOut": "_analyticsdata_63_RunReportRequestOut",
        "ActiveMetricRestrictionIn": "_analyticsdata_64_ActiveMetricRestrictionIn",
        "ActiveMetricRestrictionOut": "_analyticsdata_65_ActiveMetricRestrictionOut",
        "PivotIn": "_analyticsdata_66_PivotIn",
        "PivotOut": "_analyticsdata_67_PivotOut",
        "StringFilterIn": "_analyticsdata_68_StringFilterIn",
        "StringFilterOut": "_analyticsdata_69_StringFilterOut",
        "DimensionOrderByIn": "_analyticsdata_70_DimensionOrderByIn",
        "DimensionOrderByOut": "_analyticsdata_71_DimensionOrderByOut",
        "QuotaStatusIn": "_analyticsdata_72_QuotaStatusIn",
        "QuotaStatusOut": "_analyticsdata_73_QuotaStatusOut",
        "BatchRunReportsRequestIn": "_analyticsdata_74_BatchRunReportsRequestIn",
        "BatchRunReportsRequestOut": "_analyticsdata_75_BatchRunReportsRequestOut",
        "DimensionHeaderIn": "_analyticsdata_76_DimensionHeaderIn",
        "DimensionHeaderOut": "_analyticsdata_77_DimensionHeaderOut",
        "PropertyQuotaIn": "_analyticsdata_78_PropertyQuotaIn",
        "PropertyQuotaOut": "_analyticsdata_79_PropertyQuotaOut",
        "MetricCompatibilityIn": "_analyticsdata_80_MetricCompatibilityIn",
        "MetricCompatibilityOut": "_analyticsdata_81_MetricCompatibilityOut",
        "PivotHeaderIn": "_analyticsdata_82_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsdata_83_PivotHeaderOut",
        "BatchRunPivotReportsRequestIn": "_analyticsdata_84_BatchRunPivotReportsRequestIn",
        "BatchRunPivotReportsRequestOut": "_analyticsdata_85_BatchRunPivotReportsRequestOut",
        "PivotOrderByIn": "_analyticsdata_86_PivotOrderByIn",
        "PivotOrderByOut": "_analyticsdata_87_PivotOrderByOut",
        "NumericValueIn": "_analyticsdata_88_NumericValueIn",
        "NumericValueOut": "_analyticsdata_89_NumericValueOut",
        "CohortReportSettingsIn": "_analyticsdata_90_CohortReportSettingsIn",
        "CohortReportSettingsOut": "_analyticsdata_91_CohortReportSettingsOut",
        "DimensionCompatibilityIn": "_analyticsdata_92_DimensionCompatibilityIn",
        "DimensionCompatibilityOut": "_analyticsdata_93_DimensionCompatibilityOut",
        "CaseExpressionIn": "_analyticsdata_94_CaseExpressionIn",
        "CaseExpressionOut": "_analyticsdata_95_CaseExpressionOut",
        "DimensionIn": "_analyticsdata_96_DimensionIn",
        "DimensionOut": "_analyticsdata_97_DimensionOut",
        "DateRangeIn": "_analyticsdata_98_DateRangeIn",
        "DateRangeOut": "_analyticsdata_99_DateRangeOut",
        "InListFilterIn": "_analyticsdata_100_InListFilterIn",
        "InListFilterOut": "_analyticsdata_101_InListFilterOut",
        "BatchRunReportsResponseIn": "_analyticsdata_102_BatchRunReportsResponseIn",
        "BatchRunReportsResponseOut": "_analyticsdata_103_BatchRunReportsResponseOut",
        "BatchRunPivotReportsResponseIn": "_analyticsdata_104_BatchRunPivotReportsResponseIn",
        "BatchRunPivotReportsResponseOut": "_analyticsdata_105_BatchRunPivotReportsResponseOut",
        "CohortsRangeIn": "_analyticsdata_106_CohortsRangeIn",
        "CohortsRangeOut": "_analyticsdata_107_CohortsRangeOut",
        "MetricHeaderIn": "_analyticsdata_108_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsdata_109_MetricHeaderOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MetricValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["MetricValueIn"]
    )
    types["MetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricValueOut"])
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
    types["DimensionMetadataIn"] = t.struct(
        {
            "description": t.string().optional(),
            "apiName": t.string().optional(),
            "customDefinition": t.boolean().optional(),
            "category": t.string().optional(),
            "uiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
        }
    ).named(renames["DimensionMetadataIn"])
    types["DimensionMetadataOut"] = t.struct(
        {
            "description": t.string().optional(),
            "apiName": t.string().optional(),
            "customDefinition": t.boolean().optional(),
            "category": t.string().optional(),
            "uiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionMetadataOut"])
    types["ResponseMetaDataIn"] = t.struct(
        {
            "subjectToThresholding": t.boolean().optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseIn"]
            ).optional(),
            "timeZone": t.string().optional(),
            "emptyReason": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["ResponseMetaDataIn"])
    types["ResponseMetaDataOut"] = t.struct(
        {
            "subjectToThresholding": t.boolean().optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "emptyReason": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseMetaDataOut"])
    types["DimensionExpressionIn"] = t.struct(
        {
            "lowerCase": t.proxy(renames["CaseExpressionIn"]).optional(),
            "upperCase": t.proxy(renames["CaseExpressionIn"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionIn"]).optional(),
        }
    ).named(renames["DimensionExpressionIn"])
    types["DimensionExpressionOut"] = t.struct(
        {
            "lowerCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "upperCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionExpressionOut"])
    types["RunRealtimeReportResponseIn"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "rowCount": t.integer().optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "kind": t.string().optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
        }
    ).named(renames["RunRealtimeReportResponseIn"])
    types["RunRealtimeReportResponseOut"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "rowCount": t.integer().optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "kind": t.string().optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportResponseOut"])
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
            "name": t.string().optional(),
            "invisible": t.boolean().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "name": t.string().optional(),
            "invisible": t.boolean().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
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
    types["RunReportResponseIn"] = t.struct(
        {
            "rowCount": t.integer().optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "kind": t.string().optional(),
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
        }
    ).named(renames["RunReportResponseIn"])
    types["RunReportResponseOut"] = t.struct(
        {
            "rowCount": t.integer().optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "kind": t.string().optional(),
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportResponseOut"])
    types["FilterExpressionListIn"] = t.struct(
        {"expressions": t.array(t.proxy(renames["FilterExpressionIn"])).optional()}
    ).named(renames["FilterExpressionListIn"])
    types["FilterExpressionListOut"] = t.struct(
        {
            "expressions": t.array(t.proxy(renames["FilterExpressionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionListOut"])
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
    types["MetricOrderByIn"] = t.struct({"metricName": t.string().optional()}).named(
        renames["MetricOrderByIn"]
    )
    types["MetricOrderByOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOrderByOut"])
    types["RunPivotReportRequestIn"] = t.struct(
        {
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "currencyCode": t.string().optional(),
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "property": t.string().optional(),
        }
    ).named(renames["RunPivotReportRequestIn"])
    types["RunPivotReportRequestOut"] = t.struct(
        {
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "currencyCode": t.string().optional(),
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "property": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportRequestOut"])
    types["CheckCompatibilityRequestIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "compatibilityFilter": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
        }
    ).named(renames["CheckCompatibilityRequestIn"])
    types["CheckCompatibilityRequestOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "compatibilityFilter": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckCompatibilityRequestOut"])
    types["MetricMetadataIn"] = t.struct(
        {
            "apiName": t.string().optional(),
            "category": t.string().optional(),
            "type": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "customDefinition": t.boolean().optional(),
            "uiName": t.string().optional(),
        }
    ).named(renames["MetricMetadataIn"])
    types["MetricMetadataOut"] = t.struct(
        {
            "apiName": t.string().optional(),
            "category": t.string().optional(),
            "type": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "customDefinition": t.boolean().optional(),
            "uiName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMetadataOut"])
    types["DimensionValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DimensionValueIn"]
    )
    types["DimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueOut"])
    types["RunRealtimeReportRequestIn"] = t.struct(
        {
            "limit": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
        }
    ).named(renames["RunRealtimeReportRequestIn"])
    types["RunRealtimeReportRequestOut"] = t.struct(
        {
            "limit": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeOut"])).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportRequestOut"])
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
    types["RunPivotReportResponseIn"] = t.struct(
        {
            "aggregates": t.array(t.proxy(renames["RowIn"])).optional(),
            "kind": t.string().optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderIn"])).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
        }
    ).named(renames["RunPivotReportResponseIn"])
    types["RunPivotReportResponseOut"] = t.struct(
        {
            "aggregates": t.array(t.proxy(renames["RowOut"])).optional(),
            "kind": t.string().optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderOut"])).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportResponseOut"])
    types["OrderByIn"] = t.struct(
        {
            "pivot": t.proxy(renames["PivotOrderByIn"]).optional(),
            "metric": t.proxy(renames["MetricOrderByIn"]).optional(),
            "desc": t.boolean().optional(),
            "dimension": t.proxy(renames["DimensionOrderByIn"]).optional(),
        }
    ).named(renames["OrderByIn"])
    types["OrderByOut"] = t.struct(
        {
            "pivot": t.proxy(renames["PivotOrderByOut"]).optional(),
            "metric": t.proxy(renames["MetricOrderByOut"]).optional(),
            "desc": t.boolean().optional(),
            "dimension": t.proxy(renames["DimensionOrderByOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderByOut"])
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
    types["CohortSpecIn"] = t.struct(
        {
            "cohortsRange": t.proxy(renames["CohortsRangeIn"]).optional(),
            "cohorts": t.array(t.proxy(renames["CohortIn"])).optional(),
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsIn"]
            ).optional(),
        }
    ).named(renames["CohortSpecIn"])
    types["CohortSpecOut"] = t.struct(
        {
            "cohortsRange": t.proxy(renames["CohortsRangeOut"]).optional(),
            "cohorts": t.array(t.proxy(renames["CohortOut"])).optional(),
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortSpecOut"])
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
    types["FilterIn"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "numericFilter": t.proxy(renames["NumericFilterIn"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterIn"]).optional(),
            "inListFilter": t.proxy(renames["InListFilterIn"]).optional(),
            "stringFilter": t.proxy(renames["StringFilterIn"]).optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "numericFilter": t.proxy(renames["NumericFilterOut"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterOut"]).optional(),
            "inListFilter": t.proxy(renames["InListFilterOut"]).optional(),
            "stringFilter": t.proxy(renames["StringFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
    types["MetadataIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricMetadataIn"])).optional(),
            "name": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionMetadataIn"])).optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricMetadataOut"])).optional(),
            "name": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionMetadataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["RunReportRequestIn"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "currencyCode": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "property": t.string().optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "offset": t.string().optional(),
            "limit": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "keepEmptyRows": t.boolean().optional(),
        }
    ).named(renames["RunReportRequestIn"])
    types["RunReportRequestOut"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "currencyCode": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "property": t.string().optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "offset": t.string().optional(),
            "limit": t.string().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportRequestOut"])
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
    types["PivotIn"] = t.struct(
        {
            "metricAggregations": t.array(t.string()).optional(),
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "fieldNames": t.array(t.string()).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
        }
    ).named(renames["PivotIn"])
    types["PivotOut"] = t.struct(
        {
            "metricAggregations": t.array(t.string()).optional(),
            "limit": t.string().optional(),
            "offset": t.string().optional(),
            "fieldNames": t.array(t.string()).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOut"])
    types["StringFilterIn"] = t.struct(
        {
            "value": t.string().optional(),
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
        }
    ).named(renames["StringFilterIn"])
    types["StringFilterOut"] = t.struct(
        {
            "value": t.string().optional(),
            "matchType": t.string().optional(),
            "caseSensitive": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringFilterOut"])
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
    types["QuotaStatusIn"] = t.struct(
        {"remaining": t.integer().optional(), "consumed": t.integer().optional()}
    ).named(renames["QuotaStatusIn"])
    types["QuotaStatusOut"] = t.struct(
        {
            "remaining": t.integer().optional(),
            "consumed": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaStatusOut"])
    types["BatchRunReportsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["RunReportRequestIn"])).optional()}
    ).named(renames["BatchRunReportsRequestIn"])
    types["BatchRunReportsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RunReportRequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunReportsRequestOut"])
    types["DimensionHeaderIn"] = t.struct({"name": t.string().optional()}).named(
        renames["DimensionHeaderIn"]
    )
    types["DimensionHeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionHeaderOut"])
    types["PropertyQuotaIn"] = t.struct(
        {
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusIn"]).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusIn"]).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
        }
    ).named(renames["PropertyQuotaIn"])
    types["PropertyQuotaOut"] = t.struct(
        {
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusOut"]).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusOut"]).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyQuotaOut"])
    types["MetricCompatibilityIn"] = t.struct(
        {
            "metricMetadata": t.proxy(renames["MetricMetadataIn"]).optional(),
            "compatibility": t.string().optional(),
        }
    ).named(renames["MetricCompatibilityIn"])
    types["MetricCompatibilityOut"] = t.struct(
        {
            "metricMetadata": t.proxy(renames["MetricMetadataOut"]).optional(),
            "compatibility": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricCompatibilityOut"])
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
    types["NumericValueIn"] = t.struct(
        {"int64Value": t.string().optional(), "doubleValue": t.number().optional()}
    ).named(renames["NumericValueIn"])
    types["NumericValueOut"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "doubleValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NumericValueOut"])
    types["CohortReportSettingsIn"] = t.struct(
        {"accumulate": t.boolean().optional()}
    ).named(renames["CohortReportSettingsIn"])
    types["CohortReportSettingsOut"] = t.struct(
        {
            "accumulate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortReportSettingsOut"])
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
    types["CaseExpressionIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["CaseExpressionIn"])
    types["CaseExpressionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseExpressionOut"])
    types["DimensionIn"] = t.struct(
        {
            "dimensionExpression": t.proxy(renames["DimensionExpressionIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DimensionIn"])
    types["DimensionOut"] = t.struct(
        {
            "dimensionExpression": t.proxy(
                renames["DimensionExpressionOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionOut"])
    types["DateRangeIn"] = t.struct(
        {
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DateRangeIn"])
    types["DateRangeOut"] = t.struct(
        {
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateRangeOut"])
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
    types["CohortsRangeIn"] = t.struct(
        {
            "endOffset": t.integer(),
            "granularity": t.string(),
            "startOffset": t.integer().optional(),
        }
    ).named(renames["CohortsRangeIn"])
    types["CohortsRangeOut"] = t.struct(
        {
            "endOffset": t.integer(),
            "granularity": t.string(),
            "startOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortsRangeOut"])
    types["MetricHeaderIn"] = t.struct(
        {"type": t.string().optional(), "name": t.string().optional()}
    ).named(renames["MetricHeaderIn"])
    types["MetricHeaderOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricHeaderOut"])

    functions = {}
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
        importer="analyticsdata", renames=renames, types=types, functions=functions
    )
