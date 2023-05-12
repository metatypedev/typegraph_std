from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_gameservices() -> Import:
    gameservices = HTTPRuntime("https://gameservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_gameservices_1_ErrorResponse",
        "LogConfigIn": "_gameservices_2_LogConfigIn",
        "LogConfigOut": "_gameservices_3_LogConfigOut",
        "SetIamPolicyRequestIn": "_gameservices_4_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gameservices_5_SetIamPolicyRequestOut",
        "DataAccessOptionsIn": "_gameservices_6_DataAccessOptionsIn",
        "DataAccessOptionsOut": "_gameservices_7_DataAccessOptionsOut",
        "CustomFieldIn": "_gameservices_8_CustomFieldIn",
        "CustomFieldOut": "_gameservices_9_CustomFieldOut",
        "CounterOptionsIn": "_gameservices_10_CounterOptionsIn",
        "CounterOptionsOut": "_gameservices_11_CounterOptionsOut",
        "AuditLogConfigIn": "_gameservices_12_AuditLogConfigIn",
        "AuditLogConfigOut": "_gameservices_13_AuditLogConfigOut",
        "ListLocationsResponseIn": "_gameservices_14_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gameservices_15_ListLocationsResponseOut",
        "ConditionIn": "_gameservices_16_ConditionIn",
        "ConditionOut": "_gameservices_17_ConditionOut",
        "EmptyIn": "_gameservices_18_EmptyIn",
        "EmptyOut": "_gameservices_19_EmptyOut",
        "ListOperationsResponseIn": "_gameservices_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_gameservices_21_ListOperationsResponseOut",
        "CloudAuditOptionsIn": "_gameservices_22_CloudAuditOptionsIn",
        "CloudAuditOptionsOut": "_gameservices_23_CloudAuditOptionsOut",
        "LocationIn": "_gameservices_24_LocationIn",
        "LocationOut": "_gameservices_25_LocationOut",
        "CancelOperationRequestIn": "_gameservices_26_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_gameservices_27_CancelOperationRequestOut",
        "TestIamPermissionsRequestIn": "_gameservices_28_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gameservices_29_TestIamPermissionsRequestOut",
        "AuthorizationLoggingOptionsIn": "_gameservices_30_AuthorizationLoggingOptionsIn",
        "AuthorizationLoggingOptionsOut": "_gameservices_31_AuthorizationLoggingOptionsOut",
        "RuleIn": "_gameservices_32_RuleIn",
        "RuleOut": "_gameservices_33_RuleOut",
        "PolicyIn": "_gameservices_34_PolicyIn",
        "PolicyOut": "_gameservices_35_PolicyOut",
        "AuditConfigIn": "_gameservices_36_AuditConfigIn",
        "AuditConfigOut": "_gameservices_37_AuditConfigOut",
        "StatusIn": "_gameservices_38_StatusIn",
        "StatusOut": "_gameservices_39_StatusOut",
        "OperationIn": "_gameservices_40_OperationIn",
        "OperationOut": "_gameservices_41_OperationOut",
        "TestIamPermissionsResponseIn": "_gameservices_42_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gameservices_43_TestIamPermissionsResponseOut",
        "ExprIn": "_gameservices_44_ExprIn",
        "ExprOut": "_gameservices_45_ExprOut",
        "BindingIn": "_gameservices_46_BindingIn",
        "BindingOut": "_gameservices_47_BindingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DataAccessOptionsIn"] = t.struct({"logMode": t.string()}).named(
        renames["DataAccessOptionsIn"]
    )
    types["DataAccessOptionsOut"] = t.struct(
        {"logMode": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DataAccessOptionsOut"])
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
    types["ConditionIn"] = t.struct(
        {
            "svc": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "iam": t.string().optional(),
            "sys": t.string().optional(),
            "op": t.string().optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "svc": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "iam": t.string().optional(),
            "sys": t.string().optional(),
            "op": t.string().optional(),
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
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
            "action": t.string(),
            "notIn": t.array(t.string()).optional(),
            "in": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])).optional(),
            "permissions": t.array(t.string()).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "action": t.string(),
            "notIn": t.array(t.string()).optional(),
            "in": t.array(t.string()).optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])).optional(),
            "permissions": t.array(t.string()).optional(),
            "logConfig": t.array(t.proxy(renames["LogConfigOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "bindingId": t.string(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "bindingId": t.string(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])

    functions = {}
    functions["projectsLocationsGet"] = gameservices.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = gameservices.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = gameservices.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGameServerDeploymentsTestIamPermissions"
    ] = gameservices.post(
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
    functions["projectsLocationsGameServerDeploymentsGetIamPolicy"] = gameservices.post(
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
    functions["projectsLocationsGameServerDeploymentsSetIamPolicy"] = gameservices.post(
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
        importer="gameservices",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
