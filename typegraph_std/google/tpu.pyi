from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    GenerateServiceIdentityRequestIn: t.typedef = ...
    GenerateServiceIdentityRequestOut: t.typedef = ...
    GetGuestAttributesResponseIn: t.typedef = ...
    GetGuestAttributesResponseOut: t.typedef = ...
    GenerateServiceIdentityResponseIn: t.typedef = ...
    GenerateServiceIdentityResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    RuntimeVersionIn: t.typedef = ...
    RuntimeVersionOut: t.typedef = ...
    AttachedDiskIn: t.typedef = ...
    AttachedDiskOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    AcceleratorConfigIn: t.typedef = ...
    AcceleratorConfigOut: t.typedef = ...
    SymptomIn: t.typedef = ...
    SymptomOut: t.typedef = ...
    NodeIn: t.typedef = ...
    NodeOut: t.typedef = ...
    ServiceIdentityIn: t.typedef = ...
    ServiceIdentityOut: t.typedef = ...
    ListAcceleratorTypesResponseIn: t.typedef = ...
    ListAcceleratorTypesResponseOut: t.typedef = ...
    ShieldedInstanceConfigIn: t.typedef = ...
    ShieldedInstanceConfigOut: t.typedef = ...
    ListRuntimeVersionsResponseIn: t.typedef = ...
    ListRuntimeVersionsResponseOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    GetGuestAttributesRequestIn: t.typedef = ...
    GetGuestAttributesRequestOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    GuestAttributesIn: t.typedef = ...
    GuestAttributesOut: t.typedef = ...
    AcceleratorTypeIn: t.typedef = ...
    AcceleratorTypeOut: t.typedef = ...
    NetworkConfigIn: t.typedef = ...
    NetworkConfigOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    GuestAttributesEntryIn: t.typedef = ...
    GuestAttributesEntryOut: t.typedef = ...
    ListNodesResponseIn: t.typedef = ...
    ListNodesResponseOut: t.typedef = ...
    NetworkEndpointIn: t.typedef = ...
    NetworkEndpointOut: t.typedef = ...
    ServiceAccountIn: t.typedef = ...
    ServiceAccountOut: t.typedef = ...
    AccessConfigIn: t.typedef = ...
    AccessConfigOut: t.typedef = ...
    StartNodeRequestIn: t.typedef = ...
    StartNodeRequestOut: t.typedef = ...
    GuestAttributesValueIn: t.typedef = ...
    GuestAttributesValueOut: t.typedef = ...
    StopNodeRequestIn: t.typedef = ...
    StopNodeRequestOut: t.typedef = ...
    SchedulingConfigIn: t.typedef = ...
    SchedulingConfigOut: t.typedef = ...

class FuncList:
    projectsLocationsList: t.func = ...
    projectsLocationsGet: t.func = ...
    projectsLocationsGenerateServiceIdentity: t.func = ...
    projectsLocationsAcceleratorTypesList: t.func = ...
    projectsLocationsAcceleratorTypesGet: t.func = ...
    projectsLocationsRuntimeVersionsList: t.func = ...
    projectsLocationsRuntimeVersionsGet: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsNodesGet: t.func = ...
    projectsLocationsNodesList: t.func = ...
    projectsLocationsNodesDelete: t.func = ...
    projectsLocationsNodesCreate: t.func = ...
    projectsLocationsNodesStart: t.func = ...
    projectsLocationsNodesStop: t.func = ...
    projectsLocationsNodesGetGuestAttributes: t.func = ...
    projectsLocationsNodesPatch: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_tpu() -> Import: ...
