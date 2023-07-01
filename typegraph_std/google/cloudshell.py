from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudshell():
    cloudshell = HTTPRuntime("https://cloudshell.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudshell_1_ErrorResponse",
        "RemovePublicKeyRequestIn": "_cloudshell_2_RemovePublicKeyRequestIn",
        "RemovePublicKeyRequestOut": "_cloudshell_3_RemovePublicKeyRequestOut",
        "EnvironmentIn": "_cloudshell_4_EnvironmentIn",
        "EnvironmentOut": "_cloudshell_5_EnvironmentOut",
        "RemovePublicKeyResponseIn": "_cloudshell_6_RemovePublicKeyResponseIn",
        "RemovePublicKeyResponseOut": "_cloudshell_7_RemovePublicKeyResponseOut",
        "AuthorizeEnvironmentRequestIn": "_cloudshell_8_AuthorizeEnvironmentRequestIn",
        "AuthorizeEnvironmentRequestOut": "_cloudshell_9_AuthorizeEnvironmentRequestOut",
        "AddPublicKeyRequestIn": "_cloudshell_10_AddPublicKeyRequestIn",
        "AddPublicKeyRequestOut": "_cloudshell_11_AddPublicKeyRequestOut",
        "CreateEnvironmentMetadataIn": "_cloudshell_12_CreateEnvironmentMetadataIn",
        "CreateEnvironmentMetadataOut": "_cloudshell_13_CreateEnvironmentMetadataOut",
        "StartEnvironmentMetadataIn": "_cloudshell_14_StartEnvironmentMetadataIn",
        "StartEnvironmentMetadataOut": "_cloudshell_15_StartEnvironmentMetadataOut",
        "DeleteEnvironmentMetadataIn": "_cloudshell_16_DeleteEnvironmentMetadataIn",
        "DeleteEnvironmentMetadataOut": "_cloudshell_17_DeleteEnvironmentMetadataOut",
        "RemovePublicKeyMetadataIn": "_cloudshell_18_RemovePublicKeyMetadataIn",
        "RemovePublicKeyMetadataOut": "_cloudshell_19_RemovePublicKeyMetadataOut",
        "ListOperationsResponseIn": "_cloudshell_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudshell_21_ListOperationsResponseOut",
        "StartEnvironmentRequestIn": "_cloudshell_22_StartEnvironmentRequestIn",
        "StartEnvironmentRequestOut": "_cloudshell_23_StartEnvironmentRequestOut",
        "CancelOperationRequestIn": "_cloudshell_24_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudshell_25_CancelOperationRequestOut",
        "AddPublicKeyMetadataIn": "_cloudshell_26_AddPublicKeyMetadataIn",
        "AddPublicKeyMetadataOut": "_cloudshell_27_AddPublicKeyMetadataOut",
        "StartEnvironmentResponseIn": "_cloudshell_28_StartEnvironmentResponseIn",
        "StartEnvironmentResponseOut": "_cloudshell_29_StartEnvironmentResponseOut",
        "StatusIn": "_cloudshell_30_StatusIn",
        "StatusOut": "_cloudshell_31_StatusOut",
        "OperationIn": "_cloudshell_32_OperationIn",
        "OperationOut": "_cloudshell_33_OperationOut",
        "AuthorizeEnvironmentResponseIn": "_cloudshell_34_AuthorizeEnvironmentResponseIn",
        "AuthorizeEnvironmentResponseOut": "_cloudshell_35_AuthorizeEnvironmentResponseOut",
        "AddPublicKeyResponseIn": "_cloudshell_36_AddPublicKeyResponseIn",
        "AddPublicKeyResponseOut": "_cloudshell_37_AddPublicKeyResponseOut",
        "EmptyIn": "_cloudshell_38_EmptyIn",
        "EmptyOut": "_cloudshell_39_EmptyOut",
        "AuthorizeEnvironmentMetadataIn": "_cloudshell_40_AuthorizeEnvironmentMetadataIn",
        "AuthorizeEnvironmentMetadataOut": "_cloudshell_41_AuthorizeEnvironmentMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RemovePublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["RemovePublicKeyRequestIn"]
    )
    types["RemovePublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemovePublicKeyRequestOut"])
    types["EnvironmentIn"] = t.struct(
        {"name": t.string().optional(), "dockerImage": t.string()}
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "sshHost": t.string().optional(),
            "dockerImage": t.string(),
            "publicKeys": t.array(t.string()).optional(),
            "webHost": t.string().optional(),
            "sshPort": t.integer().optional(),
            "sshUsername": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["RemovePublicKeyResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyResponseIn"]
    )
    types["RemovePublicKeyResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyResponseOut"])
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
    types["AddPublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyRequestIn"]
    )
    types["AddPublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyRequestOut"])
    types["CreateEnvironmentMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateEnvironmentMetadataIn"]
    )
    types["CreateEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateEnvironmentMetadataOut"])
    types["StartEnvironmentMetadataIn"] = t.struct(
        {"state": t.string().optional()}
    ).named(renames["StartEnvironmentMetadataIn"])
    types["StartEnvironmentMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartEnvironmentMetadataOut"])
    types["DeleteEnvironmentMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteEnvironmentMetadataIn"]
    )
    types["DeleteEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteEnvironmentMetadataOut"])
    types["RemovePublicKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyMetadataIn"]
    )
    types["RemovePublicKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyMetadataOut"])
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
    types["StartEnvironmentRequestIn"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "publicKeys": t.array(t.string()).optional(),
        }
    ).named(renames["StartEnvironmentRequestIn"])
    types["StartEnvironmentRequestOut"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "publicKeys": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartEnvironmentRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["AddPublicKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddPublicKeyMetadataIn"]
    )
    types["AddPublicKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddPublicKeyMetadataOut"])
    types["StartEnvironmentResponseIn"] = t.struct(
        {"environment": t.proxy(renames["EnvironmentIn"]).optional()}
    ).named(renames["StartEnvironmentResponseIn"])
    types["StartEnvironmentResponseOut"] = t.struct(
        {
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartEnvironmentResponseOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["AuthorizeEnvironmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentResponseIn"])
    types["AuthorizeEnvironmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentResponseOut"])
    types["AddPublicKeyResponseIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyResponseIn"]
    )
    types["AddPublicKeyResponseOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AuthorizeEnvironmentMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentMetadataIn"])
    types["AuthorizeEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentMetadataOut"])

    functions = {}
    functions["usersEnvironmentsAddPublicKey"] = cloudshell.post(
        "v1/{name}:authorize",
        t.struct(
            {
                "name": t.string().optional(),
                "idToken": t.string().optional(),
                "accessToken": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsRemovePublicKey"] = cloudshell.post(
        "v1/{name}:authorize",
        t.struct(
            {
                "name": t.string().optional(),
                "idToken": t.string().optional(),
                "accessToken": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsGet"] = cloudshell.post(
        "v1/{name}:authorize",
        t.struct(
            {
                "name": t.string().optional(),
                "idToken": t.string().optional(),
                "accessToken": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsStart"] = cloudshell.post(
        "v1/{name}:authorize",
        t.struct(
            {
                "name": t.string().optional(),
                "idToken": t.string().optional(),
                "accessToken": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsAuthorize"] = cloudshell.post(
        "v1/{name}:authorize",
        t.struct(
            {
                "name": t.string().optional(),
                "idToken": t.string().optional(),
                "accessToken": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = cloudshell.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudshell.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = cloudshell.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = cloudshell.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudshell",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
