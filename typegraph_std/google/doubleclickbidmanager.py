from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_doubleclickbidmanager():
    doubleclickbidmanager = HTTPRuntime("https://doubleclickbidmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_doubleclickbidmanager_1_ErrorResponse",
        "QueryScheduleIn": "_doubleclickbidmanager_2_QueryScheduleIn",
        "QueryScheduleOut": "_doubleclickbidmanager_3_QueryScheduleOut",
        "RunQueryRequestIn": "_doubleclickbidmanager_4_RunQueryRequestIn",
        "RunQueryRequestOut": "_doubleclickbidmanager_5_RunQueryRequestOut",
        "OptionsIn": "_doubleclickbidmanager_6_OptionsIn",
        "OptionsOut": "_doubleclickbidmanager_7_OptionsOut",
        "ReportKeyIn": "_doubleclickbidmanager_8_ReportKeyIn",
        "ReportKeyOut": "_doubleclickbidmanager_9_ReportKeyOut",
        "ReportStatusIn": "_doubleclickbidmanager_10_ReportStatusIn",
        "ReportStatusOut": "_doubleclickbidmanager_11_ReportStatusOut",
        "DisjunctiveMatchStatementIn": "_doubleclickbidmanager_12_DisjunctiveMatchStatementIn",
        "DisjunctiveMatchStatementOut": "_doubleclickbidmanager_13_DisjunctiveMatchStatementOut",
        "ListReportsResponseIn": "_doubleclickbidmanager_14_ListReportsResponseIn",
        "ListReportsResponseOut": "_doubleclickbidmanager_15_ListReportsResponseOut",
        "RuleIn": "_doubleclickbidmanager_16_RuleIn",
        "RuleOut": "_doubleclickbidmanager_17_RuleOut",
        "QueryIn": "_doubleclickbidmanager_18_QueryIn",
        "QueryOut": "_doubleclickbidmanager_19_QueryOut",
        "PathFilterIn": "_doubleclickbidmanager_20_PathFilterIn",
        "PathFilterOut": "_doubleclickbidmanager_21_PathFilterOut",
        "ChannelGroupingIn": "_doubleclickbidmanager_22_ChannelGroupingIn",
        "ChannelGroupingOut": "_doubleclickbidmanager_23_ChannelGroupingOut",
        "PathQueryOptionsIn": "_doubleclickbidmanager_24_PathQueryOptionsIn",
        "PathQueryOptionsOut": "_doubleclickbidmanager_25_PathQueryOptionsOut",
        "ParametersIn": "_doubleclickbidmanager_26_ParametersIn",
        "ParametersOut": "_doubleclickbidmanager_27_ParametersOut",
        "DateIn": "_doubleclickbidmanager_28_DateIn",
        "DateOut": "_doubleclickbidmanager_29_DateOut",
        "QueryMetadataIn": "_doubleclickbidmanager_30_QueryMetadataIn",
        "QueryMetadataOut": "_doubleclickbidmanager_31_QueryMetadataOut",
        "PathQueryOptionsFilterIn": "_doubleclickbidmanager_32_PathQueryOptionsFilterIn",
        "PathQueryOptionsFilterOut": "_doubleclickbidmanager_33_PathQueryOptionsFilterOut",
        "EventFilterIn": "_doubleclickbidmanager_34_EventFilterIn",
        "EventFilterOut": "_doubleclickbidmanager_35_EventFilterOut",
        "FilterPairIn": "_doubleclickbidmanager_36_FilterPairIn",
        "FilterPairOut": "_doubleclickbidmanager_37_FilterPairOut",
        "DataRangeIn": "_doubleclickbidmanager_38_DataRangeIn",
        "DataRangeOut": "_doubleclickbidmanager_39_DataRangeOut",
        "ListQueriesResponseIn": "_doubleclickbidmanager_40_ListQueriesResponseIn",
        "ListQueriesResponseOut": "_doubleclickbidmanager_41_ListQueriesResponseOut",
        "ReportMetadataIn": "_doubleclickbidmanager_42_ReportMetadataIn",
        "ReportMetadataOut": "_doubleclickbidmanager_43_ReportMetadataOut",
        "ReportIn": "_doubleclickbidmanager_44_ReportIn",
        "ReportOut": "_doubleclickbidmanager_45_ReportOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["QueryScheduleIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "frequency": t.string().optional(),
            "nextRunTimezoneCode": t.string().optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["QueryScheduleIn"])
    types["QueryScheduleOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "frequency": t.string().optional(),
            "nextRunTimezoneCode": t.string().optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryScheduleOut"])
    types["RunQueryRequestIn"] = t.struct(
        {"dataRange": t.proxy(renames["DataRangeIn"]).optional()}
    ).named(renames["RunQueryRequestIn"])
    types["RunQueryRequestOut"] = t.struct(
        {
            "dataRange": t.proxy(renames["DataRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunQueryRequestOut"])
    types["OptionsIn"] = t.struct(
        {
            "pathQueryOptions": t.proxy(renames["PathQueryOptionsIn"]).optional(),
            "includeOnlyTargetedUserLists": t.boolean().optional(),
        }
    ).named(renames["OptionsIn"])
    types["OptionsOut"] = t.struct(
        {
            "pathQueryOptions": t.proxy(renames["PathQueryOptionsOut"]).optional(),
            "includeOnlyTargetedUserLists": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionsOut"])
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
    types["ReportStatusIn"] = t.struct({"format": t.string().optional()}).named(
        renames["ReportStatusIn"]
    )
    types["ReportStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "format": t.string().optional(),
            "finishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportStatusOut"])
    types["DisjunctiveMatchStatementIn"] = t.struct(
        {"eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional()}
    ).named(renames["DisjunctiveMatchStatementIn"])
    types["DisjunctiveMatchStatementOut"] = t.struct(
        {
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisjunctiveMatchStatementOut"])
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
    types["RuleIn"] = t.struct(
        {
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "disjunctiveMatchStatements": t.array(
                t.proxy(renames["DisjunctiveMatchStatementOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["QueryIn"] = t.struct(
        {
            "schedule": t.proxy(renames["QueryScheduleIn"]).optional(),
            "metadata": t.proxy(renames["QueryMetadataIn"]).optional(),
            "params": t.proxy(renames["ParametersIn"]).optional(),
        }
    ).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {
            "schedule": t.proxy(renames["QueryScheduleOut"]).optional(),
            "queryId": t.string().optional(),
            "metadata": t.proxy(renames["QueryMetadataOut"]).optional(),
            "params": t.proxy(renames["ParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOut"])
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
    types["ChannelGroupingIn"] = t.struct(
        {
            "fallbackName": t.string().optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
        }
    ).named(renames["ChannelGroupingIn"])
    types["ChannelGroupingOut"] = t.struct(
        {
            "fallbackName": t.string().optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelGroupingOut"])
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
    types["ParametersIn"] = t.struct(
        {
            "type": t.string().optional(),
            "filters": t.array(t.proxy(renames["FilterPairIn"])).optional(),
            "groupBys": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
            "options": t.proxy(renames["OptionsIn"]).optional(),
        }
    ).named(renames["ParametersIn"])
    types["ParametersOut"] = t.struct(
        {
            "type": t.string().optional(),
            "filters": t.array(t.proxy(renames["FilterPairOut"])).optional(),
            "groupBys": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
            "options": t.proxy(renames["OptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParametersOut"])
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
    types["QueryMetadataIn"] = t.struct(
        {
            "sendNotification": t.boolean().optional(),
            "format": t.string().optional(),
            "shareEmailAddress": t.array(t.string()).optional(),
            "dataRange": t.proxy(renames["DataRangeIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["QueryMetadataIn"])
    types["QueryMetadataOut"] = t.struct(
        {
            "sendNotification": t.boolean().optional(),
            "format": t.string().optional(),
            "shareEmailAddress": t.array(t.string()).optional(),
            "dataRange": t.proxy(renames["DataRangeOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryMetadataOut"])
    types["PathQueryOptionsFilterIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "match": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["PathQueryOptionsFilterIn"])
    types["PathQueryOptionsFilterOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "match": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathQueryOptionsFilterOut"])
    types["EventFilterIn"] = t.struct(
        {"dimensionFilter": t.proxy(renames["PathQueryOptionsFilterIn"]).optional()}
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "dimensionFilter": t.proxy(renames["PathQueryOptionsFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
    types["FilterPairIn"] = t.struct(
        {"type": t.string().optional(), "value": t.string().optional()}
    ).named(renames["FilterPairIn"])
    types["FilterPairOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilterPairOut"])
    types["DataRangeIn"] = t.struct(
        {
            "customEndDate": t.proxy(renames["DateIn"]).optional(),
            "range": t.string().optional(),
            "customStartDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DataRangeIn"])
    types["DataRangeOut"] = t.struct(
        {
            "customEndDate": t.proxy(renames["DateOut"]).optional(),
            "range": t.string().optional(),
            "customStartDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataRangeOut"])
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
    types["ReportMetadataIn"] = t.struct(
        {
            "reportDataStartDate": t.proxy(renames["DateIn"]).optional(),
            "status": t.proxy(renames["ReportStatusIn"]).optional(),
            "reportDataEndDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["ReportMetadataIn"])
    types["ReportMetadataOut"] = t.struct(
        {
            "reportDataStartDate": t.proxy(renames["DateOut"]).optional(),
            "status": t.proxy(renames["ReportStatusOut"]).optional(),
            "googleCloudStoragePath": t.string().optional(),
            "reportDataEndDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportMetadataOut"])
    types["ReportIn"] = t.struct(
        {
            "params": t.proxy(renames["ParametersIn"]).optional(),
            "key": t.proxy(renames["ReportKeyIn"]).optional(),
            "metadata": t.proxy(renames["ReportMetadataIn"]).optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "params": t.proxy(renames["ParametersOut"]).optional(),
            "key": t.proxy(renames["ReportKeyOut"]).optional(),
            "metadata": t.proxy(renames["ReportMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])

    functions = {}
    functions["queriesDelete"] = doubleclickbidmanager.get(
        "queries/{queryId}",
        t.struct({"queryId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesRun"] = doubleclickbidmanager.get(
        "queries/{queryId}",
        t.struct({"queryId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesList"] = doubleclickbidmanager.get(
        "queries/{queryId}",
        t.struct({"queryId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesCreate"] = doubleclickbidmanager.get(
        "queries/{queryId}",
        t.struct({"queryId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesGet"] = doubleclickbidmanager.get(
        "queries/{queryId}",
        t.struct({"queryId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["QueryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["queriesReportsGet"] = doubleclickbidmanager.get(
        "queries/{queryId}/reports",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "queryId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "orderBy": t.string().optional(),
                "queryId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
