from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_bigqueryconnection() -> Import:
    bigqueryconnection = HTTPRuntime("https://bigqueryconnection.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryconnection_1_ErrorResponse",
        "ListConnectionsResponseIn": "_bigqueryconnection_2_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_bigqueryconnection_3_ListConnectionsResponseOut",
        "GetIamPolicyRequestIn": "_bigqueryconnection_4_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigqueryconnection_5_GetIamPolicyRequestOut",
        "SetIamPolicyRequestIn": "_bigqueryconnection_6_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigqueryconnection_7_SetIamPolicyRequestOut",
        "CloudSqlCredentialIn": "_bigqueryconnection_8_CloudSqlCredentialIn",
        "CloudSqlCredentialOut": "_bigqueryconnection_9_CloudSqlCredentialOut",
        "PolicyIn": "_bigqueryconnection_10_PolicyIn",
        "PolicyOut": "_bigqueryconnection_11_PolicyOut",
        "BindingIn": "_bigqueryconnection_12_BindingIn",
        "BindingOut": "_bigqueryconnection_13_BindingOut",
        "TestIamPermissionsResponseIn": "_bigqueryconnection_14_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigqueryconnection_15_TestIamPermissionsResponseOut",
        "GetPolicyOptionsIn": "_bigqueryconnection_16_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigqueryconnection_17_GetPolicyOptionsOut",
        "ConnectionIn": "_bigqueryconnection_18_ConnectionIn",
        "ConnectionOut": "_bigqueryconnection_19_ConnectionOut",
        "ConnectionCredentialIn": "_bigqueryconnection_20_ConnectionCredentialIn",
        "ConnectionCredentialOut": "_bigqueryconnection_21_ConnectionCredentialOut",
        "EmptyIn": "_bigqueryconnection_22_EmptyIn",
        "EmptyOut": "_bigqueryconnection_23_EmptyOut",
        "CloudSqlPropertiesIn": "_bigqueryconnection_24_CloudSqlPropertiesIn",
        "CloudSqlPropertiesOut": "_bigqueryconnection_25_CloudSqlPropertiesOut",
        "ExprIn": "_bigqueryconnection_26_ExprIn",
        "ExprOut": "_bigqueryconnection_27_ExprOut",
        "AuditLogConfigIn": "_bigqueryconnection_28_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigqueryconnection_29_AuditLogConfigOut",
        "AuditConfigIn": "_bigqueryconnection_30_AuditConfigIn",
        "AuditConfigOut": "_bigqueryconnection_31_AuditConfigOut",
        "TestIamPermissionsRequestIn": "_bigqueryconnection_32_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigqueryconnection_33_TestIamPermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
            "name": t.string().optional(),
            "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "friendlyName": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "creationTime": t.string().optional(),
            "hasCredential": t.boolean().optional(),
            "name": t.string().optional(),
            "cloudSql": t.proxy(renames["CloudSqlPropertiesOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["ConnectionCredentialIn"] = t.struct(
        {"cloudSql": t.proxy(renames["CloudSqlCredentialIn"]).optional()}
    ).named(renames["ConnectionCredentialIn"])
    types["ConnectionCredentialOut"] = t.struct(
        {
            "cloudSql": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionCredentialOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CloudSqlPropertiesIn"] = t.struct(
        {
            "credential": t.proxy(renames["CloudSqlCredentialIn"]).optional(),
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CloudSqlPropertiesIn"])
    types["CloudSqlPropertiesOut"] = t.struct(
        {
            "credential": t.proxy(renames["CloudSqlCredentialOut"]).optional(),
            "serviceAccountId": t.string().optional(),
            "instanceId": t.string().optional(),
            "database": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSqlPropertiesOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])

    functions = {}
    functions["projectsLocationsConnectionsGetIamPolicy"] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsTestIamPermissions"
    ] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsGet"] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsDelete"] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsUpdateCredential"
    ] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsSetIamPolicy"] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsList"] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsCreate"] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsPatch"] = bigqueryconnection.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "friendlyName": t.string().optional(),
                "cloudSql": t.proxy(renames["CloudSqlPropertiesIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigqueryconnection", renames=renames, types=types, functions=functions
    )
