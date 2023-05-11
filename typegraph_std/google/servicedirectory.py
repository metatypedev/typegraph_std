from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_servicedirectory() -> Import:
    servicedirectory = HTTPRuntime("https://servicedirectory.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicedirectory_1_ErrorResponse",
        "ResolveServiceRequestIn": "_servicedirectory_2_ResolveServiceRequestIn",
        "ResolveServiceRequestOut": "_servicedirectory_3_ResolveServiceRequestOut",
        "SetIamPolicyRequestIn": "_servicedirectory_4_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_servicedirectory_5_SetIamPolicyRequestOut",
        "GetPolicyOptionsIn": "_servicedirectory_6_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_servicedirectory_7_GetPolicyOptionsOut",
        "ExprIn": "_servicedirectory_8_ExprIn",
        "ExprOut": "_servicedirectory_9_ExprOut",
        "NamespaceIn": "_servicedirectory_10_NamespaceIn",
        "NamespaceOut": "_servicedirectory_11_NamespaceOut",
        "ServiceIn": "_servicedirectory_12_ServiceIn",
        "ServiceOut": "_servicedirectory_13_ServiceOut",
        "ResolveServiceResponseIn": "_servicedirectory_14_ResolveServiceResponseIn",
        "ResolveServiceResponseOut": "_servicedirectory_15_ResolveServiceResponseOut",
        "EndpointIn": "_servicedirectory_16_EndpointIn",
        "EndpointOut": "_servicedirectory_17_EndpointOut",
        "ListNamespacesResponseIn": "_servicedirectory_18_ListNamespacesResponseIn",
        "ListNamespacesResponseOut": "_servicedirectory_19_ListNamespacesResponseOut",
        "TestIamPermissionsResponseIn": "_servicedirectory_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_servicedirectory_21_TestIamPermissionsResponseOut",
        "ListLocationsResponseIn": "_servicedirectory_22_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_servicedirectory_23_ListLocationsResponseOut",
        "TestIamPermissionsRequestIn": "_servicedirectory_24_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_servicedirectory_25_TestIamPermissionsRequestOut",
        "PolicyIn": "_servicedirectory_26_PolicyIn",
        "PolicyOut": "_servicedirectory_27_PolicyOut",
        "GetIamPolicyRequestIn": "_servicedirectory_28_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_servicedirectory_29_GetIamPolicyRequestOut",
        "ListEndpointsResponseIn": "_servicedirectory_30_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_servicedirectory_31_ListEndpointsResponseOut",
        "EmptyIn": "_servicedirectory_32_EmptyIn",
        "EmptyOut": "_servicedirectory_33_EmptyOut",
        "ListServicesResponseIn": "_servicedirectory_34_ListServicesResponseIn",
        "ListServicesResponseOut": "_servicedirectory_35_ListServicesResponseOut",
        "LocationIn": "_servicedirectory_36_LocationIn",
        "LocationOut": "_servicedirectory_37_LocationOut",
        "BindingIn": "_servicedirectory_38_BindingIn",
        "BindingOut": "_servicedirectory_39_BindingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["NamespaceIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["NamespaceIn"])
    types["NamespaceOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespaceOut"])
    types["ServiceIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["ResolveServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["ServiceIn"])}
    ).named(renames["ResolveServiceResponseIn"])
    types["ResolveServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["ServiceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResolveServiceResponseOut"])
    types["EndpointIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "network": t.string().optional(),
            "name": t.string().optional(),
            "address": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "port": t.integer().optional(),
            "network": t.string().optional(),
            "name": t.string().optional(),
            "address": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ListEndpointsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
        }
    ).named(renames["ListEndpointsResponseIn"])
    types["ListEndpointsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEndpointsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])

    functions = {}
    functions["projectsLocationsGet"] = servicedirectory.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesSetIamPolicy"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesGetIamPolicy"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesDelete"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesList"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesPatch"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesGet"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesTestIamPermissions"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesCreate"] = servicedirectory.post(
        "v1/{parent}/namespaces",
        t.struct(
            {
                "namespaceId": t.string(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesList"] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
        "projectsLocationsNamespacesServicesSetIamPolicy"
    ] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
    functions["projectsLocationsNamespacesServicesDelete"] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
    functions["projectsLocationsNamespacesServicesResolve"] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
    functions["projectsLocationsNamespacesServicesPatch"] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
        "projectsLocationsNamespacesServicesTestIamPermissions"
    ] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
    functions["projectsLocationsNamespacesServicesCreate"] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
    functions["projectsLocationsNamespacesServicesGet"] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
        "projectsLocationsNamespacesServicesGetIamPolicy"
    ] = servicedirectory.post(
        "v1/{resource}:getIamPolicy",
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
        "projectsLocationsNamespacesServicesEndpointsPatch"
    ] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsDelete"
    ] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsList"
    ] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsCreate"
    ] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesServicesEndpointsGet"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicedirectory", renames=renames, types=types, functions=functions
    )
