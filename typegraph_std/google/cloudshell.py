from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudshell() -> Import:
    cloudshell = HTTPRuntime("https://cloudshell.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudshell_1_ErrorResponse",
        "EnvironmentIn": "_cloudshell_2_EnvironmentIn",
        "EnvironmentOut": "_cloudshell_3_EnvironmentOut",
        "AuthorizeEnvironmentResponseIn": "_cloudshell_4_AuthorizeEnvironmentResponseIn",
        "AuthorizeEnvironmentResponseOut": "_cloudshell_5_AuthorizeEnvironmentResponseOut",
        "RemovePublicKeyMetadataIn": "_cloudshell_6_RemovePublicKeyMetadataIn",
        "RemovePublicKeyMetadataOut": "_cloudshell_7_RemovePublicKeyMetadataOut",
        "EmptyIn": "_cloudshell_8_EmptyIn",
        "EmptyOut": "_cloudshell_9_EmptyOut",
        "StartEnvironmentRequestIn": "_cloudshell_10_StartEnvironmentRequestIn",
        "StartEnvironmentRequestOut": "_cloudshell_11_StartEnvironmentRequestOut",
        "RemovePublicKeyRequestIn": "_cloudshell_12_RemovePublicKeyRequestIn",
        "RemovePublicKeyRequestOut": "_cloudshell_13_RemovePublicKeyRequestOut",
        "StartEnvironmentResponseIn": "_cloudshell_14_StartEnvironmentResponseIn",
        "StartEnvironmentResponseOut": "_cloudshell_15_StartEnvironmentResponseOut",
        "AuthorizeEnvironmentRequestIn": "_cloudshell_16_AuthorizeEnvironmentRequestIn",
        "AuthorizeEnvironmentRequestOut": "_cloudshell_17_AuthorizeEnvironmentRequestOut",
        "DeleteEnvironmentMetadataIn": "_cloudshell_18_DeleteEnvironmentMetadataIn",
        "DeleteEnvironmentMetadataOut": "_cloudshell_19_DeleteEnvironmentMetadataOut",
        "CancelOperationRequestIn": "_cloudshell_20_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudshell_21_CancelOperationRequestOut",
        "StatusIn": "_cloudshell_22_StatusIn",
        "StatusOut": "_cloudshell_23_StatusOut",
        "AuthorizeEnvironmentMetadataIn": "_cloudshell_24_AuthorizeEnvironmentMetadataIn",
        "AuthorizeEnvironmentMetadataOut": "_cloudshell_25_AuthorizeEnvironmentMetadataOut",
        "ListOperationsResponseIn": "_cloudshell_26_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudshell_27_ListOperationsResponseOut",
        "AddPublicKeyResponseIn": "_cloudshell_28_AddPublicKeyResponseIn",
        "AddPublicKeyResponseOut": "_cloudshell_29_AddPublicKeyResponseOut",
        "AddPublicKeyRequestIn": "_cloudshell_30_AddPublicKeyRequestIn",
        "AddPublicKeyRequestOut": "_cloudshell_31_AddPublicKeyRequestOut",
        "AddPublicKeyMetadataIn": "_cloudshell_32_AddPublicKeyMetadataIn",
        "AddPublicKeyMetadataOut": "_cloudshell_33_AddPublicKeyMetadataOut",
        "CreateEnvironmentMetadataIn": "_cloudshell_34_CreateEnvironmentMetadataIn",
        "CreateEnvironmentMetadataOut": "_cloudshell_35_CreateEnvironmentMetadataOut",
        "StartEnvironmentMetadataIn": "_cloudshell_36_StartEnvironmentMetadataIn",
        "StartEnvironmentMetadataOut": "_cloudshell_37_StartEnvironmentMetadataOut",
        "RemovePublicKeyResponseIn": "_cloudshell_38_RemovePublicKeyResponseIn",
        "RemovePublicKeyResponseOut": "_cloudshell_39_RemovePublicKeyResponseOut",
        "OperationIn": "_cloudshell_40_OperationIn",
        "OperationOut": "_cloudshell_41_OperationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EnvironmentIn"] = t.struct(
        {"dockerImage": t.string(), "name": t.string().optional()}
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "sshPort": t.integer().optional(),
            "dockerImage": t.string(),
            "sshUsername": t.string().optional(),
            "webHost": t.string().optional(),
            "sshHost": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "publicKeys": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["AuthorizeEnvironmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentResponseIn"])
    types["AuthorizeEnvironmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentResponseOut"])
    types["RemovePublicKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyMetadataIn"]
    )
    types["RemovePublicKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["RemovePublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["RemovePublicKeyRequestIn"]
    )
    types["RemovePublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemovePublicKeyRequestOut"])
    types["StartEnvironmentResponseIn"] = t.struct(
        {"environment": t.proxy(renames["EnvironmentIn"]).optional()}
    ).named(renames["StartEnvironmentResponseIn"])
    types["StartEnvironmentResponseOut"] = t.struct(
        {
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartEnvironmentResponseOut"])
    types["AuthorizeEnvironmentRequestIn"] = t.struct(
        {
            "idToken": t.string().optional(),
            "expireTime": t.string().optional(),
            "accessToken": t.string().optional(),
        }
    ).named(renames["AuthorizeEnvironmentRequestIn"])
    types["AuthorizeEnvironmentRequestOut"] = t.struct(
        {
            "idToken": t.string().optional(),
            "expireTime": t.string().optional(),
            "accessToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizeEnvironmentRequestOut"])
    types["DeleteEnvironmentMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteEnvironmentMetadataIn"]
    )
    types["DeleteEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteEnvironmentMetadataOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["AuthorizeEnvironmentMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentMetadataIn"])
    types["AuthorizeEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentMetadataOut"])
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
    types["AddPublicKeyResponseIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyResponseIn"]
    )
    types["AddPublicKeyResponseOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyResponseOut"])
    types["AddPublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyRequestIn"]
    )
    types["AddPublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyRequestOut"])
    types["AddPublicKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddPublicKeyMetadataIn"]
    )
    types["AddPublicKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddPublicKeyMetadataOut"])
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
    types["RemovePublicKeyResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyResponseIn"]
    )
    types["RemovePublicKeyResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])

    functions = {}
    functions["operationsDelete"] = cloudshell.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = cloudshell.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = cloudshell.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudshell.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsRemovePublicKey"] = cloudshell.post(
        "v1/{environment}:addPublicKey",
        t.struct(
            {
                "environment": t.string().optional(),
                "key": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsGet"] = cloudshell.post(
        "v1/{environment}:addPublicKey",
        t.struct(
            {
                "environment": t.string().optional(),
                "key": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsStart"] = cloudshell.post(
        "v1/{environment}:addPublicKey",
        t.struct(
            {
                "environment": t.string().optional(),
                "key": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsAuthorize"] = cloudshell.post(
        "v1/{environment}:addPublicKey",
        t.struct(
            {
                "environment": t.string().optional(),
                "key": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersEnvironmentsAddPublicKey"] = cloudshell.post(
        "v1/{environment}:addPublicKey",
        t.struct(
            {
                "environment": t.string().optional(),
                "key": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudshell",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
