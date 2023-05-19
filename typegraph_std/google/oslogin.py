from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_oslogin() -> Import:
    oslogin = HTTPRuntime("https://oslogin.googleapis.com/")

    renames = {
        "ErrorResponse": "_oslogin_1_ErrorResponse",
        "EmptyIn": "_oslogin_2_EmptyIn",
        "EmptyOut": "_oslogin_3_EmptyOut",
        "LoginProfileIn": "_oslogin_4_LoginProfileIn",
        "LoginProfileOut": "_oslogin_5_LoginProfileOut",
        "ImportSshPublicKeyResponseIn": "_oslogin_6_ImportSshPublicKeyResponseIn",
        "ImportSshPublicKeyResponseOut": "_oslogin_7_ImportSshPublicKeyResponseOut",
        "SshPublicKeyIn": "_oslogin_8_SshPublicKeyIn",
        "SshPublicKeyOut": "_oslogin_9_SshPublicKeyOut",
        "PosixAccountIn": "_oslogin_10_PosixAccountIn",
        "PosixAccountOut": "_oslogin_11_PosixAccountOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LoginProfileIn"] = t.struct(
        {
            "sshPublicKeys": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "posixAccounts": t.array(t.proxy(renames["PosixAccountIn"])).optional(),
        }
    ).named(renames["LoginProfileIn"])
    types["LoginProfileOut"] = t.struct(
        {
            "sshPublicKeys": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "posixAccounts": t.array(t.proxy(renames["PosixAccountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoginProfileOut"])
    types["ImportSshPublicKeyResponseIn"] = t.struct(
        {
            "loginProfile": t.proxy(renames["LoginProfileIn"]).optional(),
            "details": t.string().optional(),
        }
    ).named(renames["ImportSshPublicKeyResponseIn"])
    types["ImportSshPublicKeyResponseOut"] = t.struct(
        {
            "loginProfile": t.proxy(renames["LoginProfileOut"]).optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportSshPublicKeyResponseOut"])
    types["SshPublicKeyIn"] = t.struct(
        {"expirationTimeUsec": t.string().optional(), "key": t.string().optional()}
    ).named(renames["SshPublicKeyIn"])
    types["SshPublicKeyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "fingerprint": t.string().optional(),
            "expirationTimeUsec": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SshPublicKeyOut"])
    types["PosixAccountIn"] = t.struct(
        {
            "gecos": t.string().optional(),
            "username": t.string().optional(),
            "gid": t.string().optional(),
            "uid": t.string().optional(),
            "homeDirectory": t.string().optional(),
            "primary": t.boolean().optional(),
            "systemId": t.string().optional(),
            "shell": t.string().optional(),
            "operatingSystemType": t.string().optional(),
        }
    ).named(renames["PosixAccountIn"])
    types["PosixAccountOut"] = t.struct(
        {
            "gecos": t.string().optional(),
            "username": t.string().optional(),
            "gid": t.string().optional(),
            "uid": t.string().optional(),
            "accountId": t.string().optional(),
            "homeDirectory": t.string().optional(),
            "name": t.string().optional(),
            "primary": t.boolean().optional(),
            "systemId": t.string().optional(),
            "shell": t.string().optional(),
            "operatingSystemType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosixAccountOut"])

    functions = {}
    functions["usersImportSshPublicKey"] = oslogin.get(
        "v1/{name}/loginProfile",
        t.struct(
            {
                "name": t.string(),
                "systemId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LoginProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGetLoginProfile"] = oslogin.get(
        "v1/{name}/loginProfile",
        t.struct(
            {
                "name": t.string(),
                "systemId": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LoginProfileOut"]),
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
    functions["usersSshPublicKeysGet"] = oslogin.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysPatch"] = oslogin.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysCreate"] = oslogin.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysDelete"] = oslogin.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="oslogin", renames=renames, types=Box(types), functions=Box(functions)
    )
