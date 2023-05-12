from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_workflowexecutions() -> Import:
    workflowexecutions = HTTPRuntime("https://workflowexecutions.googleapis.com/")

    renames = {
        "ErrorResponse": "_workflowexecutions_1_ErrorResponse",
        "StepIn": "_workflowexecutions_2_StepIn",
        "StepOut": "_workflowexecutions_3_StepOut",
        "PubsubMessageIn": "_workflowexecutions_4_PubsubMessageIn",
        "PubsubMessageOut": "_workflowexecutions_5_PubsubMessageOut",
        "PositionIn": "_workflowexecutions_6_PositionIn",
        "PositionOut": "_workflowexecutions_7_PositionOut",
        "ListExecutionsResponseIn": "_workflowexecutions_8_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workflowexecutions_9_ListExecutionsResponseOut",
        "StackTraceIn": "_workflowexecutions_10_StackTraceIn",
        "StackTraceOut": "_workflowexecutions_11_StackTraceOut",
        "StackTraceElementIn": "_workflowexecutions_12_StackTraceElementIn",
        "StackTraceElementOut": "_workflowexecutions_13_StackTraceElementOut",
        "ExecutionIn": "_workflowexecutions_14_ExecutionIn",
        "ExecutionOut": "_workflowexecutions_15_ExecutionOut",
        "ErrorIn": "_workflowexecutions_16_ErrorIn",
        "ErrorOut": "_workflowexecutions_17_ErrorOut",
        "TriggerPubsubExecutionRequestIn": "_workflowexecutions_18_TriggerPubsubExecutionRequestIn",
        "TriggerPubsubExecutionRequestOut": "_workflowexecutions_19_TriggerPubsubExecutionRequestOut",
        "StateErrorIn": "_workflowexecutions_20_StateErrorIn",
        "StateErrorOut": "_workflowexecutions_21_StateErrorOut",
        "CancelExecutionRequestIn": "_workflowexecutions_22_CancelExecutionRequestIn",
        "CancelExecutionRequestOut": "_workflowexecutions_23_CancelExecutionRequestOut",
        "StatusIn": "_workflowexecutions_24_StatusIn",
        "StatusOut": "_workflowexecutions_25_StatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StepIn"] = t.struct(
        {"routine": t.string().optional(), "step": t.string().optional()}
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "routine": t.string().optional(),
            "step": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["PubsubMessageIn"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["PositionIn"] = t.struct(
        {
            "length": t.string().optional(),
            "column": t.string().optional(),
            "line": t.string().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "length": t.string().optional(),
            "column": t.string().optional(),
            "line": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])
    types["StackTraceIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["StackTraceElementIn"])).optional()}
    ).named(renames["StackTraceIn"])
    types["StackTraceOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["StackTraceElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["StackTraceElementIn"] = t.struct(
        {
            "routine": t.string().optional(),
            "step": t.string().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
        }
    ).named(renames["StackTraceElementIn"])
    types["StackTraceElementOut"] = t.struct(
        {
            "routine": t.string().optional(),
            "step": t.string().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceElementOut"])
    types["ExecutionIn"] = t.struct(
        {
            "argument": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "callLogLevel": t.string().optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "argument": t.string().optional(),
            "workflowRevisionId": t.string().optional(),
            "result": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "callLogLevel": t.string().optional(),
            "stateError": t.proxy(renames["StateErrorOut"]).optional(),
            "duration": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ExecutionOut"])
    types["ErrorIn"] = t.struct(
        {
            "context": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "payload": t.string().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "context": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "payload": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["TriggerPubsubExecutionRequestIn"] = t.struct(
        {
            "GCPCloudEventsMode": t.string(),
            "subscription": t.string(),
            "message": t.proxy(renames["PubsubMessageIn"]),
        }
    ).named(renames["TriggerPubsubExecutionRequestIn"])
    types["TriggerPubsubExecutionRequestOut"] = t.struct(
        {
            "GCPCloudEventsMode": t.string(),
            "subscription": t.string(),
            "message": t.proxy(renames["PubsubMessageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerPubsubExecutionRequestOut"])
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

    functions = {}
    functions[
        "projectsLocationsWorkflowsTriggerPubsubExecution"
    ] = workflowexecutions.post(
        "v1/{workflow}:triggerPubsubExecution",
        t.struct(
            {
                "workflow": t.string(),
                "GCPCloudEventsMode": t.string(),
                "subscription": t.string(),
                "message": t.proxy(renames["PubsubMessageIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsCancel"] = workflowexecutions.post(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "argument": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "callLogLevel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsGet"] = workflowexecutions.post(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "argument": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "callLogLevel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsList"] = workflowexecutions.post(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "argument": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "callLogLevel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsCreate"] = workflowexecutions.post(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "argument": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "callLogLevel": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workflowexecutions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
