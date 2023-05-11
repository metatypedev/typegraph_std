from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_sourcerepo() -> Import:
    sourcerepo = HTTPRuntime("https://sourcerepo.googleapis.com/")

    renames = {
        "ErrorResponse": "_sourcerepo_1_ErrorResponse",
        "ListReposResponseIn": "_sourcerepo_2_ListReposResponseIn",
        "ListReposResponseOut": "_sourcerepo_3_ListReposResponseOut",
        "SetIamPolicyRequestIn": "_sourcerepo_4_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_sourcerepo_5_SetIamPolicyRequestOut",
        "RepoIn": "_sourcerepo_6_RepoIn",
        "RepoOut": "_sourcerepo_7_RepoOut",
        "MirrorConfigIn": "_sourcerepo_8_MirrorConfigIn",
        "MirrorConfigOut": "_sourcerepo_9_MirrorConfigOut",
        "AuditConfigIn": "_sourcerepo_10_AuditConfigIn",
        "AuditConfigOut": "_sourcerepo_11_AuditConfigOut",
        "OperationIn": "_sourcerepo_12_OperationIn",
        "OperationOut": "_sourcerepo_13_OperationOut",
        "TestIamPermissionsResponseIn": "_sourcerepo_14_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_sourcerepo_15_TestIamPermissionsResponseOut",
        "PolicyIn": "_sourcerepo_16_PolicyIn",
        "PolicyOut": "_sourcerepo_17_PolicyOut",
        "BindingIn": "_sourcerepo_18_BindingIn",
        "BindingOut": "_sourcerepo_19_BindingOut",
        "UpdateRepoRequestIn": "_sourcerepo_20_UpdateRepoRequestIn",
        "UpdateRepoRequestOut": "_sourcerepo_21_UpdateRepoRequestOut",
        "ExprIn": "_sourcerepo_22_ExprIn",
        "ExprOut": "_sourcerepo_23_ExprOut",
        "EmptyIn": "_sourcerepo_24_EmptyIn",
        "EmptyOut": "_sourcerepo_25_EmptyOut",
        "StatusIn": "_sourcerepo_26_StatusIn",
        "StatusOut": "_sourcerepo_27_StatusOut",
        "SyncRepoMetadataIn": "_sourcerepo_28_SyncRepoMetadataIn",
        "SyncRepoMetadataOut": "_sourcerepo_29_SyncRepoMetadataOut",
        "SyncRepoRequestIn": "_sourcerepo_30_SyncRepoRequestIn",
        "SyncRepoRequestOut": "_sourcerepo_31_SyncRepoRequestOut",
        "UpdateProjectConfigRequestIn": "_sourcerepo_32_UpdateProjectConfigRequestIn",
        "UpdateProjectConfigRequestOut": "_sourcerepo_33_UpdateProjectConfigRequestOut",
        "TestIamPermissionsRequestIn": "_sourcerepo_34_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_sourcerepo_35_TestIamPermissionsRequestOut",
        "AuditLogConfigIn": "_sourcerepo_36_AuditLogConfigIn",
        "AuditLogConfigOut": "_sourcerepo_37_AuditLogConfigOut",
        "PubsubConfigIn": "_sourcerepo_38_PubsubConfigIn",
        "PubsubConfigOut": "_sourcerepo_39_PubsubConfigOut",
        "ProjectConfigIn": "_sourcerepo_40_ProjectConfigIn",
        "ProjectConfigOut": "_sourcerepo_41_ProjectConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListReposResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repos": t.array(t.proxy(renames["RepoIn"])).optional(),
        }
    ).named(renames["ListReposResponseIn"])
    types["ListReposResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "repos": t.array(t.proxy(renames["RepoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReposResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["RepoIn"] = t.struct(
        {
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "url": t.string().optional(),
            "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
            "size": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RepoIn"])
    types["RepoOut"] = t.struct(
        {
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "url": t.string().optional(),
            "mirrorConfig": t.proxy(renames["MirrorConfigOut"]).optional(),
            "size": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoOut"])
    types["MirrorConfigIn"] = t.struct(
        {
            "url": t.string().optional(),
            "deployKeyId": t.string().optional(),
            "webhookId": t.string().optional(),
        }
    ).named(renames["MirrorConfigIn"])
    types["MirrorConfigOut"] = t.struct(
        {
            "url": t.string().optional(),
            "deployKeyId": t.string().optional(),
            "webhookId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MirrorConfigOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["UpdateRepoRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "repo": t.proxy(renames["RepoIn"]).optional(),
        }
    ).named(renames["UpdateRepoRequestIn"])
    types["UpdateRepoRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "repo": t.proxy(renames["RepoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateRepoRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["SyncRepoMetadataIn"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["SyncRepoMetadataIn"])
    types["SyncRepoMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncRepoMetadataOut"])
    types["SyncRepoRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SyncRepoRequestIn"]
    )
    types["SyncRepoRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SyncRepoRequestOut"])
    types["UpdateProjectConfigRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "projectConfig": t.proxy(renames["ProjectConfigIn"]).optional(),
        }
    ).named(renames["UpdateProjectConfigRequestIn"])
    types["UpdateProjectConfigRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "projectConfig": t.proxy(renames["ProjectConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateProjectConfigRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["PubsubConfigIn"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "topic": t.string().optional(),
            "messageFormat": t.string().optional(),
        }
    ).named(renames["PubsubConfigIn"])
    types["PubsubConfigOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "topic": t.string().optional(),
            "messageFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubConfigOut"])
    types["ProjectConfigIn"] = t.struct(
        {
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "enablePrivateKeyCheck": t.boolean().optional(),
        }
    ).named(renames["ProjectConfigIn"])
    types["ProjectConfigOut"] = t.struct(
        {
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "enablePrivateKeyCheck": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectConfigOut"])

    functions = {}
    functions["projectsUpdateConfig"] = sourcerepo.get(
        "v1/{name}/config",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetConfig"] = sourcerepo.get(
        "v1/{name}/config",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposGet"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposCreate"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposList"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposPatch"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposSync"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposTestIamPermissions"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposDelete"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposGetIamPolicy"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposSetIamPolicy"] = sourcerepo.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sourcerepo", renames=renames, types=types, functions=functions
    )
