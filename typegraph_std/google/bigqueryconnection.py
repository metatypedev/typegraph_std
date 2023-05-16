from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_bigqueryconnection() -> Import:
    bigqueryconnection = HTTPRuntime("https://bigqueryconnection.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryconnection_1_ErrorResponse",
        "TestIamPermissionsRequestIn": "_bigqueryconnection_2_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigqueryconnection_3_TestIamPermissionsRequestOut",
        "ListConnectionsResponseIn": "_bigqueryconnection_4_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_bigqueryconnection_5_ListConnectionsResponseOut",
        "GetPolicyOptionsIn": "_bigqueryconnection_6_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigqueryconnection_7_GetPolicyOptionsOut",
        "SetIamPolicyRequestIn": "_bigqueryconnection_8_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigqueryconnection_9_SetIamPolicyRequestOut",
        "AuditConfigIn": "_bigqueryconnection_10_AuditConfigIn",
        "AuditConfigOut": "_bigqueryconnection_11_AuditConfigOut",
        "GetIamPolicyRequestIn": "_bigqueryconnection_12_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigqueryconnection_13_GetIamPolicyRequestOut",
        "BindingIn": "_bigqueryconnection_14_BindingIn",
        "BindingOut": "_bigqueryconnection_15_BindingOut",
        "ConnectionIn": "_bigqueryconnection_16_ConnectionIn",
        "ConnectionOut": "_bigqueryconnection_17_ConnectionOut",
        "ExprIn": "_bigqueryconnection_18_ExprIn",
        "ExprOut": "_bigqueryconnection_19_ExprOut",
        "EmptyIn": "_bigqueryconnection_20_EmptyIn",
        "EmptyOut": "_bigqueryconnection_21_EmptyOut",
        "AuditLogConfigIn": "_bigqueryconnection_22_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigqueryconnection_23_AuditLogConfigOut",
        "ConnectionCredentialIn": "_bigqueryconnection_24_ConnectionCredentialIn",
        "ConnectionCredentialOut": "_bigqueryconnection_25_ConnectionCredentialOut",
        "CloudSqlPropertiesIn": "_bigqueryconnection_26_CloudSqlPropertiesIn",
        "CloudSqlPropertiesOut": "_bigqueryconnection_27_CloudSqlPropertiesOut",
        "CloudSqlCredentialIn": "_bigqueryconnection_28_CloudSqlCredentialIn",
        "CloudSqlCredentialOut": "_bigqueryconnection_29_CloudSqlCredentialOut",
        "TestIamPermissionsResponseIn": "_bigqueryconnection_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigqueryconnection_31_TestIamPermissionsResponseOut",
        "PolicyIn": "_bigqueryconnection_32_PolicyIn",
        "PolicyOut": "_bigqueryconnection_33_PolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListConnectionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
        }
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
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
    types["ConnectionIn"] = t.struct(
        {
            "friendlyName": t.string().optional(),
            "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "hasCredential": t.boolean().optional(),
            "friendlyName": t.string().optional(),
            "cloudSql": t.proxy(renames["CloudSqlPropertiesOut"]).optional(),
            "description": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "creationTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ConnectionCredentialIn"] = t.struct(
        {"cloudSql": t.proxy(renames["CloudSqlCredentialIn"]).optional()}
    ).named(renames["ConnectionCredentialIn"])
    types["ConnectionCredentialOut"] = t.struct(
        {
            "cloudSql": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionCredentialOut"])
    types["CloudSqlPropertiesIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
            "type": t.string().optional(),
            "credential": t.proxy(renames["CloudSqlCredentialIn"]).optional(),
        }
    ).named(renames["CloudSqlPropertiesIn"])
    types["CloudSqlPropertiesOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
            "type": t.string().optional(),
            "serviceAccountId": t.string().optional(),
            "credential": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlPropertiesOut"])
    types["CloudSqlCredentialIn"] = t.struct(
        {"username": t.string().optional(), "password": t.string().optional()}
    ).named(renames["CloudSqlCredentialIn"])
    types["CloudSqlCredentialOut"] = t.struct(
        {
            "username": t.string().optional(),
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlCredentialOut"])
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
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])

    functions = {}
    functions["projectsLocationsConnectionsList"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsTestIamPermissions"
    ] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsGet"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsPatch"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsSetIamPolicy"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsCreate"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsUpdateCredential"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsDelete"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsGetIamPolicy"] = bigqueryconnection.post(
        "v1beta1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigqueryconnection",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
