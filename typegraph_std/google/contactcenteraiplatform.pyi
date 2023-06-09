from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    QuotaIn: t.typedef = ...
    QuotaOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    URIsIn: t.typedef = ...
    URIsOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ContactCenterQuotaIn: t.typedef = ...
    ContactCenterQuotaOut: t.typedef = ...
    BasicAuthConfigIn: t.typedef = ...
    BasicAuthConfigOut: t.typedef = ...
    SAMLParamsIn: t.typedef = ...
    SAMLParamsOut: t.typedef = ...
    ContactCenterIn: t.typedef = ...
    ContactCenterOut: t.typedef = ...
    ListContactCentersResponseIn: t.typedef = ...
    ListContactCentersResponseOut: t.typedef = ...
    InstanceConfigIn: t.typedef = ...
    InstanceConfigOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    SamlConfigIn: t.typedef = ...
    SamlConfigOut: t.typedef = ...
    AuthenticationConfigIn: t.typedef = ...
    AuthenticationConfigOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    AdminUserIn: t.typedef = ...
    AdminUserOut: t.typedef = ...
    GoogleCloudCommonOperationMetadataIn: t.typedef = ...
    GoogleCloudCommonOperationMetadataOut: t.typedef = ...

class FuncList:
    projectsLocationsQueryContactCenterQuota: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsGet: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsContactCentersGet: t.func = ...
    projectsLocationsContactCentersPatch: t.func = ...
    projectsLocationsContactCentersUpdateAuthentication_config: t.func = ...
    projectsLocationsContactCentersCreate: t.func = ...
    projectsLocationsContactCentersDelete: t.func = ...
    projectsLocationsContactCentersGetAuthentication_config: t.func = ...
    projectsLocationsContactCentersList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_contactcenteraiplatform() -> Import: ...
