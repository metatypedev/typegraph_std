from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudshell() -> Import:
    cloudshell = HTTPRuntime("https://cloudshell.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudshell_1_ErrorResponse",
        "AuthorizeEnvironmentResponseIn": "_cloudshell_2_AuthorizeEnvironmentResponseIn",
        "AuthorizeEnvironmentResponseOut": "_cloudshell_3_AuthorizeEnvironmentResponseOut",
        "RemovePublicKeyRequestIn": "_cloudshell_4_RemovePublicKeyRequestIn",
        "RemovePublicKeyRequestOut": "_cloudshell_5_RemovePublicKeyRequestOut",
        "AddPublicKeyResponseIn": "_cloudshell_6_AddPublicKeyResponseIn",
        "AddPublicKeyResponseOut": "_cloudshell_7_AddPublicKeyResponseOut",
        "StartEnvironmentRequestIn": "_cloudshell_8_StartEnvironmentRequestIn",
        "StartEnvironmentRequestOut": "_cloudshell_9_StartEnvironmentRequestOut",
        "RemovePublicKeyMetadataIn": "_cloudshell_10_RemovePublicKeyMetadataIn",
        "RemovePublicKeyMetadataOut": "_cloudshell_11_RemovePublicKeyMetadataOut",
        "RemovePublicKeyResponseIn": "_cloudshell_12_RemovePublicKeyResponseIn",
        "RemovePublicKeyResponseOut": "_cloudshell_13_RemovePublicKeyResponseOut",
        "StatusIn": "_cloudshell_14_StatusIn",
        "StatusOut": "_cloudshell_15_StatusOut",
        "EnvironmentIn": "_cloudshell_16_EnvironmentIn",
        "EnvironmentOut": "_cloudshell_17_EnvironmentOut",
        "EmptyIn": "_cloudshell_18_EmptyIn",
        "EmptyOut": "_cloudshell_19_EmptyOut",
        "ListOperationsResponseIn": "_cloudshell_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudshell_21_ListOperationsResponseOut",
        "CancelOperationRequestIn": "_cloudshell_22_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_cloudshell_23_CancelOperationRequestOut",
        "DeleteEnvironmentMetadataIn": "_cloudshell_24_DeleteEnvironmentMetadataIn",
        "DeleteEnvironmentMetadataOut": "_cloudshell_25_DeleteEnvironmentMetadataOut",
        "StartEnvironmentMetadataIn": "_cloudshell_26_StartEnvironmentMetadataIn",
        "StartEnvironmentMetadataOut": "_cloudshell_27_StartEnvironmentMetadataOut",
        "CreateEnvironmentMetadataIn": "_cloudshell_28_CreateEnvironmentMetadataIn",
        "CreateEnvironmentMetadataOut": "_cloudshell_29_CreateEnvironmentMetadataOut",
        "OperationIn": "_cloudshell_30_OperationIn",
        "OperationOut": "_cloudshell_31_OperationOut",
        "AddPublicKeyMetadataIn": "_cloudshell_32_AddPublicKeyMetadataIn",
        "AddPublicKeyMetadataOut": "_cloudshell_33_AddPublicKeyMetadataOut",
        "StartEnvironmentResponseIn": "_cloudshell_34_StartEnvironmentResponseIn",
        "StartEnvironmentResponseOut": "_cloudshell_35_StartEnvironmentResponseOut",
        "AddPublicKeyRequestIn": "_cloudshell_36_AddPublicKeyRequestIn",
        "AddPublicKeyRequestOut": "_cloudshell_37_AddPublicKeyRequestOut",
        "AuthorizeEnvironmentMetadataIn": "_cloudshell_38_AuthorizeEnvironmentMetadataIn",
        "AuthorizeEnvironmentMetadataOut": "_cloudshell_39_AuthorizeEnvironmentMetadataOut",
        "AuthorizeEnvironmentRequestIn": "_cloudshell_40_AuthorizeEnvironmentRequestIn",
        "AuthorizeEnvironmentRequestOut": "_cloudshell_41_AuthorizeEnvironmentRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AuthorizeEnvironmentResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentResponseIn"])
    types["AuthorizeEnvironmentResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentResponseOut"])
    types["RemovePublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["RemovePublicKeyRequestIn"]
    )
    types["RemovePublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemovePublicKeyRequestOut"])
    types["AddPublicKeyResponseIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyResponseIn"]
    )
    types["AddPublicKeyResponseOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyResponseOut"])
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
    types["RemovePublicKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyMetadataIn"]
    )
    types["RemovePublicKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyMetadataOut"])
    types["RemovePublicKeyResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemovePublicKeyResponseIn"]
    )
    types["RemovePublicKeyResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemovePublicKeyResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EnvironmentIn"] = t.struct(
        {"dockerImage": t.string(), "name": t.string().optional()}
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "dockerImage": t.string(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "sshUsername": t.string().optional(),
            "publicKeys": t.array(t.string()).optional(),
            "sshHost": t.string().optional(),
            "state": t.string().optional(),
            "webHost": t.string().optional(),
            "sshPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["CreateEnvironmentMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateEnvironmentMetadataIn"]
    )
    types["CreateEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateEnvironmentMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AddPublicKeyRequestIn"] = t.struct({"key": t.string().optional()}).named(
        renames["AddPublicKeyRequestIn"]
    )
    types["AddPublicKeyRequestOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddPublicKeyRequestOut"])
    types["AuthorizeEnvironmentMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AuthorizeEnvironmentMetadataIn"])
    types["AuthorizeEnvironmentMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AuthorizeEnvironmentMetadataOut"])
    types["AuthorizeEnvironmentRequestIn"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "idToken": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["AuthorizeEnvironmentRequestIn"])
    types["AuthorizeEnvironmentRequestOut"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "idToken": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizeEnvironmentRequestOut"])

    functions = {}
    functions["operationsList"] = cloudshell.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudshell.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = cloudshell.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = cloudshell.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
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
