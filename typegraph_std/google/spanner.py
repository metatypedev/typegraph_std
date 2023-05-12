from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_spanner() -> Import:
    spanner = HTTPRuntime("https://spanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_spanner_1_ErrorResponse",
        "KeyRangeIn": "_spanner_2_KeyRangeIn",
        "KeyRangeOut": "_spanner_3_KeyRangeOut",
        "DeleteIn": "_spanner_4_DeleteIn",
        "DeleteOut": "_spanner_5_DeleteOut",
        "BackupIn": "_spanner_6_BackupIn",
        "BackupOut": "_spanner_7_BackupOut",
        "BeginTransactionRequestIn": "_spanner_8_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_spanner_9_BeginTransactionRequestOut",
        "KeyRangeInfoIn": "_spanner_10_KeyRangeInfoIn",
        "KeyRangeInfoOut": "_spanner_11_KeyRangeInfoOut",
        "RestoreDatabaseRequestIn": "_spanner_12_RestoreDatabaseRequestIn",
        "RestoreDatabaseRequestOut": "_spanner_13_RestoreDatabaseRequestOut",
        "OptimizeRestoredDatabaseMetadataIn": "_spanner_14_OptimizeRestoredDatabaseMetadataIn",
        "OptimizeRestoredDatabaseMetadataOut": "_spanner_15_OptimizeRestoredDatabaseMetadataOut",
        "ListBackupOperationsResponseIn": "_spanner_16_ListBackupOperationsResponseIn",
        "ListBackupOperationsResponseOut": "_spanner_17_ListBackupOperationsResponseOut",
        "UpdateInstanceRequestIn": "_spanner_18_UpdateInstanceRequestIn",
        "UpdateInstanceRequestOut": "_spanner_19_UpdateInstanceRequestOut",
        "ListSessionsResponseIn": "_spanner_20_ListSessionsResponseIn",
        "ListSessionsResponseOut": "_spanner_21_ListSessionsResponseOut",
        "ReadOnlyIn": "_spanner_22_ReadOnlyIn",
        "ReadOnlyOut": "_spanner_23_ReadOnlyOut",
        "OperationIn": "_spanner_24_OperationIn",
        "OperationOut": "_spanner_25_OperationOut",
        "ResultSetMetadataIn": "_spanner_26_ResultSetMetadataIn",
        "ResultSetMetadataOut": "_spanner_27_ResultSetMetadataOut",
        "TestIamPermissionsRequestIn": "_spanner_28_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_spanner_29_TestIamPermissionsRequestOut",
        "RequestOptionsIn": "_spanner_30_RequestOptionsIn",
        "RequestOptionsOut": "_spanner_31_RequestOptionsOut",
        "VisualizationDataIn": "_spanner_32_VisualizationDataIn",
        "VisualizationDataOut": "_spanner_33_VisualizationDataOut",
        "RestoreInfoIn": "_spanner_34_RestoreInfoIn",
        "RestoreInfoOut": "_spanner_35_RestoreInfoOut",
        "CreateDatabaseRequestIn": "_spanner_36_CreateDatabaseRequestIn",
        "CreateDatabaseRequestOut": "_spanner_37_CreateDatabaseRequestOut",
        "IndexedHotKeyIn": "_spanner_38_IndexedHotKeyIn",
        "IndexedHotKeyOut": "_spanner_39_IndexedHotKeyOut",
        "RestoreDatabaseMetadataIn": "_spanner_40_RestoreDatabaseMetadataIn",
        "RestoreDatabaseMetadataOut": "_spanner_41_RestoreDatabaseMetadataOut",
        "MetricIn": "_spanner_42_MetricIn",
        "MetricOut": "_spanner_43_MetricOut",
        "MutationIn": "_spanner_44_MutationIn",
        "MutationOut": "_spanner_45_MutationOut",
        "OperationProgressIn": "_spanner_46_OperationProgressIn",
        "OperationProgressOut": "_spanner_47_OperationProgressOut",
        "LocalizedStringIn": "_spanner_48_LocalizedStringIn",
        "LocalizedStringOut": "_spanner_49_LocalizedStringOut",
        "QueryPlanIn": "_spanner_50_QueryPlanIn",
        "QueryPlanOut": "_spanner_51_QueryPlanOut",
        "ScanDataIn": "_spanner_52_ScanDataIn",
        "ScanDataOut": "_spanner_53_ScanDataOut",
        "KeySetIn": "_spanner_54_KeySetIn",
        "KeySetOut": "_spanner_55_KeySetOut",
        "ReplicaInfoIn": "_spanner_56_ReplicaInfoIn",
        "ReplicaInfoOut": "_spanner_57_ReplicaInfoOut",
        "DiagnosticMessageIn": "_spanner_58_DiagnosticMessageIn",
        "DiagnosticMessageOut": "_spanner_59_DiagnosticMessageOut",
        "PartitionQueryRequestIn": "_spanner_60_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_spanner_61_PartitionQueryRequestOut",
        "BindingIn": "_spanner_62_BindingIn",
        "BindingOut": "_spanner_63_BindingOut",
        "PlanNodeIn": "_spanner_64_PlanNodeIn",
        "PlanNodeOut": "_spanner_65_PlanNodeOut",
        "CommitRequestIn": "_spanner_66_CommitRequestIn",
        "CommitRequestOut": "_spanner_67_CommitRequestOut",
        "UpdateDatabaseDdlRequestIn": "_spanner_68_UpdateDatabaseDdlRequestIn",
        "UpdateDatabaseDdlRequestOut": "_spanner_69_UpdateDatabaseDdlRequestOut",
        "ResultSetIn": "_spanner_70_ResultSetIn",
        "ResultSetOut": "_spanner_71_ResultSetOut",
        "ExecuteBatchDmlResponseIn": "_spanner_72_ExecuteBatchDmlResponseIn",
        "ExecuteBatchDmlResponseOut": "_spanner_73_ExecuteBatchDmlResponseOut",
        "ShortRepresentationIn": "_spanner_74_ShortRepresentationIn",
        "ShortRepresentationOut": "_spanner_75_ShortRepresentationOut",
        "KeyRangeInfosIn": "_spanner_76_KeyRangeInfosIn",
        "KeyRangeInfosOut": "_spanner_77_KeyRangeInfosOut",
        "PartitionedDmlIn": "_spanner_78_PartitionedDmlIn",
        "PartitionedDmlOut": "_spanner_79_PartitionedDmlOut",
        "RollbackRequestIn": "_spanner_80_RollbackRequestIn",
        "RollbackRequestOut": "_spanner_81_RollbackRequestOut",
        "StatementIn": "_spanner_82_StatementIn",
        "StatementOut": "_spanner_83_StatementOut",
        "GetPolicyOptionsIn": "_spanner_84_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_spanner_85_GetPolicyOptionsOut",
        "CreateDatabaseMetadataIn": "_spanner_86_CreateDatabaseMetadataIn",
        "CreateDatabaseMetadataOut": "_spanner_87_CreateDatabaseMetadataOut",
        "ExprIn": "_spanner_88_ExprIn",
        "ExprOut": "_spanner_89_ExprOut",
        "ContextValueIn": "_spanner_90_ContextValueIn",
        "ContextValueOut": "_spanner_91_ContextValueOut",
        "UpdateDatabaseMetadataIn": "_spanner_92_UpdateDatabaseMetadataIn",
        "UpdateDatabaseMetadataOut": "_spanner_93_UpdateDatabaseMetadataOut",
        "ExecuteBatchDmlRequestIn": "_spanner_94_ExecuteBatchDmlRequestIn",
        "ExecuteBatchDmlRequestOut": "_spanner_95_ExecuteBatchDmlRequestOut",
        "SessionIn": "_spanner_96_SessionIn",
        "SessionOut": "_spanner_97_SessionOut",
        "CopyBackupRequestIn": "_spanner_98_CopyBackupRequestIn",
        "CopyBackupRequestOut": "_spanner_99_CopyBackupRequestOut",
        "StatusIn": "_spanner_100_StatusIn",
        "StatusOut": "_spanner_101_StatusOut",
        "ListInstancesResponseIn": "_spanner_102_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_spanner_103_ListInstancesResponseOut",
        "ListInstanceConfigsResponseIn": "_spanner_104_ListInstanceConfigsResponseIn",
        "ListInstanceConfigsResponseOut": "_spanner_105_ListInstanceConfigsResponseOut",
        "GetDatabaseDdlResponseIn": "_spanner_106_GetDatabaseDdlResponseIn",
        "GetDatabaseDdlResponseOut": "_spanner_107_GetDatabaseDdlResponseOut",
        "MetricMatrixRowIn": "_spanner_108_MetricMatrixRowIn",
        "MetricMatrixRowOut": "_spanner_109_MetricMatrixRowOut",
        "ListBackupsResponseIn": "_spanner_110_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_spanner_111_ListBackupsResponseOut",
        "InstanceOperationProgressIn": "_spanner_112_InstanceOperationProgressIn",
        "InstanceOperationProgressOut": "_spanner_113_InstanceOperationProgressOut",
        "PartitionReadRequestIn": "_spanner_114_PartitionReadRequestIn",
        "PartitionReadRequestOut": "_spanner_115_PartitionReadRequestOut",
        "EncryptionConfigIn": "_spanner_116_EncryptionConfigIn",
        "EncryptionConfigOut": "_spanner_117_EncryptionConfigOut",
        "InstanceIn": "_spanner_118_InstanceIn",
        "InstanceOut": "_spanner_119_InstanceOut",
        "TypeIn": "_spanner_120_TypeIn",
        "TypeOut": "_spanner_121_TypeOut",
        "ScanIn": "_spanner_122_ScanIn",
        "ScanOut": "_spanner_123_ScanOut",
        "DerivedMetricIn": "_spanner_124_DerivedMetricIn",
        "DerivedMetricOut": "_spanner_125_DerivedMetricOut",
        "EmptyIn": "_spanner_126_EmptyIn",
        "EmptyOut": "_spanner_127_EmptyOut",
        "UpdateDatabaseRequestIn": "_spanner_128_UpdateDatabaseRequestIn",
        "UpdateDatabaseRequestOut": "_spanner_129_UpdateDatabaseRequestOut",
        "SetIamPolicyRequestIn": "_spanner_130_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_spanner_131_SetIamPolicyRequestOut",
        "CreateInstanceMetadataIn": "_spanner_132_CreateInstanceMetadataIn",
        "CreateInstanceMetadataOut": "_spanner_133_CreateInstanceMetadataOut",
        "CreateSessionRequestIn": "_spanner_134_CreateSessionRequestIn",
        "CreateSessionRequestOut": "_spanner_135_CreateSessionRequestOut",
        "UpdateInstanceMetadataIn": "_spanner_136_UpdateInstanceMetadataIn",
        "UpdateInstanceMetadataOut": "_spanner_137_UpdateInstanceMetadataOut",
        "CreateInstanceConfigRequestIn": "_spanner_138_CreateInstanceConfigRequestIn",
        "CreateInstanceConfigRequestOut": "_spanner_139_CreateInstanceConfigRequestOut",
        "CopyBackupEncryptionConfigIn": "_spanner_140_CopyBackupEncryptionConfigIn",
        "CopyBackupEncryptionConfigOut": "_spanner_141_CopyBackupEncryptionConfigOut",
        "DatabaseIn": "_spanner_142_DatabaseIn",
        "DatabaseOut": "_spanner_143_DatabaseOut",
        "CommitStatsIn": "_spanner_144_CommitStatsIn",
        "CommitStatsOut": "_spanner_145_CommitStatsOut",
        "DatabaseRoleIn": "_spanner_146_DatabaseRoleIn",
        "DatabaseRoleOut": "_spanner_147_DatabaseRoleOut",
        "BatchCreateSessionsResponseIn": "_spanner_148_BatchCreateSessionsResponseIn",
        "BatchCreateSessionsResponseOut": "_spanner_149_BatchCreateSessionsResponseOut",
        "ListInstanceConfigOperationsResponseIn": "_spanner_150_ListInstanceConfigOperationsResponseIn",
        "ListInstanceConfigOperationsResponseOut": "_spanner_151_ListInstanceConfigOperationsResponseOut",
        "StructTypeIn": "_spanner_152_StructTypeIn",
        "StructTypeOut": "_spanner_153_StructTypeOut",
        "ListDatabaseRolesResponseIn": "_spanner_154_ListDatabaseRolesResponseIn",
        "ListDatabaseRolesResponseOut": "_spanner_155_ListDatabaseRolesResponseOut",
        "IndexedKeyRangeInfosIn": "_spanner_156_IndexedKeyRangeInfosIn",
        "IndexedKeyRangeInfosOut": "_spanner_157_IndexedKeyRangeInfosOut",
        "CopyBackupMetadataIn": "_spanner_158_CopyBackupMetadataIn",
        "CopyBackupMetadataOut": "_spanner_159_CopyBackupMetadataOut",
        "CreateBackupMetadataIn": "_spanner_160_CreateBackupMetadataIn",
        "CreateBackupMetadataOut": "_spanner_161_CreateBackupMetadataOut",
        "FieldIn": "_spanner_162_FieldIn",
        "FieldOut": "_spanner_163_FieldOut",
        "PrefixNodeIn": "_spanner_164_PrefixNodeIn",
        "PrefixNodeOut": "_spanner_165_PrefixNodeOut",
        "CreateInstanceRequestIn": "_spanner_166_CreateInstanceRequestIn",
        "CreateInstanceRequestOut": "_spanner_167_CreateInstanceRequestOut",
        "ListOperationsResponseIn": "_spanner_168_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_spanner_169_ListOperationsResponseOut",
        "WriteIn": "_spanner_170_WriteIn",
        "WriteOut": "_spanner_171_WriteOut",
        "GetIamPolicyRequestIn": "_spanner_172_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_spanner_173_GetIamPolicyRequestOut",
        "ListDatabaseOperationsResponseIn": "_spanner_174_ListDatabaseOperationsResponseIn",
        "ListDatabaseOperationsResponseOut": "_spanner_175_ListDatabaseOperationsResponseOut",
        "TransactionIn": "_spanner_176_TransactionIn",
        "TransactionOut": "_spanner_177_TransactionOut",
        "EncryptionInfoIn": "_spanner_178_EncryptionInfoIn",
        "EncryptionInfoOut": "_spanner_179_EncryptionInfoOut",
        "PartialResultSetIn": "_spanner_180_PartialResultSetIn",
        "PartialResultSetOut": "_spanner_181_PartialResultSetOut",
        "ListDatabasesResponseIn": "_spanner_182_ListDatabasesResponseIn",
        "ListDatabasesResponseOut": "_spanner_183_ListDatabasesResponseOut",
        "ReadRequestIn": "_spanner_184_ReadRequestIn",
        "ReadRequestOut": "_spanner_185_ReadRequestOut",
        "InstanceConfigIn": "_spanner_186_InstanceConfigIn",
        "InstanceConfigOut": "_spanner_187_InstanceConfigOut",
        "QueryOptionsIn": "_spanner_188_QueryOptionsIn",
        "QueryOptionsOut": "_spanner_189_QueryOptionsOut",
        "PartitionIn": "_spanner_190_PartitionIn",
        "PartitionOut": "_spanner_191_PartitionOut",
        "ListScansResponseIn": "_spanner_192_ListScansResponseIn",
        "ListScansResponseOut": "_spanner_193_ListScansResponseOut",
        "RestoreDatabaseEncryptionConfigIn": "_spanner_194_RestoreDatabaseEncryptionConfigIn",
        "RestoreDatabaseEncryptionConfigOut": "_spanner_195_RestoreDatabaseEncryptionConfigOut",
        "TransactionOptionsIn": "_spanner_196_TransactionOptionsIn",
        "TransactionOptionsOut": "_spanner_197_TransactionOptionsOut",
        "PartitionResponseIn": "_spanner_198_PartitionResponseIn",
        "PartitionResponseOut": "_spanner_199_PartitionResponseOut",
        "CommitResponseIn": "_spanner_200_CommitResponseIn",
        "CommitResponseOut": "_spanner_201_CommitResponseOut",
        "PartitionOptionsIn": "_spanner_202_PartitionOptionsIn",
        "PartitionOptionsOut": "_spanner_203_PartitionOptionsOut",
        "ResultSetStatsIn": "_spanner_204_ResultSetStatsIn",
        "ResultSetStatsOut": "_spanner_205_ResultSetStatsOut",
        "UpdateInstanceConfigMetadataIn": "_spanner_206_UpdateInstanceConfigMetadataIn",
        "UpdateInstanceConfigMetadataOut": "_spanner_207_UpdateInstanceConfigMetadataOut",
        "BatchCreateSessionsRequestIn": "_spanner_208_BatchCreateSessionsRequestIn",
        "BatchCreateSessionsRequestOut": "_spanner_209_BatchCreateSessionsRequestOut",
        "PolicyIn": "_spanner_210_PolicyIn",
        "PolicyOut": "_spanner_211_PolicyOut",
        "CreateInstanceConfigMetadataIn": "_spanner_212_CreateInstanceConfigMetadataIn",
        "CreateInstanceConfigMetadataOut": "_spanner_213_CreateInstanceConfigMetadataOut",
        "UpdateInstanceConfigRequestIn": "_spanner_214_UpdateInstanceConfigRequestIn",
        "UpdateInstanceConfigRequestOut": "_spanner_215_UpdateInstanceConfigRequestOut",
        "BackupInfoIn": "_spanner_216_BackupInfoIn",
        "BackupInfoOut": "_spanner_217_BackupInfoOut",
        "TransactionSelectorIn": "_spanner_218_TransactionSelectorIn",
        "TransactionSelectorOut": "_spanner_219_TransactionSelectorOut",
        "MetricMatrixIn": "_spanner_220_MetricMatrixIn",
        "MetricMatrixOut": "_spanner_221_MetricMatrixOut",
        "UpdateDatabaseDdlMetadataIn": "_spanner_222_UpdateDatabaseDdlMetadataIn",
        "UpdateDatabaseDdlMetadataOut": "_spanner_223_UpdateDatabaseDdlMetadataOut",
        "ReadWriteIn": "_spanner_224_ReadWriteIn",
        "ReadWriteOut": "_spanner_225_ReadWriteOut",
        "FreeInstanceMetadataIn": "_spanner_226_FreeInstanceMetadataIn",
        "FreeInstanceMetadataOut": "_spanner_227_FreeInstanceMetadataOut",
        "ExecuteSqlRequestIn": "_spanner_228_ExecuteSqlRequestIn",
        "ExecuteSqlRequestOut": "_spanner_229_ExecuteSqlRequestOut",
        "TestIamPermissionsResponseIn": "_spanner_230_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_spanner_231_TestIamPermissionsResponseOut",
        "ChildLinkIn": "_spanner_232_ChildLinkIn",
        "ChildLinkOut": "_spanner_233_ChildLinkOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["KeyRangeIn"] = t.struct(
        {
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["KeyRangeIn"])
    types["KeyRangeOut"] = t.struct(
        {
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeOut"])
    types["DeleteIn"] = t.struct(
        {"table": t.string(), "keySet": t.proxy(renames["KeySetIn"])}
    ).named(renames["DeleteIn"])
    types["DeleteOut"] = t.struct(
        {
            "table": t.string(),
            "keySet": t.proxy(renames["KeySetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteOut"])
    types["BackupIn"] = t.struct(
        {
            "versionTime": t.string().optional(),
            "name": t.string().optional(),
            "database": t.string(),
            "expireTime": t.string(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "sizeBytes": t.string().optional(),
            "versionTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "maxExpireTime": t.string().optional(),
            "databaseDialect": t.string().optional(),
            "database": t.string(),
            "expireTime": t.string(),
            "referencingBackups": t.array(t.string()).optional(),
            "referencingDatabases": t.array(t.string()).optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    types["KeyRangeInfoIn"] = t.struct(
        {
            "value": t.number().optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
            "timeOffset": t.string().optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "contextValues": t.array(t.proxy(renames["ContextValueIn"])).optional(),
            "startKeyIndex": t.integer().optional(),
            "endKeyIndex": t.integer().optional(),
            "keysCount": t.string().optional(),
        }
    ).named(renames["KeyRangeInfoIn"])
    types["KeyRangeInfoOut"] = t.struct(
        {
            "value": t.number().optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "timeOffset": t.string().optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "contextValues": t.array(t.proxy(renames["ContextValueOut"])).optional(),
            "startKeyIndex": t.integer().optional(),
            "endKeyIndex": t.integer().optional(),
            "keysCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeInfoOut"])
    types["RestoreDatabaseRequestIn"] = t.struct(
        {
            "backup": t.string().optional(),
            "databaseId": t.string(),
            "encryptionConfig": t.proxy(
                renames["RestoreDatabaseEncryptionConfigIn"]
            ).optional(),
        }
    ).named(renames["RestoreDatabaseRequestIn"])
    types["RestoreDatabaseRequestOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "databaseId": t.string(),
            "encryptionConfig": t.proxy(
                renames["RestoreDatabaseEncryptionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseRequestOut"])
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
    types["ReadOnlyIn"] = t.struct(
        {
            "returnReadTimestamp": t.boolean().optional(),
            "maxStaleness": t.string().optional(),
            "strong": t.boolean().optional(),
            "exactStaleness": t.string().optional(),
            "minReadTimestamp": t.string().optional(),
            "readTimestamp": t.string().optional(),
        }
    ).named(renames["ReadOnlyIn"])
    types["ReadOnlyOut"] = t.struct(
        {
            "returnReadTimestamp": t.boolean().optional(),
            "maxStaleness": t.string().optional(),
            "strong": t.boolean().optional(),
            "exactStaleness": t.string().optional(),
            "minReadTimestamp": t.string().optional(),
            "readTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ResultSetMetadataIn"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionIn"]).optional(),
            "undeclaredParameters": t.proxy(renames["StructTypeIn"]).optional(),
            "rowType": t.proxy(renames["StructTypeIn"]).optional(),
        }
    ).named(renames["ResultSetMetadataIn"])
    types["ResultSetMetadataOut"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionOut"]).optional(),
            "undeclaredParameters": t.proxy(renames["StructTypeOut"]).optional(),
            "rowType": t.proxy(renames["StructTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetMetadataOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["RequestOptionsIn"] = t.struct(
        {
            "priority": t.string().optional(),
            "transactionTag": t.string().optional(),
            "requestTag": t.string().optional(),
        }
    ).named(renames["RequestOptionsIn"])
    types["RequestOptionsOut"] = t.struct(
        {
            "priority": t.string().optional(),
            "transactionTag": t.string().optional(),
            "requestTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOptionsOut"])
    types["VisualizationDataIn"] = t.struct(
        {
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageIn"])
            ).optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeIn"])).optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "keySeparator": t.string().optional(),
            "dataSourceEndToken": t.string().optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "keyUnit": t.string().optional(),
            "hasPii": t.boolean().optional(),
        }
    ).named(renames["VisualizationDataIn"])
    types["VisualizationDataOut"] = t.struct(
        {
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageOut"])
            ).optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeOut"])).optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "keySeparator": t.string().optional(),
            "dataSourceEndToken": t.string().optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "keyUnit": t.string().optional(),
            "hasPii": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VisualizationDataOut"])
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
    types["CreateDatabaseRequestIn"] = t.struct(
        {
            "createStatement": t.string(),
            "databaseDialect": t.string().optional(),
            "protoDescriptors": t.string().optional(),
            "extraStatements": t.array(t.string()).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
        }
    ).named(renames["CreateDatabaseRequestIn"])
    types["CreateDatabaseRequestOut"] = t.struct(
        {
            "createStatement": t.string(),
            "databaseDialect": t.string().optional(),
            "protoDescriptors": t.string().optional(),
            "extraStatements": t.array(t.string()).optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseRequestOut"])
    types["IndexedHotKeyIn"] = t.struct(
        {"sparseHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedHotKeyIn"])
    types["IndexedHotKeyOut"] = t.struct(
        {
            "sparseHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedHotKeyOut"])
    types["RestoreDatabaseMetadataIn"] = t.struct(
        {
            "backupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "cancelTime": t.string().optional(),
            "name": t.string().optional(),
            "sourceType": t.string().optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
        }
    ).named(renames["RestoreDatabaseMetadataIn"])
    types["RestoreDatabaseMetadataOut"] = t.struct(
        {
            "backupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "cancelTime": t.string().optional(),
            "name": t.string().optional(),
            "sourceType": t.string().optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseMetadataOut"])
    types["MetricIn"] = t.struct(
        {
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "visible": t.boolean().optional(),
            "hotValue": t.number().optional(),
            "displayLabel": t.proxy(renames["LocalizedStringIn"]).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
            "derived": t.proxy(renames["DerivedMetricIn"]).optional(),
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "aggregation": t.string().optional(),
            "matrix": t.proxy(renames["MetricMatrixIn"]).optional(),
            "category": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "visible": t.boolean().optional(),
            "hotValue": t.number().optional(),
            "displayLabel": t.proxy(renames["LocalizedStringOut"]).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "derived": t.proxy(renames["DerivedMetricOut"]).optional(),
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "aggregation": t.string().optional(),
            "matrix": t.proxy(renames["MetricMatrixOut"]).optional(),
            "category": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["MutationIn"] = t.struct(
        {
            "insert": t.proxy(renames["WriteIn"]).optional(),
            "replace": t.proxy(renames["WriteIn"]).optional(),
            "update": t.proxy(renames["WriteIn"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
        }
    ).named(renames["MutationIn"])
    types["MutationOut"] = t.struct(
        {
            "insert": t.proxy(renames["WriteOut"]).optional(),
            "replace": t.proxy(renames["WriteOut"]).optional(),
            "update": t.proxy(renames["WriteOut"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationOut"])
    types["OperationProgressIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["OperationProgressIn"])
    types["OperationProgressOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationProgressOut"])
    types["LocalizedStringIn"] = t.struct(
        {
            "token": t.string().optional(),
            "message": t.string().optional(),
            "args": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocalizedStringIn"])
    types["LocalizedStringOut"] = t.struct(
        {
            "token": t.string().optional(),
            "message": t.string().optional(),
            "args": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringOut"])
    types["QueryPlanIn"] = t.struct(
        {"planNodes": t.array(t.proxy(renames["PlanNodeIn"])).optional()}
    ).named(renames["QueryPlanIn"])
    types["QueryPlanOut"] = t.struct(
        {
            "planNodes": t.array(t.proxy(renames["PlanNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryPlanOut"])
    types["ScanDataIn"] = t.struct(
        {
            "data": t.proxy(renames["VisualizationDataIn"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ScanDataIn"])
    types["ScanDataOut"] = t.struct(
        {
            "data": t.proxy(renames["VisualizationDataOut"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanDataOut"])
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
    types["ReplicaInfoIn"] = t.struct(
        {
            "defaultLeaderLocation": t.boolean().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ReplicaInfoIn"])
    types["ReplicaInfoOut"] = t.struct(
        {
            "defaultLeaderLocation": t.boolean().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaInfoOut"])
    types["DiagnosticMessageIn"] = t.struct(
        {
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "metricSpecific": t.boolean().optional(),
            "shortMessage": t.proxy(renames["LocalizedStringIn"]).optional(),
            "severity": t.string().optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["DiagnosticMessageIn"])
    types["DiagnosticMessageOut"] = t.struct(
        {
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "metricSpecific": t.boolean().optional(),
            "shortMessage": t.proxy(renames["LocalizedStringOut"]).optional(),
            "severity": t.string().optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnosticMessageOut"])
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
            "sql": t.string(),
            "params": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "sql": t.string(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["PlanNodeIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkIn"])).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "shortRepresentation": t.proxy(renames["ShortRepresentationIn"]).optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["PlanNodeIn"])
    types["PlanNodeOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkOut"])).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "shortRepresentation": t.proxy(
                renames["ShortRepresentationOut"]
            ).optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlanNodeOut"])
    types["CommitRequestIn"] = t.struct(
        {
            "singleUseTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "transactionId": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "mutations": t.array(t.proxy(renames["MutationIn"])).optional(),
            "returnCommitStats": t.boolean().optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "singleUseTransaction": t.proxy(
                renames["TransactionOptionsOut"]
            ).optional(),
            "transactionId": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "mutations": t.array(t.proxy(renames["MutationOut"])).optional(),
            "returnCommitStats": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])
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
    types["ResultSetIn"] = t.struct(
        {
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
        }
    ).named(renames["ResultSetIn"])
    types["ResultSetOut"] = t.struct(
        {
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetOut"])
    types["ExecuteBatchDmlResponseIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "resultSets": t.array(t.proxy(renames["ResultSetIn"])).optional(),
        }
    ).named(renames["ExecuteBatchDmlResponseIn"])
    types["ExecuteBatchDmlResponseOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "resultSets": t.array(t.proxy(renames["ResultSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteBatchDmlResponseOut"])
    types["ShortRepresentationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "subqueries": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ShortRepresentationIn"])
    types["ShortRepresentationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "subqueries": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShortRepresentationOut"])
    types["KeyRangeInfosIn"] = t.struct(
        {
            "infos": t.array(t.proxy(renames["KeyRangeInfoIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["KeyRangeInfosIn"])
    types["KeyRangeInfosOut"] = t.struct(
        {
            "infos": t.array(t.proxy(renames["KeyRangeInfoOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeInfosOut"])
    types["PartitionedDmlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PartitionedDmlIn"]
    )
    types["PartitionedDmlOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartitionedDmlOut"])
    types["RollbackRequestIn"] = t.struct({"transactionId": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transactionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["CreateDatabaseMetadataIn"] = t.struct(
        {"database": t.string().optional()}
    ).named(renames["CreateDatabaseMetadataIn"])
    types["CreateDatabaseMetadataOut"] = t.struct(
        {
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseMetadataOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ContextValueIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "label": t.proxy(renames["LocalizedStringIn"]).optional(),
            "unit": t.string().optional(),
            "value": t.number().optional(),
        }
    ).named(renames["ContextValueIn"])
    types["ContextValueOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "label": t.proxy(renames["LocalizedStringOut"]).optional(),
            "unit": t.string().optional(),
            "value": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextValueOut"])
    types["UpdateDatabaseMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "cancelTime": t.string().optional(),
            "request": t.proxy(renames["UpdateDatabaseRequestIn"]).optional(),
        }
    ).named(renames["UpdateDatabaseMetadataIn"])
    types["UpdateDatabaseMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "cancelTime": t.string().optional(),
            "request": t.proxy(renames["UpdateDatabaseRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseMetadataOut"])
    types["ExecuteBatchDmlRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "statements": t.array(t.proxy(renames["StatementIn"])),
            "transaction": t.proxy(renames["TransactionSelectorIn"]),
            "seqno": t.string(),
        }
    ).named(renames["ExecuteBatchDmlRequestIn"])
    types["ExecuteBatchDmlRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "statements": t.array(t.proxy(renames["StatementOut"])),
            "transaction": t.proxy(renames["TransactionSelectorOut"]),
            "seqno": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteBatchDmlRequestOut"])
    types["SessionIn"] = t.struct(
        {
            "creatorRole": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SessionIn"])
    types["SessionOut"] = t.struct(
        {
            "approximateLastUseTime": t.string().optional(),
            "name": t.string().optional(),
            "creatorRole": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOut"])
    types["CopyBackupRequestIn"] = t.struct(
        {
            "backupId": t.string(),
            "expireTime": t.string(),
            "sourceBackup": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigIn"]
            ).optional(),
        }
    ).named(renames["CopyBackupRequestIn"])
    types["CopyBackupRequestOut"] = t.struct(
        {
            "backupId": t.string(),
            "expireTime": t.string(),
            "sourceBackup": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
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
    types["MetricMatrixRowIn"] = t.struct(
        {"cols": t.array(t.number()).optional()}
    ).named(renames["MetricMatrixRowIn"])
    types["MetricMatrixRowOut"] = t.struct(
        {
            "cols": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixRowOut"])
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
    types["PartitionReadRequestIn"] = t.struct(
        {
            "table": t.string(),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
            "keySet": t.proxy(renames["KeySetIn"]),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "index": t.string().optional(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["PartitionReadRequestIn"])
    types["PartitionReadRequestOut"] = t.struct(
        {
            "table": t.string(),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "keySet": t.proxy(renames["KeySetOut"]),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "index": t.string().optional(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionReadRequestOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["InstanceIn"] = t.struct(
        {
            "nodeCount": t.integer().optional(),
            "config": t.string(),
            "instanceType": t.string().optional(),
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataIn"]
            ).optional(),
            "name": t.string(),
            "endpointUris": t.array(t.string()).optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "processingUnits": t.integer().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "nodeCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "config": t.string(),
            "instanceType": t.string().optional(),
            "updateTime": t.string().optional(),
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataOut"]
            ).optional(),
            "name": t.string(),
            "endpointUris": t.array(t.string()).optional(),
            "displayName": t.string(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "processingUnits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["TypeIn"] = t.struct(
        {
            "typeAnnotation": t.string().optional(),
            "code": t.string(),
            "structType": t.proxy(renames["StructTypeIn"]).optional(),
            "arrayElementType": t.proxy(renames["TypeIn"]).optional(),
            "protoTypeFqn": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "typeAnnotation": t.string().optional(),
            "code": t.string(),
            "structType": t.proxy(renames["StructTypeOut"]).optional(),
            "arrayElementType": t.proxy(renames["TypeOut"]).optional(),
            "protoTypeFqn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ScanIn"] = t.struct(
        {
            "name": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ScanIn"])
    types["ScanOut"] = t.struct(
        {
            "name": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "scanData": t.proxy(renames["ScanDataOut"]).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanOut"])
    types["DerivedMetricIn"] = t.struct(
        {
            "numerator": t.proxy(renames["LocalizedStringIn"]).optional(),
            "denominator": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["DerivedMetricIn"])
    types["DerivedMetricOut"] = t.struct(
        {
            "numerator": t.proxy(renames["LocalizedStringOut"]).optional(),
            "denominator": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DerivedMetricOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["CreateInstanceMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceIn"]).optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["CreateInstanceMetadataIn"])
    types["CreateInstanceMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceMetadataOut"])
    types["CreateSessionRequestIn"] = t.struct(
        {"session": t.proxy(renames["SessionIn"])}
    ).named(renames["CreateSessionRequestIn"])
    types["CreateSessionRequestOut"] = t.struct(
        {
            "session": t.proxy(renames["SessionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSessionRequestOut"])
    types["UpdateInstanceMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceIn"]).optional(),
        }
    ).named(renames["UpdateInstanceMetadataIn"])
    types["UpdateInstanceMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceMetadataOut"])
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
    types["DatabaseIn"] = t.struct(
        {"name": t.string(), "enableDropProtection": t.boolean().optional()}
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "restoreInfo": t.proxy(renames["RestoreInfoOut"]).optional(),
            "reconciling": t.boolean().optional(),
            "encryptionInfo": t.array(t.proxy(renames["EncryptionInfoOut"])).optional(),
            "name": t.string(),
            "enableDropProtection": t.boolean().optional(),
            "defaultLeader": t.string().optional(),
            "versionRetentionPeriod": t.string().optional(),
            "state": t.string().optional(),
            "earliestVersionTime": t.string().optional(),
            "databaseDialect": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
    types["CommitStatsIn"] = t.struct({"mutationCount": t.string().optional()}).named(
        renames["CommitStatsIn"]
    )
    types["CommitStatsOut"] = t.struct(
        {
            "mutationCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitStatsOut"])
    types["DatabaseRoleIn"] = t.struct({"name": t.string()}).named(
        renames["DatabaseRoleIn"]
    )
    types["DatabaseRoleOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DatabaseRoleOut"])
    types["BatchCreateSessionsResponseIn"] = t.struct(
        {"session": t.array(t.proxy(renames["SessionIn"])).optional()}
    ).named(renames["BatchCreateSessionsResponseIn"])
    types["BatchCreateSessionsResponseOut"] = t.struct(
        {
            "session": t.array(t.proxy(renames["SessionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateSessionsResponseOut"])
    types["ListInstanceConfigOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstanceConfigOperationsResponseIn"])
    types["ListInstanceConfigOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstanceConfigOperationsResponseOut"])
    types["StructTypeIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["FieldIn"])).optional()}
    ).named(renames["StructTypeIn"])
    types["StructTypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructTypeOut"])
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
    types["IndexedKeyRangeInfosIn"] = t.struct(
        {"keyRangeInfos": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedKeyRangeInfosIn"])
    types["IndexedKeyRangeInfosOut"] = t.struct(
        {
            "keyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedKeyRangeInfosOut"])
    types["CopyBackupMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "sourceBackup": t.string().optional(),
            "name": t.string().optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["CopyBackupMetadataIn"])
    types["CopyBackupMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "sourceBackup": t.string().optional(),
            "name": t.string().optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupMetadataOut"])
    types["CreateBackupMetadataIn"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "name": t.string().optional(),
            "database": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["CreateBackupMetadataIn"])
    types["CreateBackupMetadataOut"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "name": t.string().optional(),
            "database": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBackupMetadataOut"])
    types["FieldIn"] = t.struct(
        {"name": t.string().optional(), "type": t.proxy(renames["TypeIn"]).optional()}
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.proxy(renames["TypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["PrefixNodeIn"] = t.struct(
        {
            "depth": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "word": t.string().optional(),
            "startIndex": t.integer().optional(),
            "dataSourceNode": t.boolean().optional(),
        }
    ).named(renames["PrefixNodeIn"])
    types["PrefixNodeOut"] = t.struct(
        {
            "depth": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "word": t.string().optional(),
            "startIndex": t.integer().optional(),
            "dataSourceNode": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrefixNodeOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
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
    types["TransactionIn"] = t.struct(
        {"readTimestamp": t.string().optional(), "id": t.string().optional()}
    ).named(renames["TransactionIn"])
    types["TransactionOut"] = t.struct(
        {
            "readTimestamp": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionOut"])
    types["EncryptionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EncryptionInfoIn"]
    )
    types["EncryptionInfoOut"] = t.struct(
        {
            "encryptionStatus": t.proxy(renames["StatusOut"]).optional(),
            "encryptionType": t.string().optional(),
            "kmsKeyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionInfoOut"])
    types["PartialResultSetIn"] = t.struct(
        {
            "resumeToken": t.string().optional(),
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "chunkedValue": t.boolean().optional(),
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
        }
    ).named(renames["PartialResultSetIn"])
    types["PartialResultSetOut"] = t.struct(
        {
            "resumeToken": t.string().optional(),
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "chunkedValue": t.boolean().optional(),
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialResultSetOut"])
    types["ListDatabasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "databases": t.array(t.proxy(renames["DatabaseIn"])).optional(),
        }
    ).named(renames["ListDatabasesResponseIn"])
    types["ListDatabasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "databases": t.array(t.proxy(renames["DatabaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatabasesResponseOut"])
    types["ReadRequestIn"] = t.struct(
        {
            "table": t.string(),
            "limit": t.string().optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "resumeToken": t.string().optional(),
            "columns": t.array(t.string()),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "index": t.string().optional(),
            "partitionToken": t.string().optional(),
            "keySet": t.proxy(renames["KeySetIn"]),
        }
    ).named(renames["ReadRequestIn"])
    types["ReadRequestOut"] = t.struct(
        {
            "table": t.string(),
            "limit": t.string().optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "resumeToken": t.string().optional(),
            "columns": t.array(t.string()),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "index": t.string().optional(),
            "partitionToken": t.string().optional(),
            "keySet": t.proxy(renames["KeySetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadRequestOut"])
    types["InstanceConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "baseConfig": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoIn"])).optional(),
        }
    ).named(renames["InstanceConfigIn"])
    types["InstanceConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "etag": t.string().optional(),
            "baseConfig": t.string().optional(),
            "optionalReplicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "configType": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "freeInstanceAvailability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["QueryOptionsIn"] = t.struct(
        {
            "optimizerVersion": t.string().optional(),
            "optimizerStatisticsPackage": t.string().optional(),
        }
    ).named(renames["QueryOptionsIn"])
    types["QueryOptionsOut"] = t.struct(
        {
            "optimizerVersion": t.string().optional(),
            "optimizerStatisticsPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryOptionsOut"])
    types["PartitionIn"] = t.struct({"partitionToken": t.string().optional()}).named(
        renames["PartitionIn"]
    )
    types["PartitionOut"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionOut"])
    types["ListScansResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scans": t.array(t.proxy(renames["ScanIn"])).optional(),
        }
    ).named(renames["ListScansResponseIn"])
    types["ListScansResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scans": t.array(t.proxy(renames["ScanOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScansResponseOut"])
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
    types["TransactionOptionsIn"] = t.struct(
        {
            "partitionedDml": t.proxy(renames["PartitionedDmlIn"]).optional(),
            "readWrite": t.proxy(renames["ReadWriteIn"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyIn"]).optional(),
        }
    ).named(renames["TransactionOptionsIn"])
    types["TransactionOptionsOut"] = t.struct(
        {
            "partitionedDml": t.proxy(renames["PartitionedDmlOut"]).optional(),
            "readWrite": t.proxy(renames["ReadWriteOut"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionOptionsOut"])
    types["PartitionResponseIn"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionIn"]).optional(),
            "partitions": t.array(t.proxy(renames["PartitionIn"])).optional(),
        }
    ).named(renames["PartitionResponseIn"])
    types["PartitionResponseOut"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionOut"]).optional(),
            "partitions": t.array(t.proxy(renames["PartitionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionResponseOut"])
    types["CommitResponseIn"] = t.struct(
        {
            "commitTimestamp": t.string().optional(),
            "commitStats": t.proxy(renames["CommitStatsIn"]).optional(),
        }
    ).named(renames["CommitResponseIn"])
    types["CommitResponseOut"] = t.struct(
        {
            "commitTimestamp": t.string().optional(),
            "commitStats": t.proxy(renames["CommitStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitResponseOut"])
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
    types["ResultSetStatsIn"] = t.struct(
        {
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "rowCountExact": t.string().optional(),
            "queryPlan": t.proxy(renames["QueryPlanIn"]).optional(),
            "rowCountLowerBound": t.string().optional(),
        }
    ).named(renames["ResultSetStatsIn"])
    types["ResultSetStatsOut"] = t.struct(
        {
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "rowCountExact": t.string().optional(),
            "queryPlan": t.proxy(renames["QueryPlanOut"]).optional(),
            "rowCountLowerBound": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetStatsOut"])
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
    types["BatchCreateSessionsRequestIn"] = t.struct(
        {
            "sessionCount": t.integer(),
            "sessionTemplate": t.proxy(renames["SessionIn"]).optional(),
        }
    ).named(renames["BatchCreateSessionsRequestIn"])
    types["BatchCreateSessionsRequestOut"] = t.struct(
        {
            "sessionCount": t.integer(),
            "sessionTemplate": t.proxy(renames["SessionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateSessionsRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["CreateInstanceConfigMetadataIn"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["InstanceOperationProgressIn"]).optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
        }
    ).named(renames["CreateInstanceConfigMetadataIn"])
    types["CreateInstanceConfigMetadataOut"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["InstanceOperationProgressOut"]).optional(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceConfigMetadataOut"])
    types["UpdateInstanceConfigRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "updateMask": t.string(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]),
        }
    ).named(renames["UpdateInstanceConfigRequestIn"])
    types["UpdateInstanceConfigRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "updateMask": t.string(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceConfigRequestOut"])
    types["BackupInfoIn"] = t.struct(
        {
            "backup": t.string().optional(),
            "versionTime": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceDatabase": t.string().optional(),
        }
    ).named(renames["BackupInfoIn"])
    types["BackupInfoOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "versionTime": t.string().optional(),
            "createTime": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupInfoOut"])
    types["TransactionSelectorIn"] = t.struct(
        {
            "begin": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "id": t.string().optional(),
            "singleUse": t.proxy(renames["TransactionOptionsIn"]).optional(),
        }
    ).named(renames["TransactionSelectorIn"])
    types["TransactionSelectorOut"] = t.struct(
        {
            "begin": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "id": t.string().optional(),
            "singleUse": t.proxy(renames["TransactionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionSelectorOut"])
    types["MetricMatrixIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["MetricMatrixRowIn"])).optional()}
    ).named(renames["MetricMatrixIn"])
    types["MetricMatrixOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["MetricMatrixRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixOut"])
    types["UpdateDatabaseDdlMetadataIn"] = t.struct(
        {
            "database": t.string().optional(),
            "progress": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
            "statements": t.array(t.string()).optional(),
            "commitTimestamps": t.array(t.string()).optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataIn"])
    types["UpdateDatabaseDdlMetadataOut"] = t.struct(
        {
            "database": t.string().optional(),
            "throttled": t.boolean().optional(),
            "progress": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "statements": t.array(t.string()).optional(),
            "commitTimestamps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataOut"])
    types["ReadWriteIn"] = t.struct({"readLockMode": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "readLockMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
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
    types["ExecuteSqlRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "seqno": t.string().optional(),
            "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
            "queryMode": t.string().optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "resumeToken": t.string().optional(),
            "partitionToken": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
        }
    ).named(renames["ExecuteSqlRequestIn"])
    types["ExecuteSqlRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "seqno": t.string().optional(),
            "queryOptions": t.proxy(renames["QueryOptionsOut"]).optional(),
            "queryMode": t.string().optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "resumeToken": t.string().optional(),
            "partitionToken": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ChildLinkIn"] = t.struct(
        {
            "childIndex": t.integer().optional(),
            "variable": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ChildLinkIn"])
    types["ChildLinkOut"] = t.struct(
        {
            "childIndex": t.integer().optional(),
            "variable": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChildLinkOut"])

    functions = {}
    functions["projectsInstancesList"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesSetIamPolicy"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDelete"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesPatch"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGet"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGetIamPolicy"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTestIamPermissions"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesCreate"] = spanner.post(
        "v1/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "instance": t.proxy(renames["InstanceIn"]),
                "instanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsList"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsGet"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsCancel"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesInstancePartitionsOperationsDelete"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesPatch"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesCreate"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesList"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetIamPolicy"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGet"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSetIamPolicy"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesDropDatabase"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetDdl"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetScans"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesRestore"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesTestIamPermissions"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesUpdateDdl"] = spanner.patch(
        "v1/{database}/ddl",
        t.struct(
            {
                "database": t.string(),
                "statements": t.array(t.string()),
                "operationId": t.string().optional(),
                "protoDescriptors": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteBatchDml"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsGet"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsPartitionQuery"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRollback"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRead"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBeginTransaction"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteStreamingSql"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsList"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteSql"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsPartitionRead"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsDelete"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCommit"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCreate"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBatchCreate"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsStreamingRead"] = spanner.post(
        "v1/{session}:streamingRead",
        t.struct(
            {
                "session": t.string(),
                "table": t.string(),
                "limit": t.string().optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "resumeToken": t.string().optional(),
                "columns": t.array(t.string()),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "index": t.string().optional(),
                "partitionToken": t.string().optional(),
                "keySet": t.proxy(renames["KeySetIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PartialResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesDatabaseRolesList"] = spanner.post(
        "v1/{resource}:testIamPermissions",
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
        "projectsInstancesDatabasesDatabaseRolesTestIamPermissions"
    ] = spanner.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsInstancesDatabasesOperationsGet"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesOperationsCancel"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesOperationsList"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesOperationsDelete"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsDelete"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsSetIamPolicy"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsCreate"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsPatch"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsCopy"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsTestIamPermissions"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsGetIamPolicy"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsGet"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsList"] = spanner.get(
        "v1/{parent}/backups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsDelete"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsCancel"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsGet"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsList"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupOperationsResponseOut"]),
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
    functions["projectsInstancesOperationsCancel"] = spanner.get(
        "v1/{name}",
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
    functions["projectsInstancesOperationsDelete"] = spanner.get(
        "v1/{name}",
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
    functions["projectsInstancesOperationsGet"] = spanner.get(
        "v1/{name}",
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
    functions["projectsInstancesOperationsList"] = spanner.get(
        "v1/{name}",
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
    functions["projectsInstanceConfigsOperationsDelete"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsGet"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigOperationsList"] = spanner.get(
        "v1/{parent}/instanceConfigOperations",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
