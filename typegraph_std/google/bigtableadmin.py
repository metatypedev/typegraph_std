from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_bigtableadmin():
    bigtableadmin = HTTPRuntime("https://bigtableadmin.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigtableadmin_1_ErrorResponse",
        "IntersectionIn": "_bigtableadmin_2_IntersectionIn",
        "IntersectionOut": "_bigtableadmin_3_IntersectionOut",
        "BackupInfoIn": "_bigtableadmin_4_BackupInfoIn",
        "BackupInfoOut": "_bigtableadmin_5_BackupInfoOut",
        "OperationIn": "_bigtableadmin_6_OperationIn",
        "OperationOut": "_bigtableadmin_7_OperationOut",
        "BackupIn": "_bigtableadmin_8_BackupIn",
        "BackupOut": "_bigtableadmin_9_BackupOut",
        "TestIamPermissionsResponseIn": "_bigtableadmin_10_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigtableadmin_11_TestIamPermissionsResponseOut",
        "ListLocationsResponseIn": "_bigtableadmin_12_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_bigtableadmin_13_ListLocationsResponseOut",
        "TableProgressIn": "_bigtableadmin_14_TableProgressIn",
        "TableProgressOut": "_bigtableadmin_15_TableProgressOut",
        "SingleClusterRoutingIn": "_bigtableadmin_16_SingleClusterRoutingIn",
        "SingleClusterRoutingOut": "_bigtableadmin_17_SingleClusterRoutingOut",
        "LocationIn": "_bigtableadmin_18_LocationIn",
        "LocationOut": "_bigtableadmin_19_LocationOut",
        "EmptyIn": "_bigtableadmin_20_EmptyIn",
        "EmptyOut": "_bigtableadmin_21_EmptyOut",
        "ExprIn": "_bigtableadmin_22_ExprIn",
        "ExprOut": "_bigtableadmin_23_ExprOut",
        "AuditConfigIn": "_bigtableadmin_24_AuditConfigIn",
        "AuditConfigOut": "_bigtableadmin_25_AuditConfigOut",
        "SplitIn": "_bigtableadmin_26_SplitIn",
        "SplitOut": "_bigtableadmin_27_SplitOut",
        "GetIamPolicyRequestIn": "_bigtableadmin_28_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigtableadmin_29_GetIamPolicyRequestOut",
        "CheckConsistencyRequestIn": "_bigtableadmin_30_CheckConsistencyRequestIn",
        "CheckConsistencyRequestOut": "_bigtableadmin_31_CheckConsistencyRequestOut",
        "ListHotTabletsResponseIn": "_bigtableadmin_32_ListHotTabletsResponseIn",
        "ListHotTabletsResponseOut": "_bigtableadmin_33_ListHotTabletsResponseOut",
        "AppProfileIn": "_bigtableadmin_34_AppProfileIn",
        "AppProfileOut": "_bigtableadmin_35_AppProfileOut",
        "GenerateConsistencyTokenResponseIn": "_bigtableadmin_36_GenerateConsistencyTokenResponseIn",
        "GenerateConsistencyTokenResponseOut": "_bigtableadmin_37_GenerateConsistencyTokenResponseOut",
        "CreateBackupMetadataIn": "_bigtableadmin_38_CreateBackupMetadataIn",
        "CreateBackupMetadataOut": "_bigtableadmin_39_CreateBackupMetadataOut",
        "TableIn": "_bigtableadmin_40_TableIn",
        "TableOut": "_bigtableadmin_41_TableOut",
        "GenerateConsistencyTokenRequestIn": "_bigtableadmin_42_GenerateConsistencyTokenRequestIn",
        "GenerateConsistencyTokenRequestOut": "_bigtableadmin_43_GenerateConsistencyTokenRequestOut",
        "CreateClusterRequestIn": "_bigtableadmin_44_CreateClusterRequestIn",
        "CreateClusterRequestOut": "_bigtableadmin_45_CreateClusterRequestOut",
        "PartialUpdateInstanceRequestIn": "_bigtableadmin_46_PartialUpdateInstanceRequestIn",
        "PartialUpdateInstanceRequestOut": "_bigtableadmin_47_PartialUpdateInstanceRequestOut",
        "CheckConsistencyResponseIn": "_bigtableadmin_48_CheckConsistencyResponseIn",
        "CheckConsistencyResponseOut": "_bigtableadmin_49_CheckConsistencyResponseOut",
        "ListOperationsResponseIn": "_bigtableadmin_50_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_bigtableadmin_51_ListOperationsResponseOut",
        "RestoreInfoIn": "_bigtableadmin_52_RestoreInfoIn",
        "RestoreInfoOut": "_bigtableadmin_53_RestoreInfoOut",
        "UndeleteTableRequestIn": "_bigtableadmin_54_UndeleteTableRequestIn",
        "UndeleteTableRequestOut": "_bigtableadmin_55_UndeleteTableRequestOut",
        "CopyBackupMetadataIn": "_bigtableadmin_56_CopyBackupMetadataIn",
        "CopyBackupMetadataOut": "_bigtableadmin_57_CopyBackupMetadataOut",
        "ClusterAutoscalingConfigIn": "_bigtableadmin_58_ClusterAutoscalingConfigIn",
        "ClusterAutoscalingConfigOut": "_bigtableadmin_59_ClusterAutoscalingConfigOut",
        "GcRuleIn": "_bigtableadmin_60_GcRuleIn",
        "GcRuleOut": "_bigtableadmin_61_GcRuleOut",
        "ModifyColumnFamiliesRequestIn": "_bigtableadmin_62_ModifyColumnFamiliesRequestIn",
        "ModifyColumnFamiliesRequestOut": "_bigtableadmin_63_ModifyColumnFamiliesRequestOut",
        "PolicyIn": "_bigtableadmin_64_PolicyIn",
        "PolicyOut": "_bigtableadmin_65_PolicyOut",
        "UpdateClusterMetadataIn": "_bigtableadmin_66_UpdateClusterMetadataIn",
        "UpdateClusterMetadataOut": "_bigtableadmin_67_UpdateClusterMetadataOut",
        "RestoreTableMetadataIn": "_bigtableadmin_68_RestoreTableMetadataIn",
        "RestoreTableMetadataOut": "_bigtableadmin_69_RestoreTableMetadataOut",
        "CopyBackupRequestIn": "_bigtableadmin_70_CopyBackupRequestIn",
        "CopyBackupRequestOut": "_bigtableadmin_71_CopyBackupRequestOut",
        "UpdateTableMetadataIn": "_bigtableadmin_72_UpdateTableMetadataIn",
        "UpdateTableMetadataOut": "_bigtableadmin_73_UpdateTableMetadataOut",
        "UnionIn": "_bigtableadmin_74_UnionIn",
        "UnionOut": "_bigtableadmin_75_UnionOut",
        "ColumnFamilyStatsIn": "_bigtableadmin_76_ColumnFamilyStatsIn",
        "ColumnFamilyStatsOut": "_bigtableadmin_77_ColumnFamilyStatsOut",
        "TableStatsIn": "_bigtableadmin_78_TableStatsIn",
        "TableStatsOut": "_bigtableadmin_79_TableStatsOut",
        "ListTablesResponseIn": "_bigtableadmin_80_ListTablesResponseIn",
        "ListTablesResponseOut": "_bigtableadmin_81_ListTablesResponseOut",
        "UpdateAppProfileMetadataIn": "_bigtableadmin_82_UpdateAppProfileMetadataIn",
        "UpdateAppProfileMetadataOut": "_bigtableadmin_83_UpdateAppProfileMetadataOut",
        "UpdateInstanceMetadataIn": "_bigtableadmin_84_UpdateInstanceMetadataIn",
        "UpdateInstanceMetadataOut": "_bigtableadmin_85_UpdateInstanceMetadataOut",
        "ColumnFamilyIn": "_bigtableadmin_86_ColumnFamilyIn",
        "ColumnFamilyOut": "_bigtableadmin_87_ColumnFamilyOut",
        "AutoscalingLimitsIn": "_bigtableadmin_88_AutoscalingLimitsIn",
        "AutoscalingLimitsOut": "_bigtableadmin_89_AutoscalingLimitsOut",
        "ListAppProfilesResponseIn": "_bigtableadmin_90_ListAppProfilesResponseIn",
        "ListAppProfilesResponseOut": "_bigtableadmin_91_ListAppProfilesResponseOut",
        "ClusterConfigIn": "_bigtableadmin_92_ClusterConfigIn",
        "ClusterConfigOut": "_bigtableadmin_93_ClusterConfigOut",
        "ListInstancesResponseIn": "_bigtableadmin_94_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_bigtableadmin_95_ListInstancesResponseOut",
        "HotTabletIn": "_bigtableadmin_96_HotTabletIn",
        "HotTabletOut": "_bigtableadmin_97_HotTabletOut",
        "ClusterStateIn": "_bigtableadmin_98_ClusterStateIn",
        "ClusterStateOut": "_bigtableadmin_99_ClusterStateOut",
        "CreateInstanceRequestIn": "_bigtableadmin_100_CreateInstanceRequestIn",
        "CreateInstanceRequestOut": "_bigtableadmin_101_CreateInstanceRequestOut",
        "ListClustersResponseIn": "_bigtableadmin_102_ListClustersResponseIn",
        "ListClustersResponseOut": "_bigtableadmin_103_ListClustersResponseOut",
        "MultiClusterRoutingUseAnyIn": "_bigtableadmin_104_MultiClusterRoutingUseAnyIn",
        "MultiClusterRoutingUseAnyOut": "_bigtableadmin_105_MultiClusterRoutingUseAnyOut",
        "AutoscalingTargetsIn": "_bigtableadmin_106_AutoscalingTargetsIn",
        "AutoscalingTargetsOut": "_bigtableadmin_107_AutoscalingTargetsOut",
        "ModificationIn": "_bigtableadmin_108_ModificationIn",
        "ModificationOut": "_bigtableadmin_109_ModificationOut",
        "ClusterIn": "_bigtableadmin_110_ClusterIn",
        "ClusterOut": "_bigtableadmin_111_ClusterOut",
        "UndeleteTableMetadataIn": "_bigtableadmin_112_UndeleteTableMetadataIn",
        "UndeleteTableMetadataOut": "_bigtableadmin_113_UndeleteTableMetadataOut",
        "AuditLogConfigIn": "_bigtableadmin_114_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigtableadmin_115_AuditLogConfigOut",
        "DropRowRangeRequestIn": "_bigtableadmin_116_DropRowRangeRequestIn",
        "DropRowRangeRequestOut": "_bigtableadmin_117_DropRowRangeRequestOut",
        "CreateClusterMetadataIn": "_bigtableadmin_118_CreateClusterMetadataIn",
        "CreateClusterMetadataOut": "_bigtableadmin_119_CreateClusterMetadataOut",
        "EncryptionConfigIn": "_bigtableadmin_120_EncryptionConfigIn",
        "EncryptionConfigOut": "_bigtableadmin_121_EncryptionConfigOut",
        "RestoreTableRequestIn": "_bigtableadmin_122_RestoreTableRequestIn",
        "RestoreTableRequestOut": "_bigtableadmin_123_RestoreTableRequestOut",
        "PartialUpdateClusterRequestIn": "_bigtableadmin_124_PartialUpdateClusterRequestIn",
        "PartialUpdateClusterRequestOut": "_bigtableadmin_125_PartialUpdateClusterRequestOut",
        "BindingIn": "_bigtableadmin_126_BindingIn",
        "BindingOut": "_bigtableadmin_127_BindingOut",
        "CreateTableRequestIn": "_bigtableadmin_128_CreateTableRequestIn",
        "CreateTableRequestOut": "_bigtableadmin_129_CreateTableRequestOut",
        "InstanceIn": "_bigtableadmin_130_InstanceIn",
        "InstanceOut": "_bigtableadmin_131_InstanceOut",
        "ListBackupsResponseIn": "_bigtableadmin_132_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_bigtableadmin_133_ListBackupsResponseOut",
        "GetPolicyOptionsIn": "_bigtableadmin_134_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigtableadmin_135_GetPolicyOptionsOut",
        "EncryptionInfoIn": "_bigtableadmin_136_EncryptionInfoIn",
        "EncryptionInfoOut": "_bigtableadmin_137_EncryptionInfoOut",
        "SetIamPolicyRequestIn": "_bigtableadmin_138_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigtableadmin_139_SetIamPolicyRequestOut",
        "StatusIn": "_bigtableadmin_140_StatusIn",
        "StatusOut": "_bigtableadmin_141_StatusOut",
        "OperationProgressIn": "_bigtableadmin_142_OperationProgressIn",
        "OperationProgressOut": "_bigtableadmin_143_OperationProgressOut",
        "OptimizeRestoredTableMetadataIn": "_bigtableadmin_144_OptimizeRestoredTableMetadataIn",
        "OptimizeRestoredTableMetadataOut": "_bigtableadmin_145_OptimizeRestoredTableMetadataOut",
        "CreateInstanceMetadataIn": "_bigtableadmin_146_CreateInstanceMetadataIn",
        "CreateInstanceMetadataOut": "_bigtableadmin_147_CreateInstanceMetadataOut",
        "PartialUpdateClusterMetadataIn": "_bigtableadmin_148_PartialUpdateClusterMetadataIn",
        "PartialUpdateClusterMetadataOut": "_bigtableadmin_149_PartialUpdateClusterMetadataOut",
        "TestIamPermissionsRequestIn": "_bigtableadmin_150_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigtableadmin_151_TestIamPermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["IntersectionIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["GcRuleIn"])).optional()}
    ).named(renames["IntersectionIn"])
    types["IntersectionOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["GcRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntersectionOut"])
    types["BackupInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["BackupInfoIn"]
    )
    types["BackupInfoOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "sourceBackup": t.string().optional(),
            "sourceTable": t.string().optional(),
            "startTime": t.string().optional(),
            "backup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupInfoOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["BackupIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceTable": t.string(),
            "expireTime": t.string(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "name": t.string().optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "sourceTable": t.string(),
            "startTime": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "expireTime": t.string(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["TableProgressIn"] = t.struct(
        {
            "estimatedSizeBytes": t.string().optional(),
            "state": t.string(),
            "estimatedCopiedBytes": t.string().optional(),
        }
    ).named(renames["TableProgressIn"])
    types["TableProgressOut"] = t.struct(
        {
            "estimatedSizeBytes": t.string().optional(),
            "state": t.string(),
            "estimatedCopiedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableProgressOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["SplitIn"] = t.struct({"key": t.string().optional()}).named(
        renames["SplitIn"]
    )
    types["SplitOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["CheckConsistencyRequestIn"] = t.struct(
        {"consistencyToken": t.string()}
    ).named(renames["CheckConsistencyRequestIn"])
    types["CheckConsistencyRequestOut"] = t.struct(
        {
            "consistencyToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckConsistencyRequestOut"])
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
    types["AppProfileIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "singleClusterRouting": t.proxy(
                renames["SingleClusterRoutingIn"]
            ).optional(),
            "multiClusterRoutingUseAny": t.proxy(
                renames["MultiClusterRoutingUseAnyIn"]
            ).optional(),
        }
    ).named(renames["AppProfileIn"])
    types["AppProfileOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "singleClusterRouting": t.proxy(
                renames["SingleClusterRoutingOut"]
            ).optional(),
            "multiClusterRoutingUseAny": t.proxy(
                renames["MultiClusterRoutingUseAnyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProfileOut"])
    types["GenerateConsistencyTokenResponseIn"] = t.struct(
        {"consistencyToken": t.string().optional()}
    ).named(renames["GenerateConsistencyTokenResponseIn"])
    types["GenerateConsistencyTokenResponseOut"] = t.struct(
        {
            "consistencyToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConsistencyTokenResponseOut"])
    types["CreateBackupMetadataIn"] = t.struct(
        {
            "sourceTable": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["CreateBackupMetadataIn"])
    types["CreateBackupMetadataOut"] = t.struct(
        {
            "sourceTable": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBackupMetadataOut"])
    types["TableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "stats": t.proxy(renames["TableStatsIn"]).optional(),
            "deletionProtection": t.boolean().optional(),
            "granularity": t.string().optional(),
            "columnFamilies": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "stats": t.proxy(renames["TableStatsOut"]).optional(),
            "deletionProtection": t.boolean().optional(),
            "granularity": t.string().optional(),
            "clusterStates": t.struct({"_": t.string().optional()}).optional(),
            "columnFamilies": t.struct({"_": t.string().optional()}).optional(),
            "restoreInfo": t.proxy(renames["RestoreInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["GenerateConsistencyTokenRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateConsistencyTokenRequestIn"])
    types["GenerateConsistencyTokenRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateConsistencyTokenRequestOut"])
    types["CreateClusterRequestIn"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterIn"]),
            "clusterId": t.string(),
            "parent": t.string(),
        }
    ).named(renames["CreateClusterRequestIn"])
    types["CreateClusterRequestOut"] = t.struct(
        {
            "cluster": t.proxy(renames["ClusterOut"]),
            "clusterId": t.string(),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterRequestOut"])
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
    types["CheckConsistencyResponseIn"] = t.struct(
        {"consistent": t.boolean().optional()}
    ).named(renames["CheckConsistencyResponseIn"])
    types["CheckConsistencyResponseOut"] = t.struct(
        {
            "consistent": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckConsistencyResponseOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["RestoreInfoIn"] = t.struct(
        {
            "backupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
            "sourceType": t.string().optional(),
        }
    ).named(renames["RestoreInfoIn"])
    types["RestoreInfoOut"] = t.struct(
        {
            "backupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "sourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreInfoOut"])
    types["UndeleteTableRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteTableRequestIn"]
    )
    types["UndeleteTableRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteTableRequestOut"])
    types["CopyBackupMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "sourceBackupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CopyBackupMetadataIn"])
    types["CopyBackupMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "sourceBackupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupMetadataOut"])
    types["ClusterAutoscalingConfigIn"] = t.struct(
        {
            "autoscalingTargets": t.proxy(renames["AutoscalingTargetsIn"]),
            "autoscalingLimits": t.proxy(renames["AutoscalingLimitsIn"]),
        }
    ).named(renames["ClusterAutoscalingConfigIn"])
    types["ClusterAutoscalingConfigOut"] = t.struct(
        {
            "autoscalingTargets": t.proxy(renames["AutoscalingTargetsOut"]),
            "autoscalingLimits": t.proxy(renames["AutoscalingLimitsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterAutoscalingConfigOut"])
    types["GcRuleIn"] = t.struct(
        {
            "union": t.proxy(renames["UnionIn"]).optional(),
            "intersection": t.proxy(renames["IntersectionIn"]).optional(),
            "maxAge": t.string().optional(),
            "maxNumVersions": t.integer().optional(),
        }
    ).named(renames["GcRuleIn"])
    types["GcRuleOut"] = t.struct(
        {
            "union": t.proxy(renames["UnionOut"]).optional(),
            "intersection": t.proxy(renames["IntersectionOut"]).optional(),
            "maxAge": t.string().optional(),
            "maxNumVersions": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcRuleOut"])
    types["ModifyColumnFamiliesRequestIn"] = t.struct(
        {
            "modifications": t.array(t.proxy(renames["ModificationIn"])),
            "ignoreWarnings": t.boolean().optional(),
        }
    ).named(renames["ModifyColumnFamiliesRequestIn"])
    types["ModifyColumnFamiliesRequestOut"] = t.struct(
        {
            "modifications": t.array(t.proxy(renames["ModificationOut"])),
            "ignoreWarnings": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyColumnFamiliesRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["UpdateClusterMetadataIn"] = t.struct(
        {
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(renames["ClusterIn"]).optional(),
        }
    ).named(renames["UpdateClusterMetadataIn"])
    types["UpdateClusterMetadataOut"] = t.struct(
        {
            "requestTime": t.string().optional(),
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(renames["ClusterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateClusterMetadataOut"])
    types["RestoreTableMetadataIn"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "name": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoIn"]),
            "optimizeTableOperationName": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["RestoreTableMetadataIn"])
    types["RestoreTableMetadataOut"] = t.struct(
        {
            "sourceType": t.string().optional(),
            "name": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoOut"]),
            "optimizeTableOperationName": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreTableMetadataOut"])
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
            "logicalDataBytes": t.string().optional(),
            "averageCellsPerColumn": t.number().optional(),
        }
    ).named(renames["ColumnFamilyStatsIn"])
    types["ColumnFamilyStatsOut"] = t.struct(
        {
            "averageColumnsPerRow": t.number().optional(),
            "logicalDataBytes": t.string().optional(),
            "averageCellsPerColumn": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnFamilyStatsOut"])
    types["TableStatsIn"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "logicalDataBytes": t.string().optional(),
            "averageColumnsPerRow": t.number().optional(),
            "averageCellsPerColumn": t.number().optional(),
        }
    ).named(renames["TableStatsIn"])
    types["TableStatsOut"] = t.struct(
        {
            "rowCount": t.string().optional(),
            "logicalDataBytes": t.string().optional(),
            "averageColumnsPerRow": t.number().optional(),
            "averageCellsPerColumn": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableStatsOut"])
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
    types["UpdateAppProfileMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateAppProfileMetadataIn"]
    )
    types["UpdateAppProfileMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateAppProfileMetadataOut"])
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
    types["ColumnFamilyIn"] = t.struct(
        {
            "stats": t.proxy(renames["ColumnFamilyStatsIn"]).optional(),
            "gcRule": t.proxy(renames["GcRuleIn"]).optional(),
        }
    ).named(renames["ColumnFamilyIn"])
    types["ColumnFamilyOut"] = t.struct(
        {
            "stats": t.proxy(renames["ColumnFamilyStatsOut"]).optional(),
            "gcRule": t.proxy(renames["GcRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnFamilyOut"])
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
    types["ListAppProfilesResponseIn"] = t.struct(
        {
            "failedLocations": t.array(t.string()).optional(),
            "appProfiles": t.array(t.proxy(renames["AppProfileIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAppProfilesResponseIn"])
    types["ListAppProfilesResponseOut"] = t.struct(
        {
            "failedLocations": t.array(t.string()).optional(),
            "appProfiles": t.array(t.proxy(renames["AppProfileOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAppProfilesResponseOut"])
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
    types["ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "failedLocations": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "failedLocations": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["HotTabletIn"] = t.struct(
        {
            "endKey": t.string().optional(),
            "startKey": t.string().optional(),
            "name": t.string().optional(),
            "tableName": t.string().optional(),
        }
    ).named(renames["HotTabletIn"])
    types["HotTabletOut"] = t.struct(
        {
            "endKey": t.string().optional(),
            "startKey": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "tableName": t.string().optional(),
            "nodeCpuUsagePercent": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HotTabletOut"])
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
    types["CreateInstanceRequestIn"] = t.struct(
        {
            "clusters": t.struct({"_": t.string().optional()}),
            "instanceId": t.string(),
            "instance": t.proxy(renames["InstanceIn"]),
            "parent": t.string(),
        }
    ).named(renames["CreateInstanceRequestIn"])
    types["CreateInstanceRequestOut"] = t.struct(
        {
            "clusters": t.struct({"_": t.string().optional()}),
            "instanceId": t.string(),
            "instance": t.proxy(renames["InstanceOut"]),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceRequestOut"])
    types["ListClustersResponseIn"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ClusterIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "failedLocations": t.array(t.string()).optional(),
        }
    ).named(renames["ListClustersResponseIn"])
    types["ListClustersResponseOut"] = t.struct(
        {
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "failedLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListClustersResponseOut"])
    types["MultiClusterRoutingUseAnyIn"] = t.struct(
        {"clusterIds": t.array(t.string()).optional()}
    ).named(renames["MultiClusterRoutingUseAnyIn"])
    types["MultiClusterRoutingUseAnyOut"] = t.struct(
        {
            "clusterIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClusterRoutingUseAnyOut"])
    types["AutoscalingTargetsIn"] = t.struct(
        {
            "storageUtilizationGibPerNode": t.integer().optional(),
            "cpuUtilizationPercent": t.integer().optional(),
        }
    ).named(renames["AutoscalingTargetsIn"])
    types["AutoscalingTargetsOut"] = t.struct(
        {
            "storageUtilizationGibPerNode": t.integer().optional(),
            "cpuUtilizationPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscalingTargetsOut"])
    types["ModificationIn"] = t.struct(
        {
            "drop": t.boolean().optional(),
            "create": t.proxy(renames["ColumnFamilyIn"]).optional(),
            "id": t.string().optional(),
            "update": t.proxy(renames["ColumnFamilyIn"]).optional(),
        }
    ).named(renames["ModificationIn"])
    types["ModificationOut"] = t.struct(
        {
            "drop": t.boolean().optional(),
            "create": t.proxy(renames["ColumnFamilyOut"]).optional(),
            "id": t.string().optional(),
            "update": t.proxy(renames["ColumnFamilyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModificationOut"])
    types["ClusterIn"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "location": t.string().optional(),
            "defaultStorageType": t.string().optional(),
            "name": t.string().optional(),
            "serveNodes": t.integer().optional(),
            "clusterConfig": t.proxy(renames["ClusterConfigIn"]).optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "location": t.string().optional(),
            "defaultStorageType": t.string().optional(),
            "name": t.string().optional(),
            "serveNodes": t.integer().optional(),
            "state": t.string().optional(),
            "clusterConfig": t.proxy(renames["ClusterConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
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
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["DropRowRangeRequestIn"] = t.struct(
        {
            "deleteAllDataFromTable": t.boolean().optional(),
            "rowKeyPrefix": t.string().optional(),
        }
    ).named(renames["DropRowRangeRequestIn"])
    types["DropRowRangeRequestOut"] = t.struct(
        {
            "deleteAllDataFromTable": t.boolean().optional(),
            "rowKeyPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DropRowRangeRequestOut"])
    types["CreateClusterMetadataIn"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(renames["CreateClusterRequestIn"]).optional(),
            "requestTime": t.string().optional(),
            "tables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CreateClusterMetadataIn"])
    types["CreateClusterMetadataOut"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(renames["CreateClusterRequestOut"]).optional(),
            "requestTime": t.string().optional(),
            "tables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateClusterMetadataOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["RestoreTableRequestIn"] = t.struct(
        {"backup": t.string().optional(), "tableId": t.string()}
    ).named(renames["RestoreTableRequestIn"])
    types["RestoreTableRequestOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "tableId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreTableRequestOut"])
    types["PartialUpdateClusterRequestIn"] = t.struct(
        {"updateMask": t.string(), "cluster": t.proxy(renames["ClusterIn"])}
    ).named(renames["PartialUpdateClusterRequestIn"])
    types["PartialUpdateClusterRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "cluster": t.proxy(renames["ClusterOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialUpdateClusterRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["CreateTableRequestIn"] = t.struct(
        {
            "table": t.proxy(renames["TableIn"]),
            "tableId": t.string(),
            "initialSplits": t.array(t.proxy(renames["SplitIn"])).optional(),
        }
    ).named(renames["CreateTableRequestIn"])
    types["CreateTableRequestOut"] = t.struct(
        {
            "table": t.proxy(renames["TableOut"]),
            "tableId": t.string(),
            "initialSplits": t.array(t.proxy(renames["SplitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTableRequestOut"])
    types["InstanceIn"] = t.struct(
        {
            "displayName": t.string(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string(),
            "satisfiesPzs": t.boolean().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["EncryptionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EncryptionInfoIn"]
    )
    types["EncryptionInfoOut"] = t.struct(
        {
            "encryptionStatus": t.proxy(renames["StatusOut"]).optional(),
            "kmsKeyVersion": t.string().optional(),
            "encryptionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionInfoOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["OperationProgressIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
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
    types["CreateInstanceMetadataIn"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(renames["CreateInstanceRequestIn"]).optional(),
            "requestTime": t.string().optional(),
        }
    ).named(renames["CreateInstanceMetadataIn"])
    types["CreateInstanceMetadataOut"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "originalRequest": t.proxy(renames["CreateInstanceRequestOut"]).optional(),
            "requestTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceMetadataOut"])
    types["PartialUpdateClusterMetadataIn"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "requestTime": t.string().optional(),
            "originalRequest": t.proxy(
                renames["PartialUpdateClusterRequestIn"]
            ).optional(),
        }
    ).named(renames["PartialUpdateClusterMetadataIn"])
    types["PartialUpdateClusterMetadataOut"] = t.struct(
        {
            "finishTime": t.string().optional(),
            "requestTime": t.string().optional(),
            "originalRequest": t.proxy(
                renames["PartialUpdateClusterRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialUpdateClusterMetadataOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])

    functions = {}
    functions["projectsInstancesGet"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesCreate"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesPartialUpdateInstance"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesSetIamPolicy"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTestIamPermissions"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDelete"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesList"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGetIamPolicy"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesUpdate"] = bigtableadmin.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "displayName": t.string(),
                "type": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
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
    functions["projectsInstancesClustersUpdate"] = bigtableadmin.delete(
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
    functions["projectsInstancesClustersGet"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsInstancesClustersDelete"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsTestIamPermissions"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsGetIamPolicy"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsSetIamPolicy"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsList"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsCreate"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsDelete"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsCopy"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsPatch"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersBackupsGet"] = bigtableadmin.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesClustersHotTabletsList"] = bigtableadmin.get(
        "v2/{parent}/hotTablets",
        t.struct(
            {
                "parent": t.string(),
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListHotTabletsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesGet"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesGetIamPolicy"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesModifyColumnFamilies"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesDropRowRange"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesUndelete"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesGenerateConsistencyToken"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesTestIamPermissions"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesPatch"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesList"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesRestore"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesSetIamPolicy"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesCreate"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesCheckConsistency"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTablesDelete"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesDelete"] = bigtableadmin.get(
        "v2/{parent}/appProfiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesPatch"] = bigtableadmin.get(
        "v2/{parent}/appProfiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesCreate"] = bigtableadmin.get(
        "v2/{parent}/appProfiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesGet"] = bigtableadmin.get(
        "v2/{parent}/appProfiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesAppProfilesList"] = bigtableadmin.get(
        "v2/{parent}/appProfiles",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppProfilesResponseOut"]),
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
    functions["operationsCancel"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = bigtableadmin.delete(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = bigtableadmin.delete(
        "v2/{name}",
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigtableadmin",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
