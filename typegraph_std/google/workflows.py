from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_workflows() -> Import:
    workflows = HTTPRuntime("https://workflows.googleapis.com/")

    renames = {
        "ErrorResponse": "_workflows_1_ErrorResponse",
        "ListWorkflowsResponseIn": "_workflows_2_ListWorkflowsResponseIn",
        "ListWorkflowsResponseOut": "_workflows_3_ListWorkflowsResponseOut",
        "EmptyIn": "_workflows_4_EmptyIn",
        "EmptyOut": "_workflows_5_EmptyOut",
        "ListOperationsResponseIn": "_workflows_6_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workflows_7_ListOperationsResponseOut",
        "StatusIn": "_workflows_8_StatusIn",
        "StatusOut": "_workflows_9_StatusOut",
        "OperationIn": "_workflows_10_OperationIn",
        "OperationOut": "_workflows_11_OperationOut",
        "OperationMetadataIn": "_workflows_12_OperationMetadataIn",
        "OperationMetadataOut": "_workflows_13_OperationMetadataOut",
        "ListLocationsResponseIn": "_workflows_14_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_workflows_15_ListLocationsResponseOut",
        "StateErrorIn": "_workflows_16_StateErrorIn",
        "StateErrorOut": "_workflows_17_StateErrorOut",
        "LocationIn": "_workflows_18_LocationIn",
        "LocationOut": "_workflows_19_LocationOut",
        "WorkflowIn": "_workflows_20_WorkflowIn",
        "WorkflowOut": "_workflows_21_WorkflowOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["WorkflowIn"] = t.struct(
        {
            "cryptoKeyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceContents": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["WorkflowIn"])
    types["WorkflowOut"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "cryptoKeyName": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceContents": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateError": t.proxy(renames["StateErrorOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "callLogLevel": t.string().optional(),
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowOut"])

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
    functions["projectsLocationsWorkflowsPatch"] = workflows.get(
        "v1/{parent}/workflows",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsGet"] = workflows.get(
        "v1/{parent}/workflows",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsCreate"] = workflows.get(
        "v1/{parent}/workflows",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsDelete"] = workflows.get(
        "v1/{parent}/workflows",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkflowsList"] = workflows.get(
        "v1/{parent}/workflows",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkflowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = workflows.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = workflows.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = workflows.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workflows", renames=renames, types=types, functions=functions
    )
