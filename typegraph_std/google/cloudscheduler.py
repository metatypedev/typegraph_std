from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudscheduler():
    cloudscheduler = HTTPRuntime("https://cloudscheduler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudscheduler_1_ErrorResponse",
        "ListLocationsResponseIn": "_cloudscheduler_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudscheduler_3_ListLocationsResponseOut",
        "PauseJobRequestIn": "_cloudscheduler_4_PauseJobRequestIn",
        "PauseJobRequestOut": "_cloudscheduler_5_PauseJobRequestOut",
        "AppEngineHttpTargetIn": "_cloudscheduler_6_AppEngineHttpTargetIn",
        "AppEngineHttpTargetOut": "_cloudscheduler_7_AppEngineHttpTargetOut",
        "OAuthTokenIn": "_cloudscheduler_8_OAuthTokenIn",
        "OAuthTokenOut": "_cloudscheduler_9_OAuthTokenOut",
        "RunJobRequestIn": "_cloudscheduler_10_RunJobRequestIn",
        "RunJobRequestOut": "_cloudscheduler_11_RunJobRequestOut",
        "ListJobsResponseIn": "_cloudscheduler_12_ListJobsResponseIn",
        "ListJobsResponseOut": "_cloudscheduler_13_ListJobsResponseOut",
        "PubsubTargetIn": "_cloudscheduler_14_PubsubTargetIn",
        "PubsubTargetOut": "_cloudscheduler_15_PubsubTargetOut",
        "PubsubMessageIn": "_cloudscheduler_16_PubsubMessageIn",
        "PubsubMessageOut": "_cloudscheduler_17_PubsubMessageOut",
        "LocationIn": "_cloudscheduler_18_LocationIn",
        "LocationOut": "_cloudscheduler_19_LocationOut",
        "ResumeJobRequestIn": "_cloudscheduler_20_ResumeJobRequestIn",
        "ResumeJobRequestOut": "_cloudscheduler_21_ResumeJobRequestOut",
        "RetryConfigIn": "_cloudscheduler_22_RetryConfigIn",
        "RetryConfigOut": "_cloudscheduler_23_RetryConfigOut",
        "AppEngineRoutingIn": "_cloudscheduler_24_AppEngineRoutingIn",
        "AppEngineRoutingOut": "_cloudscheduler_25_AppEngineRoutingOut",
        "EmptyIn": "_cloudscheduler_26_EmptyIn",
        "EmptyOut": "_cloudscheduler_27_EmptyOut",
        "HttpTargetIn": "_cloudscheduler_28_HttpTargetIn",
        "HttpTargetOut": "_cloudscheduler_29_HttpTargetOut",
        "OidcTokenIn": "_cloudscheduler_30_OidcTokenIn",
        "OidcTokenOut": "_cloudscheduler_31_OidcTokenOut",
        "StatusIn": "_cloudscheduler_32_StatusIn",
        "StatusOut": "_cloudscheduler_33_StatusOut",
        "JobIn": "_cloudscheduler_34_JobIn",
        "JobOut": "_cloudscheduler_35_JobOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["PauseJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseJobRequestIn"]
    )
    types["PauseJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseJobRequestOut"])
    types["AppEngineHttpTargetIn"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingIn"]).optional(),
            "relativeUri": t.string().optional(),
        }
    ).named(renames["AppEngineHttpTargetIn"])
    types["AppEngineHttpTargetOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingOut"]).optional(),
            "relativeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineHttpTargetOut"])
    types["OAuthTokenIn"] = t.struct(
        {"scope": t.string().optional(), "serviceAccountEmail": t.string().optional()}
    ).named(renames["OAuthTokenIn"])
    types["OAuthTokenOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthTokenOut"])
    types["RunJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunJobRequestIn"]
    )
    types["RunJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunJobRequestOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["PubsubTargetIn"] = t.struct(
        {
            "topicName": t.string(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["PubsubTargetIn"])
    types["PubsubTargetOut"] = t.struct(
        {
            "topicName": t.string(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubTargetOut"])
    types["PubsubMessageIn"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "publishTime": t.string().optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "publishTime": t.string().optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ResumeJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeJobRequestIn"]
    )
    types["ResumeJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeJobRequestOut"])
    types["RetryConfigIn"] = t.struct(
        {
            "retryCount": t.integer().optional(),
            "maxDoublings": t.integer().optional(),
            "minBackoffDuration": t.string().optional(),
            "maxRetryDuration": t.string().optional(),
            "maxBackoffDuration": t.string().optional(),
        }
    ).named(renames["RetryConfigIn"])
    types["RetryConfigOut"] = t.struct(
        {
            "retryCount": t.integer().optional(),
            "maxDoublings": t.integer().optional(),
            "minBackoffDuration": t.string().optional(),
            "maxRetryDuration": t.string().optional(),
            "maxBackoffDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryConfigOut"])
    types["AppEngineRoutingIn"] = t.struct(
        {
            "service": t.string().optional(),
            "instance": t.string().optional(),
            "version": t.string().optional(),
            "host": t.string().optional(),
        }
    ).named(renames["AppEngineRoutingIn"])
    types["AppEngineRoutingOut"] = t.struct(
        {
            "service": t.string().optional(),
            "instance": t.string().optional(),
            "version": t.string().optional(),
            "host": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineRoutingOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["HttpTargetIn"] = t.struct(
        {
            "oauthToken": t.proxy(renames["OAuthTokenIn"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "uri": t.string(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HttpTargetIn"])
    types["HttpTargetOut"] = t.struct(
        {
            "oauthToken": t.proxy(renames["OAuthTokenOut"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "uri": t.string(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpTargetOut"])
    types["OidcTokenIn"] = t.struct(
        {
            "audience": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
        }
    ).named(renames["OidcTokenIn"])
    types["OidcTokenOut"] = t.struct(
        {
            "audience": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OidcTokenOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["JobIn"] = t.struct(
        {
            "name": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
            "appEngineHttpTarget": t.proxy(renames["AppEngineHttpTargetIn"]).optional(),
            "timeZone": t.string().optional(),
            "lastAttemptTime": t.string().optional(),
            "description": t.string().optional(),
            "schedule": t.string(),
            "state": t.string().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "userUpdateTime": t.string().optional(),
            "pubsubTarget": t.proxy(renames["PubsubTargetIn"]).optional(),
            "attemptDeadline": t.string().optional(),
            "httpTarget": t.proxy(renames["HttpTargetIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "name": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigOut"]).optional(),
            "appEngineHttpTarget": t.proxy(
                renames["AppEngineHttpTargetOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "lastAttemptTime": t.string().optional(),
            "description": t.string().optional(),
            "schedule": t.string(),
            "state": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "userUpdateTime": t.string().optional(),
            "pubsubTarget": t.proxy(renames["PubsubTargetOut"]).optional(),
            "attemptDeadline": t.string().optional(),
            "httpTarget": t.proxy(renames["HttpTargetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])

    functions = {}
    functions["projectsLocationsGet"] = cloudscheduler.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = cloudscheduler.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPatch"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsRun"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsResume"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPause"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = cloudscheduler.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudscheduler",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
