from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_businessprofileperformance() -> Import:
    businessprofileperformance = HTTPRuntime(
        "https://businessprofileperformance.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_businessprofileperformance_1_ErrorResponse",
        "MultiDailyMetricTimeSeriesIn": "_businessprofileperformance_2_MultiDailyMetricTimeSeriesIn",
        "MultiDailyMetricTimeSeriesOut": "_businessprofileperformance_3_MultiDailyMetricTimeSeriesOut",
        "ListSearchKeywordImpressionsMonthlyResponseIn": "_businessprofileperformance_4_ListSearchKeywordImpressionsMonthlyResponseIn",
        "ListSearchKeywordImpressionsMonthlyResponseOut": "_businessprofileperformance_5_ListSearchKeywordImpressionsMonthlyResponseOut",
        "InsightsValueIn": "_businessprofileperformance_6_InsightsValueIn",
        "InsightsValueOut": "_businessprofileperformance_7_InsightsValueOut",
        "DatedValueIn": "_businessprofileperformance_8_DatedValueIn",
        "DatedValueOut": "_businessprofileperformance_9_DatedValueOut",
        "DailyMetricTimeSeriesIn": "_businessprofileperformance_10_DailyMetricTimeSeriesIn",
        "DailyMetricTimeSeriesOut": "_businessprofileperformance_11_DailyMetricTimeSeriesOut",
        "TimeOfDayIn": "_businessprofileperformance_12_TimeOfDayIn",
        "TimeOfDayOut": "_businessprofileperformance_13_TimeOfDayOut",
        "FetchMultiDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_14_FetchMultiDailyMetricsTimeSeriesResponseIn",
        "FetchMultiDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_15_FetchMultiDailyMetricsTimeSeriesResponseOut",
        "DailySubEntityTypeIn": "_businessprofileperformance_16_DailySubEntityTypeIn",
        "DailySubEntityTypeOut": "_businessprofileperformance_17_DailySubEntityTypeOut",
        "SearchKeywordCountIn": "_businessprofileperformance_18_SearchKeywordCountIn",
        "SearchKeywordCountOut": "_businessprofileperformance_19_SearchKeywordCountOut",
        "DateIn": "_businessprofileperformance_20_DateIn",
        "DateOut": "_businessprofileperformance_21_DateOut",
        "TimeSeriesIn": "_businessprofileperformance_22_TimeSeriesIn",
        "TimeSeriesOut": "_businessprofileperformance_23_TimeSeriesOut",
        "GetDailyMetricsTimeSeriesResponseIn": "_businessprofileperformance_24_GetDailyMetricsTimeSeriesResponseIn",
        "GetDailyMetricsTimeSeriesResponseOut": "_businessprofileperformance_25_GetDailyMetricsTimeSeriesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DailySubEntityTypeIn"] = t.struct(
        {
            "timeOfDay": t.proxy(renames["TimeOfDayIn"]).optional(),
            "dayOfWeek": t.string().optional(),
        }
    ).named(renames["DailySubEntityTypeIn"])
    types["DailySubEntityTypeOut"] = t.struct(
        {
            "timeOfDay": t.proxy(renames["TimeOfDayOut"]).optional(),
            "dayOfWeek": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailySubEntityTypeOut"])
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
    types["TimeSeriesIn"] = t.struct(
        {"datedValues": t.array(t.proxy(renames["DatedValueIn"])).optional()}
    ).named(renames["TimeSeriesIn"])
    types["TimeSeriesOut"] = t.struct(
        {
            "datedValues": t.array(t.proxy(renames["DatedValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeSeriesOut"])
    types["GetDailyMetricsTimeSeriesResponseIn"] = t.struct(
        {"timeSeries": t.proxy(renames["TimeSeriesIn"]).optional()}
    ).named(renames["GetDailyMetricsTimeSeriesResponseIn"])
    types["GetDailyMetricsTimeSeriesResponseOut"] = t.struct(
        {
            "timeSeries": t.proxy(renames["TimeSeriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDailyMetricsTimeSeriesResponseOut"])

    functions = {}
    functions[
        "locationsFetchMultiDailyMetricsTimeSeries"
    ] = businessprofileperformance.get(
        "v1/{name}:getDailyMetricsTimeSeries",
        t.struct(
            {
                "dailySubEntityType.timeOfDay.hours": t.integer().optional(),
                "name": t.string(),
                "dailySubEntityType.dayOfWeek": t.string().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyRange.endDate.day": t.integer().optional(),
                "dailyRange.startDate.year": t.integer().optional(),
                "dailyRange.startDate.day": t.integer().optional(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyRange.endDate.month": t.integer().optional(),
                "dailyMetric": t.string(),
                "dailySubEntityType.timeOfDay.nanos": t.integer().optional(),
                "dailySubEntityType.timeOfDay.seconds": t.integer().optional(),
                "dailySubEntityType.timeOfDay.minutes": t.integer().optional(),
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
                "dailySubEntityType.timeOfDay.hours": t.integer().optional(),
                "name": t.string(),
                "dailySubEntityType.dayOfWeek": t.string().optional(),
                "dailyRange.startDate.month": t.integer().optional(),
                "dailyRange.endDate.day": t.integer().optional(),
                "dailyRange.startDate.year": t.integer().optional(),
                "dailyRange.startDate.day": t.integer().optional(),
                "dailyRange.endDate.year": t.integer().optional(),
                "dailyRange.endDate.month": t.integer().optional(),
                "dailyMetric": t.string(),
                "dailySubEntityType.timeOfDay.nanos": t.integer().optional(),
                "dailySubEntityType.timeOfDay.seconds": t.integer().optional(),
                "dailySubEntityType.timeOfDay.minutes": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "monthlyRange.startMonth.month": t.integer().optional(),
                "monthlyRange.endMonth.year": t.integer().optional(),
                "monthlyRange.startMonth.year": t.integer().optional(),
                "monthlyRange.endMonth.day": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "monthlyRange.endMonth.month": t.integer().optional(),
                "monthlyRange.startMonth.day": t.integer().optional(),
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
