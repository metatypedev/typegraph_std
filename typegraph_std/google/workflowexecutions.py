from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_workflowexecutions():
    workflowexecutions = HTTPRuntime("https://workflowexecutions.googleapis.com/")

    renames = {
        "ErrorResponse": "_workflowexecutions_1_ErrorResponse",
        "StackTraceElementIn": "_workflowexecutions_2_StackTraceElementIn",
        "StackTraceElementOut": "_workflowexecutions_3_StackTraceElementOut",
        "StateErrorIn": "_workflowexecutions_4_StateErrorIn",
        "StateErrorOut": "_workflowexecutions_5_StateErrorOut",
        "StackTraceIn": "_workflowexecutions_6_StackTraceIn",
        "StackTraceOut": "_workflowexecutions_7_StackTraceOut",
        "CancelExecutionRequestIn": "_workflowexecutions_8_CancelExecutionRequestIn",
        "CancelExecutionRequestOut": "_workflowexecutions_9_CancelExecutionRequestOut",
        "StatusIn": "_workflowexecutions_10_StatusIn",
        "StatusOut": "_workflowexecutions_11_StatusOut",
        "ErrorIn": "_workflowexecutions_12_ErrorIn",
        "ErrorOut": "_workflowexecutions_13_ErrorOut",
        "PositionIn": "_workflowexecutions_14_PositionIn",
        "PositionOut": "_workflowexecutions_15_PositionOut",
        "StepIn": "_workflowexecutions_16_StepIn",
        "StepOut": "_workflowexecutions_17_StepOut",
        "ExecutionIn": "_workflowexecutions_18_ExecutionIn",
        "ExecutionOut": "_workflowexecutions_19_ExecutionOut",
        "PubsubMessageIn": "_workflowexecutions_20_PubsubMessageIn",
        "PubsubMessageOut": "_workflowexecutions_21_PubsubMessageOut",
        "TriggerPubsubExecutionRequestIn": "_workflowexecutions_22_TriggerPubsubExecutionRequestIn",
        "TriggerPubsubExecutionRequestOut": "_workflowexecutions_23_TriggerPubsubExecutionRequestOut",
        "ListExecutionsResponseIn": "_workflowexecutions_24_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workflowexecutions_25_ListExecutionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StackTraceElementIn"] = t.struct(
        {
            "position": t.proxy(renames["PositionIn"]).optional(),
            "routine": t.string().optional(),
            "step": t.string().optional(),
        }
    ).named(renames["StackTraceElementIn"])
    types["StackTraceElementOut"] = t.struct(
        {
            "position": t.proxy(renames["PositionOut"]).optional(),
            "routine": t.string().optional(),
            "step": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceElementOut"])
    types["StateErrorIn"] = t.struct(
        {"type": t.string().optional(), "details": t.string().optional()}
    ).named(renames["StateErrorIn"])
    types["StateErrorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateErrorOut"])
    types["StackTraceIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["StackTraceElementIn"])).optional()}
    ).named(renames["StackTraceIn"])
    types["StackTraceOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["StackTraceElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["CancelExecutionRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelExecutionRequestIn"]
    )
    types["CancelExecutionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelExecutionRequestOut"])
    types["StatusIn"] = t.struct(
        {"currentSteps": t.array(t.proxy(renames["StepIn"])).optional()}
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "currentSteps": t.array(t.proxy(renames["StepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ErrorIn"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "payload": t.string().optional(),
            "context": t.string().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "payload": t.string().optional(),
            "context": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["PositionIn"] = t.struct(
        {
            "column": t.string().optional(),
            "line": t.string().optional(),
            "length": t.string().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "column": t.string().optional(),
            "line": t.string().optional(),
            "length": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
    types["StepIn"] = t.struct(
        {"step": t.string().optional(), "routine": t.string().optional()}
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "step": t.string().optional(),
            "routine": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["ExecutionIn"] = t.struct(
        {
            "callLogLevel": t.string().optional(),
            "argument": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "result": t.string().optional(),
            "state": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "argument": t.string().optional(),
            "workflowRevisionId": t.string().optional(),
            "endTime": t.string().optional(),
            "stateError": t.proxy(renames["StateErrorOut"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ExecutionOut"])
    types["PubsubMessageIn"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "publishTime": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "publishTime": t.string().optional(),
            "data": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["TriggerPubsubExecutionRequestIn"] = t.struct(
        {
            "deliveryAttempt": t.integer().optional(),
            "GCPCloudEventsMode": t.string(),
            "message": t.proxy(renames["PubsubMessageIn"]),
            "subscription": t.string(),
        }
    ).named(renames["TriggerPubsubExecutionRequestIn"])
    types["TriggerPubsubExecutionRequestOut"] = t.struct(
        {
            "deliveryAttempt": t.integer().optional(),
            "GCPCloudEventsMode": t.string(),
            "message": t.proxy(renames["PubsubMessageOut"]),
            "subscription": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerPubsubExecutionRequestOut"])
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])

    functions = {}
    functions[
        "projectsLocationsWorkflowsTriggerPubsubExecution"
    ] = workflowexecutions.post(
        "v1/{workflow}:triggerPubsubExecution",
        t.struct(
            {
                "workflow": t.string(),
                "deliveryAttempt": t.integer().optional(),
                "GCPCloudEventsMode": t.string(),
                "message": t.proxy(renames["PubsubMessageIn"]),
                "subscription": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsGet"] = workflowexecutions.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsCancel"] = workflowexecutions.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsCreate"] = workflowexecutions.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsList"] = workflowexecutions.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workflowexecutions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
