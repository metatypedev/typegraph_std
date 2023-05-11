from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_oslogin() -> Import:
    oslogin = HTTPRuntime("https://oslogin.googleapis.com/")

    renames = {
        "ErrorResponse": "_oslogin_1_ErrorResponse",
        "SshPublicKeyIn": "_oslogin_2_SshPublicKeyIn",
        "SshPublicKeyOut": "_oslogin_3_SshPublicKeyOut",
        "ImportSshPublicKeyResponseIn": "_oslogin_4_ImportSshPublicKeyResponseIn",
        "ImportSshPublicKeyResponseOut": "_oslogin_5_ImportSshPublicKeyResponseOut",
        "EmptyIn": "_oslogin_6_EmptyIn",
        "EmptyOut": "_oslogin_7_EmptyOut",
        "PosixAccountIn": "_oslogin_8_PosixAccountIn",
        "PosixAccountOut": "_oslogin_9_PosixAccountOut",
        "LoginProfileIn": "_oslogin_10_LoginProfileIn",
        "LoginProfileOut": "_oslogin_11_LoginProfileOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SshPublicKeyIn"] = t.struct(
        {"expirationTimeUsec": t.string().optional(), "key": t.string().optional()}
    ).named(renames["SshPublicKeyIn"])
    types["SshPublicKeyOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "expirationTimeUsec": t.string().optional(),
            "key": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SshPublicKeyOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PosixAccountIn"] = t.struct(
        {
            "username": t.string().optional(),
            "primary": t.boolean().optional(),
            "systemId": t.string().optional(),
            "operatingSystemType": t.string().optional(),
            "uid": t.string().optional(),
            "homeDirectory": t.string().optional(),
            "gecos": t.string().optional(),
            "shell": t.string().optional(),
            "gid": t.string().optional(),
        }
    ).named(renames["PosixAccountIn"])
    types["PosixAccountOut"] = t.struct(
        {
            "username": t.string().optional(),
            "primary": t.boolean().optional(),
            "systemId": t.string().optional(),
            "operatingSystemType": t.string().optional(),
            "uid": t.string().optional(),
            "accountId": t.string().optional(),
            "homeDirectory": t.string().optional(),
            "name": t.string().optional(),
            "gecos": t.string().optional(),
            "shell": t.string().optional(),
            "gid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PosixAccountOut"])
    types["LoginProfileIn"] = t.struct(
        {
            "name": t.string(),
            "posixAccounts": t.array(t.proxy(renames["PosixAccountIn"])).optional(),
            "sshPublicKeys": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LoginProfileIn"])
    types["LoginProfileOut"] = t.struct(
        {
            "name": t.string(),
            "posixAccounts": t.array(t.proxy(renames["PosixAccountOut"])).optional(),
            "sshPublicKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoginProfileOut"])

    functions = {}
    functions["usersImportSshPublicKey"] = oslogin.get(
        "v1/{name}/loginProfile",
        t.struct(
            {
                "name": t.string(),
                "projectId": t.string().optional(),
                "systemId": t.string().optional(),
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
                "projectId": t.string().optional(),
                "systemId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LoginProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysDelete"] = oslogin.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SshPublicKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysCreate"] = oslogin.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SshPublicKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysPatch"] = oslogin.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SshPublicKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSshPublicKeysGet"] = oslogin.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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

    return Import(importer="oslogin", renames=renames, types=types, functions=functions)
