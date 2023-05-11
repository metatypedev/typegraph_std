from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firebaseml() -> Import:
    firebaseml = HTTPRuntime("https://firebaseml.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebaseml_1_ErrorResponse",
        "ListOperationsResponseIn": "_firebaseml_2_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_firebaseml_3_ListOperationsResponseOut",
        "CancelOperationRequestIn": "_firebaseml_4_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_firebaseml_5_CancelOperationRequestOut",
        "StatusIn": "_firebaseml_6_StatusIn",
        "StatusOut": "_firebaseml_7_StatusOut",
        "OperationIn": "_firebaseml_8_OperationIn",
        "OperationOut": "_firebaseml_9_OperationOut",
        "ModelOperationMetadataIn": "_firebaseml_10_ModelOperationMetadataIn",
        "ModelOperationMetadataOut": "_firebaseml_11_ModelOperationMetadataOut",
        "EmptyIn": "_firebaseml_12_EmptyIn",
        "EmptyOut": "_firebaseml_13_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ModelOperationMetadataIn"] = t.struct(
        {"name": t.string().optional(), "basicOperationStatus": t.string()}
    ).named(renames["ModelOperationMetadataIn"])
    types["ModelOperationMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "basicOperationStatus": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOperationMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["operationsCancel"] = firebaseml.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = firebaseml.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = firebaseml.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebaseml", renames=renames, types=types, functions=functions
    )
