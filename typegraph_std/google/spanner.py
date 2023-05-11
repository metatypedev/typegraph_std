from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_spanner() -> Import:
    spanner = HTTPRuntime("https://spanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_spanner_1_ErrorResponse",
        "ScanDataIn": "_spanner_2_ScanDataIn",
        "ScanDataOut": "_spanner_3_ScanDataOut",
        "GetPolicyOptionsIn": "_spanner_4_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_spanner_5_GetPolicyOptionsOut",
        "PolicyIn": "_spanner_6_PolicyIn",
        "PolicyOut": "_spanner_7_PolicyOut",
        "UpdateDatabaseMetadataIn": "_spanner_8_UpdateDatabaseMetadataIn",
        "UpdateDatabaseMetadataOut": "_spanner_9_UpdateDatabaseMetadataOut",
        "MetricMatrixRowIn": "_spanner_10_MetricMatrixRowIn",
        "MetricMatrixRowOut": "_spanner_11_MetricMatrixRowOut",
        "CreateDatabaseMetadataIn": "_spanner_12_CreateDatabaseMetadataIn",
        "CreateDatabaseMetadataOut": "_spanner_13_CreateDatabaseMetadataOut",
        "UpdateInstanceConfigRequestIn": "_spanner_14_UpdateInstanceConfigRequestIn",
        "UpdateInstanceConfigRequestOut": "_spanner_15_UpdateInstanceConfigRequestOut",
        "ResultSetIn": "_spanner_16_ResultSetIn",
        "ResultSetOut": "_spanner_17_ResultSetOut",
        "BatchCreateSessionsRequestIn": "_spanner_18_BatchCreateSessionsRequestIn",
        "BatchCreateSessionsRequestOut": "_spanner_19_BatchCreateSessionsRequestOut",
        "UpdateInstanceRequestIn": "_spanner_20_UpdateInstanceRequestIn",
        "UpdateInstanceRequestOut": "_spanner_21_UpdateInstanceRequestOut",
        "RollbackRequestIn": "_spanner_22_RollbackRequestIn",
        "RollbackRequestOut": "_spanner_23_RollbackRequestOut",
        "TransactionSelectorIn": "_spanner_24_TransactionSelectorIn",
        "TransactionSelectorOut": "_spanner_25_TransactionSelectorOut",
        "CreateInstanceRequestIn": "_spanner_26_CreateInstanceRequestIn",
        "CreateInstanceRequestOut": "_spanner_27_CreateInstanceRequestOut",
        "VisualizationDataIn": "_spanner_28_VisualizationDataIn",
        "VisualizationDataOut": "_spanner_29_VisualizationDataOut",
        "ScanIn": "_spanner_30_ScanIn",
        "ScanOut": "_spanner_31_ScanOut",
        "CreateSessionRequestIn": "_spanner_32_CreateSessionRequestIn",
        "CreateSessionRequestOut": "_spanner_33_CreateSessionRequestOut",
        "KeyRangeInfosIn": "_spanner_34_KeyRangeInfosIn",
        "KeyRangeInfosOut": "_spanner_35_KeyRangeInfosOut",
        "ResultSetStatsIn": "_spanner_36_ResultSetStatsIn",
        "ResultSetStatsOut": "_spanner_37_ResultSetStatsOut",
        "EncryptionInfoIn": "_spanner_38_EncryptionInfoIn",
        "EncryptionInfoOut": "_spanner_39_EncryptionInfoOut",
        "CopyBackupRequestIn": "_spanner_40_CopyBackupRequestIn",
        "CopyBackupRequestOut": "_spanner_41_CopyBackupRequestOut",
        "DerivedMetricIn": "_spanner_42_DerivedMetricIn",
        "DerivedMetricOut": "_spanner_43_DerivedMetricOut",
        "DeleteIn": "_spanner_44_DeleteIn",
        "DeleteOut": "_spanner_45_DeleteOut",
        "CommitResponseIn": "_spanner_46_CommitResponseIn",
        "CommitResponseOut": "_spanner_47_CommitResponseOut",
        "ExecuteBatchDmlRequestIn": "_spanner_48_ExecuteBatchDmlRequestIn",
        "ExecuteBatchDmlRequestOut": "_spanner_49_ExecuteBatchDmlRequestOut",
        "OptimizeRestoredDatabaseMetadataIn": "_spanner_50_OptimizeRestoredDatabaseMetadataIn",
        "OptimizeRestoredDatabaseMetadataOut": "_spanner_51_OptimizeRestoredDatabaseMetadataOut",
        "IndexedKeyRangeInfosIn": "_spanner_52_IndexedKeyRangeInfosIn",
        "IndexedKeyRangeInfosOut": "_spanner_53_IndexedKeyRangeInfosOut",
        "RestoreDatabaseMetadataIn": "_spanner_54_RestoreDatabaseMetadataIn",
        "RestoreDatabaseMetadataOut": "_spanner_55_RestoreDatabaseMetadataOut",
        "PrefixNodeIn": "_spanner_56_PrefixNodeIn",
        "PrefixNodeOut": "_spanner_57_PrefixNodeOut",
        "UpdateInstanceMetadataIn": "_spanner_58_UpdateInstanceMetadataIn",
        "UpdateInstanceMetadataOut": "_spanner_59_UpdateInstanceMetadataOut",
        "FieldIn": "_spanner_60_FieldIn",
        "FieldOut": "_spanner_61_FieldOut",
        "RestoreDatabaseRequestIn": "_spanner_62_RestoreDatabaseRequestIn",
        "RestoreDatabaseRequestOut": "_spanner_63_RestoreDatabaseRequestOut",
        "FreeInstanceMetadataIn": "_spanner_64_FreeInstanceMetadataIn",
        "FreeInstanceMetadataOut": "_spanner_65_FreeInstanceMetadataOut",
        "PartitionOptionsIn": "_spanner_66_PartitionOptionsIn",
        "PartitionOptionsOut": "_spanner_67_PartitionOptionsOut",
        "ListDatabaseOperationsResponseIn": "_spanner_68_ListDatabaseOperationsResponseIn",
        "ListDatabaseOperationsResponseOut": "_spanner_69_ListDatabaseOperationsResponseOut",
        "CreateBackupMetadataIn": "_spanner_70_CreateBackupMetadataIn",
        "CreateBackupMetadataOut": "_spanner_71_CreateBackupMetadataOut",
        "UpdateInstanceConfigMetadataIn": "_spanner_72_UpdateInstanceConfigMetadataIn",
        "UpdateInstanceConfigMetadataOut": "_spanner_73_UpdateInstanceConfigMetadataOut",
        "ListDatabaseRolesResponseIn": "_spanner_74_ListDatabaseRolesResponseIn",
        "ListDatabaseRolesResponseOut": "_spanner_75_ListDatabaseRolesResponseOut",
        "InstanceConfigIn": "_spanner_76_InstanceConfigIn",
        "InstanceConfigOut": "_spanner_77_InstanceConfigOut",
        "BackupInfoIn": "_spanner_78_BackupInfoIn",
        "BackupInfoOut": "_spanner_79_BackupInfoOut",
        "CopyBackupMetadataIn": "_spanner_80_CopyBackupMetadataIn",
        "CopyBackupMetadataOut": "_spanner_81_CopyBackupMetadataOut",
        "SessionIn": "_spanner_82_SessionIn",
        "SessionOut": "_spanner_83_SessionOut",
        "PartitionQueryRequestIn": "_spanner_84_PartitionQueryRequestIn",
        "PartitionQueryRequestOut": "_spanner_85_PartitionQueryRequestOut",
        "StatusIn": "_spanner_86_StatusIn",
        "StatusOut": "_spanner_87_StatusOut",
        "OperationIn": "_spanner_88_OperationIn",
        "OperationOut": "_spanner_89_OperationOut",
        "ListInstanceConfigOperationsResponseIn": "_spanner_90_ListInstanceConfigOperationsResponseIn",
        "ListInstanceConfigOperationsResponseOut": "_spanner_91_ListInstanceConfigOperationsResponseOut",
        "StructTypeIn": "_spanner_92_StructTypeIn",
        "StructTypeOut": "_spanner_93_StructTypeOut",
        "RequestOptionsIn": "_spanner_94_RequestOptionsIn",
        "RequestOptionsOut": "_spanner_95_RequestOptionsOut",
        "BackupIn": "_spanner_96_BackupIn",
        "BackupOut": "_spanner_97_BackupOut",
        "DiagnosticMessageIn": "_spanner_98_DiagnosticMessageIn",
        "DiagnosticMessageOut": "_spanner_99_DiagnosticMessageOut",
        "IndexedHotKeyIn": "_spanner_100_IndexedHotKeyIn",
        "IndexedHotKeyOut": "_spanner_101_IndexedHotKeyOut",
        "GetIamPolicyRequestIn": "_spanner_102_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_spanner_103_GetIamPolicyRequestOut",
        "KeyRangeInfoIn": "_spanner_104_KeyRangeInfoIn",
        "KeyRangeInfoOut": "_spanner_105_KeyRangeInfoOut",
        "KeySetIn": "_spanner_106_KeySetIn",
        "KeySetOut": "_spanner_107_KeySetOut",
        "TransactionIn": "_spanner_108_TransactionIn",
        "TransactionOut": "_spanner_109_TransactionOut",
        "MetricIn": "_spanner_110_MetricIn",
        "MetricOut": "_spanner_111_MetricOut",
        "BatchCreateSessionsResponseIn": "_spanner_112_BatchCreateSessionsResponseIn",
        "BatchCreateSessionsResponseOut": "_spanner_113_BatchCreateSessionsResponseOut",
        "GetDatabaseDdlResponseIn": "_spanner_114_GetDatabaseDdlResponseIn",
        "GetDatabaseDdlResponseOut": "_spanner_115_GetDatabaseDdlResponseOut",
        "InstanceOperationProgressIn": "_spanner_116_InstanceOperationProgressIn",
        "InstanceOperationProgressOut": "_spanner_117_InstanceOperationProgressOut",
        "ChildLinkIn": "_spanner_118_ChildLinkIn",
        "ChildLinkOut": "_spanner_119_ChildLinkOut",
        "PartitionReadRequestIn": "_spanner_120_PartitionReadRequestIn",
        "PartitionReadRequestOut": "_spanner_121_PartitionReadRequestOut",
        "ListSessionsResponseIn": "_spanner_122_ListSessionsResponseIn",
        "ListSessionsResponseOut": "_spanner_123_ListSessionsResponseOut",
        "ListScansResponseIn": "_spanner_124_ListScansResponseIn",
        "ListScansResponseOut": "_spanner_125_ListScansResponseOut",
        "QueryOptionsIn": "_spanner_126_QueryOptionsIn",
        "QueryOptionsOut": "_spanner_127_QueryOptionsOut",
        "ExecuteBatchDmlResponseIn": "_spanner_128_ExecuteBatchDmlResponseIn",
        "ExecuteBatchDmlResponseOut": "_spanner_129_ExecuteBatchDmlResponseOut",
        "DatabaseRoleIn": "_spanner_130_DatabaseRoleIn",
        "DatabaseRoleOut": "_spanner_131_DatabaseRoleOut",
        "PartitionResponseIn": "_spanner_132_PartitionResponseIn",
        "PartitionResponseOut": "_spanner_133_PartitionResponseOut",
        "CommitStatsIn": "_spanner_134_CommitStatsIn",
        "CommitStatsOut": "_spanner_135_CommitStatsOut",
        "ListDatabasesResponseIn": "_spanner_136_ListDatabasesResponseIn",
        "ListDatabasesResponseOut": "_spanner_137_ListDatabasesResponseOut",
        "QueryPlanIn": "_spanner_138_QueryPlanIn",
        "QueryPlanOut": "_spanner_139_QueryPlanOut",
        "EmptyIn": "_spanner_140_EmptyIn",
        "EmptyOut": "_spanner_141_EmptyOut",
        "ReplicaInfoIn": "_spanner_142_ReplicaInfoIn",
        "ReplicaInfoOut": "_spanner_143_ReplicaInfoOut",
        "DatabaseIn": "_spanner_144_DatabaseIn",
        "DatabaseOut": "_spanner_145_DatabaseOut",
        "ListInstanceConfigsResponseIn": "_spanner_146_ListInstanceConfigsResponseIn",
        "ListInstanceConfigsResponseOut": "_spanner_147_ListInstanceConfigsResponseOut",
        "PlanNodeIn": "_spanner_148_PlanNodeIn",
        "PlanNodeOut": "_spanner_149_PlanNodeOut",
        "PartitionIn": "_spanner_150_PartitionIn",
        "PartitionOut": "_spanner_151_PartitionOut",
        "CreateInstanceConfigMetadataIn": "_spanner_152_CreateInstanceConfigMetadataIn",
        "CreateInstanceConfigMetadataOut": "_spanner_153_CreateInstanceConfigMetadataOut",
        "EncryptionConfigIn": "_spanner_154_EncryptionConfigIn",
        "EncryptionConfigOut": "_spanner_155_EncryptionConfigOut",
        "CreateInstanceMetadataIn": "_spanner_156_CreateInstanceMetadataIn",
        "CreateInstanceMetadataOut": "_spanner_157_CreateInstanceMetadataOut",
        "ResultSetMetadataIn": "_spanner_158_ResultSetMetadataIn",
        "ResultSetMetadataOut": "_spanner_159_ResultSetMetadataOut",
        "TestIamPermissionsResponseIn": "_spanner_160_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_spanner_161_TestIamPermissionsResponseOut",
        "CreateInstanceConfigRequestIn": "_spanner_162_CreateInstanceConfigRequestIn",
        "CreateInstanceConfigRequestOut": "_spanner_163_CreateInstanceConfigRequestOut",
        "TypeIn": "_spanner_164_TypeIn",
        "TypeOut": "_spanner_165_TypeOut",
        "UpdateDatabaseRequestIn": "_spanner_166_UpdateDatabaseRequestIn",
        "UpdateDatabaseRequestOut": "_spanner_167_UpdateDatabaseRequestOut",
        "ContextValueIn": "_spanner_168_ContextValueIn",
        "ContextValueOut": "_spanner_169_ContextValueOut",
        "CopyBackupEncryptionConfigIn": "_spanner_170_CopyBackupEncryptionConfigIn",
        "CopyBackupEncryptionConfigOut": "_spanner_171_CopyBackupEncryptionConfigOut",
        "BeginTransactionRequestIn": "_spanner_172_BeginTransactionRequestIn",
        "BeginTransactionRequestOut": "_spanner_173_BeginTransactionRequestOut",
        "TransactionOptionsIn": "_spanner_174_TransactionOptionsIn",
        "TransactionOptionsOut": "_spanner_175_TransactionOptionsOut",
        "BindingIn": "_spanner_176_BindingIn",
        "BindingOut": "_spanner_177_BindingOut",
        "InstanceIn": "_spanner_178_InstanceIn",
        "InstanceOut": "_spanner_179_InstanceOut",
        "RestoreDatabaseEncryptionConfigIn": "_spanner_180_RestoreDatabaseEncryptionConfigIn",
        "RestoreDatabaseEncryptionConfigOut": "_spanner_181_RestoreDatabaseEncryptionConfigOut",
        "RestoreInfoIn": "_spanner_182_RestoreInfoIn",
        "RestoreInfoOut": "_spanner_183_RestoreInfoOut",
        "ShortRepresentationIn": "_spanner_184_ShortRepresentationIn",
        "ShortRepresentationOut": "_spanner_185_ShortRepresentationOut",
        "LocalizedStringIn": "_spanner_186_LocalizedStringIn",
        "LocalizedStringOut": "_spanner_187_LocalizedStringOut",
        "MetricMatrixIn": "_spanner_188_MetricMatrixIn",
        "MetricMatrixOut": "_spanner_189_MetricMatrixOut",
        "ReadOnlyIn": "_spanner_190_ReadOnlyIn",
        "ReadOnlyOut": "_spanner_191_ReadOnlyOut",
        "TestIamPermissionsRequestIn": "_spanner_192_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_spanner_193_TestIamPermissionsRequestOut",
        "UpdateDatabaseDdlMetadataIn": "_spanner_194_UpdateDatabaseDdlMetadataIn",
        "UpdateDatabaseDdlMetadataOut": "_spanner_195_UpdateDatabaseDdlMetadataOut",
        "StatementIn": "_spanner_196_StatementIn",
        "StatementOut": "_spanner_197_StatementOut",
        "SetIamPolicyRequestIn": "_spanner_198_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_spanner_199_SetIamPolicyRequestOut",
        "ListOperationsResponseIn": "_spanner_200_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_spanner_201_ListOperationsResponseOut",
        "ListInstancesResponseIn": "_spanner_202_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_spanner_203_ListInstancesResponseOut",
        "ReadWriteIn": "_spanner_204_ReadWriteIn",
        "ReadWriteOut": "_spanner_205_ReadWriteOut",
        "PartialResultSetIn": "_spanner_206_PartialResultSetIn",
        "PartialResultSetOut": "_spanner_207_PartialResultSetOut",
        "PartitionedDmlIn": "_spanner_208_PartitionedDmlIn",
        "PartitionedDmlOut": "_spanner_209_PartitionedDmlOut",
        "ExprIn": "_spanner_210_ExprIn",
        "ExprOut": "_spanner_211_ExprOut",
        "ReadRequestIn": "_spanner_212_ReadRequestIn",
        "ReadRequestOut": "_spanner_213_ReadRequestOut",
        "KeyRangeIn": "_spanner_214_KeyRangeIn",
        "KeyRangeOut": "_spanner_215_KeyRangeOut",
        "CreateDatabaseRequestIn": "_spanner_216_CreateDatabaseRequestIn",
        "CreateDatabaseRequestOut": "_spanner_217_CreateDatabaseRequestOut",
        "ListBackupsResponseIn": "_spanner_218_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_spanner_219_ListBackupsResponseOut",
        "UpdateDatabaseDdlRequestIn": "_spanner_220_UpdateDatabaseDdlRequestIn",
        "UpdateDatabaseDdlRequestOut": "_spanner_221_UpdateDatabaseDdlRequestOut",
        "WriteIn": "_spanner_222_WriteIn",
        "WriteOut": "_spanner_223_WriteOut",
        "OperationProgressIn": "_spanner_224_OperationProgressIn",
        "OperationProgressOut": "_spanner_225_OperationProgressOut",
        "ListBackupOperationsResponseIn": "_spanner_226_ListBackupOperationsResponseIn",
        "ListBackupOperationsResponseOut": "_spanner_227_ListBackupOperationsResponseOut",
        "ExecuteSqlRequestIn": "_spanner_228_ExecuteSqlRequestIn",
        "ExecuteSqlRequestOut": "_spanner_229_ExecuteSqlRequestOut",
        "MutationIn": "_spanner_230_MutationIn",
        "MutationOut": "_spanner_231_MutationOut",
        "CommitRequestIn": "_spanner_232_CommitRequestIn",
        "CommitRequestOut": "_spanner_233_CommitRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ScanDataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "data": t.proxy(renames["VisualizationDataIn"]).optional(),
        }
    ).named(renames["ScanDataIn"])
    types["ScanDataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "data": t.proxy(renames["VisualizationDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanDataOut"])
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
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["UpdateDatabaseMetadataIn"] = t.struct(
        {
            "request": t.proxy(renames["UpdateDatabaseRequestIn"]).optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "cancelTime": t.string().optional(),
        }
    ).named(renames["UpdateDatabaseMetadataIn"])
    types["UpdateDatabaseMetadataOut"] = t.struct(
        {
            "request": t.proxy(renames["UpdateDatabaseRequestOut"]).optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "cancelTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseMetadataOut"])
    types["MetricMatrixRowIn"] = t.struct(
        {"cols": t.array(t.number()).optional()}
    ).named(renames["MetricMatrixRowIn"])
    types["MetricMatrixRowOut"] = t.struct(
        {
            "cols": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixRowOut"])
    types["CreateDatabaseMetadataIn"] = t.struct(
        {"database": t.string().optional()}
    ).named(renames["CreateDatabaseMetadataIn"])
    types["CreateDatabaseMetadataOut"] = t.struct(
        {
            "database": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseMetadataOut"])
    types["UpdateInstanceConfigRequestIn"] = t.struct(
        {
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]),
            "updateMask": t.string(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["UpdateInstanceConfigRequestIn"])
    types["UpdateInstanceConfigRequestOut"] = t.struct(
        {
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]),
            "updateMask": t.string(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceConfigRequestOut"])
    types["ResultSetIn"] = t.struct(
        {
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
        }
    ).named(renames["ResultSetIn"])
    types["ResultSetOut"] = t.struct(
        {
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "rows": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetOut"])
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
    types["UpdateInstanceRequestIn"] = t.struct(
        {"instance": t.proxy(renames["InstanceIn"]), "fieldMask": t.string()}
    ).named(renames["UpdateInstanceRequestIn"])
    types["UpdateInstanceRequestOut"] = t.struct(
        {
            "instance": t.proxy(renames["InstanceOut"]),
            "fieldMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceRequestOut"])
    types["RollbackRequestIn"] = t.struct({"transactionId": t.string()}).named(
        renames["RollbackRequestIn"]
    )
    types["RollbackRequestOut"] = t.struct(
        {
            "transactionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackRequestOut"])
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
    types["VisualizationDataIn"] = t.struct(
        {
            "hasPii": t.boolean().optional(),
            "dataSourceEndToken": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricIn"])).optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeIn"])).optional(),
            "keySeparator": t.string().optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "keyUnit": t.string().optional(),
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageIn"])
            ).optional(),
        }
    ).named(renames["VisualizationDataIn"])
    types["VisualizationDataOut"] = t.struct(
        {
            "hasPii": t.boolean().optional(),
            "dataSourceEndToken": t.string().optional(),
            "metrics": t.array(t.proxy(renames["MetricOut"])).optional(),
            "endKeyStrings": t.array(t.string()).optional(),
            "dataSourceSeparatorToken": t.string().optional(),
            "prefixNodes": t.array(t.proxy(renames["PrefixNodeOut"])).optional(),
            "keySeparator": t.string().optional(),
            "indexedKeys": t.array(t.string()).optional(),
            "keyUnit": t.string().optional(),
            "diagnosticMessages": t.array(
                t.proxy(renames["DiagnosticMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VisualizationDataOut"])
    types["ScanIn"] = t.struct(
        {
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ScanIn"])
    types["ScanOut"] = t.struct(
        {
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "scanData": t.proxy(renames["ScanDataOut"]).optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanOut"])
    types["CreateSessionRequestIn"] = t.struct(
        {"session": t.proxy(renames["SessionIn"])}
    ).named(renames["CreateSessionRequestIn"])
    types["CreateSessionRequestOut"] = t.struct(
        {
            "session": t.proxy(renames["SessionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSessionRequestOut"])
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
    types["ResultSetStatsIn"] = t.struct(
        {
            "rowCountLowerBound": t.string().optional(),
            "rowCountExact": t.string().optional(),
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "queryPlan": t.proxy(renames["QueryPlanIn"]).optional(),
        }
    ).named(renames["ResultSetStatsIn"])
    types["ResultSetStatsOut"] = t.struct(
        {
            "rowCountLowerBound": t.string().optional(),
            "rowCountExact": t.string().optional(),
            "queryStats": t.struct({"_": t.string().optional()}).optional(),
            "queryPlan": t.proxy(renames["QueryPlanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultSetStatsOut"])
    types["EncryptionInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EncryptionInfoIn"]
    )
    types["EncryptionInfoOut"] = t.struct(
        {
            "kmsKeyVersion": t.string().optional(),
            "encryptionStatus": t.proxy(renames["StatusOut"]).optional(),
            "encryptionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionInfoOut"])
    types["CopyBackupRequestIn"] = t.struct(
        {
            "sourceBackup": t.string(),
            "backupId": t.string(),
            "expireTime": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigIn"]
            ).optional(),
        }
    ).named(renames["CopyBackupRequestIn"])
    types["CopyBackupRequestOut"] = t.struct(
        {
            "sourceBackup": t.string(),
            "backupId": t.string(),
            "expireTime": t.string(),
            "encryptionConfig": t.proxy(
                renames["CopyBackupEncryptionConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupRequestOut"])
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
    types["ExecuteBatchDmlRequestIn"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]),
            "seqno": t.string(),
            "statements": t.array(t.proxy(renames["StatementIn"])),
        }
    ).named(renames["ExecuteBatchDmlRequestIn"])
    types["ExecuteBatchDmlRequestOut"] = t.struct(
        {
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]),
            "seqno": t.string(),
            "statements": t.array(t.proxy(renames["StatementOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteBatchDmlRequestOut"])
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
    types["IndexedKeyRangeInfosIn"] = t.struct(
        {"keyRangeInfos": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedKeyRangeInfosIn"])
    types["IndexedKeyRangeInfosOut"] = t.struct(
        {
            "keyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedKeyRangeInfosOut"])
    types["RestoreDatabaseMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "sourceType": t.string().optional(),
            "cancelTime": t.string().optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RestoreDatabaseMetadataIn"])
    types["RestoreDatabaseMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "sourceType": t.string().optional(),
            "cancelTime": t.string().optional(),
            "optimizeDatabaseOperationName": t.string().optional(),
            "backupInfo": t.proxy(renames["BackupInfoOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreDatabaseMetadataOut"])
    types["PrefixNodeIn"] = t.struct(
        {
            "depth": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "word": t.string().optional(),
            "dataSourceNode": t.boolean().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["PrefixNodeIn"])
    types["PrefixNodeOut"] = t.struct(
        {
            "depth": t.integer().optional(),
            "endIndex": t.integer().optional(),
            "word": t.string().optional(),
            "dataSourceNode": t.boolean().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrefixNodeOut"])
    types["UpdateInstanceMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "startTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceIn"]).optional(),
        }
    ).named(renames["UpdateInstanceMetadataIn"])
    types["UpdateInstanceMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "cancelTime": t.string().optional(),
            "startTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceMetadataOut"])
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
    types["CreateBackupMetadataIn"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "cancelTime": t.string().optional(),
            "database": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CreateBackupMetadataIn"])
    types["CreateBackupMetadataOut"] = t.struct(
        {
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "cancelTime": t.string().optional(),
            "database": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateBackupMetadataOut"])
    types["UpdateInstanceConfigMetadataIn"] = t.struct(
        {
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]).optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["InstanceOperationProgressIn"]).optional(),
        }
    ).named(renames["UpdateInstanceConfigMetadataIn"])
    types["UpdateInstanceConfigMetadataOut"] = t.struct(
        {
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]).optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["InstanceOperationProgressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateInstanceConfigMetadataOut"])
    types["ListDatabaseRolesResponseIn"] = t.struct(
        {
            "databaseRoles": t.array(t.proxy(renames["DatabaseRoleIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDatabaseRolesResponseIn"])
    types["ListDatabaseRolesResponseOut"] = t.struct(
        {
            "databaseRoles": t.array(t.proxy(renames["DatabaseRoleOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatabaseRolesResponseOut"])
    types["InstanceConfigIn"] = t.struct(
        {
            "baseConfig": t.string().optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["InstanceConfigIn"])
    types["InstanceConfigOut"] = t.struct(
        {
            "configType": t.string().optional(),
            "baseConfig": t.string().optional(),
            "replicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "leaderOptions": t.array(t.string()).optional(),
            "freeInstanceAvailability": t.string().optional(),
            "displayName": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "optionalReplicas": t.array(t.proxy(renames["ReplicaInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["BackupInfoIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "backup": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "versionTime": t.string().optional(),
        }
    ).named(renames["BackupInfoIn"])
    types["BackupInfoOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "backup": t.string().optional(),
            "sourceDatabase": t.string().optional(),
            "versionTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupInfoOut"])
    types["CopyBackupMetadataIn"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CopyBackupMetadataIn"])
    types["CopyBackupMetadataOut"] = t.struct(
        {
            "sourceBackup": t.string().optional(),
            "cancelTime": t.string().optional(),
            "progress": t.proxy(renames["OperationProgressOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyBackupMetadataOut"])
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
            "name": t.string().optional(),
            "creatorRole": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOut"])
    types["PartitionQueryRequestIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PartitionQueryRequestIn"])
    types["PartitionQueryRequestOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionQueryRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["RequestOptionsIn"] = t.struct(
        {
            "requestTag": t.string().optional(),
            "transactionTag": t.string().optional(),
            "priority": t.string().optional(),
        }
    ).named(renames["RequestOptionsIn"])
    types["RequestOptionsOut"] = t.struct(
        {
            "requestTag": t.string().optional(),
            "transactionTag": t.string().optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOptionsOut"])
    types["BackupIn"] = t.struct(
        {
            "versionTime": t.string().optional(),
            "database": t.string(),
            "expireTime": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "referencingDatabases": t.array(t.string()).optional(),
            "versionTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "database": t.string(),
            "databaseDialect": t.string().optional(),
            "referencingBackups": t.array(t.string()).optional(),
            "expireTime": t.string(),
            "name": t.string().optional(),
            "encryptionInfo": t.proxy(renames["EncryptionInfoOut"]).optional(),
            "maxExpireTime": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["DiagnosticMessageIn"] = t.struct(
        {
            "metricSpecific": t.boolean().optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "severity": t.string().optional(),
            "shortMessage": t.proxy(renames["LocalizedStringIn"]).optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
        }
    ).named(renames["DiagnosticMessageIn"])
    types["DiagnosticMessageOut"] = t.struct(
        {
            "metricSpecific": t.boolean().optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "severity": t.string().optional(),
            "shortMessage": t.proxy(renames["LocalizedStringOut"]).optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnosticMessageOut"])
    types["IndexedHotKeyIn"] = t.struct(
        {"sparseHotKeys": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["IndexedHotKeyIn"])
    types["IndexedHotKeyOut"] = t.struct(
        {
            "sparseHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexedHotKeyOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["KeyRangeInfoIn"] = t.struct(
        {
            "keysCount": t.string().optional(),
            "value": t.number().optional(),
            "timeOffset": t.string().optional(),
            "metric": t.proxy(renames["LocalizedStringIn"]).optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "startKeyIndex": t.integer().optional(),
            "endKeyIndex": t.integer().optional(),
            "contextValues": t.array(t.proxy(renames["ContextValueIn"])).optional(),
        }
    ).named(renames["KeyRangeInfoIn"])
    types["KeyRangeInfoOut"] = t.struct(
        {
            "keysCount": t.string().optional(),
            "value": t.number().optional(),
            "timeOffset": t.string().optional(),
            "metric": t.proxy(renames["LocalizedStringOut"]).optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "startKeyIndex": t.integer().optional(),
            "endKeyIndex": t.integer().optional(),
            "contextValues": t.array(t.proxy(renames["ContextValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeInfoOut"])
    types["KeySetIn"] = t.struct(
        {
            "all": t.boolean().optional(),
            "keys": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "ranges": t.array(t.proxy(renames["KeyRangeIn"])).optional(),
        }
    ).named(renames["KeySetIn"])
    types["KeySetOut"] = t.struct(
        {
            "all": t.boolean().optional(),
            "keys": t.array(t.array(t.struct({"_": t.string().optional()}))).optional(),
            "ranges": t.array(t.proxy(renames["KeyRangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeySetOut"])
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
    types["MetricIn"] = t.struct(
        {
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "derived": t.proxy(renames["DerivedMetricIn"]).optional(),
            "category": t.proxy(renames["LocalizedStringIn"]).optional(),
            "visible": t.boolean().optional(),
            "displayLabel": t.proxy(renames["LocalizedStringIn"]).optional(),
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "matrix": t.proxy(renames["MetricMatrixIn"]).optional(),
            "aggregation": t.string().optional(),
            "unit": t.proxy(renames["LocalizedStringIn"]).optional(),
            "info": t.proxy(renames["LocalizedStringIn"]).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "hotValue": t.number().optional(),
        }
    ).named(renames["MetricIn"])
    types["MetricOut"] = t.struct(
        {
            "indexedHotKeys": t.struct({"_": t.string().optional()}).optional(),
            "derived": t.proxy(renames["DerivedMetricOut"]).optional(),
            "category": t.proxy(renames["LocalizedStringOut"]).optional(),
            "visible": t.boolean().optional(),
            "displayLabel": t.proxy(renames["LocalizedStringOut"]).optional(),
            "indexedKeyRangeInfos": t.struct({"_": t.string().optional()}).optional(),
            "matrix": t.proxy(renames["MetricMatrixOut"]).optional(),
            "aggregation": t.string().optional(),
            "unit": t.proxy(renames["LocalizedStringOut"]).optional(),
            "info": t.proxy(renames["LocalizedStringOut"]).optional(),
            "hasNonzeroData": t.boolean().optional(),
            "hotValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricOut"])
    types["BatchCreateSessionsResponseIn"] = t.struct(
        {"session": t.array(t.proxy(renames["SessionIn"])).optional()}
    ).named(renames["BatchCreateSessionsResponseIn"])
    types["BatchCreateSessionsResponseOut"] = t.struct(
        {
            "session": t.array(t.proxy(renames["SessionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateSessionsResponseOut"])
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
    types["InstanceOperationProgressIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["InstanceOperationProgressIn"])
    types["InstanceOperationProgressOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOperationProgressOut"])
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
    types["PartitionReadRequestIn"] = t.struct(
        {
            "keySet": t.proxy(renames["KeySetIn"]),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsIn"]).optional(),
            "table": t.string(),
            "index": t.string().optional(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["PartitionReadRequestIn"])
    types["PartitionReadRequestOut"] = t.struct(
        {
            "keySet": t.proxy(renames["KeySetOut"]),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "partitionOptions": t.proxy(renames["PartitionOptionsOut"]).optional(),
            "table": t.string(),
            "index": t.string().optional(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionReadRequestOut"])
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
    types["DatabaseRoleIn"] = t.struct({"name": t.string()}).named(
        renames["DatabaseRoleIn"]
    )
    types["DatabaseRoleOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DatabaseRoleOut"])
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
    types["CommitStatsIn"] = t.struct({"mutationCount": t.string().optional()}).named(
        renames["CommitStatsIn"]
    )
    types["CommitStatsOut"] = t.struct(
        {
            "mutationCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitStatsOut"])
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
    types["QueryPlanIn"] = t.struct(
        {"planNodes": t.array(t.proxy(renames["PlanNodeIn"])).optional()}
    ).named(renames["QueryPlanIn"])
    types["QueryPlanOut"] = t.struct(
        {
            "planNodes": t.array(t.proxy(renames["PlanNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryPlanOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["DatabaseIn"] = t.struct(
        {"enableDropProtection": t.boolean().optional(), "name": t.string()}
    ).named(renames["DatabaseIn"])
    types["DatabaseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "enableDropProtection": t.boolean().optional(),
            "restoreInfo": t.proxy(renames["RestoreInfoOut"]).optional(),
            "encryptionInfo": t.array(t.proxy(renames["EncryptionInfoOut"])).optional(),
            "defaultLeader": t.string().optional(),
            "versionRetentionPeriod": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "earliestVersionTime": t.string().optional(),
            "createTime": t.string().optional(),
            "databaseDialect": t.string().optional(),
            "name": t.string(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseOut"])
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
    types["PlanNodeIn"] = t.struct(
        {
            "shortRepresentation": t.proxy(renames["ShortRepresentationIn"]).optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkIn"])).optional(),
            "kind": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["PlanNodeIn"])
    types["PlanNodeOut"] = t.struct(
        {
            "shortRepresentation": t.proxy(
                renames["ShortRepresentationOut"]
            ).optional(),
            "childLinks": t.array(t.proxy(renames["ChildLinkOut"])).optional(),
            "kind": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "executionStats": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlanNodeOut"])
    types["PartitionIn"] = t.struct({"partitionToken": t.string().optional()}).named(
        renames["PartitionIn"]
    )
    types["PartitionOut"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionOut"])
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
    types["EncryptionConfigIn"] = t.struct({"kmsKeyName": t.string().optional()}).named(
        renames["EncryptionConfigIn"]
    )
    types["EncryptionConfigOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigOut"])
    types["CreateInstanceMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceIn"]).optional(),
            "cancelTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["CreateInstanceMetadataIn"])
    types["CreateInstanceMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "instance": t.proxy(renames["InstanceOut"]).optional(),
            "cancelTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceMetadataOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["CreateInstanceConfigRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "instanceConfigId": t.string(),
            "instanceConfig": t.proxy(renames["InstanceConfigIn"]),
        }
    ).named(renames["CreateInstanceConfigRequestIn"])
    types["CreateInstanceConfigRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "instanceConfigId": t.string(),
            "instanceConfig": t.proxy(renames["InstanceConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateInstanceConfigRequestOut"])
    types["TypeIn"] = t.struct(
        {
            "protoTypeFqn": t.string().optional(),
            "arrayElementType": t.proxy(renames["TypeIn"]).optional(),
            "code": t.string(),
            "structType": t.proxy(renames["StructTypeIn"]).optional(),
            "typeAnnotation": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "protoTypeFqn": t.string().optional(),
            "arrayElementType": t.proxy(renames["TypeOut"]).optional(),
            "code": t.string(),
            "structType": t.proxy(renames["StructTypeOut"]).optional(),
            "typeAnnotation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["ContextValueIn"] = t.struct(
        {
            "label": t.proxy(renames["LocalizedStringIn"]).optional(),
            "value": t.number().optional(),
            "severity": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["ContextValueIn"])
    types["ContextValueOut"] = t.struct(
        {
            "label": t.proxy(renames["LocalizedStringOut"]).optional(),
            "value": t.number().optional(),
            "severity": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextValueOut"])
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
    types["InstanceIn"] = t.struct(
        {
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataIn"]
            ).optional(),
            "config": t.string(),
            "instanceType": t.string().optional(),
            "endpointUris": t.array(t.string()).optional(),
            "processingUnits": t.integer().optional(),
            "nodeCount": t.integer().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "freeInstanceMetadata": t.proxy(
                renames["FreeInstanceMetadataOut"]
            ).optional(),
            "config": t.string(),
            "instanceType": t.string().optional(),
            "endpointUris": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "processingUnits": t.integer().optional(),
            "nodeCount": t.integer().optional(),
            "state": t.string().optional(),
            "displayName": t.string(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
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
    types["LocalizedStringIn"] = t.struct(
        {
            "message": t.string().optional(),
            "args": t.struct({"_": t.string().optional()}).optional(),
            "token": t.string().optional(),
        }
    ).named(renames["LocalizedStringIn"])
    types["LocalizedStringOut"] = t.struct(
        {
            "message": t.string().optional(),
            "args": t.struct({"_": t.string().optional()}).optional(),
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedStringOut"])
    types["MetricMatrixIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["MetricMatrixRowIn"])).optional()}
    ).named(renames["MetricMatrixIn"])
    types["MetricMatrixOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["MetricMatrixRowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricMatrixOut"])
    types["ReadOnlyIn"] = t.struct(
        {
            "strong": t.boolean().optional(),
            "minReadTimestamp": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "readTimestamp": t.string().optional(),
            "returnReadTimestamp": t.boolean().optional(),
            "exactStaleness": t.string().optional(),
        }
    ).named(renames["ReadOnlyIn"])
    types["ReadOnlyOut"] = t.struct(
        {
            "strong": t.boolean().optional(),
            "minReadTimestamp": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "readTimestamp": t.string().optional(),
            "returnReadTimestamp": t.boolean().optional(),
            "exactStaleness": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadOnlyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["UpdateDatabaseDdlMetadataIn"] = t.struct(
        {
            "progress": t.array(t.proxy(renames["OperationProgressIn"])).optional(),
            "database": t.string().optional(),
            "commitTimestamps": t.array(t.string()).optional(),
            "statements": t.array(t.string()).optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataIn"])
    types["UpdateDatabaseDdlMetadataOut"] = t.struct(
        {
            "progress": t.array(t.proxy(renames["OperationProgressOut"])).optional(),
            "database": t.string().optional(),
            "commitTimestamps": t.array(t.string()).optional(),
            "throttled": t.boolean().optional(),
            "statements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDatabaseDdlMetadataOut"])
    types["StatementIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
        }
    ).named(renames["StatementIn"])
    types["StatementOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "sql": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatementOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["ListInstancesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["ReadWriteIn"] = t.struct({"readLockMode": t.string().optional()}).named(
        renames["ReadWriteIn"]
    )
    types["ReadWriteOut"] = t.struct(
        {
            "readLockMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadWriteOut"])
    types["PartialResultSetIn"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "metadata": t.proxy(renames["ResultSetMetadataIn"]).optional(),
            "resumeToken": t.string().optional(),
            "chunkedValue": t.boolean().optional(),
            "stats": t.proxy(renames["ResultSetStatsIn"]).optional(),
        }
    ).named(renames["PartialResultSetIn"])
    types["PartialResultSetOut"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "metadata": t.proxy(renames["ResultSetMetadataOut"]).optional(),
            "resumeToken": t.string().optional(),
            "chunkedValue": t.boolean().optional(),
            "stats": t.proxy(renames["ResultSetStatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartialResultSetOut"])
    types["PartitionedDmlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PartitionedDmlIn"]
    )
    types["PartitionedDmlOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartitionedDmlOut"])
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
    types["ReadRequestIn"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "keySet": t.proxy(renames["KeySetIn"]),
            "limit": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "resumeToken": t.string().optional(),
            "columns": t.array(t.string()),
            "dataBoostEnabled": t.boolean().optional(),
            "table": t.string(),
            "index": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
        }
    ).named(renames["ReadRequestIn"])
    types["ReadRequestOut"] = t.struct(
        {
            "partitionToken": t.string().optional(),
            "keySet": t.proxy(renames["KeySetOut"]),
            "limit": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "resumeToken": t.string().optional(),
            "columns": t.array(t.string()),
            "dataBoostEnabled": t.boolean().optional(),
            "table": t.string(),
            "index": t.string().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadRequestOut"])
    types["KeyRangeIn"] = t.struct(
        {
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["KeyRangeIn"])
    types["KeyRangeOut"] = t.struct(
        {
            "endOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "endClosed": t.array(t.struct({"_": t.string().optional()})).optional(),
            "startOpen": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyRangeOut"])
    types["CreateDatabaseRequestIn"] = t.struct(
        {
            "createStatement": t.string(),
            "protoDescriptors": t.string().optional(),
            "extraStatements": t.array(t.string()).optional(),
            "databaseDialect": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigIn"]).optional(),
        }
    ).named(renames["CreateDatabaseRequestIn"])
    types["CreateDatabaseRequestOut"] = t.struct(
        {
            "createStatement": t.string(),
            "protoDescriptors": t.string().optional(),
            "extraStatements": t.array(t.string()).optional(),
            "databaseDialect": t.string().optional(),
            "encryptionConfig": t.proxy(renames["EncryptionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateDatabaseRequestOut"])
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
    types["WriteIn"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "table": t.string(),
            "columns": t.array(t.string()).optional(),
        }
    ).named(renames["WriteIn"])
    types["WriteOut"] = t.struct(
        {
            "values": t.array(
                t.array(t.struct({"_": t.string().optional()}))
            ).optional(),
            "table": t.string(),
            "columns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteOut"])
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
    types["ExecuteSqlRequestIn"] = t.struct(
        {
            "dataBoostEnabled": t.boolean().optional(),
            "queryMode": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorIn"]).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "queryOptions": t.proxy(renames["QueryOptionsIn"]).optional(),
            "partitionToken": t.string().optional(),
            "resumeToken": t.string().optional(),
            "sql": t.string(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
            "seqno": t.string().optional(),
        }
    ).named(renames["ExecuteSqlRequestIn"])
    types["ExecuteSqlRequestOut"] = t.struct(
        {
            "dataBoostEnabled": t.boolean().optional(),
            "queryMode": t.string().optional(),
            "transaction": t.proxy(renames["TransactionSelectorOut"]).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "paramTypes": t.struct({"_": t.string().optional()}).optional(),
            "queryOptions": t.proxy(renames["QueryOptionsOut"]).optional(),
            "partitionToken": t.string().optional(),
            "resumeToken": t.string().optional(),
            "sql": t.string(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "seqno": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlRequestOut"])
    types["MutationIn"] = t.struct(
        {
            "insert": t.proxy(renames["WriteIn"]).optional(),
            "replace": t.proxy(renames["WriteIn"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteIn"]).optional(),
            "update": t.proxy(renames["WriteIn"]).optional(),
            "delete": t.proxy(renames["DeleteIn"]).optional(),
        }
    ).named(renames["MutationIn"])
    types["MutationOut"] = t.struct(
        {
            "insert": t.proxy(renames["WriteOut"]).optional(),
            "replace": t.proxy(renames["WriteOut"]).optional(),
            "insertOrUpdate": t.proxy(renames["WriteOut"]).optional(),
            "update": t.proxy(renames["WriteOut"]).optional(),
            "delete": t.proxy(renames["DeleteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MutationOut"])
    types["CommitRequestIn"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "mutations": t.array(t.proxy(renames["MutationIn"])).optional(),
            "singleUseTransaction": t.proxy(renames["TransactionOptionsIn"]).optional(),
            "returnCommitStats": t.boolean().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
        }
    ).named(renames["CommitRequestIn"])
    types["CommitRequestOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "mutations": t.array(t.proxy(renames["MutationOut"])).optional(),
            "singleUseTransaction": t.proxy(
                renames["TransactionOptionsOut"]
            ).optional(),
            "returnCommitStats": t.boolean().optional(),
            "requestOptions": t.proxy(renames["RequestOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitRequestOut"])

    functions = {}
    functions["scansList"] = spanner.get(
        "v1/{parent}",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsGet"] = spanner.delete(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsGet"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsList"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsDelete"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstanceConfigsOperationsCancel"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesTestIamPermissions"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGetIamPolicy"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesGet"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesSetIamPolicy"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesCreate"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDelete"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesPatch"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesList"] = spanner.get(
        "v1/{parent}/instances",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "instanceDeadline": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInstancesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabaseOperationsList"] = spanner.get(
        "v1/{parent}/databaseOperations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatabaseOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsDelete"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsGet"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsList"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesOperationsCancel"] = spanner.post(
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
    functions["projectsInstancesInstancePartitionsOperationsCancel"] = spanner.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsInstancesBackupsOperationsCancel"] = spanner.get(
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
    functions["projectsInstancesBackupsOperationsList"] = spanner.get(
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
    functions["projectsInstancesBackupOperationsList"] = spanner.get(
        "v1/{parent}/backupOperations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesDropDatabase"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesCreate"] = spanner.get(
        "v1/{name}/scans",
        t.struct(
            {
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
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
                "startTime": t.string().optional(),
                "name": t.string(),
                "view": t.string().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanOut"]),
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
    functions["projectsInstancesDatabasesOperationsGet"] = spanner.delete(
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
    functions[
        "projectsInstancesDatabasesDatabaseRolesTestIamPermissions"
    ] = spanner.get(
        "v1/{parent}/databaseRoles",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatabaseRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsGet"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsPartitionRead"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteStreamingSql"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsPartitionQuery"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsDelete"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCreate"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsStreamingRead"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRollback"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteBatchDml"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsRead"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsCommit"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBatchCreate"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsExecuteSql"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsList"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInstancesDatabasesSessionsBeginTransaction"] = spanner.post(
        "v1/{session}:beginTransaction",
        t.struct(
            {
                "session": t.string(),
                "options": t.proxy(renames["TransactionOptionsIn"]),
                "requestOptions": t.proxy(renames["RequestOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransactionOut"]),
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

    return Import(importer="spanner", renames=renames, types=types, functions=functions)
