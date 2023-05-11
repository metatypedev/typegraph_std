from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_gameservices() -> Import:
    gameservices = HTTPRuntime("https://gameservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_gameservices_1_ErrorResponse",
        "CancelOperationRequestIn": "_gameservices_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gameservices_3_CancelOperationRequestOut",
        "AuditConfigIn": "_gameservices_4_AuditConfigIn",
        "AuditConfigOut": "_gameservices_5_AuditConfigOut",
        "ConditionIn": "_gameservices_6_ConditionIn",
        "ConditionOut": "_gameservices_7_ConditionOut",
        "EmptyIn": "_gameservices_8_EmptyIn",
        "EmptyOut": "_gameservices_9_EmptyOut",
        "ListOperationsResponseIn": "_gameservices_10_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gameservices_11_ListOperationsResponseOut",
        "ListLocationsResponseIn": "_gameservices_12_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gameservices_13_ListLocationsResponseOut",
        "LogConfigIn": "_gameservices_14_LogConfigIn",
        "LogConfigOut": "_gameservices_15_LogConfigOut",
        "ExprIn": "_gameservices_16_ExprIn",
        "ExprOut": "_gameservices_17_ExprOut",
        "TestIamPermissionsResponseIn": "_gameservices_18_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gameservices_19_TestIamPermissionsResponseOut",
        "DataAccessOptionsIn": "_gameservices_20_DataAccessOptionsIn",
        "DataAccessOptionsOut": "_gameservices_21_DataAccessOptionsOut",
        "LocationIn": "_gameservices_22_LocationIn",
        "LocationOut": "_gameservices_23_LocationOut",
        "CustomFieldIn": "_gameservices_24_CustomFieldIn",
        "CustomFieldOut": "_gameservices_25_CustomFieldOut",
        "AuditLogConfigIn": "_gameservices_26_AuditLogConfigIn",
        "AuditLogConfigOut": "_gameservices_27_AuditLogConfigOut",
        "TestIamPermissionsRequestIn": "_gameservices_28_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gameservices_29_TestIamPermissionsRequestOut",
        "CloudAuditOptionsIn": "_gameservices_30_CloudAuditOptionsIn",
        "CloudAuditOptionsOut": "_gameservices_31_CloudAuditOptionsOut",
        "BindingIn": "_gameservices_32_BindingIn",
        "BindingOut": "_gameservices_33_BindingOut",
        "StatusIn": "_gameservices_34_StatusIn",
        "StatusOut": "_gameservices_35_StatusOut",
        "AuthorizationLoggingOptionsIn": "_gameservices_36_AuthorizationLoggingOptionsIn",
        "AuthorizationLoggingOptionsOut": "_gameservices_37_AuthorizationLoggingOptionsOut",
        "OperationIn": "_gameservices_38_OperationIn",
        "OperationOut": "_gameservices_39_OperationOut",
        "CounterOptionsIn": "_gameservices_40_CounterOptionsIn",
        "CounterOptionsOut": "_gameservices_41_CounterOptionsOut",
        "PolicyIn": "_gameservices_42_PolicyIn",
        "PolicyOut": "_gameservices_43_PolicyOut",
        "RuleIn": "_gameservices_44_RuleIn",
        "RuleOut": "_gameservices_45_RuleOut",
        "SetIamPolicyRequestIn": "_gameservices_46_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gameservices_47_SetIamPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["ConditionIn"] = t.struct(
        {
            "svc": t.string().optional(),
            "op": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "sys": t.string().optional(),
            "iam": t.string().optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "svc": t.string().optional(),
            "op": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "sys": t.string().optional(),
            "iam": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LogConfigIn"] = t.struct(
        {
            "counter": t.proxy(renames["CounterOptionsIn"]).optional(),
            "cloudAudit": t.proxy(renames["CloudAuditOptionsIn"]).optional(),
            "dataAccess": t.proxy(renames["DataAccessOptionsIn"]).optional(),
        }
    ).named(renames["LogConfigIn"])
    types["LogConfigOut"] = t.struct(
        {
            "counter": t.proxy(renames["CounterOptionsOut"]).optional(),
            "cloudAudit": t.proxy(renames["CloudAuditOptionsOut"]).optional(),
            "dataAccess": t.proxy(renames["DataAccessOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogConfigOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["DataAccessOptionsIn"] = t.struct({"logMode": t.string()}).named(
        renames["DataAccessOptionsIn"]
    )
    types["DataAccessOptionsOut"] = t.struct(
        {"logMode": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DataAccessOptionsOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "ignoreChildExemptions": t.boolean(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "ignoreChildExemptions": t.boolean(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["AuthorizationLoggingOptionsIn"] = t.struct(
        {"permissionType": t.string().optional()}
    ).named(renames["AuthorizationLoggingOptionsIn"])
    types["AuthorizationLoggingOptionsOut"] = t.struct(
        {
            "permissionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationLoggingOptionsOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["CounterOptionsIn"] = t.struct(
        {
            "customFields": t.array(t.proxy(renames["CustomFieldIn"])).optional(),
            "field": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["CounterOptionsIn"])
    types["CounterOptionsOut"] = t.struct(
        {
            "customFields": t.array(t.proxy(renames["CustomFieldOut"])).optional(),
            "field": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CounterOptionsOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["RuleIn"] = t.struct(
        {
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "description": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "notIn": t.array(t.string()).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigIn"])).optional(),
            "in": t.array(t.string()).optional(),
            "action": t.string(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "description": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "notIn": t.array(t.string()).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigOut"])).optional(),
            "in": t.array(t.string()).optional(),
            "action": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
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
    functions["projectsLocationsGameServerDeploymentsSetIamPolicy"] = gameservices.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGameServerDeploymentsTestIamPermissions"
    ] = gameservices.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
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
        importer="gameservices", renames=renames, types=types, functions=functions
    )
