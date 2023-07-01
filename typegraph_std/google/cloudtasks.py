from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudtasks():
    cloudtasks = HTTPRuntime("https://cloudtasks.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudtasks_1_ErrorResponse",
        "StackdriverLoggingConfigIn": "_cloudtasks_2_StackdriverLoggingConfigIn",
        "StackdriverLoggingConfigOut": "_cloudtasks_3_StackdriverLoggingConfigOut",
        "HttpRequestIn": "_cloudtasks_4_HttpRequestIn",
        "HttpRequestOut": "_cloudtasks_5_HttpRequestOut",
        "GetIamPolicyRequestIn": "_cloudtasks_6_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_cloudtasks_7_GetIamPolicyRequestOut",
        "OidcTokenIn": "_cloudtasks_8_OidcTokenIn",
        "OidcTokenOut": "_cloudtasks_9_OidcTokenOut",
        "PauseQueueRequestIn": "_cloudtasks_10_PauseQueueRequestIn",
        "PauseQueueRequestOut": "_cloudtasks_11_PauseQueueRequestOut",
        "ExprIn": "_cloudtasks_12_ExprIn",
        "ExprOut": "_cloudtasks_13_ExprOut",
        "ResumeQueueRequestIn": "_cloudtasks_14_ResumeQueueRequestIn",
        "ResumeQueueRequestOut": "_cloudtasks_15_ResumeQueueRequestOut",
        "EmptyIn": "_cloudtasks_16_EmptyIn",
        "EmptyOut": "_cloudtasks_17_EmptyOut",
        "PolicyIn": "_cloudtasks_18_PolicyIn",
        "PolicyOut": "_cloudtasks_19_PolicyOut",
        "ListTasksResponseIn": "_cloudtasks_20_ListTasksResponseIn",
        "ListTasksResponseOut": "_cloudtasks_21_ListTasksResponseOut",
        "RetryConfigIn": "_cloudtasks_22_RetryConfigIn",
        "RetryConfigOut": "_cloudtasks_23_RetryConfigOut",
        "QueueIn": "_cloudtasks_24_QueueIn",
        "QueueOut": "_cloudtasks_25_QueueOut",
        "PurgeQueueRequestIn": "_cloudtasks_26_PurgeQueueRequestIn",
        "PurgeQueueRequestOut": "_cloudtasks_27_PurgeQueueRequestOut",
        "TaskIn": "_cloudtasks_28_TaskIn",
        "TaskOut": "_cloudtasks_29_TaskOut",
        "ListQueuesResponseIn": "_cloudtasks_30_ListQueuesResponseIn",
        "ListQueuesResponseOut": "_cloudtasks_31_ListQueuesResponseOut",
        "OAuthTokenIn": "_cloudtasks_32_OAuthTokenIn",
        "OAuthTokenOut": "_cloudtasks_33_OAuthTokenOut",
        "BindingIn": "_cloudtasks_34_BindingIn",
        "BindingOut": "_cloudtasks_35_BindingOut",
        "TestIamPermissionsRequestIn": "_cloudtasks_36_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudtasks_37_TestIamPermissionsRequestOut",
        "RateLimitsIn": "_cloudtasks_38_RateLimitsIn",
        "RateLimitsOut": "_cloudtasks_39_RateLimitsOut",
        "GetPolicyOptionsIn": "_cloudtasks_40_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_cloudtasks_41_GetPolicyOptionsOut",
        "SetIamPolicyRequestIn": "_cloudtasks_42_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudtasks_43_SetIamPolicyRequestOut",
        "RunTaskRequestIn": "_cloudtasks_44_RunTaskRequestIn",
        "RunTaskRequestOut": "_cloudtasks_45_RunTaskRequestOut",
        "ListLocationsResponseIn": "_cloudtasks_46_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudtasks_47_ListLocationsResponseOut",
        "TestIamPermissionsResponseIn": "_cloudtasks_48_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudtasks_49_TestIamPermissionsResponseOut",
        "AppEngineRoutingIn": "_cloudtasks_50_AppEngineRoutingIn",
        "AppEngineRoutingOut": "_cloudtasks_51_AppEngineRoutingOut",
        "AttemptIn": "_cloudtasks_52_AttemptIn",
        "AttemptOut": "_cloudtasks_53_AttemptOut",
        "StatusIn": "_cloudtasks_54_StatusIn",
        "StatusOut": "_cloudtasks_55_StatusOut",
        "CreateTaskRequestIn": "_cloudtasks_56_CreateTaskRequestIn",
        "CreateTaskRequestOut": "_cloudtasks_57_CreateTaskRequestOut",
        "AppEngineHttpRequestIn": "_cloudtasks_58_AppEngineHttpRequestIn",
        "AppEngineHttpRequestOut": "_cloudtasks_59_AppEngineHttpRequestOut",
        "LocationIn": "_cloudtasks_60_LocationIn",
        "LocationOut": "_cloudtasks_61_LocationOut",
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
    types["HttpRequestIn"] = t.struct(
        {
            "oauthToken": t.proxy(renames["OAuthTokenIn"]).optional(),
            "body": t.string().optional(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "url": t.string(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HttpRequestIn"])
    types["HttpRequestOut"] = t.struct(
        {
            "oauthToken": t.proxy(renames["OAuthTokenOut"]).optional(),
            "body": t.string().optional(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "url": t.string(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRequestOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
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
    types["PauseQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseQueueRequestIn"]
    )
    types["PauseQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseQueueRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ResumeQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeQueueRequestIn"]
    )
    types["ResumeQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeQueueRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["RetryConfigIn"] = t.struct(
        {
            "maxRetryDuration": t.string().optional(),
            "minBackoff": t.string().optional(),
            "maxAttempts": t.integer().optional(),
            "maxDoublings": t.integer().optional(),
            "maxBackoff": t.string().optional(),
        }
    ).named(renames["RetryConfigIn"])
    types["RetryConfigOut"] = t.struct(
        {
            "maxRetryDuration": t.string().optional(),
            "minBackoff": t.string().optional(),
            "maxAttempts": t.integer().optional(),
            "maxDoublings": t.integer().optional(),
            "maxBackoff": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryConfigOut"])
    types["QueueIn"] = t.struct(
        {
            "appEngineRoutingOverride": t.proxy(
                renames["AppEngineRoutingIn"]
            ).optional(),
            "stackdriverLoggingConfig": t.proxy(
                renames["StackdriverLoggingConfigIn"]
            ).optional(),
            "purgeTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigIn"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "rateLimits": t.proxy(renames["RateLimitsIn"]).optional(),
        }
    ).named(renames["QueueIn"])
    types["QueueOut"] = t.struct(
        {
            "appEngineRoutingOverride": t.proxy(
                renames["AppEngineRoutingOut"]
            ).optional(),
            "stackdriverLoggingConfig": t.proxy(
                renames["StackdriverLoggingConfigOut"]
            ).optional(),
            "purgeTime": t.string().optional(),
            "retryConfig": t.proxy(renames["RetryConfigOut"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "rateLimits": t.proxy(renames["RateLimitsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueueOut"])
    types["PurgeQueueRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PurgeQueueRequestIn"]
    )
    types["PurgeQueueRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PurgeQueueRequestOut"])
    types["TaskIn"] = t.struct(
        {
            "lastAttempt": t.proxy(renames["AttemptIn"]).optional(),
            "dispatchCount": t.integer().optional(),
            "view": t.string().optional(),
            "name": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "appEngineHttpRequest": t.proxy(
                renames["AppEngineHttpRequestIn"]
            ).optional(),
            "dispatchDeadline": t.string().optional(),
            "firstAttempt": t.proxy(renames["AttemptIn"]).optional(),
            "responseCount": t.integer().optional(),
            "httpRequest": t.proxy(renames["HttpRequestIn"]).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["TaskIn"])
    types["TaskOut"] = t.struct(
        {
            "lastAttempt": t.proxy(renames["AttemptOut"]).optional(),
            "dispatchCount": t.integer().optional(),
            "view": t.string().optional(),
            "name": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "appEngineHttpRequest": t.proxy(
                renames["AppEngineHttpRequestOut"]
            ).optional(),
            "dispatchDeadline": t.string().optional(),
            "firstAttempt": t.proxy(renames["AttemptOut"]).optional(),
            "responseCount": t.integer().optional(),
            "httpRequest": t.proxy(renames["HttpRequestOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["RateLimitsIn"] = t.struct(
        {
            "maxDispatchesPerSecond": t.number().optional(),
            "maxConcurrentDispatches": t.integer().optional(),
            "maxBurstSize": t.integer().optional(),
        }
    ).named(renames["RateLimitsIn"])
    types["RateLimitsOut"] = t.struct(
        {
            "maxDispatchesPerSecond": t.number().optional(),
            "maxConcurrentDispatches": t.integer().optional(),
            "maxBurstSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RateLimitsOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["RunTaskRequestIn"] = t.struct({"responseView": t.string().optional()}).named(
        renames["RunTaskRequestIn"]
    )
    types["RunTaskRequestOut"] = t.struct(
        {
            "responseView": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunTaskRequestOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["AppEngineRoutingIn"] = t.struct(
        {
            "host": t.string().optional(),
            "instance": t.string().optional(),
            "service": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["AppEngineRoutingIn"])
    types["AppEngineRoutingOut"] = t.struct(
        {
            "host": t.string().optional(),
            "instance": t.string().optional(),
            "service": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineRoutingOut"])
    types["AttemptIn"] = t.struct(
        {
            "dispatchTime": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "responseStatus": t.proxy(renames["StatusIn"]).optional(),
            "responseTime": t.string().optional(),
        }
    ).named(renames["AttemptIn"])
    types["AttemptOut"] = t.struct(
        {
            "dispatchTime": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "responseStatus": t.proxy(renames["StatusOut"]).optional(),
            "responseTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttemptOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
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
    types["AppEngineHttpRequestIn"] = t.struct(
        {
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingIn"]).optional(),
            "relativeUri": t.string().optional(),
        }
    ).named(renames["AppEngineHttpRequestIn"])
    types["AppEngineHttpRequestOut"] = t.struct(
        {
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "appEngineRouting": t.proxy(renames["AppEngineRoutingOut"]).optional(),
            "relativeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppEngineHttpRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])

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
    functions["projectsLocationsQueuesSetIamPolicy"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPatch"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPurge"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesList"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesPause"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesCreate"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesResume"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesGet"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesDelete"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTestIamPermissions"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesGetIamPolicy"] = cloudtasks.post(
        "v2/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksRun"] = cloudtasks.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksGet"] = cloudtasks.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksCreate"] = cloudtasks.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksList"] = cloudtasks.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsQueuesTasksDelete"] = cloudtasks.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudtasks",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
