from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_bigqueryconnection() -> Import:
    bigqueryconnection = HTTPRuntime("https://bigqueryconnection.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryconnection_1_ErrorResponse",
        "ExprIn": "_bigqueryconnection_2_ExprIn",
        "ExprOut": "_bigqueryconnection_3_ExprOut",
        "ConnectionIn": "_bigqueryconnection_4_ConnectionIn",
        "ConnectionOut": "_bigqueryconnection_5_ConnectionOut",
        "BindingIn": "_bigqueryconnection_6_BindingIn",
        "BindingOut": "_bigqueryconnection_7_BindingOut",
        "GetPolicyOptionsIn": "_bigqueryconnection_8_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigqueryconnection_9_GetPolicyOptionsOut",
        "ListConnectionsResponseIn": "_bigqueryconnection_10_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_bigqueryconnection_11_ListConnectionsResponseOut",
        "AuditConfigIn": "_bigqueryconnection_12_AuditConfigIn",
        "AuditConfigOut": "_bigqueryconnection_13_AuditConfigOut",
        "TestIamPermissionsRequestIn": "_bigqueryconnection_14_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigqueryconnection_15_TestIamPermissionsRequestOut",
        "SetIamPolicyRequestIn": "_bigqueryconnection_16_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigqueryconnection_17_SetIamPolicyRequestOut",
        "AuditLogConfigIn": "_bigqueryconnection_18_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigqueryconnection_19_AuditLogConfigOut",
        "CloudSqlCredentialIn": "_bigqueryconnection_20_CloudSqlCredentialIn",
        "CloudSqlCredentialOut": "_bigqueryconnection_21_CloudSqlCredentialOut",
        "EmptyIn": "_bigqueryconnection_22_EmptyIn",
        "EmptyOut": "_bigqueryconnection_23_EmptyOut",
        "CloudSqlPropertiesIn": "_bigqueryconnection_24_CloudSqlPropertiesIn",
        "CloudSqlPropertiesOut": "_bigqueryconnection_25_CloudSqlPropertiesOut",
        "PolicyIn": "_bigqueryconnection_26_PolicyIn",
        "PolicyOut": "_bigqueryconnection_27_PolicyOut",
        "ConnectionCredentialIn": "_bigqueryconnection_28_ConnectionCredentialIn",
        "ConnectionCredentialOut": "_bigqueryconnection_29_ConnectionCredentialOut",
        "TestIamPermissionsResponseIn": "_bigqueryconnection_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigqueryconnection_31_TestIamPermissionsResponseOut",
        "GetIamPolicyRequestIn": "_bigqueryconnection_32_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigqueryconnection_33_GetIamPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ConnectionIn"] = t.struct(
        {
            "friendlyName": t.string().optional(),
            "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "friendlyName": t.string().optional(),
            "hasCredential": t.boolean().optional(),
            "cloudSql": t.proxy(renames["CloudSqlPropertiesOut"]).optional(),
            "creationTime": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CloudSqlPropertiesIn"] = t.struct(
        {
            "type": t.string().optional(),
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
            "credential": t.proxy(renames["CloudSqlCredentialIn"]).optional(),
        }
    ).named(renames["CloudSqlPropertiesIn"])
    types["CloudSqlPropertiesOut"] = t.struct(
        {
            "type": t.string().optional(),
            "serviceAccountId": t.string().optional(),
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
            "credential": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlPropertiesOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ConnectionCredentialIn"] = t.struct(
        {"cloudSql": t.proxy(renames["CloudSqlCredentialIn"]).optional()}
    ).named(renames["ConnectionCredentialIn"])
    types["ConnectionCredentialOut"] = t.struct(
        {
            "cloudSql": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionCredentialOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])

    functions = {}
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
