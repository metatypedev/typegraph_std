from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_clouderrorreporting() -> Import:
    clouderrorreporting = HTTPRuntime("https://clouderrorreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouderrorreporting_1_ErrorResponse",
        "TimedCountIn": "_clouderrorreporting_2_TimedCountIn",
        "TimedCountOut": "_clouderrorreporting_3_TimedCountOut",
        "DeleteEventsResponseIn": "_clouderrorreporting_4_DeleteEventsResponseIn",
        "DeleteEventsResponseOut": "_clouderrorreporting_5_DeleteEventsResponseOut",
        "ListGroupStatsResponseIn": "_clouderrorreporting_6_ListGroupStatsResponseIn",
        "ListGroupStatsResponseOut": "_clouderrorreporting_7_ListGroupStatsResponseOut",
        "HttpRequestContextIn": "_clouderrorreporting_8_HttpRequestContextIn",
        "HttpRequestContextOut": "_clouderrorreporting_9_HttpRequestContextOut",
        "ListEventsResponseIn": "_clouderrorreporting_10_ListEventsResponseIn",
        "ListEventsResponseOut": "_clouderrorreporting_11_ListEventsResponseOut",
        "ErrorContextIn": "_clouderrorreporting_12_ErrorContextIn",
        "ErrorContextOut": "_clouderrorreporting_13_ErrorContextOut",
        "ReportedErrorEventIn": "_clouderrorreporting_14_ReportedErrorEventIn",
        "ReportedErrorEventOut": "_clouderrorreporting_15_ReportedErrorEventOut",
        "SourceLocationIn": "_clouderrorreporting_16_SourceLocationIn",
        "SourceLocationOut": "_clouderrorreporting_17_SourceLocationOut",
        "ReportErrorEventResponseIn": "_clouderrorreporting_18_ReportErrorEventResponseIn",
        "ReportErrorEventResponseOut": "_clouderrorreporting_19_ReportErrorEventResponseOut",
        "ErrorEventIn": "_clouderrorreporting_20_ErrorEventIn",
        "ErrorEventOut": "_clouderrorreporting_21_ErrorEventOut",
        "ServiceContextIn": "_clouderrorreporting_22_ServiceContextIn",
        "ServiceContextOut": "_clouderrorreporting_23_ServiceContextOut",
        "SourceReferenceIn": "_clouderrorreporting_24_SourceReferenceIn",
        "SourceReferenceOut": "_clouderrorreporting_25_SourceReferenceOut",
        "TrackingIssueIn": "_clouderrorreporting_26_TrackingIssueIn",
        "TrackingIssueOut": "_clouderrorreporting_27_TrackingIssueOut",
        "ErrorGroupStatsIn": "_clouderrorreporting_28_ErrorGroupStatsIn",
        "ErrorGroupStatsOut": "_clouderrorreporting_29_ErrorGroupStatsOut",
        "ErrorGroupIn": "_clouderrorreporting_30_ErrorGroupIn",
        "ErrorGroupOut": "_clouderrorreporting_31_ErrorGroupOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TimedCountIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "count": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["TimedCountIn"])
    types["TimedCountOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "count": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimedCountOut"])
    types["DeleteEventsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteEventsResponseIn"]
    )
    types["DeleteEventsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteEventsResponseOut"])
    types["ListGroupStatsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "errorGroupStats": t.array(
                t.proxy(renames["ErrorGroupStatsIn"])
            ).optional(),
            "timeRangeBegin": t.string().optional(),
        }
    ).named(renames["ListGroupStatsResponseIn"])
    types["ListGroupStatsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "errorGroupStats": t.array(
                t.proxy(renames["ErrorGroupStatsOut"])
            ).optional(),
            "timeRangeBegin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupStatsResponseOut"])
    types["HttpRequestContextIn"] = t.struct(
        {
            "url": t.string().optional(),
            "remoteIp": t.string().optional(),
            "referrer": t.string().optional(),
            "userAgent": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["HttpRequestContextIn"])
    types["HttpRequestContextOut"] = t.struct(
        {
            "url": t.string().optional(),
            "remoteIp": t.string().optional(),
            "referrer": t.string().optional(),
            "userAgent": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestContextOut"])
    types["ListEventsResponseIn"] = t.struct(
        {
            "errorEvents": t.array(t.proxy(renames["ErrorEventIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "timeRangeBegin": t.string().optional(),
        }
    ).named(renames["ListEventsResponseIn"])
    types["ListEventsResponseOut"] = t.struct(
        {
            "errorEvents": t.array(t.proxy(renames["ErrorEventOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "timeRangeBegin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEventsResponseOut"])
    types["ErrorContextIn"] = t.struct(
        {
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "httpRequest": t.proxy(renames["HttpRequestContextIn"]).optional(),
            "reportLocation": t.proxy(renames["SourceLocationIn"]).optional(),
            "user": t.string().optional(),
        }
    ).named(renames["ErrorContextIn"])
    types["ErrorContextOut"] = t.struct(
        {
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "httpRequest": t.proxy(renames["HttpRequestContextOut"]).optional(),
            "reportLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "user": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorContextOut"])
    types["ReportedErrorEventIn"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "eventTime": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextIn"]),
            "message": t.string(),
        }
    ).named(renames["ReportedErrorEventIn"])
    types["ReportedErrorEventOut"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "eventTime": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextOut"]),
            "message": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportedErrorEventOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "filePath": t.string().optional(),
            "functionName": t.string().optional(),
            "lineNumber": t.integer().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "functionName": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
    types["ReportErrorEventResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportErrorEventResponseIn"]
    )
    types["ReportErrorEventResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportErrorEventResponseOut"])
    types["ErrorEventIn"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "message": t.string().optional(),
            "eventTime": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextIn"]).optional(),
        }
    ).named(renames["ErrorEventIn"])
    types["ErrorEventOut"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "message": t.string().optional(),
            "eventTime": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorEventOut"])
    types["ServiceContextIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "service": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ServiceContextIn"])
    types["ServiceContextOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "service": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceContextOut"])
    types["SourceReferenceIn"] = t.struct(
        {"repository": t.string().optional(), "revisionId": t.string().optional()}
    ).named(renames["SourceReferenceIn"])
    types["SourceReferenceOut"] = t.struct(
        {
            "repository": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceReferenceOut"])
    types["TrackingIssueIn"] = t.struct({"url": t.string().optional()}).named(
        renames["TrackingIssueIn"]
    )
    types["TrackingIssueOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackingIssueOut"])
    types["ErrorGroupStatsIn"] = t.struct(
        {
            "timedCounts": t.array(t.proxy(renames["TimedCountIn"])).optional(),
            "affectedUsersCount": t.string().optional(),
            "lastSeenTime": t.string().optional(),
            "firstSeenTime": t.string().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextIn"])
            ).optional(),
            "group": t.proxy(renames["ErrorGroupIn"]).optional(),
            "numAffectedServices": t.integer().optional(),
            "count": t.string().optional(),
            "representative": t.proxy(renames["ErrorEventIn"]).optional(),
        }
    ).named(renames["ErrorGroupStatsIn"])
    types["ErrorGroupStatsOut"] = t.struct(
        {
            "timedCounts": t.array(t.proxy(renames["TimedCountOut"])).optional(),
            "affectedUsersCount": t.string().optional(),
            "lastSeenTime": t.string().optional(),
            "firstSeenTime": t.string().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextOut"])
            ).optional(),
            "group": t.proxy(renames["ErrorGroupOut"]).optional(),
            "numAffectedServices": t.integer().optional(),
            "count": t.string().optional(),
            "representative": t.proxy(renames["ErrorEventOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorGroupStatsOut"])
    types["ErrorGroupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "resolutionStatus": t.string().optional(),
            "groupId": t.string().optional(),
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueIn"])).optional(),
        }
    ).named(renames["ErrorGroupIn"])
    types["ErrorGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "resolutionStatus": t.string().optional(),
            "groupId": t.string().optional(),
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorGroupOut"])

    functions = {}
    functions["projectsDeleteEvents"] = clouderrorreporting.delete(
        "v1beta1/{projectName}/events",
        t.struct({"projectName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeleteEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsUpdate"] = clouderrorreporting.get(
        "v1beta1/{groupName}",
        t.struct({"groupName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ErrorGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = clouderrorreporting.get(
        "v1beta1/{groupName}",
        t.struct({"groupName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ErrorGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupStatsList"] = clouderrorreporting.get(
        "v1beta1/{projectName}/groupStats",
        t.struct(
            {
                "alignmentTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "projectName": t.string(),
                "serviceFilter.resourceType": t.string().optional(),
                "order": t.string().optional(),
                "timedCountDuration": t.string().optional(),
                "serviceFilter.service": t.string().optional(),
                "pageSize": t.integer().optional(),
                "alignment": t.string().optional(),
                "groupId": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEventsReport"] = clouderrorreporting.get(
        "v1beta1/{projectName}/events",
        t.struct(
            {
                "timeRange.period": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
                "projectName": t.string(),
                "groupId": t.string(),
                "serviceFilter.service": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEventsList"] = clouderrorreporting.get(
        "v1beta1/{projectName}/events",
        t.struct(
            {
                "timeRange.period": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
                "projectName": t.string(),
                "groupId": t.string(),
                "serviceFilter.service": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouderrorreporting",
        renames=renames,
        types=types,
        functions=functions,
    )
