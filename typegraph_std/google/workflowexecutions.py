from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_workflowexecutions() -> Import:
    workflowexecutions = HTTPRuntime("https://workflowexecutions.googleapis.com/")

    renames = {
        "ErrorResponse": "_workflowexecutions_1_ErrorResponse",
        "PubsubMessageIn": "_workflowexecutions_2_PubsubMessageIn",
        "PubsubMessageOut": "_workflowexecutions_3_PubsubMessageOut",
        "PositionIn": "_workflowexecutions_4_PositionIn",
        "PositionOut": "_workflowexecutions_5_PositionOut",
        "ErrorIn": "_workflowexecutions_6_ErrorIn",
        "ErrorOut": "_workflowexecutions_7_ErrorOut",
        "StackTraceIn": "_workflowexecutions_8_StackTraceIn",
        "StackTraceOut": "_workflowexecutions_9_StackTraceOut",
        "StatusIn": "_workflowexecutions_10_StatusIn",
        "StatusOut": "_workflowexecutions_11_StatusOut",
        "StepIn": "_workflowexecutions_12_StepIn",
        "StepOut": "_workflowexecutions_13_StepOut",
        "StateErrorIn": "_workflowexecutions_14_StateErrorIn",
        "StateErrorOut": "_workflowexecutions_15_StateErrorOut",
        "StackTraceElementIn": "_workflowexecutions_16_StackTraceElementIn",
        "StackTraceElementOut": "_workflowexecutions_17_StackTraceElementOut",
        "CancelExecutionRequestIn": "_workflowexecutions_18_CancelExecutionRequestIn",
        "CancelExecutionRequestOut": "_workflowexecutions_19_CancelExecutionRequestOut",
        "TriggerPubsubExecutionRequestIn": "_workflowexecutions_20_TriggerPubsubExecutionRequestIn",
        "TriggerPubsubExecutionRequestOut": "_workflowexecutions_21_TriggerPubsubExecutionRequestOut",
        "ExecutionIn": "_workflowexecutions_22_ExecutionIn",
        "ExecutionOut": "_workflowexecutions_23_ExecutionOut",
        "ListExecutionsResponseIn": "_workflowexecutions_24_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workflowexecutions_25_ListExecutionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PubsubMessageIn"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "publishTime": t.string().optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "publishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["PositionIn"] = t.struct(
        {
            "column": t.string().optional(),
            "length": t.string().optional(),
            "line": t.string().optional(),
        }
    ).named(renames["PositionIn"])
    types["PositionOut"] = t.struct(
        {
            "column": t.string().optional(),
            "length": t.string().optional(),
            "line": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PositionOut"])
    types["ErrorIn"] = t.struct(
        {
            "payload": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "context": t.string().optional(),
        }
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "payload": t.string().optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "context": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["StackTraceIn"] = t.struct(
        {"elements": t.array(t.proxy(renames["StackTraceElementIn"])).optional()}
    ).named(renames["StackTraceIn"])
    types["StackTraceOut"] = t.struct(
        {
            "elements": t.array(t.proxy(renames["StackTraceElementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["StatusIn"] = t.struct(
        {"currentSteps": t.array(t.proxy(renames["StepIn"])).optional()}
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "currentSteps": t.array(t.proxy(renames["StepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["StackTraceElementIn"] = t.struct(
        {
            "step": t.string().optional(),
            "position": t.proxy(renames["PositionIn"]).optional(),
            "routine": t.string().optional(),
        }
    ).named(renames["StackTraceElementIn"])
    types["StackTraceElementOut"] = t.struct(
        {
            "step": t.string().optional(),
            "position": t.proxy(renames["PositionOut"]).optional(),
            "routine": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceElementOut"])
    types["CancelExecutionRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelExecutionRequestIn"]
    )
    types["CancelExecutionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelExecutionRequestOut"])
    types["TriggerPubsubExecutionRequestIn"] = t.struct(
        {
            "GCPCloudEventsMode": t.string(),
            "message": t.proxy(renames["PubsubMessageIn"]),
            "subscription": t.string(),
        }
    ).named(renames["TriggerPubsubExecutionRequestIn"])
    types["TriggerPubsubExecutionRequestOut"] = t.struct(
        {
            "GCPCloudEventsMode": t.string(),
            "message": t.proxy(renames["PubsubMessageOut"]),
            "subscription": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TriggerPubsubExecutionRequestOut"])
    types["ExecutionIn"] = t.struct(
        {
            "argument": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "endTime": t.string().optional(),
            "argument": t.string().optional(),
            "result": t.string().optional(),
            "state": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stateError": t.proxy(renames["StateErrorOut"]).optional(),
            "workflowRevisionId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
        }
    ).named(renames["ExecutionOut"])
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

    functions = {}
    functions[
        "projectsLocationsWorkflowsTriggerPubsubExecution"
    ] = workflowexecutions.post(
        "v1/{workflow}:triggerPubsubExecution",
        t.struct(
            {
                "workflow": t.string(),
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
        importer="workflowexecutions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
