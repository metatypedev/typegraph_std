from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_clouderrorreporting() -> Import:
    clouderrorreporting = HTTPRuntime("https://clouderrorreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouderrorreporting_1_ErrorResponse",
        "ErrorEventIn": "_clouderrorreporting_2_ErrorEventIn",
        "ErrorEventOut": "_clouderrorreporting_3_ErrorEventOut",
        "DeleteEventsResponseIn": "_clouderrorreporting_4_DeleteEventsResponseIn",
        "DeleteEventsResponseOut": "_clouderrorreporting_5_DeleteEventsResponseOut",
        "ErrorContextIn": "_clouderrorreporting_6_ErrorContextIn",
        "ErrorContextOut": "_clouderrorreporting_7_ErrorContextOut",
        "ListGroupStatsResponseIn": "_clouderrorreporting_8_ListGroupStatsResponseIn",
        "ListGroupStatsResponseOut": "_clouderrorreporting_9_ListGroupStatsResponseOut",
        "HttpRequestContextIn": "_clouderrorreporting_10_HttpRequestContextIn",
        "HttpRequestContextOut": "_clouderrorreporting_11_HttpRequestContextOut",
        "ReportErrorEventResponseIn": "_clouderrorreporting_12_ReportErrorEventResponseIn",
        "ReportErrorEventResponseOut": "_clouderrorreporting_13_ReportErrorEventResponseOut",
        "ErrorGroupStatsIn": "_clouderrorreporting_14_ErrorGroupStatsIn",
        "ErrorGroupStatsOut": "_clouderrorreporting_15_ErrorGroupStatsOut",
        "ServiceContextIn": "_clouderrorreporting_16_ServiceContextIn",
        "ServiceContextOut": "_clouderrorreporting_17_ServiceContextOut",
        "ListEventsResponseIn": "_clouderrorreporting_18_ListEventsResponseIn",
        "ListEventsResponseOut": "_clouderrorreporting_19_ListEventsResponseOut",
        "TimedCountIn": "_clouderrorreporting_20_TimedCountIn",
        "TimedCountOut": "_clouderrorreporting_21_TimedCountOut",
        "SourceReferenceIn": "_clouderrorreporting_22_SourceReferenceIn",
        "SourceReferenceOut": "_clouderrorreporting_23_SourceReferenceOut",
        "ReportedErrorEventIn": "_clouderrorreporting_24_ReportedErrorEventIn",
        "ReportedErrorEventOut": "_clouderrorreporting_25_ReportedErrorEventOut",
        "SourceLocationIn": "_clouderrorreporting_26_SourceLocationIn",
        "SourceLocationOut": "_clouderrorreporting_27_SourceLocationOut",
        "TrackingIssueIn": "_clouderrorreporting_28_TrackingIssueIn",
        "TrackingIssueOut": "_clouderrorreporting_29_TrackingIssueOut",
        "ErrorGroupIn": "_clouderrorreporting_30_ErrorGroupIn",
        "ErrorGroupOut": "_clouderrorreporting_31_ErrorGroupOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ErrorEventIn"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "eventTime": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextIn"]).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ErrorEventIn"])
    types["ErrorEventOut"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "eventTime": t.string().optional(),
            "serviceContext": t.proxy(renames["ServiceContextOut"]).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorEventOut"])
    types["DeleteEventsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteEventsResponseIn"]
    )
    types["DeleteEventsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteEventsResponseOut"])
    types["ErrorContextIn"] = t.struct(
        {
            "reportLocation": t.proxy(renames["SourceLocationIn"]).optional(),
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "user": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestContextIn"]).optional(),
        }
    ).named(renames["ErrorContextIn"])
    types["ErrorContextOut"] = t.struct(
        {
            "reportLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "user": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorContextOut"])
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
    types["HttpRequestContextIn"] = t.struct(
        {
            "remoteIp": t.string().optional(),
            "userAgent": t.string().optional(),
            "url": t.string().optional(),
            "referrer": t.string().optional(),
            "method": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
        }
    ).named(renames["HttpRequestContextIn"])
    types["HttpRequestContextOut"] = t.struct(
        {
            "remoteIp": t.string().optional(),
            "userAgent": t.string().optional(),
            "url": t.string().optional(),
            "referrer": t.string().optional(),
            "method": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestContextOut"])
    types["ReportErrorEventResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportErrorEventResponseIn"]
    )
    types["ReportErrorEventResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportErrorEventResponseOut"])
    types["ErrorGroupStatsIn"] = t.struct(
        {
            "timedCounts": t.array(t.proxy(renames["TimedCountIn"])).optional(),
            "numAffectedServices": t.integer().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextIn"])
            ).optional(),
            "group": t.proxy(renames["ErrorGroupIn"]).optional(),
            "representative": t.proxy(renames["ErrorEventIn"]).optional(),
            "lastSeenTime": t.string().optional(),
            "count": t.string().optional(),
            "firstSeenTime": t.string().optional(),
            "affectedUsersCount": t.string().optional(),
        }
    ).named(renames["ErrorGroupStatsIn"])
    types["ErrorGroupStatsOut"] = t.struct(
        {
            "timedCounts": t.array(t.proxy(renames["TimedCountOut"])).optional(),
            "numAffectedServices": t.integer().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextOut"])
            ).optional(),
            "group": t.proxy(renames["ErrorGroupOut"]).optional(),
            "representative": t.proxy(renames["ErrorEventOut"]).optional(),
            "lastSeenTime": t.string().optional(),
            "count": t.string().optional(),
            "firstSeenTime": t.string().optional(),
            "affectedUsersCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorGroupStatsOut"])
    types["ServiceContextIn"] = t.struct(
        {
            "version": t.string().optional(),
            "resourceType": t.string().optional(),
            "service": t.string().optional(),
        }
    ).named(renames["ServiceContextIn"])
    types["ServiceContextOut"] = t.struct(
        {
            "version": t.string().optional(),
            "resourceType": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceContextOut"])
    types["ListEventsResponseIn"] = t.struct(
        {
            "timeRangeBegin": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "errorEvents": t.array(t.proxy(renames["ErrorEventIn"])).optional(),
        }
    ).named(renames["ListEventsResponseIn"])
    types["ListEventsResponseOut"] = t.struct(
        {
            "timeRangeBegin": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "errorEvents": t.array(t.proxy(renames["ErrorEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEventsResponseOut"])
    types["TimedCountIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["TimedCountIn"])
    types["TimedCountOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimedCountOut"])
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
    types["ReportedErrorEventIn"] = t.struct(
        {
            "serviceContext": t.proxy(renames["ServiceContextIn"]),
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "message": t.string(),
            "eventTime": t.string().optional(),
        }
    ).named(renames["ReportedErrorEventIn"])
    types["ReportedErrorEventOut"] = t.struct(
        {
            "serviceContext": t.proxy(renames["ServiceContextOut"]),
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "message": t.string(),
            "eventTime": t.string().optional(),
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
            "resolutionStatus": t.string().optional(),
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueIn"])).optional(),
            "groupId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ErrorGroupIn"])
    types["ErrorGroupOut"] = t.struct(
        {
            "resolutionStatus": t.string().optional(),
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueOut"])).optional(),
            "groupId": t.string().optional(),
            "name": t.string().optional(),
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
    functions["projectsEventsReport"] = clouderrorreporting.get(
        "v1beta1/{projectName}/events",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupId": t.string(),
                "serviceFilter.version": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "projectName": t.string(),
                "serviceFilter.service": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "groupId": t.string(),
                "serviceFilter.version": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "projectName": t.string(),
                "serviceFilter.service": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupStatsList"] = clouderrorreporting.get(
        "v1beta1/{projectName}/groupStats",
        t.struct(
            {
                "timedCountDuration": t.string().optional(),
                "order": t.string().optional(),
                "alignmentTime": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
                "groupId": t.string().optional(),
                "serviceFilter.service": t.string().optional(),
                "pageToken": t.string().optional(),
                "alignment": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "projectName": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGroupStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = clouderrorreporting.put(
        "v1beta1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "resolutionStatus": t.string().optional(),
                "trackingIssues": t.array(
                    t.proxy(renames["TrackingIssueIn"])
                ).optional(),
                "groupId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ErrorGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsUpdate"] = clouderrorreporting.put(
        "v1beta1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "resolutionStatus": t.string().optional(),
                "trackingIssues": t.array(
                    t.proxy(renames["TrackingIssueIn"])
                ).optional(),
                "groupId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ErrorGroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouderrorreporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
