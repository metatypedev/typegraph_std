from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    ListQueuesResponseIn: t.typedef = ...
    ListQueuesResponseOut: t.typedef = ...
    QueueIn: t.typedef = ...
    QueueOut: t.typedef = ...
    AppEngineRoutingIn: t.typedef = ...
    AppEngineRoutingOut: t.typedef = ...
    RateLimitsIn: t.typedef = ...
    RateLimitsOut: t.typedef = ...
    RetryConfigIn: t.typedef = ...
    RetryConfigOut: t.typedef = ...
    StackdriverLoggingConfigIn: t.typedef = ...
    StackdriverLoggingConfigOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    PurgeQueueRequestIn: t.typedef = ...
    PurgeQueueRequestOut: t.typedef = ...
    PauseQueueRequestIn: t.typedef = ...
    PauseQueueRequestOut: t.typedef = ...
    ResumeQueueRequestIn: t.typedef = ...
    ResumeQueueRequestOut: t.typedef = ...
    GetIamPolicyRequestIn: t.typedef = ...
    GetIamPolicyRequestOut: t.typedef = ...
    GetPolicyOptionsIn: t.typedef = ...
    GetPolicyOptionsOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    ListTasksResponseIn: t.typedef = ...
    ListTasksResponseOut: t.typedef = ...
    TaskIn: t.typedef = ...
    TaskOut: t.typedef = ...
    AppEngineHttpRequestIn: t.typedef = ...
    AppEngineHttpRequestOut: t.typedef = ...
    HttpRequestIn: t.typedef = ...
    HttpRequestOut: t.typedef = ...
    OAuthTokenIn: t.typedef = ...
    OAuthTokenOut: t.typedef = ...
    OidcTokenIn: t.typedef = ...
    OidcTokenOut: t.typedef = ...
    AttemptIn: t.typedef = ...
    AttemptOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    CreateTaskRequestIn: t.typedef = ...
    CreateTaskRequestOut: t.typedef = ...
    RunTaskRequestIn: t.typedef = ...
    RunTaskRequestOut: t.typedef = ...

class FuncList:
    projectsLocationsList: t.func = ...
    projectsLocationsGet: t.func = ...
    projectsLocationsQueuesList: t.func = ...
    projectsLocationsQueuesGet: t.func = ...
    projectsLocationsQueuesCreate: t.func = ...
    projectsLocationsQueuesPatch: t.func = ...
    projectsLocationsQueuesDelete: t.func = ...
    projectsLocationsQueuesPurge: t.func = ...
    projectsLocationsQueuesPause: t.func = ...
    projectsLocationsQueuesResume: t.func = ...
    projectsLocationsQueuesGetIamPolicy: t.func = ...
    projectsLocationsQueuesSetIamPolicy: t.func = ...
    projectsLocationsQueuesTestIamPermissions: t.func = ...
    projectsLocationsQueuesTasksList: t.func = ...
    projectsLocationsQueuesTasksGet: t.func = ...
    projectsLocationsQueuesTasksCreate: t.func = ...
    projectsLocationsQueuesTasksDelete: t.func = ...
    projectsLocationsQueuesTasksRun: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_cloudtasks() -> Import: ...