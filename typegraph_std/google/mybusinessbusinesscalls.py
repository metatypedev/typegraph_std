from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinessbusinesscalls() -> Import:
    mybusinessbusinesscalls = HTTPRuntime(
        "https://mybusinessbusinesscalls.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessbusinesscalls_1_ErrorResponse",
        "HourlyMetricsIn": "_mybusinessbusinesscalls_2_HourlyMetricsIn",
        "HourlyMetricsOut": "_mybusinessbusinesscalls_3_HourlyMetricsOut",
        "DateIn": "_mybusinessbusinesscalls_4_DateIn",
        "DateOut": "_mybusinessbusinesscalls_5_DateOut",
        "ListBusinessCallsInsightsResponseIn": "_mybusinessbusinesscalls_6_ListBusinessCallsInsightsResponseIn",
        "ListBusinessCallsInsightsResponseOut": "_mybusinessbusinesscalls_7_ListBusinessCallsInsightsResponseOut",
        "BusinessCallsSettingsIn": "_mybusinessbusinesscalls_8_BusinessCallsSettingsIn",
        "BusinessCallsSettingsOut": "_mybusinessbusinesscalls_9_BusinessCallsSettingsOut",
        "BusinessCallsInsightsIn": "_mybusinessbusinesscalls_10_BusinessCallsInsightsIn",
        "BusinessCallsInsightsOut": "_mybusinessbusinesscalls_11_BusinessCallsInsightsOut",
        "AggregateMetricsIn": "_mybusinessbusinesscalls_12_AggregateMetricsIn",
        "AggregateMetricsOut": "_mybusinessbusinesscalls_13_AggregateMetricsOut",
        "WeekDayMetricsIn": "_mybusinessbusinesscalls_14_WeekDayMetricsIn",
        "WeekDayMetricsOut": "_mybusinessbusinesscalls_15_WeekDayMetricsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HourlyMetricsIn"] = t.struct(
        {"hour": t.integer().optional(), "missedCallsCount": t.integer().optional()}
    ).named(renames["HourlyMetricsIn"])
    types["HourlyMetricsOut"] = t.struct(
        {
            "hour": t.integer().optional(),
            "missedCallsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HourlyMetricsOut"])
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
    types["ListBusinessCallsInsightsResponseIn"] = t.struct(
        {
            "businessCallsInsights": t.array(
                t.proxy(renames["BusinessCallsInsightsIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBusinessCallsInsightsResponseIn"])
    types["ListBusinessCallsInsightsResponseOut"] = t.struct(
        {
            "businessCallsInsights": t.array(
                t.proxy(renames["BusinessCallsInsightsOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBusinessCallsInsightsResponseOut"])
    types["BusinessCallsSettingsIn"] = t.struct(
        {
            "name": t.string(),
            "callsState": t.string(),
            "consentTime": t.string().optional(),
        }
    ).named(renames["BusinessCallsSettingsIn"])
    types["BusinessCallsSettingsOut"] = t.struct(
        {
            "name": t.string(),
            "callsState": t.string(),
            "consentTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessCallsSettingsOut"])
    types["BusinessCallsInsightsIn"] = t.struct(
        {
            "aggregateMetrics": t.proxy(renames["AggregateMetricsIn"]).optional(),
            "name": t.string(),
            "metricType": t.string().optional(),
        }
    ).named(renames["BusinessCallsInsightsIn"])
    types["BusinessCallsInsightsOut"] = t.struct(
        {
            "aggregateMetrics": t.proxy(renames["AggregateMetricsOut"]).optional(),
            "name": t.string(),
            "metricType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessCallsInsightsOut"])
    types["AggregateMetricsIn"] = t.struct(
        {
            "hourlyMetrics": t.array(t.proxy(renames["HourlyMetricsIn"])).optional(),
            "weekdayMetrics": t.array(t.proxy(renames["WeekDayMetricsIn"])).optional(),
            "answeredCallsCount": t.integer().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "missedCallsCount": t.integer().optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["AggregateMetricsIn"])
    types["AggregateMetricsOut"] = t.struct(
        {
            "hourlyMetrics": t.array(t.proxy(renames["HourlyMetricsOut"])).optional(),
            "weekdayMetrics": t.array(t.proxy(renames["WeekDayMetricsOut"])).optional(),
            "answeredCallsCount": t.integer().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "missedCallsCount": t.integer().optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateMetricsOut"])
    types["WeekDayMetricsIn"] = t.struct(
        {"day": t.string().optional(), "missedCallsCount": t.integer().optional()}
    ).named(renames["WeekDayMetricsIn"])
    types["WeekDayMetricsOut"] = t.struct(
        {
            "day": t.string().optional(),
            "missedCallsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeekDayMetricsOut"])

    functions = {}
    functions["locationsUpdateBusinesscallssettings"] = mybusinessbusinesscalls.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BusinessCallsSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetBusinesscallssettings"] = mybusinessbusinesscalls.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BusinessCallsSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBusinesscallsinsightsList"] = mybusinessbusinesscalls.get(
        "v1/{parent}/businesscallsinsights",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBusinessCallsInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessbusinesscalls",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
