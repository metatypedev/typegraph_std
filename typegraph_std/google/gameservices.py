from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gameservices() -> Import:
    gameservices = HTTPRuntime("https://gameservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_gameservices_1_ErrorResponse",
        "AuditLogConfigIn": "_gameservices_2_AuditLogConfigIn",
        "AuditLogConfigOut": "_gameservices_3_AuditLogConfigOut",
        "SetIamPolicyRequestIn": "_gameservices_4_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gameservices_5_SetIamPolicyRequestOut",
        "StatusIn": "_gameservices_6_StatusIn",
        "StatusOut": "_gameservices_7_StatusOut",
        "LogConfigIn": "_gameservices_8_LogConfigIn",
        "LogConfigOut": "_gameservices_9_LogConfigOut",
        "PolicyIn": "_gameservices_10_PolicyIn",
        "PolicyOut": "_gameservices_11_PolicyOut",
        "LocationIn": "_gameservices_12_LocationIn",
        "LocationOut": "_gameservices_13_LocationOut",
        "ExprIn": "_gameservices_14_ExprIn",
        "ExprOut": "_gameservices_15_ExprOut",
        "ListOperationsResponseIn": "_gameservices_16_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gameservices_17_ListOperationsResponseOut",
        "ConditionIn": "_gameservices_18_ConditionIn",
        "ConditionOut": "_gameservices_19_ConditionOut",
        "CustomFieldIn": "_gameservices_20_CustomFieldIn",
        "CustomFieldOut": "_gameservices_21_CustomFieldOut",
        "EmptyIn": "_gameservices_22_EmptyIn",
        "EmptyOut": "_gameservices_23_EmptyOut",
        "TestIamPermissionsResponseIn": "_gameservices_24_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gameservices_25_TestIamPermissionsResponseOut",
        "TestIamPermissionsRequestIn": "_gameservices_26_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gameservices_27_TestIamPermissionsRequestOut",
        "ListLocationsResponseIn": "_gameservices_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gameservices_29_ListLocationsResponseOut",
        "AuditConfigIn": "_gameservices_30_AuditConfigIn",
        "AuditConfigOut": "_gameservices_31_AuditConfigOut",
        "CounterOptionsIn": "_gameservices_32_CounterOptionsIn",
        "CounterOptionsOut": "_gameservices_33_CounterOptionsOut",
        "DataAccessOptionsIn": "_gameservices_34_DataAccessOptionsIn",
        "DataAccessOptionsOut": "_gameservices_35_DataAccessOptionsOut",
        "BindingIn": "_gameservices_36_BindingIn",
        "BindingOut": "_gameservices_37_BindingOut",
        "CloudAuditOptionsIn": "_gameservices_38_CloudAuditOptionsIn",
        "CloudAuditOptionsOut": "_gameservices_39_CloudAuditOptionsOut",
        "AuthorizationLoggingOptionsIn": "_gameservices_40_AuthorizationLoggingOptionsIn",
        "AuthorizationLoggingOptionsOut": "_gameservices_41_AuthorizationLoggingOptionsOut",
        "RuleIn": "_gameservices_42_RuleIn",
        "RuleOut": "_gameservices_43_RuleOut",
        "OperationIn": "_gameservices_44_OperationIn",
        "OperationOut": "_gameservices_45_OperationOut",
        "CancelOperationRequestIn": "_gameservices_46_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gameservices_47_CancelOperationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "ignoreChildExemptions": t.boolean(),
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "ignoreChildExemptions": t.boolean(),
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
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
    types["LogConfigIn"] = t.struct(
        {
            "cloudAudit": t.proxy(renames["CloudAuditOptionsIn"]).optional(),
            "dataAccess": t.proxy(renames["DataAccessOptionsIn"]).optional(),
            "counter": t.proxy(renames["CounterOptionsIn"]).optional(),
        }
    ).named(renames["LogConfigIn"])
    types["LogConfigOut"] = t.struct(
        {
            "cloudAudit": t.proxy(renames["CloudAuditOptionsOut"]).optional(),
            "dataAccess": t.proxy(renames["DataAccessOptionsOut"]).optional(),
            "counter": t.proxy(renames["CounterOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ConditionIn"] = t.struct(
        {
            "sys": t.string().optional(),
            "svc": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "iam": t.string().optional(),
            "op": t.string().optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "sys": t.string().optional(),
            "svc": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "iam": t.string().optional(),
            "op": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["CustomFieldIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["CustomFieldIn"])
    types["CustomFieldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomFieldOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["CounterOptionsIn"] = t.struct(
        {
            "metric": t.string().optional(),
            "field": t.string().optional(),
            "customFields": t.array(t.proxy(renames["CustomFieldIn"])).optional(),
        }
    ).named(renames["CounterOptionsIn"])
    types["CounterOptionsOut"] = t.struct(
        {
            "metric": t.string().optional(),
            "field": t.string().optional(),
            "customFields": t.array(t.proxy(renames["CustomFieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterOptionsOut"])
    types["DataAccessOptionsIn"] = t.struct({"logMode": t.string()}).named(
        renames["DataAccessOptionsIn"]
    )
    types["DataAccessOptionsOut"] = t.struct(
        {"logMode": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DataAccessOptionsOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "bindingId": t.string(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "bindingId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["AuthorizationLoggingOptionsIn"] = t.struct(
        {"permissionType": t.string().optional()}
    ).named(renames["AuthorizationLoggingOptionsIn"])
    types["AuthorizationLoggingOptionsOut"] = t.struct(
        {
            "permissionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationLoggingOptionsOut"])
    types["RuleIn"] = t.struct(
        {
            "in": t.array(t.string()).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigIn"])).optional(),
            "action": t.string(),
            "notIn": t.array(t.string()).optional(),
            "permissions": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "in": t.array(t.string()).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigOut"])).optional(),
            "action": t.string(),
            "notIn": t.array(t.string()).optional(),
            "permissions": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])

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
    functions[
        "projectsLocationsGameServerDeploymentsTestIamPermissions"
    ] = gameservices.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGameServerDeploymentsSetIamPolicy"] = gameservices.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGameServerDeploymentsGetIamPolicy"] = gameservices.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = gameservices.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = gameservices.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = gameservices.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = gameservices.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gameservices",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
