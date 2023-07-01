from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_oslogin():
    oslogin = HTTPRuntime("https://oslogin.googleapis.com/")

    renames = {
        "ErrorResponse": "_oslogin_1_ErrorResponse",
        "SshPublicKeyIn": "_oslogin_2_SshPublicKeyIn",
        "SshPublicKeyOut": "_oslogin_3_SshPublicKeyOut",
        "PosixAccountIn": "_oslogin_4_PosixAccountIn",
        "PosixAccountOut": "_oslogin_5_PosixAccountOut",
        "ImportSshPublicKeyResponseIn": "_oslogin_6_ImportSshPublicKeyResponseIn",
        "ImportSshPublicKeyResponseOut": "_oslogin_7_ImportSshPublicKeyResponseOut",
        "LoginProfileIn": "_oslogin_8_LoginProfileIn",
        "LoginProfileOut": "_oslogin_9_LoginProfileOut",
        "EmptyIn": "_oslogin_10_EmptyIn",
        "EmptyOut": "_oslogin_11_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SshPublicKeyIn"] = t.struct(
        {"key": t.string().optional(), "expirationTimeUsec": t.string().optional()}
    ).named(renames["SshPublicKeyIn"])
    types["SshPublicKeyOut"] = t.struct(
        {
            "key": t.string().optional(),
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "expirationTimeUsec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SshPublicKeyOut"])
    types["PosixAccountIn"] = t.struct(
        {
            "homeDirectory": t.string().optional(),
            "gecos": t.string().optional(),
            "username": t.string().optional(),
            "primary": t.boolean().optional(),
            "gid": t.string().optional(),
            "operatingSystemType": t.string().optional(),
            "uid": t.string().optional(),
            "shell": t.string().optional(),
            "systemId": t.string().optional(),
        }
    ).named(renames["PosixAccountIn"])
    types["PosixAccountOut"] = t.struct(
        {
            "homeDirectory": t.string().optional(),
            "gecos": t.string().optional(),
            "name": t.string().optional(),
            "accountId": t.string().optional(),
            "username": t.string().optional(),
            "primary": t.boolean().optional(),
            "gid": t.string().optional(),
            "operatingSystemType": t.string().optional(),
            "uid": t.string().optional(),
            "shell": t.string().optional(),
            "systemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosixAccountOut"])
    types["ImportSshPublicKeyResponseIn"] = t.struct(
        {
            "details": t.string().optional(),
            "loginProfile": t.proxy(renames["LoginProfileIn"]).optional(),
        }
    ).named(renames["ImportSshPublicKeyResponseIn"])
    types["ImportSshPublicKeyResponseOut"] = t.struct(
        {
            "details": t.string().optional(),
            "loginProfile": t.proxy(renames["LoginProfileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportSshPublicKeyResponseOut"])
    types["LoginProfileIn"] = t.struct(
        {
            "name": t.string(),
            "sshPublicKeys": t.struct({"_": t.string().optional()}).optional(),
            "posixAccounts": t.array(t.proxy(renames["PosixAccountIn"])).optional(),
        }
    ).named(renames["LoginProfileIn"])
    types["LoginProfileOut"] = t.struct(
        {
            "name": t.string(),
            "sshPublicKeys": t.struct({"_": t.string().optional()}).optional(),
            "posixAccounts": t.array(t.proxy(renames["PosixAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoginProfileOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["usersGetLoginProfile"] = oslogin.post(
        "v1/{parent}:importSshPublicKey",
        t.struct(
            {
                "projectId": t.string().optional(),
                "parent": t.string(),
                "key": t.string().optional(),
                "expirationTimeUsec": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportSshPublicKeyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersImportSshPublicKey"] = oslogin.post(
        "v1/{parent}:importSshPublicKey",
        t.struct(
            {
                "projectId": t.string().optional(),
                "parent": t.string(),
                "key": t.string().optional(),
                "expirationTimeUsec": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ImportSshPublicKeyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysDelete"] = oslogin.post(
        "v1/{parent}/sshPublicKeys",
        t.struct(
            {
                "parent": t.string(),
                "key": t.string().optional(),
                "expirationTimeUsec": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SshPublicKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysPatch"] = oslogin.post(
        "v1/{parent}/sshPublicKeys",
        t.struct(
            {
                "parent": t.string(),
                "key": t.string().optional(),
                "expirationTimeUsec": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SshPublicKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysGet"] = oslogin.post(
        "v1/{parent}/sshPublicKeys",
        t.struct(
            {
                "parent": t.string(),
                "key": t.string().optional(),
                "expirationTimeUsec": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SshPublicKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysCreate"] = oslogin.post(
        "v1/{parent}/sshPublicKeys",
        t.struct(
            {
                "parent": t.string(),
                "key": t.string().optional(),
                "expirationTimeUsec": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SshPublicKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersProjectsDelete"] = oslogin.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="oslogin", renames=renames, types=Box(types), functions=Box(functions)
    )
