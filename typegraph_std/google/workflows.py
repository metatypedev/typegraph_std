from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_workflows() -> Import:
    workflows = HTTPRuntime("https://workflows.googleapis.com/")

    renames = {
        "ErrorResponse": "_workflows_1_ErrorResponse",
        "StatusIn": "_workflows_2_StatusIn",
        "StatusOut": "_workflows_3_StatusOut",
        "ListWorkflowsResponseIn": "_workflows_4_ListWorkflowsResponseIn",
        "ListWorkflowsResponseOut": "_workflows_5_ListWorkflowsResponseOut",
        "OperationMetadataIn": "_workflows_6_OperationMetadataIn",
        "OperationMetadataOut": "_workflows_7_OperationMetadataOut",
        "StateErrorIn": "_workflows_8_StateErrorIn",
        "StateErrorOut": "_workflows_9_StateErrorOut",
        "OperationIn": "_workflows_10_OperationIn",
        "OperationOut": "_workflows_11_OperationOut",
        "EmptyIn": "_workflows_12_EmptyIn",
        "EmptyOut": "_workflows_13_EmptyOut",
        "WorkflowIn": "_workflows_14_WorkflowIn",
        "WorkflowOut": "_workflows_15_WorkflowOut",
        "ListOperationsResponseIn": "_workflows_16_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workflows_17_ListOperationsResponseOut",
        "LocationIn": "_workflows_18_LocationIn",
        "LocationOut": "_workflows_19_LocationOut",
        "ListLocationsResponseIn": "_workflows_20_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_workflows_21_ListLocationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListWorkflowsResponseIn"] = t.struct(
        {
            "workflows": t.array(t.proxy(renames["WorkflowIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListWorkflowsResponseIn"])
    types["ListWorkflowsResponseOut"] = t.struct(
        {
            "workflows": t.array(t.proxy(renames["WorkflowOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkflowsResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["WorkflowIn"] = t.struct(
        {
            "description": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "name": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceContents": t.string().optional(),
        }
    ).named(renames["WorkflowIn"])
    types["WorkflowOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "stateError": t.proxy(renames["StateErrorOut"]).optional(),
            "sourceContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = workflows.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = workflows.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsGet"] = workflows.post(
        "v1/{parent}/workflows",
        t.struct(
            {
                "workflowId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "name": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "sourceContents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsDelete"] = workflows.post(
        "v1/{parent}/workflows",
        t.struct(
            {
                "workflowId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "name": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "sourceContents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsList"] = workflows.post(
        "v1/{parent}/workflows",
        t.struct(
            {
                "workflowId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "name": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "sourceContents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsPatch"] = workflows.post(
        "v1/{parent}/workflows",
        t.struct(
            {
                "workflowId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "name": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "sourceContents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsCreate"] = workflows.post(
        "v1/{parent}/workflows",
        t.struct(
            {
                "workflowId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "callLogLevel": t.string().optional(),
                "name": t.string().optional(),
                "cryptoKeyName": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "sourceContents": t.string().optional(),
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
