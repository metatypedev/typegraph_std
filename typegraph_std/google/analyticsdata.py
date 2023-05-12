from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_analyticsdata() -> Import:
    analyticsdata = HTTPRuntime("https://analyticsdata.googleapis.com/")

    renames = {
        "ErrorResponse": "_analyticsdata_1_ErrorResponse",
        "RunPivotReportRequestIn": "_analyticsdata_2_RunPivotReportRequestIn",
        "RunPivotReportRequestOut": "_analyticsdata_3_RunPivotReportRequestOut",
        "CaseExpressionIn": "_analyticsdata_4_CaseExpressionIn",
        "CaseExpressionOut": "_analyticsdata_5_CaseExpressionOut",
        "MetadataIn": "_analyticsdata_6_MetadataIn",
        "MetadataOut": "_analyticsdata_7_MetadataOut",
        "NumericFilterIn": "_analyticsdata_8_NumericFilterIn",
        "NumericFilterOut": "_analyticsdata_9_NumericFilterOut",
        "DimensionValueIn": "_analyticsdata_10_DimensionValueIn",
        "DimensionValueOut": "_analyticsdata_11_DimensionValueOut",
        "RunReportRequestIn": "_analyticsdata_12_RunReportRequestIn",
        "RunReportRequestOut": "_analyticsdata_13_RunReportRequestOut",
        "FilterExpressionIn": "_analyticsdata_14_FilterExpressionIn",
        "FilterExpressionOut": "_analyticsdata_15_FilterExpressionOut",
        "InListFilterIn": "_analyticsdata_16_InListFilterIn",
        "InListFilterOut": "_analyticsdata_17_InListFilterOut",
        "OrderByIn": "_analyticsdata_18_OrderByIn",
        "OrderByOut": "_analyticsdata_19_OrderByOut",
        "RunReportResponseIn": "_analyticsdata_20_RunReportResponseIn",
        "RunReportResponseOut": "_analyticsdata_21_RunReportResponseOut",
        "DimensionCompatibilityIn": "_analyticsdata_22_DimensionCompatibilityIn",
        "DimensionCompatibilityOut": "_analyticsdata_23_DimensionCompatibilityOut",
        "DateRangeIn": "_analyticsdata_24_DateRangeIn",
        "DateRangeOut": "_analyticsdata_25_DateRangeOut",
        "DimensionHeaderIn": "_analyticsdata_26_DimensionHeaderIn",
        "DimensionHeaderOut": "_analyticsdata_27_DimensionHeaderOut",
        "CheckCompatibilityRequestIn": "_analyticsdata_28_CheckCompatibilityRequestIn",
        "CheckCompatibilityRequestOut": "_analyticsdata_29_CheckCompatibilityRequestOut",
        "CohortReportSettingsIn": "_analyticsdata_30_CohortReportSettingsIn",
        "CohortReportSettingsOut": "_analyticsdata_31_CohortReportSettingsOut",
        "MetricCompatibilityIn": "_analyticsdata_32_MetricCompatibilityIn",
        "MetricCompatibilityOut": "_analyticsdata_33_MetricCompatibilityOut",
        "QuotaStatusIn": "_analyticsdata_34_QuotaStatusIn",
        "QuotaStatusOut": "_analyticsdata_35_QuotaStatusOut",
        "PivotHeaderIn": "_analyticsdata_36_PivotHeaderIn",
        "PivotHeaderOut": "_analyticsdata_37_PivotHeaderOut",
        "NumericValueIn": "_analyticsdata_38_NumericValueIn",
        "NumericValueOut": "_analyticsdata_39_NumericValueOut",
        "MinuteRangeIn": "_analyticsdata_40_MinuteRangeIn",
        "MinuteRangeOut": "_analyticsdata_41_MinuteRangeOut",
        "MetricValueIn": "_analyticsdata_42_MetricValueIn",
        "MetricValueOut": "_analyticsdata_43_MetricValueOut",
        "RunRealtimeReportRequestIn": "_analyticsdata_44_RunRealtimeReportRequestIn",
        "RunRealtimeReportRequestOut": "_analyticsdata_45_RunRealtimeReportRequestOut",
        "DimensionOrderByIn": "_analyticsdata_46_DimensionOrderByIn",
        "DimensionOrderByOut": "_analyticsdata_47_DimensionOrderByOut",
        "PivotDimensionHeaderIn": "_analyticsdata_48_PivotDimensionHeaderIn",
        "PivotDimensionHeaderOut": "_analyticsdata_49_PivotDimensionHeaderOut",
        "MetricIn": "_analyticsdata_50_MetricIn",
        "MetricOut": "_analyticsdata_51_MetricOut",
        "CohortSpecIn": "_analyticsdata_52_CohortSpecIn",
        "CohortSpecOut": "_analyticsdata_53_CohortSpecOut",
        "FilterExpressionListIn": "_analyticsdata_54_FilterExpressionListIn",
        "FilterExpressionListOut": "_analyticsdata_55_FilterExpressionListOut",
        "CheckCompatibilityResponseIn": "_analyticsdata_56_CheckCompatibilityResponseIn",
        "CheckCompatibilityResponseOut": "_analyticsdata_57_CheckCompatibilityResponseOut",
        "DimensionIn": "_analyticsdata_58_DimensionIn",
        "DimensionOut": "_analyticsdata_59_DimensionOut",
        "ConcatenateExpressionIn": "_analyticsdata_60_ConcatenateExpressionIn",
        "ConcatenateExpressionOut": "_analyticsdata_61_ConcatenateExpressionOut",
        "DimensionMetadataIn": "_analyticsdata_62_DimensionMetadataIn",
        "DimensionMetadataOut": "_analyticsdata_63_DimensionMetadataOut",
        "PivotOrderByIn": "_analyticsdata_64_PivotOrderByIn",
        "PivotOrderByOut": "_analyticsdata_65_PivotOrderByOut",
        "ResponseMetaDataIn": "_analyticsdata_66_ResponseMetaDataIn",
        "ResponseMetaDataOut": "_analyticsdata_67_ResponseMetaDataOut",
        "RunPivotReportResponseIn": "_analyticsdata_68_RunPivotReportResponseIn",
        "RunPivotReportResponseOut": "_analyticsdata_69_RunPivotReportResponseOut",
        "BatchRunPivotReportsRequestIn": "_analyticsdata_70_BatchRunPivotReportsRequestIn",
        "BatchRunPivotReportsRequestOut": "_analyticsdata_71_BatchRunPivotReportsRequestOut",
        "DimensionExpressionIn": "_analyticsdata_72_DimensionExpressionIn",
        "DimensionExpressionOut": "_analyticsdata_73_DimensionExpressionOut",
        "CohortsRangeIn": "_analyticsdata_74_CohortsRangeIn",
        "CohortsRangeOut": "_analyticsdata_75_CohortsRangeOut",
        "RunRealtimeReportResponseIn": "_analyticsdata_76_RunRealtimeReportResponseIn",
        "RunRealtimeReportResponseOut": "_analyticsdata_77_RunRealtimeReportResponseOut",
        "PivotSelectionIn": "_analyticsdata_78_PivotSelectionIn",
        "PivotSelectionOut": "_analyticsdata_79_PivotSelectionOut",
        "FilterIn": "_analyticsdata_80_FilterIn",
        "FilterOut": "_analyticsdata_81_FilterOut",
        "MetricHeaderIn": "_analyticsdata_82_MetricHeaderIn",
        "MetricHeaderOut": "_analyticsdata_83_MetricHeaderOut",
        "BatchRunReportsRequestIn": "_analyticsdata_84_BatchRunReportsRequestIn",
        "BatchRunReportsRequestOut": "_analyticsdata_85_BatchRunReportsRequestOut",
        "MetricOrderByIn": "_analyticsdata_86_MetricOrderByIn",
        "MetricOrderByOut": "_analyticsdata_87_MetricOrderByOut",
        "CohortIn": "_analyticsdata_88_CohortIn",
        "CohortOut": "_analyticsdata_89_CohortOut",
        "SchemaRestrictionResponseIn": "_analyticsdata_90_SchemaRestrictionResponseIn",
        "SchemaRestrictionResponseOut": "_analyticsdata_91_SchemaRestrictionResponseOut",
        "PropertyQuotaIn": "_analyticsdata_92_PropertyQuotaIn",
        "PropertyQuotaOut": "_analyticsdata_93_PropertyQuotaOut",
        "BatchRunPivotReportsResponseIn": "_analyticsdata_94_BatchRunPivotReportsResponseIn",
        "BatchRunPivotReportsResponseOut": "_analyticsdata_95_BatchRunPivotReportsResponseOut",
        "BetweenFilterIn": "_analyticsdata_96_BetweenFilterIn",
        "BetweenFilterOut": "_analyticsdata_97_BetweenFilterOut",
        "RowIn": "_analyticsdata_98_RowIn",
        "RowOut": "_analyticsdata_99_RowOut",
        "ActiveMetricRestrictionIn": "_analyticsdata_100_ActiveMetricRestrictionIn",
        "ActiveMetricRestrictionOut": "_analyticsdata_101_ActiveMetricRestrictionOut",
        "MetricMetadataIn": "_analyticsdata_102_MetricMetadataIn",
        "MetricMetadataOut": "_analyticsdata_103_MetricMetadataOut",
        "BatchRunReportsResponseIn": "_analyticsdata_104_BatchRunReportsResponseIn",
        "BatchRunReportsResponseOut": "_analyticsdata_105_BatchRunReportsResponseOut",
        "StringFilterIn": "_analyticsdata_106_StringFilterIn",
        "StringFilterOut": "_analyticsdata_107_StringFilterOut",
        "PivotIn": "_analyticsdata_108_PivotIn",
        "PivotOut": "_analyticsdata_109_PivotOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RunPivotReportRequestIn"] = t.struct(
        {
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "pivots": t.array(t.proxy(renames["PivotIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "property": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "currencyCode": t.string().optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
        }
    ).named(renames["RunPivotReportRequestIn"])
    types["RunPivotReportRequestOut"] = t.struct(
        {
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "pivots": t.array(t.proxy(renames["PivotOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "property": t.string().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "keepEmptyRows": t.boolean().optional(),
            "currencyCode": t.string().optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportRequestOut"])
    types["CaseExpressionIn"] = t.struct(
        {"dimensionName": t.string().optional()}
    ).named(renames["CaseExpressionIn"])
    types["CaseExpressionOut"] = t.struct(
        {
            "dimensionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseExpressionOut"])
    types["MetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricMetadataIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionMetadataIn"])).optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricMetadataOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionMetadataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["DimensionValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["DimensionValueIn"]
    )
    types["DimensionValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionValueOut"])
    types["RunReportRequestIn"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "limit": t.string().optional(),
            "keepEmptyRows": t.boolean().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeIn"])).optional(),
            "currencyCode": t.string().optional(),
            "property": t.string().optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "offset": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
        }
    ).named(renames["RunReportRequestIn"])
    types["RunReportRequestOut"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "limit": t.string().optional(),
            "keepEmptyRows": t.boolean().optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "dateRanges": t.array(t.proxy(renames["DateRangeOut"])).optional(),
            "currencyCode": t.string().optional(),
            "property": t.string().optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "offset": t.string().optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "cohortSpec": t.proxy(renames["CohortSpecOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportRequestOut"])
    types["FilterExpressionIn"] = t.struct(
        {
            "filter": t.proxy(renames["FilterIn"]).optional(),
            "notExpression": t.proxy(renames["FilterExpressionIn"]).optional(),
            "andGroup": t.proxy(renames["FilterExpressionListIn"]).optional(),
            "orGroup": t.proxy(renames["FilterExpressionListIn"]).optional(),
        }
    ).named(renames["FilterExpressionIn"])
    types["FilterExpressionOut"] = t.struct(
        {
            "filter": t.proxy(renames["FilterOut"]).optional(),
            "notExpression": t.proxy(renames["FilterExpressionOut"]).optional(),
            "andGroup": t.proxy(renames["FilterExpressionListOut"]).optional(),
            "orGroup": t.proxy(renames["FilterExpressionListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterExpressionOut"])
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
    types["OrderByIn"] = t.struct(
        {
            "dimension": t.proxy(renames["DimensionOrderByIn"]).optional(),
            "desc": t.boolean().optional(),
            "metric": t.proxy(renames["MetricOrderByIn"]).optional(),
            "pivot": t.proxy(renames["PivotOrderByIn"]).optional(),
        }
    ).named(renames["OrderByIn"])
    types["OrderByOut"] = t.struct(
        {
            "dimension": t.proxy(renames["DimensionOrderByOut"]).optional(),
            "desc": t.boolean().optional(),
            "metric": t.proxy(renames["MetricOrderByOut"]).optional(),
            "pivot": t.proxy(renames["PivotOrderByOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrderByOut"])
    types["RunReportResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "rowCount": t.integer().optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
        }
    ).named(renames["RunReportResponseIn"])
    types["RunReportResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "rowCount": t.integer().optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunReportResponseOut"])
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
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "compatibilityFilter": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
        }
    ).named(renames["CheckCompatibilityRequestIn"])
    types["CheckCompatibilityRequestOut"] = t.struct(
        {
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "compatibilityFilter": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckCompatibilityRequestOut"])
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
    types["MinuteRangeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "endMinutesAgo": t.integer().optional(),
            "startMinutesAgo": t.integer().optional(),
        }
    ).named(renames["MinuteRangeIn"])
    types["MinuteRangeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "endMinutesAgo": t.integer().optional(),
            "startMinutesAgo": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinuteRangeOut"])
    types["MetricValueIn"] = t.struct({"value": t.string().optional()}).named(
        renames["MetricValueIn"]
    )
    types["MetricValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricValueOut"])
    types["RunRealtimeReportRequestIn"] = t.struct(
        {
            "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "limit": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
        }
    ).named(renames["RunRealtimeReportRequestIn"])
    types["RunRealtimeReportRequestOut"] = t.struct(
        {
            "metricFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "limit": t.string().optional(),
            "dimensionFilter": t.proxy(renames["FilterExpressionOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "returnPropertyQuota": t.boolean().optional(),
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "minuteRanges": t.array(t.proxy(renames["MinuteRangeOut"])).optional(),
            "dimensions": t.array(t.proxy(renames["DimensionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportRequestOut"])
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
    types["MetricIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "name": t.string().optional(),
            "invisible": t.boolean().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "name": t.string().optional(),
            "invisible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["CohortSpecIn"] = t.struct(
        {
            "cohorts": t.array(t.proxy(renames["CohortIn"])).optional(),
            "cohortsRange": t.proxy(renames["CohortsRangeIn"]).optional(),
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsIn"]
            ).optional(),
        }
    ).named(renames["CohortSpecIn"])
    types["CohortSpecOut"] = t.struct(
        {
            "cohorts": t.array(t.proxy(renames["CohortOut"])).optional(),
            "cohortsRange": t.proxy(renames["CohortsRangeOut"]).optional(),
            "cohortReportSettings": t.proxy(
                renames["CohortReportSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortSpecOut"])
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
            "dimensionCompatibilities": t.array(
                t.proxy(renames["DimensionCompatibilityIn"])
            ).optional(),
            "metricCompatibilities": t.array(
                t.proxy(renames["MetricCompatibilityIn"])
            ).optional(),
        }
    ).named(renames["CheckCompatibilityResponseIn"])
    types["CheckCompatibilityResponseOut"] = t.struct(
        {
            "dimensionCompatibilities": t.array(
                t.proxy(renames["DimensionCompatibilityOut"])
            ).optional(),
            "metricCompatibilities": t.array(
                t.proxy(renames["MetricCompatibilityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckCompatibilityResponseOut"])
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
    types["DimensionMetadataIn"] = t.struct(
        {
            "deprecatedApiNames": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "apiName": t.string().optional(),
            "description": t.string().optional(),
            "uiName": t.string().optional(),
            "customDefinition": t.boolean().optional(),
        }
    ).named(renames["DimensionMetadataIn"])
    types["DimensionMetadataOut"] = t.struct(
        {
            "deprecatedApiNames": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "apiName": t.string().optional(),
            "description": t.string().optional(),
            "uiName": t.string().optional(),
            "customDefinition": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionMetadataOut"])
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
    types["ResponseMetaDataIn"] = t.struct(
        {
            "emptyReason": t.string().optional(),
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseIn"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "timeZone": t.string().optional(),
            "subjectToThresholding": t.boolean().optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
        }
    ).named(renames["ResponseMetaDataIn"])
    types["ResponseMetaDataOut"] = t.struct(
        {
            "emptyReason": t.string().optional(),
            "schemaRestrictionResponse": t.proxy(
                renames["SchemaRestrictionResponseOut"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "timeZone": t.string().optional(),
            "subjectToThresholding": t.boolean().optional(),
            "dataLossFromOtherRow": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseMetaDataOut"])
    types["RunPivotReportResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataIn"]).optional(),
            "aggregates": t.array(t.proxy(renames["RowIn"])).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderIn"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
        }
    ).named(renames["RunPivotReportResponseIn"])
    types["RunPivotReportResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "metadata": t.proxy(renames["ResponseMetaDataOut"]).optional(),
            "aggregates": t.array(t.proxy(renames["RowOut"])).optional(),
            "pivotHeaders": t.array(t.proxy(renames["PivotHeaderOut"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunPivotReportResponseOut"])
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
    types["DimensionExpressionIn"] = t.struct(
        {
            "upperCase": t.proxy(renames["CaseExpressionIn"]).optional(),
            "lowerCase": t.proxy(renames["CaseExpressionIn"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionIn"]).optional(),
        }
    ).named(renames["DimensionExpressionIn"])
    types["DimensionExpressionOut"] = t.struct(
        {
            "upperCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "lowerCase": t.proxy(renames["CaseExpressionOut"]).optional(),
            "concatenate": t.proxy(renames["ConcatenateExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionExpressionOut"])
    types["CohortsRangeIn"] = t.struct(
        {
            "startOffset": t.integer().optional(),
            "granularity": t.string(),
            "endOffset": t.integer(),
        }
    ).named(renames["CohortsRangeIn"])
    types["CohortsRangeOut"] = t.struct(
        {
            "startOffset": t.integer().optional(),
            "granularity": t.string(),
            "endOffset": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortsRangeOut"])
    types["RunRealtimeReportResponseIn"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["RowIn"])).optional(),
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "rowCount": t.integer().optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderIn"])
            ).optional(),
            "totals": t.array(t.proxy(renames["RowIn"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaIn"]).optional(),
            "minimums": t.array(t.proxy(renames["RowIn"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["RunRealtimeReportResponseIn"])
    types["RunRealtimeReportResponseOut"] = t.struct(
        {
            "maximums": t.array(t.proxy(renames["RowOut"])).optional(),
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "rowCount": t.integer().optional(),
            "dimensionHeaders": t.array(
                t.proxy(renames["DimensionHeaderOut"])
            ).optional(),
            "totals": t.array(t.proxy(renames["RowOut"])).optional(),
            "propertyQuota": t.proxy(renames["PropertyQuotaOut"]).optional(),
            "minimums": t.array(t.proxy(renames["RowOut"])).optional(),
            "metricHeaders": t.array(t.proxy(renames["MetricHeaderOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunRealtimeReportResponseOut"])
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
    types["FilterIn"] = t.struct(
        {
            "numericFilter": t.proxy(renames["NumericFilterIn"]).optional(),
            "stringFilter": t.proxy(renames["StringFilterIn"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterIn"]).optional(),
            "inListFilter": t.proxy(renames["InListFilterIn"]).optional(),
            "fieldName": t.string().optional(),
        }
    ).named(renames["FilterIn"])
    types["FilterOut"] = t.struct(
        {
            "numericFilter": t.proxy(renames["NumericFilterOut"]).optional(),
            "stringFilter": t.proxy(renames["StringFilterOut"]).optional(),
            "betweenFilter": t.proxy(renames["BetweenFilterOut"]).optional(),
            "inListFilter": t.proxy(renames["InListFilterOut"]).optional(),
            "fieldName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterOut"])
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
    types["BatchRunReportsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["RunReportRequestIn"])).optional()}
    ).named(renames["BatchRunReportsRequestIn"])
    types["BatchRunReportsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["RunReportRequestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchRunReportsRequestOut"])
    types["MetricOrderByIn"] = t.struct({"metricName": t.string().optional()}).named(
        renames["MetricOrderByIn"]
    )
    types["MetricOrderByOut"] = t.struct(
        {
            "metricName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOrderByOut"])
    types["CohortIn"] = t.struct(
        {
            "dimension": t.string().optional(),
            "name": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeIn"]).optional(),
        }
    ).named(renames["CohortIn"])
    types["CohortOut"] = t.struct(
        {
            "dimension": t.string().optional(),
            "name": t.string().optional(),
            "dateRange": t.proxy(renames["DateRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CohortOut"])
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
    types["PropertyQuotaIn"] = t.struct(
        {
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusIn"]).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusIn"]
            ).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusIn"]).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusIn"]).optional(),
        }
    ).named(renames["PropertyQuotaIn"])
    types["PropertyQuotaOut"] = t.struct(
        {
            "potentiallyThresholdedRequestsPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "concurrentRequests": t.proxy(renames["QuotaStatusOut"]).optional(),
            "tokensPerProjectPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "serverErrorsPerProjectPerHour": t.proxy(
                renames["QuotaStatusOut"]
            ).optional(),
            "tokensPerHour": t.proxy(renames["QuotaStatusOut"]).optional(),
            "tokensPerDay": t.proxy(renames["QuotaStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyQuotaOut"])
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
    types["MetricMetadataIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "uiName": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "customDefinition": t.boolean().optional(),
            "apiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
        }
    ).named(renames["MetricMetadataIn"])
    types["MetricMetadataOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "uiName": t.string().optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "blockedReasons": t.array(t.string()).optional(),
            "customDefinition": t.boolean().optional(),
            "apiName": t.string().optional(),
            "deprecatedApiNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMetadataOut"])
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
    types["PivotIn"] = t.struct(
        {
            "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
            "fieldNames": t.array(t.string()).optional(),
            "offset": t.string().optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "limit": t.string().optional(),
        }
    ).named(renames["PivotIn"])
    types["PivotOut"] = t.struct(
        {
            "orderBys": t.array(t.proxy(renames["OrderByOut"])).optional(),
            "fieldNames": t.array(t.string()).optional(),
            "offset": t.string().optional(),
            "metricAggregations": t.array(t.string()).optional(),
            "limit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PivotOut"])

    functions = {}
    functions["propertiesBatchRunReports"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "limit": t.string().optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
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
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "limit": t.string().optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
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
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "limit": t.string().optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
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
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "limit": t.string().optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RunRealtimeReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["propertiesGetMetadata"] = analyticsdata.post(
        "v1beta/{property}:runRealtimeReport",
        t.struct(
            {
                "property": t.string().optional(),
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "limit": t.string().optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
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
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "limit": t.string().optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
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
                "metricFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "limit": t.string().optional(),
                "dimensionFilter": t.proxy(renames["FilterExpressionIn"]).optional(),
                "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
                "metricAggregations": t.array(t.string()).optional(),
                "returnPropertyQuota": t.boolean().optional(),
                "orderBys": t.array(t.proxy(renames["OrderByIn"])).optional(),
                "minuteRanges": t.array(t.proxy(renames["MinuteRangeIn"])).optional(),
                "dimensions": t.array(t.proxy(renames["DimensionIn"])).optional(),
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
