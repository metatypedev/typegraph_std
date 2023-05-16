from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_bigtableadmin() -> Import:
    bigtableadmin = HTTPRuntime("https://bigtableadmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigtableadmin_1_ErrorResponse",
        "ListOperationsResponseIn": "_bigtableadmin_2_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_bigtableadmin_3_ListOperationsResponseOut",
        "OperationIn": "_bigtableadmin_4_OperationIn",
        "OperationOut": "_bigtableadmin_5_OperationOut",
        "StatusIn": "_bigtableadmin_6_StatusIn",
        "StatusOut": "_bigtableadmin_7_StatusOut",
        "EmptyIn": "_bigtableadmin_8_EmptyIn",
        "EmptyOut": "_bigtableadmin_9_EmptyOut",
        "CreateInstanceRequestIn": "_bigtableadmin_10_CreateInstanceRequestIn",
        "CreateInstanceRequestOut": "_bigtableadmin_11_CreateInstanceRequestOut",
        "InstanceIn": "_bigtableadmin_12_InstanceIn",
        "InstanceOut": "_bigtableadmin_13_InstanceOut",
        "ClusterIn": "_bigtableadmin_14_ClusterIn",
        "ClusterOut": "_bigtableadmin_15_ClusterOut",
        "ClusterConfigIn": "_bigtableadmin_16_ClusterConfigIn",
        "ClusterConfigOut": "_bigtableadmin_17_ClusterConfigOut",
        "ClusterAutoscalingConfigIn": "_bigtableadmin_18_ClusterAutoscalingConfigIn",
        "ClusterAutoscalingConfigOut": "_bigtableadmin_19_ClusterAutoscalingConfigOut",
        "AutoscalingLimitsIn": "_bigtableadmin_20_AutoscalingLimitsIn",
        "AutoscalingLimitsOut": "_bigtableadmin_21_AutoscalingLimitsOut",
        "AutoscalingTargetsIn": "_bigtableadmin_22_AutoscalingTargetsIn",
        "AutoscalingTargetsOut": "_bigtableadmin_23_AutoscalingTargetsOut",
        "EncryptionConfigIn": "_bigtableadmin_24_EncryptionConfigIn",
        "EncryptionConfigOut": "_bigtableadmin_25_EncryptionConfigOut",
        "ListInstancesResponseIn": "_bigtableadmin_26_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_bigtableadmin_27_ListInstancesResponseOut",
        "ListClustersResponseIn": "_bigtableadmin_28_ListClustersResponseIn",
        "ListClustersResponseOut": "_bigtableadmin_29_ListClustersResponseOut",
        "AppProfileIn": "_bigtableadmin_30_AppProfileIn",
        "AppProfileOut": "_bigtableadmin_31_AppProfileOut",
        "MultiClusterRoutingUseAnyIn": "_bigtableadmin_32_MultiClusterRoutingUseAnyIn",
        "MultiClusterRoutingUseAnyOut": "_bigtableadmin_33_MultiClusterRoutingUseAnyOut",
        "SingleClusterRoutingIn": "_bigtableadmin_34_SingleClusterRoutingIn",
        "SingleClusterRoutingOut": "_bigtableadmin_35_SingleClusterRoutingOut",
        "ListAppProfilesResponseIn": "_bigtableadmin_36_ListAppProfilesResponseIn",
        "ListAppProfilesResponseOut": "_bigtableadmin_37_ListAppProfilesResponseOut",
        "GetIamPolicyRequestIn": "_bigtableadmin_38_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigtableadmin_39_GetIamPolicyRequestOut",
        "GetPolicyOptionsIn": "_bigtableadmin_40_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigtableadmin_41_GetPolicyOptionsOut",
        "PolicyIn": "_bigtableadmin_42_PolicyIn",
        "PolicyOut": "_bigtableadmin_43_PolicyOut",
        "BindingIn": "_bigtableadmin_44_BindingIn",
        "BindingOut": "_bigtableadmin_45_BindingOut",
        "ExprIn": "_bigtableadmin_46_ExprIn",
        "ExprOut": "_bigtableadmin_47_ExprOut",
        "AuditConfigIn": "_bigtableadmin_48_AuditConfigIn",
        "AuditConfigOut": "_bigtableadmin_49_AuditConfigOut",
        "AuditLogConfigIn": "_bigtableadmin_50_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigtableadmin_51_AuditLogConfigOut",
        "SetIamPolicyRequestIn": "_bigtableadmin_52_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigtableadmin_53_SetIamPolicyRequestOut",
        "TestIamPermissionsRequestIn": "_bigtableadmin_54_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigtableadmin_55_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_bigtableadmin_56_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigtableadmin_57_TestIamPermissionsResponseOut",
        "ListHotTabletsResponseIn": "_bigtableadmin_58_ListHotTabletsResponseIn",
        "ListHotTabletsResponseOut": "_bigtableadmin_59_ListHotTabletsResponseOut",
        "HotTabletIn": "_bigtableadmin_60_HotTabletIn",
        "HotTabletOut": "_bigtableadmin_61_HotTabletOut",
        "CreateTableRequestIn": "_bigtableadmin_62_CreateTableRequestIn",
        "CreateTableRequestOut": "_bigtableadmin_63_CreateTableRequestOut",
        "TableIn": "_bigtableadmin_64_TableIn",
        "TableOut": "_bigtableadmin_65_TableOut",
        "ClusterStateIn": "_bigtableadmin_66_ClusterStateIn",
        "ClusterStateOut": "_bigtableadmin_67_ClusterStateOut",
        "EncryptionInfoIn": "_bigtableadmin_68_EncryptionInfoIn",
        "EncryptionInfoOut": "_bigtableadmin_69_EncryptionInfoOut",
        "ColumnFamilyIn": "_bigtableadmin_70_ColumnFamilyIn",
        "ColumnFamilyOut": "_bigtableadmin_71_ColumnFamilyOut",
        "GcRuleIn": "_bigtableadmin_72_GcRuleIn",
        "GcRuleOut": "_bigtableadmin_73_GcRuleOut",
        "IntersectionIn": "_bigtableadmin_74_IntersectionIn",
        "IntersectionOut": "_bigtableadmin_75_IntersectionOut",
        "UnionIn": "_bigtableadmin_76_UnionIn",
        "UnionOut": "_bigtableadmin_77_UnionOut",
        "ColumnFamilyStatsIn": "_bigtableadmin_78_ColumnFamilyStatsIn",
        "ColumnFamilyStatsOut": "_bigtableadmin_79_ColumnFamilyStatsOut",
        "RestoreInfoIn": "_bigtableadmin_80_RestoreInfoIn",
        "RestoreInfoOut": "_bigtableadmin_81_RestoreInfoOut",
        "BackupInfoIn": "_bigtableadmin_82_BackupInfoIn",
        "BackupInfoOut": "_bigtableadmin_83_BackupInfoOut",
        "TableStatsIn": "_bigtableadmin_84_TableStatsIn",
        "TableStatsOut": "_bigtableadmin_85_TableStatsOut",
        "SplitIn": "_bigtableadmin_86_SplitIn",
        "SplitOut": "_bigtableadmin_87_SplitOut",
        "ListTablesResponseIn": "_bigtableadmin_88_ListTablesResponseIn",
        "ListTablesResponseOut": "_bigtableadmin_89_ListTablesResponseOut",
        "UndeleteTableRequestIn": "_bigtableadmin_90_UndeleteTableRequestIn",
        "UndeleteTableRequestOut": "_bigtableadmin_91_UndeleteTableRequestOut",
        "ModifyColumnFamiliesRequestIn": "_bigtableadmin_92_ModifyColumnFamiliesRequestIn",
        "ModifyColumnFamiliesRequestOut": "_bigtableadmin_93_ModifyColumnFamiliesRequestOut",
        "ModificationIn": "_bigtableadmin_94_ModificationIn",
        "ModificationOut": "_bigtableadmin_95_ModificationOut",
        "DropRowRangeRequestIn": "_bigtableadmin_96_DropRowRangeRequestIn",
        "DropRowRangeRequestOut": "_bigtableadmin_97_DropRowRangeRequestOut",
        "GenerateConsistencyTokenRequestIn": "_bigtableadmin_98_GenerateConsistencyTokenRequestIn",
        "GenerateConsistencyTokenRequestOut": "_bigtableadmin_99_GenerateConsistencyTokenRequestOut",
        "GenerateConsistencyTokenResponseIn": "_bigtableadmin_100_GenerateConsistencyTokenResponseIn",
        "GenerateConsistencyTokenResponseOut": "_bigtableadmin_101_GenerateConsistencyTokenResponseOut",
        "CheckConsistencyRequestIn": "_bigtableadmin_102_CheckConsistencyRequestIn",
        "CheckConsistencyRequestOut": "_bigtableadmin_103_CheckConsistencyRequestOut",
        "CheckConsistencyResponseIn": "_bigtableadmin_104_CheckConsistencyResponseIn",
        "CheckConsistencyResponseOut": "_bigtableadmin_105_CheckConsistencyResponseOut",
        "BackupIn": "_bigtableadmin_106_BackupIn",
        "BackupOut": "_bigtableadmin_107_BackupOut",
        "ListBackupsResponseIn": "_bigtableadmin_108_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_bigtableadmin_109_ListBackupsResponseOut",
        "RestoreTableRequestIn": "_bigtableadmin_110_RestoreTableRequestIn",
        "RestoreTableRequestOut": "_bigtableadmin_111_RestoreTableRequestOut",
        "CopyBackupRequestIn": "_bigtableadmin_112_CopyBackupRequestIn",
        "CopyBackupRequestOut": "_bigtableadmin_113_CopyBackupRequestOut",
        "ListLocationsResponseIn": "_bigtableadmin_114_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_bigtableadmin_115_ListLocationsResponseOut",
        "LocationIn": "_bigtableadmin_116_LocationIn",
        "LocationOut": "_bigtableadmin_117_LocationOut",
        "CreateInstanceMetadataIn": "_bigtableadmin_118_CreateInstanceMetadataIn",
        "CreateInstanceMetadataOut": "_bigtableadmin_119_CreateInstanceMetadataOut",
        "UpdateInstanceMetadataIn": "_bigtableadmin_120_UpdateInstanceMetadataIn",
        "UpdateInstanceMetadataOut": "_bigtableadmin_121_UpdateInstanceMetadataOut",
        "PartialUpdateInstanceRequestIn": "_bigtableadmin_122_PartialUpdateInstanceRequestIn",
        "PartialUpdateInstanceRequestOut": "_bigtableadmin_123_PartialUpdateInstanceRequestOut",
        "CreateClusterMetadataIn": "_bigtableadmin_124_CreateClusterMetadataIn",
        "CreateClusterMetadataOut": "_bigtableadmin_125_CreateClusterMetadataOut",
        "CreateClusterRequestIn": "_bigtableadmin_126_CreateClusterRequestIn",
        "CreateClusterRequestOut": "_bigtableadmin_127_CreateClusterRequestOut",
        "TableProgressIn": "_bigtableadmin_128_TableProgressIn",
        "TableProgressOut": "_bigtableadmin_129_TableProgressOut",
        "PartialUpdateClusterMetadataIn": "_bigtableadmin_130_PartialUpdateClusterMetadataIn",
        "PartialUpdateClusterMetadataOut": "_bigtableadmin_131_PartialUpdateClusterMetadataOut",
        "PartialUpdateClusterRequestIn": "_bigtableadmin_132_PartialUpdateClusterRequestIn",
        "PartialUpdateClusterRequestOut": "_bigtableadmin_133_PartialUpdateClusterRequestOut",
        "UpdateClusterMetadataIn": "_bigtableadmin_134_UpdateClusterMetadataIn",
        "UpdateClusterMetadataOut": "_bigtableadmin_135_UpdateClusterMetadataOut",
        "UpdateAppProfileMetadataIn": "_bigtableadmin_136_UpdateAppProfileMetadataIn",
        "UpdateAppProfileMetadataOut": "_bigtableadmin_137_UpdateAppProfileMetadataOut",
        "CreateBackupMetadataIn": "_bigtableadmin_138_CreateBackupMetadataIn",
        "CreateBackupMetadataOut": "_bigtableadmin_139_CreateBackupMetadataOut",
        "CopyBackupMetadataIn": "_bigtableadmin_140_CopyBackupMetadataIn",
        "CopyBackupMetadataOut": "_bigtableadmin_141_CopyBackupMetadataOut",
        "OperationProgressIn": "_bigtableadmin_142_OperationProgressIn",
        "OperationProgressOut": "_bigtableadmin_143_OperationProgressOut",
        "RestoreTableMetadataIn": "_bigtableadmin_144_RestoreTableMetadataIn",
        "RestoreTableMetadataOut": "_bigtableadmin_145_RestoreTableMetadataOut",
        "OptimizeRestoredTableMetadataIn": "_bigtableadmin_146_OptimizeRestoredTableMetadataIn",
        "OptimizeRestoredTableMetadataOut": "_bigtableadmin_147_OptimizeRestoredTableMetadataOut",
        "UndeleteTableMetadataIn": "_bigtableadmin_148_UndeleteTableMetadataIn",
        "UndeleteTableMetadataOut": "_bigtableadmin_149_UndeleteTableMetadataOut",
        "UpdateTableMetadataIn": "_bigtableadmin_150_UpdateTableMetadataIn",
        "UpdateTableMetadataOut": "_bigtableadmin_151_UpdateTableMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CreateInstanceRequestIn"] = t.struct(
        {
            "parent": t.string(),
            "instanceId": t.string(),
            "instance": t.proxy(renames["InstanceIn"]),
            "clusters": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["CreateInstanceRequestIn"])
    types["CreateInstanceRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "instanceId": t.string(),
            "instance": t.proxy(renames["InstanceOut"]),
            "clusters": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceRequestOut"])
    types["InstanceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string(),
            "state": t.string().optional(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["ClusterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "location": t.string().optional(),
            "serveNodes": t.integer().optional(),
            "clusterConfig": t.proxy(renames["ClusterConfigIn"]).optional(),
            "defaultStorageType": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "name": t.string().optional(),
            "location": t.string().optional(),
            "state": t.string().optional(),
            "serveNodes": t.integer().optional(),
            "clusterConfig": t.proxy(renames["ClusterConfigOut"]).optional(),
            "defaultStorageType": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["ClusterConfigIn"] = t.struct(
        {
            "clusterAutoscalingConfig": t.proxy(
                renames["ClusterAutoscalingConfigIn"]
            ).optional()
        }
    ).named(renames["ClusterConfigIn"])
    types["ClusterConfigOut"] = t.struct(
        {
            "clusterAutoscalingConfig": t.proxy(
                renames["ClusterAutoscalingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterConfigOut"])
    types["ClusterAutoscalingConfigIn"] = t.struct(
        {
            "autoscalingLimits": t.proxy(renames["AutoscalingLimitsIn"]),
            "autoscalingTargets": t.proxy(renames["AutoscalingTargetsIn"]),
        }
    ).named(renames["ClusterAutoscalingConfigIn"])
    types["ClusterAutoscalingConfigOut"] = t.struct(
        {
            "autoscalingLimits": t.proxy(renames["AutoscalingLimitsOut"]),
            "autoscalingTargets": t.proxy(renames["AutoscalingTargetsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterAutoscalingConfigOut"])
    types["AutoscalingLimitsIn"] = t.struct(
        {"minServeNodes": t.integer(), "maxServeNodes": t.integer()}
    ).named(renames["AutoscalingLimitsIn"])
    types["AutoscalingLimitsOut"] = t.struct(
        {
            "minServeNodes": t.integer(),
            "maxServeNodes": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingLimitsOut"])
    types["AutoscalingTargetsIn"] = t.struct(
        {
            "cpuUtilizationPercent": t.integer().optional(),
            "storageUtilizationGibPerNode": t.integer().optional(),
        }
    ).named(renames["AutoscalingTargetsIn"])
    types["AutoscalingTargetsOut"] = t.struct(
        {
            "cpuUtilizationPercent": t.integer().optional(),
            "storageUtilizationGibPerNode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingTargetsOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "failedLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "failedLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["ListClustersResponseIn"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ClusterIn"])).optional(),
            "failedLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListClustersResponseIn"])
    types["ListClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "failedLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClustersResponseOut"])
    types["AppProfileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "multiClusterRoutingUseAny": t.proxy(
                renames["MultiClusterRoutingUseAnyIn"]
            ).optional(),
            "singleClusterRouting": t.proxy(
                renames["SingleClusterRoutingIn"]
            ).optional(),
        }
    ).named(renames["AppProfileIn"])
    types["AppProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "multiClusterRoutingUseAny": t.proxy(
                renames["MultiClusterRoutingUseAnyOut"]
            ).optional(),
            "singleClusterRouting": t.proxy(
                renames["SingleClusterRoutingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProfileOut"])
    types["MultiClusterRoutingUseAnyIn"] = t.struct(
        {"clusterIds": t.array(t.string()).optional()}
    ).named(renames["MultiClusterRoutingUseAnyIn"])
    types["MultiClusterRoutingUseAnyOut"] = t.struct(
        {
            "clusterIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClusterRoutingUseAnyOut"])
    types["SingleClusterRoutingIn"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "allowTransactionalWrites": t.boolean().optional(),
        }
    ).named(renames["SingleClusterRoutingIn"])
    types["SingleClusterRoutingOut"] = t.struct(
        {
            "clusterId": t.string().optional(),
            "allowTransactionalWrites": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SingleClusterRoutingOut"])
    types["ListAppProfilesResponseIn"] = t.struct(
        {
            "appProfiles": t.array(t.proxy(renames["AppProfileIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "failedLocations": t.array(t.string()).optional(),
        }
    ).named(renames["ListAppProfilesResponseIn"])
    types["ListAppProfilesResponseOut"] = t.struct(
        {
            "appProfiles": t.array(t.proxy(renames["AppProfileOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "failedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAppProfilesResponseOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListHotTabletsResponseIn"] = t.struct(
        {
            "hotTablets": t.array(t.proxy(renames["HotTabletIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListHotTabletsResponseIn"])
    types["ListHotTabletsResponseOut"] = t.struct(
        {
            "hotTablets": t.array(t.proxy(renames["HotTabletOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListHotTabletsResponseOut"])
    types["HotTabletIn"] = t.struct(
        {
            "name": t.string().optional(),
            "tableName": t.string().optional(),
            "startKey": t.string().optional(),
            "endKey": t.string().optional(),
        }
    ).named(renames["HotTabletIn"])
    types["HotTabletOut"] = t.struct(
        {
            "name": t.string().optional(),
            "tableName": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "startKey": t.string().optional(),
            "endKey": t.string().optional(),
            "nodeCpuUsagePercent": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotTabletOut"])
    types["CreateTableRequestIn"] = t.struct(
        {
            "tableId": t.string(),
            "table": t.proxy(renames["TableIn"]),
            "initialSplits": t.array(t.proxy(renames["SplitIn"])).optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "tableId": t.string(),
            "table": t.proxy(renames["TableOut"]),
            "initialSplits": t.array(t.proxy(renames["SplitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["TableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "columnFamilies": t.struct({"_": t.string().optional()}).optional(),
            "granularity": t.string().optional(),
            "deletionProtection": t.boolean().optional(),
            "stats": t.proxy(renames["TableStatsIn"]).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "clusterStates": t.struct({"_": t.string().optional()}).optional(),
            "columnFamilies": t.struct({"_": t.string().optional()}).optional(),
            "granularity": t.string().optional(),
            "restoreInfo": t.proxy(renames["RestoreInfoOut"]).optional(),
            "deletionProtection": t.boolean().optional(),
            "stats": t.proxy(renames["TableStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["ClusterStateIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ClusterStateIn"]
    )
    types["ClusterStateOut"] = t.struct(
        {
            "replicationState": t.string().optional(),
            "encryptionInfo": t.array(t.proxy(renames["EncryptionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterStateOut"])
    types["EncryptionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EncryptionInfoIn"]
    )
    types["EncryptionInfoOut"] = t.struct(
        {
            "encryptionType": t.string().optional(),
            "encryptionStatus": t.proxy(renames["StatusOut"]).optional(),
            "kmsKeyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionInfoOut"])
    types["ColumnFamilyIn"] = t.struct(
        {
            "gcRule": t.proxy(renames["GcRuleIn"]).optional(),
            "stats": t.proxy(renames["ColumnFamilyStatsIn"]).optional(),
        }
    ).named(renames["ColumnFamilyIn"])
    types["ColumnFamilyOut"] = t.struct(
        {
            "gcRule": t.proxy(renames["GcRuleOut"]).optional(),
            "stats": t.proxy(renames["ColumnFamilyStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnFamilyOut"])
    types["GcRuleIn"] = t.struct(
        {
            "maxNumVersions": t.integer().optional(),
            "maxAge": t.string().optional(),
            "intersection": t.proxy(renames["IntersectionIn"]).optional(),
            "union": t.proxy(renames["UnionIn"]).optional(),
        }
    ).named(renames["GcRuleIn"])
    types["GcRuleOut"] = t.struct(
        {
            "maxNumVersions": t.integer().optional(),
            "maxAge": t.string().optional(),
            "intersection": t.proxy(renames["IntersectionOut"]).optional(),
            "union": t.proxy(renames["UnionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcRuleOut"])
    types["IntersectionIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["GcRuleIn"])).optional()}
    ).named(renames["IntersectionIn"])
    types["IntersectionOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["GcRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntersectionOut"])
    types["UnionIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["GcRuleIn"])).optional()}
    ).named(renames["UnionIn"])
    types["UnionOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["GcRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnionOut"])
    types["ColumnFamilyStatsIn"] = t.struct(
        {
            "averageColumnsPerRow": t.number().optional(),
            "averageCellsPerColumn": t.number().optional(),
            "logicalDataBytes": t.string().optional(),
        }
    ).named(renames["ColumnFamilyStatsIn"])
    types["ColumnFamilyStatsOut"] = t.struct(
        {
            "averageColumnsPerRow": t.number().optional(),
            "averageCellsPerColumn": t.number().optional(),
            "logicalDataBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnFamilyStatsOut"])
    types["RestoreInfoIn"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
        }
    ).named(renames["RestoreInfoIn"])
    types["RestoreInfoOut"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreInfoOut"])
    types["BackupInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BackupInfoIn"]
    )
    types["BackupInfoOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "sourceTable": t.string().optional(),
            "sourceBackup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupInfoOut"])
    types["TableStatsIn"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "averageColumnsPerRow": t.number().optional(),
            "averageCellsPerColumn": t.number().optional(),
            "logicalDataBytes": t.string().optional(),
        }
    ).named(renames["TableStatsIn"])
    types["TableStatsOut"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "averageColumnsPerRow": t.number().optional(),
            "averageCellsPerColumn": t.number().optional(),
            "logicalDataBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableStatsOut"])
    types["SplitIn"] = t.struct({"key": t.string().optional()}).named(
        renames["SplitIn"]
    )
    types["SplitOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitOut"])
    types["ListTablesResponseIn"] = t.struct(
        {
            "tables": t.array(t.proxy(renames["TableIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTablesResponseIn"])
    types["ListTablesResponseOut"] = t.struct(
        {
            "tables": t.array(t.proxy(renames["TableOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTablesResponseOut"])
    types["UndeleteTableRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteTableRequestIn"]
    )
    types["UndeleteTableRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteTableRequestOut"])
    types["ModifyColumnFamiliesRequestIn"] = t.struct(
        {"modifications": t.array(t.proxy(renames["ModificationIn"]))}
    ).named(renames["ModifyColumnFamiliesRequestIn"])
    types["ModifyColumnFamiliesRequestOut"] = t.struct(
        {
            "modifications": t.array(t.proxy(renames["ModificationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyColumnFamiliesRequestOut"])
    types["ModificationIn"] = t.struct(
        {
            "id": t.string().optional(),
            "create": t.proxy(renames["ColumnFamilyIn"]).optional(),
            "update": t.proxy(renames["ColumnFamilyIn"]).optional(),
            "drop": t.boolean().optional(),
        }
    ).named(renames["ModificationIn"])
    types["ModificationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "create": t.proxy(renames["ColumnFamilyOut"]).optional(),
            "update": t.proxy(renames["ColumnFamilyOut"]).optional(),
            "drop": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModificationOut"])
    types["DropRowRangeRequestIn"] = t.struct(
        {
            "rowKeyPrefix": t.string().optional(),
            "deleteAllDataFromTable": t.boolean().optional(),
        }
    ).named(renames["DropRowRangeRequestIn"])
    types["DropRowRangeRequestOut"] = t.struct(
        {
            "rowKeyPrefix": t.string().optional(),
            "deleteAllDataFromTable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DropRowRangeRequestOut"])
    types["GenerateConsistencyTokenRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateConsistencyTokenRequestIn"])
    types["GenerateConsistencyTokenRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateConsistencyTokenRequestOut"])
    types["GenerateConsistencyTokenResponseIn"] = t.struct(
        {"consistencyToken": t.string().optional()}
    ).named(renames["GenerateConsistencyTokenResponseIn"])
    types["GenerateConsistencyTokenResponseOut"] = t.struct(
        {
            "consistencyToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConsistencyTokenResponseOut"])
    types["CheckConsistencyRequestIn"] = t.struct(
        {"consistencyToken": t.string()}
    ).named(renames["CheckConsistencyRequestIn"])
    types["CheckConsistencyRequestOut"] = t.struct(
        {
            "consistencyToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckConsistencyRequestOut"])
    types["CheckConsistencyResponseIn"] = t.struct(
        {"consistent": t.boolean().optional()}
    ).named(renames["CheckConsistencyResponseIn"])
    types["CheckConsistencyResponseOut"] = t.struct(
        {
            "consistent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckConsistencyResponseOut"])
    types["BackupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceTable": t.string(),
            "expireTime": t.string(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceTable": t.string(),
            "sourceBackup": t.string().optional(),
            "expireTime": t.string(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "state": t.string().optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["RestoreTableRequestIn"] = t.struct(
        {"tableId": t.string(), "backup": t.string().optional()}
    ).named(renames["RestoreTableRequestIn"])
    types["RestoreTableRequestOut"] = t.struct(
        {
            "tableId": t.string(),
            "backup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreTableRequestOut"])
    types["CopyBackupRequestIn"] = t.struct(
        {"backupId": t.string(), "sourceBackup": t.string(), "expireTime": t.string()}
    ).named(renames["CopyBackupRequestIn"])
    types["CopyBackupRequestOut"] = t.struct(
        {
            "backupId": t.string(),
            "sourceBackup": t.string(),
            "expireTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupRequestOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CreateInstanceMetadataIn"] = t.struct(
        {
            "originalRequest": t.proxy(renames["CreateInstanceRequestIn"]).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
        }
    ).named(renames["CreateInstanceMetadataIn"])
    types["CreateInstanceMetadataOut"] = t.struct(
        {
            "originalRequest": t.proxy(renames["CreateInstanceRequestOut"]).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceMetadataOut"])
    types["UpdateInstanceMetadataIn"] = t.struct(
        {
            "originalRequest": t.proxy(
                renames["PartialUpdateInstanceRequestIn"]
            ).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
        }
    ).named(renames["UpdateInstanceMetadataIn"])
    types["UpdateInstanceMetadataOut"] = t.struct(
        {
            "originalRequest": t.proxy(
                renames["PartialUpdateInstanceRequestOut"]
            ).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceMetadataOut"])
    types["PartialUpdateInstanceRequestIn"] = t.struct(
        {"instance": t.proxy(renames["InstanceIn"]), "updateMask": t.string()}
    ).named(renames["PartialUpdateInstanceRequestIn"])
    types["PartialUpdateInstanceRequestOut"] = t.struct(
        {
            "instance": t.proxy(renames["InstanceOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialUpdateInstanceRequestOut"])
    types["CreateClusterMetadataIn"] = t.struct(
        {
            "originalRequest": t.proxy(renames["CreateClusterRequestIn"]).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "tables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CreateClusterMetadataIn"])
    types["CreateClusterMetadataOut"] = t.struct(
        {
            "originalRequest": t.proxy(renames["CreateClusterRequestOut"]).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "tables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterMetadataOut"])
    types["CreateClusterRequestIn"] = t.struct(
        {
            "parent": t.string(),
            "clusterId": t.string(),
            "cluster": t.proxy(renames["ClusterIn"]),
        }
    ).named(renames["CreateClusterRequestIn"])
    types["CreateClusterRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "clusterId": t.string(),
            "cluster": t.proxy(renames["ClusterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterRequestOut"])
    types["TableProgressIn"] = t.struct(
        {
            "estimatedSizeBytes": t.string().optional(),
            "estimatedCopiedBytes": t.string().optional(),
            "state": t.string(),
        }
    ).named(renames["TableProgressIn"])
    types["TableProgressOut"] = t.struct(
        {
            "estimatedSizeBytes": t.string().optional(),
            "estimatedCopiedBytes": t.string().optional(),
            "state": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableProgressOut"])
    types["PartialUpdateClusterMetadataIn"] = t.struct(
        {
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(
                renames["PartialUpdateClusterRequestIn"]
            ).optional(),
        }
    ).named(renames["PartialUpdateClusterMetadataIn"])
    types["PartialUpdateClusterMetadataOut"] = t.struct(
        {
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(
                renames["PartialUpdateClusterRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialUpdateClusterMetadataOut"])
    types["PartialUpdateClusterRequestIn"] = t.struct(
        {"cluster": t.proxy(renames["ClusterIn"]), "updateMask": t.string()}
    ).named(renames["PartialUpdateClusterRequestIn"])
    types["PartialUpdateClusterRequestOut"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialUpdateClusterRequestOut"])
    types["UpdateClusterMetadataIn"] = t.struct(
        {
            "originalRequest": t.proxy(renames["ClusterIn"]).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
        }
    ).named(renames["UpdateClusterMetadataIn"])
    types["UpdateClusterMetadataOut"] = t.struct(
        {
            "originalRequest": t.proxy(renames["ClusterOut"]).optional(),
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateClusterMetadataOut"])
    types["UpdateAppProfileMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateAppProfileMetadataIn"]
    )
    types["UpdateAppProfileMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateAppProfileMetadataOut"])
    types["CreateBackupMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceTable": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["CreateBackupMetadataIn"])
    types["CreateBackupMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceTable": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBackupMetadataOut"])
    types["CopyBackupMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceBackupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["CopyBackupMetadataIn"])
    types["CopyBackupMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceBackupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupMetadataOut"])
    types["OperationProgressIn"] = t.struct(
        {
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
    types["RestoreTableMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceType": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoIn"]),
            "optimizeTableOperationName": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["RestoreTableMetadataIn"])
    types["RestoreTableMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceType": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoOut"]),
            "optimizeTableOperationName": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreTableMetadataOut"])
    types["OptimizeRestoredTableMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["OptimizeRestoredTableMetadataIn"])
    types["OptimizeRestoredTableMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptimizeRestoredTableMetadataOut"])
    types["UndeleteTableMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["UndeleteTableMetadataIn"])
    types["UndeleteTableMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteTableMetadataOut"])
    types["UpdateTableMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["UpdateTableMetadataIn"])
    types["UpdateTableMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTableMetadataOut"])

    functions = {}
    functions["operationsGet"] = bigtableadmin.post(
        "v2/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = bigtableadmin.post(
        "v2/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = bigtableadmin.post(
        "v2/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsProjectsOperationsList"] = bigtableadmin.get(
        "v2/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesCreate"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGet"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesList"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesUpdate"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesPartialUpdateInstance"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDelete"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGetIamPolicy"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesSetIamPolicy"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTestIamPermissions"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersCreate"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersGet"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersList"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersUpdate"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersPartialUpdateCluster"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersDelete"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersHotTabletsList"] = bigtableadmin.get(
        "v2/{parent}/hotTablets",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string().optional(),
                "endTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListHotTabletsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsCreate"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsGet"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsPatch"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsDelete"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsList"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsCopy"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsGetIamPolicy"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsSetIamPolicy"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsInstancesClustersBackupsTestIamPermissions"
    ] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesCreate"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "ignoreWarnings": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesGet"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "ignoreWarnings": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesList"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "ignoreWarnings": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesPatch"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "ignoreWarnings": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesDelete"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "ignoreWarnings": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesCreate"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesList"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesGet"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesPatch"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesDelete"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesUndelete"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesModifyColumnFamilies"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesDropRowRange"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesGenerateConsistencyToken"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesCheckConsistency"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesRestore"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesGetIamPolicy"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesSetIamPolicy"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesTestIamPermissions"] = bigtableadmin.post(
        "v2/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigtableadmin",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
