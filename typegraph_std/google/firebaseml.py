from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firebaseml() -> Import:
    firebaseml = HTTPRuntime("https://firebaseml.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebaseml_1_ErrorResponse",
        "StatusIn": "_firebaseml_2_StatusIn",
        "StatusOut": "_firebaseml_3_StatusOut",
        "CancelOperationRequestIn": "_firebaseml_4_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_firebaseml_5_CancelOperationRequestOut",
        "ListOperationsResponseIn": "_firebaseml_6_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_firebaseml_7_ListOperationsResponseOut",
        "EmptyIn": "_firebaseml_8_EmptyIn",
        "EmptyOut": "_firebaseml_9_EmptyOut",
        "ModelOperationMetadataIn": "_firebaseml_10_ModelOperationMetadataIn",
        "ModelOperationMetadataOut": "_firebaseml_11_ModelOperationMetadataOut",
        "OperationIn": "_firebaseml_12_OperationIn",
        "OperationOut": "_firebaseml_13_OperationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ModelOperationMetadataIn"] = t.struct(
        {"basicOperationStatus": t.string(), "name": t.string().optional()}
    ).named(renames["ModelOperationMetadataIn"])
    types["ModelOperationMetadataOut"] = t.struct(
        {
            "basicOperationStatus": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])

    functions = {}
    functions["operationsCancel"] = firebaseml.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = firebaseml.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = firebaseml.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebaseml",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
