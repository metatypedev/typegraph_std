from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_bigqueryconnection():
    bigqueryconnection = HTTPRuntime("https://bigqueryconnection.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryconnection_1_ErrorResponse",
        "GetPolicyOptionsIn": "_bigqueryconnection_2_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigqueryconnection_3_GetPolicyOptionsOut",
        "ConnectionIn": "_bigqueryconnection_4_ConnectionIn",
        "ConnectionOut": "_bigqueryconnection_5_ConnectionOut",
        "ListConnectionsResponseIn": "_bigqueryconnection_6_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_bigqueryconnection_7_ListConnectionsResponseOut",
        "ExprIn": "_bigqueryconnection_8_ExprIn",
        "ExprOut": "_bigqueryconnection_9_ExprOut",
        "EmptyIn": "_bigqueryconnection_10_EmptyIn",
        "EmptyOut": "_bigqueryconnection_11_EmptyOut",
        "ConnectionCredentialIn": "_bigqueryconnection_12_ConnectionCredentialIn",
        "ConnectionCredentialOut": "_bigqueryconnection_13_ConnectionCredentialOut",
        "CloudSqlCredentialIn": "_bigqueryconnection_14_CloudSqlCredentialIn",
        "CloudSqlCredentialOut": "_bigqueryconnection_15_CloudSqlCredentialOut",
        "AuditConfigIn": "_bigqueryconnection_16_AuditConfigIn",
        "AuditConfigOut": "_bigqueryconnection_17_AuditConfigOut",
        "GetIamPolicyRequestIn": "_bigqueryconnection_18_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigqueryconnection_19_GetIamPolicyRequestOut",
        "PolicyIn": "_bigqueryconnection_20_PolicyIn",
        "PolicyOut": "_bigqueryconnection_21_PolicyOut",
        "CloudSqlPropertiesIn": "_bigqueryconnection_22_CloudSqlPropertiesIn",
        "CloudSqlPropertiesOut": "_bigqueryconnection_23_CloudSqlPropertiesOut",
        "TestIamPermissionsRequestIn": "_bigqueryconnection_24_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigqueryconnection_25_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_bigqueryconnection_26_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigqueryconnection_27_TestIamPermissionsResponseOut",
        "BindingIn": "_bigqueryconnection_28_BindingIn",
        "BindingOut": "_bigqueryconnection_29_BindingOut",
        "SetIamPolicyRequestIn": "_bigqueryconnection_30_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigqueryconnection_31_SetIamPolicyRequestOut",
        "AuditLogConfigIn": "_bigqueryconnection_32_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigqueryconnection_33_AuditLogConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
            "lastModifiedTime": t.string().optional(),
            "friendlyName": t.string().optional(),
            "hasCredential": t.boolean().optional(),
            "creationTime": t.string().optional(),
            "cloudSql": t.proxy(renames["CloudSqlPropertiesOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
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
    types["ConnectionCredentialIn"] = t.struct(
        {"cloudSql": t.proxy(renames["CloudSqlCredentialIn"]).optional()}
    ).named(renames["ConnectionCredentialIn"])
    types["ConnectionCredentialOut"] = t.struct(
        {
            "cloudSql": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionCredentialOut"])
    types["CloudSqlCredentialIn"] = t.struct(
        {"password": t.string().optional(), "username": t.string().optional()}
    ).named(renames["CloudSqlCredentialIn"])
    types["CloudSqlCredentialOut"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlCredentialOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["CloudSqlPropertiesIn"] = t.struct(
        {
            "credential": t.proxy(renames["CloudSqlCredentialIn"]).optional(),
            "database": t.string().optional(),
            "type": t.string().optional(),
            "instanceId": t.string().optional(),
        }
    ).named(renames["CloudSqlPropertiesIn"])
    types["CloudSqlPropertiesOut"] = t.struct(
        {
            "credential": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "database": t.string().optional(),
            "serviceAccountId": t.string().optional(),
            "type": t.string().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlPropertiesOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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

    functions = {}
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
