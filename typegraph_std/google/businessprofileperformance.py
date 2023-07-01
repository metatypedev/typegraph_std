from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_businessprofileperformance():
    businessprofileperformance = HTTPRuntime(
        "https://businessprofileperformance.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_businessprofileperformance_1_ErrorResponse",
        "TimeSeriesIn": "_businessprofileperformance_2_TimeSeriesIn",
        "TimeSeriesOut": "_businessprofileperformance_3_TimeSeriesOut",
        "DateIn": "_businessprofileperformance_4_DateIn",
        "DateOut": "_businessprofileperformance_5_DateOut",
        "DailySubEntityTypeIn": "_businessprofileperformance_6_DailySubEntityTypeIn",
        "DailySubEntityTypeOut": "_businessprofileperformance_7_DailySubEntityTypeOut",
        "DatedValueIn": "_businessprofileperformance_8_DatedValueIn",
        "DatedValueOut": "_businessprofileperformance_9_DatedValueOut",
        "GetDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_10_GetDailyMetricsTimeSeriesResponseIn",
        "GetDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_11_GetDailyMetricsTimeSeriesResponseOut",
        "DailyMetricTimeSeriesIn": "_businessprofileperformance_12_DailyMetricTimeSeriesIn",
        "DailyMetricTimeSeriesOut": "_businessprofileperformance_13_DailyMetricTimeSeriesOut",
        "SearchKeywordCountIn": "_businessprofileperformance_14_SearchKeywordCountIn",
        "SearchKeywordCountOut": "_businessprofileperformance_15_SearchKeywordCountOut",
        "FetchMultiDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_16_FetchMultiDailyMetricsTimeSeriesResponseIn",
        "FetchMultiDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_17_FetchMultiDailyMetricsTimeSeriesResponseOut",
        "InsightsValueIn": "_businessprofileperformance_18_InsightsValueIn",
        "InsightsValueOut": "_businessprofileperformance_19_InsightsValueOut",
        "ListSearchKeywordImpressionsMonthlyResponseIn": "_businessprofileperformance_20_ListSearchKeywordImpressionsMonthlyResponseIn",
        "ListSearchKeywordImpressionsMonthlyResponseOut": "_businessprofileperformance_21_ListSearchKeywordImpressionsMonthlyResponseOut",
        "MultiDailyMetricTimeSeriesIn": "_businessprofileperformance_22_MultiDailyMetricTimeSeriesIn",
        "MultiDailyMetricTimeSeriesOut": "_businessprofileperformance_23_MultiDailyMetricTimeSeriesOut",
        "TimeOfDayIn": "_businessprofileperformance_24_TimeOfDayIn",
        "TimeOfDayOut": "_businessprofileperformance_25_TimeOfDayOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TimeSeriesIn"] = t.struct(
        {"datedValues": t.array(t.proxy(renames["DatedValueIn"])).optional()}
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "datedValues": t.array(t.proxy(renames["DatedValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["DailySubEntityTypeIn"] = t.struct(
        {
            "dayOfWeek": t.string().optional(),
            "timeOfDay": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DailySubEntityTypeIn"])
    types["DailySubEntityTypeOut"] = t.struct(
        {
            "dayOfWeek": t.string().optional(),
            "timeOfDay": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailySubEntityTypeOut"])
    types["DatedValueIn"] = t.struct(
        {"date": t.proxy(renames["DateIn"]).optional(), "value": t.string().optional()}
    ).named(renames["DatedValueIn"])
    types["DatedValueOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatedValueOut"])
    types["GetDailyMetricsTimeSeriesResponseIn"] = t.struct(
        {"timeSeries": t.proxy(renames["TimeSeriesIn"]).optional()}
    ).named(renames["GetDailyMetricsTimeSeriesResponseIn"])
    types["GetDailyMetricsTimeSeriesResponseOut"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDailyMetricsTimeSeriesResponseOut"])
    types["DailyMetricTimeSeriesIn"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesIn"]).optional(),
            "dailyMetric": t.string().optional(),
            "dailySubEntityType": t.proxy(renames["DailySubEntityTypeIn"]).optional(),
        }
    ).named(renames["DailyMetricTimeSeriesIn"])
    types["DailyMetricTimeSeriesOut"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesOut"]).optional(),
            "dailyMetric": t.string().optional(),
            "dailySubEntityType": t.proxy(renames["DailySubEntityTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyMetricTimeSeriesOut"])
    types["SearchKeywordCountIn"] = t.struct(
        {
            "searchKeyword": t.string().optional(),
            "insightsValue": t.proxy(renames["InsightsValueIn"]).optional(),
        }
    ).named(renames["SearchKeywordCountIn"])
    types["SearchKeywordCountOut"] = t.struct(
        {
            "searchKeyword": t.string().optional(),
            "insightsValue": t.proxy(renames["InsightsValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchKeywordCountOut"])
    types["FetchMultiDailyMetricsTimeSeriesResponseIn"] = t.struct(
        {
            "multiDailyMetricTimeSeries": t.array(
                t.proxy(renames["MultiDailyMetricTimeSeriesIn"])
            ).optional()
        }
    ).named(renames["FetchMultiDailyMetricsTimeSeriesResponseIn"])
    types["FetchMultiDailyMetricsTimeSeriesResponseOut"] = t.struct(
        {
            "multiDailyMetricTimeSeries": t.array(
                t.proxy(renames["MultiDailyMetricTimeSeriesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchMultiDailyMetricsTimeSeriesResponseOut"])
    types["InsightsValueIn"] = t.struct(
        {"threshold": t.string().optional(), "value": t.string().optional()}
    ).named(renames["InsightsValueIn"])
    types["InsightsValueOut"] = t.struct(
        {
            "threshold": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightsValueOut"])
    types["ListSearchKeywordImpressionsMonthlyResponseIn"] = t.struct(
        {
            "searchKeywordsCounts": t.array(
                t.proxy(renames["SearchKeywordCountIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSearchKeywordImpressionsMonthlyResponseIn"])
    types["ListSearchKeywordImpressionsMonthlyResponseOut"] = t.struct(
        {
            "searchKeywordsCounts": t.array(
                t.proxy(renames["SearchKeywordCountOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSearchKeywordImpressionsMonthlyResponseOut"])
    types["MultiDailyMetricTimeSeriesIn"] = t.struct(
        {
            "dailyMetricTimeSeries": t.array(
                t.proxy(renames["DailyMetricTimeSeriesIn"])
            ).optional()
        }
    ).named(renames["MultiDailyMetricTimeSeriesIn"])
    types["MultiDailyMetricTimeSeriesOut"] = t.struct(
        {
            "dailyMetricTimeSeries": t.array(
                t.proxy(renames["DailyMetricTimeSeriesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiDailyMetricTimeSeriesOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])

    functions = {}
    functions["locationsGetDailyMetricsTimeSeries"] = businessprofileperformance.get(
        "v1/{location}:fetchMultiDailyMetricsTimeSeries",
        t.struct(
            {
                "dailyRange.startDate.year": t.integer().optional(),
                "dailyRange.endDate.day": t.integer().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyMetrics": t.string(),
                "location": t.string(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyRange.endDate.month": t.integer().optional(),
                "dailyRange.startDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchMultiDailyMetricsTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "locationsFetchMultiDailyMetricsTimeSeries"
    ] = businessprofileperformance.get(
        "v1/{location}:fetchMultiDailyMetricsTimeSeries",
        t.struct(
            {
                "dailyRange.startDate.year": t.integer().optional(),
                "dailyRange.endDate.day": t.integer().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyMetrics": t.string(),
                "location": t.string(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyRange.endDate.month": t.integer().optional(),
                "dailyRange.startDate.day": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FetchMultiDailyMetricsTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "locationsSearchkeywordsImpressionsMonthlyList"
    ] = businessprofileperformance.get(
        "v1/{parent}/searchkeywords/impressions/monthly",
        t.struct(
            {
                "monthlyRange.endMonth.month": t.integer().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "monthlyRange.endMonth.year": t.integer().optional(),
                "monthlyRange.startMonth.month": t.integer().optional(),
                "pageToken": t.string().optional(),
                "monthlyRange.endMonth.day": t.integer().optional(),
                "monthlyRange.startMonth.day": t.integer().optional(),
                "monthlyRange.startMonth.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSearchKeywordImpressionsMonthlyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="businessprofileperformance",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
