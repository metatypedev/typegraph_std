from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudtasks() -> Import:
    cloudtasks = HTTPRuntime("https://cloudtasks.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudtasks_1_ErrorResponse",
        "ListLocationsResponseIn": "_cloudtasks_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudtasks_3_ListLocationsResponseOut",
        "LocationIn": "_cloudtasks_4_LocationIn",
        "LocationOut": "_cloudtasks_5_LocationOut",
        "ListQueuesResponseIn": "_cloudtasks_6_ListQueuesResponseIn",
        "ListQueuesResponseOut": "_cloudtasks_7_ListQueuesResponseOut",
        "QueueIn": "_cloudtasks_8_QueueIn",
        "QueueOut": "_cloudtasks_9_QueueOut",
        "AppEngineRoutingIn": "_cloudtasks_10_AppEngineRoutingIn",
        "AppEngineRoutingOut": "_cloudtasks_11_AppEngineRoutingOut",
        "RateLimitsIn": "_cloudtasks_12_RateLimitsIn",
        "RateLimitsOut": "_cloudtasks_13_RateLimitsOut",
        "RetryConfigIn": "_cloudtasks_14_RetryConfigIn",
        "RetryConfigOut": "_cloudtasks_15_RetryConfigOut",
        "StackdriverLoggingConfigIn": "_cloudtasks_16_StackdriverLoggingConfigIn",
        "StackdriverLoggingConfigOut": "_cloudtasks_17_StackdriverLoggingConfigOut",
        "EmptyIn": "_cloudtasks_18_EmptyIn",
        "EmptyOut": "_cloudtasks_19_EmptyOut",
        "PurgeQueueRequestIn": "_cloudtasks_20_PurgeQueueRequestIn",
        "PurgeQueueRequestOut": "_cloudtasks_21_PurgeQueueRequestOut",
        "PauseQueueRequestIn": "_cloudtasks_22_PauseQueueRequestIn",
        "PauseQueueRequestOut": "_cloudtasks_23_PauseQueueRequestOut",
        "ResumeQueueRequestIn": "_cloudtasks_24_ResumeQueueRequestIn",
        "ResumeQueueRequestOut": "_cloudtasks_25_ResumeQueueRequestOut",
        "GetIamPolicyRequestIn": "_cloudtasks_26_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_cloudtasks_27_GetIamPolicyRequestOut",
        "GetPolicyOptionsIn": "_cloudtasks_28_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_cloudtasks_29_GetPolicyOptionsOut",
        "PolicyIn": "_cloudtasks_30_PolicyIn",
        "PolicyOut": "_cloudtasks_31_PolicyOut",
        "BindingIn": "_cloudtasks_32_BindingIn",
        "BindingOut": "_cloudtasks_33_BindingOut",
        "ExprIn": "_cloudtasks_34_ExprIn",
        "ExprOut": "_cloudtasks_35_ExprOut",
        "SetIamPolicyRequestIn": "_cloudtasks_36_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudtasks_37_SetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_cloudtasks_38_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudtasks_39_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_cloudtasks_40_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudtasks_41_TestIamPermissionsResponseOut",
        "ListTasksResponseIn": "_cloudtasks_42_ListTasksResponseIn",
        "ListTasksResponseOut": "_cloudtasks_43_ListTasksResponseOut",
        "TaskIn": "_cloudtasks_44_TaskIn",
        "TaskOut": "_cloudtasks_45_TaskOut",
        "AppEngineHttpRequestIn": "_cloudtasks_46_AppEngineHttpRequestIn",
        "AppEngineHttpRequestOut": "_cloudtasks_47_AppEngineHttpRequestOut",
        "HttpRequestIn": "_cloudtasks_48_HttpRequestIn",
        "HttpRequestOut": "_cloudtasks_49_HttpRequestOut",
        "OAuthTokenIn": "_cloudtasks_50_OAuthTokenIn",
        "OAuthTokenOut": "_cloudtasks_51_OAuthTokenOut",
        "OidcTokenIn": "_cloudtasks_52_OidcTokenIn",
        "OidcTokenOut": "_cloudtasks_53_OidcTokenOut",
        "AttemptIn": "_cloudtasks_54_AttemptIn",
        "AttemptOut": "_cloudtasks_55_AttemptOut",
        "StatusIn": "_cloudtasks_56_StatusIn",
        "StatusOut": "_cloudtasks_57_StatusOut",
        "CreateTaskRequestIn": "_cloudtasks_58_CreateTaskRequestIn",
        "CreateTaskRequestOut": "_cloudtasks_59_CreateTaskRequestOut",
        "RunTaskRequestIn": "_cloudtasks_60_RunTaskRequestIn",
        "RunTaskRequestOut": "_cloudtasks_61_RunTaskRequestOut",
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListQueuesResponseIn"] = t.struct(
        {
            "queues": t.array(t.proxy(renames["QueueIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListQueuesResponseIn"])
    types["ListQueuesResponseOut"] = t.struct(
        {
            "queues": t.array(t.proxy(renames["QueueOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQueuesResponseOut"])
    types["QueueIn"] = t.struct(
        {
            "name": t.string().optional(),
            "appEngineRoutingOverride": t.proxy(
                renames["AppEngineRoutingIn"]
            ).optional(),
            "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
            "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
            "state": t.string().optional(),
            "purgeTime": t.string().optional(),
            "stackdriverLoggingConfig": t.proxy(
                renames["StackdriverLoggingConfigIn"]
            ).optional(),
        }
    ).named(renames["QueueIn"])
    types["QueueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "appEngineRoutingOverride": t.proxy(
                renames["AppEngineRoutingOut"]
            ).optional(),
            "rateLimits": t.proxy(renames["RateLimitsOut"]).optional(),
            "retryConfig": t.proxy(renames["RetryConfigOut"]).optional(),
            "state": t.string().optional(),
            "purgeTime": t.string().optional(),
            "stackdriverLoggingConfig": t.proxy(
                renames["StackdriverLoggingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueueOut"])
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
    types["RateLimitsIn"] = t.struct(
        {
            "maxDispatchesPerSecond": t.number().optional(),
            "maxBurstSize": t.integer().optional(),
            "maxConcurrentDispatches": t.integer().optional(),
        }
    ).named(renames["RateLimitsIn"])
    types["RateLimitsOut"] = t.struct(
        {
            "maxDispatchesPerSecond": t.number().optional(),
            "maxBurstSize": t.integer().optional(),
            "maxConcurrentDispatches": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateLimitsOut"])
    types["RetryConfigIn"] = t.struct(
        {
            "maxAttempts": t.integer().optional(),
            "maxRetryDuration": t.string().optional(),
            "minBackoff": t.string().optional(),
            "maxBackoff": t.string().optional(),
            "maxDoublings": t.integer().optional(),
        }
    ).named(renames["RetryConfigIn"])
    types["RetryConfigOut"] = t.struct(
        {
            "maxAttempts": t.integer().optional(),
            "maxRetryDuration": t.string().optional(),
            "minBackoff": t.string().optional(),
            "maxBackoff": t.string().optional(),
            "maxDoublings": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryConfigOut"])
    types["StackdriverLoggingConfigIn"] = t.struct(
        {"samplingRatio": t.number().optional()}
    ).named(renames["StackdriverLoggingConfigIn"])
    types["StackdriverLoggingConfigOut"] = t.struct(
        {
            "samplingRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackdriverLoggingConfigOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PurgeQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PurgeQueueRequestIn"]
    )
    types["PurgeQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PurgeQueueRequestOut"])
    types["PauseQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseQueueRequestIn"]
    )
    types["PauseQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseQueueRequestOut"])
    types["ResumeQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeQueueRequestIn"]
    )
    types["ResumeQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeQueueRequestOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["TaskIn"] = t.struct(
        {
            "name": t.string().optional(),
            "appEngineHttpRequest": t.proxy(
                renames["AppEngineHttpRequestIn"]
            ).optional(),
            "httpRequest": t.proxy(renames["HttpRequestIn"]).optional(),
            "scheduleTime": t.string().optional(),
            "createTime": t.string().optional(),
            "dispatchDeadline": t.string().optional(),
            "dispatchCount": t.integer().optional(),
            "responseCount": t.integer().optional(),
            "firstAttempt": t.proxy(renames["AttemptIn"]).optional(),
            "lastAttempt": t.proxy(renames["AttemptIn"]).optional(),
            "view": t.string().optional(),
        }
    ).named(renames["TaskIn"])
    types["TaskOut"] = t.struct(
        {
            "name": t.string().optional(),
            "appEngineHttpRequest": t.proxy(
                renames["AppEngineHttpRequestOut"]
            ).optional(),
            "httpRequest": t.proxy(renames["HttpRequestOut"]).optional(),
            "scheduleTime": t.string().optional(),
            "createTime": t.string().optional(),
            "dispatchDeadline": t.string().optional(),
            "dispatchCount": t.integer().optional(),
            "responseCount": t.integer().optional(),
            "firstAttempt": t.proxy(renames["AttemptOut"]).optional(),
            "lastAttempt": t.proxy(renames["AttemptOut"]).optional(),
            "view": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskOut"])
    types["AppEngineHttpRequestIn"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingIn"]).optional(),
            "relativeUri": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "body": t.string().optional(),
        }
    ).named(renames["AppEngineHttpRequestIn"])
    types["AppEngineHttpRequestOut"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingOut"]).optional(),
            "relativeUri": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "body": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineHttpRequestOut"])
    types["HttpRequestIn"] = t.struct(
        {
            "url": t.string(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "body": t.string().optional(),
            "oauthToken": t.proxy(renames["OAuthTokenIn"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
        }
    ).named(renames["HttpRequestIn"])
    types["HttpRequestOut"] = t.struct(
        {
            "url": t.string(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "body": t.string().optional(),
            "oauthToken": t.proxy(renames["OAuthTokenOut"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestOut"])
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
    types["AttemptIn"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "dispatchTime": t.string().optional(),
            "responseTime": t.string().optional(),
            "responseStatus": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["AttemptIn"])
    types["AttemptOut"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "dispatchTime": t.string().optional(),
            "responseTime": t.string().optional(),
            "responseStatus": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttemptOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["RunTaskRequestIn"] = t.struct({"responseView": t.string().optional()}).named(
        renames["RunTaskRequestIn"]
    )
    types["RunTaskRequestOut"] = t.struct(
        {
            "responseView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunTaskRequestOut"])

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
    functions["projectsLocationsQueuesList"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesGet"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesCreate"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPatch"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesDelete"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPurge"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPause"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesResume"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesGetIamPolicy"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesSetIamPolicy"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTestIamPermissions"] = cloudtasks.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksList"] = cloudtasks.post(
        "v2/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "responseView": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksGet"] = cloudtasks.post(
        "v2/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "responseView": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksCreate"] = cloudtasks.post(
        "v2/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "responseView": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksDelete"] = cloudtasks.post(
        "v2/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "responseView": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksRun"] = cloudtasks.post(
        "v2/{name}:run",
        t.struct(
            {
                "name": t.string(),
                "responseView": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudtasks",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
