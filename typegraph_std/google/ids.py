from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_ids():
    ids = HTTPRuntime("https://ids.googleapis.com/")

    renames = {
        "ErrorResponse": "_ids_1_ErrorResponse",
        "PolicyIn": "_ids_2_PolicyIn",
        "PolicyOut": "_ids_3_PolicyOut",
        "ListEndpointsResponseIn": "_ids_4_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_ids_5_ListEndpointsResponseOut",
        "LocationIn": "_ids_6_LocationIn",
        "LocationOut": "_ids_7_LocationOut",
        "AuditConfigIn": "_ids_8_AuditConfigIn",
        "AuditConfigOut": "_ids_9_AuditConfigOut",
        "TestIamPermissionsRequestIn": "_ids_10_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_ids_11_TestIamPermissionsRequestOut",
        "AuditLogConfigIn": "_ids_12_AuditLogConfigIn",
        "AuditLogConfigOut": "_ids_13_AuditLogConfigOut",
        "EndpointIn": "_ids_14_EndpointIn",
        "EndpointOut": "_ids_15_EndpointOut",
        "ExprIn": "_ids_16_ExprIn",
        "ExprOut": "_ids_17_ExprOut",
        "BindingIn": "_ids_18_BindingIn",
        "BindingOut": "_ids_19_BindingOut",
        "TestIamPermissionsResponseIn": "_ids_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_ids_21_TestIamPermissionsResponseOut",
        "EmptyIn": "_ids_22_EmptyIn",
        "EmptyOut": "_ids_23_EmptyOut",
        "CancelOperationRequestIn": "_ids_24_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_ids_25_CancelOperationRequestOut",
        "OperationIn": "_ids_26_OperationIn",
        "OperationOut": "_ids_27_OperationOut",
        "ListLocationsResponseIn": "_ids_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_ids_29_ListLocationsResponseOut",
        "ListOperationsResponseIn": "_ids_30_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_ids_31_ListOperationsResponseOut",
        "StatusIn": "_ids_32_StatusIn",
        "StatusOut": "_ids_33_StatusOut",
        "SetIamPolicyRequestIn": "_ids_34_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_ids_35_SetIamPolicyRequestOut",
        "OperationMetadataIn": "_ids_36_OperationMetadataIn",
        "OperationMetadataOut": "_ids_37_OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListEndpointsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEndpointsResponseIn"])
    types["ListEndpointsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEndpointsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "severity": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "threatExceptions": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "network": t.string(),
            "trafficLogs": t.boolean().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "severity": t.string(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endpointIp": t.string().optional(),
            "threatExceptions": t.array(t.string()).optional(),
            "endpointForwardingRule": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "network": t.string(),
            "trafficLogs": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])

    functions = {}
    functions["projectsLocationsList"] = ids.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = ids.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsCreate"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsDelete"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsGet"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsSetIamPolicy"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsTestIamPermissions"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsGetIamPolicy"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsList"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsPatch"] = ids.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "severity": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "threatExceptions": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "network": t.string(),
                "trafficLogs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = ids.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = ids.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = ids.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = ids.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="ids", renames=renames, types=Box(types), functions=Box(functions)
    )
