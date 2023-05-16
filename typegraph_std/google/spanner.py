from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_spanner() -> Import:
    spanner = HTTPRuntime("https://spanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_spanner_1_ErrorResponse",
        "UpdateInstanceConfigRequestIn": "_spanner_2_UpdateInstanceConfigRequestIn",
        "UpdateInstanceConfigRequestOut": "_spanner_3_UpdateInstanceConfigRequestOut",
        "ResultSetStatsIn": "_spanner_4_ResultSetStatsIn",
        "ResultSetStatsOut": "_spanner_5_ResultSetStatsOut",
        "ListBackupsResponseIn": "_spanner_6_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_spanner_7_ListBackupsResponseOut",
        "TestIamPermissionsRequestIn": "_spanner_8_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_spanner_9_TestIamPermissionsRequestOut",
        "UpdateDatabaseDdlRequestIn": "_spanner_10_UpdateDatabaseDdlRequestIn",
        "UpdateDatabaseDdlRequestOut": "_spanner_11_UpdateDatabaseDdlRequestOut",
        "PartitionIn": "_spanner_12_PartitionIn",
        "PartitionOut": "_spanner_13_PartitionOut",
        "ChildLinkIn": "_spanner_14_ChildLinkIn",
        "ChildLinkOut": "_spanner_15_ChildLinkOut",
        "UpdateInstanceMetadataIn": "_spanner_16_UpdateInstanceMetadataIn",
        "UpdateInstanceMetadataOut": "_spanner_17_UpdateInstanceMetadataOut",
        "StatusIn": "_spanner_18_StatusIn",
        "StatusOut": "_spanner_19_StatusOut",
        "ReplicaInfoIn": "_spanner_20_ReplicaInfoIn",
        "ReplicaInfoOut": "_spanner_21_ReplicaInfoOut",
        "BatchCreateSessionsResponseIn": "_spanner_22_BatchCreateSessionsResponseIn",
        "BatchCreateSessionsResponseOut": "_spanner_23_BatchCreateSessionsResponseOut",
        "EncryptionInfoIn": "_spanner_24_EncryptionInfoIn",
        "EncryptionInfoOut": "_spanner_25_EncryptionInfoOut",
        "InstanceConfigIn": "_spanner_26_InstanceConfigIn",
        "InstanceConfigOut": "_spanner_27_InstanceConfigOut",
        "PlanNodeIn": "_spanner_28_PlanNodeIn",
        "PlanNodeOut": "_spanner_29_PlanNodeOut",
        "PartitionedDmlIn": "_spanner_30_PartitionedDmlIn",
        "PartitionedDmlOut": "_spanner_31_PartitionedDmlOut",
        "ListDatabaseRolesResponseIn": "_spanner_32_ListDatabaseRolesResponseIn",
        "ListDatabaseRolesResponseOut": "_spanner_33_ListDatabaseRolesResponseOut",
        "CreateInstanceRequestIn": "_spanner_34_CreateInstanceRequestIn",
        "CreateInstanceRequestOut": "_spanner_35_CreateInstanceRequestOut",
        "WriteIn": "_spanner_36_WriteIn",
        "WriteOut": "_spanner_37_WriteOut",
        "ListOperationsResponseIn": "_spanner_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_spanner_39_ListOperationsResponseOut",
        "ReadWriteIn": "_spanner_40_ReadWriteIn",
        "ReadWriteOut": "_spanner_41_ReadWriteOut",
        "FieldIn": "_spanner_42_FieldIn",
        "FieldOut": "_spanner_43_FieldOut",
        "CreateBackupMetadataIn": "_spanner_44_CreateBackupMetadataIn",
        "CreateBackupMetadataOut": "_spanner_45_CreateBackupMetadataOut",
        "MutationIn": "_spanner_46_MutationIn",
        "MutationOut": "_spanner_47_MutationOut",
        "DatabaseRoleIn": "_spanner_48_DatabaseRoleIn",
        "DatabaseRoleOut": "_spanner_49_DatabaseRoleOut",
        "ListBackupOperationsResponseIn": "_spanner_50_ListBackupOperationsResponseIn",
        "ListBackupOperationsResponseOut": "_spanner_51_ListBackupOperationsResponseOut",
        "DatabaseIn": "_spanner_52_DatabaseIn",
        "DatabaseOut": "_spanner_53_DatabaseOut",
        "RestoreDatabaseEncryptionConfigIn": "_spanner_54_RestoreDatabaseEncryptionConfigIn",
        "RestoreDatabaseEncryptionConfigOut": "_spanner_55_RestoreDatabaseEncryptionConfigOut",
        "ExecuteBatchDmlRequestIn": "_spanner_56_ExecuteBatchDmlRequestIn",
        "ExecuteBatchDmlRequestOut": "_spanner_57_ExecuteBatchDmlRequestOut",
        "ListDatabaseOperationsResponseIn": "_spanner_58_ListDatabaseOperationsResponseIn",
        "ListDatabaseOperationsResponseOut": "_spanner_59_ListDatabaseOperationsResponseOut",
        "PrefixNodeIn": "_spanner_60_PrefixNodeIn",
        "PrefixNodeOut": "_spanner_61_PrefixNodeOut",
        "QueryPlanIn": "_spanner_62_QueryPlanIn",
        "QueryPlanOut": "_spanner_63_QueryPlanOut",
        "MetricIn": "_spanner_64_MetricIn",
        "MetricOut": "_spanner_65_MetricOut",
        "CommitStatsIn": "_spanner_66_CommitStatsIn",
        "CommitStatsOut": "_spanner_67_CommitStatsOut",
        "ExecuteBatchDmlResponseIn": "_spanner_68_ExecuteBatchDmlResponseIn",
        "ExecuteBatchDmlResponseOut": "_spanner_69_ExecuteBatchDmlResponseOut",
        "PartitionQueryRequestIn": "_spanner_70_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_spanner_71_PartitionQueryRequestOut",
        "CommitRequestIn": "_spanner_72_CommitRequestIn",
        "CommitRequestOut": "_spanner_73_CommitRequestOut",
        "CreateDatabaseMetadataIn": "_spanner_74_CreateDatabaseMetadataIn",
        "CreateDatabaseMetadataOut": "_spanner_75_CreateDatabaseMetadataOut",
        "GetPolicyOptionsIn": "_spanner_76_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_spanner_77_GetPolicyOptionsOut",
        "StatementIn": "_spanner_78_StatementIn",
        "StatementOut": "_spanner_79_StatementOut",
        "ListInstanceConfigsResponseIn": "_spanner_80_ListInstanceConfigsResponseIn",
        "ListInstanceConfigsResponseOut": "_spanner_81_ListInstanceConfigsResponseOut",
        "KeyRangeInfosIn": "_spanner_82_KeyRangeInfosIn",
        "KeyRangeInfosOut": "_spanner_83_KeyRangeInfosOut",
        "ListInstancesResponseIn": "_spanner_84_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_spanner_85_ListInstancesResponseOut",
        "EmptyIn": "_spanner_86_EmptyIn",
        "EmptyOut": "_spanner_87_EmptyOut",
        "CreateSessionRequestIn": "_spanner_88_CreateSessionRequestIn",
        "CreateSessionRequestOut": "_spanner_89_CreateSessionRequestOut",
        "ReadOnlyIn": "_spanner_90_ReadOnlyIn",
        "ReadOnlyOut": "_spanner_91_ReadOnlyOut",
        "CopyBackupRequestIn": "_spanner_92_CopyBackupRequestIn",
        "CopyBackupRequestOut": "_spanner_93_CopyBackupRequestOut",
        "CommitResponseIn": "_spanner_94_CommitResponseIn",
        "CommitResponseOut": "_spanner_95_CommitResponseOut",
        "TestIamPermissionsResponseIn": "_spanner_96_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_spanner_97_TestIamPermissionsResponseOut",
        "QueryOptionsIn": "_spanner_98_QueryOptionsIn",
        "QueryOptionsOut": "_spanner_99_QueryOptionsOut",
        "ExprIn": "_spanner_100_ExprIn",
        "ExprOut": "_spanner_101_ExprOut",
        "RestoreDatabaseMetadataIn": "_spanner_102_RestoreDatabaseMetadataIn",
        "RestoreDatabaseMetadataOut": "_spanner_103_RestoreDatabaseMetadataOut",
        "OptimizeRestoredDatabaseMetadataIn": "_spanner_104_OptimizeRestoredDatabaseMetadataIn",
        "OptimizeRestoredDatabaseMetadataOut": "_spanner_105_OptimizeRestoredDatabaseMetadataOut",
        "ScanIn": "_spanner_106_ScanIn",
        "ScanOut": "_spanner_107_ScanOut",
        "OperationProgressIn": "_spanner_108_OperationProgressIn",
        "OperationProgressOut": "_spanner_109_OperationProgressOut",
        "RollbackRequestIn": "_spanner_110_RollbackRequestIn",
        "RollbackRequestOut": "_spanner_111_RollbackRequestOut",
        "BatchCreateSessionsRequestIn": "_spanner_112_BatchCreateSessionsRequestIn",
        "BatchCreateSessionsRequestOut": "_spanner_113_BatchCreateSessionsRequestOut",
        "UpdateInstanceConfigMetadataIn": "_spanner_114_UpdateInstanceConfigMetadataIn",
        "UpdateInstanceConfigMetadataOut": "_spanner_115_UpdateInstanceConfigMetadataOut",
        "RestoreInfoIn": "_spanner_116_RestoreInfoIn",
        "RestoreInfoOut": "_spanner_117_RestoreInfoOut",
        "IndexedHotKeyIn": "_spanner_118_IndexedHotKeyIn",
        "IndexedHotKeyOut": "_spanner_119_IndexedHotKeyOut",
        "FreeInstanceMetadataIn": "_spanner_120_FreeInstanceMetadataIn",
        "FreeInstanceMetadataOut": "_spanner_121_FreeInstanceMetadataOut",
        "TypeIn": "_spanner_122_TypeIn",
        "TypeOut": "_spanner_123_TypeOut",
        "MetricMatrixRowIn": "_spanner_124_MetricMatrixRowIn",
        "MetricMatrixRowOut": "_spanner_125_MetricMatrixRowOut",
        "BindingIn": "_spanner_126_BindingIn",
        "BindingOut": "_spanner_127_BindingOut",
        "KeyRangeIn": "_spanner_128_KeyRangeIn",
        "KeyRangeOut": "_spanner_129_KeyRangeOut",
        "TransactionOptionsIn": "_spanner_130_TransactionOptionsIn",
        "TransactionOptionsOut": "_spanner_131_TransactionOptionsOut",
        "BeginTransactionRequestIn": "_spanner_132_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_spanner_133_BeginTransactionRequestOut",
        "UpdateDatabaseRequestIn": "_spanner_134_UpdateDatabaseRequestIn",
        "UpdateDatabaseRequestOut": "_spanner_135_UpdateDatabaseRequestOut",
        "CreateInstanceMetadataIn": "_spanner_136_CreateInstanceMetadataIn",
        "CreateInstanceMetadataOut": "_spanner_137_CreateInstanceMetadataOut",
        "UpdateDatabaseDdlMetadataIn": "_spanner_138_UpdateDatabaseDdlMetadataIn",
        "UpdateDatabaseDdlMetadataOut": "_spanner_139_UpdateDatabaseDdlMetadataOut",
        "ListDatabasesResponseIn": "_spanner_140_ListDatabasesResponseIn",
        "ListDatabasesResponseOut": "_spanner_141_ListDatabasesResponseOut",
        "LocalizedStringIn": "_spanner_142_LocalizedStringIn",
        "LocalizedStringOut": "_spanner_143_LocalizedStringOut",
        "StructTypeIn": "_spanner_144_StructTypeIn",
        "StructTypeOut": "_spanner_145_StructTypeOut",
        "TransactionSelectorIn": "_spanner_146_TransactionSelectorIn",
        "TransactionSelectorOut": "_spanner_147_TransactionSelectorOut",
        "UpdateDatabaseMetadataIn": "_spanner_148_UpdateDatabaseMetadataIn",
        "UpdateDatabaseMetadataOut": "_spanner_149_UpdateDatabaseMetadataOut",
        "PolicyIn": "_spanner_150_PolicyIn",
        "PolicyOut": "_spanner_151_PolicyOut",
        "PartialResultSetIn": "_spanner_152_PartialResultSetIn",
        "PartialResultSetOut": "_spanner_153_PartialResultSetOut",
        "BackupIn": "_spanner_154_BackupIn",
        "BackupOut": "_spanner_155_BackupOut",
        "OperationIn": "_spanner_156_OperationIn",
        "OperationOut": "_spanner_157_OperationOut",
        "VisualizationDataIn": "_spanner_158_VisualizationDataIn",
        "VisualizationDataOut": "_spanner_159_VisualizationDataOut",
        "TransactionIn": "_spanner_160_TransactionIn",
        "TransactionOut": "_spanner_161_TransactionOut",
        "ExecuteSqlRequestIn": "_spanner_162_ExecuteSqlRequestIn",
        "ExecuteSqlRequestOut": "_spanner_163_ExecuteSqlRequestOut",
        "ListSessionsResponseIn": "_spanner_164_ListSessionsResponseIn",
        "ListSessionsResponseOut": "_spanner_165_ListSessionsResponseOut",
        "CopyBackupEncryptionConfigIn": "_spanner_166_CopyBackupEncryptionConfigIn",
        "CopyBackupEncryptionConfigOut": "_spanner_167_CopyBackupEncryptionConfigOut",
        "SetIamPolicyRequestIn": "_spanner_168_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_spanner_169_SetIamPolicyRequestOut",
        "ContextValueIn": "_spanner_170_ContextValueIn",
        "ContextValueOut": "_spanner_171_ContextValueOut",
        "ListScansResponseIn": "_spanner_172_ListScansResponseIn",
        "ListScansResponseOut": "_spanner_173_ListScansResponseOut",
        "PartitionReadRequestIn": "_spanner_174_PartitionReadRequestIn",
        "PartitionReadRequestOut": "_spanner_175_PartitionReadRequestOut",
        "ResultSetIn": "_spanner_176_ResultSetIn",
        "ResultSetOut": "_spanner_177_ResultSetOut",
        "InstanceOperationProgressIn": "_spanner_178_InstanceOperationProgressIn",
        "InstanceOperationProgressOut": "_spanner_179_InstanceOperationProgressOut",
        "DerivedMetricIn": "_spanner_180_DerivedMetricIn",
        "DerivedMetricOut": "_spanner_181_DerivedMetricOut",
        "DeleteIn": "_spanner_182_DeleteIn",
        "DeleteOut": "_spanner_183_DeleteOut",
        "CreateDatabaseRequestIn": "_spanner_184_CreateDatabaseRequestIn",
        "CreateDatabaseRequestOut": "_spanner_185_CreateDatabaseRequestOut",
        "BackupInfoIn": "_spanner_186_BackupInfoIn",
        "BackupInfoOut": "_spanner_187_BackupInfoOut",
        "GetDatabaseDdlResponseIn": "_spanner_188_GetDatabaseDdlResponseIn",
        "GetDatabaseDdlResponseOut": "_spanner_189_GetDatabaseDdlResponseOut",
        "ScanDataIn": "_spanner_190_ScanDataIn",
        "ScanDataOut": "_spanner_191_ScanDataOut",
        "ShortRepresentationIn": "_spanner_192_ShortRepresentationIn",
        "ShortRepresentationOut": "_spanner_193_ShortRepresentationOut",
        "KeySetIn": "_spanner_194_KeySetIn",
        "KeySetOut": "_spanner_195_KeySetOut",
        "KeyRangeInfoIn": "_spanner_196_KeyRangeInfoIn",
        "KeyRangeInfoOut": "_spanner_197_KeyRangeInfoOut",
        "PartitionOptionsIn": "_spanner_198_PartitionOptionsIn",
        "PartitionOptionsOut": "_spanner_199_PartitionOptionsOut",
        "EncryptionConfigIn": "_spanner_200_EncryptionConfigIn",
        "EncryptionConfigOut": "_spanner_201_EncryptionConfigOut",
        "ListInstanceConfigOperationsResponseIn": "_spanner_202_ListInstanceConfigOperationsResponseIn",
        "ListInstanceConfigOperationsResponseOut": "_spanner_203_ListInstanceConfigOperationsResponseOut",
        "PartitionResponseIn": "_spanner_204_PartitionResponseIn",
        "PartitionResponseOut": "_spanner_205_PartitionResponseOut",
        "UpdateInstanceRequestIn": "_spanner_206_UpdateInstanceRequestIn",
        "UpdateInstanceRequestOut": "_spanner_207_UpdateInstanceRequestOut",
        "InstanceIn": "_spanner_208_InstanceIn",
        "InstanceOut": "_spanner_209_InstanceOut",
        "RestoreDatabaseRequestIn": "_spanner_210_RestoreDatabaseRequestIn",
        "RestoreDatabaseRequestOut": "_spanner_211_RestoreDatabaseRequestOut",
        "SessionIn": "_spanner_212_SessionIn",
        "SessionOut": "_spanner_213_SessionOut",
        "ReadRequestIn": "_spanner_214_ReadRequestIn",
        "ReadRequestOut": "_spanner_215_ReadRequestOut",
        "CreateInstanceConfigMetadataIn": "_spanner_216_CreateInstanceConfigMetadataIn",
        "CreateInstanceConfigMetadataOut": "_spanner_217_CreateInstanceConfigMetadataOut",
        "RequestOptionsIn": "_spanner_218_RequestOptionsIn",
        "RequestOptionsOut": "_spanner_219_RequestOptionsOut",
        "DiagnosticMessageIn": "_spanner_220_DiagnosticMessageIn",
        "DiagnosticMessageOut": "_spanner_221_DiagnosticMessageOut",
        "CopyBackupMetadataIn": "_spanner_222_CopyBackupMetadataIn",
        "CopyBackupMetadataOut": "_spanner_223_CopyBackupMetadataOut",
        "ResultSetMetadataIn": "_spanner_224_ResultSetMetadataIn",
        "ResultSetMetadataOut": "_spanner_225_ResultSetMetadataOut",
        "GetIamPolicyRequestIn": "_spanner_226_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_spanner_227_GetIamPolicyRequestOut",
        "CreateInstanceConfigRequestIn": "_spanner_228_CreateInstanceConfigRequestIn",
        "CreateInstanceConfigRequestOut": "_spanner_229_CreateInstanceConfigRequestOut",
        "IndexedKeyRangeInfosIn": "_spanner_230_IndexedKeyRangeInfosIn",
        "IndexedKeyRangeInfosOut": "_spanner_231_IndexedKeyRangeInfosOut",
        "MetricMatrixIn": "_spanner_232_MetricMatrixIn",
        "MetricMatrixOut": "_spanner_233_MetricMatrixOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UpdateInstanceConfigRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]),
            "updateMask": t.string(),
        }
    ).named(renames["UpdateInstanceConfigRequestIn"])
    types["UpdateInstanceConfigRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceConfigRequestOut"])
    types["ResultSetStatsIn"] = t.struct(
        {
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "queryPlan": t.proxy(renames["QueryPlanIn"]).optional(),
            "rowCountLowerBound": t.string().optional(),
            "rowCountExact": t.string().optional(),
        }
    ).named(renames["ResultSetStatsIn"])
    types["ResultSetStatsOut"] = t.struct(
        {
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "queryPlan": t.proxy(renames["QueryPlanOut"]).optional(),
            "rowCountLowerBound": t.string().optional(),
            "rowCountExact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetStatsOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["UpdateDatabaseDdlRequestIn"] = t.struct(
        {
            "statements": t.array(t.string()),
            "operationId": t.string().optional(),
            "protoDescriptors": t.string().optional(),
        }
    ).named(renames["UpdateDatabaseDdlRequestIn"])
    types["UpdateDatabaseDdlRequestOut"] = t.struct(
        {
            "statements": t.array(t.string()),
            "operationId": t.string().optional(),
            "protoDescriptors": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseDdlRequestOut"])
    types["PartitionIn"] = t.struct({"partitionToken": t.string().optional()}).named(
        renames["PartitionIn"]
    )
    types["PartitionOut"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionOut"])
    types["ChildLinkIn"] = t.struct(
        {
            "childIndex": t.integer().optional(),
            "type": t.string().optional(),
            "variable": t.string().optional(),
        }
    ).named(renames["ChildLinkIn"])
    types["ChildLinkOut"] = t.struct(
        {
            "childIndex": t.integer().optional(),
            "type": t.string().optional(),
            "variable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChildLinkOut"])
    types["UpdateInstanceMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceIn"]).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["UpdateInstanceMetadataIn"])
    types["UpdateInstanceMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceMetadataOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ReplicaInfoIn"] = t.struct(
        {
            "type": t.string().optional(),
            "defaultLeaderLocation": t.boolean().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ReplicaInfoIn"])
    types["ReplicaInfoOut"] = t.struct(
        {
            "type": t.string().optional(),
            "defaultLeaderLocation": t.boolean().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaInfoOut"])
    types["BatchCreateSessionsResponseIn"] = t.struct(
        {"session": t.array(t.proxy(renames["SessionIn"])).optional()}
    ).named(renames["BatchCreateSessionsResponseIn"])
    types["BatchCreateSessionsResponseOut"] = t.struct(
        {
            "session": t.array(t.proxy(renames["SessionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateSessionsResponseOut"])
    types["EncryptionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EncryptionInfoIn"]
    )
    types["EncryptionInfoOut"] = t.struct(
        {
            "kmsKeyVersion": t.string().optional(),
            "encryptionType": t.string().optional(),
            "encryptionStatus": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionInfoOut"])
    types["InstanceConfigIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoIn"])).optional(),
            "displayName": t.string().optional(),
            "baseConfig": t.string().optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["InstanceConfigIn"])
    types["InstanceConfigOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "displayName": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "optionalReplicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "baseConfig": t.string().optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "configType": t.string().optional(),
            "name": t.string().optional(),
            "freeInstanceAvailability": t.string().optional(),
            "state": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["PlanNodeIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "index": t.integer().optional(),
            "displayName": t.string().optional(),
            "shortRepresentation": t.proxy(renames["ShortRepresentationIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkIn"])).optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PlanNodeIn"])
    types["PlanNodeOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "index": t.integer().optional(),
            "displayName": t.string().optional(),
            "shortRepresentation": t.proxy(
                renames["ShortRepresentationOut"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkOut"])).optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlanNodeOut"])
    types["PartitionedDmlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PartitionedDmlIn"]
    )
    types["PartitionedDmlOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartitionedDmlOut"])
    types["ListDatabaseRolesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "databaseRoles": t.array(t.proxy(renames["DatabaseRoleIn"])).optional(),
        }
    ).named(renames["ListDatabaseRolesResponseIn"])
    types["ListDatabaseRolesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "databaseRoles": t.array(t.proxy(renames["DatabaseRoleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatabaseRolesResponseOut"])
    types["CreateInstanceRequestIn"] = t.struct(
        {"instance": t.proxy(renames["InstanceIn"]), "instanceId": t.string()}
    ).named(renames["CreateInstanceRequestIn"])
    types["CreateInstanceRequestOut"] = t.struct(
        {
            "instance": t.proxy(renames["InstanceOut"]),
            "instanceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceRequestOut"])
    types["WriteIn"] = t.struct(
        {
            "table": t.string(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["WriteIn"])
    types["WriteOut"] = t.struct(
        {
            "table": t.string(),
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteOut"])
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
    types["ReadWriteIn"] = t.struct({"readLockMode": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "readLockMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
    types["FieldIn"] = t.struct(
        {"type": t.proxy(renames["TypeIn"]).optional(), "name": t.string().optional()}
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "type": t.proxy(renames["TypeOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["CreateBackupMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "database": t.string().optional(),
        }
    ).named(renames["CreateBackupMetadataIn"])
    types["CreateBackupMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBackupMetadataOut"])
    types["MutationIn"] = t.struct(
        {
            "update": t.proxy(renames["WriteIn"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
            "insert": t.proxy(renames["WriteIn"]).optional(),
            "replace": t.proxy(renames["WriteIn"]).optional(),
        }
    ).named(renames["MutationIn"])
    types["MutationOut"] = t.struct(
        {
            "update": t.proxy(renames["WriteOut"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "insert": t.proxy(renames["WriteOut"]).optional(),
            "replace": t.proxy(renames["WriteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationOut"])
    types["DatabaseRoleIn"] = t.struct({"name": t.string()}).named(
        renames["DatabaseRoleIn"]
    )
    types["DatabaseRoleOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DatabaseRoleOut"])
    types["ListBackupOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListBackupOperationsResponseIn"])
    types["ListBackupOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupOperationsResponseOut"])
    types["DatabaseIn"] = t.struct(
        {"name": t.string(), "enableDropProtection": t.boolean().optional()}
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "name": t.string(),
            "state": t.string().optional(),
            "restoreInfo": t.proxy(renames["RestoreInfoOut"]).optional(),
            "createTime": t.string().optional(),
            "defaultLeader": t.string().optional(),
            "earliestVersionTime": t.string().optional(),
            "databaseDialect": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "enableDropProtection": t.boolean().optional(),
            "versionRetentionPeriod": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "encryptionInfo": t.array(t.proxy(renames["EncryptionInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
    types["RestoreDatabaseEncryptionConfigIn"] = t.struct(
        {"encryptionType": t.string(), "kmsKeyName": t.string().optional()}
    ).named(renames["RestoreDatabaseEncryptionConfigIn"])
    types["RestoreDatabaseEncryptionConfigOut"] = t.struct(
        {
            "encryptionType": t.string(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseEncryptionConfigOut"])
    types["ExecuteBatchDmlRequestIn"] = t.struct(
        {
            "statements": t.array(t.proxy(renames["StatementIn"])),
            "seqno": t.string(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]),
        }
    ).named(renames["ExecuteBatchDmlRequestIn"])
    types["ExecuteBatchDmlRequestOut"] = t.struct(
        {
            "statements": t.array(t.proxy(renames["StatementOut"])),
            "seqno": t.string(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteBatchDmlRequestOut"])
    types["ListDatabaseOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDatabaseOperationsResponseIn"])
    types["ListDatabaseOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatabaseOperationsResponseOut"])
    types["PrefixNodeIn"] = t.struct(
        {
            "dataSourceNode": t.boolean().optional(),
            "endIndex": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "word": t.string().optional(),
            "depth": t.integer().optional(),
        }
    ).named(renames["PrefixNodeIn"])
    types["PrefixNodeOut"] = t.struct(
        {
            "dataSourceNode": t.boolean().optional(),
            "endIndex": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "word": t.string().optional(),
            "depth": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrefixNodeOut"])
    types["QueryPlanIn"] = t.struct(
        {"planNodes": t.array(t.proxy(renames["PlanNodeIn"])).optional()}
    ).named(renames["QueryPlanIn"])
    types["QueryPlanOut"] = t.struct(
        {
            "planNodes": t.array(t.proxy(renames["PlanNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryPlanOut"])
    types["MetricIn"] = t.struct(
        {
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "category": t.proxy(renames["LocalizedStringIn"]).optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "aggregation": t.string().optional(),
            "displayLabel": t.proxy(renames["LocalizedStringIn"]).optional(),
            "visible": t.boolean().optional(),
            "derived": t.proxy(renames["DerivedMetricIn"]).optional(),
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "hotValue": t.number().optional(),
            "matrix": t.proxy(renames["MetricMatrixIn"]).optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "category": t.proxy(renames["LocalizedStringOut"]).optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "aggregation": t.string().optional(),
            "displayLabel": t.proxy(renames["LocalizedStringOut"]).optional(),
            "visible": t.boolean().optional(),
            "derived": t.proxy(renames["DerivedMetricOut"]).optional(),
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "hotValue": t.number().optional(),
            "matrix": t.proxy(renames["MetricMatrixOut"]).optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["CommitStatsIn"] = t.struct({"mutationCount": t.string().optional()}).named(
        renames["CommitStatsIn"]
    )
    types["CommitStatsOut"] = t.struct(
        {
            "mutationCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitStatsOut"])
    types["ExecuteBatchDmlResponseIn"] = t.struct(
        {
            "resultSets": t.array(t.proxy(renames["ResultSetIn"])).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ExecuteBatchDmlResponseIn"])
    types["ExecuteBatchDmlResponseOut"] = t.struct(
        {
            "resultSets": t.array(t.proxy(renames["ResultSetOut"])).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteBatchDmlResponseOut"])
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["CommitRequestIn"] = t.struct(
        {
            "returnCommitStats": t.boolean().optional(),
            "mutations": t.array(t.proxy(renames["MutationIn"])).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "transactionId": t.string().optional(),
            "singleUseTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "returnCommitStats": t.boolean().optional(),
            "mutations": t.array(t.proxy(renames["MutationOut"])).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "transactionId": t.string().optional(),
            "singleUseTransaction": t.proxy(
                renames["TransactionOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])
    types["CreateDatabaseMetadataIn"] = t.struct(
        {"database": t.string().optional()}
    ).named(renames["CreateDatabaseMetadataIn"])
    types["CreateDatabaseMetadataOut"] = t.struct(
        {
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseMetadataOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["StatementIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StatementIn"])
    types["StatementOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatementOut"])
    types["ListInstanceConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instanceConfigs": t.array(t.proxy(renames["InstanceConfigIn"])).optional(),
        }
    ).named(renames["ListInstanceConfigsResponseIn"])
    types["ListInstanceConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instanceConfigs": t.array(
                t.proxy(renames["InstanceConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstanceConfigsResponseOut"])
    types["KeyRangeInfosIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "infos": t.array(t.proxy(renames["KeyRangeInfoIn"])).optional(),
        }
    ).named(renames["KeyRangeInfosIn"])
    types["KeyRangeInfosOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "infos": t.array(t.proxy(renames["KeyRangeInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeInfosOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CreateSessionRequestIn"] = t.struct(
        {"session": t.proxy(renames["SessionIn"])}
    ).named(renames["CreateSessionRequestIn"])
    types["CreateSessionRequestOut"] = t.struct(
        {
            "session": t.proxy(renames["SessionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSessionRequestOut"])
    types["ReadOnlyIn"] = t.struct(
        {
            "strong": t.boolean().optional(),
            "exactStaleness": t.string().optional(),
            "readTimestamp": t.string().optional(),
            "minReadTimestamp": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "returnReadTimestamp": t.boolean().optional(),
        }
    ).named(renames["ReadOnlyIn"])
    types["ReadOnlyOut"] = t.struct(
        {
            "strong": t.boolean().optional(),
            "exactStaleness": t.string().optional(),
            "readTimestamp": t.string().optional(),
            "minReadTimestamp": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "returnReadTimestamp": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["CopyBackupRequestIn"] = t.struct(
        {
            "expireTime": t.string(),
            "sourceBackup": t.string(),
            "backupId": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigIn"]
            ).optional(),
        }
    ).named(renames["CopyBackupRequestIn"])
    types["CopyBackupRequestOut"] = t.struct(
        {
            "expireTime": t.string(),
            "sourceBackup": t.string(),
            "backupId": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupRequestOut"])
    types["CommitResponseIn"] = t.struct(
        {
            "commitStats": t.proxy(renames["CommitStatsIn"]).optional(),
            "commitTimestamp": t.string().optional(),
        }
    ).named(renames["CommitResponseIn"])
    types["CommitResponseOut"] = t.struct(
        {
            "commitStats": t.proxy(renames["CommitStatsOut"]).optional(),
            "commitTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["QueryOptionsIn"] = t.struct(
        {
            "optimizerStatisticsPackage": t.string().optional(),
            "optimizerVersion": t.string().optional(),
        }
    ).named(renames["QueryOptionsIn"])
    types["QueryOptionsOut"] = t.struct(
        {
            "optimizerStatisticsPackage": t.string().optional(),
            "optimizerVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOptionsOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RestoreDatabaseMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
            "sourceType": t.string().optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["RestoreDatabaseMetadataIn"])
    types["RestoreDatabaseMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "sourceType": t.string().optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseMetadataOut"])
    types["OptimizeRestoredDatabaseMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["OptimizeRestoredDatabaseMetadataIn"])
    types["OptimizeRestoredDatabaseMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptimizeRestoredDatabaseMetadataOut"])
    types["ScanIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ScanIn"])
    types["ScanOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "scanData": t.proxy(renames["ScanDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanOut"])
    types["OperationProgressIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
    types["RollbackRequestIn"] = t.struct({"transactionId": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transactionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
    types["BatchCreateSessionsRequestIn"] = t.struct(
        {
            "sessionTemplate": t.proxy(renames["SessionIn"]).optional(),
            "sessionCount": t.integer(),
        }
    ).named(renames["BatchCreateSessionsRequestIn"])
    types["BatchCreateSessionsRequestOut"] = t.struct(
        {
            "sessionTemplate": t.proxy(renames["SessionOut"]).optional(),
            "sessionCount": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateSessionsRequestOut"])
    types["UpdateInstanceConfigMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["InstanceOperationProgressIn"]).optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["UpdateInstanceConfigMetadataIn"])
    types["UpdateInstanceConfigMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["InstanceOperationProgressOut"]).optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceConfigMetadataOut"])
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
    types["IndexedHotKeyIn"] = t.struct(
        {"sparseHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedHotKeyIn"])
    types["IndexedHotKeyOut"] = t.struct(
        {
            "sparseHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedHotKeyOut"])
    types["FreeInstanceMetadataIn"] = t.struct(
        {"expireBehavior": t.string().optional()}
    ).named(renames["FreeInstanceMetadataIn"])
    types["FreeInstanceMetadataOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "upgradeTime": t.string().optional(),
            "expireBehavior": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeInstanceMetadataOut"])
    types["TypeIn"] = t.struct(
        {
            "structType": t.proxy(renames["StructTypeIn"]).optional(),
            "typeAnnotation": t.string().optional(),
            "arrayElementType": t.proxy(renames["TypeIn"]).optional(),
            "code": t.string(),
            "protoTypeFqn": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "structType": t.proxy(renames["StructTypeOut"]).optional(),
            "typeAnnotation": t.string().optional(),
            "arrayElementType": t.proxy(renames["TypeOut"]).optional(),
            "code": t.string(),
            "protoTypeFqn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["MetricMatrixRowIn"] = t.struct(
        {"cols": t.array(t.number()).optional()}
    ).named(renames["MetricMatrixRowIn"])
    types["MetricMatrixRowOut"] = t.struct(
        {
            "cols": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixRowOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["KeyRangeIn"] = t.struct(
        {
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["KeyRangeIn"])
    types["KeyRangeOut"] = t.struct(
        {
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeOut"])
    types["TransactionOptionsIn"] = t.struct(
        {
            "readWrite": t.proxy(renames["ReadWriteIn"]).optional(),
            "partitionedDml": t.proxy(renames["PartitionedDmlIn"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyIn"]).optional(),
        }
    ).named(renames["TransactionOptionsIn"])
    types["TransactionOptionsOut"] = t.struct(
        {
            "readWrite": t.proxy(renames["ReadWriteOut"]).optional(),
            "partitionedDml": t.proxy(renames["PartitionedDmlOut"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionOptionsOut"])
    types["BeginTransactionRequestIn"] = t.struct(
        {
            "options": t.proxy(renames["TransactionOptionsIn"]),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
        }
    ).named(renames["BeginTransactionRequestIn"])
    types["BeginTransactionRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["TransactionOptionsOut"]),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionRequestOut"])
    types["UpdateDatabaseRequestIn"] = t.struct(
        {"updateMask": t.string(), "database": t.proxy(renames["DatabaseIn"])}
    ).named(renames["UpdateDatabaseRequestIn"])
    types["UpdateDatabaseRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "database": t.proxy(renames["DatabaseOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseRequestOut"])
    types["CreateInstanceMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceIn"]).optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["CreateInstanceMetadataIn"])
    types["CreateInstanceMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceMetadataOut"])
    types["UpdateDatabaseDdlMetadataIn"] = t.struct(
        {
            "commitTimestamps": t.array(t.string()).optional(),
            "database": t.string().optional(),
            "statements": t.array(t.string()).optional(),
            "progress": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataIn"])
    types["UpdateDatabaseDdlMetadataOut"] = t.struct(
        {
            "commitTimestamps": t.array(t.string()).optional(),
            "database": t.string().optional(),
            "statements": t.array(t.string()).optional(),
            "throttled": t.boolean().optional(),
            "progress": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataOut"])
    types["ListDatabasesResponseIn"] = t.struct(
        {
            "databases": t.array(t.proxy(renames["DatabaseIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDatabasesResponseIn"])
    types["ListDatabasesResponseOut"] = t.struct(
        {
            "databases": t.array(t.proxy(renames["DatabaseOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatabasesResponseOut"])
    types["LocalizedStringIn"] = t.struct(
        {
            "token": t.string().optional(),
            "args": t.struct({"_": t.string().optional()}).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["LocalizedStringIn"])
    types["LocalizedStringOut"] = t.struct(
        {
            "token": t.string().optional(),
            "args": t.struct({"_": t.string().optional()}).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringOut"])
    types["StructTypeIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["FieldIn"])).optional()}
    ).named(renames["StructTypeIn"])
    types["StructTypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructTypeOut"])
    types["TransactionSelectorIn"] = t.struct(
        {
            "id": t.string().optional(),
            "begin": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "singleUse": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["TransactionSelectorIn"])
    types["TransactionSelectorOut"] = t.struct(
        {
            "id": t.string().optional(),
            "begin": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "singleUse": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionSelectorOut"])
    types["UpdateDatabaseMetadataIn"] = t.struct(
        {
            "request": t.proxy(renames["UpdateDatabaseRequestIn"]).optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["UpdateDatabaseMetadataIn"])
    types["UpdateDatabaseMetadataOut"] = t.struct(
        {
            "request": t.proxy(renames["UpdateDatabaseRequestOut"]).optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseMetadataOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["PartialResultSetIn"] = t.struct(
        {
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "chunkedValue": t.boolean().optional(),
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
            "resumeToken": t.string().optional(),
        }
    ).named(renames["PartialResultSetIn"])
    types["PartialResultSetOut"] = t.struct(
        {
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "chunkedValue": t.boolean().optional(),
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "resumeToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialResultSetOut"])
    types["BackupIn"] = t.struct(
        {
            "expireTime": t.string(),
            "database": t.string(),
            "versionTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "state": t.string().optional(),
            "expireTime": t.string(),
            "databaseDialect": t.string().optional(),
            "referencingBackups": t.array(t.string()).optional(),
            "sizeBytes": t.string().optional(),
            "database": t.string(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "versionTime": t.string().optional(),
            "maxExpireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "referencingDatabases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["VisualizationDataIn"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "dataSourceEndToken": t.string().optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "keySeparator": t.string().optional(),
            "keyUnit": t.string().optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeIn"])).optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageIn"])
            ).optional(),
            "hasPii": t.boolean().optional(),
        }
    ).named(renames["VisualizationDataIn"])
    types["VisualizationDataOut"] = t.struct(
        {
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "dataSourceEndToken": t.string().optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "keySeparator": t.string().optional(),
            "keyUnit": t.string().optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeOut"])).optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageOut"])
            ).optional(),
            "hasPii": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VisualizationDataOut"])
    types["TransactionIn"] = t.struct(
        {"id": t.string().optional(), "readTimestamp": t.string().optional()}
    ).named(renames["TransactionIn"])
    types["TransactionOut"] = t.struct(
        {
            "id": t.string().optional(),
            "readTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionOut"])
    types["ExecuteSqlRequestIn"] = t.struct(
        {
            "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
            "resumeToken": t.string().optional(),
            "queryMode": t.string().optional(),
            "partitionToken": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "seqno": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
        }
    ).named(renames["ExecuteSqlRequestIn"])
    types["ExecuteSqlRequestOut"] = t.struct(
        {
            "queryOptions": t.proxy(renames["QueryOptionsOut"]).optional(),
            "resumeToken": t.string().optional(),
            "queryMode": t.string().optional(),
            "partitionToken": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "seqno": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlRequestOut"])
    types["ListSessionsResponseIn"] = t.struct(
        {
            "sessions": t.array(t.proxy(renames["SessionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSessionsResponseIn"])
    types["ListSessionsResponseOut"] = t.struct(
        {
            "sessions": t.array(t.proxy(renames["SessionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSessionsResponseOut"])
    types["CopyBackupEncryptionConfigIn"] = t.struct(
        {"encryptionType": t.string(), "kmsKeyName": t.string().optional()}
    ).named(renames["CopyBackupEncryptionConfigIn"])
    types["CopyBackupEncryptionConfigOut"] = t.struct(
        {
            "encryptionType": t.string(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupEncryptionConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ContextValueIn"] = t.struct(
        {
            "value": t.number().optional(),
            "unit": t.string().optional(),
            "severity": t.string().optional(),
            "label": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["ContextValueIn"])
    types["ContextValueOut"] = t.struct(
        {
            "value": t.number().optional(),
            "unit": t.string().optional(),
            "severity": t.string().optional(),
            "label": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextValueOut"])
    types["ListScansResponseIn"] = t.struct(
        {
            "scans": t.array(t.proxy(renames["ScanIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListScansResponseIn"])
    types["ListScansResponseOut"] = t.struct(
        {
            "scans": t.array(t.proxy(renames["ScanOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScansResponseOut"])
    types["PartitionReadRequestIn"] = t.struct(
        {
            "index": t.string().optional(),
            "keySet": t.proxy(renames["KeySetIn"]),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
            "table": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["PartitionReadRequestIn"])
    types["PartitionReadRequestOut"] = t.struct(
        {
            "index": t.string().optional(),
            "keySet": t.proxy(renames["KeySetOut"]),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "table": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionReadRequestOut"])
    types["ResultSetIn"] = t.struct(
        {
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
        }
    ).named(renames["ResultSetIn"])
    types["ResultSetOut"] = t.struct(
        {
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetOut"])
    types["InstanceOperationProgressIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["InstanceOperationProgressIn"])
    types["InstanceOperationProgressOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOperationProgressOut"])
    types["DerivedMetricIn"] = t.struct(
        {
            "denominator": t.proxy(renames["LocalizedStringIn"]).optional(),
            "numerator": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["DerivedMetricIn"])
    types["DerivedMetricOut"] = t.struct(
        {
            "denominator": t.proxy(renames["LocalizedStringOut"]).optional(),
            "numerator": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DerivedMetricOut"])
    types["DeleteIn"] = t.struct(
        {"keySet": t.proxy(renames["KeySetIn"]), "table": t.string()}
    ).named(renames["DeleteIn"])
    types["DeleteOut"] = t.struct(
        {
            "keySet": t.proxy(renames["KeySetOut"]),
            "table": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteOut"])
    types["CreateDatabaseRequestIn"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
            "extraStatements": t.array(t.string()).optional(),
            "protoDescriptors": t.string().optional(),
            "createStatement": t.string(),
            "databaseDialect": t.string().optional(),
        }
    ).named(renames["CreateDatabaseRequestIn"])
    types["CreateDatabaseRequestOut"] = t.struct(
        {
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "extraStatements": t.array(t.string()).optional(),
            "protoDescriptors": t.string().optional(),
            "createStatement": t.string(),
            "databaseDialect": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseRequestOut"])
    types["BackupInfoIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "backup": t.string().optional(),
            "versionTime": t.string().optional(),
        }
    ).named(renames["BackupInfoIn"])
    types["BackupInfoOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "backup": t.string().optional(),
            "versionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupInfoOut"])
    types["GetDatabaseDdlResponseIn"] = t.struct(
        {
            "statements": t.array(t.string()).optional(),
            "protoDescriptors": t.string().optional(),
        }
    ).named(renames["GetDatabaseDdlResponseIn"])
    types["GetDatabaseDdlResponseOut"] = t.struct(
        {
            "statements": t.array(t.string()).optional(),
            "protoDescriptors": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDatabaseDdlResponseOut"])
    types["ScanDataIn"] = t.struct(
        {
            "data": t.proxy(renames["VisualizationDataIn"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["ScanDataIn"])
    types["ScanDataOut"] = t.struct(
        {
            "data": t.proxy(renames["VisualizationDataOut"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanDataOut"])
    types["ShortRepresentationIn"] = t.struct(
        {
            "subqueries": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ShortRepresentationIn"])
    types["ShortRepresentationOut"] = t.struct(
        {
            "subqueries": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShortRepresentationOut"])
    types["KeySetIn"] = t.struct(
        {
            "keys": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "all": t.boolean().optional(),
            "ranges": t.array(t.proxy(renames["KeyRangeIn"])).optional(),
        }
    ).named(renames["KeySetIn"])
    types["KeySetOut"] = t.struct(
        {
            "keys": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "all": t.boolean().optional(),
            "ranges": t.array(t.proxy(renames["KeyRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeySetOut"])
    types["KeyRangeInfoIn"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "endKeyIndex": t.integer().optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
            "value": t.number().optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "startKeyIndex": t.integer().optional(),
            "keysCount": t.string().optional(),
            "contextValues": t.array(t.proxy(renames["ContextValueIn"])).optional(),
        }
    ).named(renames["KeyRangeInfoIn"])
    types["KeyRangeInfoOut"] = t.struct(
        {
            "timeOffset": t.string().optional(),
            "endKeyIndex": t.integer().optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "value": t.number().optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "startKeyIndex": t.integer().optional(),
            "keysCount": t.string().optional(),
            "contextValues": t.array(t.proxy(renames["ContextValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeInfoOut"])
    types["PartitionOptionsIn"] = t.struct(
        {
            "partitionSizeBytes": t.string().optional(),
            "maxPartitions": t.string().optional(),
        }
    ).named(renames["PartitionOptionsIn"])
    types["PartitionOptionsOut"] = t.struct(
        {
            "partitionSizeBytes": t.string().optional(),
            "maxPartitions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionOptionsOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["ListInstanceConfigOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListInstanceConfigOperationsResponseIn"])
    types["ListInstanceConfigOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstanceConfigOperationsResponseOut"])
    types["PartitionResponseIn"] = t.struct(
        {
            "partitions": t.array(t.proxy(renames["PartitionIn"])).optional(),
            "transaction": t.proxy(renames["TransactionIn"]).optional(),
        }
    ).named(renames["PartitionResponseIn"])
    types["PartitionResponseOut"] = t.struct(
        {
            "partitions": t.array(t.proxy(renames["PartitionOut"])).optional(),
            "transaction": t.proxy(renames["TransactionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionResponseOut"])
    types["UpdateInstanceRequestIn"] = t.struct(
        {"fieldMask": t.string(), "instance": t.proxy(renames["InstanceIn"])}
    ).named(renames["UpdateInstanceRequestIn"])
    types["UpdateInstanceRequestOut"] = t.struct(
        {
            "fieldMask": t.string(),
            "instance": t.proxy(renames["InstanceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceRequestOut"])
    types["InstanceIn"] = t.struct(
        {
            "config": t.string(),
            "instanceType": t.string().optional(),
            "displayName": t.string(),
            "endpointUris": t.array(t.string()).optional(),
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataIn"]
            ).optional(),
            "processingUnits": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nodeCount": t.integer().optional(),
            "name": t.string(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "config": t.string(),
            "state": t.string().optional(),
            "instanceType": t.string().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "endpointUris": t.array(t.string()).optional(),
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataOut"]
            ).optional(),
            "processingUnits": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "nodeCount": t.integer().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["RestoreDatabaseRequestIn"] = t.struct(
        {
            "databaseId": t.string(),
            "backup": t.string().optional(),
            "encryptionConfig": t.proxy(
                renames["RestoreDatabaseEncryptionConfigIn"]
            ).optional(),
        }
    ).named(renames["RestoreDatabaseRequestIn"])
    types["RestoreDatabaseRequestOut"] = t.struct(
        {
            "databaseId": t.string(),
            "backup": t.string().optional(),
            "encryptionConfig": t.proxy(
                renames["RestoreDatabaseEncryptionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseRequestOut"])
    types["SessionIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "creatorRole": t.string().optional(),
        }
    ).named(renames["SessionIn"])
    types["SessionOut"] = t.struct(
        {
            "approximateLastUseTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "creatorRole": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOut"])
    types["ReadRequestIn"] = t.struct(
        {
            "resumeToken": t.string().optional(),
            "partitionToken": t.string().optional(),
            "keySet": t.proxy(renames["KeySetIn"]),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "columns": t.array(t.string()),
            "table": t.string(),
            "limit": t.string().optional(),
            "index": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
        }
    ).named(renames["ReadRequestIn"])
    types["ReadRequestOut"] = t.struct(
        {
            "resumeToken": t.string().optional(),
            "partitionToken": t.string().optional(),
            "keySet": t.proxy(renames["KeySetOut"]),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "columns": t.array(t.string()),
            "table": t.string(),
            "limit": t.string().optional(),
            "index": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadRequestOut"])
    types["CreateInstanceConfigMetadataIn"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
            "progress": t.proxy(renames["InstanceOperationProgressIn"]).optional(),
        }
    ).named(renames["CreateInstanceConfigMetadataIn"])
    types["CreateInstanceConfigMetadataOut"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "progress": t.proxy(renames["InstanceOperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceConfigMetadataOut"])
    types["RequestOptionsIn"] = t.struct(
        {
            "requestTag": t.string().optional(),
            "priority": t.string().optional(),
            "transactionTag": t.string().optional(),
        }
    ).named(renames["RequestOptionsIn"])
    types["RequestOptionsOut"] = t.struct(
        {
            "requestTag": t.string().optional(),
            "priority": t.string().optional(),
            "transactionTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOptionsOut"])
    types["DiagnosticMessageIn"] = t.struct(
        {
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "shortMessage": t.proxy(renames["LocalizedStringIn"]).optional(),
            "severity": t.string().optional(),
            "metricSpecific": t.boolean().optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["DiagnosticMessageIn"])
    types["DiagnosticMessageOut"] = t.struct(
        {
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "shortMessage": t.proxy(renames["LocalizedStringOut"]).optional(),
            "severity": t.string().optional(),
            "metricSpecific": t.boolean().optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnosticMessageOut"])
    types["CopyBackupMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "cancelTime": t.string().optional(),
            "sourceBackup": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["CopyBackupMetadataIn"])
    types["CopyBackupMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "cancelTime": t.string().optional(),
            "sourceBackup": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupMetadataOut"])
    types["ResultSetMetadataIn"] = t.struct(
        {
            "rowType": t.proxy(renames["StructTypeIn"]).optional(),
            "undeclaredParameters": t.proxy(renames["StructTypeIn"]).optional(),
            "transaction": t.proxy(renames["TransactionIn"]).optional(),
        }
    ).named(renames["ResultSetMetadataIn"])
    types["ResultSetMetadataOut"] = t.struct(
        {
            "rowType": t.proxy(renames["StructTypeOut"]).optional(),
            "undeclaredParameters": t.proxy(renames["StructTypeOut"]).optional(),
            "transaction": t.proxy(renames["TransactionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetMetadataOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["CreateInstanceConfigRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]),
            "instanceConfigId": t.string(),
        }
    ).named(renames["CreateInstanceConfigRequestIn"])
    types["CreateInstanceConfigRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]),
            "instanceConfigId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceConfigRequestOut"])
    types["IndexedKeyRangeInfosIn"] = t.struct(
        {"keyRangeInfos": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedKeyRangeInfosIn"])
    types["IndexedKeyRangeInfosOut"] = t.struct(
        {
            "keyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedKeyRangeInfosOut"])
    types["MetricMatrixIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["MetricMatrixRowIn"])).optional()}
    ).named(renames["MetricMatrixIn"])
    types["MetricMatrixOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["MetricMatrixRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixOut"])

    functions = {}
    functions["projectsInstanceConfigsCreate"] = spanner.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsList"] = spanner.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsGet"] = spanner.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsPatch"] = spanner.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsDelete"] = spanner.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsGet"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsCancel"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsDelete"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsList"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGet"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDelete"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesCreate"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesPatch"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTestIamPermissions"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGetIamPolicy"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesList"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesSetIamPolicy"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsDelete"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsList"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsGet"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsCancel"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabaseOperationsList"] = spanner.get(
        "v1/{parent}/databaseOperations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatabaseOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesCreate"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesRestore"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetIamPolicy"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesTestIamPermissions"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetDdl"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGet"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSetIamPolicy"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesPatch"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesUpdateDdl"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesList"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesDropDatabase"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetScans"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "endTime": t.string().optional(),
                "name": t.string(),
                "startTime": t.string().optional(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsPartitionRead"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRollback"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteSql"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsDelete"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBatchCreate"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsPartitionQuery"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBeginTransaction"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsList"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsGet"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCreate"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteStreamingSql"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsStreamingRead"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRead"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCommit"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteBatchDml"] = spanner.post(
        "v1/{session}:executeBatchDml",
        t.struct(
            {
                "session": t.string(),
                "statements": t.array(t.proxy(renames["StatementIn"])),
                "seqno": t.string(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteBatchDmlResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesOperationsList"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesOperationsGet"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesOperationsDelete"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesOperationsCancel"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsInstancesDatabasesDatabaseRolesTestIamPermissions"
    ] = spanner.get(
        "v1/{parent}/databaseRoles",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatabaseRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesDatabaseRolesList"] = spanner.get(
        "v1/{parent}/databaseRoles",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatabaseRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsDelete"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsCreate"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsPatch"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsTestIamPermissions"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsGet"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsList"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsGetIamPolicy"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsCopy"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsSetIamPolicy"] = spanner.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsList"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsDelete"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsCancel"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsGet"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsCancel"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsGet"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsDelete"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsList"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupOperationsList"] = spanner.get(
        "v1/{parent}/backupOperations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigOperationsList"] = spanner.get(
        "v1/{parent}/instanceConfigOperations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstanceConfigOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scansList"] = spanner.get(
        "v1/{parent}",
        t.struct(
            {
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="spanner", renames=renames, types=Box(types), functions=Box(functions)
    )
