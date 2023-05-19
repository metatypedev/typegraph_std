from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_doubleclickbidmanager() -> Import:
    doubleclickbidmanager = HTTPRuntime("https://doubleclickbidmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_doubleclickbidmanager_1_ErrorResponse",
        "ReportStatusIn": "_doubleclickbidmanager_2_ReportStatusIn",
        "ReportStatusOut": "_doubleclickbidmanager_3_ReportStatusOut",
        "DateIn": "_doubleclickbidmanager_4_DateIn",
        "DateOut": "_doubleclickbidmanager_5_DateOut",
        "PathQueryOptionsFilterIn": "_doubleclickbidmanager_6_PathQueryOptionsFilterIn",
        "PathQueryOptionsFilterOut": "_doubleclickbidmanager_7_PathQueryOptionsFilterOut",
        "ReportKeyIn": "_doubleclickbidmanager_8_ReportKeyIn",
        "ReportKeyOut": "_doubleclickbidmanager_9_ReportKeyOut",
        "RuleIn": "_doubleclickbidmanager_10_RuleIn",
        "RuleOut": "_doubleclickbidmanager_11_RuleOut",
        "ListQueriesResponseIn": "_doubleclickbidmanager_12_ListQueriesResponseIn",
        "ListQueriesResponseOut": "_doubleclickbidmanager_13_ListQueriesResponseOut",
        "DataRangeIn": "_doubleclickbidmanager_14_DataRangeIn",
        "DataRangeOut": "_doubleclickbidmanager_15_DataRangeOut",
        "EventFilterIn": "_doubleclickbidmanager_16_EventFilterIn",
        "EventFilterOut": "_doubleclickbidmanager_17_EventFilterOut",
        "OptionsIn": "_doubleclickbidmanager_18_OptionsIn",
        "OptionsOut": "_doubleclickbidmanager_19_OptionsOut",
        "ReportIn": "_doubleclickbidmanager_20_ReportIn",
        "ReportOut": "_doubleclickbidmanager_21_ReportOut",
        "QueryMetadataIn": "_doubleclickbidmanager_22_QueryMetadataIn",
        "QueryMetadataOut": "_doubleclickbidmanager_23_QueryMetadataOut",
        "QueryScheduleIn": "_doubleclickbidmanager_24_QueryScheduleIn",
        "QueryScheduleOut": "_doubleclickbidmanager_25_QueryScheduleOut",
        "QueryIn": "_doubleclickbidmanager_26_QueryIn",
        "QueryOut": "_doubleclickbidmanager_27_QueryOut",
        "FilterPairIn": "_doubleclickbidmanager_28_FilterPairIn",
        "FilterPairOut": "_doubleclickbidmanager_29_FilterPairOut",
        "PathQueryOptionsIn": "_doubleclickbidmanager_30_PathQueryOptionsIn",
        "PathQueryOptionsOut": "_doubleclickbidmanager_31_PathQueryOptionsOut",
        "ChannelGroupingIn": "_doubleclickbidmanager_32_ChannelGroupingIn",
        "ChannelGroupingOut": "_doubleclickbidmanager_33_ChannelGroupingOut",
        "RunQueryRequestIn": "_doubleclickbidmanager_34_RunQueryRequestIn",
        "RunQueryRequestOut": "_doubleclickbidmanager_35_RunQueryRequestOut",
        "ParametersIn": "_doubleclickbidmanager_36_ParametersIn",
        "ParametersOut": "_doubleclickbidmanager_37_ParametersOut",
        "ListReportsResponseIn": "_doubleclickbidmanager_38_ListReportsResponseIn",
        "ListReportsResponseOut": "_doubleclickbidmanager_39_ListReportsResponseOut",
        "PathFilterIn": "_doubleclickbidmanager_40_PathFilterIn",
        "PathFilterOut": "_doubleclickbidmanager_41_PathFilterOut",
        "DisjunctiveMatchStatementIn": "_doubleclickbidmanager_42_DisjunctiveMatchStatementIn",
        "DisjunctiveMatchStatementOut": "_doubleclickbidmanager_43_DisjunctiveMatchStatementOut",
        "ReportMetadataIn": "_doubleclickbidmanager_44_ReportMetadataIn",
        "ReportMetadataOut": "_doubleclickbidmanager_45_ReportMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReportStatusIn"] = t.struct({"format": t.string().optional()}).named(
        renames["ReportStatusIn"]
    )
    types["ReportStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "finishTime": t.string().optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStatusOut"])
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
    types["PathQueryOptionsFilterIn"] = t.struct(
        {
            "match": t.string().optional(),
            "filter": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["PathQueryOptionsFilterIn"])
    types["PathQueryOptionsFilterOut"] = t.struct(
        {
            "match": t.string().optional(),
            "filter": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathQueryOptionsFilterOut"])
    types["ReportKeyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportKeyIn"]
    )
    types["ReportKeyOut"] = t.struct(
        {
            "queryId": t.string().optional(),
            "reportId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportKeyOut"])
    types["RuleIn"] = t.struct(
        {
            "name": t.string().optional(),
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementIn"])
            ).optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "name": t.string().optional(),
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["ListQueriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "queries": t.array(t.proxy(renames["QueryIn"])).optional(),
        }
    ).named(renames["ListQueriesResponseIn"])
    types["ListQueriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "queries": t.array(t.proxy(renames["QueryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQueriesResponseOut"])
    types["DataRangeIn"] = t.struct(
        {
            "customStartDate": t.proxy(renames["DateIn"]).optional(),
            "customEndDate": t.proxy(renames["DateIn"]).optional(),
            "range": t.string().optional(),
        }
    ).named(renames["DataRangeIn"])
    types["DataRangeOut"] = t.struct(
        {
            "customStartDate": t.proxy(renames["DateOut"]).optional(),
            "customEndDate": t.proxy(renames["DateOut"]).optional(),
            "range": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataRangeOut"])
    types["EventFilterIn"] = t.struct(
        {"dimensionFilter": t.proxy(renames["PathQueryOptionsFilterIn"]).optional()}
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["PathQueryOptionsFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
    types["OptionsIn"] = t.struct(
        {
            "includeOnlyTargetedUserLists": t.boolean().optional(),
            "pathQueryOptions": t.proxy(renames["PathQueryOptionsIn"]).optional(),
        }
    ).named(renames["OptionsIn"])
    types["OptionsOut"] = t.struct(
        {
            "includeOnlyTargetedUserLists": t.boolean().optional(),
            "pathQueryOptions": t.proxy(renames["PathQueryOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionsOut"])
    types["ReportIn"] = t.struct(
        {
            "params": t.proxy(renames["ParametersIn"]).optional(),
            "metadata": t.proxy(renames["ReportMetadataIn"]).optional(),
            "key": t.proxy(renames["ReportKeyIn"]).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "params": t.proxy(renames["ParametersOut"]).optional(),
            "metadata": t.proxy(renames["ReportMetadataOut"]).optional(),
            "key": t.proxy(renames["ReportKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["QueryMetadataIn"] = t.struct(
        {
            "shareEmailAddress": t.array(t.string()).optional(),
            "format": t.string().optional(),
            "dataRange": t.proxy(renames["DataRangeIn"]).optional(),
            "sendNotification": t.boolean().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["QueryMetadataIn"])
    types["QueryMetadataOut"] = t.struct(
        {
            "shareEmailAddress": t.array(t.string()).optional(),
            "format": t.string().optional(),
            "dataRange": t.proxy(renames["DataRangeOut"]).optional(),
            "sendNotification": t.boolean().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryMetadataOut"])
    types["QueryScheduleIn"] = t.struct(
        {
            "frequency": t.string().optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "nextRunTimezoneCode": t.string().optional(),
        }
    ).named(renames["QueryScheduleIn"])
    types["QueryScheduleOut"] = t.struct(
        {
            "frequency": t.string().optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "nextRunTimezoneCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryScheduleOut"])
    types["QueryIn"] = t.struct(
        {
            "schedule": t.proxy(renames["QueryScheduleIn"]).optional(),
            "params": t.proxy(renames["ParametersIn"]).optional(),
            "metadata": t.proxy(renames["QueryMetadataIn"]).optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "schedule": t.proxy(renames["QueryScheduleOut"]).optional(),
            "queryId": t.string().optional(),
            "params": t.proxy(renames["ParametersOut"]).optional(),
            "metadata": t.proxy(renames["QueryMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
    types["FilterPairIn"] = t.struct(
        {"value": t.string().optional(), "type": t.string().optional()}
    ).named(renames["FilterPairIn"])
    types["FilterPairOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterPairOut"])
    types["PathQueryOptionsIn"] = t.struct(
        {
            "channelGrouping": t.proxy(renames["ChannelGroupingIn"]).optional(),
            "pathFilters": t.array(t.proxy(renames["PathFilterIn"])).optional(),
        }
    ).named(renames["PathQueryOptionsIn"])
    types["PathQueryOptionsOut"] = t.struct(
        {
            "channelGrouping": t.proxy(renames["ChannelGroupingOut"]).optional(),
            "pathFilters": t.array(t.proxy(renames["PathFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathQueryOptionsOut"])
    types["ChannelGroupingIn"] = t.struct(
        {
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "fallbackName": t.string().optional(),
        }
    ).named(renames["ChannelGroupingIn"])
    types["ChannelGroupingOut"] = t.struct(
        {
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "fallbackName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelGroupingOut"])
    types["RunQueryRequestIn"] = t.struct(
        {"dataRange": t.proxy(renames["DataRangeIn"]).optional()}
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "dataRange": t.proxy(renames["DataRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
    types["ParametersIn"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "groupBys": t.array(t.string()).optional(),
            "options": t.proxy(renames["OptionsIn"]).optional(),
            "filters": t.array(t.proxy(renames["FilterPairIn"])).optional(),
        }
    ).named(renames["ParametersIn"])
    types["ParametersOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "groupBys": t.array(t.string()).optional(),
            "options": t.proxy(renames["OptionsOut"]).optional(),
            "filters": t.array(t.proxy(renames["FilterPairOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParametersOut"])
    types["ListReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
        }
    ).named(renames["ListReportsResponseIn"])
    types["ListReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportsResponseOut"])
    types["PathFilterIn"] = t.struct(
        {
            "pathMatchPosition": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
        }
    ).named(renames["PathFilterIn"])
    types["PathFilterOut"] = t.struct(
        {
            "pathMatchPosition": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathFilterOut"])
    types["DisjunctiveMatchStatementIn"] = t.struct(
        {"eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional()}
    ).named(renames["DisjunctiveMatchStatementIn"])
    types["DisjunctiveMatchStatementOut"] = t.struct(
        {
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisjunctiveMatchStatementOut"])
    types["ReportMetadataIn"] = t.struct(
        {
            "reportDataEndDate": t.proxy(renames["DateIn"]).optional(),
            "reportDataStartDate": t.proxy(renames["DateIn"]).optional(),
            "status": t.proxy(renames["ReportStatusIn"]).optional(),
        }
    ).named(renames["ReportMetadataIn"])
    types["ReportMetadataOut"] = t.struct(
        {
            "reportDataEndDate": t.proxy(renames["DateOut"]).optional(),
            "reportDataStartDate": t.proxy(renames["DateOut"]).optional(),
            "googleCloudStoragePath": t.string().optional(),
            "status": t.proxy(renames["ReportStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportMetadataOut"])

    functions = {}
    functions["queriesList"] = doubleclickbidmanager.post(
        "queries",
        t.struct(
            {
                "schedule": t.proxy(renames["QueryScheduleIn"]).optional(),
                "params": t.proxy(renames["ParametersIn"]).optional(),
                "metadata": t.proxy(renames["QueryMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesGet"] = doubleclickbidmanager.post(
        "queries",
        t.struct(
            {
                "schedule": t.proxy(renames["QueryScheduleIn"]).optional(),
                "params": t.proxy(renames["ParametersIn"]).optional(),
                "metadata": t.proxy(renames["QueryMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesRun"] = doubleclickbidmanager.post(
        "queries",
        t.struct(
            {
                "schedule": t.proxy(renames["QueryScheduleIn"]).optional(),
                "params": t.proxy(renames["ParametersIn"]).optional(),
                "metadata": t.proxy(renames["QueryMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesDelete"] = doubleclickbidmanager.post(
        "queries",
        t.struct(
            {
                "schedule": t.proxy(renames["QueryScheduleIn"]).optional(),
                "params": t.proxy(renames["ParametersIn"]).optional(),
                "metadata": t.proxy(renames["QueryMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesCreate"] = doubleclickbidmanager.post(
        "queries",
        t.struct(
            {
                "schedule": t.proxy(renames["QueryScheduleIn"]).optional(),
                "params": t.proxy(renames["ParametersIn"]).optional(),
                "metadata": t.proxy(renames["QueryMetadataIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesReportsGet"] = doubleclickbidmanager.get(
        "queries/{queryId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "queryId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesReportsList"] = doubleclickbidmanager.get(
        "queries/{queryId}/reports",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "queryId": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="doubleclickbidmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
