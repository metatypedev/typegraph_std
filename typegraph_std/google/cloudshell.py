from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudshell() -> Import:
    cloudshell = HTTPRuntime("https://cloudshell.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudshell_1_ErrorResponse",
        "AddPublicKeyMetadataIn": "_cloudshell_2_AddPublicKeyMetadataIn",
        "AddPublicKeyMetadataOut": "_cloudshell_3_AddPublicKeyMetadataOut",
        "RemovePublicKeyRequestIn": "_cloudshell_4_RemovePublicKeyRequestIn",
        "RemovePublicKeyRequestOut": "_cloudshell_5_RemovePublicKeyRequestOut",
        "StartEnvironmentRequestIn": "_cloudshell_6_StartEnvironmentRequestIn",
        "StartEnvironmentRequestOut": "_cloudshell_7_StartEnvironmentRequestOut",
        "AuthorizeEnvironmentMetadataIn": "_cloudshell_8_AuthorizeEnvironmentMetadataIn",
        "AuthorizeEnvironmentMetadataOut": "_cloudshell_9_AuthorizeEnvironmentMetadataOut",
        "AuthorizeEnvironmentResponseIn": "_cloudshell_10_AuthorizeEnvironmentResponseIn",
        "AuthorizeEnvironmentResponseOut": "_cloudshell_11_AuthorizeEnvironmentResponseOut",
        "StartEnvironmentResponseIn": "_cloudshell_12_StartEnvironmentResponseIn",
        "StartEnvironmentResponseOut": "_cloudshell_13_StartEnvironmentResponseOut",
        "DeleteEnvironmentMetadataIn": "_cloudshell_14_DeleteEnvironmentMetadataIn",
        "DeleteEnvironmentMetadataOut": "_cloudshell_15_DeleteEnvironmentMetadataOut",
        "StartEnvironmentMetadataIn": "_cloudshell_16_StartEnvironmentMetadataIn",
        "StartEnvironmentMetadataOut": "_cloudshell_17_StartEnvironmentMetadataOut",
        "CancelOperationRequestIn": "_cloudshell_18_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudshell_19_CancelOperationRequestOut",
        "AddPublicKeyRequestIn": "_cloudshell_20_AddPublicKeyRequestIn",
        "AddPublicKeyRequestOut": "_cloudshell_21_AddPublicKeyRequestOut",
        "ListOperationsResponseIn": "_cloudshell_22_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudshell_23_ListOperationsResponseOut",
        "RemovePublicKeyResponseIn": "_cloudshell_24_RemovePublicKeyResponseIn",
        "RemovePublicKeyResponseOut": "_cloudshell_25_RemovePublicKeyResponseOut",
        "RemovePublicKeyMetadataIn": "_cloudshell_26_RemovePublicKeyMetadataIn",
        "RemovePublicKeyMetadataOut": "_cloudshell_27_RemovePublicKeyMetadataOut",
        "CreateEnvironmentMetadataIn": "_cloudshell_28_CreateEnvironmentMetadataIn",
        "CreateEnvironmentMetadataOut": "_cloudshell_29_CreateEnvironmentMetadataOut",
        "AuthorizeEnvironmentRequestIn": "_cloudshell_30_AuthorizeEnvironmentRequestIn",
        "AuthorizeEnvironmentRequestOut": "_cloudshell_31_AuthorizeEnvironmentRequestOut",
        "OperationIn": "_cloudshell_32_OperationIn",
        "OperationOut": "_cloudshell_33_OperationOut",
        "StatusIn": "_cloudshell_34_StatusIn",
        "StatusOut": "_cloudshell_35_StatusOut",
        "EnvironmentIn": "_cloudshell_36_EnvironmentIn",
        "EnvironmentOut": "_cloudshell_37_EnvironmentOut",
        "EmptyIn": "_cloudshell_38_EmptyIn",
        "EmptyOut": "_cloudshell_39_EmptyOut",
        "AddPublicKeyResponseIn": "_cloudshell_40_AddPublicKeyResponseIn",
        "AddPublicKeyResponseOut": "_cloudshell_41_AddPublicKeyResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AddPublicKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddPublicKeyMetadataIn"]
    )
    types["AddPublicKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddPublicKeyMetadataOut"])
    types["RemovePublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["RemovePublicKeyRequestIn"]
    )
    types["RemovePublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemovePublicKeyRequestOut"])
    types["StartEnvironmentRequestIn"] = t.struct(
        {
            "publicKeys": t.array(t.string()).optional(),
            "accessToken": t.string().optional(),
        }
    ).named(renames["StartEnvironmentRequestIn"])
    types["StartEnvironmentRequestOut"] = t.struct(
        {
            "publicKeys": t.array(t.string()).optional(),
            "accessToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartEnvironmentRequestOut"])
    types["AuthorizeEnvironmentMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentMetadataIn"])
    types["AuthorizeEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentMetadataOut"])
    types["AuthorizeEnvironmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentResponseIn"])
    types["AuthorizeEnvironmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentResponseOut"])
    types["StartEnvironmentResponseIn"] = t.struct(
        {"environment": t.proxy(renames["EnvironmentIn"]).optional()}
    ).named(renames["StartEnvironmentResponseIn"])
    types["StartEnvironmentResponseOut"] = t.struct(
        {
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartEnvironmentResponseOut"])
    types["DeleteEnvironmentMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteEnvironmentMetadataIn"]
    )
    types["DeleteEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteEnvironmentMetadataOut"])
    types["StartEnvironmentMetadataIn"] = t.struct(
        {"state": t.string().optional()}
    ).named(renames["StartEnvironmentMetadataIn"])
    types["StartEnvironmentMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartEnvironmentMetadataOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["AddPublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyRequestIn"]
    )
    types["AddPublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyRequestOut"])
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
    types["RemovePublicKeyResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyResponseIn"]
    )
    types["RemovePublicKeyResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyResponseOut"])
    types["RemovePublicKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyMetadataIn"]
    )
    types["RemovePublicKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyMetadataOut"])
    types["CreateEnvironmentMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateEnvironmentMetadataIn"]
    )
    types["CreateEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateEnvironmentMetadataOut"])
    types["AuthorizeEnvironmentRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "accessToken": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["AuthorizeEnvironmentRequestIn"])
    types["AuthorizeEnvironmentRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "accessToken": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizeEnvironmentRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["EnvironmentIn"] = t.struct(
        {"name": t.string().optional(), "dockerImage": t.string()}
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "publicKeys": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "webHost": t.string().optional(),
            "name": t.string().optional(),
            "sshPort": t.integer().optional(),
            "sshUsername": t.string().optional(),
            "sshHost": t.string().optional(),
            "dockerImage": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AddPublicKeyResponseIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyResponseIn"]
    )
    types["AddPublicKeyResponseOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyResponseOut"])

    functions = {}
    functions["operationsDelete"] = cloudshell.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = cloudshell.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudshell.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = cloudshell.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsAddPublicKey"] = cloudshell.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string().optional(),
                "publicKeys": t.array(t.string()).optional(),
                "accessToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsGet"] = cloudshell.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string().optional(),
                "publicKeys": t.array(t.string()).optional(),
                "accessToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsRemovePublicKey"] = cloudshell.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string().optional(),
                "publicKeys": t.array(t.string()).optional(),
                "accessToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsAuthorize"] = cloudshell.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string().optional(),
                "publicKeys": t.array(t.string()).optional(),
                "accessToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsStart"] = cloudshell.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string().optional(),
                "publicKeys": t.array(t.string()).optional(),
                "accessToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudshell", renames=renames, types=types, functions=functions
    )
