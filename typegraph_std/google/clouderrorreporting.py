from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_clouderrorreporting():
    clouderrorreporting = HTTPRuntime("https://clouderrorreporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouderrorreporting_1_ErrorResponse",
        "TimedCountIn": "_clouderrorreporting_2_TimedCountIn",
        "TimedCountOut": "_clouderrorreporting_3_TimedCountOut",
        "ErrorEventIn": "_clouderrorreporting_4_ErrorEventIn",
        "ErrorEventOut": "_clouderrorreporting_5_ErrorEventOut",
        "ErrorGroupIn": "_clouderrorreporting_6_ErrorGroupIn",
        "ErrorGroupOut": "_clouderrorreporting_7_ErrorGroupOut",
        "ListGroupStatsResponseIn": "_clouderrorreporting_8_ListGroupStatsResponseIn",
        "ListGroupStatsResponseOut": "_clouderrorreporting_9_ListGroupStatsResponseOut",
        "ServiceContextIn": "_clouderrorreporting_10_ServiceContextIn",
        "ServiceContextOut": "_clouderrorreporting_11_ServiceContextOut",
        "SourceLocationIn": "_clouderrorreporting_12_SourceLocationIn",
        "SourceLocationOut": "_clouderrorreporting_13_SourceLocationOut",
        "SourceReferenceIn": "_clouderrorreporting_14_SourceReferenceIn",
        "SourceReferenceOut": "_clouderrorreporting_15_SourceReferenceOut",
        "DeleteEventsResponseIn": "_clouderrorreporting_16_DeleteEventsResponseIn",
        "DeleteEventsResponseOut": "_clouderrorreporting_17_DeleteEventsResponseOut",
        "TrackingIssueIn": "_clouderrorreporting_18_TrackingIssueIn",
        "TrackingIssueOut": "_clouderrorreporting_19_TrackingIssueOut",
        "HttpRequestContextIn": "_clouderrorreporting_20_HttpRequestContextIn",
        "HttpRequestContextOut": "_clouderrorreporting_21_HttpRequestContextOut",
        "ReportedErrorEventIn": "_clouderrorreporting_22_ReportedErrorEventIn",
        "ReportedErrorEventOut": "_clouderrorreporting_23_ReportedErrorEventOut",
        "ErrorContextIn": "_clouderrorreporting_24_ErrorContextIn",
        "ErrorContextOut": "_clouderrorreporting_25_ErrorContextOut",
        "ReportErrorEventResponseIn": "_clouderrorreporting_26_ReportErrorEventResponseIn",
        "ReportErrorEventResponseOut": "_clouderrorreporting_27_ReportErrorEventResponseOut",
        "ErrorGroupStatsIn": "_clouderrorreporting_28_ErrorGroupStatsIn",
        "ErrorGroupStatsOut": "_clouderrorreporting_29_ErrorGroupStatsOut",
        "ListEventsResponseIn": "_clouderrorreporting_30_ListEventsResponseIn",
        "ListEventsResponseOut": "_clouderrorreporting_31_ListEventsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TimedCountIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["TimedCountIn"])
    types["TimedCountOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimedCountOut"])
    types["ErrorEventIn"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "serviceContext": t.proxy(renames["ServiceContextIn"]).optional(),
            "eventTime": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ErrorEventIn"])
    types["ErrorEventOut"] = t.struct(
        {
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "serviceContext": t.proxy(renames["ServiceContextOut"]).optional(),
            "eventTime": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorEventOut"])
    types["ErrorGroupIn"] = t.struct(
        {
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueIn"])).optional(),
            "name": t.string().optional(),
            "groupId": t.string().optional(),
            "resolutionStatus": t.string().optional(),
        }
    ).named(renames["ErrorGroupIn"])
    types["ErrorGroupOut"] = t.struct(
        {
            "trackingIssues": t.array(t.proxy(renames["TrackingIssueOut"])).optional(),
            "name": t.string().optional(),
            "groupId": t.string().optional(),
            "resolutionStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorGroupOut"])
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
    types["ServiceContextIn"] = t.struct(
        {
            "service": t.string().optional(),
            "resourceType": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ServiceContextIn"])
    types["ServiceContextOut"] = t.struct(
        {
            "service": t.string().optional(),
            "resourceType": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceContextOut"])
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
    types["HttpRequestContextIn"] = t.struct(
        {
            "remoteIp": t.string().optional(),
            "url": t.string().optional(),
            "referrer": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
            "method": t.string().optional(),
            "userAgent": t.string().optional(),
        }
    ).named(renames["HttpRequestContextIn"])
    types["HttpRequestContextOut"] = t.struct(
        {
            "remoteIp": t.string().optional(),
            "url": t.string().optional(),
            "referrer": t.string().optional(),
            "responseStatusCode": t.integer().optional(),
            "method": t.string().optional(),
            "userAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestContextOut"])
    types["ReportedErrorEventIn"] = t.struct(
        {
            "serviceContext": t.proxy(renames["ServiceContextIn"]),
            "context": t.proxy(renames["ErrorContextIn"]).optional(),
            "eventTime": t.string().optional(),
            "message": t.string(),
        }
    ).named(renames["ReportedErrorEventIn"])
    types["ReportedErrorEventOut"] = t.struct(
        {
            "serviceContext": t.proxy(renames["ServiceContextOut"]),
            "context": t.proxy(renames["ErrorContextOut"]).optional(),
            "eventTime": t.string().optional(),
            "message": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportedErrorEventOut"])
    types["ErrorContextIn"] = t.struct(
        {
            "httpRequest": t.proxy(renames["HttpRequestContextIn"]).optional(),
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceIn"])
            ).optional(),
            "user": t.string().optional(),
            "reportLocation": t.proxy(renames["SourceLocationIn"]).optional(),
        }
    ).named(renames["ErrorContextIn"])
    types["ErrorContextOut"] = t.struct(
        {
            "httpRequest": t.proxy(renames["HttpRequestContextOut"]).optional(),
            "sourceReferences": t.array(
                t.proxy(renames["SourceReferenceOut"])
            ).optional(),
            "user": t.string().optional(),
            "reportLocation": t.proxy(renames["SourceLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorContextOut"])
    types["ReportErrorEventResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportErrorEventResponseIn"]
    )
    types["ReportErrorEventResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportErrorEventResponseOut"])
    types["ErrorGroupStatsIn"] = t.struct(
        {
            "representative": t.proxy(renames["ErrorEventIn"]).optional(),
            "count": t.string().optional(),
            "affectedUsersCount": t.string().optional(),
            "timedCounts": t.array(t.proxy(renames["TimedCountIn"])).optional(),
            "firstSeenTime": t.string().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextIn"])
            ).optional(),
            "lastSeenTime": t.string().optional(),
            "numAffectedServices": t.integer().optional(),
            "group": t.proxy(renames["ErrorGroupIn"]).optional(),
        }
    ).named(renames["ErrorGroupStatsIn"])
    types["ErrorGroupStatsOut"] = t.struct(
        {
            "representative": t.proxy(renames["ErrorEventOut"]).optional(),
            "count": t.string().optional(),
            "affectedUsersCount": t.string().optional(),
            "timedCounts": t.array(t.proxy(renames["TimedCountOut"])).optional(),
            "firstSeenTime": t.string().optional(),
            "affectedServices": t.array(
                t.proxy(renames["ServiceContextOut"])
            ).optional(),
            "lastSeenTime": t.string().optional(),
            "numAffectedServices": t.integer().optional(),
            "group": t.proxy(renames["ErrorGroupOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorGroupStatsOut"])
    types["ListEventsResponseIn"] = t.struct(
        {
            "errorEvents": t.array(t.proxy(renames["ErrorEventIn"])).optional(),
            "timeRangeBegin": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEventsResponseIn"])
    types["ListEventsResponseOut"] = t.struct(
        {
            "errorEvents": t.array(t.proxy(renames["ErrorEventOut"])).optional(),
            "timeRangeBegin": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEventsResponseOut"])

    functions = {}
    functions["projectsDeleteEvents"] = clouderrorreporting.delete(
        "v1beta1/{projectName}/events",
        t.struct({"projectName": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeleteEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupStatsList"] = clouderrorreporting.get(
        "v1beta1/{projectName}/groupStats",
        t.struct(
            {
                "serviceFilter.service": t.string().optional(),
                "alignmentTime": t.string().optional(),
                "order": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "timedCountDuration": t.string().optional(),
                "alignment": t.string().optional(),
                "groupId": t.string().optional(),
                "serviceFilter.version": t.string().optional(),
                "projectName": t.string(),
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
                "pageToken": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "pageSize": t.integer().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "groupId": t.string(),
                "serviceFilter.service": t.string().optional(),
                "projectName": t.string(),
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
                "pageToken": t.string().optional(),
                "timeRange.period": t.string().optional(),
                "pageSize": t.integer().optional(),
                "serviceFilter.resourceType": t.string().optional(),
                "groupId": t.string(),
                "serviceFilter.service": t.string().optional(),
                "projectName": t.string(),
                "serviceFilter.version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = clouderrorreporting.put(
        "v1beta1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "trackingIssues": t.array(
                    t.proxy(renames["TrackingIssueIn"])
                ).optional(),
                "groupId": t.string().optional(),
                "resolutionStatus": t.string().optional(),
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
                "trackingIssues": t.array(
                    t.proxy(renames["TrackingIssueIn"])
                ).optional(),
                "groupId": t.string().optional(),
                "resolutionStatus": t.string().optional(),
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
