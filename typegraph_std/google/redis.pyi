from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListInstancesResponseIn: t.typedef = ...
    ListInstancesResponseOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    GcsDestinationIn: t.typedef = ...
    GcsDestinationOut: t.typedef = ...
    GoogleCloudRedisV1OperationMetadataIn: t.typedef = ...
    GoogleCloudRedisV1OperationMetadataOut: t.typedef = ...
    InputConfigIn: t.typedef = ...
    InputConfigOut: t.typedef = ...
    GoogleCloudRedisV1LocationMetadataIn: t.typedef = ...
    GoogleCloudRedisV1LocationMetadataOut: t.typedef = ...
    NodeInfoIn: t.typedef = ...
    NodeInfoOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    MaintenancePolicyIn: t.typedef = ...
    MaintenancePolicyOut: t.typedef = ...
    OutputConfigIn: t.typedef = ...
    OutputConfigOut: t.typedef = ...
    GoogleCloudRedisV1ZoneMetadataIn: t.typedef = ...
    GoogleCloudRedisV1ZoneMetadataOut: t.typedef = ...
    FailoverInstanceRequestIn: t.typedef = ...
    FailoverInstanceRequestOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    GcsSourceIn: t.typedef = ...
    GcsSourceOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    PersistenceConfigIn: t.typedef = ...
    PersistenceConfigOut: t.typedef = ...
    TlsCertificateIn: t.typedef = ...
    TlsCertificateOut: t.typedef = ...
    MaintenanceScheduleIn: t.typedef = ...
    MaintenanceScheduleOut: t.typedef = ...
    ImportInstanceRequestIn: t.typedef = ...
    ImportInstanceRequestOut: t.typedef = ...
    ReconciliationOperationMetadataIn: t.typedef = ...
    ReconciliationOperationMetadataOut: t.typedef = ...
    ExportInstanceRequestIn: t.typedef = ...
    ExportInstanceRequestOut: t.typedef = ...
    RescheduleMaintenanceRequestIn: t.typedef = ...
    RescheduleMaintenanceRequestOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    InstanceAuthStringIn: t.typedef = ...
    InstanceAuthStringOut: t.typedef = ...
    WeeklyMaintenanceWindowIn: t.typedef = ...
    WeeklyMaintenanceWindowOut: t.typedef = ...
    TimeOfDayIn: t.typedef = ...
    TimeOfDayOut: t.typedef = ...
    InstanceIn: t.typedef = ...
    InstanceOut: t.typedef = ...
    UpgradeInstanceRequestIn: t.typedef = ...
    UpgradeInstanceRequestOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsInstancesCreate: t.func = ...
    projectsLocationsInstancesFailover: t.func = ...
    projectsLocationsInstancesRescheduleMaintenance: t.func = ...
    projectsLocationsInstancesGetAuthString: t.func = ...
    projectsLocationsInstancesUpgrade: t.func = ...
    projectsLocationsInstancesImport: t.func = ...
    projectsLocationsInstancesPatch: t.func = ...
    projectsLocationsInstancesExport: t.func = ...
    projectsLocationsInstancesList: t.func = ...
    projectsLocationsInstancesDelete: t.func = ...
    projectsLocationsInstancesGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_redis() -> Import: ...
