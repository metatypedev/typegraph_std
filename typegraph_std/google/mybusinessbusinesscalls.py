from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_mybusinessbusinesscalls() -> Import:
    mybusinessbusinesscalls = HTTPRuntime(
        "https://mybusinessbusinesscalls.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessbusinesscalls_1_ErrorResponse",
        "AggregateMetricsIn": "_mybusinessbusinesscalls_2_AggregateMetricsIn",
        "AggregateMetricsOut": "_mybusinessbusinesscalls_3_AggregateMetricsOut",
        "ListBusinessCallsInsightsResponseIn": "_mybusinessbusinesscalls_4_ListBusinessCallsInsightsResponseIn",
        "ListBusinessCallsInsightsResponseOut": "_mybusinessbusinesscalls_5_ListBusinessCallsInsightsResponseOut",
        "BusinessCallsSettingsIn": "_mybusinessbusinesscalls_6_BusinessCallsSettingsIn",
        "BusinessCallsSettingsOut": "_mybusinessbusinesscalls_7_BusinessCallsSettingsOut",
        "BusinessCallsInsightsIn": "_mybusinessbusinesscalls_8_BusinessCallsInsightsIn",
        "BusinessCallsInsightsOut": "_mybusinessbusinesscalls_9_BusinessCallsInsightsOut",
        "WeekDayMetricsIn": "_mybusinessbusinesscalls_10_WeekDayMetricsIn",
        "WeekDayMetricsOut": "_mybusinessbusinesscalls_11_WeekDayMetricsOut",
        "HourlyMetricsIn": "_mybusinessbusinesscalls_12_HourlyMetricsIn",
        "HourlyMetricsOut": "_mybusinessbusinesscalls_13_HourlyMetricsOut",
        "DateIn": "_mybusinessbusinesscalls_14_DateIn",
        "DateOut": "_mybusinessbusinesscalls_15_DateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AggregateMetricsIn"] = t.struct(
        {
            "missedCallsCount": t.integer().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "answeredCallsCount": t.integer().optional(),
            "weekdayMetrics": t.array(t.proxy(renames["WeekDayMetricsIn"])).optional(),
            "hourlyMetrics": t.array(t.proxy(renames["HourlyMetricsIn"])).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["AggregateMetricsIn"])
    types["AggregateMetricsOut"] = t.struct(
        {
            "missedCallsCount": t.integer().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "answeredCallsCount": t.integer().optional(),
            "weekdayMetrics": t.array(t.proxy(renames["WeekDayMetricsOut"])).optional(),
            "hourlyMetrics": t.array(t.proxy(renames["HourlyMetricsOut"])).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateMetricsOut"])
    types["ListBusinessCallsInsightsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "businessCallsInsights": t.array(
                t.proxy(renames["BusinessCallsInsightsIn"])
            ).optional(),
        }
    ).named(renames["ListBusinessCallsInsightsResponseIn"])
    types["ListBusinessCallsInsightsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "businessCallsInsights": t.array(
                t.proxy(renames["BusinessCallsInsightsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBusinessCallsInsightsResponseOut"])
    types["BusinessCallsSettingsIn"] = t.struct(
        {
            "consentTime": t.string().optional(),
            "callsState": t.string(),
            "name": t.string(),
        }
    ).named(renames["BusinessCallsSettingsIn"])
    types["BusinessCallsSettingsOut"] = t.struct(
        {
            "consentTime": t.string().optional(),
            "callsState": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessCallsSettingsOut"])
    types["BusinessCallsInsightsIn"] = t.struct(
        {
            "metricType": t.string().optional(),
            "aggregateMetrics": t.proxy(renames["AggregateMetricsIn"]).optional(),
            "name": t.string(),
        }
    ).named(renames["BusinessCallsInsightsIn"])
    types["BusinessCallsInsightsOut"] = t.struct(
        {
            "metricType": t.string().optional(),
            "aggregateMetrics": t.proxy(renames["AggregateMetricsOut"]).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessCallsInsightsOut"])
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
