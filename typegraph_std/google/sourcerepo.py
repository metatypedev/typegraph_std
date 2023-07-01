from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_sourcerepo():
    sourcerepo = HTTPRuntime("https://sourcerepo.googleapis.com/")

    renames = {
        "ErrorResponse": "_sourcerepo_1_ErrorResponse",
        "AuditLogConfigIn": "_sourcerepo_2_AuditLogConfigIn",
        "AuditLogConfigOut": "_sourcerepo_3_AuditLogConfigOut",
        "PolicyIn": "_sourcerepo_4_PolicyIn",
        "PolicyOut": "_sourcerepo_5_PolicyOut",
        "MirrorConfigIn": "_sourcerepo_6_MirrorConfigIn",
        "MirrorConfigOut": "_sourcerepo_7_MirrorConfigOut",
        "SyncRepoRequestIn": "_sourcerepo_8_SyncRepoRequestIn",
        "SyncRepoRequestOut": "_sourcerepo_9_SyncRepoRequestOut",
        "TestIamPermissionsRequestIn": "_sourcerepo_10_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_sourcerepo_11_TestIamPermissionsRequestOut",
        "SyncRepoMetadataIn": "_sourcerepo_12_SyncRepoMetadataIn",
        "SyncRepoMetadataOut": "_sourcerepo_13_SyncRepoMetadataOut",
        "UpdateProjectConfigRequestIn": "_sourcerepo_14_UpdateProjectConfigRequestIn",
        "UpdateProjectConfigRequestOut": "_sourcerepo_15_UpdateProjectConfigRequestOut",
        "BindingIn": "_sourcerepo_16_BindingIn",
        "BindingOut": "_sourcerepo_17_BindingOut",
        "UpdateRepoRequestIn": "_sourcerepo_18_UpdateRepoRequestIn",
        "UpdateRepoRequestOut": "_sourcerepo_19_UpdateRepoRequestOut",
        "RepoIn": "_sourcerepo_20_RepoIn",
        "RepoOut": "_sourcerepo_21_RepoOut",
        "ExprIn": "_sourcerepo_22_ExprIn",
        "ExprOut": "_sourcerepo_23_ExprOut",
        "PubsubConfigIn": "_sourcerepo_24_PubsubConfigIn",
        "PubsubConfigOut": "_sourcerepo_25_PubsubConfigOut",
        "StatusIn": "_sourcerepo_26_StatusIn",
        "StatusOut": "_sourcerepo_27_StatusOut",
        "SetIamPolicyRequestIn": "_sourcerepo_28_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_sourcerepo_29_SetIamPolicyRequestOut",
        "EmptyIn": "_sourcerepo_30_EmptyIn",
        "EmptyOut": "_sourcerepo_31_EmptyOut",
        "ListReposResponseIn": "_sourcerepo_32_ListReposResponseIn",
        "ListReposResponseOut": "_sourcerepo_33_ListReposResponseOut",
        "ProjectConfigIn": "_sourcerepo_34_ProjectConfigIn",
        "ProjectConfigOut": "_sourcerepo_35_ProjectConfigOut",
        "OperationIn": "_sourcerepo_36_OperationIn",
        "OperationOut": "_sourcerepo_37_OperationOut",
        "AuditConfigIn": "_sourcerepo_38_AuditConfigIn",
        "AuditConfigOut": "_sourcerepo_39_AuditConfigOut",
        "TestIamPermissionsResponseIn": "_sourcerepo_40_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_sourcerepo_41_TestIamPermissionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["MirrorConfigIn"] = t.struct(
        {
            "deployKeyId": t.string().optional(),
            "url": t.string().optional(),
            "webhookId": t.string().optional(),
        }
    ).named(renames["MirrorConfigIn"])
    types["MirrorConfigOut"] = t.struct(
        {
            "deployKeyId": t.string().optional(),
            "url": t.string().optional(),
            "webhookId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MirrorConfigOut"])
    types["SyncRepoRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SyncRepoRequestIn"]
    )
    types["SyncRepoRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SyncRepoRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["SyncRepoMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["SyncRepoMetadataIn"])
    types["SyncRepoMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SyncRepoMetadataOut"])
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
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
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
    types["RepoIn"] = t.struct(
        {
            "mirrorConfig": t.proxy(renames["MirrorConfigIn"]).optional(),
            "name": t.string().optional(),
            "size": t.string().optional(),
            "url": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RepoIn"])
    types["RepoOut"] = t.struct(
        {
            "mirrorConfig": t.proxy(renames["MirrorConfigOut"]).optional(),
            "name": t.string().optional(),
            "size": t.string().optional(),
            "url": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["ProjectConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "enablePrivateKeyCheck": t.boolean().optional(),
        }
    ).named(renames["ProjectConfigIn"])
    types["ProjectConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "pubsubConfigs": t.struct({"_": t.string().optional()}).optional(),
            "enablePrivateKeyCheck": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])

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
        importer="sourcerepo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
