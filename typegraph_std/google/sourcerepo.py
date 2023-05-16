from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_sourcerepo() -> Import:
    sourcerepo = HTTPRuntime("https://sourcerepo.googleapis.com/")

    renames = {
        "ErrorResponse": "_sourcerepo_1_ErrorResponse",
        "AuditConfigIn": "_sourcerepo_2_AuditConfigIn",
        "AuditConfigOut": "_sourcerepo_3_AuditConfigOut",
        "StatusIn": "_sourcerepo_4_StatusIn",
        "StatusOut": "_sourcerepo_5_StatusOut",
        "TestIamPermissionsResponseIn": "_sourcerepo_6_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_sourcerepo_7_TestIamPermissionsResponseOut",
        "PubsubConfigIn": "_sourcerepo_8_PubsubConfigIn",
        "PubsubConfigOut": "_sourcerepo_9_PubsubConfigOut",
        "SyncRepoMetadataIn": "_sourcerepo_10_SyncRepoMetadataIn",
        "SyncRepoMetadataOut": "_sourcerepo_11_SyncRepoMetadataOut",
        "RepoIn": "_sourcerepo_12_RepoIn",
        "RepoOut": "_sourcerepo_13_RepoOut",
        "ListReposResponseIn": "_sourcerepo_14_ListReposResponseIn",
        "ListReposResponseOut": "_sourcerepo_15_ListReposResponseOut",
        "SyncRepoRequestIn": "_sourcerepo_16_SyncRepoRequestIn",
        "SyncRepoRequestOut": "_sourcerepo_17_SyncRepoRequestOut",
        "AuditLogConfigIn": "_sourcerepo_18_AuditLogConfigIn",
        "AuditLogConfigOut": "_sourcerepo_19_AuditLogConfigOut",
        "UpdateRepoRequestIn": "_sourcerepo_20_UpdateRepoRequestIn",
        "UpdateRepoRequestOut": "_sourcerepo_21_UpdateRepoRequestOut",
        "ProjectConfigIn": "_sourcerepo_22_ProjectConfigIn",
        "ProjectConfigOut": "_sourcerepo_23_ProjectConfigOut",
        "ExprIn": "_sourcerepo_24_ExprIn",
        "ExprOut": "_sourcerepo_25_ExprOut",
        "PolicyIn": "_sourcerepo_26_PolicyIn",
        "PolicyOut": "_sourcerepo_27_PolicyOut",
        "MirrorConfigIn": "_sourcerepo_28_MirrorConfigIn",
        "MirrorConfigOut": "_sourcerepo_29_MirrorConfigOut",
        "UpdateProjectConfigRequestIn": "_sourcerepo_30_UpdateProjectConfigRequestIn",
        "UpdateProjectConfigRequestOut": "_sourcerepo_31_UpdateProjectConfigRequestOut",
        "TestIamPermissionsRequestIn": "_sourcerepo_32_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_sourcerepo_33_TestIamPermissionsRequestOut",
        "OperationIn": "_sourcerepo_34_OperationIn",
        "OperationOut": "_sourcerepo_35_OperationOut",
        "BindingIn": "_sourcerepo_36_BindingIn",
        "BindingOut": "_sourcerepo_37_BindingOut",
        "SetIamPolicyRequestIn": "_sourcerepo_38_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_sourcerepo_39_SetIamPolicyRequestOut",
        "EmptyIn": "_sourcerepo_40_EmptyIn",
        "EmptyOut": "_sourcerepo_41_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PubsubConfigIn"] = t.struct(
        {
            "topic": t.string().optional(),
            "messageFormat": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
        }
    ).named(renames["PubsubConfigIn"])
    types["PubsubConfigOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "messageFormat": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubConfigOut"])
    types["SyncRepoMetadataIn"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SyncRepoMetadataIn"])
    types["SyncRepoMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "startTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncRepoMetadataOut"])
    types["RepoIn"] = t.struct(
        {
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "size": t.string().optional(),
            "url": t.string().optional(),
            "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RepoIn"])
    types["RepoOut"] = t.struct(
        {
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "size": t.string().optional(),
            "url": t.string().optional(),
            "mirrorConfig": t.proxy(renames["MirrorConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoOut"])
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
    types["SyncRepoRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SyncRepoRequestIn"]
    )
    types["SyncRepoRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SyncRepoRequestOut"])
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
    types["ProjectConfigIn"] = t.struct(
        {
            "enablePrivateKeyCheck": t.boolean().optional(),
            "name": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ProjectConfigIn"])
    types["ProjectConfigOut"] = t.struct(
        {
            "enablePrivateKeyCheck": t.boolean().optional(),
            "name": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectConfigOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["MirrorConfigIn"] = t.struct(
        {
            "webhookId": t.string().optional(),
            "url": t.string().optional(),
            "deployKeyId": t.string().optional(),
        }
    ).named(renames["MirrorConfigIn"])
    types["MirrorConfigOut"] = t.struct(
        {
            "webhookId": t.string().optional(),
            "url": t.string().optional(),
            "deployKeyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MirrorConfigOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

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
    functions["projectsReposGetIamPolicy"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposPatch"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposSetIamPolicy"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposGet"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposDelete"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposCreate"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposList"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposSync"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReposTestIamPermissions"] = sourcerepo.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sourcerepo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
