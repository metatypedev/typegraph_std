from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_clouderrorreporting() -> Import:
    clouderrorreporting = HTTPRuntime("https://clouderrorreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouderrorreporting_1_ErrorResponse",
        "ListEventsResponseIn": "_clouderrorreporting_2_ListEventsResponseIn",
        "ListEventsResponseOut": "_clouderrorreporting_3_ListEventsResponseOut",
        "ServiceContextIn": "_clouderrorreporting_4_ServiceContextIn",
        "ServiceContextOut": "_clouderrorreporting_5_ServiceContextOut",
        "ErrorGroupStatsIn": "_clouderrorreporting_6_ErrorGroupStatsIn",
        "ErrorGroupStatsOut": "_clouderrorreporting_7_ErrorGroupStatsOut",
        "ReportedErrorEventIn": "_clouderrorreporting_8_ReportedErrorEventIn",
        "ReportedErrorEventOut": "_clouderrorreporting_9_ReportedErrorEventOut",
        "HttpRequestContextIn": "_clouderrorreporting_10_HttpRequestContextIn",
        "HttpRequestContextOut": "_clouderrorreporting_11_HttpRequestContextOut",
        "SourceLocationIn": "_clouderrorreporting_12_SourceLocationIn",
        "SourceLocationOut": "_clouderrorreporting_13_SourceLocationOut",
        "DeleteEventsResponseIn": "_clouderrorreporting_14_DeleteEventsResponseIn",
        "DeleteEventsResponseOut": "_clouderrorreporting_15_DeleteEventsResponseOut",
        "TrackingIssueIn": "_clouderrorreporting_16_TrackingIssueIn",
        "TrackingIssueOut": "_clouderrorreporting_17_TrackingIssueOut",
        "ErrorGroupIn": "_clouderrorreporting_18_ErrorGroupIn",
        "ErrorGroupOut": "_clouderrorreporting_19_ErrorGroupOut",
        "ErrorEventIn": "_clouderrorreporting_20_ErrorEventIn",
        "ErrorEventOut": "_clouderrorreporting_21_ErrorEventOut",
        "TimedCountIn": "_clouderrorreporting_22_TimedCountIn",
        "TimedCountOut": "_clouderrorreporting_23_TimedCountOut",
        "ListGroupStatsResponseIn": "_clouderrorreporting_24_ListGroupStatsResponseIn",
        "ListGroupStatsResponseOut": "_clouderrorreporting_25_ListGroupStatsResponseOut",
        "ErrorContextIn": "_clouderrorreporting_26_ErrorContextIn",
        "ErrorContextOut": "_clouderrorreporting_27_ErrorContextOut",
        "ReportErrorEventResponseIn": "_clouderrorreporting_28_ReportErrorEventResponseIn",
        "ReportErrorEventResponseOut": "_clouderrorreporting_29_ReportErrorEventResponseOut",
        "SourceReferenceIn": "_clouderrorreporting_30_SourceReferenceIn",
        "SourceReferenceOut": "_clouderrorreporting_31_SourceReferenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ServiceContextIn"] = t.struct(
        {
            "version": t.string().optional(),
            "service": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["ServiceContextIn"])
    types["ServiceContextOut"] = t.struct(
        {
            "version": t.string().optional(),
            "service": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceContextOut"])
    types["ErrorGroupStatsIn"] = t.struct(
        {
            "firstSeenTime": t.string().optional(),
            "timedCounts": t.array(t.proxy(renames["TimedCountIn"])).optional(),
            "lastSeenTime": t.string().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextIn"])
            ).optional(),
            "count": t.string().optional(),
            "representative": t.proxy(renames["ErrorEventIn"]).optional(),
            "affectedUsersCount": t.string().optional(),
            "group": t.proxy(renames["ErrorGroupIn"]).optional(),
            "numAffectedServices": t.integer().optional(),
        }
    ).named(renames["ErrorGroupStatsIn"])
    types["ErrorGroupStatsOut"] = t.struct(
        {
            "firstSeenTime": t.string().optional(),
            "timedCounts": t.array(t.proxy(renames["TimedCountOut"])).optional(),
            "lastSeenTime": t.string().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextOut"])
            ).optional(),
            "count": t.string().optional(),
            "representative": t.proxy(renames["ErrorEventOut"]).optional(),
            "affectedUsersCount": t.string().optional(),
            "group": t.proxy(renames["ErrorGroupOut"]).optional(),
            "numAffectedServices": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorGroupStatsOut"])
    types["ReportedErrorEventIn"] = t.struct(
        {
            "eventTime": t.string().optional(),
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "message": t.string(),
            "serviceContext": t.proxy(renames["ServiceContextIn"]),
        }
    ).named(renames["ReportedErrorEventIn"])
    types["ReportedErrorEventOut"] = t.struct(
        {
            "eventTime": t.string().optional(),
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "message": t.string(),
            "serviceContext": t.proxy(renames["ServiceContextOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportedErrorEventOut"])
    types["HttpRequestContextIn"] = t.struct(
        {
            "userAgent": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
            "remoteIp": t.string().optional(),
            "referrer": t.string().optional(),
            "url": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["HttpRequestContextIn"])
    types["HttpRequestContextOut"] = t.struct(
        {
            "userAgent": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
            "remoteIp": t.string().optional(),
            "referrer": t.string().optional(),
            "url": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestContextOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "functionName": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "filePath": t.string().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
    types["DeleteEventsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteEventsResponseIn"]
    )
    types["DeleteEventsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteEventsResponseOut"])
    types["TrackingIssueIn"] = t.struct({"url": t.string().optional()}).named(
        renames["TrackingIssueIn"]
    )
    types["TrackingIssueOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackingIssueOut"])
    types["ErrorGroupIn"] = t.struct(
        {
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueIn"])).optional(),
            "resolutionStatus": t.string().optional(),
            "groupId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ErrorGroupIn"])
    types["ErrorGroupOut"] = t.struct(
        {
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueOut"])).optional(),
            "resolutionStatus": t.string().optional(),
            "groupId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorGroupOut"])
    types["ErrorEventIn"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "eventTime": t.string().optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextIn"]).optional(),
        }
    ).named(renames["ErrorEventIn"])
    types["ErrorEventOut"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "eventTime": t.string().optional(),
            "message": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorEventOut"])
    types["TimedCountIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "count": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["TimedCountIn"])
    types["TimedCountOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "count": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimedCountOut"])
    types["ListGroupStatsResponseIn"] = t.struct(
        {
            "timeRangeBegin": t.string().optional(),
            "errorGroupStats": t.array(
                t.proxy(renames["ErrorGroupStatsIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGroupStatsResponseIn"])
    types["ListGroupStatsResponseOut"] = t.struct(
        {
            "timeRangeBegin": t.string().optional(),
            "errorGroupStats": t.array(
                t.proxy(renames["ErrorGroupStatsOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupStatsResponseOut"])
    types["ErrorContextIn"] = t.struct(
        {
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "reportLocation": t.proxy(renames["SourceLocationIn"]).optional(),
            "user": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestContextIn"]).optional(),
        }
    ).named(renames["ErrorContextIn"])
    types["ErrorContextOut"] = t.struct(
        {
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "reportLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "user": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorContextOut"])
    types["ReportErrorEventResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportErrorEventResponseIn"]
    )
    types["ReportErrorEventResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportErrorEventResponseOut"])
    types["SourceReferenceIn"] = t.struct(
        {"revisionId": t.string().optional(), "repository": t.string().optional()}
    ).named(renames["SourceReferenceIn"])
    types["SourceReferenceOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "repository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceReferenceOut"])

    functions = {}
    functions["projectsDeleteEvents"] = clouderrorreporting.delete(
        "v1beta1/{projectName}/events",
        t.struct({"projectName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeleteEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsEventsReport"] = clouderrorreporting.get(
        "v1beta1/{projectName}/events",
        t.struct(
            {
                "timeRange.period": t.string().optional(),
                "groupId": t.string(),
                "serviceFilter.service": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectName": t.string(),
                "pageToken": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
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
                "groupId": t.string(),
                "serviceFilter.service": t.string().optional(),
                "pageSize": t.integer().optional(),
                "projectName": t.string(),
                "pageToken": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEventsResponseOut"]),
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
                "alignment": t.string().optional(),
                "serviceFilter.service": t.string().optional(),
                "timedCountDuration": t.string().optional(),
                "pageSize": t.integer().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "order": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "pageToken": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
                "projectName": t.string(),
                "alignmentTime": t.string().optional(),
                "groupId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouderrorreporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
