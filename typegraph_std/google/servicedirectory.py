from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_servicedirectory() -> Import:
    servicedirectory = HTTPRuntime("https://servicedirectory.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicedirectory_1_ErrorResponse",
        "ListEndpointsResponseIn": "_servicedirectory_2_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_servicedirectory_3_ListEndpointsResponseOut",
        "ResolveServiceResponseIn": "_servicedirectory_4_ResolveServiceResponseIn",
        "ResolveServiceResponseOut": "_servicedirectory_5_ResolveServiceResponseOut",
        "LocationIn": "_servicedirectory_6_LocationIn",
        "LocationOut": "_servicedirectory_7_LocationOut",
        "PolicyIn": "_servicedirectory_8_PolicyIn",
        "PolicyOut": "_servicedirectory_9_PolicyOut",
        "SetIamPolicyRequestIn": "_servicedirectory_10_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_servicedirectory_11_SetIamPolicyRequestOut",
        "ServiceIn": "_servicedirectory_12_ServiceIn",
        "ServiceOut": "_servicedirectory_13_ServiceOut",
        "TestIamPermissionsResponseIn": "_servicedirectory_14_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_servicedirectory_15_TestIamPermissionsResponseOut",
        "ExprIn": "_servicedirectory_16_ExprIn",
        "ExprOut": "_servicedirectory_17_ExprOut",
        "EmptyIn": "_servicedirectory_18_EmptyIn",
        "EmptyOut": "_servicedirectory_19_EmptyOut",
        "ListServicesResponseIn": "_servicedirectory_20_ListServicesResponseIn",
        "ListServicesResponseOut": "_servicedirectory_21_ListServicesResponseOut",
        "ResolveServiceRequestIn": "_servicedirectory_22_ResolveServiceRequestIn",
        "ResolveServiceRequestOut": "_servicedirectory_23_ResolveServiceRequestOut",
        "EndpointIn": "_servicedirectory_24_EndpointIn",
        "EndpointOut": "_servicedirectory_25_EndpointOut",
        "NamespaceIn": "_servicedirectory_26_NamespaceIn",
        "NamespaceOut": "_servicedirectory_27_NamespaceOut",
        "GetPolicyOptionsIn": "_servicedirectory_28_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_servicedirectory_29_GetPolicyOptionsOut",
        "ListNamespacesResponseIn": "_servicedirectory_30_ListNamespacesResponseIn",
        "ListNamespacesResponseOut": "_servicedirectory_31_ListNamespacesResponseOut",
        "BindingIn": "_servicedirectory_32_BindingIn",
        "BindingOut": "_servicedirectory_33_BindingOut",
        "ListLocationsResponseIn": "_servicedirectory_34_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_servicedirectory_35_ListLocationsResponseOut",
        "GetIamPolicyRequestIn": "_servicedirectory_36_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_servicedirectory_37_GetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_servicedirectory_38_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_servicedirectory_39_TestIamPermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListEndpointsResponseIn"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEndpointsResponseIn"])
    types["ListEndpointsResponseOut"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEndpointsResponseOut"])
    types["ResolveServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["ServiceIn"])}
    ).named(renames["ResolveServiceResponseIn"])
    types["ResolveServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["ServiceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResolveServiceResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ServiceIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["ResolveServiceRequestIn"] = t.struct(
        {
            "endpointFilter": t.string().optional(),
            "maxEndpoints": t.integer().optional(),
        }
    ).named(renames["ResolveServiceRequestIn"])
    types["ResolveServiceRequestOut"] = t.struct(
        {
            "endpointFilter": t.string().optional(),
            "maxEndpoints": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResolveServiceRequestOut"])
    types["EndpointIn"] = t.struct(
        {
            "address": t.string().optional(),
            "port": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "address": t.string().optional(),
            "port": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "network": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["NamespaceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["NamespaceIn"])
    types["NamespaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespaceOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["ListNamespacesResponseIn"] = t.struct(
        {
            "namespaces": t.array(t.proxy(renames["NamespaceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNamespacesResponseIn"])
    types["ListNamespacesResponseOut"] = t.struct(
        {
            "namespaces": t.array(t.proxy(renames["NamespaceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNamespacesResponseOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
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
    functions["projectsLocationsGet"] = servicedirectory.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = servicedirectory.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesList"] = servicedirectory.post(
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
    functions["projectsLocationsNamespacesDelete"] = servicedirectory.post(
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
    functions["projectsLocationsNamespacesCreate"] = servicedirectory.post(
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
    functions["projectsLocationsNamespacesGetIamPolicy"] = servicedirectory.post(
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
    functions["projectsLocationsNamespacesGet"] = servicedirectory.post(
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
    functions["projectsLocationsNamespacesSetIamPolicy"] = servicedirectory.post(
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
    functions["projectsLocationsNamespacesPatch"] = servicedirectory.post(
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
    functions["projectsLocationsNamespacesTestIamPermissions"] = servicedirectory.post(
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
        "projectsLocationsNamespacesServicesTestIamPermissions"
    ] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesList"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesGetIamPolicy"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesSetIamPolicy"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesPatch"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesCreate"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesDelete"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesResolve"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesGet"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsDelete"
    ] = servicedirectory.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsPatch"
    ] = servicedirectory.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesEndpointsGet"] = servicedirectory.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsCreate"
    ] = servicedirectory.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsList"
    ] = servicedirectory.get(
        "v1/{parent}/endpoints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEndpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicedirectory",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
