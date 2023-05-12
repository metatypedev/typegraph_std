from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_servicedirectory() -> Import:
    servicedirectory = HTTPRuntime("https://servicedirectory.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicedirectory_1_ErrorResponse",
        "SetIamPolicyRequestIn": "_servicedirectory_2_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_servicedirectory_3_SetIamPolicyRequestOut",
        "GetPolicyOptionsIn": "_servicedirectory_4_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_servicedirectory_5_GetPolicyOptionsOut",
        "ListNamespacesResponseIn": "_servicedirectory_6_ListNamespacesResponseIn",
        "ListNamespacesResponseOut": "_servicedirectory_7_ListNamespacesResponseOut",
        "ListLocationsResponseIn": "_servicedirectory_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_servicedirectory_9_ListLocationsResponseOut",
        "BindingIn": "_servicedirectory_10_BindingIn",
        "BindingOut": "_servicedirectory_11_BindingOut",
        "EndpointIn": "_servicedirectory_12_EndpointIn",
        "EndpointOut": "_servicedirectory_13_EndpointOut",
        "TestIamPermissionsResponseIn": "_servicedirectory_14_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_servicedirectory_15_TestIamPermissionsResponseOut",
        "GetIamPolicyRequestIn": "_servicedirectory_16_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_servicedirectory_17_GetIamPolicyRequestOut",
        "ListServicesResponseIn": "_servicedirectory_18_ListServicesResponseIn",
        "ListServicesResponseOut": "_servicedirectory_19_ListServicesResponseOut",
        "ListEndpointsResponseIn": "_servicedirectory_20_ListEndpointsResponseIn",
        "ListEndpointsResponseOut": "_servicedirectory_21_ListEndpointsResponseOut",
        "LocationIn": "_servicedirectory_22_LocationIn",
        "LocationOut": "_servicedirectory_23_LocationOut",
        "NamespaceIn": "_servicedirectory_24_NamespaceIn",
        "NamespaceOut": "_servicedirectory_25_NamespaceOut",
        "PolicyIn": "_servicedirectory_26_PolicyIn",
        "PolicyOut": "_servicedirectory_27_PolicyOut",
        "EmptyIn": "_servicedirectory_28_EmptyIn",
        "EmptyOut": "_servicedirectory_29_EmptyOut",
        "ResolveServiceRequestIn": "_servicedirectory_30_ResolveServiceRequestIn",
        "ResolveServiceRequestOut": "_servicedirectory_31_ResolveServiceRequestOut",
        "TestIamPermissionsRequestIn": "_servicedirectory_32_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_servicedirectory_33_TestIamPermissionsRequestOut",
        "ExprIn": "_servicedirectory_34_ExprIn",
        "ExprOut": "_servicedirectory_35_ExprOut",
        "ResolveServiceResponseIn": "_servicedirectory_36_ResolveServiceResponseIn",
        "ResolveServiceResponseOut": "_servicedirectory_37_ResolveServiceResponseOut",
        "ServiceIn": "_servicedirectory_38_ServiceIn",
        "ServiceOut": "_servicedirectory_39_ServiceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListNamespacesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "namespaces": t.array(t.proxy(renames["NamespaceIn"])).optional(),
        }
    ).named(renames["ListNamespacesResponseIn"])
    types["ListNamespacesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "namespaces": t.array(t.proxy(renames["NamespaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNamespacesResponseOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "network": t.string().optional(),
            "address": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "network": t.string().optional(),
            "address": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["ResolveServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["ServiceIn"])}
    ).named(renames["ResolveServiceResponseIn"])
    types["ResolveServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["ServiceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResolveServiceResponseOut"])
    types["ServiceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])

    functions = {}
    functions["projectsLocationsGet"] = servicedirectory.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesDelete"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesTestIamPermissions"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesSetIamPolicy"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesCreate"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesGetIamPolicy"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesPatch"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesList"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNamespacesGet"] = servicedirectory.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NamespaceOut"]),
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
        "projectsLocationsNamespacesServicesEndpointsDelete"
    ] = servicedirectory.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "port": t.integer().optional(),
                "network": t.string().optional(),
                "address": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsList"
    ] = servicedirectory.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "port": t.integer().optional(),
                "network": t.string().optional(),
                "address": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsGet"
    ] = servicedirectory.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "port": t.integer().optional(),
                "network": t.string().optional(),
                "address": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsCreate"
    ] = servicedirectory.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "port": t.integer().optional(),
                "network": t.string().optional(),
                "address": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsNamespacesServicesEndpointsPatch"
    ] = servicedirectory.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "port": t.integer().optional(),
                "network": t.string().optional(),
                "address": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EndpointOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicedirectory",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
