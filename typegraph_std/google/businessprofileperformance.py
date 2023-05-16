from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_businessprofileperformance() -> Import:
    businessprofileperformance = HTTPRuntime(
        "https://businessprofileperformance.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_businessprofileperformance_1_ErrorResponse",
        "FetchMultiDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_2_FetchMultiDailyMetricsTimeSeriesResponseIn",
        "FetchMultiDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_3_FetchMultiDailyMetricsTimeSeriesResponseOut",
        "ListSearchKeywordImpressionsMonthlyResponseIn": "_businessprofileperformance_4_ListSearchKeywordImpressionsMonthlyResponseIn",
        "ListSearchKeywordImpressionsMonthlyResponseOut": "_businessprofileperformance_5_ListSearchKeywordImpressionsMonthlyResponseOut",
        "DailySubEntityTypeIn": "_businessprofileperformance_6_DailySubEntityTypeIn",
        "DailySubEntityTypeOut": "_businessprofileperformance_7_DailySubEntityTypeOut",
        "MultiDailyMetricTimeSeriesIn": "_businessprofileperformance_8_MultiDailyMetricTimeSeriesIn",
        "MultiDailyMetricTimeSeriesOut": "_businessprofileperformance_9_MultiDailyMetricTimeSeriesOut",
        "DatedValueIn": "_businessprofileperformance_10_DatedValueIn",
        "DatedValueOut": "_businessprofileperformance_11_DatedValueOut",
        "TimeOfDayIn": "_businessprofileperformance_12_TimeOfDayIn",
        "TimeOfDayOut": "_businessprofileperformance_13_TimeOfDayOut",
        "DateIn": "_businessprofileperformance_14_DateIn",
        "DateOut": "_businessprofileperformance_15_DateOut",
        "DailyMetricTimeSeriesIn": "_businessprofileperformance_16_DailyMetricTimeSeriesIn",
        "DailyMetricTimeSeriesOut": "_businessprofileperformance_17_DailyMetricTimeSeriesOut",
        "GetDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_18_GetDailyMetricsTimeSeriesResponseIn",
        "GetDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_19_GetDailyMetricsTimeSeriesResponseOut",
        "InsightsValueIn": "_businessprofileperformance_20_InsightsValueIn",
        "InsightsValueOut": "_businessprofileperformance_21_InsightsValueOut",
        "TimeSeriesIn": "_businessprofileperformance_22_TimeSeriesIn",
        "TimeSeriesOut": "_businessprofileperformance_23_TimeSeriesOut",
        "SearchKeywordCountIn": "_businessprofileperformance_24_SearchKeywordCountIn",
        "SearchKeywordCountOut": "_businessprofileperformance_25_SearchKeywordCountOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListSearchKeywordImpressionsMonthlyResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "searchKeywordsCounts": t.array(
                t.proxy(renames["SearchKeywordCountIn"])
            ).optional(),
        }
    ).named(renames["ListSearchKeywordImpressionsMonthlyResponseIn"])
    types["ListSearchKeywordImpressionsMonthlyResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "searchKeywordsCounts": t.array(
                t.proxy(renames["SearchKeywordCountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSearchKeywordImpressionsMonthlyResponseOut"])
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
    types["DatedValueIn"] = t.struct(
        {"value": t.string().optional(), "date": t.proxy(renames["DateIn"]).optional()}
    ).named(renames["DatedValueIn"])
    types["DatedValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatedValueOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["DailyMetricTimeSeriesIn"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesIn"]).optional(),
            "dailySubEntityType": t.proxy(renames["DailySubEntityTypeIn"]).optional(),
            "dailyMetric": t.string().optional(),
        }
    ).named(renames["DailyMetricTimeSeriesIn"])
    types["DailyMetricTimeSeriesOut"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesOut"]).optional(),
            "dailySubEntityType": t.proxy(renames["DailySubEntityTypeOut"]).optional(),
            "dailyMetric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyMetricTimeSeriesOut"])
    types["GetDailyMetricsTimeSeriesResponseIn"] = t.struct(
        {"timeSeries": t.proxy(renames["TimeSeriesIn"]).optional()}
    ).named(renames["GetDailyMetricsTimeSeriesResponseIn"])
    types["GetDailyMetricsTimeSeriesResponseOut"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDailyMetricsTimeSeriesResponseOut"])
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
    types["TimeSeriesIn"] = t.struct(
        {"datedValues": t.array(t.proxy(renames["DatedValueIn"])).optional()}
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "datedValues": t.array(t.proxy(renames["DatedValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
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

    functions = {}
    functions["locationsGetDailyMetricsTimeSeries"] = businessprofileperformance.get(
        "v1/{location}:fetchMultiDailyMetricsTimeSeries",
        t.struct(
            {
                "dailyRange.startDate.day": t.integer().optional(),
                "dailyRange.startDate.year": t.integer().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyRange.endDate.month": t.integer().optional(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyMetrics": t.string(),
                "location": t.string(),
                "dailyRange.endDate.day": t.integer().optional(),
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
                "dailyRange.startDate.day": t.integer().optional(),
                "dailyRange.startDate.year": t.integer().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyRange.endDate.month": t.integer().optional(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyMetrics": t.string(),
                "location": t.string(),
                "dailyRange.endDate.day": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "monthlyRange.startMonth.month": t.integer().optional(),
                "monthlyRange.endMonth.year": t.integer().optional(),
                "monthlyRange.startMonth.year": t.integer().optional(),
                "monthlyRange.endMonth.day": t.integer().optional(),
                "monthlyRange.startMonth.day": t.integer().optional(),
                "monthlyRange.endMonth.month": t.integer().optional(),
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
