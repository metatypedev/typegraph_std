from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_bigquery():
    bigquery = HTTPRuntime("https://bigquery.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigquery_1_ErrorResponse",
        "TableReferenceIn": "_bigquery_2_TableReferenceIn",
        "TableReferenceOut": "_bigquery_3_TableReferenceOut",
        "QueryTimelineSampleIn": "_bigquery_4_QueryTimelineSampleIn",
        "QueryTimelineSampleOut": "_bigquery_5_QueryTimelineSampleOut",
        "QueryRequestIn": "_bigquery_6_QueryRequestIn",
        "QueryRequestOut": "_bigquery_7_QueryRequestOut",
        "BigtableColumnIn": "_bigquery_8_BigtableColumnIn",
        "BigtableColumnOut": "_bigquery_9_BigtableColumnOut",
        "JobListIn": "_bigquery_10_JobListIn",
        "JobListOut": "_bigquery_11_JobListOut",
        "EncryptionConfigurationIn": "_bigquery_12_EncryptionConfigurationIn",
        "EncryptionConfigurationOut": "_bigquery_13_EncryptionConfigurationOut",
        "StreamingbufferIn": "_bigquery_14_StreamingbufferIn",
        "StreamingbufferOut": "_bigquery_15_StreamingbufferOut",
        "JobConfigurationQueryIn": "_bigquery_16_JobConfigurationQueryIn",
        "JobConfigurationQueryOut": "_bigquery_17_JobConfigurationQueryOut",
        "RoutineIn": "_bigquery_18_RoutineIn",
        "RoutineOut": "_bigquery_19_RoutineOut",
        "SessionInfoIn": "_bigquery_20_SessionInfoIn",
        "SessionInfoOut": "_bigquery_21_SessionInfoOut",
        "JsonOptionsIn": "_bigquery_22_JsonOptionsIn",
        "JsonOptionsOut": "_bigquery_23_JsonOptionsOut",
        "AvroOptionsIn": "_bigquery_24_AvroOptionsIn",
        "AvroOptionsOut": "_bigquery_25_AvroOptionsOut",
        "TableListIn": "_bigquery_26_TableListIn",
        "TableListOut": "_bigquery_27_TableListOut",
        "RegressionMetricsIn": "_bigquery_28_RegressionMetricsIn",
        "RegressionMetricsOut": "_bigquery_29_RegressionMetricsOut",
        "SparkLoggingInfoIn": "_bigquery_30_SparkLoggingInfoIn",
        "SparkLoggingInfoOut": "_bigquery_31_SparkLoggingInfoOut",
        "ExternalDataConfigurationIn": "_bigquery_32_ExternalDataConfigurationIn",
        "ExternalDataConfigurationOut": "_bigquery_33_ExternalDataConfigurationOut",
        "IterationResultIn": "_bigquery_34_IterationResultIn",
        "IterationResultOut": "_bigquery_35_IterationResultOut",
        "RowLevelSecurityStatisticsIn": "_bigquery_36_RowLevelSecurityStatisticsIn",
        "RowLevelSecurityStatisticsOut": "_bigquery_37_RowLevelSecurityStatisticsOut",
        "DmlStatisticsIn": "_bigquery_38_DmlStatisticsIn",
        "DmlStatisticsOut": "_bigquery_39_DmlStatisticsOut",
        "ArimaResultIn": "_bigquery_40_ArimaResultIn",
        "ArimaResultOut": "_bigquery_41_ArimaResultOut",
        "BiEngineReasonIn": "_bigquery_42_BiEngineReasonIn",
        "BiEngineReasonOut": "_bigquery_43_BiEngineReasonOut",
        "LocationMetadataIn": "_bigquery_44_LocationMetadataIn",
        "LocationMetadataOut": "_bigquery_45_LocationMetadataOut",
        "AuditLogConfigIn": "_bigquery_46_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigquery_47_AuditLogConfigOut",
        "DataSplitResultIn": "_bigquery_48_DataSplitResultIn",
        "DataSplitResultOut": "_bigquery_49_DataSplitResultOut",
        "AggregateClassificationMetricsIn": "_bigquery_50_AggregateClassificationMetricsIn",
        "AggregateClassificationMetricsOut": "_bigquery_51_AggregateClassificationMetricsOut",
        "GetIamPolicyRequestIn": "_bigquery_52_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigquery_53_GetIamPolicyRequestOut",
        "JobReferenceIn": "_bigquery_54_JobReferenceIn",
        "JobReferenceOut": "_bigquery_55_JobReferenceOut",
        "CloneDefinitionIn": "_bigquery_56_CloneDefinitionIn",
        "CloneDefinitionOut": "_bigquery_57_CloneDefinitionOut",
        "BinaryConfusionMatrixIn": "_bigquery_58_BinaryConfusionMatrixIn",
        "BinaryConfusionMatrixOut": "_bigquery_59_BinaryConfusionMatrixOut",
        "QueryResponseIn": "_bigquery_60_QueryResponseIn",
        "QueryResponseOut": "_bigquery_61_QueryResponseOut",
        "DimensionalityReductionMetricsIn": "_bigquery_62_DimensionalityReductionMetricsIn",
        "DimensionalityReductionMetricsOut": "_bigquery_63_DimensionalityReductionMetricsOut",
        "ArgumentIn": "_bigquery_64_ArgumentIn",
        "ArgumentOut": "_bigquery_65_ArgumentOut",
        "DestinationTablePropertiesIn": "_bigquery_66_DestinationTablePropertiesIn",
        "DestinationTablePropertiesOut": "_bigquery_67_DestinationTablePropertiesOut",
        "ParquetOptionsIn": "_bigquery_68_ParquetOptionsIn",
        "ParquetOptionsOut": "_bigquery_69_ParquetOptionsOut",
        "DatasetListIn": "_bigquery_70_DatasetListIn",
        "DatasetListOut": "_bigquery_71_DatasetListOut",
        "GlobalExplanationIn": "_bigquery_72_GlobalExplanationIn",
        "GlobalExplanationOut": "_bigquery_73_GlobalExplanationOut",
        "DatasetAccessEntryIn": "_bigquery_74_DatasetAccessEntryIn",
        "DatasetAccessEntryOut": "_bigquery_75_DatasetAccessEntryOut",
        "IntArrayIn": "_bigquery_76_IntArrayIn",
        "IntArrayOut": "_bigquery_77_IntArrayOut",
        "BqmlIterationResultIn": "_bigquery_78_BqmlIterationResultIn",
        "BqmlIterationResultOut": "_bigquery_79_BqmlIterationResultOut",
        "TrainingOptionsIn": "_bigquery_80_TrainingOptionsIn",
        "TrainingOptionsOut": "_bigquery_81_TrainingOptionsOut",
        "RowIn": "_bigquery_82_RowIn",
        "RowOut": "_bigquery_83_RowOut",
        "JobCancelResponseIn": "_bigquery_84_JobCancelResponseIn",
        "JobCancelResponseOut": "_bigquery_85_JobCancelResponseOut",
        "TimePartitioningIn": "_bigquery_86_TimePartitioningIn",
        "TimePartitioningOut": "_bigquery_87_TimePartitioningOut",
        "HparamTuningTrialIn": "_bigquery_88_HparamTuningTrialIn",
        "HparamTuningTrialOut": "_bigquery_89_HparamTuningTrialOut",
        "AuditConfigIn": "_bigquery_90_AuditConfigIn",
        "AuditConfigOut": "_bigquery_91_AuditConfigOut",
        "StandardSqlFieldIn": "_bigquery_92_StandardSqlFieldIn",
        "StandardSqlFieldOut": "_bigquery_93_StandardSqlFieldOut",
        "DatasetReferenceIn": "_bigquery_94_DatasetReferenceIn",
        "DatasetReferenceOut": "_bigquery_95_DatasetReferenceOut",
        "ArimaSingleModelForecastingMetricsIn": "_bigquery_96_ArimaSingleModelForecastingMetricsIn",
        "ArimaSingleModelForecastingMetricsOut": "_bigquery_97_ArimaSingleModelForecastingMetricsOut",
        "ClusterIn": "_bigquery_98_ClusterIn",
        "ClusterOut": "_bigquery_99_ClusterOut",
        "ClusteringMetricsIn": "_bigquery_100_ClusteringMetricsIn",
        "ClusteringMetricsOut": "_bigquery_101_ClusteringMetricsOut",
        "RemoteModelInfoIn": "_bigquery_102_RemoteModelInfoIn",
        "RemoteModelInfoOut": "_bigquery_103_RemoteModelInfoOut",
        "HivePartitioningOptionsIn": "_bigquery_104_HivePartitioningOptionsIn",
        "HivePartitioningOptionsOut": "_bigquery_105_HivePartitioningOptionsOut",
        "ExplanationIn": "_bigquery_106_ExplanationIn",
        "ExplanationOut": "_bigquery_107_ExplanationOut",
        "JobStatistics3In": "_bigquery_108_JobStatistics3In",
        "JobStatistics3Out": "_bigquery_109_JobStatistics3Out",
        "SearchStatisticsIn": "_bigquery_110_SearchStatisticsIn",
        "SearchStatisticsOut": "_bigquery_111_SearchStatisticsOut",
        "ExprIn": "_bigquery_112_ExprIn",
        "ExprOut": "_bigquery_113_ExprOut",
        "ProjectListIn": "_bigquery_114_ProjectListIn",
        "ProjectListOut": "_bigquery_115_ProjectListOut",
        "JobConfigurationTableCopyIn": "_bigquery_116_JobConfigurationTableCopyIn",
        "JobConfigurationTableCopyOut": "_bigquery_117_JobConfigurationTableCopyOut",
        "StandardSqlStructTypeIn": "_bigquery_118_StandardSqlStructTypeIn",
        "StandardSqlStructTypeOut": "_bigquery_119_StandardSqlStructTypeOut",
        "TableCellIn": "_bigquery_120_TableCellIn",
        "TableCellOut": "_bigquery_121_TableCellOut",
        "TableRowIn": "_bigquery_122_TableRowIn",
        "TableRowOut": "_bigquery_123_TableRowOut",
        "ViewDefinitionIn": "_bigquery_124_ViewDefinitionIn",
        "ViewDefinitionOut": "_bigquery_125_ViewDefinitionOut",
        "BinaryClassificationMetricsIn": "_bigquery_126_BinaryClassificationMetricsIn",
        "BinaryClassificationMetricsOut": "_bigquery_127_BinaryClassificationMetricsOut",
        "JobConfigurationIn": "_bigquery_128_JobConfigurationIn",
        "JobConfigurationOut": "_bigquery_129_JobConfigurationOut",
        "RowAccessPolicyIn": "_bigquery_130_RowAccessPolicyIn",
        "RowAccessPolicyOut": "_bigquery_131_RowAccessPolicyOut",
        "RankingMetricsIn": "_bigquery_132_RankingMetricsIn",
        "RankingMetricsOut": "_bigquery_133_RankingMetricsOut",
        "JobStatusIn": "_bigquery_134_JobStatusIn",
        "JobStatusOut": "_bigquery_135_JobStatusOut",
        "CategoryCountIn": "_bigquery_136_CategoryCountIn",
        "CategoryCountOut": "_bigquery_137_CategoryCountOut",
        "ScriptStatisticsIn": "_bigquery_138_ScriptStatisticsIn",
        "ScriptStatisticsOut": "_bigquery_139_ScriptStatisticsOut",
        "StandardSqlDataTypeIn": "_bigquery_140_StandardSqlDataTypeIn",
        "StandardSqlDataTypeOut": "_bigquery_141_StandardSqlDataTypeOut",
        "UserDefinedFunctionResourceIn": "_bigquery_142_UserDefinedFunctionResourceIn",
        "UserDefinedFunctionResourceOut": "_bigquery_143_UserDefinedFunctionResourceOut",
        "JobStatistics4In": "_bigquery_144_JobStatistics4In",
        "JobStatistics4Out": "_bigquery_145_JobStatistics4Out",
        "JobStatisticsIn": "_bigquery_146_JobStatisticsIn",
        "JobStatisticsOut": "_bigquery_147_JobStatisticsOut",
        "ModelReferenceIn": "_bigquery_148_ModelReferenceIn",
        "ModelReferenceOut": "_bigquery_149_ModelReferenceOut",
        "TestIamPermissionsResponseIn": "_bigquery_150_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigquery_151_TestIamPermissionsResponseOut",
        "GetServiceAccountResponseIn": "_bigquery_152_GetServiceAccountResponseIn",
        "GetServiceAccountResponseOut": "_bigquery_153_GetServiceAccountResponseOut",
        "JobConfigurationExtractIn": "_bigquery_154_JobConfigurationExtractIn",
        "JobConfigurationExtractOut": "_bigquery_155_JobConfigurationExtractOut",
        "IntHparamSearchSpaceIn": "_bigquery_156_IntHparamSearchSpaceIn",
        "IntHparamSearchSpaceOut": "_bigquery_157_IntHparamSearchSpaceOut",
        "ArimaFittingMetricsIn": "_bigquery_158_ArimaFittingMetricsIn",
        "ArimaFittingMetricsOut": "_bigquery_159_ArimaFittingMetricsOut",
        "EntryIn": "_bigquery_160_EntryIn",
        "EntryOut": "_bigquery_161_EntryOut",
        "IntCandidatesIn": "_bigquery_162_IntCandidatesIn",
        "IntCandidatesOut": "_bigquery_163_IntCandidatesOut",
        "TableFieldSchemaIn": "_bigquery_164_TableFieldSchemaIn",
        "TableFieldSchemaOut": "_bigquery_165_TableFieldSchemaOut",
        "BigtableColumnFamilyIn": "_bigquery_166_BigtableColumnFamilyIn",
        "BigtableColumnFamilyOut": "_bigquery_167_BigtableColumnFamilyOut",
        "BqmlTrainingRunIn": "_bigquery_168_BqmlTrainingRunIn",
        "BqmlTrainingRunOut": "_bigquery_169_BqmlTrainingRunOut",
        "MaterializedViewDefinitionIn": "_bigquery_170_MaterializedViewDefinitionIn",
        "MaterializedViewDefinitionOut": "_bigquery_171_MaterializedViewDefinitionOut",
        "QueryParameterIn": "_bigquery_172_QueryParameterIn",
        "QueryParameterOut": "_bigquery_173_QueryParameterOut",
        "TestIamPermissionsRequestIn": "_bigquery_174_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigquery_175_TestIamPermissionsRequestOut",
        "SnapshotDefinitionIn": "_bigquery_176_SnapshotDefinitionIn",
        "SnapshotDefinitionOut": "_bigquery_177_SnapshotDefinitionOut",
        "HparamSearchSpacesIn": "_bigquery_178_HparamSearchSpacesIn",
        "HparamSearchSpacesOut": "_bigquery_179_HparamSearchSpacesOut",
        "ModelDefinitionIn": "_bigquery_180_ModelDefinitionIn",
        "ModelDefinitionOut": "_bigquery_181_ModelDefinitionOut",
        "DoubleCandidatesIn": "_bigquery_182_DoubleCandidatesIn",
        "DoubleCandidatesOut": "_bigquery_183_DoubleCandidatesOut",
        "GetPolicyOptionsIn": "_bigquery_184_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigquery_185_GetPolicyOptionsOut",
        "TrainingRunIn": "_bigquery_186_TrainingRunIn",
        "TrainingRunOut": "_bigquery_187_TrainingRunOut",
        "StringHparamSearchSpaceIn": "_bigquery_188_StringHparamSearchSpaceIn",
        "StringHparamSearchSpaceOut": "_bigquery_189_StringHparamSearchSpaceOut",
        "ExplainQueryStageIn": "_bigquery_190_ExplainQueryStageIn",
        "ExplainQueryStageOut": "_bigquery_191_ExplainQueryStageOut",
        "JobConfigurationLoadIn": "_bigquery_192_JobConfigurationLoadIn",
        "JobConfigurationLoadOut": "_bigquery_193_JobConfigurationLoadOut",
        "JobStatistics2In": "_bigquery_194_JobStatistics2In",
        "JobStatistics2Out": "_bigquery_195_JobStatistics2Out",
        "TableDataInsertAllRequestIn": "_bigquery_196_TableDataInsertAllRequestIn",
        "TableDataInsertAllRequestOut": "_bigquery_197_TableDataInsertAllRequestOut",
        "GetQueryResultsResponseIn": "_bigquery_198_GetQueryResultsResponseIn",
        "GetQueryResultsResponseOut": "_bigquery_199_GetQueryResultsResponseOut",
        "TableConstraintsIn": "_bigquery_200_TableConstraintsIn",
        "TableConstraintsOut": "_bigquery_201_TableConstraintsOut",
        "ArimaForecastingMetricsIn": "_bigquery_202_ArimaForecastingMetricsIn",
        "ArimaForecastingMetricsOut": "_bigquery_203_ArimaForecastingMetricsOut",
        "JobStatistics5In": "_bigquery_204_JobStatistics5In",
        "JobStatistics5Out": "_bigquery_205_JobStatistics5Out",
        "ListRowAccessPoliciesResponseIn": "_bigquery_206_ListRowAccessPoliciesResponseIn",
        "ListRowAccessPoliciesResponseOut": "_bigquery_207_ListRowAccessPoliciesResponseOut",
        "RowAccessPolicyReferenceIn": "_bigquery_208_RowAccessPolicyReferenceIn",
        "RowAccessPolicyReferenceOut": "_bigquery_209_RowAccessPolicyReferenceOut",
        "TableSchemaIn": "_bigquery_210_TableSchemaIn",
        "TableSchemaOut": "_bigquery_211_TableSchemaOut",
        "RoutineReferenceIn": "_bigquery_212_RoutineReferenceIn",
        "RoutineReferenceOut": "_bigquery_213_RoutineReferenceOut",
        "ListRoutinesResponseIn": "_bigquery_214_ListRoutinesResponseIn",
        "ListRoutinesResponseOut": "_bigquery_215_ListRoutinesResponseOut",
        "DataMaskingStatisticsIn": "_bigquery_216_DataMaskingStatisticsIn",
        "DataMaskingStatisticsOut": "_bigquery_217_DataMaskingStatisticsOut",
        "TransactionInfoIn": "_bigquery_218_TransactionInfoIn",
        "TransactionInfoOut": "_bigquery_219_TransactionInfoOut",
        "ModelIn": "_bigquery_220_ModelIn",
        "ModelOut": "_bigquery_221_ModelOut",
        "ProjectReferenceIn": "_bigquery_222_ProjectReferenceIn",
        "ProjectReferenceOut": "_bigquery_223_ProjectReferenceOut",
        "IntArrayHparamSearchSpaceIn": "_bigquery_224_IntArrayHparamSearchSpaceIn",
        "IntArrayHparamSearchSpaceOut": "_bigquery_225_IntArrayHparamSearchSpaceOut",
        "MultiClassClassificationMetricsIn": "_bigquery_226_MultiClassClassificationMetricsIn",
        "MultiClassClassificationMetricsOut": "_bigquery_227_MultiClassClassificationMetricsOut",
        "BigtableOptionsIn": "_bigquery_228_BigtableOptionsIn",
        "BigtableOptionsOut": "_bigquery_229_BigtableOptionsOut",
        "StandardSqlTableTypeIn": "_bigquery_230_StandardSqlTableTypeIn",
        "StandardSqlTableTypeOut": "_bigquery_231_StandardSqlTableTypeOut",
        "ArimaOrderIn": "_bigquery_232_ArimaOrderIn",
        "ArimaOrderOut": "_bigquery_233_ArimaOrderOut",
        "BiEngineStatisticsIn": "_bigquery_234_BiEngineStatisticsIn",
        "BiEngineStatisticsOut": "_bigquery_235_BiEngineStatisticsOut",
        "ConnectionPropertyIn": "_bigquery_236_ConnectionPropertyIn",
        "ConnectionPropertyOut": "_bigquery_237_ConnectionPropertyOut",
        "ExplainQueryStepIn": "_bigquery_238_ExplainQueryStepIn",
        "ExplainQueryStepOut": "_bigquery_239_ExplainQueryStepOut",
        "PolicyIn": "_bigquery_240_PolicyIn",
        "PolicyOut": "_bigquery_241_PolicyOut",
        "CsvOptionsIn": "_bigquery_242_CsvOptionsIn",
        "CsvOptionsOut": "_bigquery_243_CsvOptionsOut",
        "ArimaCoefficientsIn": "_bigquery_244_ArimaCoefficientsIn",
        "ArimaCoefficientsOut": "_bigquery_245_ArimaCoefficientsOut",
        "EvaluationMetricsIn": "_bigquery_246_EvaluationMetricsIn",
        "EvaluationMetricsOut": "_bigquery_247_EvaluationMetricsOut",
        "SparkOptionsIn": "_bigquery_248_SparkOptionsIn",
        "SparkOptionsOut": "_bigquery_249_SparkOptionsOut",
        "TableIn": "_bigquery_250_TableIn",
        "TableOut": "_bigquery_251_TableOut",
        "RemoteFunctionOptionsIn": "_bigquery_252_RemoteFunctionOptionsIn",
        "RemoteFunctionOptionsOut": "_bigquery_253_RemoteFunctionOptionsOut",
        "SparkStatisticsIn": "_bigquery_254_SparkStatisticsIn",
        "SparkStatisticsOut": "_bigquery_255_SparkStatisticsOut",
        "JsonObjectIn": "_bigquery_256_JsonObjectIn",
        "JsonObjectOut": "_bigquery_257_JsonObjectOut",
        "ClusteringIn": "_bigquery_258_ClusteringIn",
        "ClusteringOut": "_bigquery_259_ClusteringOut",
        "QueryParameterTypeIn": "_bigquery_260_QueryParameterTypeIn",
        "QueryParameterTypeOut": "_bigquery_261_QueryParameterTypeOut",
        "ScriptStackFrameIn": "_bigquery_262_ScriptStackFrameIn",
        "ScriptStackFrameOut": "_bigquery_263_ScriptStackFrameOut",
        "DoubleRangeIn": "_bigquery_264_DoubleRangeIn",
        "DoubleRangeOut": "_bigquery_265_DoubleRangeOut",
        "TableDataListIn": "_bigquery_266_TableDataListIn",
        "TableDataListOut": "_bigquery_267_TableDataListOut",
        "CategoricalValueIn": "_bigquery_268_CategoricalValueIn",
        "CategoricalValueOut": "_bigquery_269_CategoricalValueOut",
        "ListModelsResponseIn": "_bigquery_270_ListModelsResponseIn",
        "ListModelsResponseOut": "_bigquery_271_ListModelsResponseOut",
        "DoubleHparamSearchSpaceIn": "_bigquery_272_DoubleHparamSearchSpaceIn",
        "DoubleHparamSearchSpaceOut": "_bigquery_273_DoubleHparamSearchSpaceOut",
        "RangePartitioningIn": "_bigquery_274_RangePartitioningIn",
        "RangePartitioningOut": "_bigquery_275_RangePartitioningOut",
        "JobIn": "_bigquery_276_JobIn",
        "JobOut": "_bigquery_277_JobOut",
        "PrincipalComponentInfoIn": "_bigquery_278_PrincipalComponentInfoIn",
        "PrincipalComponentInfoOut": "_bigquery_279_PrincipalComponentInfoOut",
        "QueryParameterValueIn": "_bigquery_280_QueryParameterValueIn",
        "QueryParameterValueOut": "_bigquery_281_QueryParameterValueOut",
        "TableDataInsertAllResponseIn": "_bigquery_282_TableDataInsertAllResponseIn",
        "TableDataInsertAllResponseOut": "_bigquery_283_TableDataInsertAllResponseOut",
        "ArimaModelInfoIn": "_bigquery_284_ArimaModelInfoIn",
        "ArimaModelInfoOut": "_bigquery_285_ArimaModelInfoOut",
        "ConfusionMatrixIn": "_bigquery_286_ConfusionMatrixIn",
        "ConfusionMatrixOut": "_bigquery_287_ConfusionMatrixOut",
        "ErrorProtoIn": "_bigquery_288_ErrorProtoIn",
        "ErrorProtoOut": "_bigquery_289_ErrorProtoOut",
        "GoogleSheetsOptionsIn": "_bigquery_290_GoogleSheetsOptionsIn",
        "GoogleSheetsOptionsOut": "_bigquery_291_GoogleSheetsOptionsOut",
        "ClusterInfoIn": "_bigquery_292_ClusterInfoIn",
        "ClusterInfoOut": "_bigquery_293_ClusterInfoOut",
        "IntRangeIn": "_bigquery_294_IntRangeIn",
        "IntRangeOut": "_bigquery_295_IntRangeOut",
        "IndexUnusedReasonIn": "_bigquery_296_IndexUnusedReasonIn",
        "IndexUnusedReasonOut": "_bigquery_297_IndexUnusedReasonOut",
        "BindingIn": "_bigquery_298_BindingIn",
        "BindingOut": "_bigquery_299_BindingOut",
        "BigQueryModelTrainingIn": "_bigquery_300_BigQueryModelTrainingIn",
        "BigQueryModelTrainingOut": "_bigquery_301_BigQueryModelTrainingOut",
        "SetIamPolicyRequestIn": "_bigquery_302_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigquery_303_SetIamPolicyRequestOut",
        "FeatureValueIn": "_bigquery_304_FeatureValueIn",
        "FeatureValueOut": "_bigquery_305_FeatureValueOut",
        "DatasetIn": "_bigquery_306_DatasetIn",
        "DatasetOut": "_bigquery_307_DatasetOut",
        "MlStatisticsIn": "_bigquery_308_MlStatisticsIn",
        "MlStatisticsOut": "_bigquery_309_MlStatisticsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TableReferenceIn"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "projectId": t.string().optional(),
            "tableId": t.string().optional(),
        }
    ).named(renames["TableReferenceIn"])
    types["TableReferenceOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "projectId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableReferenceOut"])
    types["QueryTimelineSampleIn"] = t.struct(
        {
            "totalSlotMs": t.string().optional(),
            "estimatedRunnableUnits": t.string().optional(),
            "activeUnits": t.string().optional(),
            "completedUnits": t.string().optional(),
            "pendingUnits": t.string().optional(),
            "elapsedMs": t.string().optional(),
        }
    ).named(renames["QueryTimelineSampleIn"])
    types["QueryTimelineSampleOut"] = t.struct(
        {
            "totalSlotMs": t.string().optional(),
            "estimatedRunnableUnits": t.string().optional(),
            "activeUnits": t.string().optional(),
            "completedUnits": t.string().optional(),
            "pendingUnits": t.string().optional(),
            "elapsedMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimelineSampleOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "maxResults": t.integer().optional(),
            "queryParameters": t.array(t.proxy(renames["QueryParameterIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "useLegacySql": t.boolean().optional(),
            "useQueryCache": t.boolean().optional(),
            "maximumBytesBilled": t.string().optional(),
            "timeoutMs": t.integer().optional(),
            "continuous": t.boolean().optional(),
            "parameterMode": t.string().optional(),
            "location": t.string().optional(),
            "requestId": t.string().optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "query": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "kind": t.string().optional(),
            "createSession": t.boolean().optional(),
            "preserveNulls": t.boolean().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyIn"])
            ).optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "maxResults": t.integer().optional(),
            "queryParameters": t.array(
                t.proxy(renames["QueryParameterOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "useLegacySql": t.boolean().optional(),
            "useQueryCache": t.boolean().optional(),
            "maximumBytesBilled": t.string().optional(),
            "timeoutMs": t.integer().optional(),
            "continuous": t.boolean().optional(),
            "parameterMode": t.string().optional(),
            "location": t.string().optional(),
            "requestId": t.string().optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "query": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "kind": t.string().optional(),
            "createSession": t.boolean().optional(),
            "preserveNulls": t.boolean().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
    types["BigtableColumnIn"] = t.struct(
        {
            "type": t.string().optional(),
            "encoding": t.string().optional(),
            "qualifierString": t.string(),
            "qualifierEncoded": t.string().optional(),
            "fieldName": t.string().optional(),
            "onlyReadLatest": t.boolean().optional(),
        }
    ).named(renames["BigtableColumnIn"])
    types["BigtableColumnOut"] = t.struct(
        {
            "type": t.string().optional(),
            "encoding": t.string().optional(),
            "qualifierString": t.string(),
            "qualifierEncoded": t.string().optional(),
            "fieldName": t.string().optional(),
            "onlyReadLatest": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigtableColumnOut"])
    types["JobListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "jobs": t.array(
                t.struct(
                    {
                        "errorResult": t.proxy(renames["ErrorProtoIn"]).optional(),
                        "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                        "state": t.string().optional(),
                        "kind": t.string().optional(),
                        "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                        "status": t.proxy(renames["JobStatusIn"]).optional(),
                        "configuration": t.proxy(
                            renames["JobConfigurationIn"]
                        ).optional(),
                        "id": t.string().optional(),
                        "user_email": t.string().optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["JobListIn"])
    types["JobListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "jobs": t.array(
                t.struct(
                    {
                        "errorResult": t.proxy(renames["ErrorProtoOut"]).optional(),
                        "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
                        "state": t.string().optional(),
                        "kind": t.string().optional(),
                        "statistics": t.proxy(renames["JobStatisticsOut"]).optional(),
                        "status": t.proxy(renames["JobStatusOut"]).optional(),
                        "configuration": t.proxy(
                            renames["JobConfigurationOut"]
                        ).optional(),
                        "id": t.string().optional(),
                        "user_email": t.string().optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobListOut"])
    types["EncryptionConfigurationIn"] = t.struct(
        {"kmsKeyName": t.string().optional()}
    ).named(renames["EncryptionConfigurationIn"])
    types["EncryptionConfigurationOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigurationOut"])
    types["StreamingbufferIn"] = t.struct(
        {
            "oldestEntryTime": t.string().optional(),
            "estimatedRows": t.string().optional(),
            "estimatedBytes": t.string().optional(),
        }
    ).named(renames["StreamingbufferIn"])
    types["StreamingbufferOut"] = t.struct(
        {
            "oldestEntryTime": t.string().optional(),
            "estimatedRows": t.string().optional(),
            "estimatedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingbufferOut"])
    types["JobConfigurationQueryIn"] = t.struct(
        {
            "preserveNulls": t.boolean().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "tableDefinitions": t.struct({"_": t.string().optional()}).optional(),
            "priority": t.string().optional(),
            "createDisposition": t.string().optional(),
            "createSession": t.boolean().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
            "maximumBillingTier": t.integer().optional(),
            "clustering": t.proxy(renames["ClusteringIn"]).optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
            "query": t.string().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyIn"])
            ).optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
            "parameterMode": t.string().optional(),
            "useLegacySql": t.boolean().optional(),
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceIn"])
            ).optional(),
            "maximumBytesBilled": t.string().optional(),
            "continuous": t.boolean().optional(),
            "useQueryCache": t.boolean().optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "destinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "queryParameters": t.array(t.proxy(renames["QueryParameterIn"])).optional(),
            "allowLargeResults": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "flattenResults": t.boolean().optional(),
        }
    ).named(renames["JobConfigurationQueryIn"])
    types["JobConfigurationQueryOut"] = t.struct(
        {
            "preserveNulls": t.boolean().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "tableDefinitions": t.struct({"_": t.string().optional()}).optional(),
            "priority": t.string().optional(),
            "createDisposition": t.string().optional(),
            "createSession": t.boolean().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningOut"]).optional(),
            "maximumBillingTier": t.integer().optional(),
            "clustering": t.proxy(renames["ClusteringOut"]).optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningOut"]).optional(),
            "query": t.string().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyOut"])
            ).optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
            "parameterMode": t.string().optional(),
            "useLegacySql": t.boolean().optional(),
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceOut"])
            ).optional(),
            "maximumBytesBilled": t.string().optional(),
            "continuous": t.boolean().optional(),
            "useQueryCache": t.boolean().optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "destinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "queryParameters": t.array(
                t.proxy(renames["QueryParameterOut"])
            ).optional(),
            "allowLargeResults": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "flattenResults": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationQueryOut"])
    types["RoutineIn"] = t.struct(
        {
            "returnTableType": t.proxy(renames["StandardSqlTableTypeIn"]).optional(),
            "language": t.string().optional(),
            "returnType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
            "strictMode": t.boolean().optional(),
            "routineType": t.string(),
            "arguments": t.array(t.proxy(renames["ArgumentIn"])).optional(),
            "remoteFunctionOptions": t.proxy(
                renames["RemoteFunctionOptionsIn"]
            ).optional(),
            "importedLibraries": t.array(t.string()).optional(),
            "definitionBody": t.string(),
            "determinismLevel": t.string().optional(),
            "routineReference": t.proxy(renames["RoutineReferenceIn"]),
            "description": t.string().optional(),
            "sparkOptions": t.proxy(renames["SparkOptionsIn"]).optional(),
        }
    ).named(renames["RoutineIn"])
    types["RoutineOut"] = t.struct(
        {
            "returnTableType": t.proxy(renames["StandardSqlTableTypeOut"]).optional(),
            "language": t.string().optional(),
            "creationTime": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "returnType": t.proxy(renames["StandardSqlDataTypeOut"]).optional(),
            "strictMode": t.boolean().optional(),
            "routineType": t.string(),
            "arguments": t.array(t.proxy(renames["ArgumentOut"])).optional(),
            "etag": t.string().optional(),
            "remoteFunctionOptions": t.proxy(
                renames["RemoteFunctionOptionsOut"]
            ).optional(),
            "importedLibraries": t.array(t.string()).optional(),
            "definitionBody": t.string(),
            "determinismLevel": t.string().optional(),
            "routineReference": t.proxy(renames["RoutineReferenceOut"]),
            "description": t.string().optional(),
            "sparkOptions": t.proxy(renames["SparkOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutineOut"])
    types["SessionInfoIn"] = t.struct({"sessionId": t.string().optional()}).named(
        renames["SessionInfoIn"]
    )
    types["SessionInfoOut"] = t.struct(
        {
            "sessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionInfoOut"])
    types["JsonOptionsIn"] = t.struct({"encoding": t.string().optional()}).named(
        renames["JsonOptionsIn"]
    )
    types["JsonOptionsOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JsonOptionsOut"])
    types["AvroOptionsIn"] = t.struct(
        {"useAvroLogicalTypes": t.boolean().optional()}
    ).named(renames["AvroOptionsIn"])
    types["AvroOptionsOut"] = t.struct(
        {
            "useAvroLogicalTypes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvroOptionsOut"])
    types["TableListIn"] = t.struct(
        {
            "tables": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "timePartitioning": t.proxy(
                            renames["TimePartitioningIn"]
                        ).optional(),
                        "kind": t.string().optional(),
                        "type": t.string().optional(),
                        "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                        "rangePartitioning": t.proxy(
                            renames["RangePartitioningIn"]
                        ).optional(),
                        "expirationTime": t.string().optional(),
                        "view": t.struct(
                            {"useLegacySql": t.boolean().optional()}
                        ).optional(),
                        "friendlyName": t.string().optional(),
                        "creationTime": t.string().optional(),
                        "tableReference": t.proxy(
                            renames["TableReferenceIn"]
                        ).optional(),
                    }
                )
            ).optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["TableListIn"])
    types["TableListOut"] = t.struct(
        {
            "tables": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "timePartitioning": t.proxy(
                            renames["TimePartitioningOut"]
                        ).optional(),
                        "kind": t.string().optional(),
                        "type": t.string().optional(),
                        "clustering": t.proxy(renames["ClusteringOut"]).optional(),
                        "rangePartitioning": t.proxy(
                            renames["RangePartitioningOut"]
                        ).optional(),
                        "expirationTime": t.string().optional(),
                        "view": t.struct(
                            {"useLegacySql": t.boolean().optional()}
                        ).optional(),
                        "friendlyName": t.string().optional(),
                        "creationTime": t.string().optional(),
                        "tableReference": t.proxy(
                            renames["TableReferenceOut"]
                        ).optional(),
                    }
                )
            ).optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableListOut"])
    types["RegressionMetricsIn"] = t.struct(
        {
            "meanSquaredError": t.number().optional(),
            "rSquared": t.number().optional(),
            "meanAbsoluteError": t.number().optional(),
            "medianAbsoluteError": t.number().optional(),
            "meanSquaredLogError": t.number().optional(),
        }
    ).named(renames["RegressionMetricsIn"])
    types["RegressionMetricsOut"] = t.struct(
        {
            "meanSquaredError": t.number().optional(),
            "rSquared": t.number().optional(),
            "meanAbsoluteError": t.number().optional(),
            "medianAbsoluteError": t.number().optional(),
            "meanSquaredLogError": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegressionMetricsOut"])
    types["SparkLoggingInfoIn"] = t.struct(
        {"resource_type": t.string().optional(), "project_id": t.string().optional()}
    ).named(renames["SparkLoggingInfoIn"])
    types["SparkLoggingInfoOut"] = t.struct(
        {
            "resource_type": t.string().optional(),
            "project_id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkLoggingInfoOut"])
    types["ExternalDataConfigurationIn"] = t.struct(
        {
            "csvOptions": t.proxy(renames["CsvOptionsIn"]).optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "googleSheetsOptions": t.proxy(renames["GoogleSheetsOptionsIn"]).optional(),
            "fileSetSpecType": t.string().optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsIn"]
            ).optional(),
            "avroOptions": t.proxy(renames["AvroOptionsIn"]).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "maxBadRecords": t.integer().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsIn"]).optional(),
            "compression": t.string().optional(),
            "sourceUris": t.array(t.string()).optional(),
            "autodetect": t.boolean().optional(),
            "bigtableOptions": t.proxy(renames["BigtableOptionsIn"]).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "sourceFormat": t.string().optional(),
            "connectionId": t.string().optional(),
            "metadataCacheMode": t.string().optional(),
            "objectMetadata": t.string().optional(),
            "jsonOptions": t.proxy(renames["JsonOptionsIn"]).optional(),
        }
    ).named(renames["ExternalDataConfigurationIn"])
    types["ExternalDataConfigurationOut"] = t.struct(
        {
            "csvOptions": t.proxy(renames["CsvOptionsOut"]).optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "googleSheetsOptions": t.proxy(
                renames["GoogleSheetsOptionsOut"]
            ).optional(),
            "fileSetSpecType": t.string().optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsOut"]
            ).optional(),
            "avroOptions": t.proxy(renames["AvroOptionsOut"]).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "maxBadRecords": t.integer().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsOut"]).optional(),
            "compression": t.string().optional(),
            "sourceUris": t.array(t.string()).optional(),
            "autodetect": t.boolean().optional(),
            "bigtableOptions": t.proxy(renames["BigtableOptionsOut"]).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "sourceFormat": t.string().optional(),
            "connectionId": t.string().optional(),
            "metadataCacheMode": t.string().optional(),
            "objectMetadata": t.string().optional(),
            "jsonOptions": t.proxy(renames["JsonOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalDataConfigurationOut"])
    types["IterationResultIn"] = t.struct(
        {
            "trainingLoss": t.number().optional(),
            "durationMs": t.string().optional(),
            "index": t.integer().optional(),
            "evalLoss": t.number().optional(),
            "learnRate": t.number().optional(),
        }
    ).named(renames["IterationResultIn"])
    types["IterationResultOut"] = t.struct(
        {
            "trainingLoss": t.number().optional(),
            "durationMs": t.string().optional(),
            "index": t.integer().optional(),
            "evalLoss": t.number().optional(),
            "learnRate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IterationResultOut"])
    types["RowLevelSecurityStatisticsIn"] = t.struct(
        {"rowLevelSecurityApplied": t.boolean().optional()}
    ).named(renames["RowLevelSecurityStatisticsIn"])
    types["RowLevelSecurityStatisticsOut"] = t.struct(
        {
            "rowLevelSecurityApplied": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowLevelSecurityStatisticsOut"])
    types["DmlStatisticsIn"] = t.struct(
        {
            "insertedRowCount": t.string().optional(),
            "updatedRowCount": t.string().optional(),
            "deletedRowCount": t.string().optional(),
        }
    ).named(renames["DmlStatisticsIn"])
    types["DmlStatisticsOut"] = t.struct(
        {
            "insertedRowCount": t.string().optional(),
            "updatedRowCount": t.string().optional(),
            "deletedRowCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DmlStatisticsOut"])
    types["ArimaResultIn"] = t.struct(
        {
            "seasonalPeriods": t.array(t.string()).optional(),
            "arimaModelInfo": t.array(t.proxy(renames["ArimaModelInfoIn"])).optional(),
        }
    ).named(renames["ArimaResultIn"])
    types["ArimaResultOut"] = t.struct(
        {
            "seasonalPeriods": t.array(t.string()).optional(),
            "arimaModelInfo": t.array(t.proxy(renames["ArimaModelInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaResultOut"])
    types["BiEngineReasonIn"] = t.struct(
        {"message": t.string().optional(), "code": t.string().optional()}
    ).named(renames["BiEngineReasonIn"])
    types["BiEngineReasonOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiEngineReasonOut"])
    types["LocationMetadataIn"] = t.struct(
        {"legacyLocationId": t.string().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "legacyLocationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
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
    types["DataSplitResultIn"] = t.struct(
        {
            "trainingTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "testTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "evaluationTable": t.proxy(renames["TableReferenceIn"]).optional(),
        }
    ).named(renames["DataSplitResultIn"])
    types["DataSplitResultOut"] = t.struct(
        {
            "trainingTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "testTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "evaluationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSplitResultOut"])
    types["AggregateClassificationMetricsIn"] = t.struct(
        {
            "precision": t.number().optional(),
            "accuracy": t.number().optional(),
            "recall": t.number().optional(),
            "rocAuc": t.number().optional(),
            "threshold": t.number().optional(),
            "f1Score": t.number().optional(),
            "logLoss": t.number().optional(),
        }
    ).named(renames["AggregateClassificationMetricsIn"])
    types["AggregateClassificationMetricsOut"] = t.struct(
        {
            "precision": t.number().optional(),
            "accuracy": t.number().optional(),
            "recall": t.number().optional(),
            "rocAuc": t.number().optional(),
            "threshold": t.number().optional(),
            "f1Score": t.number().optional(),
            "logLoss": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateClassificationMetricsOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["JobReferenceIn"] = t.struct(
        {
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "jobId": t.string().optional(),
        }
    ).named(renames["JobReferenceIn"])
    types["JobReferenceOut"] = t.struct(
        {
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "jobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobReferenceOut"])
    types["CloneDefinitionIn"] = t.struct(
        {
            "cloneTime": t.string().optional(),
            "baseTableReference": t.proxy(renames["TableReferenceIn"]).optional(),
        }
    ).named(renames["CloneDefinitionIn"])
    types["CloneDefinitionOut"] = t.struct(
        {
            "cloneTime": t.string().optional(),
            "baseTableReference": t.proxy(renames["TableReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneDefinitionOut"])
    types["BinaryConfusionMatrixIn"] = t.struct(
        {
            "truePositives": t.string().optional(),
            "falseNegatives": t.string().optional(),
            "f1Score": t.number().optional(),
            "accuracy": t.number().optional(),
            "recall": t.number().optional(),
            "positiveClassThreshold": t.number().optional(),
            "precision": t.number().optional(),
            "trueNegatives": t.string().optional(),
            "falsePositives": t.string().optional(),
        }
    ).named(renames["BinaryConfusionMatrixIn"])
    types["BinaryConfusionMatrixOut"] = t.struct(
        {
            "truePositives": t.string().optional(),
            "falseNegatives": t.string().optional(),
            "f1Score": t.number().optional(),
            "accuracy": t.number().optional(),
            "recall": t.number().optional(),
            "positiveClassThreshold": t.number().optional(),
            "precision": t.number().optional(),
            "trueNegatives": t.string().optional(),
            "falsePositives": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinaryConfusionMatrixOut"])
    types["QueryResponseIn"] = t.struct(
        {
            "sessionInfo": t.proxy(renames["SessionInfoIn"]).optional(),
            "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "jobComplete": t.boolean().optional(),
            "totalBytesProcessed": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsIn"]).optional(),
            "totalRows": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "pageToken": t.string().optional(),
            "kind": t.string().optional(),
            "numDmlAffectedRows": t.string().optional(),
            "cacheHit": t.boolean().optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "sessionInfo": t.proxy(renames["SessionInfoOut"]).optional(),
            "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
            "jobComplete": t.boolean().optional(),
            "totalBytesProcessed": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsOut"]).optional(),
            "totalRows": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "pageToken": t.string().optional(),
            "kind": t.string().optional(),
            "numDmlAffectedRows": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["DimensionalityReductionMetricsIn"] = t.struct(
        {"totalExplainedVarianceRatio": t.number().optional()}
    ).named(renames["DimensionalityReductionMetricsIn"])
    types["DimensionalityReductionMetricsOut"] = t.struct(
        {
            "totalExplainedVarianceRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionalityReductionMetricsOut"])
    types["ArgumentIn"] = t.struct(
        {
            "argumentKind": t.string().optional(),
            "mode": t.string().optional(),
            "dataType": t.proxy(renames["StandardSqlDataTypeIn"]),
            "name": t.string().optional(),
        }
    ).named(renames["ArgumentIn"])
    types["ArgumentOut"] = t.struct(
        {
            "argumentKind": t.string().optional(),
            "mode": t.string().optional(),
            "dataType": t.proxy(renames["StandardSqlDataTypeOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArgumentOut"])
    types["DestinationTablePropertiesIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expirationTime": t.string().optional(),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DestinationTablePropertiesIn"])
    types["DestinationTablePropertiesOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expirationTime": t.string().optional(),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationTablePropertiesOut"])
    types["ParquetOptionsIn"] = t.struct(
        {
            "enumAsString": t.boolean().optional(),
            "enableListInference": t.boolean().optional(),
        }
    ).named(renames["ParquetOptionsIn"])
    types["ParquetOptionsOut"] = t.struct(
        {
            "enumAsString": t.boolean().optional(),
            "enableListInference": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParquetOptionsOut"])
    types["DatasetListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "datasets": t.array(
                t.struct(
                    {
                        "friendlyName": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "datasetReference": t.proxy(
                            renames["DatasetReferenceIn"]
                        ).optional(),
                        "location": t.string().optional(),
                        "kind": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["DatasetListIn"])
    types["DatasetListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "datasets": t.array(
                t.struct(
                    {
                        "friendlyName": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "datasetReference": t.proxy(
                            renames["DatasetReferenceOut"]
                        ).optional(),
                        "location": t.string().optional(),
                        "kind": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetListOut"])
    types["GlobalExplanationIn"] = t.struct(
        {
            "explanations": t.array(t.proxy(renames["ExplanationIn"])).optional(),
            "classLabel": t.string().optional(),
        }
    ).named(renames["GlobalExplanationIn"])
    types["GlobalExplanationOut"] = t.struct(
        {
            "explanations": t.array(t.proxy(renames["ExplanationOut"])).optional(),
            "classLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlobalExplanationOut"])
    types["DatasetAccessEntryIn"] = t.struct(
        {
            "dataset": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "targetTypes": t.array(t.string()),
        }
    ).named(renames["DatasetAccessEntryIn"])
    types["DatasetAccessEntryOut"] = t.struct(
        {
            "dataset": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "targetTypes": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetAccessEntryOut"])
    types["IntArrayIn"] = t.struct({"elements": t.array(t.string()).optional()}).named(
        renames["IntArrayIn"]
    )
    types["IntArrayOut"] = t.struct(
        {
            "elements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntArrayOut"])
    types["BqmlIterationResultIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "durationMs": t.string().optional(),
            "evalLoss": t.number().optional(),
            "learnRate": t.number().optional(),
            "trainingLoss": t.number().optional(),
        }
    ).named(renames["BqmlIterationResultIn"])
    types["BqmlIterationResultOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "durationMs": t.string().optional(),
            "evalLoss": t.number().optional(),
            "learnRate": t.number().optional(),
            "trainingLoss": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BqmlIterationResultOut"])
    types["TrainingOptionsIn"] = t.struct(
        {
            "approxGlobalFeatureContrib": t.boolean().optional(),
            "labelClassWeights": t.struct({"_": t.string().optional()}).optional(),
            "colsampleBynode": t.number().optional(),
            "numParallelTree": t.string().optional(),
            "walsAlpha": t.number().optional(),
            "numTrials": t.string().optional(),
            "itemColumn": t.string().optional(),
            "batchSize": t.string().optional(),
            "distanceType": t.string().optional(),
            "lossType": t.string().optional(),
            "numClusters": t.string().optional(),
            "warmStart": t.boolean().optional(),
            "feedbackType": t.string().optional(),
            "dataFrequency": t.string().optional(),
            "adjustStepChanges": t.boolean().optional(),
            "dataSplitColumn": t.string().optional(),
            "colorSpace": t.string().optional(),
            "tfVersion": t.string().optional(),
            "dataSplitEvalFraction": t.number().optional(),
            "holidayRegion": t.string().optional(),
            "learnRate": t.number().optional(),
            "userColumn": t.string().optional(),
            "autoArima": t.boolean().optional(),
            "xgboostVersion": t.string().optional(),
            "maxTimeSeriesLength": t.string().optional(),
            "subsample": t.number().optional(),
            "kmeansInitializationMethod": t.string().optional(),
            "includeDrift": t.boolean().optional(),
            "numFactors": t.string().optional(),
            "dartNormalizeType": t.string().optional(),
            "dataSplitMethod": t.string().optional(),
            "hparamTuningObjectives": t.array(t.string()).optional(),
            "inputLabelColumns": t.array(t.string()).optional(),
            "learnRateStrategy": t.string().optional(),
            "sampledShapleyNumPaths": t.string().optional(),
            "optimizationStrategy": t.string().optional(),
            "timeSeriesLengthFraction": t.number().optional(),
            "maxParallelTrials": t.string().optional(),
            "dropout": t.number().optional(),
            "timeSeriesIdColumns": t.array(t.string()).optional(),
            "timeSeriesTimestampColumn": t.string().optional(),
            "cleanSpikesAndDips": t.boolean().optional(),
            "instanceWeightColumn": t.string().optional(),
            "maxTreeDepth": t.string().optional(),
            "l2Regularization": t.number().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderIn"]).optional(),
            "enableGlobalExplain": t.boolean().optional(),
            "minRelativeProgress": t.number().optional(),
            "treeMethod": t.string().optional(),
            "minSplitLoss": t.number().optional(),
            "horizon": t.string().optional(),
            "calculatePValues": t.boolean().optional(),
            "timeSeriesIdColumn": t.string().optional(),
            "colsampleBytree": t.number().optional(),
            "minTreeChildWeight": t.string().optional(),
            "integratedGradientsNumSteps": t.string().optional(),
            "l1Regularization": t.number().optional(),
            "maxIterations": t.string().optional(),
            "autoArimaMaxOrder": t.string().optional(),
            "trendSmoothingWindowSize": t.string().optional(),
            "kmeansInitializationColumn": t.string().optional(),
            "decomposeTimeSeries": t.boolean().optional(),
            "initialLearnRate": t.number().optional(),
            "timeSeriesDataColumn": t.string().optional(),
            "boosterType": t.string().optional(),
            "modelUri": t.string().optional(),
            "earlyStop": t.boolean().optional(),
            "autoArimaMinOrder": t.string().optional(),
            "colsampleBylevel": t.number().optional(),
            "hiddenUnits": t.array(t.string()).optional(),
            "minTimeSeriesLength": t.string().optional(),
        }
    ).named(renames["TrainingOptionsIn"])
    types["TrainingOptionsOut"] = t.struct(
        {
            "approxGlobalFeatureContrib": t.boolean().optional(),
            "labelClassWeights": t.struct({"_": t.string().optional()}).optional(),
            "colsampleBynode": t.number().optional(),
            "numParallelTree": t.string().optional(),
            "walsAlpha": t.number().optional(),
            "numTrials": t.string().optional(),
            "itemColumn": t.string().optional(),
            "batchSize": t.string().optional(),
            "distanceType": t.string().optional(),
            "lossType": t.string().optional(),
            "numClusters": t.string().optional(),
            "warmStart": t.boolean().optional(),
            "feedbackType": t.string().optional(),
            "dataFrequency": t.string().optional(),
            "adjustStepChanges": t.boolean().optional(),
            "dataSplitColumn": t.string().optional(),
            "colorSpace": t.string().optional(),
            "tfVersion": t.string().optional(),
            "dataSplitEvalFraction": t.number().optional(),
            "holidayRegion": t.string().optional(),
            "learnRate": t.number().optional(),
            "userColumn": t.string().optional(),
            "autoArima": t.boolean().optional(),
            "xgboostVersion": t.string().optional(),
            "maxTimeSeriesLength": t.string().optional(),
            "subsample": t.number().optional(),
            "kmeansInitializationMethod": t.string().optional(),
            "includeDrift": t.boolean().optional(),
            "numFactors": t.string().optional(),
            "dartNormalizeType": t.string().optional(),
            "dataSplitMethod": t.string().optional(),
            "hparamTuningObjectives": t.array(t.string()).optional(),
            "inputLabelColumns": t.array(t.string()).optional(),
            "learnRateStrategy": t.string().optional(),
            "sampledShapleyNumPaths": t.string().optional(),
            "optimizationStrategy": t.string().optional(),
            "timeSeriesLengthFraction": t.number().optional(),
            "maxParallelTrials": t.string().optional(),
            "dropout": t.number().optional(),
            "timeSeriesIdColumns": t.array(t.string()).optional(),
            "timeSeriesTimestampColumn": t.string().optional(),
            "cleanSpikesAndDips": t.boolean().optional(),
            "instanceWeightColumn": t.string().optional(),
            "maxTreeDepth": t.string().optional(),
            "l2Regularization": t.number().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderOut"]).optional(),
            "enableGlobalExplain": t.boolean().optional(),
            "minRelativeProgress": t.number().optional(),
            "treeMethod": t.string().optional(),
            "minSplitLoss": t.number().optional(),
            "horizon": t.string().optional(),
            "calculatePValues": t.boolean().optional(),
            "timeSeriesIdColumn": t.string().optional(),
            "colsampleBytree": t.number().optional(),
            "minTreeChildWeight": t.string().optional(),
            "integratedGradientsNumSteps": t.string().optional(),
            "l1Regularization": t.number().optional(),
            "maxIterations": t.string().optional(),
            "autoArimaMaxOrder": t.string().optional(),
            "trendSmoothingWindowSize": t.string().optional(),
            "kmeansInitializationColumn": t.string().optional(),
            "decomposeTimeSeries": t.boolean().optional(),
            "initialLearnRate": t.number().optional(),
            "timeSeriesDataColumn": t.string().optional(),
            "boosterType": t.string().optional(),
            "modelUri": t.string().optional(),
            "earlyStop": t.boolean().optional(),
            "autoArimaMinOrder": t.string().optional(),
            "colsampleBylevel": t.number().optional(),
            "hiddenUnits": t.array(t.string()).optional(),
            "minTimeSeriesLength": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrainingOptionsOut"])
    types["RowIn"] = t.struct(
        {
            "actualLabel": t.string().optional(),
            "entries": t.array(t.proxy(renames["EntryIn"])).optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "actualLabel": t.string().optional(),
            "entries": t.array(t.proxy(renames["EntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["JobCancelResponseIn"] = t.struct(
        {"kind": t.string().optional(), "job": t.proxy(renames["JobIn"]).optional()}
    ).named(renames["JobCancelResponseIn"])
    types["JobCancelResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "job": t.proxy(renames["JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobCancelResponseOut"])
    types["TimePartitioningIn"] = t.struct(
        {
            "field": t.string().optional(),
            "expirationMs": t.string().optional(),
            "type": t.string().optional(),
            "requirePartitionFilter": t.boolean(),
        }
    ).named(renames["TimePartitioningIn"])
    types["TimePartitioningOut"] = t.struct(
        {
            "field": t.string().optional(),
            "expirationMs": t.string().optional(),
            "type": t.string().optional(),
            "requirePartitionFilter": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePartitioningOut"])
    types["HparamTuningTrialIn"] = t.struct(
        {
            "trialId": t.string().optional(),
            "endTimeMs": t.string().optional(),
            "startTimeMs": t.string().optional(),
            "errorMessage": t.string().optional(),
            "evaluationMetrics": t.proxy(renames["EvaluationMetricsIn"]).optional(),
            "hparams": t.proxy(renames["TrainingOptionsIn"]).optional(),
            "trainingLoss": t.number().optional(),
            "status": t.string().optional(),
            "hparamTuningEvaluationMetrics": t.proxy(
                renames["EvaluationMetricsIn"]
            ).optional(),
            "evalLoss": t.number().optional(),
        }
    ).named(renames["HparamTuningTrialIn"])
    types["HparamTuningTrialOut"] = t.struct(
        {
            "trialId": t.string().optional(),
            "endTimeMs": t.string().optional(),
            "startTimeMs": t.string().optional(),
            "errorMessage": t.string().optional(),
            "evaluationMetrics": t.proxy(renames["EvaluationMetricsOut"]).optional(),
            "hparams": t.proxy(renames["TrainingOptionsOut"]).optional(),
            "trainingLoss": t.number().optional(),
            "status": t.string().optional(),
            "hparamTuningEvaluationMetrics": t.proxy(
                renames["EvaluationMetricsOut"]
            ).optional(),
            "evalLoss": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HparamTuningTrialOut"])
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
    types["StandardSqlFieldIn"] = t.struct(
        {
            "type": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["StandardSqlFieldIn"])
    types["StandardSqlFieldOut"] = t.struct(
        {
            "type": t.proxy(renames["StandardSqlDataTypeOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlFieldOut"])
    types["DatasetReferenceIn"] = t.struct(
        {"datasetId": t.string().optional(), "projectId": t.string().optional()}
    ).named(renames["DatasetReferenceIn"])
    types["DatasetReferenceOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetReferenceOut"])
    types["ArimaSingleModelForecastingMetricsIn"] = t.struct(
        {
            "seasonalPeriods": t.array(t.string()).optional(),
            "hasSpikesAndDips": t.boolean().optional(),
            "timeSeriesIds": t.array(t.string()).optional(),
            "hasStepChanges": t.boolean().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderIn"]).optional(),
            "arimaFittingMetrics": t.proxy(renames["ArimaFittingMetricsIn"]).optional(),
            "hasDrift": t.boolean().optional(),
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesId": t.string().optional(),
        }
    ).named(renames["ArimaSingleModelForecastingMetricsIn"])
    types["ArimaSingleModelForecastingMetricsOut"] = t.struct(
        {
            "seasonalPeriods": t.array(t.string()).optional(),
            "hasSpikesAndDips": t.boolean().optional(),
            "timeSeriesIds": t.array(t.string()).optional(),
            "hasStepChanges": t.boolean().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderOut"]).optional(),
            "arimaFittingMetrics": t.proxy(
                renames["ArimaFittingMetricsOut"]
            ).optional(),
            "hasDrift": t.boolean().optional(),
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaSingleModelForecastingMetricsOut"])
    types["ClusterIn"] = t.struct(
        {
            "featureValues": t.array(t.proxy(renames["FeatureValueIn"])).optional(),
            "count": t.string().optional(),
            "centroidId": t.string().optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "featureValues": t.array(t.proxy(renames["FeatureValueOut"])).optional(),
            "count": t.string().optional(),
            "centroidId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["ClusteringMetricsIn"] = t.struct(
        {
            "daviesBouldinIndex": t.number().optional(),
            "clusters": t.array(t.proxy(renames["ClusterIn"])).optional(),
            "meanSquaredDistance": t.number().optional(),
        }
    ).named(renames["ClusteringMetricsIn"])
    types["ClusteringMetricsOut"] = t.struct(
        {
            "daviesBouldinIndex": t.number().optional(),
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "meanSquaredDistance": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusteringMetricsOut"])
    types["RemoteModelInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoteModelInfoIn"]
    )
    types["RemoteModelInfoOut"] = t.struct(
        {
            "connection": t.string().optional(),
            "maxBatchingRows": t.string().optional(),
            "endpoint": t.string().optional(),
            "remoteServiceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteModelInfoOut"])
    types["HivePartitioningOptionsIn"] = t.struct(
        {
            "requirePartitionFilter": t.boolean().optional(),
            "mode": t.string().optional(),
            "sourceUriPrefix": t.string().optional(),
            "fields": t.array(t.string()).optional(),
        }
    ).named(renames["HivePartitioningOptionsIn"])
    types["HivePartitioningOptionsOut"] = t.struct(
        {
            "requirePartitionFilter": t.boolean().optional(),
            "mode": t.string().optional(),
            "sourceUriPrefix": t.string().optional(),
            "fields": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HivePartitioningOptionsOut"])
    types["ExplanationIn"] = t.struct(
        {"attribution": t.number().optional(), "featureName": t.string().optional()}
    ).named(renames["ExplanationIn"])
    types["ExplanationOut"] = t.struct(
        {
            "attribution": t.number().optional(),
            "featureName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplanationOut"])
    types["JobStatistics3In"] = t.struct(
        {
            "inputFiles": t.string().optional(),
            "badRecords": t.string().optional(),
            "outputRows": t.string().optional(),
            "outputBytes": t.string().optional(),
            "inputFileBytes": t.string().optional(),
        }
    ).named(renames["JobStatistics3In"])
    types["JobStatistics3Out"] = t.struct(
        {
            "inputFiles": t.string().optional(),
            "badRecords": t.string().optional(),
            "outputRows": t.string().optional(),
            "outputBytes": t.string().optional(),
            "inputFileBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatistics3Out"])
    types["SearchStatisticsIn"] = t.struct(
        {
            "indexUnusedReason": t.array(
                t.proxy(renames["IndexUnusedReasonIn"])
            ).optional(),
            "indexUsageMode": t.string().optional(),
        }
    ).named(renames["SearchStatisticsIn"])
    types["SearchStatisticsOut"] = t.struct(
        {
            "indexUnusedReason": t.array(
                t.proxy(renames["IndexUnusedReasonOut"])
            ).optional(),
            "indexUsageMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchStatisticsOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ProjectListIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "projects": t.array(
                t.struct(
                    {
                        "numericId": t.string().optional(),
                        "projectReference": t.proxy(
                            renames["ProjectReferenceIn"]
                        ).optional(),
                        "kind": t.string().optional(),
                        "friendlyName": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["ProjectListIn"])
    types["ProjectListOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "projects": t.array(
                t.struct(
                    {
                        "numericId": t.string().optional(),
                        "projectReference": t.proxy(
                            renames["ProjectReferenceOut"]
                        ).optional(),
                        "kind": t.string().optional(),
                        "friendlyName": t.string().optional(),
                        "id": t.string().optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectListOut"])
    types["JobConfigurationTableCopyIn"] = t.struct(
        {
            "sourceTables": t.array(t.proxy(renames["TableReferenceIn"])).optional(),
            "destinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "destinationExpirationTime": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "writeDisposition": t.string().optional(),
            "createDisposition": t.string().optional(),
            "sourceTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "operationType": t.string().optional(),
        }
    ).named(renames["JobConfigurationTableCopyIn"])
    types["JobConfigurationTableCopyOut"] = t.struct(
        {
            "sourceTables": t.array(t.proxy(renames["TableReferenceOut"])).optional(),
            "destinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "destinationExpirationTime": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "writeDisposition": t.string().optional(),
            "createDisposition": t.string().optional(),
            "sourceTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationTableCopyOut"])
    types["StandardSqlStructTypeIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["StandardSqlFieldIn"]))}
    ).named(renames["StandardSqlStructTypeIn"])
    types["StandardSqlStructTypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["StandardSqlFieldOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlStructTypeOut"])
    types["TableCellIn"] = t.struct(
        {"v": t.struct({"_": t.string().optional()})}
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "v": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["TableRowIn"] = t.struct(
        {"f": t.array(t.proxy(renames["TableCellIn"])).optional()}
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "f": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["ViewDefinitionIn"] = t.struct(
        {
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceIn"])
            ).optional(),
            "useExplicitColumnNames": t.boolean().optional(),
            "useLegacySql": t.boolean().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["ViewDefinitionIn"])
    types["ViewDefinitionOut"] = t.struct(
        {
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceOut"])
            ).optional(),
            "useExplicitColumnNames": t.boolean().optional(),
            "useLegacySql": t.boolean().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewDefinitionOut"])
    types["BinaryClassificationMetricsIn"] = t.struct(
        {
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsIn"]
            ).optional(),
            "positiveLabel": t.string().optional(),
            "binaryConfusionMatrixList": t.array(
                t.proxy(renames["BinaryConfusionMatrixIn"])
            ).optional(),
            "negativeLabel": t.string().optional(),
        }
    ).named(renames["BinaryClassificationMetricsIn"])
    types["BinaryClassificationMetricsOut"] = t.struct(
        {
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsOut"]
            ).optional(),
            "positiveLabel": t.string().optional(),
            "binaryConfusionMatrixList": t.array(
                t.proxy(renames["BinaryConfusionMatrixOut"])
            ).optional(),
            "negativeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinaryClassificationMetricsOut"])
    types["JobConfigurationIn"] = t.struct(
        {
            "query": t.proxy(renames["JobConfigurationQueryIn"]).optional(),
            "extract": t.proxy(renames["JobConfigurationExtractIn"]).optional(),
            "load": t.proxy(renames["JobConfigurationLoadIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "copy": t.proxy(renames["JobConfigurationTableCopyIn"]).optional(),
            "jobType": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "jobTimeoutMs": t.string().optional(),
        }
    ).named(renames["JobConfigurationIn"])
    types["JobConfigurationOut"] = t.struct(
        {
            "query": t.proxy(renames["JobConfigurationQueryOut"]).optional(),
            "extract": t.proxy(renames["JobConfigurationExtractOut"]).optional(),
            "load": t.proxy(renames["JobConfigurationLoadOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "copy": t.proxy(renames["JobConfigurationTableCopyOut"]).optional(),
            "jobType": t.string().optional(),
            "dryRun": t.boolean().optional(),
            "jobTimeoutMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationOut"])
    types["RowAccessPolicyIn"] = t.struct(
        {
            "filterPredicate": t.string(),
            "rowAccessPolicyReference": t.proxy(renames["RowAccessPolicyReferenceIn"]),
        }
    ).named(renames["RowAccessPolicyIn"])
    types["RowAccessPolicyOut"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "filterPredicate": t.string(),
            "lastModifiedTime": t.string().optional(),
            "rowAccessPolicyReference": t.proxy(renames["RowAccessPolicyReferenceOut"]),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowAccessPolicyOut"])
    types["RankingMetricsIn"] = t.struct(
        {
            "meanSquaredError": t.number().optional(),
            "meanAveragePrecision": t.number().optional(),
            "averageRank": t.number().optional(),
            "normalizedDiscountedCumulativeGain": t.number().optional(),
        }
    ).named(renames["RankingMetricsIn"])
    types["RankingMetricsOut"] = t.struct(
        {
            "meanSquaredError": t.number().optional(),
            "meanAveragePrecision": t.number().optional(),
            "averageRank": t.number().optional(),
            "normalizedDiscountedCumulativeGain": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RankingMetricsOut"])
    types["JobStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "errorResult": t.proxy(renames["ErrorProtoIn"]).optional(),
        }
    ).named(renames["JobStatusIn"])
    types["JobStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
            "errorResult": t.proxy(renames["ErrorProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
    types["CategoryCountIn"] = t.struct(
        {"category": t.string().optional(), "count": t.string().optional()}
    ).named(renames["CategoryCountIn"])
    types["CategoryCountOut"] = t.struct(
        {
            "category": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryCountOut"])
    types["ScriptStatisticsIn"] = t.struct(
        {
            "evaluationKind": t.string().optional(),
            "stackFrames": t.array(t.proxy(renames["ScriptStackFrameIn"])).optional(),
        }
    ).named(renames["ScriptStatisticsIn"])
    types["ScriptStatisticsOut"] = t.struct(
        {
            "evaluationKind": t.string().optional(),
            "stackFrames": t.array(t.proxy(renames["ScriptStackFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptStatisticsOut"])
    types["StandardSqlDataTypeIn"] = t.struct(
        {
            "typeKind": t.string(),
            "arrayElementType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
            "structType": t.proxy(renames["StandardSqlStructTypeIn"]).optional(),
        }
    ).named(renames["StandardSqlDataTypeIn"])
    types["StandardSqlDataTypeOut"] = t.struct(
        {
            "typeKind": t.string(),
            "arrayElementType": t.proxy(renames["StandardSqlDataTypeOut"]).optional(),
            "structType": t.proxy(renames["StandardSqlStructTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlDataTypeOut"])
    types["UserDefinedFunctionResourceIn"] = t.struct(
        {"inlineCode": t.string().optional(), "resourceUri": t.string().optional()}
    ).named(renames["UserDefinedFunctionResourceIn"])
    types["UserDefinedFunctionResourceOut"] = t.struct(
        {
            "inlineCode": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedFunctionResourceOut"])
    types["JobStatistics4In"] = t.struct(
        {
            "destinationUriFileCounts": t.array(t.string()).optional(),
            "inputBytes": t.string().optional(),
        }
    ).named(renames["JobStatistics4In"])
    types["JobStatistics4Out"] = t.struct(
        {
            "destinationUriFileCounts": t.array(t.string()).optional(),
            "inputBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatistics4Out"])
    types["JobStatisticsIn"] = t.struct(
        {
            "load": t.proxy(renames["JobStatistics3In"]).optional(),
            "query": t.proxy(renames["JobStatistics2In"]).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"name": t.string().optional(), "slotMs": t.string().optional()}
                )
            ).optional(),
            "numChildJobs": t.string().optional(),
            "creationTime": t.string().optional(),
            "scriptStatistics": t.proxy(renames["ScriptStatisticsIn"]).optional(),
            "quotaDeferments": t.array(t.string()).optional(),
            "sessionInfo": t.proxy(renames["SessionInfoIn"]).optional(),
            "copy": t.proxy(renames["JobStatistics5In"]).optional(),
            "reservation_id": t.string().optional(),
            "startTime": t.string().optional(),
            "parentJobId": t.string().optional(),
            "endTime": t.string().optional(),
            "transactionInfo": t.proxy(renames["TransactionInfoIn"]).optional(),
            "totalSlotMs": t.string().optional(),
            "rowLevelSecurityStatistics": t.proxy(
                renames["RowLevelSecurityStatisticsIn"]
            ).optional(),
            "extract": t.proxy(renames["JobStatistics4In"]).optional(),
            "completionRatio": t.number().optional(),
            "totalBytesProcessed": t.string().optional(),
            "dataMaskingStatistics": t.proxy(
                renames["DataMaskingStatisticsIn"]
            ).optional(),
        }
    ).named(renames["JobStatisticsIn"])
    types["JobStatisticsOut"] = t.struct(
        {
            "load": t.proxy(renames["JobStatistics3Out"]).optional(),
            "query": t.proxy(renames["JobStatistics2Out"]).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"name": t.string().optional(), "slotMs": t.string().optional()}
                )
            ).optional(),
            "numChildJobs": t.string().optional(),
            "creationTime": t.string().optional(),
            "scriptStatistics": t.proxy(renames["ScriptStatisticsOut"]).optional(),
            "quotaDeferments": t.array(t.string()).optional(),
            "sessionInfo": t.proxy(renames["SessionInfoOut"]).optional(),
            "copy": t.proxy(renames["JobStatistics5Out"]).optional(),
            "reservation_id": t.string().optional(),
            "startTime": t.string().optional(),
            "parentJobId": t.string().optional(),
            "endTime": t.string().optional(),
            "transactionInfo": t.proxy(renames["TransactionInfoOut"]).optional(),
            "totalSlotMs": t.string().optional(),
            "rowLevelSecurityStatistics": t.proxy(
                renames["RowLevelSecurityStatisticsOut"]
            ).optional(),
            "extract": t.proxy(renames["JobStatistics4Out"]).optional(),
            "completionRatio": t.number().optional(),
            "totalBytesProcessed": t.string().optional(),
            "dataMaskingStatistics": t.proxy(
                renames["DataMaskingStatisticsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatisticsOut"])
    types["ModelReferenceIn"] = t.struct(
        {"projectId": t.string(), "modelId": t.string(), "datasetId": t.string()}
    ).named(renames["ModelReferenceIn"])
    types["ModelReferenceOut"] = t.struct(
        {
            "projectId": t.string(),
            "modelId": t.string(),
            "datasetId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelReferenceOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GetServiceAccountResponseIn"] = t.struct(
        {"email": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["GetServiceAccountResponseIn"])
    types["GetServiceAccountResponseOut"] = t.struct(
        {
            "email": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetServiceAccountResponseOut"])
    types["JobConfigurationExtractIn"] = t.struct(
        {
            "useAvroLogicalTypes": t.boolean().optional(),
            "fieldDelimiter": t.string().optional(),
            "compression": t.string().optional(),
            "printHeader": t.boolean().optional(),
            "sourceTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "destinationUris": t.array(t.string()).optional(),
            "destinationUri": t.string().optional(),
            "destinationFormat": t.string().optional(),
            "sourceModel": t.proxy(renames["ModelReferenceIn"]).optional(),
        }
    ).named(renames["JobConfigurationExtractIn"])
    types["JobConfigurationExtractOut"] = t.struct(
        {
            "useAvroLogicalTypes": t.boolean().optional(),
            "fieldDelimiter": t.string().optional(),
            "compression": t.string().optional(),
            "printHeader": t.boolean().optional(),
            "sourceTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "destinationUris": t.array(t.string()).optional(),
            "destinationUri": t.string().optional(),
            "destinationFormat": t.string().optional(),
            "sourceModel": t.proxy(renames["ModelReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationExtractOut"])
    types["IntHparamSearchSpaceIn"] = t.struct(
        {
            "range": t.proxy(renames["IntRangeIn"]).optional(),
            "candidates": t.proxy(renames["IntCandidatesIn"]).optional(),
        }
    ).named(renames["IntHparamSearchSpaceIn"])
    types["IntHparamSearchSpaceOut"] = t.struct(
        {
            "range": t.proxy(renames["IntRangeOut"]).optional(),
            "candidates": t.proxy(renames["IntCandidatesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntHparamSearchSpaceOut"])
    types["ArimaFittingMetricsIn"] = t.struct(
        {
            "logLikelihood": t.number().optional(),
            "aic": t.number().optional(),
            "variance": t.number().optional(),
        }
    ).named(renames["ArimaFittingMetricsIn"])
    types["ArimaFittingMetricsOut"] = t.struct(
        {
            "logLikelihood": t.number().optional(),
            "aic": t.number().optional(),
            "variance": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaFittingMetricsOut"])
    types["EntryIn"] = t.struct(
        {"itemCount": t.string().optional(), "predictedLabel": t.string().optional()}
    ).named(renames["EntryIn"])
    types["EntryOut"] = t.struct(
        {
            "itemCount": t.string().optional(),
            "predictedLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntryOut"])
    types["IntCandidatesIn"] = t.struct(
        {"candidates": t.array(t.string()).optional()}
    ).named(renames["IntCandidatesIn"])
    types["IntCandidatesOut"] = t.struct(
        {
            "candidates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntCandidatesOut"])
    types["TableFieldSchemaIn"] = t.struct(
        {
            "type": t.string().optional(),
            "maxLength": t.string().optional(),
            "collation": t.string().optional(),
            "scale": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional(),
            "roundingMode": t.string().optional(),
            "policyTags": t.struct({"names": t.array(t.string()).optional()}),
            "categories": t.struct(
                {"names": t.array(t.string()).optional()}
            ).optional(),
            "precision": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "mode": t.string().optional(),
            "defaultValueExpression": t.string().optional(),
        }
    ).named(renames["TableFieldSchemaIn"])
    types["TableFieldSchemaOut"] = t.struct(
        {
            "type": t.string().optional(),
            "maxLength": t.string().optional(),
            "collation": t.string().optional(),
            "scale": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "roundingMode": t.string().optional(),
            "policyTags": t.struct({"names": t.array(t.string()).optional()}),
            "categories": t.struct(
                {"names": t.array(t.string()).optional()}
            ).optional(),
            "precision": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "mode": t.string().optional(),
            "defaultValueExpression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableFieldSchemaOut"])
    types["BigtableColumnFamilyIn"] = t.struct(
        {
            "familyId": t.string().optional(),
            "onlyReadLatest": t.boolean().optional(),
            "type": t.string().optional(),
            "columns": t.array(t.proxy(renames["BigtableColumnIn"])).optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["BigtableColumnFamilyIn"])
    types["BigtableColumnFamilyOut"] = t.struct(
        {
            "familyId": t.string().optional(),
            "onlyReadLatest": t.boolean().optional(),
            "type": t.string().optional(),
            "columns": t.array(t.proxy(renames["BigtableColumnOut"])).optional(),
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigtableColumnFamilyOut"])
    types["BqmlTrainingRunIn"] = t.struct(
        {
            "trainingOptions": t.struct(
                {
                    "minRelProgress": t.number(),
                    "warmStart": t.boolean(),
                    "l2Reg": t.number(),
                    "l1Reg": t.number(),
                    "maxIteration": t.string(),
                    "learnRateStrategy": t.string(),
                    "earlyStop": t.boolean(),
                    "lineSearchInitLearnRate": t.number(),
                    "learnRate": t.number(),
                }
            ).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "iterationResults": t.array(
                t.proxy(renames["BqmlIterationResultIn"])
            ).optional(),
        }
    ).named(renames["BqmlTrainingRunIn"])
    types["BqmlTrainingRunOut"] = t.struct(
        {
            "trainingOptions": t.struct(
                {
                    "minRelProgress": t.number(),
                    "warmStart": t.boolean(),
                    "l2Reg": t.number(),
                    "l1Reg": t.number(),
                    "maxIteration": t.string(),
                    "learnRateStrategy": t.string(),
                    "earlyStop": t.boolean(),
                    "lineSearchInitLearnRate": t.number(),
                    "learnRate": t.number(),
                }
            ).optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "iterationResults": t.array(
                t.proxy(renames["BqmlIterationResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BqmlTrainingRunOut"])
    types["MaterializedViewDefinitionIn"] = t.struct(
        {
            "allow_non_incremental_definition": t.boolean().optional(),
            "refreshIntervalMs": t.string().optional(),
            "query": t.string().optional(),
            "enableRefresh": t.boolean().optional(),
            "maxStaleness": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
        }
    ).named(renames["MaterializedViewDefinitionIn"])
    types["MaterializedViewDefinitionOut"] = t.struct(
        {
            "allow_non_incremental_definition": t.boolean().optional(),
            "refreshIntervalMs": t.string().optional(),
            "query": t.string().optional(),
            "enableRefresh": t.boolean().optional(),
            "maxStaleness": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaterializedViewDefinitionOut"])
    types["QueryParameterIn"] = t.struct(
        {
            "parameterType": t.proxy(renames["QueryParameterTypeIn"]).optional(),
            "parameterValue": t.proxy(renames["QueryParameterValueIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["QueryParameterIn"])
    types["QueryParameterOut"] = t.struct(
        {
            "parameterType": t.proxy(renames["QueryParameterTypeOut"]).optional(),
            "parameterValue": t.proxy(renames["QueryParameterValueOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryParameterOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["SnapshotDefinitionIn"] = t.struct(
        {
            "baseTableReference": t.proxy(renames["TableReferenceIn"]).optional(),
            "snapshotTime": t.string().optional(),
        }
    ).named(renames["SnapshotDefinitionIn"])
    types["SnapshotDefinitionOut"] = t.struct(
        {
            "baseTableReference": t.proxy(renames["TableReferenceOut"]).optional(),
            "snapshotTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotDefinitionOut"])
    types["HparamSearchSpacesIn"] = t.struct(
        {
            "boosterType": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "optimizer": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "hiddenUnits": t.proxy(renames["IntArrayHparamSearchSpaceIn"]).optional(),
            "batchSize": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "l1Reg": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "colsampleBytree": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "numClusters": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "minSplitLoss": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "subsample": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "learnRate": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "walsAlpha": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "maxTreeDepth": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "dartNormalizeType": t.proxy(
                renames["StringHparamSearchSpaceIn"]
            ).optional(),
            "colsampleBynode": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "dropout": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "colsampleBylevel": t.proxy(
                renames["DoubleHparamSearchSpaceIn"]
            ).optional(),
            "numFactors": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "treeMethod": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "l2Reg": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "activationFn": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "minTreeChildWeight": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "numParallelTree": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
        }
    ).named(renames["HparamSearchSpacesIn"])
    types["HparamSearchSpacesOut"] = t.struct(
        {
            "boosterType": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "optimizer": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "hiddenUnits": t.proxy(renames["IntArrayHparamSearchSpaceOut"]).optional(),
            "batchSize": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "l1Reg": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "colsampleBytree": t.proxy(
                renames["DoubleHparamSearchSpaceOut"]
            ).optional(),
            "numClusters": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "minSplitLoss": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "subsample": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "learnRate": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "walsAlpha": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "maxTreeDepth": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "dartNormalizeType": t.proxy(
                renames["StringHparamSearchSpaceOut"]
            ).optional(),
            "colsampleBynode": t.proxy(
                renames["DoubleHparamSearchSpaceOut"]
            ).optional(),
            "dropout": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "colsampleBylevel": t.proxy(
                renames["DoubleHparamSearchSpaceOut"]
            ).optional(),
            "numFactors": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "treeMethod": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "l2Reg": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "activationFn": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "minTreeChildWeight": t.proxy(
                renames["IntHparamSearchSpaceOut"]
            ).optional(),
            "numParallelTree": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HparamSearchSpacesOut"])
    types["ModelDefinitionIn"] = t.struct(
        {
            "trainingRuns": t.array(t.proxy(renames["BqmlTrainingRunIn"])).optional(),
            "modelOptions": t.struct(
                {
                    "lossType": t.string(),
                    "modelType": t.string(),
                    "labels": t.array(t.string()),
                }
            ).optional(),
        }
    ).named(renames["ModelDefinitionIn"])
    types["ModelDefinitionOut"] = t.struct(
        {
            "trainingRuns": t.array(t.proxy(renames["BqmlTrainingRunOut"])).optional(),
            "modelOptions": t.struct(
                {
                    "lossType": t.string(),
                    "modelType": t.string(),
                    "labels": t.array(t.string()),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelDefinitionOut"])
    types["DoubleCandidatesIn"] = t.struct(
        {"candidates": t.array(t.number()).optional()}
    ).named(renames["DoubleCandidatesIn"])
    types["DoubleCandidatesOut"] = t.struct(
        {
            "candidates": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleCandidatesOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["TrainingRunIn"] = t.struct({"vertexAiModelId": t.string().optional()}).named(
        renames["TrainingRunIn"]
    )
    types["TrainingRunOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "evaluationMetrics": t.proxy(renames["EvaluationMetricsOut"]).optional(),
            "vertexAiModelId": t.string().optional(),
            "classLevelGlobalExplanations": t.array(
                t.proxy(renames["GlobalExplanationOut"])
            ).optional(),
            "trainingOptions": t.proxy(renames["TrainingOptionsOut"]).optional(),
            "results": t.array(t.proxy(renames["IterationResultOut"])).optional(),
            "vertexAiModelVersion": t.string().optional(),
            "trainingStartTime": t.string().optional(),
            "modelLevelGlobalExplanation": t.proxy(
                renames["GlobalExplanationOut"]
            ).optional(),
            "dataSplitResult": t.proxy(renames["DataSplitResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrainingRunOut"])
    types["StringHparamSearchSpaceIn"] = t.struct(
        {"candidates": t.array(t.string()).optional()}
    ).named(renames["StringHparamSearchSpaceIn"])
    types["StringHparamSearchSpaceOut"] = t.struct(
        {
            "candidates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringHparamSearchSpaceOut"])
    types["ExplainQueryStageIn"] = t.struct(
        {
            "shuffleOutputBytesSpilled": t.string().optional(),
            "parallelInputs": t.string().optional(),
            "completedParallelInputs": t.string().optional(),
            "computeRatioMax": t.number().optional(),
            "readRatioAvg": t.number().optional(),
            "startMs": t.string().optional(),
            "id": t.string().optional(),
            "computeMsMax": t.string().optional(),
            "waitMsAvg": t.string().optional(),
            "readRatioMax": t.number().optional(),
            "waitRatioAvg": t.number().optional(),
            "waitMsMax": t.string().optional(),
            "waitRatioMax": t.number().optional(),
            "recordsWritten": t.string().optional(),
            "slotMs": t.string().optional(),
            "name": t.string().optional(),
            "inputStages": t.array(t.string()).optional(),
            "computeRatioAvg": t.number().optional(),
            "endMs": t.string().optional(),
            "readMsMax": t.string().optional(),
            "readMsAvg": t.string().optional(),
            "recordsRead": t.string().optional(),
            "status": t.string().optional(),
            "computeMsAvg": t.string().optional(),
            "writeMsMax": t.string().optional(),
            "shuffleOutputBytes": t.string().optional(),
            "writeRatioMax": t.number().optional(),
            "writeRatioAvg": t.number().optional(),
            "steps": t.array(t.proxy(renames["ExplainQueryStepIn"])).optional(),
            "writeMsAvg": t.string().optional(),
        }
    ).named(renames["ExplainQueryStageIn"])
    types["ExplainQueryStageOut"] = t.struct(
        {
            "shuffleOutputBytesSpilled": t.string().optional(),
            "parallelInputs": t.string().optional(),
            "completedParallelInputs": t.string().optional(),
            "computeRatioMax": t.number().optional(),
            "readRatioAvg": t.number().optional(),
            "startMs": t.string().optional(),
            "id": t.string().optional(),
            "computeMsMax": t.string().optional(),
            "waitMsAvg": t.string().optional(),
            "readRatioMax": t.number().optional(),
            "waitRatioAvg": t.number().optional(),
            "waitMsMax": t.string().optional(),
            "waitRatioMax": t.number().optional(),
            "recordsWritten": t.string().optional(),
            "slotMs": t.string().optional(),
            "name": t.string().optional(),
            "inputStages": t.array(t.string()).optional(),
            "computeRatioAvg": t.number().optional(),
            "endMs": t.string().optional(),
            "readMsMax": t.string().optional(),
            "readMsAvg": t.string().optional(),
            "recordsRead": t.string().optional(),
            "status": t.string().optional(),
            "computeMsAvg": t.string().optional(),
            "writeMsMax": t.string().optional(),
            "shuffleOutputBytes": t.string().optional(),
            "writeRatioMax": t.number().optional(),
            "writeRatioAvg": t.number().optional(),
            "steps": t.array(t.proxy(renames["ExplainQueryStepOut"])).optional(),
            "writeMsAvg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplainQueryStageOut"])
    types["JobConfigurationLoadIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "fieldDelimiter": t.string().optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsIn"]).optional(),
            "projectionFields": t.array(t.string()).optional(),
            "jsonExtension": t.string().optional(),
            "destinationTableProperties": t.proxy(
                renames["DestinationTablePropertiesIn"]
            ).optional(),
            "writeDisposition": t.string().optional(),
            "autodetect": t.boolean().optional(),
            "maxBadRecords": t.integer().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "allowQuotedNewlines": t.boolean().optional(),
            "fileSetSpecType": t.string().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyIn"])
            ).optional(),
            "quote": t.string().optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsIn"]
            ).optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "nullMarker": t.string().optional(),
            "useAvroLogicalTypes": t.boolean().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "createSession": t.boolean().optional(),
            "schemaInline": t.string().optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
            "sourceFormat": t.string().optional(),
            "createDisposition": t.string().optional(),
            "schemaInlineFormat": t.string().optional(),
            "sourceUris": t.array(t.string()).optional(),
            "clustering": t.proxy(renames["ClusteringIn"]).optional(),
            "skipLeadingRows": t.integer().optional(),
            "destinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
        }
    ).named(renames["JobConfigurationLoadIn"])
    types["JobConfigurationLoadOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "fieldDelimiter": t.string().optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsOut"]).optional(),
            "projectionFields": t.array(t.string()).optional(),
            "jsonExtension": t.string().optional(),
            "destinationTableProperties": t.proxy(
                renames["DestinationTablePropertiesOut"]
            ).optional(),
            "writeDisposition": t.string().optional(),
            "autodetect": t.boolean().optional(),
            "maxBadRecords": t.integer().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "allowQuotedNewlines": t.boolean().optional(),
            "fileSetSpecType": t.string().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyOut"])
            ).optional(),
            "quote": t.string().optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsOut"]
            ).optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "nullMarker": t.string().optional(),
            "useAvroLogicalTypes": t.boolean().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningOut"]).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "createSession": t.boolean().optional(),
            "schemaInline": t.string().optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningOut"]).optional(),
            "sourceFormat": t.string().optional(),
            "createDisposition": t.string().optional(),
            "schemaInlineFormat": t.string().optional(),
            "sourceUris": t.array(t.string()).optional(),
            "clustering": t.proxy(renames["ClusteringOut"]).optional(),
            "skipLeadingRows": t.integer().optional(),
            "destinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationLoadOut"])
    types["JobStatistics2In"] = t.struct(
        {
            "queryPlan": t.array(t.proxy(renames["ExplainQueryStageIn"])).optional(),
            "modelTrainingExpectedTotalIteration": t.string().optional(),
            "ddlTargetDataset": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "timeline": t.array(t.proxy(renames["QueryTimelineSampleIn"])).optional(),
            "totalBytesBilled": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "searchStatistics": t.proxy(renames["SearchStatisticsIn"]).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "undeclaredQueryParameters": t.array(
                t.proxy(renames["QueryParameterIn"])
            ).optional(),
            "sparkStatistics": t.proxy(renames["SparkStatisticsIn"]).optional(),
            "ddlTargetRoutine": t.proxy(renames["RoutineReferenceIn"]).optional(),
            "modelTraining": t.proxy(renames["BigQueryModelTrainingIn"]).optional(),
            "ddlDestinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "totalBytesProcessed": t.string().optional(),
            "ddlAffectedRowAccessPolicyCount": t.string().optional(),
            "referencedTables": t.array(
                t.proxy(renames["TableReferenceIn"])
            ).optional(),
            "totalPartitionsProcessed": t.string().optional(),
            "biEngineStatistics": t.proxy(renames["BiEngineStatisticsIn"]).optional(),
            "mlStatistics": t.proxy(renames["MlStatisticsIn"]).optional(),
            "estimatedBytesProcessed": t.string().optional(),
            "modelTrainingCurrentIteration": t.integer().optional(),
            "transferredBytes": t.string().optional(),
            "billingTier": t.integer().optional(),
            "ddlTargetTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "ddlTargetRowAccessPolicy": t.proxy(
                renames["RowAccessPolicyReferenceIn"]
            ).optional(),
            "statementType": t.string().optional(),
            "referencedRoutines": t.array(
                t.proxy(renames["RoutineReferenceIn"])
            ).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"slotMs": t.string().optional(), "name": t.string().optional()}
                )
            ).optional(),
            "cacheHit": t.boolean().optional(),
            "ddlOperationPerformed": t.string().optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsIn"]).optional(),
            "totalSlotMs": t.string().optional(),
            "totalBytesProcessedAccuracy": t.string().optional(),
        }
    ).named(renames["JobStatistics2In"])
    types["JobStatistics2Out"] = t.struct(
        {
            "queryPlan": t.array(t.proxy(renames["ExplainQueryStageOut"])).optional(),
            "modelTrainingExpectedTotalIteration": t.string().optional(),
            "ddlTargetDataset": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "timeline": t.array(t.proxy(renames["QueryTimelineSampleOut"])).optional(),
            "totalBytesBilled": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "searchStatistics": t.proxy(renames["SearchStatisticsOut"]).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "undeclaredQueryParameters": t.array(
                t.proxy(renames["QueryParameterOut"])
            ).optional(),
            "sparkStatistics": t.proxy(renames["SparkStatisticsOut"]).optional(),
            "ddlTargetRoutine": t.proxy(renames["RoutineReferenceOut"]).optional(),
            "modelTraining": t.proxy(renames["BigQueryModelTrainingOut"]).optional(),
            "ddlDestinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "totalBytesProcessed": t.string().optional(),
            "ddlAffectedRowAccessPolicyCount": t.string().optional(),
            "referencedTables": t.array(
                t.proxy(renames["TableReferenceOut"])
            ).optional(),
            "totalPartitionsProcessed": t.string().optional(),
            "biEngineStatistics": t.proxy(renames["BiEngineStatisticsOut"]).optional(),
            "mlStatistics": t.proxy(renames["MlStatisticsOut"]).optional(),
            "estimatedBytesProcessed": t.string().optional(),
            "modelTrainingCurrentIteration": t.integer().optional(),
            "transferredBytes": t.string().optional(),
            "billingTier": t.integer().optional(),
            "ddlTargetTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "ddlTargetRowAccessPolicy": t.proxy(
                renames["RowAccessPolicyReferenceOut"]
            ).optional(),
            "statementType": t.string().optional(),
            "referencedRoutines": t.array(
                t.proxy(renames["RoutineReferenceOut"])
            ).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"slotMs": t.string().optional(), "name": t.string().optional()}
                )
            ).optional(),
            "cacheHit": t.boolean().optional(),
            "ddlOperationPerformed": t.string().optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsOut"]).optional(),
            "totalSlotMs": t.string().optional(),
            "totalBytesProcessedAccuracy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatistics2Out"])
    types["TableDataInsertAllRequestIn"] = t.struct(
        {
            "ignoreUnknownValues": t.boolean().optional(),
            "templateSuffix": t.string().optional(),
            "skipInvalidRows": t.boolean().optional(),
            "kind": t.string().optional(),
            "rows": t.array(
                t.struct(
                    {
                        "insertId": t.string().optional(),
                        "json": t.proxy(renames["JsonObjectIn"]).optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["TableDataInsertAllRequestIn"])
    types["TableDataInsertAllRequestOut"] = t.struct(
        {
            "ignoreUnknownValues": t.boolean().optional(),
            "templateSuffix": t.string().optional(),
            "skipInvalidRows": t.boolean().optional(),
            "kind": t.string().optional(),
            "rows": t.array(
                t.struct(
                    {
                        "insertId": t.string().optional(),
                        "json": t.proxy(renames["JsonObjectOut"]).optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableDataInsertAllRequestOut"])
    types["GetQueryResultsResponseIn"] = t.struct(
        {
            "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
            "cacheHit": t.boolean().optional(),
            "kind": t.string().optional(),
            "totalRows": t.string().optional(),
            "etag": t.string().optional(),
            "pageToken": t.string().optional(),
            "totalBytesProcessed": t.string().optional(),
            "numDmlAffectedRows": t.string().optional(),
            "jobComplete": t.boolean().optional(),
            "rows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
        }
    ).named(renames["GetQueryResultsResponseIn"])
    types["GetQueryResultsResponseOut"] = t.struct(
        {
            "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
            "cacheHit": t.boolean().optional(),
            "kind": t.string().optional(),
            "totalRows": t.string().optional(),
            "etag": t.string().optional(),
            "pageToken": t.string().optional(),
            "totalBytesProcessed": t.string().optional(),
            "numDmlAffectedRows": t.string().optional(),
            "jobComplete": t.boolean().optional(),
            "rows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetQueryResultsResponseOut"])
    types["TableConstraintsIn"] = t.struct(
        {
            "primaryKey": t.struct({"columns": t.array(t.string())}).optional(),
            "foreignKeys": t.array(
                t.struct(
                    {
                        "columnReferences": t.array(
                            t.struct(
                                {
                                    "referencedColumn": t.string(),
                                    "referencingColumn": t.string(),
                                }
                            )
                        ),
                        "referencedTable": t.struct(
                            {
                                "projectId": t.string(),
                                "tableId": t.string(),
                                "datasetId": t.string(),
                            }
                        ),
                        "name": t.string(),
                    }
                )
            ).optional(),
        }
    ).named(renames["TableConstraintsIn"])
    types["TableConstraintsOut"] = t.struct(
        {
            "primaryKey": t.struct({"columns": t.array(t.string())}).optional(),
            "foreignKeys": t.array(
                t.struct(
                    {
                        "columnReferences": t.array(
                            t.struct(
                                {
                                    "referencedColumn": t.string(),
                                    "referencingColumn": t.string(),
                                }
                            )
                        ),
                        "referencedTable": t.struct(
                            {
                                "projectId": t.string(),
                                "tableId": t.string(),
                                "datasetId": t.string(),
                            }
                        ),
                        "name": t.string(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableConstraintsOut"])
    types["ArimaForecastingMetricsIn"] = t.struct(
        {
            "hasDrift": t.array(t.boolean()).optional(),
            "arimaSingleModelForecastingMetrics": t.array(
                t.proxy(renames["ArimaSingleModelForecastingMetricsIn"])
            ).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "nonSeasonalOrder": t.array(t.proxy(renames["ArimaOrderIn"])).optional(),
            "arimaFittingMetrics": t.array(
                t.proxy(renames["ArimaFittingMetricsIn"])
            ).optional(),
            "timeSeriesId": t.array(t.string()).optional(),
        }
    ).named(renames["ArimaForecastingMetricsIn"])
    types["ArimaForecastingMetricsOut"] = t.struct(
        {
            "hasDrift": t.array(t.boolean()).optional(),
            "arimaSingleModelForecastingMetrics": t.array(
                t.proxy(renames["ArimaSingleModelForecastingMetricsOut"])
            ).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "nonSeasonalOrder": t.array(t.proxy(renames["ArimaOrderOut"])).optional(),
            "arimaFittingMetrics": t.array(
                t.proxy(renames["ArimaFittingMetricsOut"])
            ).optional(),
            "timeSeriesId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaForecastingMetricsOut"])
    types["JobStatistics5In"] = t.struct(
        {
            "copied_rows": t.string().optional(),
            "copied_logical_bytes": t.string().optional(),
        }
    ).named(renames["JobStatistics5In"])
    types["JobStatistics5Out"] = t.struct(
        {
            "copied_rows": t.string().optional(),
            "copied_logical_bytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatistics5Out"])
    types["ListRowAccessPoliciesResponseIn"] = t.struct(
        {
            "rowAccessPolicies": t.array(
                t.proxy(renames["RowAccessPolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRowAccessPoliciesResponseIn"])
    types["ListRowAccessPoliciesResponseOut"] = t.struct(
        {
            "rowAccessPolicies": t.array(
                t.proxy(renames["RowAccessPolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRowAccessPoliciesResponseOut"])
    types["RowAccessPolicyReferenceIn"] = t.struct(
        {
            "policyId": t.string(),
            "tableId": t.string(),
            "datasetId": t.string(),
            "projectId": t.string(),
        }
    ).named(renames["RowAccessPolicyReferenceIn"])
    types["RowAccessPolicyReferenceOut"] = t.struct(
        {
            "policyId": t.string(),
            "tableId": t.string(),
            "datasetId": t.string(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowAccessPolicyReferenceOut"])
    types["TableSchemaIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional()}
    ).named(renames["TableSchemaIn"])
    types["TableSchemaOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableSchemaOut"])
    types["RoutineReferenceIn"] = t.struct(
        {"projectId": t.string(), "routineId": t.string(), "datasetId": t.string()}
    ).named(renames["RoutineReferenceIn"])
    types["RoutineReferenceOut"] = t.struct(
        {
            "projectId": t.string(),
            "routineId": t.string(),
            "datasetId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutineReferenceOut"])
    types["ListRoutinesResponseIn"] = t.struct(
        {
            "routines": t.array(t.proxy(renames["RoutineIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRoutinesResponseIn"])
    types["ListRoutinesResponseOut"] = t.struct(
        {
            "routines": t.array(t.proxy(renames["RoutineOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRoutinesResponseOut"])
    types["DataMaskingStatisticsIn"] = t.struct(
        {"dataMaskingApplied": t.boolean().optional()}
    ).named(renames["DataMaskingStatisticsIn"])
    types["DataMaskingStatisticsOut"] = t.struct(
        {
            "dataMaskingApplied": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataMaskingStatisticsOut"])
    types["TransactionInfoIn"] = t.struct(
        {"transactionId": t.string().optional()}
    ).named(renames["TransactionInfoIn"])
    types["TransactionInfoOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionInfoOut"])
    types["ModelIn"] = t.struct(
        {
            "modelReference": t.proxy(renames["ModelReferenceIn"]),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "bestTrialId": t.string().optional(),
            "trainingRuns": t.array(t.proxy(renames["TrainingRunIn"])).optional(),
            "expirationTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
        }
    ).named(renames["ModelIn"])
    types["ModelOut"] = t.struct(
        {
            "modelReference": t.proxy(renames["ModelReferenceOut"]),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "hparamTrials": t.array(
                t.proxy(renames["HparamTuningTrialOut"])
            ).optional(),
            "defaultTrialId": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "bestTrialId": t.string().optional(),
            "location": t.string().optional(),
            "featureColumns": t.array(
                t.proxy(renames["StandardSqlFieldOut"])
            ).optional(),
            "trainingRuns": t.array(t.proxy(renames["TrainingRunOut"])).optional(),
            "remoteModelInfo": t.proxy(renames["RemoteModelInfoOut"]).optional(),
            "expirationTime": t.string().optional(),
            "optimalTrialIds": t.array(t.string()).optional(),
            "labelColumns": t.array(t.proxy(renames["StandardSqlFieldOut"])).optional(),
            "modelType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "creationTime": t.string().optional(),
            "hparamSearchSpaces": t.proxy(renames["HparamSearchSpacesOut"]).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOut"])
    types["ProjectReferenceIn"] = t.struct({"projectId": t.string().optional()}).named(
        renames["ProjectReferenceIn"]
    )
    types["ProjectReferenceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectReferenceOut"])
    types["IntArrayHparamSearchSpaceIn"] = t.struct(
        {"candidates": t.array(t.proxy(renames["IntArrayIn"])).optional()}
    ).named(renames["IntArrayHparamSearchSpaceIn"])
    types["IntArrayHparamSearchSpaceOut"] = t.struct(
        {
            "candidates": t.array(t.proxy(renames["IntArrayOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntArrayHparamSearchSpaceOut"])
    types["MultiClassClassificationMetricsIn"] = t.struct(
        {
            "confusionMatrixList": t.array(
                t.proxy(renames["ConfusionMatrixIn"])
            ).optional(),
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsIn"]
            ).optional(),
        }
    ).named(renames["MultiClassClassificationMetricsIn"])
    types["MultiClassClassificationMetricsOut"] = t.struct(
        {
            "confusionMatrixList": t.array(
                t.proxy(renames["ConfusionMatrixOut"])
            ).optional(),
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClassClassificationMetricsOut"])
    types["BigtableOptionsIn"] = t.struct(
        {
            "columnFamilies": t.array(
                t.proxy(renames["BigtableColumnFamilyIn"])
            ).optional(),
            "ignoreUnspecifiedColumnFamilies": t.boolean().optional(),
            "readRowkeyAsString": t.boolean().optional(),
        }
    ).named(renames["BigtableOptionsIn"])
    types["BigtableOptionsOut"] = t.struct(
        {
            "columnFamilies": t.array(
                t.proxy(renames["BigtableColumnFamilyOut"])
            ).optional(),
            "ignoreUnspecifiedColumnFamilies": t.boolean().optional(),
            "readRowkeyAsString": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigtableOptionsOut"])
    types["StandardSqlTableTypeIn"] = t.struct(
        {"columns": t.array(t.proxy(renames["StandardSqlFieldIn"])).optional()}
    ).named(renames["StandardSqlTableTypeIn"])
    types["StandardSqlTableTypeOut"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["StandardSqlFieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlTableTypeOut"])
    types["ArimaOrderIn"] = t.struct(
        {
            "d": t.string().optional(),
            "q": t.string().optional(),
            "p": t.string().optional(),
        }
    ).named(renames["ArimaOrderIn"])
    types["ArimaOrderOut"] = t.struct(
        {
            "d": t.string().optional(),
            "q": t.string().optional(),
            "p": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaOrderOut"])
    types["BiEngineStatisticsIn"] = t.struct(
        {
            "biEngineMode": t.string().optional(),
            "biEngineReasons": t.array(t.proxy(renames["BiEngineReasonIn"])).optional(),
            "accelerationMode": t.string().optional(),
        }
    ).named(renames["BiEngineStatisticsIn"])
    types["BiEngineStatisticsOut"] = t.struct(
        {
            "biEngineMode": t.string().optional(),
            "biEngineReasons": t.array(
                t.proxy(renames["BiEngineReasonOut"])
            ).optional(),
            "accelerationMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiEngineStatisticsOut"])
    types["ConnectionPropertyIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["ConnectionPropertyIn"])
    types["ConnectionPropertyOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionPropertyOut"])
    types["ExplainQueryStepIn"] = t.struct(
        {"kind": t.string().optional(), "substeps": t.array(t.string()).optional()}
    ).named(renames["ExplainQueryStepIn"])
    types["ExplainQueryStepOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "substeps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplainQueryStepOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["CsvOptionsIn"] = t.struct(
        {
            "null_marker": t.string().optional(),
            "quote": t.string().optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "allowQuotedNewlines": t.boolean().optional(),
            "fieldDelimiter": t.string().optional(),
            "skipLeadingRows": t.string().optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["CsvOptionsIn"])
    types["CsvOptionsOut"] = t.struct(
        {
            "null_marker": t.string().optional(),
            "quote": t.string().optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "allowQuotedNewlines": t.boolean().optional(),
            "fieldDelimiter": t.string().optional(),
            "skipLeadingRows": t.string().optional(),
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvOptionsOut"])
    types["ArimaCoefficientsIn"] = t.struct(
        {
            "interceptCoefficient": t.number().optional(),
            "movingAverageCoefficients": t.array(t.number()).optional(),
            "autoRegressiveCoefficients": t.array(t.number()).optional(),
        }
    ).named(renames["ArimaCoefficientsIn"])
    types["ArimaCoefficientsOut"] = t.struct(
        {
            "interceptCoefficient": t.number().optional(),
            "movingAverageCoefficients": t.array(t.number()).optional(),
            "autoRegressiveCoefficients": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaCoefficientsOut"])
    types["EvaluationMetricsIn"] = t.struct(
        {
            "rankingMetrics": t.proxy(renames["RankingMetricsIn"]).optional(),
            "multiClassClassificationMetrics": t.proxy(
                renames["MultiClassClassificationMetricsIn"]
            ).optional(),
            "clusteringMetrics": t.proxy(renames["ClusteringMetricsIn"]).optional(),
            "regressionMetrics": t.proxy(renames["RegressionMetricsIn"]).optional(),
            "binaryClassificationMetrics": t.proxy(
                renames["BinaryClassificationMetricsIn"]
            ).optional(),
            "arimaForecastingMetrics": t.proxy(
                renames["ArimaForecastingMetricsIn"]
            ).optional(),
            "dimensionalityReductionMetrics": t.proxy(
                renames["DimensionalityReductionMetricsIn"]
            ).optional(),
        }
    ).named(renames["EvaluationMetricsIn"])
    types["EvaluationMetricsOut"] = t.struct(
        {
            "rankingMetrics": t.proxy(renames["RankingMetricsOut"]).optional(),
            "multiClassClassificationMetrics": t.proxy(
                renames["MultiClassClassificationMetricsOut"]
            ).optional(),
            "clusteringMetrics": t.proxy(renames["ClusteringMetricsOut"]).optional(),
            "regressionMetrics": t.proxy(renames["RegressionMetricsOut"]).optional(),
            "binaryClassificationMetrics": t.proxy(
                renames["BinaryClassificationMetricsOut"]
            ).optional(),
            "arimaForecastingMetrics": t.proxy(
                renames["ArimaForecastingMetricsOut"]
            ).optional(),
            "dimensionalityReductionMetrics": t.proxy(
                renames["DimensionalityReductionMetricsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluationMetricsOut"])
    types["SparkOptionsIn"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "pyFileUris": t.array(t.string()).optional(),
            "mainFileUri": t.string().optional(),
            "containerImage": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "fileUris": t.array(t.string()).optional(),
            "connection": t.string().optional(),
            "jarUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkOptionsIn"])
    types["SparkOptionsOut"] = t.struct(
        {
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "archiveUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "pyFileUris": t.array(t.string()).optional(),
            "mainFileUri": t.string().optional(),
            "containerImage": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "fileUris": t.array(t.string()).optional(),
            "connection": t.string().optional(),
            "jarUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkOptionsOut"])
    types["TableIn"] = t.struct(
        {
            "maxStaleness": t.string().optional(),
            "numLongTermLogicalBytes": t.string().optional(),
            "description": t.string().optional(),
            "snapshotDefinition": t.proxy(renames["SnapshotDefinitionIn"]).optional(),
            "lastModifiedTime": t.string().optional(),
            "friendlyName": t.string().optional(),
            "numRows": t.string().optional(),
            "numLongTermPhysicalBytes": t.string().optional(),
            "materializedView": t.proxy(
                renames["MaterializedViewDefinitionIn"]
            ).optional(),
            "numPartitions": t.string().optional(),
            "numActiveLogicalBytes": t.string().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
            "numTotalPhysicalBytes": t.string().optional(),
            "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
            "numPhysicalBytes": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "numTotalLogicalBytes": t.string().optional(),
            "selfLink": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "numActivePhysicalBytes": t.string().optional(),
            "numTimeTravelPhysicalBytes": t.string().optional(),
            "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
            "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
            "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
            "creationTime": t.string().optional(),
            "etag": t.string().optional(),
            "externalDataConfiguration": t.proxy(
                renames["ExternalDataConfigurationIn"]
            ).optional(),
            "expirationTime": t.string().optional(),
            "location": t.string().optional(),
            "numBytes": t.string().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "numLongTermBytes": t.string().optional(),
            "clustering": t.proxy(renames["ClusteringIn"]).optional(),
            "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
            "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
            "defaultRoundingMode": t.string().optional(),
            "defaultCollation": t.string().optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "maxStaleness": t.string().optional(),
            "numLongTermLogicalBytes": t.string().optional(),
            "description": t.string().optional(),
            "snapshotDefinition": t.proxy(renames["SnapshotDefinitionOut"]).optional(),
            "lastModifiedTime": t.string().optional(),
            "friendlyName": t.string().optional(),
            "numRows": t.string().optional(),
            "numLongTermPhysicalBytes": t.string().optional(),
            "materializedView": t.proxy(
                renames["MaterializedViewDefinitionOut"]
            ).optional(),
            "numPartitions": t.string().optional(),
            "numActiveLogicalBytes": t.string().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningOut"]).optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
            "numTotalPhysicalBytes": t.string().optional(),
            "tableConstraints": t.proxy(renames["TableConstraintsOut"]).optional(),
            "numPhysicalBytes": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "numTotalLogicalBytes": t.string().optional(),
            "selfLink": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "numActivePhysicalBytes": t.string().optional(),
            "numTimeTravelPhysicalBytes": t.string().optional(),
            "tableReference": t.proxy(renames["TableReferenceOut"]).optional(),
            "model": t.proxy(renames["ModelDefinitionOut"]).optional(),
            "view": t.proxy(renames["ViewDefinitionOut"]).optional(),
            "creationTime": t.string().optional(),
            "etag": t.string().optional(),
            "externalDataConfiguration": t.proxy(
                renames["ExternalDataConfigurationOut"]
            ).optional(),
            "expirationTime": t.string().optional(),
            "location": t.string().optional(),
            "numBytes": t.string().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningOut"]).optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "numLongTermBytes": t.string().optional(),
            "clustering": t.proxy(renames["ClusteringOut"]).optional(),
            "cloneDefinition": t.proxy(renames["CloneDefinitionOut"]).optional(),
            "streamingBuffer": t.proxy(renames["StreamingbufferOut"]).optional(),
            "defaultRoundingMode": t.string().optional(),
            "defaultCollation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["RemoteFunctionOptionsIn"] = t.struct(
        {
            "userDefinedContext": t.struct({"_": t.string().optional()}).optional(),
            "maxBatchingRows": t.string().optional(),
            "endpoint": t.string().optional(),
            "connection": t.string().optional(),
        }
    ).named(renames["RemoteFunctionOptionsIn"])
    types["RemoteFunctionOptionsOut"] = t.struct(
        {
            "userDefinedContext": t.struct({"_": t.string().optional()}).optional(),
            "maxBatchingRows": t.string().optional(),
            "endpoint": t.string().optional(),
            "connection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteFunctionOptionsOut"])
    types["SparkStatisticsIn"] = t.struct(
        {
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "logging_info": t.proxy(renames["SparkLoggingInfoIn"]).optional(),
            "spark_job_location": t.string().optional(),
            "spark_job_id": t.string().optional(),
        }
    ).named(renames["SparkStatisticsIn"])
    types["SparkStatisticsOut"] = t.struct(
        {
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "logging_info": t.proxy(renames["SparkLoggingInfoOut"]).optional(),
            "spark_job_location": t.string().optional(),
            "spark_job_id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkStatisticsOut"])
    types["JsonObjectIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JsonObjectIn"]
    )
    types["JsonObjectOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["JsonObjectOut"])
    types["ClusteringIn"] = t.struct({"fields": t.array(t.string()).optional()}).named(
        renames["ClusteringIn"]
    )
    types["ClusteringOut"] = t.struct(
        {
            "fields": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusteringOut"])
    types["QueryParameterTypeIn"] = t.struct(
        {
            "structTypes": t.array(
                t.struct(
                    {
                        "type": t.proxy(renames["QueryParameterTypeIn"]).optional(),
                        "description": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "arrayType": t.proxy(renames["QueryParameterTypeIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["QueryParameterTypeIn"])
    types["QueryParameterTypeOut"] = t.struct(
        {
            "structTypes": t.array(
                t.struct(
                    {
                        "type": t.proxy(renames["QueryParameterTypeOut"]).optional(),
                        "description": t.string().optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "arrayType": t.proxy(renames["QueryParameterTypeOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryParameterTypeOut"])
    types["ScriptStackFrameIn"] = t.struct(
        {
            "startColumn": t.integer().optional(),
            "startLine": t.integer().optional(),
            "procedureId": t.string().optional(),
            "text": t.string().optional(),
            "endLine": t.integer().optional(),
            "endColumn": t.integer().optional(),
        }
    ).named(renames["ScriptStackFrameIn"])
    types["ScriptStackFrameOut"] = t.struct(
        {
            "startColumn": t.integer().optional(),
            "startLine": t.integer().optional(),
            "procedureId": t.string().optional(),
            "text": t.string().optional(),
            "endLine": t.integer().optional(),
            "endColumn": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptStackFrameOut"])
    types["DoubleRangeIn"] = t.struct(
        {"min": t.number().optional(), "max": t.number().optional()}
    ).named(renames["DoubleRangeIn"])
    types["DoubleRangeOut"] = t.struct(
        {
            "min": t.number().optional(),
            "max": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleRangeOut"])
    types["TableDataListIn"] = t.struct(
        {
            "totalRows": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "pageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["TableDataListIn"])
    types["TableDataListOut"] = t.struct(
        {
            "totalRows": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "pageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableDataListOut"])
    types["CategoricalValueIn"] = t.struct(
        {"categoryCounts": t.array(t.proxy(renames["CategoryCountIn"])).optional()}
    ).named(renames["CategoricalValueIn"])
    types["CategoricalValueOut"] = t.struct(
        {
            "categoryCounts": t.array(t.proxy(renames["CategoryCountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoricalValueOut"])
    types["ListModelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "models": t.array(t.proxy(renames["ModelIn"])).optional(),
        }
    ).named(renames["ListModelsResponseIn"])
    types["ListModelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "models": t.array(t.proxy(renames["ModelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListModelsResponseOut"])
    types["DoubleHparamSearchSpaceIn"] = t.struct(
        {
            "range": t.proxy(renames["DoubleRangeIn"]).optional(),
            "candidates": t.proxy(renames["DoubleCandidatesIn"]).optional(),
        }
    ).named(renames["DoubleHparamSearchSpaceIn"])
    types["DoubleHparamSearchSpaceOut"] = t.struct(
        {
            "range": t.proxy(renames["DoubleRangeOut"]).optional(),
            "candidates": t.proxy(renames["DoubleCandidatesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleHparamSearchSpaceOut"])
    types["RangePartitioningIn"] = t.struct(
        {
            "range": t.struct(
                {
                    "start": t.string().optional(),
                    "interval": t.string().optional(),
                    "end": t.string().optional(),
                }
            ).optional(),
            "field": t.string().optional(),
        }
    ).named(renames["RangePartitioningIn"])
    types["RangePartitioningOut"] = t.struct(
        {
            "range": t.struct(
                {
                    "start": t.string().optional(),
                    "interval": t.string().optional(),
                    "end": t.string().optional(),
                }
            ).optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangePartitioningOut"])
    types["JobIn"] = t.struct(
        {
            "user_email": t.string().optional(),
            "selfLink": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.proxy(renames["JobStatusIn"]).optional(),
            "id": t.string().optional(),
            "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
            "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
            "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "user_email": t.string().optional(),
            "selfLink": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "id": t.string().optional(),
            "statistics": t.proxy(renames["JobStatisticsOut"]).optional(),
            "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
            "configuration": t.proxy(renames["JobConfigurationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["PrincipalComponentInfoIn"] = t.struct(
        {
            "principalComponentId": t.string().optional(),
            "cumulativeExplainedVarianceRatio": t.number().optional(),
            "explainedVariance": t.number().optional(),
            "explainedVarianceRatio": t.number().optional(),
        }
    ).named(renames["PrincipalComponentInfoIn"])
    types["PrincipalComponentInfoOut"] = t.struct(
        {
            "principalComponentId": t.string().optional(),
            "cumulativeExplainedVarianceRatio": t.number().optional(),
            "explainedVariance": t.number().optional(),
            "explainedVarianceRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalComponentInfoOut"])
    types["QueryParameterValueIn"] = t.struct(
        {
            "structValues": t.struct({"_": t.string().optional()}).optional(),
            "arrayValues": t.array(
                t.proxy(renames["QueryParameterValueIn"])
            ).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["QueryParameterValueIn"])
    types["QueryParameterValueOut"] = t.struct(
        {
            "structValues": t.struct({"_": t.string().optional()}).optional(),
            "arrayValues": t.array(
                t.proxy(renames["QueryParameterValueOut"])
            ).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryParameterValueOut"])
    types["TableDataInsertAllResponseIn"] = t.struct(
        {
            "insertErrors": t.array(
                t.struct(
                    {
                        "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
                        "index": t.integer().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["TableDataInsertAllResponseIn"])
    types["TableDataInsertAllResponseOut"] = t.struct(
        {
            "insertErrors": t.array(
                t.struct(
                    {
                        "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
                        "index": t.integer().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableDataInsertAllResponseOut"])
    types["ArimaModelInfoIn"] = t.struct(
        {
            "timeSeriesIds": t.array(t.string()).optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderIn"]).optional(),
            "hasStepChanges": t.boolean().optional(),
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesId": t.string().optional(),
            "hasDrift": t.boolean().optional(),
            "arimaFittingMetrics": t.proxy(renames["ArimaFittingMetricsIn"]).optional(),
            "arimaCoefficients": t.proxy(renames["ArimaCoefficientsIn"]).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "hasSpikesAndDips": t.boolean().optional(),
        }
    ).named(renames["ArimaModelInfoIn"])
    types["ArimaModelInfoOut"] = t.struct(
        {
            "timeSeriesIds": t.array(t.string()).optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderOut"]).optional(),
            "hasStepChanges": t.boolean().optional(),
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesId": t.string().optional(),
            "hasDrift": t.boolean().optional(),
            "arimaFittingMetrics": t.proxy(
                renames["ArimaFittingMetricsOut"]
            ).optional(),
            "arimaCoefficients": t.proxy(renames["ArimaCoefficientsOut"]).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "hasSpikesAndDips": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaModelInfoOut"])
    types["ConfusionMatrixIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "confidenceThreshold": t.number().optional(),
        }
    ).named(renames["ConfusionMatrixIn"])
    types["ConfusionMatrixOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "confidenceThreshold": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfusionMatrixOut"])
    types["ErrorProtoIn"] = t.struct(
        {
            "location": t.string().optional(),
            "reason": t.string().optional(),
            "message": t.string().optional(),
            "debugInfo": t.string().optional(),
        }
    ).named(renames["ErrorProtoIn"])
    types["ErrorProtoOut"] = t.struct(
        {
            "location": t.string().optional(),
            "reason": t.string().optional(),
            "message": t.string().optional(),
            "debugInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorProtoOut"])
    types["GoogleSheetsOptionsIn"] = t.struct(
        {"range": t.string().optional(), "skipLeadingRows": t.string().optional()}
    ).named(renames["GoogleSheetsOptionsIn"])
    types["GoogleSheetsOptionsOut"] = t.struct(
        {
            "range": t.string().optional(),
            "skipLeadingRows": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSheetsOptionsOut"])
    types["ClusterInfoIn"] = t.struct(
        {
            "centroidId": t.string().optional(),
            "clusterSize": t.string().optional(),
            "clusterRadius": t.number().optional(),
        }
    ).named(renames["ClusterInfoIn"])
    types["ClusterInfoOut"] = t.struct(
        {
            "centroidId": t.string().optional(),
            "clusterSize": t.string().optional(),
            "clusterRadius": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterInfoOut"])
    types["IntRangeIn"] = t.struct(
        {"max": t.string().optional(), "min": t.string().optional()}
    ).named(renames["IntRangeIn"])
    types["IntRangeOut"] = t.struct(
        {
            "max": t.string().optional(),
            "min": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntRangeOut"])
    types["IndexUnusedReasonIn"] = t.struct(
        {
            "index_name": t.string().optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
            "base_table": t.proxy(renames["TableReferenceIn"]).optional(),
        }
    ).named(renames["IndexUnusedReasonIn"])
    types["IndexUnusedReasonOut"] = t.struct(
        {
            "index_name": t.string().optional(),
            "code": t.string().optional(),
            "message": t.string().optional(),
            "base_table": t.proxy(renames["TableReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexUnusedReasonOut"])
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
    types["BigQueryModelTrainingIn"] = t.struct(
        {
            "currentIteration": t.integer().optional(),
            "expectedTotalIterations": t.string().optional(),
        }
    ).named(renames["BigQueryModelTrainingIn"])
    types["BigQueryModelTrainingOut"] = t.struct(
        {
            "currentIteration": t.integer().optional(),
            "expectedTotalIterations": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryModelTrainingOut"])
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
    types["FeatureValueIn"] = t.struct(
        {
            "categoricalValue": t.proxy(renames["CategoricalValueIn"]).optional(),
            "featureColumn": t.string().optional(),
            "numericalValue": t.number().optional(),
        }
    ).named(renames["FeatureValueIn"])
    types["FeatureValueOut"] = t.struct(
        {
            "categoricalValue": t.proxy(renames["CategoricalValueOut"]).optional(),
            "featureColumn": t.string().optional(),
            "numericalValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureValueOut"])
    types["DatasetIn"] = t.struct(
        {
            "satisfiesPzs": t.boolean().optional(),
            "defaultTableExpirationMs": t.string().optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "defaultPartitionExpirationMs": t.string().optional(),
            "defaultRoundingMode": t.string().optional(),
            "friendlyName": t.string().optional(),
            "storageBillingModel": t.string().optional(),
            "creationTime": t.string().optional(),
            "defaultEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ),
            "selfLink": t.string().optional(),
            "access": t.array(
                t.struct(
                    {
                        "view": t.proxy(renames["TableReferenceIn"]).optional(),
                        "iamMember": t.string().optional(),
                        "dataset": t.proxy(renames["DatasetAccessEntryIn"]).optional(),
                        "routine": t.proxy(renames["RoutineReferenceIn"]).optional(),
                        "role": t.string().optional(),
                        "groupByEmail": t.string().optional(),
                        "specialGroup": t.string().optional(),
                        "domain": t.string().optional(),
                        "userByEmail": t.string().optional(),
                    }
                )
            ).optional(),
            "maxTimeTravelHours": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "isCaseInsensitive": t.boolean().optional(),
            "lastModifiedTime": t.string().optional(),
            "defaultCollation": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "tags": t.array(
                t.struct(
                    {"tagValue": t.string().optional(), "tagKey": t.string().optional()}
                )
            ).optional(),
            "kind": t.string().optional(),
            "datasetReference": t.proxy(renames["DatasetReferenceIn"]).optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "satisfiesPzs": t.boolean().optional(),
            "defaultTableExpirationMs": t.string().optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "defaultPartitionExpirationMs": t.string().optional(),
            "defaultRoundingMode": t.string().optional(),
            "friendlyName": t.string().optional(),
            "storageBillingModel": t.string().optional(),
            "creationTime": t.string().optional(),
            "defaultEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ),
            "selfLink": t.string().optional(),
            "access": t.array(
                t.struct(
                    {
                        "view": t.proxy(renames["TableReferenceOut"]).optional(),
                        "iamMember": t.string().optional(),
                        "dataset": t.proxy(renames["DatasetAccessEntryOut"]).optional(),
                        "routine": t.proxy(renames["RoutineReferenceOut"]).optional(),
                        "role": t.string().optional(),
                        "groupByEmail": t.string().optional(),
                        "specialGroup": t.string().optional(),
                        "domain": t.string().optional(),
                        "userByEmail": t.string().optional(),
                    }
                )
            ).optional(),
            "maxTimeTravelHours": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "isCaseInsensitive": t.boolean().optional(),
            "lastModifiedTime": t.string().optional(),
            "defaultCollation": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "tags": t.array(
                t.struct(
                    {"tagValue": t.string().optional(), "tagKey": t.string().optional()}
                )
            ).optional(),
            "kind": t.string().optional(),
            "datasetReference": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["MlStatisticsIn"] = t.struct(
        {
            "iterationResults": t.array(
                t.proxy(renames["IterationResultIn"])
            ).optional(),
            "maxIterations": t.string().optional(),
        }
    ).named(renames["MlStatisticsIn"])
    types["MlStatisticsOut"] = t.struct(
        {
            "iterationResults": t.array(
                t.proxy(renames["IterationResultOut"])
            ).optional(),
            "maxIterations": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MlStatisticsOut"])

    functions = {}
    functions["tabledataList"] = bigquery.post(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll",
        t.struct(
            {
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "ignoreUnknownValues": t.boolean().optional(),
                "templateSuffix": t.string().optional(),
                "skipInvalidRows": t.boolean().optional(),
                "kind": t.string().optional(),
                "rows": t.array(
                    t.struct(
                        {
                            "insertId": t.string().optional(),
                            "json": t.proxy(renames["JsonObjectIn"]).optional(),
                        }
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableDataInsertAllResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tabledataInsertAll"] = bigquery.post(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll",
        t.struct(
            {
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "ignoreUnknownValues": t.boolean().optional(),
                "templateSuffix": t.string().optional(),
                "skipInvalidRows": t.boolean().optional(),
                "kind": t.string().optional(),
                "rows": t.array(
                    t.struct(
                        {
                            "insertId": t.string().optional(),
                            "json": t.proxy(renames["JsonObjectIn"]).optional(),
                        }
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableDataInsertAllResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["modelsGet"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}/models/{modelId}",
        t.struct(
            {
                "projectId": t.string(),
                "modelId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["modelsPatch"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}/models/{modelId}",
        t.struct(
            {
                "projectId": t.string(),
                "modelId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["modelsList"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}/models/{modelId}",
        t.struct(
            {
                "projectId": t.string(),
                "modelId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["modelsDelete"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}/models/{modelId}",
        t.struct(
            {
                "projectId": t.string(),
                "modelId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesInsert"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesSetIamPolicy"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesGet"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesTestIamPermissions"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesList"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesUpdate"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesDelete"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesGetIamPolicy"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesPatch"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "autodetect_schema": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "tableId": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "numLongTermLogicalBytes": t.string().optional(),
                "description": t.string().optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "lastModifiedTime": t.string().optional(),
                "friendlyName": t.string().optional(),
                "numRows": t.string().optional(),
                "numLongTermPhysicalBytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numPartitions": t.string().optional(),
                "numActiveLogicalBytes": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "numTotalPhysicalBytes": t.string().optional(),
                "tableConstraints": t.proxy(renames["TableConstraintsIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "id": t.string().optional(),
                "numTotalLogicalBytes": t.string().optional(),
                "selfLink": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "numActivePhysicalBytes": t.string().optional(),
                "numTimeTravelPhysicalBytes": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "creationTime": t.string().optional(),
                "etag": t.string().optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "expirationTime": t.string().optional(),
                "location": t.string().optional(),
                "numBytes": t.string().optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "numLongTermBytes": t.string().optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "defaultRoundingMode": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsGetQueryResults"] = bigquery.post(
        "projects/{projectId}/jobs",
        t.struct(
            {
                "projectId": t.string().optional(),
                "user_email": t.string().optional(),
                "selfLink": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.proxy(renames["JobStatusIn"]).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsCancel"] = bigquery.post(
        "projects/{projectId}/jobs",
        t.struct(
            {
                "projectId": t.string().optional(),
                "user_email": t.string().optional(),
                "selfLink": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.proxy(renames["JobStatusIn"]).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsQuery"] = bigquery.post(
        "projects/{projectId}/jobs",
        t.struct(
            {
                "projectId": t.string().optional(),
                "user_email": t.string().optional(),
                "selfLink": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.proxy(renames["JobStatusIn"]).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsGet"] = bigquery.post(
        "projects/{projectId}/jobs",
        t.struct(
            {
                "projectId": t.string().optional(),
                "user_email": t.string().optional(),
                "selfLink": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.proxy(renames["JobStatusIn"]).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsList"] = bigquery.post(
        "projects/{projectId}/jobs",
        t.struct(
            {
                "projectId": t.string().optional(),
                "user_email": t.string().optional(),
                "selfLink": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.proxy(renames["JobStatusIn"]).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsDelete"] = bigquery.post(
        "projects/{projectId}/jobs",
        t.struct(
            {
                "projectId": t.string().optional(),
                "user_email": t.string().optional(),
                "selfLink": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.proxy(renames["JobStatusIn"]).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsInsert"] = bigquery.post(
        "projects/{projectId}/jobs",
        t.struct(
            {
                "projectId": t.string().optional(),
                "user_email": t.string().optional(),
                "selfLink": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.proxy(renames["JobStatusIn"]).optional(),
                "id": t.string().optional(),
                "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = bigquery.get(
        "projects/{projectId}/serviceAccount",
        t.struct({"projectId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GetServiceAccountResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetServiceAccount"] = bigquery.get(
        "projects/{projectId}/serviceAccount",
        t.struct({"projectId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GetServiceAccountResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsPatch"] = bigquery.get(
        "projects/{projectId}/datasets",
        t.struct(
            {
                "projectId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "all": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsUpdate"] = bigquery.get(
        "projects/{projectId}/datasets",
        t.struct(
            {
                "projectId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "all": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsDelete"] = bigquery.get(
        "projects/{projectId}/datasets",
        t.struct(
            {
                "projectId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "all": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsInsert"] = bigquery.get(
        "projects/{projectId}/datasets",
        t.struct(
            {
                "projectId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "all": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsGet"] = bigquery.get(
        "projects/{projectId}/datasets",
        t.struct(
            {
                "projectId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "all": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsList"] = bigquery.get(
        "projects/{projectId}/datasets",
        t.struct(
            {
                "projectId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "all": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["rowAccessPoliciesGetIamPolicy"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "projectId": t.string(),
                "pageSize": t.integer().optional(),
                "tableId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["rowAccessPoliciesSetIamPolicy"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "projectId": t.string(),
                "pageSize": t.integer().optional(),
                "tableId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["rowAccessPoliciesTestIamPermissions"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "projectId": t.string(),
                "pageSize": t.integer().optional(),
                "tableId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["rowAccessPoliciesList"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "projectId": t.string(),
                "pageSize": t.integer().optional(),
                "tableId": t.string(),
                "datasetId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesUpdate"] = bigquery.post(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "datasetId": t.string(),
                "returnTableType": t.proxy(
                    renames["StandardSqlTableTypeIn"]
                ).optional(),
                "language": t.string().optional(),
                "returnType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
                "strictMode": t.boolean().optional(),
                "routineType": t.string(),
                "arguments": t.array(t.proxy(renames["ArgumentIn"])).optional(),
                "remoteFunctionOptions": t.proxy(
                    renames["RemoteFunctionOptionsIn"]
                ).optional(),
                "importedLibraries": t.array(t.string()).optional(),
                "definitionBody": t.string(),
                "determinismLevel": t.string().optional(),
                "routineReference": t.proxy(renames["RoutineReferenceIn"]),
                "description": t.string().optional(),
                "sparkOptions": t.proxy(renames["SparkOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RoutineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesGet"] = bigquery.post(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "datasetId": t.string(),
                "returnTableType": t.proxy(
                    renames["StandardSqlTableTypeIn"]
                ).optional(),
                "language": t.string().optional(),
                "returnType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
                "strictMode": t.boolean().optional(),
                "routineType": t.string(),
                "arguments": t.array(t.proxy(renames["ArgumentIn"])).optional(),
                "remoteFunctionOptions": t.proxy(
                    renames["RemoteFunctionOptionsIn"]
                ).optional(),
                "importedLibraries": t.array(t.string()).optional(),
                "definitionBody": t.string(),
                "determinismLevel": t.string().optional(),
                "routineReference": t.proxy(renames["RoutineReferenceIn"]),
                "description": t.string().optional(),
                "sparkOptions": t.proxy(renames["SparkOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RoutineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesList"] = bigquery.post(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "datasetId": t.string(),
                "returnTableType": t.proxy(
                    renames["StandardSqlTableTypeIn"]
                ).optional(),
                "language": t.string().optional(),
                "returnType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
                "strictMode": t.boolean().optional(),
                "routineType": t.string(),
                "arguments": t.array(t.proxy(renames["ArgumentIn"])).optional(),
                "remoteFunctionOptions": t.proxy(
                    renames["RemoteFunctionOptionsIn"]
                ).optional(),
                "importedLibraries": t.array(t.string()).optional(),
                "definitionBody": t.string(),
                "determinismLevel": t.string().optional(),
                "routineReference": t.proxy(renames["RoutineReferenceIn"]),
                "description": t.string().optional(),
                "sparkOptions": t.proxy(renames["SparkOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RoutineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesDelete"] = bigquery.post(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "datasetId": t.string(),
                "returnTableType": t.proxy(
                    renames["StandardSqlTableTypeIn"]
                ).optional(),
                "language": t.string().optional(),
                "returnType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
                "strictMode": t.boolean().optional(),
                "routineType": t.string(),
                "arguments": t.array(t.proxy(renames["ArgumentIn"])).optional(),
                "remoteFunctionOptions": t.proxy(
                    renames["RemoteFunctionOptionsIn"]
                ).optional(),
                "importedLibraries": t.array(t.string()).optional(),
                "definitionBody": t.string(),
                "determinismLevel": t.string().optional(),
                "routineReference": t.proxy(renames["RoutineReferenceIn"]),
                "description": t.string().optional(),
                "sparkOptions": t.proxy(renames["SparkOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RoutineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesInsert"] = bigquery.post(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "datasetId": t.string(),
                "returnTableType": t.proxy(
                    renames["StandardSqlTableTypeIn"]
                ).optional(),
                "language": t.string().optional(),
                "returnType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
                "strictMode": t.boolean().optional(),
                "routineType": t.string(),
                "arguments": t.array(t.proxy(renames["ArgumentIn"])).optional(),
                "remoteFunctionOptions": t.proxy(
                    renames["RemoteFunctionOptionsIn"]
                ).optional(),
                "importedLibraries": t.array(t.string()).optional(),
                "definitionBody": t.string(),
                "determinismLevel": t.string().optional(),
                "routineReference": t.proxy(renames["RoutineReferenceIn"]),
                "description": t.string().optional(),
                "sparkOptions": t.proxy(renames["SparkOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RoutineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigquery", renames=renames, types=Box(types), functions=Box(functions)
    )
