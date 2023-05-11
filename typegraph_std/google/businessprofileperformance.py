from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_businessprofileperformance() -> Import:
    businessprofileperformance = HTTPRuntime(
        "https://businessprofileperformance.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_businessprofileperformance_1_ErrorResponse",
        "ListSearchKeywordImpressionsMonthlyResponseIn": "_businessprofileperformance_2_ListSearchKeywordImpressionsMonthlyResponseIn",
        "ListSearchKeywordImpressionsMonthlyResponseOut": "_businessprofileperformance_3_ListSearchKeywordImpressionsMonthlyResponseOut",
        "DatedValueIn": "_businessprofileperformance_4_DatedValueIn",
        "DatedValueOut": "_businessprofileperformance_5_DatedValueOut",
        "SearchKeywordCountIn": "_businessprofileperformance_6_SearchKeywordCountIn",
        "SearchKeywordCountOut": "_businessprofileperformance_7_SearchKeywordCountOut",
        "InsightsValueIn": "_businessprofileperformance_8_InsightsValueIn",
        "InsightsValueOut": "_businessprofileperformance_9_InsightsValueOut",
        "DailyMetricTimeSeriesIn": "_businessprofileperformance_10_DailyMetricTimeSeriesIn",
        "DailyMetricTimeSeriesOut": "_businessprofileperformance_11_DailyMetricTimeSeriesOut",
        "DateIn": "_businessprofileperformance_12_DateIn",
        "DateOut": "_businessprofileperformance_13_DateOut",
        "TimeSeriesIn": "_businessprofileperformance_14_TimeSeriesIn",
        "TimeSeriesOut": "_businessprofileperformance_15_TimeSeriesOut",
        "DailySubEntityTypeIn": "_businessprofileperformance_16_DailySubEntityTypeIn",
        "DailySubEntityTypeOut": "_businessprofileperformance_17_DailySubEntityTypeOut",
        "FetchMultiDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_18_FetchMultiDailyMetricsTimeSeriesResponseIn",
        "FetchMultiDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_19_FetchMultiDailyMetricsTimeSeriesResponseOut",
        "TimeOfDayIn": "_businessprofileperformance_20_TimeOfDayIn",
        "TimeOfDayOut": "_businessprofileperformance_21_TimeOfDayOut",
        "GetDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_22_GetDailyMetricsTimeSeriesResponseIn",
        "GetDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_23_GetDailyMetricsTimeSeriesResponseOut",
        "MultiDailyMetricTimeSeriesIn": "_businessprofileperformance_24_MultiDailyMetricTimeSeriesIn",
        "MultiDailyMetricTimeSeriesOut": "_businessprofileperformance_25_MultiDailyMetricTimeSeriesOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SearchKeywordCountIn"] = t.struct(
        {
            "insightsValue": t.proxy(renames["InsightsValueIn"]).optional(),
            "searchKeyword": t.string().optional(),
        }
    ).named(renames["SearchKeywordCountIn"])
    types["SearchKeywordCountOut"] = t.struct(
        {
            "insightsValue": t.proxy(renames["InsightsValueOut"]).optional(),
            "searchKeyword": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchKeywordCountOut"])
    types["InsightsValueIn"] = t.struct(
        {"value": t.string().optional(), "threshold": t.string().optional()}
    ).named(renames["InsightsValueIn"])
    types["InsightsValueOut"] = t.struct(
        {
            "value": t.string().optional(),
            "threshold": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightsValueOut"])
    types["DailyMetricTimeSeriesIn"] = t.struct(
        {
            "dailyMetric": t.string().optional(),
            "dailySubEntityType": t.proxy(renames["DailySubEntityTypeIn"]).optional(),
            "timeSeries": t.proxy(renames["TimeSeriesIn"]).optional(),
        }
    ).named(renames["DailyMetricTimeSeriesIn"])
    types["DailyMetricTimeSeriesOut"] = t.struct(
        {
            "dailyMetric": t.string().optional(),
            "dailySubEntityType": t.proxy(renames["DailySubEntityTypeOut"]).optional(),
            "timeSeries": t.proxy(renames["TimeSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyMetricTimeSeriesOut"])
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
    types["TimeSeriesIn"] = t.struct(
        {"datedValues": t.array(t.proxy(renames["DatedValueIn"])).optional()}
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "datedValues": t.array(t.proxy(renames["DatedValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["GetDailyMetricsTimeSeriesResponseIn"] = t.struct(
        {"timeSeries": t.proxy(renames["TimeSeriesIn"]).optional()}
    ).named(renames["GetDailyMetricsTimeSeriesResponseIn"])
    types["GetDailyMetricsTimeSeriesResponseOut"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDailyMetricsTimeSeriesResponseOut"])
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

    functions = {}
    functions[
        "locationsFetchMultiDailyMetricsTimeSeries"
    ] = businessprofileperformance.get(
        "v1/{name}:getDailyMetricsTimeSeries",
        t.struct(
            {
                "dailyRange.endDate.month": t.integer().optional(),
                "dailySubEntityType.dayOfWeek": t.string().optional(),
                "dailySubEntityType.timeOfDay.nanos": t.integer().optional(),
                "dailySubEntityType.timeOfDay.hours": t.integer().optional(),
                "dailySubEntityType.timeOfDay.seconds": t.integer().optional(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyMetric": t.string(),
                "dailyRange.startDate.day": t.integer().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyRange.endDate.day": t.integer().optional(),
                "name": t.string(),
                "dailySubEntityType.timeOfDay.minutes": t.integer().optional(),
                "dailyRange.startDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDailyMetricsTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetDailyMetricsTimeSeries"] = businessprofileperformance.get(
        "v1/{name}:getDailyMetricsTimeSeries",
        t.struct(
            {
                "dailyRange.endDate.month": t.integer().optional(),
                "dailySubEntityType.dayOfWeek": t.string().optional(),
                "dailySubEntityType.timeOfDay.nanos": t.integer().optional(),
                "dailySubEntityType.timeOfDay.hours": t.integer().optional(),
                "dailySubEntityType.timeOfDay.seconds": t.integer().optional(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyMetric": t.string(),
                "dailyRange.startDate.day": t.integer().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyRange.endDate.day": t.integer().optional(),
                "name": t.string(),
                "dailySubEntityType.timeOfDay.minutes": t.integer().optional(),
                "dailyRange.startDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetDailyMetricsTimeSeriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "locationsSearchkeywordsImpressionsMonthlyList"
    ] = businessprofileperformance.get(
        "v1/{parent}/searchkeywords/impressions/monthly",
        t.struct(
            {
                "monthlyRange.endMonth.year": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "monthlyRange.endMonth.month": t.integer().optional(),
                "monthlyRange.startMonth.month": t.integer().optional(),
                "parent": t.string(),
                "monthlyRange.endMonth.day": t.integer().optional(),
                "monthlyRange.startMonth.day": t.integer().optional(),
                "pageToken": t.string().optional(),
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
        types=types,
        functions=functions,
    )
