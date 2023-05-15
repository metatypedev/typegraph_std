from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    DataProviderIn: t.typedef = ...
    DataProviderOut: t.typedef = ...
    SubscribeListingRequestIn: t.typedef = ...
    SubscribeListingRequestOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    GetPolicyOptionsIn: t.typedef = ...
    GetPolicyOptionsOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    ListOrgDataExchangesResponseIn: t.typedef = ...
    ListOrgDataExchangesResponseOut: t.typedef = ...
    BigQueryDatasetSourceIn: t.typedef = ...
    BigQueryDatasetSourceOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    SubscribeListingResponseIn: t.typedef = ...
    SubscribeListingResponseOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    DataExchangeIn: t.typedef = ...
    DataExchangeOut: t.typedef = ...
    ListingIn: t.typedef = ...
    ListingOut: t.typedef = ...
    GetIamPolicyRequestIn: t.typedef = ...
    GetIamPolicyRequestOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListListingsResponseIn: t.typedef = ...
    ListListingsResponseOut: t.typedef = ...
    DestinationDatasetIn: t.typedef = ...
    DestinationDatasetOut: t.typedef = ...
    DestinationDatasetReferenceIn: t.typedef = ...
    DestinationDatasetReferenceOut: t.typedef = ...
    ListDataExchangesResponseIn: t.typedef = ...
    ListDataExchangesResponseOut: t.typedef = ...
    PublisherIn: t.typedef = ...
    PublisherOut: t.typedef = ...

class FuncList:
    organizationsLocationsDataExchangesList: t.func = ...
    projectsLocationsDataExchangesList: t.func = ...
    projectsLocationsDataExchangesPatch: t.func = ...
    projectsLocationsDataExchangesCreate: t.func = ...
    projectsLocationsDataExchangesSetIamPolicy: t.func = ...
    projectsLocationsDataExchangesDelete: t.func = ...
    projectsLocationsDataExchangesGet: t.func = ...
    projectsLocationsDataExchangesGetIamPolicy: t.func = ...
    projectsLocationsDataExchangesTestIamPermissions: t.func = ...
    projectsLocationsDataExchangesListingsSetIamPolicy: t.func = ...
    projectsLocationsDataExchangesListingsSubscribe: t.func = ...
    projectsLocationsDataExchangesListingsPatch: t.func = ...
    projectsLocationsDataExchangesListingsGetIamPolicy: t.func = ...
    projectsLocationsDataExchangesListingsTestIamPermissions: t.func = ...
    projectsLocationsDataExchangesListingsDelete: t.func = ...
    projectsLocationsDataExchangesListingsCreate: t.func = ...
    projectsLocationsDataExchangesListingsGet: t.func = ...
    projectsLocationsDataExchangesListingsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_analyticshub() -> Import: ...