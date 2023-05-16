from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudtasks() -> Import:
    cloudtasks = HTTPRuntime("https://cloudtasks.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudtasks_1_ErrorResponse",
        "StackdriverLoggingConfigIn": "_cloudtasks_2_StackdriverLoggingConfigIn",
        "StackdriverLoggingConfigOut": "_cloudtasks_3_StackdriverLoggingConfigOut",
        "AppEngineRoutingIn": "_cloudtasks_4_AppEngineRoutingIn",
        "AppEngineRoutingOut": "_cloudtasks_5_AppEngineRoutingOut",
        "ListTasksResponseIn": "_cloudtasks_6_ListTasksResponseIn",
        "ListTasksResponseOut": "_cloudtasks_7_ListTasksResponseOut",
        "ListLocationsResponseIn": "_cloudtasks_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudtasks_9_ListLocationsResponseOut",
        "RetryConfigIn": "_cloudtasks_10_RetryConfigIn",
        "RetryConfigOut": "_cloudtasks_11_RetryConfigOut",
        "RateLimitsIn": "_cloudtasks_12_RateLimitsIn",
        "RateLimitsOut": "_cloudtasks_13_RateLimitsOut",
        "PurgeQueueRequestIn": "_cloudtasks_14_PurgeQueueRequestIn",
        "PurgeQueueRequestOut": "_cloudtasks_15_PurgeQueueRequestOut",
        "PolicyIn": "_cloudtasks_16_PolicyIn",
        "PolicyOut": "_cloudtasks_17_PolicyOut",
        "LocationIn": "_cloudtasks_18_LocationIn",
        "LocationOut": "_cloudtasks_19_LocationOut",
        "AppEngineHttpRequestIn": "_cloudtasks_20_AppEngineHttpRequestIn",
        "AppEngineHttpRequestOut": "_cloudtasks_21_AppEngineHttpRequestOut",
        "QueueIn": "_cloudtasks_22_QueueIn",
        "QueueOut": "_cloudtasks_23_QueueOut",
        "HttpRequestIn": "_cloudtasks_24_HttpRequestIn",
        "HttpRequestOut": "_cloudtasks_25_HttpRequestOut",
        "ExprIn": "_cloudtasks_26_ExprIn",
        "ExprOut": "_cloudtasks_27_ExprOut",
        "OidcTokenIn": "_cloudtasks_28_OidcTokenIn",
        "OidcTokenOut": "_cloudtasks_29_OidcTokenOut",
        "EmptyIn": "_cloudtasks_30_EmptyIn",
        "EmptyOut": "_cloudtasks_31_EmptyOut",
        "TestIamPermissionsRequestIn": "_cloudtasks_32_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudtasks_33_TestIamPermissionsRequestOut",
        "PauseQueueRequestIn": "_cloudtasks_34_PauseQueueRequestIn",
        "PauseQueueRequestOut": "_cloudtasks_35_PauseQueueRequestOut",
        "TaskIn": "_cloudtasks_36_TaskIn",
        "TaskOut": "_cloudtasks_37_TaskOut",
        "BindingIn": "_cloudtasks_38_BindingIn",
        "BindingOut": "_cloudtasks_39_BindingOut",
        "GetIamPolicyRequestIn": "_cloudtasks_40_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_cloudtasks_41_GetIamPolicyRequestOut",
        "GetPolicyOptionsIn": "_cloudtasks_42_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_cloudtasks_43_GetPolicyOptionsOut",
        "CreateTaskRequestIn": "_cloudtasks_44_CreateTaskRequestIn",
        "CreateTaskRequestOut": "_cloudtasks_45_CreateTaskRequestOut",
        "OAuthTokenIn": "_cloudtasks_46_OAuthTokenIn",
        "OAuthTokenOut": "_cloudtasks_47_OAuthTokenOut",
        "SetIamPolicyRequestIn": "_cloudtasks_48_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudtasks_49_SetIamPolicyRequestOut",
        "TestIamPermissionsResponseIn": "_cloudtasks_50_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudtasks_51_TestIamPermissionsResponseOut",
        "AttemptIn": "_cloudtasks_52_AttemptIn",
        "AttemptOut": "_cloudtasks_53_AttemptOut",
        "ResumeQueueRequestIn": "_cloudtasks_54_ResumeQueueRequestIn",
        "ResumeQueueRequestOut": "_cloudtasks_55_ResumeQueueRequestOut",
        "RunTaskRequestIn": "_cloudtasks_56_RunTaskRequestIn",
        "RunTaskRequestOut": "_cloudtasks_57_RunTaskRequestOut",
        "StatusIn": "_cloudtasks_58_StatusIn",
        "StatusOut": "_cloudtasks_59_StatusOut",
        "ListQueuesResponseIn": "_cloudtasks_60_ListQueuesResponseIn",
        "ListQueuesResponseOut": "_cloudtasks_61_ListQueuesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StackdriverLoggingConfigIn"] = t.struct(
        {"samplingRatio": t.number().optional()}
    ).named(renames["StackdriverLoggingConfigIn"])
    types["StackdriverLoggingConfigOut"] = t.struct(
        {
            "samplingRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackdriverLoggingConfigOut"])
    types["AppEngineRoutingIn"] = t.struct(
        {
            "version": t.string().optional(),
            "host": t.string().optional(),
            "instance": t.string().optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AppEngineRoutingIn"])
    types["AppEngineRoutingOut"] = t.struct(
        {
            "version": t.string().optional(),
            "host": t.string().optional(),
            "instance": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineRoutingOut"])
    types["ListTasksResponseIn"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["TaskIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTasksResponseIn"])
    types["ListTasksResponseOut"] = t.struct(
        {
            "tasks": t.array(t.proxy(renames["TaskOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTasksResponseOut"])
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
    types["RetryConfigIn"] = t.struct(
        {
            "maxRetryDuration": t.string().optional(),
            "maxBackoff": t.string().optional(),
            "maxDoublings": t.integer().optional(),
            "minBackoff": t.string().optional(),
            "maxAttempts": t.integer().optional(),
        }
    ).named(renames["RetryConfigIn"])
    types["RetryConfigOut"] = t.struct(
        {
            "maxRetryDuration": t.string().optional(),
            "maxBackoff": t.string().optional(),
            "maxDoublings": t.integer().optional(),
            "minBackoff": t.string().optional(),
            "maxAttempts": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryConfigOut"])
    types["RateLimitsIn"] = t.struct(
        {
            "maxBurstSize": t.integer().optional(),
            "maxConcurrentDispatches": t.integer().optional(),
            "maxDispatchesPerSecond": t.number().optional(),
        }
    ).named(renames["RateLimitsIn"])
    types["RateLimitsOut"] = t.struct(
        {
            "maxBurstSize": t.integer().optional(),
            "maxConcurrentDispatches": t.integer().optional(),
            "maxDispatchesPerSecond": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateLimitsOut"])
    types["PurgeQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PurgeQueueRequestIn"]
    )
    types["PurgeQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PurgeQueueRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AppEngineHttpRequestIn"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingIn"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "relativeUri": t.string().optional(),
        }
    ).named(renames["AppEngineHttpRequestIn"])
    types["AppEngineHttpRequestOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingOut"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "relativeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineHttpRequestOut"])
    types["QueueIn"] = t.struct(
        {
            "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
            "stackdriverLoggingConfig": t.proxy(
                renames["StackdriverLoggingConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "purgeTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
            "appEngineRoutingOverride": t.proxy(
                renames["AppEngineRoutingIn"]
            ).optional(),
        }
    ).named(renames["QueueIn"])
    types["QueueOut"] = t.struct(
        {
            "rateLimits": t.proxy(renames["RateLimitsOut"]).optional(),
            "stackdriverLoggingConfig": t.proxy(
                renames["StackdriverLoggingConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "purgeTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigOut"]).optional(),
            "appEngineRoutingOverride": t.proxy(
                renames["AppEngineRoutingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueueOut"])
    types["HttpRequestIn"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "url": t.string(),
            "oauthToken": t.proxy(renames["OAuthTokenIn"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
        }
    ).named(renames["HttpRequestIn"])
    types["HttpRequestOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "url": t.string(),
            "oauthToken": t.proxy(renames["OAuthTokenOut"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["PauseQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseQueueRequestIn"]
    )
    types["PauseQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseQueueRequestOut"])
    types["TaskIn"] = t.struct(
        {
            "dispatchDeadline": t.string().optional(),
            "dispatchCount": t.integer().optional(),
            "appEngineHttpRequest": t.proxy(
                renames["AppEngineHttpRequestIn"]
            ).optional(),
            "view": t.string().optional(),
            "responseCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestIn"]).optional(),
            "name": t.string().optional(),
            "firstAttempt": t.proxy(renames["AttemptIn"]).optional(),
            "scheduleTime": t.string().optional(),
            "lastAttempt": t.proxy(renames["AttemptIn"]).optional(),
        }
    ).named(renames["TaskIn"])
    types["TaskOut"] = t.struct(
        {
            "dispatchDeadline": t.string().optional(),
            "dispatchCount": t.integer().optional(),
            "appEngineHttpRequest": t.proxy(
                renames["AppEngineHttpRequestOut"]
            ).optional(),
            "view": t.string().optional(),
            "responseCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "httpRequest": t.proxy(renames["HttpRequestOut"]).optional(),
            "name": t.string().optional(),
            "firstAttempt": t.proxy(renames["AttemptOut"]).optional(),
            "scheduleTime": t.string().optional(),
            "lastAttempt": t.proxy(renames["AttemptOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["CreateTaskRequestIn"] = t.struct(
        {"task": t.proxy(renames["TaskIn"]), "responseView": t.string().optional()}
    ).named(renames["CreateTaskRequestIn"])
    types["CreateTaskRequestOut"] = t.struct(
        {
            "task": t.proxy(renames["TaskOut"]),
            "responseView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTaskRequestOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["AttemptIn"] = t.struct(
        {
            "responseStatus": t.proxy(renames["StatusIn"]).optional(),
            "scheduleTime": t.string().optional(),
            "dispatchTime": t.string().optional(),
            "responseTime": t.string().optional(),
        }
    ).named(renames["AttemptIn"])
    types["AttemptOut"] = t.struct(
        {
            "responseStatus": t.proxy(renames["StatusOut"]).optional(),
            "scheduleTime": t.string().optional(),
            "dispatchTime": t.string().optional(),
            "responseTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttemptOut"])
    types["ResumeQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeQueueRequestIn"]
    )
    types["ResumeQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeQueueRequestOut"])
    types["RunTaskRequestIn"] = t.struct({"responseView": t.string().optional()}).named(
        renames["RunTaskRequestIn"]
    )
    types["RunTaskRequestOut"] = t.struct(
        {
            "responseView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunTaskRequestOut"])
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
    types["ListQueuesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "queues": t.array(t.proxy(renames["QueueIn"])).optional(),
        }
    ).named(renames["ListQueuesResponseIn"])
    types["ListQueuesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "queues": t.array(t.proxy(renames["QueueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQueuesResponseOut"])

    functions = {}
    functions["projectsLocationsList"] = cloudtasks.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = cloudtasks.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesList"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTestIamPermissions"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesGetIamPolicy"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesSetIamPolicy"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesCreate"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPause"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesDelete"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesResume"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPurge"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesGet"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPatch"] = cloudtasks.patch(
        "v2/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
                "stackdriverLoggingConfig": t.proxy(
                    renames["StackdriverLoggingConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "purgeTime": t.string().optional(),
                "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
                "appEngineRoutingOverride": t.proxy(
                    renames["AppEngineRoutingIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QueueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksGet"] = cloudtasks.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "responseView": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksRun"] = cloudtasks.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "responseView": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksCreate"] = cloudtasks.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "responseView": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksDelete"] = cloudtasks.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "responseView": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksList"] = cloudtasks.get(
        "v2/{parent}/tasks",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "responseView": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTasksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudtasks",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
