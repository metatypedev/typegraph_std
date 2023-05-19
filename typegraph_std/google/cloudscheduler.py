from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudscheduler() -> Import:
    cloudscheduler = HTTPRuntime("https://cloudscheduler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudscheduler_1_ErrorResponse",
        "OAuthTokenIn": "_cloudscheduler_2_OAuthTokenIn",
        "OAuthTokenOut": "_cloudscheduler_3_OAuthTokenOut",
        "ListLocationsResponseIn": "_cloudscheduler_4_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudscheduler_5_ListLocationsResponseOut",
        "RunJobRequestIn": "_cloudscheduler_6_RunJobRequestIn",
        "RunJobRequestOut": "_cloudscheduler_7_RunJobRequestOut",
        "ListJobsResponseIn": "_cloudscheduler_8_ListJobsResponseIn",
        "ListJobsResponseOut": "_cloudscheduler_9_ListJobsResponseOut",
        "AppEngineHttpTargetIn": "_cloudscheduler_10_AppEngineHttpTargetIn",
        "AppEngineHttpTargetOut": "_cloudscheduler_11_AppEngineHttpTargetOut",
        "HttpTargetIn": "_cloudscheduler_12_HttpTargetIn",
        "HttpTargetOut": "_cloudscheduler_13_HttpTargetOut",
        "JobIn": "_cloudscheduler_14_JobIn",
        "JobOut": "_cloudscheduler_15_JobOut",
        "PubsubTargetIn": "_cloudscheduler_16_PubsubTargetIn",
        "PubsubTargetOut": "_cloudscheduler_17_PubsubTargetOut",
        "AppEngineRoutingIn": "_cloudscheduler_18_AppEngineRoutingIn",
        "AppEngineRoutingOut": "_cloudscheduler_19_AppEngineRoutingOut",
        "RetryConfigIn": "_cloudscheduler_20_RetryConfigIn",
        "RetryConfigOut": "_cloudscheduler_21_RetryConfigOut",
        "OidcTokenIn": "_cloudscheduler_22_OidcTokenIn",
        "OidcTokenOut": "_cloudscheduler_23_OidcTokenOut",
        "StatusIn": "_cloudscheduler_24_StatusIn",
        "StatusOut": "_cloudscheduler_25_StatusOut",
        "LocationIn": "_cloudscheduler_26_LocationIn",
        "LocationOut": "_cloudscheduler_27_LocationOut",
        "EmptyIn": "_cloudscheduler_28_EmptyIn",
        "EmptyOut": "_cloudscheduler_29_EmptyOut",
        "PauseJobRequestIn": "_cloudscheduler_30_PauseJobRequestIn",
        "PauseJobRequestOut": "_cloudscheduler_31_PauseJobRequestOut",
        "ResumeJobRequestIn": "_cloudscheduler_32_ResumeJobRequestIn",
        "ResumeJobRequestOut": "_cloudscheduler_33_ResumeJobRequestOut",
        "PubsubMessageIn": "_cloudscheduler_34_PubsubMessageIn",
        "PubsubMessageOut": "_cloudscheduler_35_PubsubMessageOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OAuthTokenIn"] = t.struct(
        {"serviceAccountEmail": t.string().optional(), "scope": t.string().optional()}
    ).named(renames["OAuthTokenIn"])
    types["OAuthTokenOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthTokenOut"])
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
    types["RunJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RunJobRequestIn"]
    )
    types["RunJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RunJobRequestOut"])
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
    types["AppEngineHttpTargetIn"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingIn"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "relativeUri": t.string().optional(),
        }
    ).named(renames["AppEngineHttpTargetIn"])
    types["AppEngineHttpTargetOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingOut"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "relativeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineHttpTargetOut"])
    types["HttpTargetIn"] = t.struct(
        {
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "uri": t.string(),
            "oauthToken": t.proxy(renames["OAuthTokenIn"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HttpTargetIn"])
    types["HttpTargetOut"] = t.struct(
        {
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "uri": t.string(),
            "oauthToken": t.proxy(renames["OAuthTokenOut"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpTargetOut"])
    types["JobIn"] = t.struct(
        {
            "appEngineHttpTarget": t.proxy(renames["AppEngineHttpTargetIn"]).optional(),
            "lastAttemptTime": t.string().optional(),
            "pubsubTarget": t.proxy(renames["PubsubTargetIn"]).optional(),
            "userUpdateTime": t.string().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "httpTarget": t.proxy(renames["HttpTargetIn"]).optional(),
            "description": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
            "timeZone": t.string().optional(),
            "attemptDeadline": t.string().optional(),
            "schedule": t.string(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "appEngineHttpTarget": t.proxy(
                renames["AppEngineHttpTargetOut"]
            ).optional(),
            "lastAttemptTime": t.string().optional(),
            "pubsubTarget": t.proxy(renames["PubsubTargetOut"]).optional(),
            "userUpdateTime": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "httpTarget": t.proxy(renames["HttpTargetOut"]).optional(),
            "description": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigOut"]).optional(),
            "timeZone": t.string().optional(),
            "attemptDeadline": t.string().optional(),
            "schedule": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["PubsubTargetIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "topicName": t.string(),
            "data": t.string().optional(),
        }
    ).named(renames["PubsubTargetIn"])
    types["PubsubTargetOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "topicName": t.string(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubTargetOut"])
    types["AppEngineRoutingIn"] = t.struct(
        {
            "host": t.string().optional(),
            "service": t.string().optional(),
            "instance": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["AppEngineRoutingIn"])
    types["AppEngineRoutingOut"] = t.struct(
        {
            "host": t.string().optional(),
            "service": t.string().optional(),
            "instance": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineRoutingOut"])
    types["RetryConfigIn"] = t.struct(
        {
            "maxBackoffDuration": t.string().optional(),
            "maxRetryDuration": t.string().optional(),
            "minBackoffDuration": t.string().optional(),
            "maxDoublings": t.integer().optional(),
            "retryCount": t.integer().optional(),
        }
    ).named(renames["RetryConfigIn"])
    types["RetryConfigOut"] = t.struct(
        {
            "maxBackoffDuration": t.string().optional(),
            "maxRetryDuration": t.string().optional(),
            "minBackoffDuration": t.string().optional(),
            "maxDoublings": t.integer().optional(),
            "retryCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryConfigOut"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PauseJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseJobRequestIn"]
    )
    types["PauseJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseJobRequestOut"])
    types["ResumeJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeJobRequestIn"]
    )
    types["ResumeJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeJobRequestOut"])
    types["PubsubMessageIn"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "orderingKey": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "orderingKey": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])

    functions = {}
    functions["projectsLocationsGet"] = cloudscheduler.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPause"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsList"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsRun"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsPatch"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsResume"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsCreate"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsGet"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobsDelete"] = cloudscheduler.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudscheduler",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
