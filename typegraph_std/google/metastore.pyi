from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    NetworkConfigIn: t.typedef = ...
    NetworkConfigOut: t.typedef = ...
    ErrorDetailsIn: t.typedef = ...
    ErrorDetailsOut: t.typedef = ...
    ListMetadataImportsResponseIn: t.typedef = ...
    ListMetadataImportsResponseOut: t.typedef = ...
    HiveMetastoreConfigIn: t.typedef = ...
    HiveMetastoreConfigOut: t.typedef = ...
    ScalingConfigIn: t.typedef = ...
    ScalingConfigOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    ListFederationsResponseIn: t.typedef = ...
    ListFederationsResponseOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    MoveTableToDatabaseResponseIn: t.typedef = ...
    MoveTableToDatabaseResponseOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    ExportMetadataRequestIn: t.typedef = ...
    ExportMetadataRequestOut: t.typedef = ...
    KerberosConfigIn: t.typedef = ...
    KerberosConfigOut: t.typedef = ...
    MaintenanceWindowIn: t.typedef = ...
    MaintenanceWindowOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    AuxiliaryVersionConfigIn: t.typedef = ...
    AuxiliaryVersionConfigOut: t.typedef = ...
    ListServicesResponseIn: t.typedef = ...
    ListServicesResponseOut: t.typedef = ...
    QueryMetadataResponseIn: t.typedef = ...
    QueryMetadataResponseOut: t.typedef = ...
    EncryptionConfigIn: t.typedef = ...
    EncryptionConfigOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    RestoreIn: t.typedef = ...
    RestoreOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    AlterMetadataResourceLocationRequestIn: t.typedef = ...
    AlterMetadataResourceLocationRequestOut: t.typedef = ...
    SecretIn: t.typedef = ...
    SecretOut: t.typedef = ...
    ConsumerIn: t.typedef = ...
    ConsumerOut: t.typedef = ...
    BackupIn: t.typedef = ...
    BackupOut: t.typedef = ...
    BackendMetastoreIn: t.typedef = ...
    BackendMetastoreOut: t.typedef = ...
    MoveTableToDatabaseRequestIn: t.typedef = ...
    MoveTableToDatabaseRequestOut: t.typedef = ...
    LocationMetadataIn: t.typedef = ...
    LocationMetadataOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    AlterMetadataResourceLocationResponseIn: t.typedef = ...
    AlterMetadataResourceLocationResponseOut: t.typedef = ...
    ListBackupsResponseIn: t.typedef = ...
    ListBackupsResponseOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    QueryMetadataRequestIn: t.typedef = ...
    QueryMetadataRequestOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    DatabaseDumpIn: t.typedef = ...
    DatabaseDumpOut: t.typedef = ...
    MetadataExportIn: t.typedef = ...
    MetadataExportOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    HiveMetastoreVersionIn: t.typedef = ...
    HiveMetastoreVersionOut: t.typedef = ...
    ServiceIn: t.typedef = ...
    ServiceOut: t.typedef = ...
    TelemetryConfigIn: t.typedef = ...
    TelemetryConfigOut: t.typedef = ...
    MetadataManagementActivityIn: t.typedef = ...
    MetadataManagementActivityOut: t.typedef = ...
    FederationIn: t.typedef = ...
    FederationOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    RestoreServiceRequestIn: t.typedef = ...
    RestoreServiceRequestOut: t.typedef = ...
    MetadataImportIn: t.typedef = ...
    MetadataImportOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsServicesList: t.func = ...
    projectsLocationsServicesGetIamPolicy: t.func = ...
    projectsLocationsServicesAlterLocation: t.func = ...
    projectsLocationsServicesTestIamPermissions: t.func = ...
    projectsLocationsServicesDelete: t.func = ...
    projectsLocationsServicesQueryMetadata: t.func = ...
    projectsLocationsServicesRestore: t.func = ...
    projectsLocationsServicesSetIamPolicy: t.func = ...
    projectsLocationsServicesMoveTableToDatabase: t.func = ...
    projectsLocationsServicesPatch: t.func = ...
    projectsLocationsServicesGet: t.func = ...
    projectsLocationsServicesCreate: t.func = ...
    projectsLocationsServicesExportMetadata: t.func = ...
    projectsLocationsServicesBackupsList: t.func = ...
    projectsLocationsServicesBackupsSetIamPolicy: t.func = ...
    projectsLocationsServicesBackupsDelete: t.func = ...
    projectsLocationsServicesBackupsGetIamPolicy: t.func = ...
    projectsLocationsServicesBackupsCreate: t.func = ...
    projectsLocationsServicesBackupsGet: t.func = ...
    projectsLocationsServicesMetadataImportsCreate: t.func = ...
    projectsLocationsServicesMetadataImportsPatch: t.func = ...
    projectsLocationsServicesMetadataImportsGet: t.func = ...
    projectsLocationsServicesMetadataImportsList: t.func = ...
    projectsLocationsFederationsPatch: t.func = ...
    projectsLocationsFederationsGet: t.func = ...
    projectsLocationsFederationsSetIamPolicy: t.func = ...
    projectsLocationsFederationsCreate: t.func = ...
    projectsLocationsFederationsList: t.func = ...
    projectsLocationsFederationsGetIamPolicy: t.func = ...
    projectsLocationsFederationsDelete: t.func = ...
    projectsLocationsFederationsTestIamPermissions: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_metastore() -> Import: ...