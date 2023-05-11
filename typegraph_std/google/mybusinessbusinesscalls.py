from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_mybusinessbusinesscalls() -> Import:
    mybusinessbusinesscalls = HTTPRuntime(
        "https://mybusinessbusinesscalls.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessbusinesscalls_1_ErrorResponse",
        "BusinessCallsInsightsIn": "_mybusinessbusinesscalls_2_BusinessCallsInsightsIn",
        "BusinessCallsInsightsOut": "_mybusinessbusinesscalls_3_BusinessCallsInsightsOut",
        "ListBusinessCallsInsightsResponseIn": "_mybusinessbusinesscalls_4_ListBusinessCallsInsightsResponseIn",
        "ListBusinessCallsInsightsResponseOut": "_mybusinessbusinesscalls_5_ListBusinessCallsInsightsResponseOut",
        "HourlyMetricsIn": "_mybusinessbusinesscalls_6_HourlyMetricsIn",
        "HourlyMetricsOut": "_mybusinessbusinesscalls_7_HourlyMetricsOut",
        "DateIn": "_mybusinessbusinesscalls_8_DateIn",
        "DateOut": "_mybusinessbusinesscalls_9_DateOut",
        "WeekDayMetricsIn": "_mybusinessbusinesscalls_10_WeekDayMetricsIn",
        "WeekDayMetricsOut": "_mybusinessbusinesscalls_11_WeekDayMetricsOut",
        "AggregateMetricsIn": "_mybusinessbusinesscalls_12_AggregateMetricsIn",
        "AggregateMetricsOut": "_mybusinessbusinesscalls_13_AggregateMetricsOut",
        "BusinessCallsSettingsIn": "_mybusinessbusinesscalls_14_BusinessCallsSettingsIn",
        "BusinessCallsSettingsOut": "_mybusinessbusinesscalls_15_BusinessCallsSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BusinessCallsInsightsIn"] = t.struct(
        {
            "metricType": t.string().optional(),
            "name": t.string(),
            "aggregateMetrics": t.proxy(renames["AggregateMetricsIn"]).optional(),
        }
    ).named(renames["BusinessCallsInsightsIn"])
    types["BusinessCallsInsightsOut"] = t.struct(
        {
            "metricType": t.string().optional(),
            "name": t.string(),
            "aggregateMetrics": t.proxy(renames["AggregateMetricsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessCallsInsightsOut"])
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
    types["WeekDayMetricsIn"] = t.struct(
        {"missedCallsCount": t.integer().optional(), "day": t.string().optional()}
    ).named(renames["WeekDayMetricsIn"])
    types["WeekDayMetricsOut"] = t.struct(
        {
            "missedCallsCount": t.integer().optional(),
            "day": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeekDayMetricsOut"])
    types["AggregateMetricsIn"] = t.struct(
        {
            "hourlyMetrics": t.array(t.proxy(renames["HourlyMetricsIn"])).optional(),
            "weekdayMetrics": t.array(t.proxy(renames["WeekDayMetricsIn"])).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "missedCallsCount": t.integer().optional(),
            "answeredCallsCount": t.integer().optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["AggregateMetricsIn"])
    types["AggregateMetricsOut"] = t.struct(
        {
            "hourlyMetrics": t.array(t.proxy(renames["HourlyMetricsOut"])).optional(),
            "weekdayMetrics": t.array(t.proxy(renames["WeekDayMetricsOut"])).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "missedCallsCount": t.integer().optional(),
            "answeredCallsCount": t.integer().optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateMetricsOut"])
    types["BusinessCallsSettingsIn"] = t.struct(
        {
            "name": t.string(),
            "consentTime": t.string().optional(),
            "callsState": t.string(),
        }
    ).named(renames["BusinessCallsSettingsIn"])
    types["BusinessCallsSettingsOut"] = t.struct(
        {
            "name": t.string(),
            "consentTime": t.string().optional(),
            "callsState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessCallsSettingsOut"])

    functions = {}
    functions["locationsGetBusinesscallssettings"] = mybusinessbusinesscalls.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "consentTime": t.string().optional(),
                "callsState": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BusinessCallsSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateBusinesscallssettings"] = mybusinessbusinesscalls.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "consentTime": t.string().optional(),
                "callsState": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BusinessCallsSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsBusinesscallsinsightsList"] = mybusinessbusinesscalls.get(
        "v1/{parent}/businesscallsinsights",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
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
        types=types,
        functions=functions,
    )
