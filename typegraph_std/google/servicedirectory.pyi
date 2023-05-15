from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    GetPolicyOptionsIn: t.typedef = ...
    GetPolicyOptionsOut: t.typedef = ...
    ListNamespacesResponseIn: t.typedef = ...
    ListNamespacesResponseOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    EndpointIn: t.typedef = ...
    EndpointOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    GetIamPolicyRequestIn: t.typedef = ...
    GetIamPolicyRequestOut: t.typedef = ...
    ListServicesResponseIn: t.typedef = ...
    ListServicesResponseOut: t.typedef = ...
    ListEndpointsResponseIn: t.typedef = ...
    ListEndpointsResponseOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    NamespaceIn: t.typedef = ...
    NamespaceOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ResolveServiceRequestIn: t.typedef = ...
    ResolveServiceRequestOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    ResolveServiceResponseIn: t.typedef = ...
    ResolveServiceResponseOut: t.typedef = ...
    ServiceIn: t.typedef = ...
    ServiceOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsNamespacesDelete: t.func = ...
    projectsLocationsNamespacesTestIamPermissions: t.func = ...
    projectsLocationsNamespacesSetIamPolicy: t.func = ...
    projectsLocationsNamespacesCreate: t.func = ...
    projectsLocationsNamespacesGetIamPolicy: t.func = ...
    projectsLocationsNamespacesPatch: t.func = ...
    projectsLocationsNamespacesList: t.func = ...
    projectsLocationsNamespacesGet: t.func = ...
    projectsLocationsNamespacesServicesCreate: t.func = ...
    projectsLocationsNamespacesServicesList: t.func = ...
    projectsLocationsNamespacesServicesGet: t.func = ...
    projectsLocationsNamespacesServicesResolve: t.func = ...
    projectsLocationsNamespacesServicesTestIamPermissions: t.func = ...
    projectsLocationsNamespacesServicesSetIamPolicy: t.func = ...
    projectsLocationsNamespacesServicesDelete: t.func = ...
    projectsLocationsNamespacesServicesPatch: t.func = ...
    projectsLocationsNamespacesServicesGetIamPolicy: t.func = ...
    projectsLocationsNamespacesServicesEndpointsDelete: t.func = ...
    projectsLocationsNamespacesServicesEndpointsList: t.func = ...
    projectsLocationsNamespacesServicesEndpointsGet: t.func = ...
    projectsLocationsNamespacesServicesEndpointsCreate: t.func = ...
    projectsLocationsNamespacesServicesEndpointsPatch: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_servicedirectory() -> Import: ...