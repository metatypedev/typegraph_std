from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudscheduler() -> Import:
    cloudscheduler = HTTPRuntime("https://cloudscheduler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudscheduler_1_ErrorResponse",
        "HttpTargetIn": "_cloudscheduler_2_HttpTargetIn",
        "HttpTargetOut": "_cloudscheduler_3_HttpTargetOut",
        "LocationIn": "_cloudscheduler_4_LocationIn",
        "LocationOut": "_cloudscheduler_5_LocationOut",
        "ListJobsResponseIn": "_cloudscheduler_6_ListJobsResponseIn",
        "ListJobsResponseOut": "_cloudscheduler_7_ListJobsResponseOut",
        "OAuthTokenIn": "_cloudscheduler_8_OAuthTokenIn",
        "OAuthTokenOut": "_cloudscheduler_9_OAuthTokenOut",
        "ResumeJobRequestIn": "_cloudscheduler_10_ResumeJobRequestIn",
        "ResumeJobRequestOut": "_cloudscheduler_11_ResumeJobRequestOut",
        "RunJobRequestIn": "_cloudscheduler_12_RunJobRequestIn",
        "RunJobRequestOut": "_cloudscheduler_13_RunJobRequestOut",
        "RetryConfigIn": "_cloudscheduler_14_RetryConfigIn",
        "RetryConfigOut": "_cloudscheduler_15_RetryConfigOut",
        "OidcTokenIn": "_cloudscheduler_16_OidcTokenIn",
        "OidcTokenOut": "_cloudscheduler_17_OidcTokenOut",
        "PubsubTargetIn": "_cloudscheduler_18_PubsubTargetIn",
        "PubsubTargetOut": "_cloudscheduler_19_PubsubTargetOut",
        "StatusIn": "_cloudscheduler_20_StatusIn",
        "StatusOut": "_cloudscheduler_21_StatusOut",
        "JobIn": "_cloudscheduler_22_JobIn",
        "JobOut": "_cloudscheduler_23_JobOut",
        "AppEngineHttpTargetIn": "_cloudscheduler_24_AppEngineHttpTargetIn",
        "AppEngineHttpTargetOut": "_cloudscheduler_25_AppEngineHttpTargetOut",
        "EmptyIn": "_cloudscheduler_26_EmptyIn",
        "EmptyOut": "_cloudscheduler_27_EmptyOut",
        "AppEngineRoutingIn": "_cloudscheduler_28_AppEngineRoutingIn",
        "AppEngineRoutingOut": "_cloudscheduler_29_AppEngineRoutingOut",
        "PauseJobRequestIn": "_cloudscheduler_30_PauseJobRequestIn",
        "PauseJobRequestOut": "_cloudscheduler_31_PauseJobRequestOut",
        "ListLocationsResponseIn": "_cloudscheduler_32_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudscheduler_33_ListLocationsResponseOut",
        "PubsubMessageIn": "_cloudscheduler_34_PubsubMessageIn",
        "PubsubMessageOut": "_cloudscheduler_35_PubsubMessageOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["HttpTargetIn"] = t.struct(
        {
            "uri": t.string(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "body": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "httpMethod": t.string().optional(),
            "oauthToken": t.proxy(renames["OAuthTokenIn"]).optional(),
        }
    ).named(renames["HttpTargetIn"])
    types["HttpTargetOut"] = t.struct(
        {
            "uri": t.string(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "body": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "httpMethod": t.string().optional(),
            "oauthToken": t.proxy(renames["OAuthTokenOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpTargetOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["ResumeJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeJobRequestIn"]
    )
    types["ResumeJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeJobRequestOut"])
    types["RunJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunJobRequestIn"]
    )
    types["RunJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunJobRequestOut"])
    types["RetryConfigIn"] = t.struct(
        {
            "maxRetryDuration": t.string().optional(),
            "maxBackoffDuration": t.string().optional(),
            "retryCount": t.integer().optional(),
            "maxDoublings": t.integer().optional(),
            "minBackoffDuration": t.string().optional(),
        }
    ).named(renames["RetryConfigIn"])
    types["RetryConfigOut"] = t.struct(
        {
            "maxRetryDuration": t.string().optional(),
            "maxBackoffDuration": t.string().optional(),
            "retryCount": t.integer().optional(),
            "maxDoublings": t.integer().optional(),
            "minBackoffDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryConfigOut"])
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
    types["PubsubTargetIn"] = t.struct(
        {
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "topicName": t.string(),
        }
    ).named(renames["PubsubTargetIn"])
    types["PubsubTargetOut"] = t.struct(
        {
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "topicName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubTargetOut"])
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
    types["JobIn"] = t.struct(
        {
            "pubsubTarget": t.proxy(renames["PubsubTargetIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "userUpdateTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "appEngineHttpTarget": t.proxy(renames["AppEngineHttpTargetIn"]).optional(),
            "timeZone": t.string().optional(),
            "lastAttemptTime": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "attemptDeadline": t.string().optional(),
            "httpTarget": t.proxy(renames["HttpTargetIn"]).optional(),
            "name": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
            "schedule": t.string(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "pubsubTarget": t.proxy(renames["PubsubTargetOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "userUpdateTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "appEngineHttpTarget": t.proxy(
                renames["AppEngineHttpTargetOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "lastAttemptTime": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "attemptDeadline": t.string().optional(),
            "httpTarget": t.proxy(renames["HttpTargetOut"]).optional(),
            "name": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigOut"]).optional(),
            "schedule": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["AppEngineHttpTargetIn"] = t.struct(
        {
            "relativeUri": t.string().optional(),
            "httpMethod": t.string().optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingIn"]).optional(),
            "body": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AppEngineHttpTargetIn"])
    types["AppEngineHttpTargetOut"] = t.struct(
        {
            "relativeUri": t.string().optional(),
            "httpMethod": t.string().optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingOut"]).optional(),
            "body": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineHttpTargetOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AppEngineRoutingIn"] = t.struct(
        {
            "instance": t.string().optional(),
            "host": t.string().optional(),
            "version": t.string().optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AppEngineRoutingIn"])
    types["AppEngineRoutingOut"] = t.struct(
        {
            "instance": t.string().optional(),
            "host": t.string().optional(),
            "version": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineRoutingOut"])
    types["PauseJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseJobRequestIn"]
    )
    types["PauseJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseJobRequestOut"])
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
    types["PubsubMessageIn"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "messageId": t.string().optional(),
            "publishTime": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "messageId": t.string().optional(),
            "publishTime": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])

    functions = {}
    functions["projectsLocationsList"] = cloudscheduler.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = cloudscheduler.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
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
        importer="cloudscheduler", renames=renames, types=types, functions=functions
    )
