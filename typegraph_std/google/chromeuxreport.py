from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_chromeuxreport() -> Import:
    chromeuxreport = HTTPRuntime("https://chromeuxreport.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromeuxreport_1_ErrorResponse",
        "HistoryRecordIn": "_chromeuxreport_2_HistoryRecordIn",
        "HistoryRecordOut": "_chromeuxreport_3_HistoryRecordOut",
        "HistoryKeyIn": "_chromeuxreport_4_HistoryKeyIn",
        "HistoryKeyOut": "_chromeuxreport_5_HistoryKeyOut",
        "QueryResponseIn": "_chromeuxreport_6_QueryResponseIn",
        "QueryResponseOut": "_chromeuxreport_7_QueryResponseOut",
        "MetricIn": "_chromeuxreport_8_MetricIn",
        "MetricOut": "_chromeuxreport_9_MetricOut",
        "QueryHistoryResponseIn": "_chromeuxreport_10_QueryHistoryResponseIn",
        "QueryHistoryResponseOut": "_chromeuxreport_11_QueryHistoryResponseOut",
        "RecordIn": "_chromeuxreport_12_RecordIn",
        "RecordOut": "_chromeuxreport_13_RecordOut",
        "BinIn": "_chromeuxreport_14_BinIn",
        "BinOut": "_chromeuxreport_15_BinOut",
        "TimeseriesBinIn": "_chromeuxreport_16_TimeseriesBinIn",
        "TimeseriesBinOut": "_chromeuxreport_17_TimeseriesBinOut",
        "TimeseriesPercentilesIn": "_chromeuxreport_18_TimeseriesPercentilesIn",
        "TimeseriesPercentilesOut": "_chromeuxreport_19_TimeseriesPercentilesOut",
        "MetricTimeseriesIn": "_chromeuxreport_20_MetricTimeseriesIn",
        "MetricTimeseriesOut": "_chromeuxreport_21_MetricTimeseriesOut",
        "UrlNormalizationIn": "_chromeuxreport_22_UrlNormalizationIn",
        "UrlNormalizationOut": "_chromeuxreport_23_UrlNormalizationOut",
        "PercentilesIn": "_chromeuxreport_24_PercentilesIn",
        "PercentilesOut": "_chromeuxreport_25_PercentilesOut",
        "CollectionPeriodIn": "_chromeuxreport_26_CollectionPeriodIn",
        "CollectionPeriodOut": "_chromeuxreport_27_CollectionPeriodOut",
        "DateIn": "_chromeuxreport_28_DateIn",
        "DateOut": "_chromeuxreport_29_DateOut",
        "QueryHistoryRequestIn": "_chromeuxreport_30_QueryHistoryRequestIn",
        "QueryHistoryRequestOut": "_chromeuxreport_31_QueryHistoryRequestOut",
        "QueryRequestIn": "_chromeuxreport_32_QueryRequestIn",
        "QueryRequestOut": "_chromeuxreport_33_QueryRequestOut",
        "KeyIn": "_chromeuxreport_34_KeyIn",
        "KeyOut": "_chromeuxreport_35_KeyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HistoryRecordIn"] = t.struct(
        {
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "collectionPeriods": t.array(
                t.proxy(renames["CollectionPeriodIn"])
            ).optional(),
            "key": t.proxy(renames["HistoryKeyIn"]).optional(),
        }
    ).named(renames["HistoryRecordIn"])
    types["HistoryRecordOut"] = t.struct(
        {
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "collectionPeriods": t.array(
                t.proxy(renames["CollectionPeriodOut"])
            ).optional(),
            "key": t.proxy(renames["HistoryKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryRecordOut"])
    types["HistoryKeyIn"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["HistoryKeyIn"])
    types["HistoryKeyOut"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryKeyOut"])
    types["QueryResponseIn"] = t.struct(
        {
            "record": t.proxy(renames["RecordIn"]).optional(),
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationIn"]
            ).optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "record": t.proxy(renames["RecordOut"]).optional(),
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["MetricIn"] = t.struct(
        {
            "percentiles": t.proxy(renames["PercentilesIn"]).optional(),
            "histogram": t.array(t.proxy(renames["BinIn"])).optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "percentiles": t.proxy(renames["PercentilesOut"]).optional(),
            "histogram": t.array(t.proxy(renames["BinOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["QueryHistoryResponseIn"] = t.struct(
        {
            "record": t.proxy(renames["HistoryRecordIn"]).optional(),
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationIn"]
            ).optional(),
        }
    ).named(renames["QueryHistoryResponseIn"])
    types["QueryHistoryResponseOut"] = t.struct(
        {
            "record": t.proxy(renames["HistoryRecordOut"]).optional(),
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryHistoryResponseOut"])
    types["RecordIn"] = t.struct(
        {
            "key": t.proxy(renames["KeyIn"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "collectionPeriod": t.proxy(renames["CollectionPeriodIn"]).optional(),
        }
    ).named(renames["RecordIn"])
    types["RecordOut"] = t.struct(
        {
            "key": t.proxy(renames["KeyOut"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "collectionPeriod": t.proxy(renames["CollectionPeriodOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordOut"])
    types["BinIn"] = t.struct(
        {
            "start": t.struct({"_": t.string().optional()}).optional(),
            "density": t.number().optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BinIn"])
    types["BinOut"] = t.struct(
        {
            "start": t.struct({"_": t.string().optional()}).optional(),
            "density": t.number().optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinOut"])
    types["TimeseriesBinIn"] = t.struct(
        {
            "densities": t.array(t.number()).optional(),
            "start": t.struct({"_": t.string().optional()}).optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TimeseriesBinIn"])
    types["TimeseriesBinOut"] = t.struct(
        {
            "densities": t.array(t.number()).optional(),
            "start": t.struct({"_": t.string().optional()}).optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeseriesBinOut"])
    types["TimeseriesPercentilesIn"] = t.struct(
        {"p75s": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["TimeseriesPercentilesIn"])
    types["TimeseriesPercentilesOut"] = t.struct(
        {
            "p75s": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeseriesPercentilesOut"])
    types["MetricTimeseriesIn"] = t.struct(
        {
            "histogramTimeseries": t.array(
                t.proxy(renames["TimeseriesBinIn"])
            ).optional(),
            "percentilesTimeseries": t.proxy(
                renames["TimeseriesPercentilesIn"]
            ).optional(),
        }
    ).named(renames["MetricTimeseriesIn"])
    types["MetricTimeseriesOut"] = t.struct(
        {
            "histogramTimeseries": t.array(
                t.proxy(renames["TimeseriesBinOut"])
            ).optional(),
            "percentilesTimeseries": t.proxy(
                renames["TimeseriesPercentilesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricTimeseriesOut"])
    types["UrlNormalizationIn"] = t.struct(
        {"originalUrl": t.string().optional(), "normalizedUrl": t.string().optional()}
    ).named(renames["UrlNormalizationIn"])
    types["UrlNormalizationOut"] = t.struct(
        {
            "originalUrl": t.string().optional(),
            "normalizedUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlNormalizationOut"])
    types["PercentilesIn"] = t.struct(
        {"p75": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PercentilesIn"])
    types["PercentilesOut"] = t.struct(
        {
            "p75": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PercentilesOut"])
    types["CollectionPeriodIn"] = t.struct(
        {
            "firstDate": t.proxy(renames["DateIn"]).optional(),
            "lastDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CollectionPeriodIn"])
    types["CollectionPeriodOut"] = t.struct(
        {
            "firstDate": t.proxy(renames["DateOut"]).optional(),
            "lastDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionPeriodOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["QueryHistoryRequestIn"] = t.struct(
        {
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["QueryHistoryRequestIn"])
    types["QueryHistoryRequestOut"] = t.struct(
        {
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryHistoryRequestOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "effectiveConnectionType": t.string().optional(),
            "url": t.string().optional(),
            "origin": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "effectiveConnectionType": t.string().optional(),
            "url": t.string().optional(),
            "origin": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
    types["KeyIn"] = t.struct(
        {
            "effectiveConnectionType": t.string().optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["KeyIn"])
    types["KeyOut"] = t.struct(
        {
            "effectiveConnectionType": t.string().optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyOut"])

    functions = {}
    functions["recordsQueryHistoryRecord"] = chromeuxreport.post(
        "v1/records:queryRecord",
        t.struct(
            {
                "effectiveConnectionType": t.string().optional(),
                "url": t.string().optional(),
                "origin": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "formFactor": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["recordsQueryRecord"] = chromeuxreport.post(
        "v1/records:queryRecord",
        t.struct(
            {
                "effectiveConnectionType": t.string().optional(),
                "url": t.string().optional(),
                "origin": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "formFactor": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="chromeuxreport",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
