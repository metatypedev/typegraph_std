from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_chromeuxreport() -> Import:
    chromeuxreport = HTTPRuntime("https://chromeuxreport.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromeuxreport_1_ErrorResponse",
        "CollectionPeriodIn": "_chromeuxreport_2_CollectionPeriodIn",
        "CollectionPeriodOut": "_chromeuxreport_3_CollectionPeriodOut",
        "QueryHistoryRequestIn": "_chromeuxreport_4_QueryHistoryRequestIn",
        "QueryHistoryRequestOut": "_chromeuxreport_5_QueryHistoryRequestOut",
        "TimeseriesPercentilesIn": "_chromeuxreport_6_TimeseriesPercentilesIn",
        "TimeseriesPercentilesOut": "_chromeuxreport_7_TimeseriesPercentilesOut",
        "MetricTimeseriesIn": "_chromeuxreport_8_MetricTimeseriesIn",
        "MetricTimeseriesOut": "_chromeuxreport_9_MetricTimeseriesOut",
        "HistoryRecordIn": "_chromeuxreport_10_HistoryRecordIn",
        "HistoryRecordOut": "_chromeuxreport_11_HistoryRecordOut",
        "PercentilesIn": "_chromeuxreport_12_PercentilesIn",
        "PercentilesOut": "_chromeuxreport_13_PercentilesOut",
        "KeyIn": "_chromeuxreport_14_KeyIn",
        "KeyOut": "_chromeuxreport_15_KeyOut",
        "RecordIn": "_chromeuxreport_16_RecordIn",
        "RecordOut": "_chromeuxreport_17_RecordOut",
        "HistoryKeyIn": "_chromeuxreport_18_HistoryKeyIn",
        "HistoryKeyOut": "_chromeuxreport_19_HistoryKeyOut",
        "UrlNormalizationIn": "_chromeuxreport_20_UrlNormalizationIn",
        "UrlNormalizationOut": "_chromeuxreport_21_UrlNormalizationOut",
        "QueryRequestIn": "_chromeuxreport_22_QueryRequestIn",
        "QueryRequestOut": "_chromeuxreport_23_QueryRequestOut",
        "BinIn": "_chromeuxreport_24_BinIn",
        "BinOut": "_chromeuxreport_25_BinOut",
        "QueryResponseIn": "_chromeuxreport_26_QueryResponseIn",
        "QueryResponseOut": "_chromeuxreport_27_QueryResponseOut",
        "DateIn": "_chromeuxreport_28_DateIn",
        "DateOut": "_chromeuxreport_29_DateOut",
        "MetricIn": "_chromeuxreport_30_MetricIn",
        "MetricOut": "_chromeuxreport_31_MetricOut",
        "QueryHistoryResponseIn": "_chromeuxreport_32_QueryHistoryResponseIn",
        "QueryHistoryResponseOut": "_chromeuxreport_33_QueryHistoryResponseOut",
        "TimeseriesBinIn": "_chromeuxreport_34_TimeseriesBinIn",
        "TimeseriesBinOut": "_chromeuxreport_35_TimeseriesBinOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["QueryHistoryRequestIn"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["QueryHistoryRequestIn"])
    types["QueryHistoryRequestOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryHistoryRequestOut"])
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
    types["PercentilesIn"] = t.struct(
        {"p75": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["PercentilesIn"])
    types["PercentilesOut"] = t.struct(
        {
            "p75": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PercentilesOut"])
    types["KeyIn"] = t.struct(
        {
            "origin": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["KeyIn"])
    types["KeyOut"] = t.struct(
        {
            "origin": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
            "formFactor": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyOut"])
    types["RecordIn"] = t.struct(
        {
            "collectionPeriod": t.proxy(renames["CollectionPeriodIn"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "key": t.proxy(renames["KeyIn"]).optional(),
        }
    ).named(renames["RecordIn"])
    types["RecordOut"] = t.struct(
        {
            "collectionPeriod": t.proxy(renames["CollectionPeriodOut"]).optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "key": t.proxy(renames["KeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RecordOut"])
    types["HistoryKeyIn"] = t.struct(
        {
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["HistoryKeyIn"])
    types["HistoryKeyOut"] = t.struct(
        {
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistoryKeyOut"])
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
    types["QueryRequestIn"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "url": t.string().optional(),
            "effectiveConnectionType": t.string().optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
    types["BinIn"] = t.struct(
        {
            "end": t.struct({"_": t.string().optional()}).optional(),
            "start": t.struct({"_": t.string().optional()}).optional(),
            "density": t.number().optional(),
        }
    ).named(renames["BinIn"])
    types["BinOut"] = t.struct(
        {
            "end": t.struct({"_": t.string().optional()}).optional(),
            "start": t.struct({"_": t.string().optional()}).optional(),
            "density": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinOut"])
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
    types["QueryHistoryResponseIn"] = t.struct(
        {
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationIn"]
            ).optional(),
            "record": t.proxy(renames["HistoryRecordIn"]).optional(),
        }
    ).named(renames["QueryHistoryResponseIn"])
    types["QueryHistoryResponseOut"] = t.struct(
        {
            "urlNormalizationDetails": t.proxy(
                renames["UrlNormalizationOut"]
            ).optional(),
            "record": t.proxy(renames["HistoryRecordOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryHistoryResponseOut"])
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

    functions = {}
    functions["recordsQueryHistoryRecord"] = chromeuxreport.post(
        "v1/records:queryRecord",
        t.struct(
            {
                "metrics": t.array(t.string()).optional(),
                "origin": t.string().optional(),
                "url": t.string().optional(),
                "effectiveConnectionType": t.string().optional(),
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
                "metrics": t.array(t.string()).optional(),
                "origin": t.string().optional(),
                "url": t.string().optional(),
                "effectiveConnectionType": t.string().optional(),
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
