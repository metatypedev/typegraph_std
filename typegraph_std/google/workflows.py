from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_workflows():
    workflows = HTTPRuntime("https://workflows.googleapis.com/")

    renames = {
        "ErrorResponse": "_workflows_1_ErrorResponse",
        "ListLocationsResponseIn": "_workflows_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_workflows_3_ListLocationsResponseOut",
        "WorkflowIn": "_workflows_4_WorkflowIn",
        "WorkflowOut": "_workflows_5_WorkflowOut",
        "EmptyIn": "_workflows_6_EmptyIn",
        "EmptyOut": "_workflows_7_EmptyOut",
        "StateErrorIn": "_workflows_8_StateErrorIn",
        "StateErrorOut": "_workflows_9_StateErrorOut",
        "LocationIn": "_workflows_10_LocationIn",
        "LocationOut": "_workflows_11_LocationOut",
        "OperationIn": "_workflows_12_OperationIn",
        "OperationOut": "_workflows_13_OperationOut",
        "ListOperationsResponseIn": "_workflows_14_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workflows_15_ListOperationsResponseOut",
        "StatusIn": "_workflows_16_StatusIn",
        "StatusOut": "_workflows_17_StatusOut",
        "ListWorkflowsResponseIn": "_workflows_18_ListWorkflowsResponseIn",
        "ListWorkflowsResponseOut": "_workflows_19_ListWorkflowsResponseOut",
        "OperationMetadataIn": "_workflows_20_OperationMetadataIn",
        "OperationMetadataOut": "_workflows_21_OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["WorkflowIn"] = t.struct(
        {
            "description": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "sourceContents": t.string().optional(),
            "userEnvVars": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkflowIn"])
    types["WorkflowOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "stateError": t.proxy(renames["StateErrorOut"]).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "sourceContents": t.string().optional(),
            "userEnvVars": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
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
    types["ListWorkflowsResponseIn"] = t.struct(
        {
            "workflows": t.array(t.proxy(renames["WorkflowIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWorkflowsResponseIn"])
    types["ListWorkflowsResponseOut"] = t.struct(
        {
            "workflows": t.array(t.proxy(renames["WorkflowOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowsResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])

    functions = {}
    functions["projectsLocationsList"] = workflows.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = workflows.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsDelete"] = workflows.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "serviceAccount": t.string().optional(),
                "sourceContents": t.string().optional(),
                "userEnvVars": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsCreate"] = workflows.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "serviceAccount": t.string().optional(),
                "sourceContents": t.string().optional(),
                "userEnvVars": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsGet"] = workflows.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "serviceAccount": t.string().optional(),
                "sourceContents": t.string().optional(),
                "userEnvVars": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsList"] = workflows.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "serviceAccount": t.string().optional(),
                "sourceContents": t.string().optional(),
                "userEnvVars": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsPatch"] = workflows.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "serviceAccount": t.string().optional(),
                "sourceContents": t.string().optional(),
                "userEnvVars": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = workflows.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = workflows.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = workflows.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workflows",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
