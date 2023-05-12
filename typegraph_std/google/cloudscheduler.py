from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudscheduler() -> Import:
    cloudscheduler = HTTPRuntime("https://cloudscheduler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudscheduler_1_ErrorResponse",
        "PubsubTargetIn": "_cloudscheduler_2_PubsubTargetIn",
        "PubsubTargetOut": "_cloudscheduler_3_PubsubTargetOut",
        "JobIn": "_cloudscheduler_4_JobIn",
        "JobOut": "_cloudscheduler_5_JobOut",
        "RunJobRequestIn": "_cloudscheduler_6_RunJobRequestIn",
        "RunJobRequestOut": "_cloudscheduler_7_RunJobRequestOut",
        "ListLocationsResponseIn": "_cloudscheduler_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudscheduler_9_ListLocationsResponseOut",
        "StatusIn": "_cloudscheduler_10_StatusIn",
        "StatusOut": "_cloudscheduler_11_StatusOut",
        "RetryConfigIn": "_cloudscheduler_12_RetryConfigIn",
        "RetryConfigOut": "_cloudscheduler_13_RetryConfigOut",
        "AppEngineRoutingIn": "_cloudscheduler_14_AppEngineRoutingIn",
        "AppEngineRoutingOut": "_cloudscheduler_15_AppEngineRoutingOut",
        "PauseJobRequestIn": "_cloudscheduler_16_PauseJobRequestIn",
        "PauseJobRequestOut": "_cloudscheduler_17_PauseJobRequestOut",
        "LocationIn": "_cloudscheduler_18_LocationIn",
        "LocationOut": "_cloudscheduler_19_LocationOut",
        "OAuthTokenIn": "_cloudscheduler_20_OAuthTokenIn",
        "OAuthTokenOut": "_cloudscheduler_21_OAuthTokenOut",
        "HttpTargetIn": "_cloudscheduler_22_HttpTargetIn",
        "HttpTargetOut": "_cloudscheduler_23_HttpTargetOut",
        "PubsubMessageIn": "_cloudscheduler_24_PubsubMessageIn",
        "PubsubMessageOut": "_cloudscheduler_25_PubsubMessageOut",
        "ListJobsResponseIn": "_cloudscheduler_26_ListJobsResponseIn",
        "ListJobsResponseOut": "_cloudscheduler_27_ListJobsResponseOut",
        "EmptyIn": "_cloudscheduler_28_EmptyIn",
        "EmptyOut": "_cloudscheduler_29_EmptyOut",
        "ResumeJobRequestIn": "_cloudscheduler_30_ResumeJobRequestIn",
        "ResumeJobRequestOut": "_cloudscheduler_31_ResumeJobRequestOut",
        "OidcTokenIn": "_cloudscheduler_32_OidcTokenIn",
        "OidcTokenOut": "_cloudscheduler_33_OidcTokenOut",
        "AppEngineHttpTargetIn": "_cloudscheduler_34_AppEngineHttpTargetIn",
        "AppEngineHttpTargetOut": "_cloudscheduler_35_AppEngineHttpTargetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PubsubTargetIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "data": t.string().optional(),
            "topicName": t.string(),
        }
    ).named(renames["PubsubTargetIn"])
    types["PubsubTargetOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "data": t.string().optional(),
            "topicName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubTargetOut"])
    types["JobIn"] = t.struct(
        {
            "appEngineHttpTarget": t.proxy(renames["AppEngineHttpTargetIn"]).optional(),
            "httpTarget": t.proxy(renames["HttpTargetIn"]).optional(),
            "timeZone": t.string().optional(),
            "userUpdateTime": t.string().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "state": t.string().optional(),
            "pubsubTarget": t.proxy(renames["PubsubTargetIn"]).optional(),
            "scheduleTime": t.string().optional(),
            "schedule": t.string(),
            "name": t.string().optional(),
            "lastAttemptTime": t.string().optional(),
            "attemptDeadline": t.string().optional(),
            "description": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "appEngineHttpTarget": t.proxy(
                renames["AppEngineHttpTargetOut"]
            ).optional(),
            "httpTarget": t.proxy(renames["HttpTargetOut"]).optional(),
            "timeZone": t.string().optional(),
            "userUpdateTime": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "state": t.string().optional(),
            "pubsubTarget": t.proxy(renames["PubsubTargetOut"]).optional(),
            "scheduleTime": t.string().optional(),
            "schedule": t.string(),
            "name": t.string().optional(),
            "lastAttemptTime": t.string().optional(),
            "attemptDeadline": t.string().optional(),
            "description": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["RunJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunJobRequestIn"]
    )
    types["RunJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunJobRequestOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["RetryConfigIn"] = t.struct(
        {
            "maxBackoffDuration": t.string().optional(),
            "retryCount": t.integer().optional(),
            "minBackoffDuration": t.string().optional(),
            "maxRetryDuration": t.string().optional(),
            "maxDoublings": t.integer().optional(),
        }
    ).named(renames["RetryConfigIn"])
    types["RetryConfigOut"] = t.struct(
        {
            "maxBackoffDuration": t.string().optional(),
            "retryCount": t.integer().optional(),
            "minBackoffDuration": t.string().optional(),
            "maxRetryDuration": t.string().optional(),
            "maxDoublings": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryConfigOut"])
    types["AppEngineRoutingIn"] = t.struct(
        {
            "service": t.string().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "host": t.string().optional(),
        }
    ).named(renames["AppEngineRoutingIn"])
    types["AppEngineRoutingOut"] = t.struct(
        {
            "service": t.string().optional(),
            "version": t.string().optional(),
            "instance": t.string().optional(),
            "host": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineRoutingOut"])
    types["PauseJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseJobRequestIn"]
    )
    types["PauseJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseJobRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["HttpTargetIn"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "oauthToken": t.proxy(renames["OAuthTokenIn"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string(),
            "body": t.string().optional(),
        }
    ).named(renames["HttpTargetIn"])
    types["HttpTargetOut"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "oauthToken": t.proxy(renames["OAuthTokenOut"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string(),
            "body": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpTargetOut"])
    types["PubsubMessageIn"] = t.struct(
        {
            "messageId": t.string().optional(),
            "publishTime": t.string().optional(),
            "orderingKey": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "messageId": t.string().optional(),
            "publishTime": t.string().optional(),
            "orderingKey": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ResumeJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeJobRequestIn"]
    )
    types["ResumeJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeJobRequestOut"])
    types["OidcTokenIn"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "audience": t.string().optional(),
        }
    ).named(renames["OidcTokenIn"])
    types["OidcTokenOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "audience": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OidcTokenOut"])
    types["AppEngineHttpTargetIn"] = t.struct(
        {
            "appEngineRouting": t.proxy(renames["AppEngineRoutingIn"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "relativeUri": t.string().optional(),
        }
    ).named(renames["AppEngineHttpTargetIn"])
    types["AppEngineHttpTargetOut"] = t.struct(
        {
            "appEngineRouting": t.proxy(renames["AppEngineRoutingOut"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "relativeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineHttpTargetOut"])

    functions = {}
    functions["projectsLocationsGet"] = cloudscheduler.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPause"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPatch"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsRun"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsResume"] = cloudscheduler.post(
        "v1/{name}:resume",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudscheduler",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
