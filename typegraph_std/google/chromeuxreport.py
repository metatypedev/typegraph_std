from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_chromeuxreport() -> Import:
    chromeuxreport = HTTPRuntime("https://chromeuxreport.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromeuxreport_1_ErrorResponse",
        "QueryHistoryRequestIn": "_chromeuxreport_2_QueryHistoryRequestIn",
        "QueryHistoryRequestOut": "_chromeuxreport_3_QueryHistoryRequestOut",
        "CollectionPeriodIn": "_chromeuxreport_4_CollectionPeriodIn",
        "CollectionPeriodOut": "_chromeuxreport_5_CollectionPeriodOut",
        "QueryHistoryResponseIn": "_chromeuxreport_6_QueryHistoryResponseIn",
        "QueryHistoryResponseOut": "_chromeuxreport_7_QueryHistoryResponseOut",
        "QueryResponseIn": "_chromeuxreport_8_QueryResponseIn",
        "QueryResponseOut": "_chromeuxreport_9_QueryResponseOut",
        "QueryRequestIn": "_chromeuxreport_10_QueryRequestIn",
        "QueryRequestOut": "_chromeuxreport_11_QueryRequestOut",
        "HistoryRecordIn": "_chromeuxreport_12_HistoryRecordIn",
        "HistoryRecordOut": "_chromeuxreport_13_HistoryRecordOut",
        "TimeseriesBinIn": "_chromeuxreport_14_TimeseriesBinIn",
        "TimeseriesBinOut": "_chromeuxreport_15_TimeseriesBinOut",
        "TimeseriesPercentilesIn": "_chromeuxreport_16_TimeseriesPercentilesIn",
        "TimeseriesPercentilesOut": "_chromeuxreport_17_TimeseriesPercentilesOut",
        "DateIn": "_chromeuxreport_18_DateIn",
        "DateOut": "_chromeuxreport_19_DateOut",
        "UrlNormalizationIn": "_chromeuxreport_20_UrlNormalizationIn",
        "UrlNormalizationOut": "_chromeuxreport_21_UrlNormalizationOut",
        "KeyIn": "_chromeuxreport_22_KeyIn",
        "KeyOut": "_chromeuxreport_23_KeyOut",
        "BinIn": "_chromeuxreport_24_BinIn",
        "BinOut": "_chromeuxreport_25_BinOut",
        "PercentilesIn": "_chromeuxreport_26_PercentilesIn",
        "PercentilesOut": "_chromeuxreport_27_PercentilesOut",
        "MetricIn": "_chromeuxreport_28_MetricIn",
        "MetricOut": "_chromeuxreport_29_MetricOut",
        "HistoryKeyIn": "_chromeuxreport_30_HistoryKeyIn",
        "HistoryKeyOut": "_chromeuxreport_31_HistoryKeyOut",
        "MetricTimeseriesIn": "_chromeuxreport_32_MetricTimeseriesIn",
        "MetricTimeseriesOut": "_chromeuxreport_33_MetricTimeseriesOut",
        "RecordIn": "_chromeuxreport_34_RecordIn",
        "RecordOut": "_chromeuxreport_35_RecordOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["QueryHistoryRequestIn"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "origin": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["QueryHistoryRequestIn"])
    types["QueryHistoryRequestOut"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "origin": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryHistoryRequestOut"])
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
    types["QueryResponseIn"] = t.struct(
        {
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationIn"]
            ).optional(),
            "record": t.proxy(renames["RecordIn"]).optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationOut"]
            ).optional(),
            "record": t.proxy(renames["RecordOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
    types["HistoryRecordIn"] = t.struct(
        {
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "key": t.proxy(renames["HistoryKeyIn"]).optional(),
            "collectionPeriods": t.array(
                t.proxy(renames["CollectionPeriodIn"])
            ).optional(),
        }
    ).named(renames["HistoryRecordIn"])
    types["HistoryRecordOut"] = t.struct(
        {
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "key": t.proxy(renames["HistoryKeyOut"]).optional(),
            "collectionPeriods": t.array(
                t.proxy(renames["CollectionPeriodOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryRecordOut"])
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
    types["UrlNormalizationIn"] = t.struct(
        {"normalizedUrl": t.string().optional(), "originalUrl": t.string().optional()}
    ).named(renames["UrlNormalizationIn"])
    types["UrlNormalizationOut"] = t.struct(
        {
            "normalizedUrl": t.string().optional(),
            "originalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlNormalizationOut"])
    types["KeyIn"] = t.struct(
        {
            "effectiveConnectionType": t.string().optional(),
            "url": t.string().optional(),
            "origin": t.string().optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["KeyIn"])
    types["KeyOut"] = t.struct(
        {
            "effectiveConnectionType": t.string().optional(),
            "url": t.string().optional(),
            "origin": t.string().optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyOut"])
    types["BinIn"] = t.struct(
        {
            "start": t.struct({"_": t.string().optional()}).optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
            "density": t.number().optional(),
        }
    ).named(renames["BinIn"])
    types["BinOut"] = t.struct(
        {
            "start": t.struct({"_": t.string().optional()}).optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
            "density": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinOut"])
    types["PercentilesIn"] = t.struct(
        {"p75": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PercentilesIn"])
    types["PercentilesOut"] = t.struct(
        {
            "p75": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PercentilesOut"])
    types["MetricIn"] = t.struct(
        {
            "histogram": t.array(t.proxy(renames["BinIn"])).optional(),
            "percentiles": t.proxy(renames["PercentilesIn"]).optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "histogram": t.array(t.proxy(renames["BinOut"])).optional(),
            "percentiles": t.proxy(renames["PercentilesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["HistoryKeyIn"] = t.struct(
        {
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
            "origin": t.string().optional(),
        }
    ).named(renames["HistoryKeyIn"])
    types["HistoryKeyOut"] = t.struct(
        {
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
            "origin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryKeyOut"])
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

    functions = {}
    functions["recordsQueryRecord"] = chromeuxreport.post(
        "v1/records:queryHistoryRecord",
        t.struct(
            {
                "formFactor": t.string().optional(),
                "origin": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["recordsQueryHistoryRecord"] = chromeuxreport.post(
        "v1/records:queryHistoryRecord",
        t.struct(
            {
                "formFactor": t.string().optional(),
                "origin": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryHistoryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="chromeuxreport", renames=renames, types=types, functions=functions
    )
