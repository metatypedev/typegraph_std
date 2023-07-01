from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponseOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1OriginIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1OriginOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1EntityReferenceIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1EntityReferenceOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1SearchLinksRequestIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1SearchLinksRequestOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ListRunsResponseIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ListRunsResponseOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1LineageEventIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1LineageEventOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1EventLinkIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1EventLinkOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ProcessIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ProcessOut: t.typedef = ...
    GoogleLongrunningCancelOperationRequestIn: t.typedef = ...
    GoogleLongrunningCancelOperationRequestOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1LinkIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1LinkOut: t.typedef = ...
    GoogleLongrunningOperationIn: t.typedef = ...
    GoogleLongrunningOperationOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequestOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ProcessLinkInfoIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ProcessLinkInfoOut: t.typedef = ...
    GoogleProtobufEmptyIn: t.typedef = ...
    GoogleProtobufEmptyOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ProcessLinksIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ProcessLinksOut: t.typedef = ...
    GoogleLongrunningListOperationsResponseIn: t.typedef = ...
    GoogleLongrunningListOperationsResponseOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ListLineageEventsResponseIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ListLineageEventsResponseOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ListProcessesResponseIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1ListProcessesResponseOut: t.typedef = ...
    GoogleRpcStatusIn: t.typedef = ...
    GoogleRpcStatusOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1SearchLinksResponseIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1SearchLinksResponseOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1RunIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1RunOut: t.typedef = ...
    GoogleCloudDatacatalogLineageV1OperationMetadataIn: t.typedef = ...
    GoogleCloudDatacatalogLineageV1OperationMetadataOut: t.typedef = ...

class FuncList:
    projectsLocationsBatchSearchLinkProcesses: t.func = ...
    projectsLocationsSearchLinks: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsProcessesDelete: t.func = ...
    projectsLocationsProcessesPatch: t.func = ...
    projectsLocationsProcessesGet: t.func = ...
    projectsLocationsProcessesList: t.func = ...
    projectsLocationsProcessesCreate: t.func = ...
    projectsLocationsProcessesRunsDelete: t.func = ...
    projectsLocationsProcessesRunsPatch: t.func = ...
    projectsLocationsProcessesRunsCreate: t.func = ...
    projectsLocationsProcessesRunsList: t.func = ...
    projectsLocationsProcessesRunsGet: t.func = ...
    projectsLocationsProcessesRunsLineageEventsCreate: t.func = ...
    projectsLocationsProcessesRunsLineageEventsGet: t.func = ...
    projectsLocationsProcessesRunsLineageEventsList: t.func = ...
    projectsLocationsProcessesRunsLineageEventsDelete: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_datalineage() -> Import: ...
