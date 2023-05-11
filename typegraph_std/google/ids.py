from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_ids() -> Import:
    ids = HTTPRuntime("https://ids.googleapis.com/")

    renames = {
        "ErrorResponse": "_ids_1_ErrorResponse",
        "EndpointIn": "_ids_2_EndpointIn",
        "EndpointOut": "_ids_3_EndpointOut",
        "ListEndpointsResponseIn": "_ids_4_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_ids_5_ListEndpointsResponseOut",
        "LocationIn": "_ids_6_LocationIn",
        "LocationOut": "_ids_7_LocationOut",
        "EmptyIn": "_ids_8_EmptyIn",
        "EmptyOut": "_ids_9_EmptyOut",
        "OperationMetadataIn": "_ids_10_OperationMetadataIn",
        "OperationMetadataOut": "_ids_11_OperationMetadataOut",
        "ListOperationsResponseIn": "_ids_12_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_ids_13_ListOperationsResponseOut",
        "ListLocationsResponseIn": "_ids_14_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_ids_15_ListLocationsResponseOut",
        "TestIamPermissionsRequestIn": "_ids_16_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_ids_17_TestIamPermissionsRequestOut",
        "OperationIn": "_ids_18_OperationIn",
        "OperationOut": "_ids_19_OperationOut",
        "AuditLogConfigIn": "_ids_20_AuditLogConfigIn",
        "AuditLogConfigOut": "_ids_21_AuditLogConfigOut",
        "PolicyIn": "_ids_22_PolicyIn",
        "PolicyOut": "_ids_23_PolicyOut",
        "StatusIn": "_ids_24_StatusIn",
        "StatusOut": "_ids_25_StatusOut",
        "SetIamPolicyRequestIn": "_ids_26_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_ids_27_SetIamPolicyRequestOut",
        "AuditConfigIn": "_ids_28_AuditConfigIn",
        "AuditConfigOut": "_ids_29_AuditConfigOut",
        "TestIamPermissionsResponseIn": "_ids_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_ids_31_TestIamPermissionsResponseOut",
        "BindingIn": "_ids_32_BindingIn",
        "BindingOut": "_ids_33_BindingOut",
        "ExprIn": "_ids_34_ExprIn",
        "ExprOut": "_ids_35_ExprOut",
        "CancelOperationRequestIn": "_ids_36_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_ids_37_CancelOperationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EndpointIn"] = t.struct(
        {
            "network": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "trafficLogs": t.boolean().optional(),
            "threatExceptions": t.array(t.string()).optional(),
            "severity": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "endpointForwardingRule": t.string().optional(),
            "network": t.string(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "endpointIp": t.string().optional(),
            "trafficLogs": t.boolean().optional(),
            "threatExceptions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "severity": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["ListEndpointsResponseIn"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListEndpointsResponseIn"])
    types["ListEndpointsResponseOut"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEndpointsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
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
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])

    functions = {}
    functions["projectsLocationsGet"] = ids.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = ids.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = ids.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = ids.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = ids.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = ids.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsDelete"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsSetIamPolicy"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsGetIamPolicy"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsPatch"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsCreate"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsTestIamPermissions"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsGet"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEndpointsList"] = ids.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="ids", renames=renames, types=types, functions=functions)
