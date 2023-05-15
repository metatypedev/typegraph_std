from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    CreateInstanceRequestIn: t.typedef = ...
    CreateInstanceRequestOut: t.typedef = ...
    InstanceIn: t.typedef = ...
    InstanceOut: t.typedef = ...
    ClusterIn: t.typedef = ...
    ClusterOut: t.typedef = ...
    ClusterConfigIn: t.typedef = ...
    ClusterConfigOut: t.typedef = ...
    ClusterAutoscalingConfigIn: t.typedef = ...
    ClusterAutoscalingConfigOut: t.typedef = ...
    AutoscalingLimitsIn: t.typedef = ...
    AutoscalingLimitsOut: t.typedef = ...
    AutoscalingTargetsIn: t.typedef = ...
    AutoscalingTargetsOut: t.typedef = ...
    EncryptionConfigIn: t.typedef = ...
    EncryptionConfigOut: t.typedef = ...
    ListInstancesResponseIn: t.typedef = ...
    ListInstancesResponseOut: t.typedef = ...
    ListClustersResponseIn: t.typedef = ...
    ListClustersResponseOut: t.typedef = ...
    AppProfileIn: t.typedef = ...
    AppProfileOut: t.typedef = ...
    MultiClusterRoutingUseAnyIn: t.typedef = ...
    MultiClusterRoutingUseAnyOut: t.typedef = ...
    SingleClusterRoutingIn: t.typedef = ...
    SingleClusterRoutingOut: t.typedef = ...
    ListAppProfilesResponseIn: t.typedef = ...
    ListAppProfilesResponseOut: t.typedef = ...
    GetIamPolicyRequestIn: t.typedef = ...
    GetIamPolicyRequestOut: t.typedef = ...
    GetPolicyOptionsIn: t.typedef = ...
    GetPolicyOptionsOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    ListHotTabletsResponseIn: t.typedef = ...
    ListHotTabletsResponseOut: t.typedef = ...
    HotTabletIn: t.typedef = ...
    HotTabletOut: t.typedef = ...
    CreateTableRequestIn: t.typedef = ...
    CreateTableRequestOut: t.typedef = ...
    TableIn: t.typedef = ...
    TableOut: t.typedef = ...
    ClusterStateIn: t.typedef = ...
    ClusterStateOut: t.typedef = ...
    EncryptionInfoIn: t.typedef = ...
    EncryptionInfoOut: t.typedef = ...
    ColumnFamilyIn: t.typedef = ...
    ColumnFamilyOut: t.typedef = ...
    GcRuleIn: t.typedef = ...
    GcRuleOut: t.typedef = ...
    IntersectionIn: t.typedef = ...
    IntersectionOut: t.typedef = ...
    UnionIn: t.typedef = ...
    UnionOut: t.typedef = ...
    ColumnFamilyStatsIn: t.typedef = ...
    ColumnFamilyStatsOut: t.typedef = ...
    RestoreInfoIn: t.typedef = ...
    RestoreInfoOut: t.typedef = ...
    BackupInfoIn: t.typedef = ...
    BackupInfoOut: t.typedef = ...
    TableStatsIn: t.typedef = ...
    TableStatsOut: t.typedef = ...
    SplitIn: t.typedef = ...
    SplitOut: t.typedef = ...
    ListTablesResponseIn: t.typedef = ...
    ListTablesResponseOut: t.typedef = ...
    UndeleteTableRequestIn: t.typedef = ...
    UndeleteTableRequestOut: t.typedef = ...
    ModifyColumnFamiliesRequestIn: t.typedef = ...
    ModifyColumnFamiliesRequestOut: t.typedef = ...
    ModificationIn: t.typedef = ...
    ModificationOut: t.typedef = ...
    DropRowRangeRequestIn: t.typedef = ...
    DropRowRangeRequestOut: t.typedef = ...
    GenerateConsistencyTokenRequestIn: t.typedef = ...
    GenerateConsistencyTokenRequestOut: t.typedef = ...
    GenerateConsistencyTokenResponseIn: t.typedef = ...
    GenerateConsistencyTokenResponseOut: t.typedef = ...
    CheckConsistencyRequestIn: t.typedef = ...
    CheckConsistencyRequestOut: t.typedef = ...
    CheckConsistencyResponseIn: t.typedef = ...
    CheckConsistencyResponseOut: t.typedef = ...
    BackupIn: t.typedef = ...
    BackupOut: t.typedef = ...
    ListBackupsResponseIn: t.typedef = ...
    ListBackupsResponseOut: t.typedef = ...
    RestoreTableRequestIn: t.typedef = ...
    RestoreTableRequestOut: t.typedef = ...
    CopyBackupRequestIn: t.typedef = ...
    CopyBackupRequestOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    CreateInstanceMetadataIn: t.typedef = ...
    CreateInstanceMetadataOut: t.typedef = ...
    UpdateInstanceMetadataIn: t.typedef = ...
    UpdateInstanceMetadataOut: t.typedef = ...
    PartialUpdateInstanceRequestIn: t.typedef = ...
    PartialUpdateInstanceRequestOut: t.typedef = ...
    CreateClusterMetadataIn: t.typedef = ...
    CreateClusterMetadataOut: t.typedef = ...
    CreateClusterRequestIn: t.typedef = ...
    CreateClusterRequestOut: t.typedef = ...
    TableProgressIn: t.typedef = ...
    TableProgressOut: t.typedef = ...
    PartialUpdateClusterMetadataIn: t.typedef = ...
    PartialUpdateClusterMetadataOut: t.typedef = ...
    PartialUpdateClusterRequestIn: t.typedef = ...
    PartialUpdateClusterRequestOut: t.typedef = ...
    UpdateClusterMetadataIn: t.typedef = ...
    UpdateClusterMetadataOut: t.typedef = ...
    UpdateAppProfileMetadataIn: t.typedef = ...
    UpdateAppProfileMetadataOut: t.typedef = ...
    CreateBackupMetadataIn: t.typedef = ...
    CreateBackupMetadataOut: t.typedef = ...
    CopyBackupMetadataIn: t.typedef = ...
    CopyBackupMetadataOut: t.typedef = ...
    OperationProgressIn: t.typedef = ...
    OperationProgressOut: t.typedef = ...
    RestoreTableMetadataIn: t.typedef = ...
    RestoreTableMetadataOut: t.typedef = ...
    OptimizeRestoredTableMetadataIn: t.typedef = ...
    OptimizeRestoredTableMetadataOut: t.typedef = ...
    UndeleteTableMetadataIn: t.typedef = ...
    UndeleteTableMetadataOut: t.typedef = ...
    UpdateTableMetadataIn: t.typedef = ...
    UpdateTableMetadataOut: t.typedef = ...

class FuncList:
    operationsGet: t.func = ...
    operationsDelete: t.func = ...
    operationsCancel: t.func = ...
    operationsProjectsOperationsList: t.func = ...
    projectsInstancesCreate: t.func = ...
    projectsInstancesGet: t.func = ...
    projectsInstancesList: t.func = ...
    projectsInstancesUpdate: t.func = ...
    projectsInstancesPartialUpdateInstance: t.func = ...
    projectsInstancesDelete: t.func = ...
    projectsInstancesGetIamPolicy: t.func = ...
    projectsInstancesSetIamPolicy: t.func = ...
    projectsInstancesTestIamPermissions: t.func = ...
    projectsInstancesClustersCreate: t.func = ...
    projectsInstancesClustersGet: t.func = ...
    projectsInstancesClustersList: t.func = ...
    projectsInstancesClustersUpdate: t.func = ...
    projectsInstancesClustersPartialUpdateCluster: t.func = ...
    projectsInstancesClustersDelete: t.func = ...
    projectsInstancesClustersHotTabletsList: t.func = ...
    projectsInstancesClustersBackupsCreate: t.func = ...
    projectsInstancesClustersBackupsGet: t.func = ...
    projectsInstancesClustersBackupsPatch: t.func = ...
    projectsInstancesClustersBackupsDelete: t.func = ...
    projectsInstancesClustersBackupsList: t.func = ...
    projectsInstancesClustersBackupsCopy: t.func = ...
    projectsInstancesClustersBackupsGetIamPolicy: t.func = ...
    projectsInstancesClustersBackupsSetIamPolicy: t.func = ...
    projectsInstancesClustersBackupsTestIamPermissions: t.func = ...
    projectsInstancesAppProfilesCreate: t.func = ...
    projectsInstancesAppProfilesGet: t.func = ...
    projectsInstancesAppProfilesList: t.func = ...
    projectsInstancesAppProfilesPatch: t.func = ...
    projectsInstancesAppProfilesDelete: t.func = ...
    projectsInstancesTablesCreate: t.func = ...
    projectsInstancesTablesList: t.func = ...
    projectsInstancesTablesGet: t.func = ...
    projectsInstancesTablesPatch: t.func = ...
    projectsInstancesTablesDelete: t.func = ...
    projectsInstancesTablesUndelete: t.func = ...
    projectsInstancesTablesModifyColumnFamilies: t.func = ...
    projectsInstancesTablesDropRowRange: t.func = ...
    projectsInstancesTablesGenerateConsistencyToken: t.func = ...
    projectsInstancesTablesCheckConsistency: t.func = ...
    projectsInstancesTablesRestore: t.func = ...
    projectsInstancesTablesGetIamPolicy: t.func = ...
    projectsInstancesTablesSetIamPolicy: t.func = ...
    projectsInstancesTablesTestIamPermissions: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_bigtableadmin() -> Import: ...