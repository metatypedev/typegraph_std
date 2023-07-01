from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_spanner():
    spanner = HTTPRuntime("https://spanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_spanner_1_ErrorResponse",
        "ScanDataIn": "_spanner_2_ScanDataIn",
        "ScanDataOut": "_spanner_3_ScanDataOut",
        "UpdateDatabaseMetadataIn": "_spanner_4_UpdateDatabaseMetadataIn",
        "UpdateDatabaseMetadataOut": "_spanner_5_UpdateDatabaseMetadataOut",
        "PartitionedDmlIn": "_spanner_6_PartitionedDmlIn",
        "PartitionedDmlOut": "_spanner_7_PartitionedDmlOut",
        "UpdateDatabaseRequestIn": "_spanner_8_UpdateDatabaseRequestIn",
        "UpdateDatabaseRequestOut": "_spanner_9_UpdateDatabaseRequestOut",
        "ExecuteBatchDmlRequestIn": "_spanner_10_ExecuteBatchDmlRequestIn",
        "ExecuteBatchDmlRequestOut": "_spanner_11_ExecuteBatchDmlRequestOut",
        "ReadWriteIn": "_spanner_12_ReadWriteIn",
        "ReadWriteOut": "_spanner_13_ReadWriteOut",
        "DeleteIn": "_spanner_14_DeleteIn",
        "DeleteOut": "_spanner_15_DeleteOut",
        "CommitRequestIn": "_spanner_16_CommitRequestIn",
        "CommitRequestOut": "_spanner_17_CommitRequestOut",
        "DiagnosticMessageIn": "_spanner_18_DiagnosticMessageIn",
        "DiagnosticMessageOut": "_spanner_19_DiagnosticMessageOut",
        "CopyBackupEncryptionConfigIn": "_spanner_20_CopyBackupEncryptionConfigIn",
        "CopyBackupEncryptionConfigOut": "_spanner_21_CopyBackupEncryptionConfigOut",
        "CreateInstanceMetadataIn": "_spanner_22_CreateInstanceMetadataIn",
        "CreateInstanceMetadataOut": "_spanner_23_CreateInstanceMetadataOut",
        "QueryPlanIn": "_spanner_24_QueryPlanIn",
        "QueryPlanOut": "_spanner_25_QueryPlanOut",
        "WriteIn": "_spanner_26_WriteIn",
        "WriteOut": "_spanner_27_WriteOut",
        "CreateDatabaseMetadataIn": "_spanner_28_CreateDatabaseMetadataIn",
        "CreateDatabaseMetadataOut": "_spanner_29_CreateDatabaseMetadataOut",
        "TransactionOptionsIn": "_spanner_30_TransactionOptionsIn",
        "TransactionOptionsOut": "_spanner_31_TransactionOptionsOut",
        "ListBackupsResponseIn": "_spanner_32_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_spanner_33_ListBackupsResponseOut",
        "ShortRepresentationIn": "_spanner_34_ShortRepresentationIn",
        "ShortRepresentationOut": "_spanner_35_ShortRepresentationOut",
        "UpdateInstanceConfigRequestIn": "_spanner_36_UpdateInstanceConfigRequestIn",
        "UpdateInstanceConfigRequestOut": "_spanner_37_UpdateInstanceConfigRequestOut",
        "CreateInstanceRequestIn": "_spanner_38_CreateInstanceRequestIn",
        "CreateInstanceRequestOut": "_spanner_39_CreateInstanceRequestOut",
        "ResultSetMetadataIn": "_spanner_40_ResultSetMetadataIn",
        "ResultSetMetadataOut": "_spanner_41_ResultSetMetadataOut",
        "ListDatabasesResponseIn": "_spanner_42_ListDatabasesResponseIn",
        "ListDatabasesResponseOut": "_spanner_43_ListDatabasesResponseOut",
        "CopyBackupMetadataIn": "_spanner_44_CopyBackupMetadataIn",
        "CopyBackupMetadataOut": "_spanner_45_CopyBackupMetadataOut",
        "StatusIn": "_spanner_46_StatusIn",
        "StatusOut": "_spanner_47_StatusOut",
        "KeySetIn": "_spanner_48_KeySetIn",
        "KeySetOut": "_spanner_49_KeySetOut",
        "TestIamPermissionsRequestIn": "_spanner_50_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_spanner_51_TestIamPermissionsRequestOut",
        "UpdateInstanceConfigMetadataIn": "_spanner_52_UpdateInstanceConfigMetadataIn",
        "UpdateInstanceConfigMetadataOut": "_spanner_53_UpdateInstanceConfigMetadataOut",
        "PartitionResponseIn": "_spanner_54_PartitionResponseIn",
        "PartitionResponseOut": "_spanner_55_PartitionResponseOut",
        "UpdateInstanceMetadataIn": "_spanner_56_UpdateInstanceMetadataIn",
        "UpdateInstanceMetadataOut": "_spanner_57_UpdateInstanceMetadataOut",
        "GetIamPolicyRequestIn": "_spanner_58_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_spanner_59_GetIamPolicyRequestOut",
        "FreeInstanceMetadataIn": "_spanner_60_FreeInstanceMetadataIn",
        "FreeInstanceMetadataOut": "_spanner_61_FreeInstanceMetadataOut",
        "MetricMatrixIn": "_spanner_62_MetricMatrixIn",
        "MetricMatrixOut": "_spanner_63_MetricMatrixOut",
        "QueryOptionsIn": "_spanner_64_QueryOptionsIn",
        "QueryOptionsOut": "_spanner_65_QueryOptionsOut",
        "DdlStatementActionInfoIn": "_spanner_66_DdlStatementActionInfoIn",
        "DdlStatementActionInfoOut": "_spanner_67_DdlStatementActionInfoOut",
        "ListInstancesResponseIn": "_spanner_68_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_spanner_69_ListInstancesResponseOut",
        "GetPolicyOptionsIn": "_spanner_70_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_spanner_71_GetPolicyOptionsOut",
        "PartitionReadRequestIn": "_spanner_72_PartitionReadRequestIn",
        "PartitionReadRequestOut": "_spanner_73_PartitionReadRequestOut",
        "EmptyIn": "_spanner_74_EmptyIn",
        "EmptyOut": "_spanner_75_EmptyOut",
        "RestoreInfoIn": "_spanner_76_RestoreInfoIn",
        "RestoreInfoOut": "_spanner_77_RestoreInfoOut",
        "RollbackRequestIn": "_spanner_78_RollbackRequestIn",
        "RollbackRequestOut": "_spanner_79_RollbackRequestOut",
        "ExecuteSqlRequestIn": "_spanner_80_ExecuteSqlRequestIn",
        "ExecuteSqlRequestOut": "_spanner_81_ExecuteSqlRequestOut",
        "PartitionIn": "_spanner_82_PartitionIn",
        "PartitionOut": "_spanner_83_PartitionOut",
        "ListDatabaseRolesResponseIn": "_spanner_84_ListDatabaseRolesResponseIn",
        "ListDatabaseRolesResponseOut": "_spanner_85_ListDatabaseRolesResponseOut",
        "ListDatabaseOperationsResponseIn": "_spanner_86_ListDatabaseOperationsResponseIn",
        "ListDatabaseOperationsResponseOut": "_spanner_87_ListDatabaseOperationsResponseOut",
        "UpdateDatabaseDdlMetadataIn": "_spanner_88_UpdateDatabaseDdlMetadataIn",
        "UpdateDatabaseDdlMetadataOut": "_spanner_89_UpdateDatabaseDdlMetadataOut",
        "ListScansResponseIn": "_spanner_90_ListScansResponseIn",
        "ListScansResponseOut": "_spanner_91_ListScansResponseOut",
        "MetricIn": "_spanner_92_MetricIn",
        "MetricOut": "_spanner_93_MetricOut",
        "KeyRangeInfoIn": "_spanner_94_KeyRangeInfoIn",
        "KeyRangeInfoOut": "_spanner_95_KeyRangeInfoOut",
        "GetDatabaseDdlResponseIn": "_spanner_96_GetDatabaseDdlResponseIn",
        "GetDatabaseDdlResponseOut": "_spanner_97_GetDatabaseDdlResponseOut",
        "IndexedKeyRangeInfosIn": "_spanner_98_IndexedKeyRangeInfosIn",
        "IndexedKeyRangeInfosOut": "_spanner_99_IndexedKeyRangeInfosOut",
        "UpdateInstanceRequestIn": "_spanner_100_UpdateInstanceRequestIn",
        "UpdateInstanceRequestOut": "_spanner_101_UpdateInstanceRequestOut",
        "InstanceIn": "_spanner_102_InstanceIn",
        "InstanceOut": "_spanner_103_InstanceOut",
        "SessionIn": "_spanner_104_SessionIn",
        "SessionOut": "_spanner_105_SessionOut",
        "TransactionIn": "_spanner_106_TransactionIn",
        "TransactionOut": "_spanner_107_TransactionOut",
        "ListInstanceConfigOperationsResponseIn": "_spanner_108_ListInstanceConfigOperationsResponseIn",
        "ListInstanceConfigOperationsResponseOut": "_spanner_109_ListInstanceConfigOperationsResponseOut",
        "PolicyIn": "_spanner_110_PolicyIn",
        "PolicyOut": "_spanner_111_PolicyOut",
        "CopyBackupRequestIn": "_spanner_112_CopyBackupRequestIn",
        "CopyBackupRequestOut": "_spanner_113_CopyBackupRequestOut",
        "PartialResultSetIn": "_spanner_114_PartialResultSetIn",
        "PartialResultSetOut": "_spanner_115_PartialResultSetOut",
        "MetricMatrixRowIn": "_spanner_116_MetricMatrixRowIn",
        "MetricMatrixRowOut": "_spanner_117_MetricMatrixRowOut",
        "EncryptionConfigIn": "_spanner_118_EncryptionConfigIn",
        "EncryptionConfigOut": "_spanner_119_EncryptionConfigOut",
        "RestoreDatabaseMetadataIn": "_spanner_120_RestoreDatabaseMetadataIn",
        "RestoreDatabaseMetadataOut": "_spanner_121_RestoreDatabaseMetadataOut",
        "ListInstanceConfigsResponseIn": "_spanner_122_ListInstanceConfigsResponseIn",
        "ListInstanceConfigsResponseOut": "_spanner_123_ListInstanceConfigsResponseOut",
        "SetIamPolicyRequestIn": "_spanner_124_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_spanner_125_SetIamPolicyRequestOut",
        "UpdateDatabaseDdlRequestIn": "_spanner_126_UpdateDatabaseDdlRequestIn",
        "UpdateDatabaseDdlRequestOut": "_spanner_127_UpdateDatabaseDdlRequestOut",
        "FieldIn": "_spanner_128_FieldIn",
        "FieldOut": "_spanner_129_FieldOut",
        "PartitionQueryRequestIn": "_spanner_130_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_spanner_131_PartitionQueryRequestOut",
        "ReplicaInfoIn": "_spanner_132_ReplicaInfoIn",
        "ReplicaInfoOut": "_spanner_133_ReplicaInfoOut",
        "IndexedHotKeyIn": "_spanner_134_IndexedHotKeyIn",
        "IndexedHotKeyOut": "_spanner_135_IndexedHotKeyOut",
        "InstanceConfigIn": "_spanner_136_InstanceConfigIn",
        "InstanceConfigOut": "_spanner_137_InstanceConfigOut",
        "BindingIn": "_spanner_138_BindingIn",
        "BindingOut": "_spanner_139_BindingOut",
        "TypeIn": "_spanner_140_TypeIn",
        "TypeOut": "_spanner_141_TypeOut",
        "LocalizedStringIn": "_spanner_142_LocalizedStringIn",
        "LocalizedStringOut": "_spanner_143_LocalizedStringOut",
        "ScanIn": "_spanner_144_ScanIn",
        "ScanOut": "_spanner_145_ScanOut",
        "BatchCreateSessionsResponseIn": "_spanner_146_BatchCreateSessionsResponseIn",
        "BatchCreateSessionsResponseOut": "_spanner_147_BatchCreateSessionsResponseOut",
        "ResultSetIn": "_spanner_148_ResultSetIn",
        "ResultSetOut": "_spanner_149_ResultSetOut",
        "BatchCreateSessionsRequestIn": "_spanner_150_BatchCreateSessionsRequestIn",
        "BatchCreateSessionsRequestOut": "_spanner_151_BatchCreateSessionsRequestOut",
        "PartitionOptionsIn": "_spanner_152_PartitionOptionsIn",
        "PartitionOptionsOut": "_spanner_153_PartitionOptionsOut",
        "CreateBackupMetadataIn": "_spanner_154_CreateBackupMetadataIn",
        "CreateBackupMetadataOut": "_spanner_155_CreateBackupMetadataOut",
        "KeyRangeIn": "_spanner_156_KeyRangeIn",
        "KeyRangeOut": "_spanner_157_KeyRangeOut",
        "ListBackupOperationsResponseIn": "_spanner_158_ListBackupOperationsResponseIn",
        "ListBackupOperationsResponseOut": "_spanner_159_ListBackupOperationsResponseOut",
        "DerivedMetricIn": "_spanner_160_DerivedMetricIn",
        "DerivedMetricOut": "_spanner_161_DerivedMetricOut",
        "ExecuteBatchDmlResponseIn": "_spanner_162_ExecuteBatchDmlResponseIn",
        "ExecuteBatchDmlResponseOut": "_spanner_163_ExecuteBatchDmlResponseOut",
        "CreateSessionRequestIn": "_spanner_164_CreateSessionRequestIn",
        "CreateSessionRequestOut": "_spanner_165_CreateSessionRequestOut",
        "ContextValueIn": "_spanner_166_ContextValueIn",
        "ContextValueOut": "_spanner_167_ContextValueOut",
        "CreateInstanceConfigMetadataIn": "_spanner_168_CreateInstanceConfigMetadataIn",
        "CreateInstanceConfigMetadataOut": "_spanner_169_CreateInstanceConfigMetadataOut",
        "KeyRangeInfosIn": "_spanner_170_KeyRangeInfosIn",
        "KeyRangeInfosOut": "_spanner_171_KeyRangeInfosOut",
        "CreateDatabaseRequestIn": "_spanner_172_CreateDatabaseRequestIn",
        "CreateDatabaseRequestOut": "_spanner_173_CreateDatabaseRequestOut",
        "ListOperationsResponseIn": "_spanner_174_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_spanner_175_ListOperationsResponseOut",
        "ExprIn": "_spanner_176_ExprIn",
        "ExprOut": "_spanner_177_ExprOut",
        "ListSessionsResponseIn": "_spanner_178_ListSessionsResponseIn",
        "ListSessionsResponseOut": "_spanner_179_ListSessionsResponseOut",
        "TransactionSelectorIn": "_spanner_180_TransactionSelectorIn",
        "TransactionSelectorOut": "_spanner_181_TransactionSelectorOut",
        "InstanceOperationProgressIn": "_spanner_182_InstanceOperationProgressIn",
        "InstanceOperationProgressOut": "_spanner_183_InstanceOperationProgressOut",
        "CommitStatsIn": "_spanner_184_CommitStatsIn",
        "CommitStatsOut": "_spanner_185_CommitStatsOut",
        "BackupInfoIn": "_spanner_186_BackupInfoIn",
        "BackupInfoOut": "_spanner_187_BackupInfoOut",
        "ReadOnlyIn": "_spanner_188_ReadOnlyIn",
        "ReadOnlyOut": "_spanner_189_ReadOnlyOut",
        "OperationIn": "_spanner_190_OperationIn",
        "OperationOut": "_spanner_191_OperationOut",
        "RequestOptionsIn": "_spanner_192_RequestOptionsIn",
        "RequestOptionsOut": "_spanner_193_RequestOptionsOut",
        "EncryptionInfoIn": "_spanner_194_EncryptionInfoIn",
        "EncryptionInfoOut": "_spanner_195_EncryptionInfoOut",
        "CommitResponseIn": "_spanner_196_CommitResponseIn",
        "CommitResponseOut": "_spanner_197_CommitResponseOut",
        "VisualizationDataIn": "_spanner_198_VisualizationDataIn",
        "VisualizationDataOut": "_spanner_199_VisualizationDataOut",
        "RestoreDatabaseEncryptionConfigIn": "_spanner_200_RestoreDatabaseEncryptionConfigIn",
        "RestoreDatabaseEncryptionConfigOut": "_spanner_201_RestoreDatabaseEncryptionConfigOut",
        "MutationIn": "_spanner_202_MutationIn",
        "MutationOut": "_spanner_203_MutationOut",
        "BackupIn": "_spanner_204_BackupIn",
        "BackupOut": "_spanner_205_BackupOut",
        "ReadRequestIn": "_spanner_206_ReadRequestIn",
        "ReadRequestOut": "_spanner_207_ReadRequestOut",
        "StatementIn": "_spanner_208_StatementIn",
        "StatementOut": "_spanner_209_StatementOut",
        "DatabaseRoleIn": "_spanner_210_DatabaseRoleIn",
        "DatabaseRoleOut": "_spanner_211_DatabaseRoleOut",
        "BeginTransactionRequestIn": "_spanner_212_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_spanner_213_BeginTransactionRequestOut",
        "RestoreDatabaseRequestIn": "_spanner_214_RestoreDatabaseRequestIn",
        "RestoreDatabaseRequestOut": "_spanner_215_RestoreDatabaseRequestOut",
        "ResultSetStatsIn": "_spanner_216_ResultSetStatsIn",
        "ResultSetStatsOut": "_spanner_217_ResultSetStatsOut",
        "PrefixNodeIn": "_spanner_218_PrefixNodeIn",
        "PrefixNodeOut": "_spanner_219_PrefixNodeOut",
        "OperationProgressIn": "_spanner_220_OperationProgressIn",
        "OperationProgressOut": "_spanner_221_OperationProgressOut",
        "CreateInstanceConfigRequestIn": "_spanner_222_CreateInstanceConfigRequestIn",
        "CreateInstanceConfigRequestOut": "_spanner_223_CreateInstanceConfigRequestOut",
        "StructTypeIn": "_spanner_224_StructTypeIn",
        "StructTypeOut": "_spanner_225_StructTypeOut",
        "OptimizeRestoredDatabaseMetadataIn": "_spanner_226_OptimizeRestoredDatabaseMetadataIn",
        "OptimizeRestoredDatabaseMetadataOut": "_spanner_227_OptimizeRestoredDatabaseMetadataOut",
        "PlanNodeIn": "_spanner_228_PlanNodeIn",
        "PlanNodeOut": "_spanner_229_PlanNodeOut",
        "ChildLinkIn": "_spanner_230_ChildLinkIn",
        "ChildLinkOut": "_spanner_231_ChildLinkOut",
        "DatabaseIn": "_spanner_232_DatabaseIn",
        "DatabaseOut": "_spanner_233_DatabaseOut",
        "TestIamPermissionsResponseIn": "_spanner_234_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_spanner_235_TestIamPermissionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ScanDataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "data": t.proxy(renames["VisualizationDataIn"]).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["ScanDataIn"])
    types["ScanDataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "data": t.proxy(renames["VisualizationDataOut"]).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanDataOut"])
    types["UpdateDatabaseMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "request": t.proxy(renames["UpdateDatabaseRequestIn"]).optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["UpdateDatabaseMetadataIn"])
    types["UpdateDatabaseMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "request": t.proxy(renames["UpdateDatabaseRequestOut"]).optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseMetadataOut"])
    types["PartitionedDmlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PartitionedDmlIn"]
    )
    types["PartitionedDmlOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartitionedDmlOut"])
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
    types["ExecuteBatchDmlRequestIn"] = t.struct(
        {
            "seqno": t.string(),
            "statements": t.array(t.proxy(renames["StatementIn"])),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]),
        }
    ).named(renames["ExecuteBatchDmlRequestIn"])
    types["ExecuteBatchDmlRequestOut"] = t.struct(
        {
            "seqno": t.string(),
            "statements": t.array(t.proxy(renames["StatementOut"])),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteBatchDmlRequestOut"])
    types["ReadWriteIn"] = t.struct({"readLockMode": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "readLockMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
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
    types["CommitRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "transactionId": t.string().optional(),
            "singleUseTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "mutations": t.array(t.proxy(renames["MutationIn"])).optional(),
            "returnCommitStats": t.boolean().optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "transactionId": t.string().optional(),
            "singleUseTransaction": t.proxy(
                renames["TransactionOptionsOut"]
            ).optional(),
            "mutations": t.array(t.proxy(renames["MutationOut"])).optional(),
            "returnCommitStats": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])
    types["DiagnosticMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
            "shortMessage": t.proxy(renames["LocalizedStringIn"]).optional(),
            "metricSpecific": t.boolean().optional(),
        }
    ).named(renames["DiagnosticMessageIn"])
    types["DiagnosticMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "shortMessage": t.proxy(renames["LocalizedStringOut"]).optional(),
            "metricSpecific": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnosticMessageOut"])
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
    types["CreateInstanceMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceIn"]).optional(),
            "endTime": t.string().optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["CreateInstanceMetadataIn"])
    types["CreateInstanceMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "endTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceMetadataOut"])
    types["QueryPlanIn"] = t.struct(
        {"planNodes": t.array(t.proxy(renames["PlanNodeIn"])).optional()}
    ).named(renames["QueryPlanIn"])
    types["QueryPlanOut"] = t.struct(
        {
            "planNodes": t.array(t.proxy(renames["PlanNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryPlanOut"])
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
    types["CreateDatabaseMetadataIn"] = t.struct(
        {"database": t.string().optional()}
    ).named(renames["CreateDatabaseMetadataIn"])
    types["CreateDatabaseMetadataOut"] = t.struct(
        {
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseMetadataOut"])
    types["TransactionOptionsIn"] = t.struct(
        {
            "partitionedDml": t.proxy(renames["PartitionedDmlIn"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyIn"]).optional(),
            "readWrite": t.proxy(renames["ReadWriteIn"]).optional(),
        }
    ).named(renames["TransactionOptionsIn"])
    types["TransactionOptionsOut"] = t.struct(
        {
            "partitionedDml": t.proxy(renames["PartitionedDmlOut"]).optional(),
            "readOnly": t.proxy(renames["ReadOnlyOut"]).optional(),
            "readWrite": t.proxy(renames["ReadWriteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionOptionsOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
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
    types["CreateInstanceRequestIn"] = t.struct(
        {"instanceId": t.string(), "instance": t.proxy(renames["InstanceIn"])}
    ).named(renames["CreateInstanceRequestIn"])
    types["CreateInstanceRequestOut"] = t.struct(
        {
            "instanceId": t.string(),
            "instance": t.proxy(renames["InstanceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceRequestOut"])
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
    types["CopyBackupMetadataIn"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "sourceBackup": t.string().optional(),
        }
    ).named(renames["CopyBackupMetadataIn"])
    types["CopyBackupMetadataOut"] = t.struct(
        {
            "cancelTime": t.string().optional(),
            "name": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "sourceBackup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupMetadataOut"])
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
    types["KeySetIn"] = t.struct(
        {
            "keys": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "ranges": t.array(t.proxy(renames["KeyRangeIn"])).optional(),
            "all": t.boolean().optional(),
        }
    ).named(renames["KeySetIn"])
    types["KeySetOut"] = t.struct(
        {
            "keys": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "ranges": t.array(t.proxy(renames["KeyRangeOut"])).optional(),
            "all": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeySetOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["UpdateInstanceMetadataIn"] = t.struct(
        {
            "instance": t.proxy(renames["InstanceIn"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["UpdateInstanceMetadataIn"])
    types["UpdateInstanceMetadataOut"] = t.struct(
        {
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceMetadataOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
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
    types["MetricMatrixIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["MetricMatrixRowIn"])).optional()}
    ).named(renames["MetricMatrixIn"])
    types["MetricMatrixOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["MetricMatrixRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixOut"])
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
    types["DdlStatementActionInfoIn"] = t.struct(
        {
            "entityType": t.string().optional(),
            "entityNames": t.array(t.string()).optional(),
            "action": t.string().optional(),
        }
    ).named(renames["DdlStatementActionInfoIn"])
    types["DdlStatementActionInfoOut"] = t.struct(
        {
            "entityType": t.string().optional(),
            "entityNames": t.array(t.string()).optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DdlStatementActionInfoOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["PartitionReadRequestIn"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
            "columns": t.array(t.string()).optional(),
            "index": t.string().optional(),
            "table": t.string(),
            "keySet": t.proxy(renames["KeySetIn"]),
        }
    ).named(renames["PartitionReadRequestIn"])
    types["PartitionReadRequestOut"] = t.struct(
        {
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "columns": t.array(t.string()).optional(),
            "index": t.string().optional(),
            "table": t.string(),
            "keySet": t.proxy(renames["KeySetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionReadRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["RollbackRequestIn"] = t.struct({"transactionId": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transactionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
    types["ExecuteSqlRequestIn"] = t.struct(
        {
            "seqno": t.string().optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "partitionToken": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "resumeToken": t.string().optional(),
            "queryMode": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ExecuteSqlRequestIn"])
    types["ExecuteSqlRequestOut"] = t.struct(
        {
            "seqno": t.string().optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "queryOptions": t.proxy(renames["QueryOptionsOut"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "partitionToken": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "resumeToken": t.string().optional(),
            "queryMode": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlRequestOut"])
    types["PartitionIn"] = t.struct({"partitionToken": t.string().optional()}).named(
        renames["PartitionIn"]
    )
    types["PartitionOut"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionOut"])
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
    types["ListDatabaseOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListDatabaseOperationsResponseIn"])
    types["ListDatabaseOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatabaseOperationsResponseOut"])
    types["UpdateDatabaseDdlMetadataIn"] = t.struct(
        {
            "statements": t.array(t.string()).optional(),
            "actions": t.array(t.proxy(renames["DdlStatementActionInfoIn"])).optional(),
            "commitTimestamps": t.array(t.string()).optional(),
            "progress": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
            "database": t.string().optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataIn"])
    types["UpdateDatabaseDdlMetadataOut"] = t.struct(
        {
            "throttled": t.boolean().optional(),
            "statements": t.array(t.string()).optional(),
            "actions": t.array(
                t.proxy(renames["DdlStatementActionInfoOut"])
            ).optional(),
            "commitTimestamps": t.array(t.string()).optional(),
            "progress": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataOut"])
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
    types["MetricIn"] = t.struct(
        {
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "matrix": t.proxy(renames["MetricMatrixIn"]).optional(),
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "hotValue": t.number().optional(),
            "derived": t.proxy(renames["DerivedMetricIn"]).optional(),
            "visible": t.boolean().optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
            "displayLabel": t.proxy(renames["LocalizedStringIn"]).optional(),
            "category": t.proxy(renames["LocalizedStringIn"]).optional(),
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "aggregation": t.string().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "matrix": t.proxy(renames["MetricMatrixOut"]).optional(),
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "hotValue": t.number().optional(),
            "derived": t.proxy(renames["DerivedMetricOut"]).optional(),
            "visible": t.boolean().optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "displayLabel": t.proxy(renames["LocalizedStringOut"]).optional(),
            "category": t.proxy(renames["LocalizedStringOut"]).optional(),
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "aggregation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["KeyRangeInfoIn"] = t.struct(
        {
            "contextValues": t.array(t.proxy(renames["ContextValueIn"])).optional(),
            "startKeyIndex": t.integer().optional(),
            "value": t.number().optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
            "keysCount": t.string().optional(),
            "timeOffset": t.string().optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
            "endKeyIndex": t.integer().optional(),
        }
    ).named(renames["KeyRangeInfoIn"])
    types["KeyRangeInfoOut"] = t.struct(
        {
            "contextValues": t.array(t.proxy(renames["ContextValueOut"])).optional(),
            "startKeyIndex": t.integer().optional(),
            "value": t.number().optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "keysCount": t.string().optional(),
            "timeOffset": t.string().optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "endKeyIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeInfoOut"])
    types["GetDatabaseDdlResponseIn"] = t.struct(
        {
            "protoDescriptors": t.string().optional(),
            "statements": t.array(t.string()).optional(),
        }
    ).named(renames["GetDatabaseDdlResponseIn"])
    types["GetDatabaseDdlResponseOut"] = t.struct(
        {
            "protoDescriptors": t.string().optional(),
            "statements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetDatabaseDdlResponseOut"])
    types["IndexedKeyRangeInfosIn"] = t.struct(
        {"keyRangeInfos": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedKeyRangeInfosIn"])
    types["IndexedKeyRangeInfosOut"] = t.struct(
        {
            "keyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedKeyRangeInfosOut"])
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
            "instanceType": t.string().optional(),
            "displayName": t.string(),
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "config": t.string(),
            "name": t.string(),
            "endpointUris": t.array(t.string()).optional(),
            "nodeCount": t.integer().optional(),
            "processingUnits": t.integer().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "instanceType": t.string().optional(),
            "displayName": t.string(),
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "config": t.string(),
            "name": t.string(),
            "endpointUris": t.array(t.string()).optional(),
            "nodeCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "processingUnits": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
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
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "creatorRole": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOut"])
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
    types["CopyBackupRequestIn"] = t.struct(
        {
            "backupId": t.string(),
            "sourceBackup": t.string(),
            "expireTime": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigIn"]
            ).optional(),
        }
    ).named(renames["CopyBackupRequestIn"])
    types["CopyBackupRequestOut"] = t.struct(
        {
            "backupId": t.string(),
            "sourceBackup": t.string(),
            "expireTime": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupRequestOut"])
    types["PartialResultSetIn"] = t.struct(
        {
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
            "chunkedValue": t.boolean().optional(),
            "resumeToken": t.string().optional(),
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["PartialResultSetIn"])
    types["PartialResultSetOut"] = t.struct(
        {
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "chunkedValue": t.boolean().optional(),
            "resumeToken": t.string().optional(),
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialResultSetOut"])
    types["MetricMatrixRowIn"] = t.struct(
        {"cols": t.array(t.number()).optional()}
    ).named(renames["MetricMatrixRowIn"])
    types["MetricMatrixRowOut"] = t.struct(
        {
            "cols": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixRowOut"])
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["RestoreDatabaseMetadataIn"] = t.struct(
        {
            "backupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
            "cancelTime": t.string().optional(),
            "sourceType": t.string().optional(),
            "name": t.string().optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
        }
    ).named(renames["RestoreDatabaseMetadataIn"])
    types["RestoreDatabaseMetadataOut"] = t.struct(
        {
            "backupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "cancelTime": t.string().optional(),
            "sourceType": t.string().optional(),
            "name": t.string().optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseMetadataOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["UpdateDatabaseDdlRequestIn"] = t.struct(
        {
            "protoDescriptors": t.string().optional(),
            "operationId": t.string().optional(),
            "statements": t.array(t.string()),
        }
    ).named(renames["UpdateDatabaseDdlRequestIn"])
    types["UpdateDatabaseDdlRequestOut"] = t.struct(
        {
            "protoDescriptors": t.string().optional(),
            "operationId": t.string().optional(),
            "statements": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseDdlRequestOut"])
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
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["ReplicaInfoIn"] = t.struct(
        {
            "location": t.string().optional(),
            "defaultLeaderLocation": t.boolean().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ReplicaInfoIn"])
    types["ReplicaInfoOut"] = t.struct(
        {
            "location": t.string().optional(),
            "defaultLeaderLocation": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaInfoOut"])
    types["IndexedHotKeyIn"] = t.struct(
        {"sparseHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedHotKeyIn"])
    types["IndexedHotKeyOut"] = t.struct(
        {
            "sparseHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedHotKeyOut"])
    types["InstanceConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoIn"])).optional(),
            "baseConfig": t.string().optional(),
        }
    ).named(renames["InstanceConfigIn"])
    types["InstanceConfigOut"] = t.struct(
        {
            "freeInstanceAvailability": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "optionalReplicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "reconciling": t.boolean().optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "configType": t.string().optional(),
            "baseConfig": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
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
    types["TypeIn"] = t.struct(
        {
            "code": t.string(),
            "typeAnnotation": t.string().optional(),
            "arrayElementType": t.proxy(renames["TypeIn"]).optional(),
            "structType": t.proxy(renames["StructTypeIn"]).optional(),
            "protoTypeFqn": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "code": t.string(),
            "typeAnnotation": t.string().optional(),
            "arrayElementType": t.proxy(renames["TypeOut"]).optional(),
            "structType": t.proxy(renames["StructTypeOut"]).optional(),
            "protoTypeFqn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["ScanIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ScanIn"])
    types["ScanOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "scanData": t.proxy(renames["ScanDataOut"]).optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanOut"])
    types["BatchCreateSessionsResponseIn"] = t.struct(
        {"session": t.array(t.proxy(renames["SessionIn"])).optional()}
    ).named(renames["BatchCreateSessionsResponseIn"])
    types["BatchCreateSessionsResponseOut"] = t.struct(
        {
            "session": t.array(t.proxy(renames["SessionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateSessionsResponseOut"])
    types["ResultSetIn"] = t.struct(
        {
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
        }
    ).named(renames["ResultSetIn"])
    types["ResultSetOut"] = t.struct(
        {
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetOut"])
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
    types["CreateBackupMetadataIn"] = t.struct(
        {
            "database": t.string().optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CreateBackupMetadataIn"])
    types["CreateBackupMetadataOut"] = t.struct(
        {
            "database": t.string().optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBackupMetadataOut"])
    types["KeyRangeIn"] = t.struct(
        {
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["KeyRangeIn"])
    types["KeyRangeOut"] = t.struct(
        {
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeOut"])
    types["ListBackupOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBackupOperationsResponseIn"])
    types["ListBackupOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupOperationsResponseOut"])
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
    types["CreateSessionRequestIn"] = t.struct(
        {"session": t.proxy(renames["SessionIn"])}
    ).named(renames["CreateSessionRequestIn"])
    types["CreateSessionRequestOut"] = t.struct(
        {
            "session": t.proxy(renames["SessionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSessionRequestOut"])
    types["ContextValueIn"] = t.struct(
        {
            "value": t.number().optional(),
            "label": t.proxy(renames["LocalizedStringIn"]).optional(),
            "severity": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["ContextValueIn"])
    types["ContextValueOut"] = t.struct(
        {
            "value": t.number().optional(),
            "label": t.proxy(renames["LocalizedStringOut"]).optional(),
            "severity": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextValueOut"])
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
    types["CreateDatabaseRequestIn"] = t.struct(
        {
            "extraStatements": t.array(t.string()).optional(),
            "protoDescriptors": t.string().optional(),
            "databaseDialect": t.string().optional(),
            "createStatement": t.string(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
        }
    ).named(renames["CreateDatabaseRequestIn"])
    types["CreateDatabaseRequestOut"] = t.struct(
        {
            "extraStatements": t.array(t.string()).optional(),
            "protoDescriptors": t.string().optional(),
            "databaseDialect": t.string().optional(),
            "createStatement": t.string(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseRequestOut"])
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
    types["InstanceOperationProgressIn"] = t.struct(
        {
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["InstanceOperationProgressIn"])
    types["InstanceOperationProgressOut"] = t.struct(
        {
            "progressPercent": t.integer().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOperationProgressOut"])
    types["CommitStatsIn"] = t.struct({"mutationCount": t.string().optional()}).named(
        renames["CommitStatsIn"]
    )
    types["CommitStatsOut"] = t.struct(
        {
            "mutationCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitStatsOut"])
    types["BackupInfoIn"] = t.struct(
        {
            "backup": t.string().optional(),
            "createTime": t.string().optional(),
            "versionTime": t.string().optional(),
            "sourceDatabase": t.string().optional(),
        }
    ).named(renames["BackupInfoIn"])
    types["BackupInfoOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "createTime": t.string().optional(),
            "versionTime": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupInfoOut"])
    types["ReadOnlyIn"] = t.struct(
        {
            "strong": t.boolean().optional(),
            "returnReadTimestamp": t.boolean().optional(),
            "readTimestamp": t.string().optional(),
            "minReadTimestamp": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "exactStaleness": t.string().optional(),
        }
    ).named(renames["ReadOnlyIn"])
    types["ReadOnlyOut"] = t.struct(
        {
            "strong": t.boolean().optional(),
            "returnReadTimestamp": t.boolean().optional(),
            "readTimestamp": t.string().optional(),
            "minReadTimestamp": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "exactStaleness": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["VisualizationDataIn"] = t.struct(
        {
            "dataSourceEndToken": t.string().optional(),
            "keyUnit": t.string().optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "keySeparator": t.string().optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeIn"])).optional(),
            "hasPii": t.boolean().optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageIn"])
            ).optional(),
        }
    ).named(renames["VisualizationDataIn"])
    types["VisualizationDataOut"] = t.struct(
        {
            "dataSourceEndToken": t.string().optional(),
            "keyUnit": t.string().optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "keySeparator": t.string().optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeOut"])).optional(),
            "hasPii": t.boolean().optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VisualizationDataOut"])
    types["RestoreDatabaseEncryptionConfigIn"] = t.struct(
        {"kmsKeyName": t.string().optional(), "encryptionType": t.string()}
    ).named(renames["RestoreDatabaseEncryptionConfigIn"])
    types["RestoreDatabaseEncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "encryptionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseEncryptionConfigOut"])
    types["MutationIn"] = t.struct(
        {
            "update": t.proxy(renames["WriteIn"]).optional(),
            "insert": t.proxy(renames["WriteIn"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteIn"]).optional(),
            "replace": t.proxy(renames["WriteIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
        }
    ).named(renames["MutationIn"])
    types["MutationOut"] = t.struct(
        {
            "update": t.proxy(renames["WriteOut"]).optional(),
            "insert": t.proxy(renames["WriteOut"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteOut"]).optional(),
            "replace": t.proxy(renames["WriteOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationOut"])
    types["BackupIn"] = t.struct(
        {
            "versionTime": t.string().optional(),
            "expireTime": t.string(),
            "name": t.string().optional(),
            "database": t.string(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "state": t.string().optional(),
            "versionTime": t.string().optional(),
            "referencingBackups": t.array(t.string()).optional(),
            "expireTime": t.string(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "referencingDatabases": t.array(t.string()).optional(),
            "maxExpireTime": t.string().optional(),
            "databaseDialect": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "database": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["ReadRequestIn"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "columns": t.array(t.string()),
            "keySet": t.proxy(renames["KeySetIn"]),
            "index": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "table": t.string(),
            "limit": t.string().optional(),
            "resumeToken": t.string().optional(),
        }
    ).named(renames["ReadRequestIn"])
    types["ReadRequestOut"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "columns": t.array(t.string()),
            "keySet": t.proxy(renames["KeySetOut"]),
            "index": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "dataBoostEnabled": t.boolean().optional(),
            "table": t.string(),
            "limit": t.string().optional(),
            "resumeToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadRequestOut"])
    types["StatementIn"] = t.struct(
        {
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "params": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StatementIn"])
    types["StatementOut"] = t.struct(
        {
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatementOut"])
    types["DatabaseRoleIn"] = t.struct({"name": t.string()}).named(
        renames["DatabaseRoleIn"]
    )
    types["DatabaseRoleOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DatabaseRoleOut"])
    types["BeginTransactionRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "options": t.proxy(renames["TransactionOptionsIn"]),
        }
    ).named(renames["BeginTransactionRequestIn"])
    types["BeginTransactionRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "options": t.proxy(renames["TransactionOptionsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BeginTransactionRequestOut"])
    types["RestoreDatabaseRequestIn"] = t.struct(
        {
            "backup": t.string().optional(),
            "encryptionConfig": t.proxy(
                renames["RestoreDatabaseEncryptionConfigIn"]
            ).optional(),
            "databaseId": t.string(),
        }
    ).named(renames["RestoreDatabaseRequestIn"])
    types["RestoreDatabaseRequestOut"] = t.struct(
        {
            "backup": t.string().optional(),
            "encryptionConfig": t.proxy(
                renames["RestoreDatabaseEncryptionConfigOut"]
            ).optional(),
            "databaseId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseRequestOut"])
    types["ResultSetStatsIn"] = t.struct(
        {
            "queryPlan": t.proxy(renames["QueryPlanIn"]).optional(),
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "rowCountLowerBound": t.string().optional(),
            "rowCountExact": t.string().optional(),
        }
    ).named(renames["ResultSetStatsIn"])
    types["ResultSetStatsOut"] = t.struct(
        {
            "queryPlan": t.proxy(renames["QueryPlanOut"]).optional(),
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "rowCountLowerBound": t.string().optional(),
            "rowCountExact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetStatsOut"])
    types["PrefixNodeIn"] = t.struct(
        {
            "word": t.string().optional(),
            "startIndex": t.integer().optional(),
            "dataSourceNode": t.boolean().optional(),
            "depth": t.integer().optional(),
            "endIndex": t.integer().optional(),
        }
    ).named(renames["PrefixNodeIn"])
    types["PrefixNodeOut"] = t.struct(
        {
            "word": t.string().optional(),
            "startIndex": t.integer().optional(),
            "dataSourceNode": t.boolean().optional(),
            "depth": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrefixNodeOut"])
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
    types["StructTypeIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["FieldIn"])).optional()}
    ).named(renames["StructTypeIn"])
    types["StructTypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructTypeOut"])
    types["OptimizeRestoredDatabaseMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OptimizeRestoredDatabaseMetadataIn"])
    types["OptimizeRestoredDatabaseMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptimizeRestoredDatabaseMetadataOut"])
    types["PlanNodeIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkIn"])).optional(),
            "index": t.integer().optional(),
            "shortRepresentation": t.proxy(renames["ShortRepresentationIn"]).optional(),
        }
    ).named(renames["PlanNodeIn"])
    types["PlanNodeOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkOut"])).optional(),
            "index": t.integer().optional(),
            "shortRepresentation": t.proxy(
                renames["ShortRepresentationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlanNodeOut"])
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
    types["DatabaseIn"] = t.struct(
        {"name": t.string(), "enableDropProtection": t.boolean().optional()}
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "earliestVersionTime": t.string().optional(),
            "versionRetentionPeriod": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "reconciling": t.boolean().optional(),
            "enableDropProtection": t.boolean().optional(),
            "encryptionInfo": t.array(t.proxy(renames["EncryptionInfoOut"])).optional(),
            "defaultLeader": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "databaseDialect": t.string().optional(),
            "restoreInfo": t.proxy(renames["RestoreInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])

    functions = {}
    functions["scansList"] = spanner.get(
        "v1/{parent}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDelete"] = spanner.post(
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
    functions["projectsInstancesSetIamPolicy"] = spanner.post(
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
    functions["projectsInstancesPatch"] = spanner.post(
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
    functions["projectsInstancesCreate"] = spanner.post(
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
    functions["projectsInstancesGetIamPolicy"] = spanner.post(
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
    functions["projectsInstancesList"] = spanner.post(
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
    functions["projectsInstancesGet"] = spanner.post(
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
    functions["projectsInstancesTestIamPermissions"] = spanner.post(
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
    functions["projectsInstancesBackupOperationsList"] = spanner.get(
        "v1/{parent}/backupOperations",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatabaseOperationsResponseOut"]),
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
    functions["projectsInstancesInstancePartitionsOperationsList"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsInstancesInstancePartitionsOperationsCancel"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsGet"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsCancel"] = spanner.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsList"] = spanner.post(
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
    functions["projectsInstancesBackupsCopy"] = spanner.post(
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
    functions["projectsInstancesBackupsGet"] = spanner.post(
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
    functions["projectsInstancesBackupsPatch"] = spanner.post(
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
    functions["projectsInstancesBackupsGetIamPolicy"] = spanner.post(
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
    functions["projectsInstancesBackupsCreate"] = spanner.post(
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
    functions["projectsInstancesBackupsSetIamPolicy"] = spanner.post(
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
    functions["projectsInstancesBackupsDelete"] = spanner.post(
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
    functions["projectsInstancesBackupsTestIamPermissions"] = spanner.post(
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
    functions["projectsInstancesBackupsOperationsList"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsGet"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsCancel"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesBackupsOperationsDelete"] = spanner.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesCreate"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetDdl"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesDropDatabase"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGet"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesRestore"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetScans"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesUpdateDdl"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesTestIamPermissions"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesGetIamPolicy"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesList"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSetIamPolicy"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesPatch"] = spanner.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "enableDropProtection": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsInstancesDatabasesOperationsDelete"] = spanner.get(
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
    functions["projectsInstancesDatabasesOperationsGet"] = spanner.get(
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
    functions["projectsInstancesDatabasesOperationsCancel"] = spanner.get(
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
    functions["projectsInstancesDatabasesOperationsList"] = spanner.get(
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
    functions["projectsInstancesDatabasesSessionsPartitionRead"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBeginTransaction"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsPartitionQuery"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteBatchDml"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsGet"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCommit"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBatchCreate"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRollback"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRead"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteStreamingSql"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsList"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCreate"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsDelete"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsStreamingRead"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteSql"] = spanner.post(
        "v1/{session}:executeSql",
        t.struct(
            {
                "session": t.string(),
                "seqno": t.string().optional(),
                "paramTypes": t.struct({"_": t.string().optional()}).optional(),
                "sql": t.string(),
                "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
                "dataBoostEnabled": t.boolean().optional(),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "partitionToken": t.string().optional(),
                "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
                "resumeToken": t.string().optional(),
                "queryMode": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResultSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsDelete"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsCreate"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsList"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsPatch"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsGet"] = spanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InstanceConfigOut"]),
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
    functions["projectsInstanceConfigOperationsList"] = spanner.get(
        "v1/{parent}/instanceConfigOperations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstanceConfigOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="spanner", renames=renames, types=Box(types), functions=Box(functions)
    )
