from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_sourcerepo() -> Import:
    sourcerepo = HTTPRuntime("https://sourcerepo.googleapis.com/")

    renames = {
        "ErrorResponse": "_sourcerepo_1_ErrorResponse",
        "StatusIn": "_sourcerepo_2_StatusIn",
        "StatusOut": "_sourcerepo_3_StatusOut",
        "TestIamPermissionsRequestIn": "_sourcerepo_4_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_sourcerepo_5_TestIamPermissionsRequestOut",
        "ExprIn": "_sourcerepo_6_ExprIn",
        "ExprOut": "_sourcerepo_7_ExprOut",
        "ListReposResponseIn": "_sourcerepo_8_ListReposResponseIn",
        "ListReposResponseOut": "_sourcerepo_9_ListReposResponseOut",
        "UpdateRepoRequestIn": "_sourcerepo_10_UpdateRepoRequestIn",
        "UpdateRepoRequestOut": "_sourcerepo_11_UpdateRepoRequestOut",
        "AuditConfigIn": "_sourcerepo_12_AuditConfigIn",
        "AuditConfigOut": "_sourcerepo_13_AuditConfigOut",
        "BindingIn": "_sourcerepo_14_BindingIn",
        "BindingOut": "_sourcerepo_15_BindingOut",
        "EmptyIn": "_sourcerepo_16_EmptyIn",
        "EmptyOut": "_sourcerepo_17_EmptyOut",
        "AuditLogConfigIn": "_sourcerepo_18_AuditLogConfigIn",
        "AuditLogConfigOut": "_sourcerepo_19_AuditLogConfigOut",
        "ProjectConfigIn": "_sourcerepo_20_ProjectConfigIn",
        "ProjectConfigOut": "_sourcerepo_21_ProjectConfigOut",
        "PolicyIn": "_sourcerepo_22_PolicyIn",
        "PolicyOut": "_sourcerepo_23_PolicyOut",
        "SyncRepoRequestIn": "_sourcerepo_24_SyncRepoRequestIn",
        "SyncRepoRequestOut": "_sourcerepo_25_SyncRepoRequestOut",
        "PubsubConfigIn": "_sourcerepo_26_PubsubConfigIn",
        "PubsubConfigOut": "_sourcerepo_27_PubsubConfigOut",
        "UpdateProjectConfigRequestIn": "_sourcerepo_28_UpdateProjectConfigRequestIn",
        "UpdateProjectConfigRequestOut": "_sourcerepo_29_UpdateProjectConfigRequestOut",
        "TestIamPermissionsResponseIn": "_sourcerepo_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_sourcerepo_31_TestIamPermissionsResponseOut",
        "OperationIn": "_sourcerepo_32_OperationIn",
        "OperationOut": "_sourcerepo_33_OperationOut",
        "SetIamPolicyRequestIn": "_sourcerepo_34_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_sourcerepo_35_SetIamPolicyRequestOut",
        "RepoIn": "_sourcerepo_36_RepoIn",
        "RepoOut": "_sourcerepo_37_RepoOut",
        "SyncRepoMetadataIn": "_sourcerepo_38_SyncRepoMetadataIn",
        "SyncRepoMetadataOut": "_sourcerepo_39_SyncRepoMetadataOut",
        "MirrorConfigIn": "_sourcerepo_40_MirrorConfigIn",
        "MirrorConfigOut": "_sourcerepo_41_MirrorConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ListReposResponseIn"] = t.struct(
        {
            "repos": t.array(t.proxy(renames["RepoIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReposResponseIn"])
    types["ListReposResponseOut"] = t.struct(
        {
            "repos": t.array(t.proxy(renames["RepoOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReposResponseOut"])
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
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["SyncRepoRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SyncRepoRequestIn"]
    )
    types["SyncRepoRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SyncRepoRequestOut"])
    types["PubsubConfigIn"] = t.struct(
        {
            "messageFormat": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["PubsubConfigIn"])
    types["PubsubConfigOut"] = t.struct(
        {
            "messageFormat": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubConfigOut"])
    types["UpdateProjectConfigRequestIn"] = t.struct(
        {
            "projectConfig": t.proxy(renames["ProjectConfigIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["UpdateProjectConfigRequestIn"])
    types["UpdateProjectConfigRequestOut"] = t.struct(
        {
            "projectConfig": t.proxy(renames["ProjectConfigOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateProjectConfigRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["RepoIn"] = t.struct(
        {
            "url": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "size": t.string().optional(),
            "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
        }
    ).named(renames["RepoIn"])
    types["RepoOut"] = t.struct(
        {
            "url": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "size": t.string().optional(),
            "mirrorConfig": t.proxy(renames["MirrorConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoOut"])
    types["SyncRepoMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "statusMessage": t.string().optional(),
        }
    ).named(renames["SyncRepoMetadataIn"])
    types["SyncRepoMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncRepoMetadataOut"])
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

    functions = {}
    functions["projectsGetConfig"] = sourcerepo.patch(
        "v1/{name}/config",
        t.struct(
            {
                "name": t.string().optional(),
                "projectConfig": t.proxy(renames["ProjectConfigIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateConfig"] = sourcerepo.patch(
        "v1/{name}/config",
        t.struct(
            {
                "name": t.string().optional(),
                "projectConfig": t.proxy(renames["ProjectConfigIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposPatch"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposDelete"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposGetIamPolicy"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposTestIamPermissions"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposList"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposGet"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposSync"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposSetIamPolicy"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposCreate"] = sourcerepo.post(
        "v1/{parent}/repos",
        t.struct(
            {
                "parent": t.string().optional(),
                "url": t.string().optional(),
                "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "size": t.string().optional(),
                "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sourcerepo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
