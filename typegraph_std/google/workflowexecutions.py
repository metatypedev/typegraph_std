from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_workflowexecutions() -> Import:
    workflowexecutions = HTTPRuntime("https://workflowexecutions.googleapis.com/")

    renames = {
        "ErrorResponse": "_workflowexecutions_1_ErrorResponse",
        "ErrorIn": "_workflowexecutions_2_ErrorIn",
        "ErrorOut": "_workflowexecutions_3_ErrorOut",
        "ListExecutionsResponseIn": "_workflowexecutions_4_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workflowexecutions_5_ListExecutionsResponseOut",
        "PositionIn": "_workflowexecutions_6_PositionIn",
        "PositionOut": "_workflowexecutions_7_PositionOut",
        "StackTraceElementIn": "_workflowexecutions_8_StackTraceElementIn",
        "StackTraceElementOut": "_workflowexecutions_9_StackTraceElementOut",
        "StackTraceIn": "_workflowexecutions_10_StackTraceIn",
        "StackTraceOut": "_workflowexecutions_11_StackTraceOut",
        "StateErrorIn": "_workflowexecutions_12_StateErrorIn",
        "StateErrorOut": "_workflowexecutions_13_StateErrorOut",
        "ExecutionIn": "_workflowexecutions_14_ExecutionIn",
        "ExecutionOut": "_workflowexecutions_15_ExecutionOut",
        "CancelExecutionRequestIn": "_workflowexecutions_16_CancelExecutionRequestIn",
        "CancelExecutionRequestOut": "_workflowexecutions_17_CancelExecutionRequestOut",
        "StatusIn": "_workflowexecutions_18_StatusIn",
        "StatusOut": "_workflowexecutions_19_StatusOut",
        "PubsubMessageIn": "_workflowexecutions_20_PubsubMessageIn",
        "PubsubMessageOut": "_workflowexecutions_21_PubsubMessageOut",
        "TriggerPubsubExecutionRequestIn": "_workflowexecutions_22_TriggerPubsubExecutionRequestIn",
        "TriggerPubsubExecutionRequestOut": "_workflowexecutions_23_TriggerPubsubExecutionRequestOut",
        "StepIn": "_workflowexecutions_24_StepIn",
        "StepOut": "_workflowexecutions_25_StepOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["StackTraceElementIn"] = t.struct(
        {
            "routine": t.string().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "step": t.string().optional(),
        }
    ).named(renames["StackTraceElementIn"])
    types["StackTraceElementOut"] = t.struct(
        {
            "routine": t.string().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "step": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceElementOut"])
    types["StackTraceIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["StackTraceElementIn"])).optional()}
    ).named(renames["StackTraceIn"])
    types["StackTraceOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["StackTraceElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["StateErrorIn"] = t.struct(
        {"details": t.string().optional(), "type": t.string().optional()}
    ).named(renames["StateErrorIn"])
    types["StateErrorOut"] = t.struct(
        {
            "details": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StateErrorOut"])
    types["ExecutionIn"] = t.struct(
        {
            "callLogLevel": t.string().optional(),
            "argument": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "workflowRevisionId": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "startTime": t.string().optional(),
            "argument": t.string().optional(),
            "name": t.string().optional(),
            "duration": t.string().optional(),
            "result": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stateError": t.proxy(renames["StateErrorOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["ExecutionOut"])
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
    types["PubsubMessageIn"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "data": t.string().optional(),
            "orderingKey": t.string().optional(),
            "messageId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "data": t.string().optional(),
            "orderingKey": t.string().optional(),
            "messageId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["TriggerPubsubExecutionRequestIn"] = t.struct(
        {
            "subscription": t.string(),
            "GCPCloudEventsMode": t.string(),
            "message": t.proxy(renames["PubsubMessageIn"]),
        }
    ).named(renames["TriggerPubsubExecutionRequestIn"])
    types["TriggerPubsubExecutionRequestOut"] = t.struct(
        {
            "subscription": t.string(),
            "GCPCloudEventsMode": t.string(),
            "message": t.proxy(renames["PubsubMessageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerPubsubExecutionRequestOut"])
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

    functions = {}
    functions[
        "projectsLocationsWorkflowsTriggerPubsubExecution"
    ] = workflowexecutions.post(
        "v1/{workflow}:triggerPubsubExecution",
        t.struct(
            {
                "workflow": t.string(),
                "subscription": t.string(),
                "GCPCloudEventsMode": t.string(),
                "message": t.proxy(renames["PubsubMessageIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsList"] = workflowexecutions.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsCreate"] = workflowexecutions.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsCancel"] = workflowexecutions.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsExecutionsGet"] = workflowexecutions.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workflowexecutions", renames=renames, types=types, functions=functions
    )
