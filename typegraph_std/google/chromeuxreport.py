from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_chromeuxreport():
    chromeuxreport = HTTPRuntime("https://chromeuxreport.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromeuxreport_1_ErrorResponse",
        "QueryResponseIn": "_chromeuxreport_2_QueryResponseIn",
        "QueryResponseOut": "_chromeuxreport_3_QueryResponseOut",
        "CollectionPeriodIn": "_chromeuxreport_4_CollectionPeriodIn",
        "CollectionPeriodOut": "_chromeuxreport_5_CollectionPeriodOut",
        "QueryHistoryRequestIn": "_chromeuxreport_6_QueryHistoryRequestIn",
        "QueryHistoryRequestOut": "_chromeuxreport_7_QueryHistoryRequestOut",
        "RecordIn": "_chromeuxreport_8_RecordIn",
        "RecordOut": "_chromeuxreport_9_RecordOut",
        "HistoryKeyIn": "_chromeuxreport_10_HistoryKeyIn",
        "HistoryKeyOut": "_chromeuxreport_11_HistoryKeyOut",
        "PercentilesIn": "_chromeuxreport_12_PercentilesIn",
        "PercentilesOut": "_chromeuxreport_13_PercentilesOut",
        "BinIn": "_chromeuxreport_14_BinIn",
        "BinOut": "_chromeuxreport_15_BinOut",
        "QueryHistoryResponseIn": "_chromeuxreport_16_QueryHistoryResponseIn",
        "QueryHistoryResponseOut": "_chromeuxreport_17_QueryHistoryResponseOut",
        "DateIn": "_chromeuxreport_18_DateIn",
        "DateOut": "_chromeuxreport_19_DateOut",
        "TimeseriesBinIn": "_chromeuxreport_20_TimeseriesBinIn",
        "TimeseriesBinOut": "_chromeuxreport_21_TimeseriesBinOut",
        "MetricIn": "_chromeuxreport_22_MetricIn",
        "MetricOut": "_chromeuxreport_23_MetricOut",
        "KeyIn": "_chromeuxreport_24_KeyIn",
        "KeyOut": "_chromeuxreport_25_KeyOut",
        "UrlNormalizationIn": "_chromeuxreport_26_UrlNormalizationIn",
        "UrlNormalizationOut": "_chromeuxreport_27_UrlNormalizationOut",
        "MetricTimeseriesIn": "_chromeuxreport_28_MetricTimeseriesIn",
        "MetricTimeseriesOut": "_chromeuxreport_29_MetricTimeseriesOut",
        "HistoryRecordIn": "_chromeuxreport_30_HistoryRecordIn",
        "HistoryRecordOut": "_chromeuxreport_31_HistoryRecordOut",
        "TimeseriesPercentilesIn": "_chromeuxreport_32_TimeseriesPercentilesIn",
        "TimeseriesPercentilesOut": "_chromeuxreport_33_TimeseriesPercentilesOut",
        "QueryRequestIn": "_chromeuxreport_34_QueryRequestIn",
        "QueryRequestOut": "_chromeuxreport_35_QueryRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["CollectionPeriodIn"] = t.struct(
        {
            "lastDate": t.proxy(renames["DateIn"]).optional(),
            "firstDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["CollectionPeriodIn"])
    types["CollectionPeriodOut"] = t.struct(
        {
            "lastDate": t.proxy(renames["DateOut"]).optional(),
            "firstDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CollectionPeriodOut"])
    types["QueryHistoryRequestIn"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
        }
    ).named(renames["QueryHistoryRequestIn"])
    types["QueryHistoryRequestOut"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryHistoryRequestOut"])
    types["RecordIn"] = t.struct(
        {
            "collectionPeriod": t.proxy(renames["CollectionPeriodIn"]).optional(),
            "key": t.proxy(renames["KeyIn"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RecordIn"])
    types["RecordOut"] = t.struct(
        {
            "collectionPeriod": t.proxy(renames["CollectionPeriodOut"]).optional(),
            "key": t.proxy(renames["KeyOut"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordOut"])
    types["HistoryKeyIn"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
            "origin": t.string().optional(),
        }
    ).named(renames["HistoryKeyIn"])
    types["HistoryKeyOut"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
            "origin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryKeyOut"])
    types["PercentilesIn"] = t.struct(
        {"p75": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PercentilesIn"])
    types["PercentilesOut"] = t.struct(
        {
            "p75": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PercentilesOut"])
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
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["TimeseriesBinIn"] = t.struct(
        {
            "start": t.struct({"_": t.string().optional()}).optional(),
            "densities": t.array(t.number()).optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TimeseriesBinIn"])
    types["TimeseriesBinOut"] = t.struct(
        {
            "start": t.struct({"_": t.string().optional()}).optional(),
            "densities": t.array(t.number()).optional(),
            "end": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeseriesBinOut"])
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
    types["MetricTimeseriesIn"] = t.struct(
        {
            "percentilesTimeseries": t.proxy(
                renames["TimeseriesPercentilesIn"]
            ).optional(),
            "histogramTimeseries": t.array(
                t.proxy(renames["TimeseriesBinIn"])
            ).optional(),
        }
    ).named(renames["MetricTimeseriesIn"])
    types["MetricTimeseriesOut"] = t.struct(
        {
            "percentilesTimeseries": t.proxy(
                renames["TimeseriesPercentilesOut"]
            ).optional(),
            "histogramTimeseries": t.array(
                t.proxy(renames["TimeseriesBinOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricTimeseriesOut"])
    types["HistoryRecordIn"] = t.struct(
        {
            "collectionPeriods": t.array(
                t.proxy(renames["CollectionPeriodIn"])
            ).optional(),
            "key": t.proxy(renames["HistoryKeyIn"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HistoryRecordIn"])
    types["HistoryRecordOut"] = t.struct(
        {
            "collectionPeriods": t.array(
                t.proxy(renames["CollectionPeriodOut"])
            ).optional(),
            "key": t.proxy(renames["HistoryKeyOut"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryRecordOut"])
    types["TimeseriesPercentilesIn"] = t.struct(
        {"p75s": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["TimeseriesPercentilesIn"])
    types["TimeseriesPercentilesOut"] = t.struct(
        {
            "p75s": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeseriesPercentilesOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "url": t.string().optional(),
            "origin": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "url": t.string().optional(),
            "origin": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "formFactor": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])

    functions = {}
    functions["recordsQueryHistoryRecord"] = chromeuxreport.post(
        "v1/records:queryRecord",
        t.struct(
            {
                "url": t.string().optional(),
                "origin": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "formFactor": t.string().optional(),
                "effectiveConnectionType": t.string().optional(),
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
                "url": t.string().optional(),
                "origin": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "formFactor": t.string().optional(),
                "effectiveConnectionType": t.string().optional(),
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
