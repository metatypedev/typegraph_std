from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gameservices():
    gameservices = HTTPRuntime("https://gameservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_gameservices_1_ErrorResponse",
        "CloudAuditOptionsIn": "_gameservices_2_CloudAuditOptionsIn",
        "CloudAuditOptionsOut": "_gameservices_3_CloudAuditOptionsOut",
        "ListLocationsResponseIn": "_gameservices_4_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gameservices_5_ListLocationsResponseOut",
        "PolicyIn": "_gameservices_6_PolicyIn",
        "PolicyOut": "_gameservices_7_PolicyOut",
        "EmptyIn": "_gameservices_8_EmptyIn",
        "EmptyOut": "_gameservices_9_EmptyOut",
        "ConditionIn": "_gameservices_10_ConditionIn",
        "ConditionOut": "_gameservices_11_ConditionOut",
        "SetIamPolicyRequestIn": "_gameservices_12_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gameservices_13_SetIamPolicyRequestOut",
        "LogConfigIn": "_gameservices_14_LogConfigIn",
        "LogConfigOut": "_gameservices_15_LogConfigOut",
        "DataAccessOptionsIn": "_gameservices_16_DataAccessOptionsIn",
        "DataAccessOptionsOut": "_gameservices_17_DataAccessOptionsOut",
        "TestIamPermissionsRequestIn": "_gameservices_18_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gameservices_19_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_gameservices_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gameservices_21_TestIamPermissionsResponseOut",
        "CounterOptionsIn": "_gameservices_22_CounterOptionsIn",
        "CounterOptionsOut": "_gameservices_23_CounterOptionsOut",
        "RuleIn": "_gameservices_24_RuleIn",
        "RuleOut": "_gameservices_25_RuleOut",
        "AuditLogConfigIn": "_gameservices_26_AuditLogConfigIn",
        "AuditLogConfigOut": "_gameservices_27_AuditLogConfigOut",
        "AuditConfigIn": "_gameservices_28_AuditConfigIn",
        "AuditConfigOut": "_gameservices_29_AuditConfigOut",
        "StatusIn": "_gameservices_30_StatusIn",
        "StatusOut": "_gameservices_31_StatusOut",
        "LocationIn": "_gameservices_32_LocationIn",
        "LocationOut": "_gameservices_33_LocationOut",
        "CancelOperationRequestIn": "_gameservices_34_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gameservices_35_CancelOperationRequestOut",
        "ListOperationsResponseIn": "_gameservices_36_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gameservices_37_ListOperationsResponseOut",
        "ExprIn": "_gameservices_38_ExprIn",
        "ExprOut": "_gameservices_39_ExprOut",
        "OperationIn": "_gameservices_40_OperationIn",
        "OperationOut": "_gameservices_41_OperationOut",
        "AuthorizationLoggingOptionsIn": "_gameservices_42_AuthorizationLoggingOptionsIn",
        "AuthorizationLoggingOptionsOut": "_gameservices_43_AuthorizationLoggingOptionsOut",
        "BindingIn": "_gameservices_44_BindingIn",
        "BindingOut": "_gameservices_45_BindingOut",
        "CustomFieldIn": "_gameservices_46_CustomFieldIn",
        "CustomFieldOut": "_gameservices_47_CustomFieldOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CloudAuditOptionsIn"] = t.struct(
        {
            "logName": t.string().optional(),
            "authorizationLoggingOptions": t.proxy(
                renames["AuthorizationLoggingOptionsIn"]
            ).optional(),
        }
    ).named(renames["CloudAuditOptionsIn"])
    types["CloudAuditOptionsOut"] = t.struct(
        {
            "logName": t.string().optional(),
            "authorizationLoggingOptions": t.proxy(
                renames["AuthorizationLoggingOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudAuditOptionsOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ConditionIn"] = t.struct(
        {
            "iam": t.string().optional(),
            "op": t.string().optional(),
            "svc": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "sys": t.string().optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "iam": t.string().optional(),
            "op": t.string().optional(),
            "svc": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "sys": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
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
    types["LogConfigIn"] = t.struct(
        {
            "dataAccess": t.proxy(renames["DataAccessOptionsIn"]).optional(),
            "cloudAudit": t.proxy(renames["CloudAuditOptionsIn"]).optional(),
            "counter": t.proxy(renames["CounterOptionsIn"]).optional(),
        }
    ).named(renames["LogConfigIn"])
    types["LogConfigOut"] = t.struct(
        {
            "dataAccess": t.proxy(renames["DataAccessOptionsOut"]).optional(),
            "cloudAudit": t.proxy(renames["CloudAuditOptionsOut"]).optional(),
            "counter": t.proxy(renames["CounterOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogConfigOut"])
    types["DataAccessOptionsIn"] = t.struct({"logMode": t.string()}).named(
        renames["DataAccessOptionsIn"]
    )
    types["DataAccessOptionsOut"] = t.struct(
        {"logMode": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DataAccessOptionsOut"])
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
    types["CounterOptionsIn"] = t.struct(
        {
            "field": t.string().optional(),
            "metric": t.string().optional(),
            "customFields": t.array(t.proxy(renames["CustomFieldIn"])).optional(),
        }
    ).named(renames["CounterOptionsIn"])
    types["CounterOptionsOut"] = t.struct(
        {
            "field": t.string().optional(),
            "metric": t.string().optional(),
            "customFields": t.array(t.proxy(renames["CustomFieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterOptionsOut"])
    types["RuleIn"] = t.struct(
        {
            "action": t.string(),
            "notIn": t.array(t.string()).optional(),
            "in": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigIn"])).optional(),
            "permissions": t.array(t.string()).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "action": t.string(),
            "notIn": t.array(t.string()).optional(),
            "in": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigOut"])).optional(),
            "permissions": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "ignoreChildExemptions": t.boolean(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "ignoreChildExemptions": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["AuthorizationLoggingOptionsIn"] = t.struct(
        {"permissionType": t.string().optional()}
    ).named(renames["AuthorizationLoggingOptionsIn"])
    types["AuthorizationLoggingOptionsOut"] = t.struct(
        {
            "permissionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationLoggingOptionsOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "bindingId": t.string(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "bindingId": t.string(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["CustomFieldIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["CustomFieldIn"])
    types["CustomFieldOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomFieldOut"])

    functions = {}
    functions["projectsLocationsList"] = gameservices.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = gameservices.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = gameservices.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = gameservices.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = gameservices.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = gameservices.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGameServerDeploymentsSetIamPolicy"] = gameservices.post(
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
    functions["projectsLocationsGameServerDeploymentsGetIamPolicy"] = gameservices.post(
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
    functions[
        "projectsLocationsGameServerDeploymentsTestIamPermissions"
    ] = gameservices.post(
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
        importer="gameservices",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
