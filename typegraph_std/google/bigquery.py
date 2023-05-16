from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_bigquery() -> Import:
    bigquery = HTTPRuntime("https://bigquery.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigquery_1_ErrorResponse",
        "ArimaModelInfoIn": "_bigquery_2_ArimaModelInfoIn",
        "ArimaModelInfoOut": "_bigquery_3_ArimaModelInfoOut",
        "HparamSearchSpacesIn": "_bigquery_4_HparamSearchSpacesIn",
        "HparamSearchSpacesOut": "_bigquery_5_HparamSearchSpacesOut",
        "StandardSqlTableTypeIn": "_bigquery_6_StandardSqlTableTypeIn",
        "StandardSqlTableTypeOut": "_bigquery_7_StandardSqlTableTypeOut",
        "DataMaskingStatisticsIn": "_bigquery_8_DataMaskingStatisticsIn",
        "DataMaskingStatisticsOut": "_bigquery_9_DataMaskingStatisticsOut",
        "QueryTimelineSampleIn": "_bigquery_10_QueryTimelineSampleIn",
        "QueryTimelineSampleOut": "_bigquery_11_QueryTimelineSampleOut",
        "TableRowIn": "_bigquery_12_TableRowIn",
        "TableRowOut": "_bigquery_13_TableRowOut",
        "AvroOptionsIn": "_bigquery_14_AvroOptionsIn",
        "AvroOptionsOut": "_bigquery_15_AvroOptionsOut",
        "JobConfigurationIn": "_bigquery_16_JobConfigurationIn",
        "JobConfigurationOut": "_bigquery_17_JobConfigurationOut",
        "MaterializedViewDefinitionIn": "_bigquery_18_MaterializedViewDefinitionIn",
        "MaterializedViewDefinitionOut": "_bigquery_19_MaterializedViewDefinitionOut",
        "AuditLogConfigIn": "_bigquery_20_AuditLogConfigIn",
        "AuditLogConfigOut": "_bigquery_21_AuditLogConfigOut",
        "DestinationTablePropertiesIn": "_bigquery_22_DestinationTablePropertiesIn",
        "DestinationTablePropertiesOut": "_bigquery_23_DestinationTablePropertiesOut",
        "UserDefinedFunctionResourceIn": "_bigquery_24_UserDefinedFunctionResourceIn",
        "UserDefinedFunctionResourceOut": "_bigquery_25_UserDefinedFunctionResourceOut",
        "ErrorProtoIn": "_bigquery_26_ErrorProtoIn",
        "ErrorProtoOut": "_bigquery_27_ErrorProtoOut",
        "IntHparamSearchSpaceIn": "_bigquery_28_IntHparamSearchSpaceIn",
        "IntHparamSearchSpaceOut": "_bigquery_29_IntHparamSearchSpaceOut",
        "SetIamPolicyRequestIn": "_bigquery_30_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_bigquery_31_SetIamPolicyRequestOut",
        "DoubleHparamSearchSpaceIn": "_bigquery_32_DoubleHparamSearchSpaceIn",
        "DoubleHparamSearchSpaceOut": "_bigquery_33_DoubleHparamSearchSpaceOut",
        "BiEngineReasonIn": "_bigquery_34_BiEngineReasonIn",
        "BiEngineReasonOut": "_bigquery_35_BiEngineReasonOut",
        "MlStatisticsIn": "_bigquery_36_MlStatisticsIn",
        "MlStatisticsOut": "_bigquery_37_MlStatisticsOut",
        "JobConfigurationExtractIn": "_bigquery_38_JobConfigurationExtractIn",
        "JobConfigurationExtractOut": "_bigquery_39_JobConfigurationExtractOut",
        "FeatureValueIn": "_bigquery_40_FeatureValueIn",
        "FeatureValueOut": "_bigquery_41_FeatureValueOut",
        "DatasetListIn": "_bigquery_42_DatasetListIn",
        "DatasetListOut": "_bigquery_43_DatasetListOut",
        "JobStatusIn": "_bigquery_44_JobStatusIn",
        "JobStatusOut": "_bigquery_45_JobStatusOut",
        "BqmlIterationResultIn": "_bigquery_46_BqmlIterationResultIn",
        "BqmlIterationResultOut": "_bigquery_47_BqmlIterationResultOut",
        "ClusteringMetricsIn": "_bigquery_48_ClusteringMetricsIn",
        "ClusteringMetricsOut": "_bigquery_49_ClusteringMetricsOut",
        "TransactionInfoIn": "_bigquery_50_TransactionInfoIn",
        "TransactionInfoOut": "_bigquery_51_TransactionInfoOut",
        "ViewDefinitionIn": "_bigquery_52_ViewDefinitionIn",
        "ViewDefinitionOut": "_bigquery_53_ViewDefinitionOut",
        "SparkStatisticsIn": "_bigquery_54_SparkStatisticsIn",
        "SparkStatisticsOut": "_bigquery_55_SparkStatisticsOut",
        "ExplainQueryStepIn": "_bigquery_56_ExplainQueryStepIn",
        "ExplainQueryStepOut": "_bigquery_57_ExplainQueryStepOut",
        "CategoricalValueIn": "_bigquery_58_CategoricalValueIn",
        "CategoricalValueOut": "_bigquery_59_CategoricalValueOut",
        "ExplainQueryStageIn": "_bigquery_60_ExplainQueryStageIn",
        "ExplainQueryStageOut": "_bigquery_61_ExplainQueryStageOut",
        "CsvOptionsIn": "_bigquery_62_CsvOptionsIn",
        "CsvOptionsOut": "_bigquery_63_CsvOptionsOut",
        "AuditConfigIn": "_bigquery_64_AuditConfigIn",
        "AuditConfigOut": "_bigquery_65_AuditConfigOut",
        "PolicyIn": "_bigquery_66_PolicyIn",
        "PolicyOut": "_bigquery_67_PolicyOut",
        "RankingMetricsIn": "_bigquery_68_RankingMetricsIn",
        "RankingMetricsOut": "_bigquery_69_RankingMetricsOut",
        "ConnectionPropertyIn": "_bigquery_70_ConnectionPropertyIn",
        "ConnectionPropertyOut": "_bigquery_71_ConnectionPropertyOut",
        "ArimaCoefficientsIn": "_bigquery_72_ArimaCoefficientsIn",
        "ArimaCoefficientsOut": "_bigquery_73_ArimaCoefficientsOut",
        "ScriptStackFrameIn": "_bigquery_74_ScriptStackFrameIn",
        "ScriptStackFrameOut": "_bigquery_75_ScriptStackFrameOut",
        "ModelIn": "_bigquery_76_ModelIn",
        "ModelOut": "_bigquery_77_ModelOut",
        "ModelDefinitionIn": "_bigquery_78_ModelDefinitionIn",
        "ModelDefinitionOut": "_bigquery_79_ModelDefinitionOut",
        "RowLevelSecurityStatisticsIn": "_bigquery_80_RowLevelSecurityStatisticsIn",
        "RowLevelSecurityStatisticsOut": "_bigquery_81_RowLevelSecurityStatisticsOut",
        "StandardSqlDataTypeIn": "_bigquery_82_StandardSqlDataTypeIn",
        "StandardSqlDataTypeOut": "_bigquery_83_StandardSqlDataTypeOut",
        "SparkLoggingInfoIn": "_bigquery_84_SparkLoggingInfoIn",
        "SparkLoggingInfoOut": "_bigquery_85_SparkLoggingInfoOut",
        "TableCellIn": "_bigquery_86_TableCellIn",
        "TableCellOut": "_bigquery_87_TableCellOut",
        "ExternalDataConfigurationIn": "_bigquery_88_ExternalDataConfigurationIn",
        "ExternalDataConfigurationOut": "_bigquery_89_ExternalDataConfigurationOut",
        "TableDataListIn": "_bigquery_90_TableDataListIn",
        "TableDataListOut": "_bigquery_91_TableDataListOut",
        "IndexUnusedReasonIn": "_bigquery_92_IndexUnusedReasonIn",
        "IndexUnusedReasonOut": "_bigquery_93_IndexUnusedReasonOut",
        "ArimaOrderIn": "_bigquery_94_ArimaOrderIn",
        "ArimaOrderOut": "_bigquery_95_ArimaOrderOut",
        "GetServiceAccountResponseIn": "_bigquery_96_GetServiceAccountResponseIn",
        "GetServiceAccountResponseOut": "_bigquery_97_GetServiceAccountResponseOut",
        "ConfusionMatrixIn": "_bigquery_98_ConfusionMatrixIn",
        "ConfusionMatrixOut": "_bigquery_99_ConfusionMatrixOut",
        "TrainingOptionsIn": "_bigquery_100_TrainingOptionsIn",
        "TrainingOptionsOut": "_bigquery_101_TrainingOptionsOut",
        "BigtableColumnFamilyIn": "_bigquery_102_BigtableColumnFamilyIn",
        "BigtableColumnFamilyOut": "_bigquery_103_BigtableColumnFamilyOut",
        "DmlStatisticsIn": "_bigquery_104_DmlStatisticsIn",
        "DmlStatisticsOut": "_bigquery_105_DmlStatisticsOut",
        "IntArrayHparamSearchSpaceIn": "_bigquery_106_IntArrayHparamSearchSpaceIn",
        "IntArrayHparamSearchSpaceOut": "_bigquery_107_IntArrayHparamSearchSpaceOut",
        "CategoryCountIn": "_bigquery_108_CategoryCountIn",
        "CategoryCountOut": "_bigquery_109_CategoryCountOut",
        "QueryResponseIn": "_bigquery_110_QueryResponseIn",
        "QueryResponseOut": "_bigquery_111_QueryResponseOut",
        "EntryIn": "_bigquery_112_EntryIn",
        "EntryOut": "_bigquery_113_EntryOut",
        "BigtableOptionsIn": "_bigquery_114_BigtableOptionsIn",
        "BigtableOptionsOut": "_bigquery_115_BigtableOptionsOut",
        "ArimaFittingMetricsIn": "_bigquery_116_ArimaFittingMetricsIn",
        "ArimaFittingMetricsOut": "_bigquery_117_ArimaFittingMetricsOut",
        "BinaryConfusionMatrixIn": "_bigquery_118_BinaryConfusionMatrixIn",
        "BinaryConfusionMatrixOut": "_bigquery_119_BinaryConfusionMatrixOut",
        "SnapshotDefinitionIn": "_bigquery_120_SnapshotDefinitionIn",
        "SnapshotDefinitionOut": "_bigquery_121_SnapshotDefinitionOut",
        "DimensionalityReductionMetricsIn": "_bigquery_122_DimensionalityReductionMetricsIn",
        "DimensionalityReductionMetricsOut": "_bigquery_123_DimensionalityReductionMetricsOut",
        "TimePartitioningIn": "_bigquery_124_TimePartitioningIn",
        "TimePartitioningOut": "_bigquery_125_TimePartitioningOut",
        "ArimaSingleModelForecastingMetricsIn": "_bigquery_126_ArimaSingleModelForecastingMetricsIn",
        "ArimaSingleModelForecastingMetricsOut": "_bigquery_127_ArimaSingleModelForecastingMetricsOut",
        "HparamTuningTrialIn": "_bigquery_128_HparamTuningTrialIn",
        "HparamTuningTrialOut": "_bigquery_129_HparamTuningTrialOut",
        "ClusterIn": "_bigquery_130_ClusterIn",
        "ClusterOut": "_bigquery_131_ClusterOut",
        "ArimaForecastingMetricsIn": "_bigquery_132_ArimaForecastingMetricsIn",
        "ArimaForecastingMetricsOut": "_bigquery_133_ArimaForecastingMetricsOut",
        "GlobalExplanationIn": "_bigquery_134_GlobalExplanationIn",
        "GlobalExplanationOut": "_bigquery_135_GlobalExplanationOut",
        "ProjectReferenceIn": "_bigquery_136_ProjectReferenceIn",
        "ProjectReferenceOut": "_bigquery_137_ProjectReferenceOut",
        "JobReferenceIn": "_bigquery_138_JobReferenceIn",
        "JobReferenceOut": "_bigquery_139_JobReferenceOut",
        "EncryptionConfigurationIn": "_bigquery_140_EncryptionConfigurationIn",
        "EncryptionConfigurationOut": "_bigquery_141_EncryptionConfigurationOut",
        "QueryParameterValueIn": "_bigquery_142_QueryParameterValueIn",
        "QueryParameterValueOut": "_bigquery_143_QueryParameterValueOut",
        "JobConfigurationLoadIn": "_bigquery_144_JobConfigurationLoadIn",
        "JobConfigurationLoadOut": "_bigquery_145_JobConfigurationLoadOut",
        "RowAccessPolicyReferenceIn": "_bigquery_146_RowAccessPolicyReferenceIn",
        "RowAccessPolicyReferenceOut": "_bigquery_147_RowAccessPolicyReferenceOut",
        "StandardSqlFieldIn": "_bigquery_148_StandardSqlFieldIn",
        "StandardSqlFieldOut": "_bigquery_149_StandardSqlFieldOut",
        "PrincipalComponentInfoIn": "_bigquery_150_PrincipalComponentInfoIn",
        "PrincipalComponentInfoOut": "_bigquery_151_PrincipalComponentInfoOut",
        "RegressionMetricsIn": "_bigquery_152_RegressionMetricsIn",
        "RegressionMetricsOut": "_bigquery_153_RegressionMetricsOut",
        "JobListIn": "_bigquery_154_JobListIn",
        "JobListOut": "_bigquery_155_JobListOut",
        "TableFieldSchemaIn": "_bigquery_156_TableFieldSchemaIn",
        "TableFieldSchemaOut": "_bigquery_157_TableFieldSchemaOut",
        "IntRangeIn": "_bigquery_158_IntRangeIn",
        "IntRangeOut": "_bigquery_159_IntRangeOut",
        "SessionInfoIn": "_bigquery_160_SessionInfoIn",
        "SessionInfoOut": "_bigquery_161_SessionInfoOut",
        "BinaryClassificationMetricsIn": "_bigquery_162_BinaryClassificationMetricsIn",
        "BinaryClassificationMetricsOut": "_bigquery_163_BinaryClassificationMetricsOut",
        "MultiClassClassificationMetricsIn": "_bigquery_164_MultiClassClassificationMetricsIn",
        "MultiClassClassificationMetricsOut": "_bigquery_165_MultiClassClassificationMetricsOut",
        "SearchStatisticsIn": "_bigquery_166_SearchStatisticsIn",
        "SearchStatisticsOut": "_bigquery_167_SearchStatisticsOut",
        "JobConfigurationQueryIn": "_bigquery_168_JobConfigurationQueryIn",
        "JobConfigurationQueryOut": "_bigquery_169_JobConfigurationQueryOut",
        "CloneDefinitionIn": "_bigquery_170_CloneDefinitionIn",
        "CloneDefinitionOut": "_bigquery_171_CloneDefinitionOut",
        "JobCancelResponseIn": "_bigquery_172_JobCancelResponseIn",
        "JobCancelResponseOut": "_bigquery_173_JobCancelResponseOut",
        "ParquetOptionsIn": "_bigquery_174_ParquetOptionsIn",
        "ParquetOptionsOut": "_bigquery_175_ParquetOptionsOut",
        "IntCandidatesIn": "_bigquery_176_IntCandidatesIn",
        "IntCandidatesOut": "_bigquery_177_IntCandidatesOut",
        "TableReferenceIn": "_bigquery_178_TableReferenceIn",
        "TableReferenceOut": "_bigquery_179_TableReferenceOut",
        "ProjectListIn": "_bigquery_180_ProjectListIn",
        "ProjectListOut": "_bigquery_181_ProjectListOut",
        "StringHparamSearchSpaceIn": "_bigquery_182_StringHparamSearchSpaceIn",
        "StringHparamSearchSpaceOut": "_bigquery_183_StringHparamSearchSpaceOut",
        "DatasetAccessEntryIn": "_bigquery_184_DatasetAccessEntryIn",
        "DatasetAccessEntryOut": "_bigquery_185_DatasetAccessEntryOut",
        "ArimaResultIn": "_bigquery_186_ArimaResultIn",
        "ArimaResultOut": "_bigquery_187_ArimaResultOut",
        "TrainingRunIn": "_bigquery_188_TrainingRunIn",
        "TrainingRunOut": "_bigquery_189_TrainingRunOut",
        "JobStatistics4In": "_bigquery_190_JobStatistics4In",
        "JobStatistics4Out": "_bigquery_191_JobStatistics4Out",
        "StandardSqlStructTypeIn": "_bigquery_192_StandardSqlStructTypeIn",
        "StandardSqlStructTypeOut": "_bigquery_193_StandardSqlStructTypeOut",
        "DataSplitResultIn": "_bigquery_194_DataSplitResultIn",
        "DataSplitResultOut": "_bigquery_195_DataSplitResultOut",
        "ExprIn": "_bigquery_196_ExprIn",
        "ExprOut": "_bigquery_197_ExprOut",
        "RowIn": "_bigquery_198_RowIn",
        "RowOut": "_bigquery_199_RowOut",
        "JobStatistics3In": "_bigquery_200_JobStatistics3In",
        "JobStatistics3Out": "_bigquery_201_JobStatistics3Out",
        "TableDataInsertAllResponseIn": "_bigquery_202_TableDataInsertAllResponseIn",
        "TableDataInsertAllResponseOut": "_bigquery_203_TableDataInsertAllResponseOut",
        "RoutineReferenceIn": "_bigquery_204_RoutineReferenceIn",
        "RoutineReferenceOut": "_bigquery_205_RoutineReferenceOut",
        "ListModelsResponseIn": "_bigquery_206_ListModelsResponseIn",
        "ListModelsResponseOut": "_bigquery_207_ListModelsResponseOut",
        "ListRoutinesResponseIn": "_bigquery_208_ListRoutinesResponseIn",
        "ListRoutinesResponseOut": "_bigquery_209_ListRoutinesResponseOut",
        "JobConfigurationTableCopyIn": "_bigquery_210_JobConfigurationTableCopyIn",
        "JobConfigurationTableCopyOut": "_bigquery_211_JobConfigurationTableCopyOut",
        "BindingIn": "_bigquery_212_BindingIn",
        "BindingOut": "_bigquery_213_BindingOut",
        "ExplanationIn": "_bigquery_214_ExplanationIn",
        "ExplanationOut": "_bigquery_215_ExplanationOut",
        "IterationResultIn": "_bigquery_216_IterationResultIn",
        "IterationResultOut": "_bigquery_217_IterationResultOut",
        "TestIamPermissionsRequestIn": "_bigquery_218_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_bigquery_219_TestIamPermissionsRequestOut",
        "ListRowAccessPoliciesResponseIn": "_bigquery_220_ListRowAccessPoliciesResponseIn",
        "ListRowAccessPoliciesResponseOut": "_bigquery_221_ListRowAccessPoliciesResponseOut",
        "HivePartitioningOptionsIn": "_bigquery_222_HivePartitioningOptionsIn",
        "HivePartitioningOptionsOut": "_bigquery_223_HivePartitioningOptionsOut",
        "StreamingbufferIn": "_bigquery_224_StreamingbufferIn",
        "StreamingbufferOut": "_bigquery_225_StreamingbufferOut",
        "ArgumentIn": "_bigquery_226_ArgumentIn",
        "ArgumentOut": "_bigquery_227_ArgumentOut",
        "GoogleSheetsOptionsIn": "_bigquery_228_GoogleSheetsOptionsIn",
        "GoogleSheetsOptionsOut": "_bigquery_229_GoogleSheetsOptionsOut",
        "IntArrayIn": "_bigquery_230_IntArrayIn",
        "IntArrayOut": "_bigquery_231_IntArrayOut",
        "RemoteFunctionOptionsIn": "_bigquery_232_RemoteFunctionOptionsIn",
        "RemoteFunctionOptionsOut": "_bigquery_233_RemoteFunctionOptionsOut",
        "DoubleRangeIn": "_bigquery_234_DoubleRangeIn",
        "DoubleRangeOut": "_bigquery_235_DoubleRangeOut",
        "TestIamPermissionsResponseIn": "_bigquery_236_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_bigquery_237_TestIamPermissionsResponseOut",
        "BiEngineStatisticsIn": "_bigquery_238_BiEngineStatisticsIn",
        "BiEngineStatisticsOut": "_bigquery_239_BiEngineStatisticsOut",
        "TableSchemaIn": "_bigquery_240_TableSchemaIn",
        "TableSchemaOut": "_bigquery_241_TableSchemaOut",
        "QueryParameterIn": "_bigquery_242_QueryParameterIn",
        "QueryParameterOut": "_bigquery_243_QueryParameterOut",
        "ScriptStatisticsIn": "_bigquery_244_ScriptStatisticsIn",
        "ScriptStatisticsOut": "_bigquery_245_ScriptStatisticsOut",
        "QueryParameterTypeIn": "_bigquery_246_QueryParameterTypeIn",
        "QueryParameterTypeOut": "_bigquery_247_QueryParameterTypeOut",
        "SparkOptionsIn": "_bigquery_248_SparkOptionsIn",
        "SparkOptionsOut": "_bigquery_249_SparkOptionsOut",
        "GetIamPolicyRequestIn": "_bigquery_250_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_bigquery_251_GetIamPolicyRequestOut",
        "RowAccessPolicyIn": "_bigquery_252_RowAccessPolicyIn",
        "RowAccessPolicyOut": "_bigquery_253_RowAccessPolicyOut",
        "ClusteringIn": "_bigquery_254_ClusteringIn",
        "ClusteringOut": "_bigquery_255_ClusteringOut",
        "GetPolicyOptionsIn": "_bigquery_256_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_bigquery_257_GetPolicyOptionsOut",
        "JobStatistics5In": "_bigquery_258_JobStatistics5In",
        "JobStatistics5Out": "_bigquery_259_JobStatistics5Out",
        "ClusterInfoIn": "_bigquery_260_ClusterInfoIn",
        "ClusterInfoOut": "_bigquery_261_ClusterInfoOut",
        "BigQueryModelTrainingIn": "_bigquery_262_BigQueryModelTrainingIn",
        "BigQueryModelTrainingOut": "_bigquery_263_BigQueryModelTrainingOut",
        "RemoteModelInfoIn": "_bigquery_264_RemoteModelInfoIn",
        "RemoteModelInfoOut": "_bigquery_265_RemoteModelInfoOut",
        "EvaluationMetricsIn": "_bigquery_266_EvaluationMetricsIn",
        "EvaluationMetricsOut": "_bigquery_267_EvaluationMetricsOut",
        "TableDataInsertAllRequestIn": "_bigquery_268_TableDataInsertAllRequestIn",
        "TableDataInsertAllRequestOut": "_bigquery_269_TableDataInsertAllRequestOut",
        "JobStatistics2In": "_bigquery_270_JobStatistics2In",
        "JobStatistics2Out": "_bigquery_271_JobStatistics2Out",
        "DoubleCandidatesIn": "_bigquery_272_DoubleCandidatesIn",
        "DoubleCandidatesOut": "_bigquery_273_DoubleCandidatesOut",
        "ModelReferenceIn": "_bigquery_274_ModelReferenceIn",
        "ModelReferenceOut": "_bigquery_275_ModelReferenceOut",
        "TableIn": "_bigquery_276_TableIn",
        "TableOut": "_bigquery_277_TableOut",
        "JobStatisticsIn": "_bigquery_278_JobStatisticsIn",
        "JobStatisticsOut": "_bigquery_279_JobStatisticsOut",
        "AggregateClassificationMetricsIn": "_bigquery_280_AggregateClassificationMetricsIn",
        "AggregateClassificationMetricsOut": "_bigquery_281_AggregateClassificationMetricsOut",
        "BqmlTrainingRunIn": "_bigquery_282_BqmlTrainingRunIn",
        "BqmlTrainingRunOut": "_bigquery_283_BqmlTrainingRunOut",
        "LocationMetadataIn": "_bigquery_284_LocationMetadataIn",
        "LocationMetadataOut": "_bigquery_285_LocationMetadataOut",
        "RoutineIn": "_bigquery_286_RoutineIn",
        "RoutineOut": "_bigquery_287_RoutineOut",
        "JsonObjectIn": "_bigquery_288_JsonObjectIn",
        "JsonObjectOut": "_bigquery_289_JsonObjectOut",
        "JobIn": "_bigquery_290_JobIn",
        "JobOut": "_bigquery_291_JobOut",
        "DatasetReferenceIn": "_bigquery_292_DatasetReferenceIn",
        "DatasetReferenceOut": "_bigquery_293_DatasetReferenceOut",
        "TableListIn": "_bigquery_294_TableListIn",
        "TableListOut": "_bigquery_295_TableListOut",
        "QueryRequestIn": "_bigquery_296_QueryRequestIn",
        "QueryRequestOut": "_bigquery_297_QueryRequestOut",
        "BigtableColumnIn": "_bigquery_298_BigtableColumnIn",
        "BigtableColumnOut": "_bigquery_299_BigtableColumnOut",
        "GetQueryResultsResponseIn": "_bigquery_300_GetQueryResultsResponseIn",
        "GetQueryResultsResponseOut": "_bigquery_301_GetQueryResultsResponseOut",
        "DatasetIn": "_bigquery_302_DatasetIn",
        "DatasetOut": "_bigquery_303_DatasetOut",
        "RangePartitioningIn": "_bigquery_304_RangePartitioningIn",
        "RangePartitioningOut": "_bigquery_305_RangePartitioningOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ArimaModelInfoIn"] = t.struct(
        {
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderIn"]).optional(),
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesIds": t.array(t.string()).optional(),
            "arimaCoefficients": t.proxy(renames["ArimaCoefficientsIn"]).optional(),
            "arimaFittingMetrics": t.proxy(renames["ArimaFittingMetricsIn"]).optional(),
            "timeSeriesId": t.string().optional(),
            "hasDrift": t.boolean().optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "hasStepChanges": t.boolean().optional(),
            "hasSpikesAndDips": t.boolean().optional(),
        }
    ).named(renames["ArimaModelInfoIn"])
    types["ArimaModelInfoOut"] = t.struct(
        {
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderOut"]).optional(),
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesIds": t.array(t.string()).optional(),
            "arimaCoefficients": t.proxy(renames["ArimaCoefficientsOut"]).optional(),
            "arimaFittingMetrics": t.proxy(
                renames["ArimaFittingMetricsOut"]
            ).optional(),
            "timeSeriesId": t.string().optional(),
            "hasDrift": t.boolean().optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "hasStepChanges": t.boolean().optional(),
            "hasSpikesAndDips": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaModelInfoOut"])
    types["HparamSearchSpacesIn"] = t.struct(
        {
            "dropout": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "subsample": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "dartNormalizeType": t.proxy(
                renames["StringHparamSearchSpaceIn"]
            ).optional(),
            "numFactors": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "walsAlpha": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "treeMethod": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "hiddenUnits": t.proxy(renames["IntArrayHparamSearchSpaceIn"]).optional(),
            "activationFn": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "colsampleBynode": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "colsampleBytree": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "learnRate": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "colsampleBylevel": t.proxy(
                renames["DoubleHparamSearchSpaceIn"]
            ).optional(),
            "numParallelTree": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "maxTreeDepth": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "minTreeChildWeight": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "l2Reg": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "boosterType": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "batchSize": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "l1Reg": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
            "optimizer": t.proxy(renames["StringHparamSearchSpaceIn"]).optional(),
            "numClusters": t.proxy(renames["IntHparamSearchSpaceIn"]).optional(),
            "minSplitLoss": t.proxy(renames["DoubleHparamSearchSpaceIn"]).optional(),
        }
    ).named(renames["HparamSearchSpacesIn"])
    types["HparamSearchSpacesOut"] = t.struct(
        {
            "dropout": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "subsample": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "dartNormalizeType": t.proxy(
                renames["StringHparamSearchSpaceOut"]
            ).optional(),
            "numFactors": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "walsAlpha": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "treeMethod": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "hiddenUnits": t.proxy(renames["IntArrayHparamSearchSpaceOut"]).optional(),
            "activationFn": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "colsampleBynode": t.proxy(
                renames["DoubleHparamSearchSpaceOut"]
            ).optional(),
            "colsampleBytree": t.proxy(
                renames["DoubleHparamSearchSpaceOut"]
            ).optional(),
            "learnRate": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "colsampleBylevel": t.proxy(
                renames["DoubleHparamSearchSpaceOut"]
            ).optional(),
            "numParallelTree": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "maxTreeDepth": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "minTreeChildWeight": t.proxy(
                renames["IntHparamSearchSpaceOut"]
            ).optional(),
            "l2Reg": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "boosterType": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "batchSize": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "l1Reg": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "optimizer": t.proxy(renames["StringHparamSearchSpaceOut"]).optional(),
            "numClusters": t.proxy(renames["IntHparamSearchSpaceOut"]).optional(),
            "minSplitLoss": t.proxy(renames["DoubleHparamSearchSpaceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HparamSearchSpacesOut"])
    types["StandardSqlTableTypeIn"] = t.struct(
        {"columns": t.array(t.proxy(renames["StandardSqlFieldIn"])).optional()}
    ).named(renames["StandardSqlTableTypeIn"])
    types["StandardSqlTableTypeOut"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["StandardSqlFieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlTableTypeOut"])
    types["DataMaskingStatisticsIn"] = t.struct(
        {"dataMaskingApplied": t.boolean().optional()}
    ).named(renames["DataMaskingStatisticsIn"])
    types["DataMaskingStatisticsOut"] = t.struct(
        {
            "dataMaskingApplied": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataMaskingStatisticsOut"])
    types["QueryTimelineSampleIn"] = t.struct(
        {
            "activeUnits": t.string().optional(),
            "elapsedMs": t.string().optional(),
            "completedUnits": t.string().optional(),
            "totalSlotMs": t.string().optional(),
            "estimatedRunnableUnits": t.string().optional(),
            "pendingUnits": t.string().optional(),
        }
    ).named(renames["QueryTimelineSampleIn"])
    types["QueryTimelineSampleOut"] = t.struct(
        {
            "activeUnits": t.string().optional(),
            "elapsedMs": t.string().optional(),
            "completedUnits": t.string().optional(),
            "totalSlotMs": t.string().optional(),
            "estimatedRunnableUnits": t.string().optional(),
            "pendingUnits": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryTimelineSampleOut"])
    types["TableRowIn"] = t.struct(
        {"f": t.array(t.proxy(renames["TableCellIn"])).optional()}
    ).named(renames["TableRowIn"])
    types["TableRowOut"] = t.struct(
        {
            "f": t.array(t.proxy(renames["TableCellOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableRowOut"])
    types["AvroOptionsIn"] = t.struct(
        {"useAvroLogicalTypes": t.boolean().optional()}
    ).named(renames["AvroOptionsIn"])
    types["AvroOptionsOut"] = t.struct(
        {
            "useAvroLogicalTypes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvroOptionsOut"])
    types["JobConfigurationIn"] = t.struct(
        {
            "jobTimeoutMs": t.string().optional(),
            "query": t.proxy(renames["JobConfigurationQueryIn"]).optional(),
            "dryRun": t.boolean().optional(),
            "extract": t.proxy(renames["JobConfigurationExtractIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "jobType": t.string().optional(),
            "load": t.proxy(renames["JobConfigurationLoadIn"]).optional(),
            "copy": t.proxy(renames["JobConfigurationTableCopyIn"]).optional(),
        }
    ).named(renames["JobConfigurationIn"])
    types["JobConfigurationOut"] = t.struct(
        {
            "jobTimeoutMs": t.string().optional(),
            "query": t.proxy(renames["JobConfigurationQueryOut"]).optional(),
            "dryRun": t.boolean().optional(),
            "extract": t.proxy(renames["JobConfigurationExtractOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "jobType": t.string().optional(),
            "load": t.proxy(renames["JobConfigurationLoadOut"]).optional(),
            "copy": t.proxy(renames["JobConfigurationTableCopyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationOut"])
    types["MaterializedViewDefinitionIn"] = t.struct(
        {
            "enableRefresh": t.boolean().optional(),
            "lastRefreshTime": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "allow_non_incremental_definition": t.boolean().optional(),
            "refreshIntervalMs": t.string().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["MaterializedViewDefinitionIn"])
    types["MaterializedViewDefinitionOut"] = t.struct(
        {
            "enableRefresh": t.boolean().optional(),
            "lastRefreshTime": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "allow_non_incremental_definition": t.boolean().optional(),
            "refreshIntervalMs": t.string().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaterializedViewDefinitionOut"])
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
    types["DestinationTablePropertiesIn"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DestinationTablePropertiesIn"])
    types["DestinationTablePropertiesOut"] = t.struct(
        {
            "expirationTime": t.string().optional(),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationTablePropertiesOut"])
    types["UserDefinedFunctionResourceIn"] = t.struct(
        {"resourceUri": t.string().optional(), "inlineCode": t.string().optional()}
    ).named(renames["UserDefinedFunctionResourceIn"])
    types["UserDefinedFunctionResourceOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "inlineCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedFunctionResourceOut"])
    types["ErrorProtoIn"] = t.struct(
        {
            "message": t.string().optional(),
            "reason": t.string().optional(),
            "debugInfo": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ErrorProtoIn"])
    types["ErrorProtoOut"] = t.struct(
        {
            "message": t.string().optional(),
            "reason": t.string().optional(),
            "debugInfo": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorProtoOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["MlStatisticsIn"] = t.struct(
        {
            "maxIterations": t.string().optional(),
            "iterationResults": t.array(
                t.proxy(renames["IterationResultIn"])
            ).optional(),
        }
    ).named(renames["MlStatisticsIn"])
    types["MlStatisticsOut"] = t.struct(
        {
            "maxIterations": t.string().optional(),
            "iterationResults": t.array(
                t.proxy(renames["IterationResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MlStatisticsOut"])
    types["JobConfigurationExtractIn"] = t.struct(
        {
            "fieldDelimiter": t.string().optional(),
            "printHeader": t.boolean().optional(),
            "destinationUris": t.array(t.string()).optional(),
            "sourceTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "sourceModel": t.proxy(renames["ModelReferenceIn"]).optional(),
            "compression": t.string().optional(),
            "useAvroLogicalTypes": t.boolean().optional(),
            "destinationUri": t.string().optional(),
            "destinationFormat": t.string().optional(),
        }
    ).named(renames["JobConfigurationExtractIn"])
    types["JobConfigurationExtractOut"] = t.struct(
        {
            "fieldDelimiter": t.string().optional(),
            "printHeader": t.boolean().optional(),
            "destinationUris": t.array(t.string()).optional(),
            "sourceTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "sourceModel": t.proxy(renames["ModelReferenceOut"]).optional(),
            "compression": t.string().optional(),
            "useAvroLogicalTypes": t.boolean().optional(),
            "destinationUri": t.string().optional(),
            "destinationFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationExtractOut"])
    types["FeatureValueIn"] = t.struct(
        {
            "featureColumn": t.string().optional(),
            "categoricalValue": t.proxy(renames["CategoricalValueIn"]).optional(),
            "numericalValue": t.number().optional(),
        }
    ).named(renames["FeatureValueIn"])
    types["FeatureValueOut"] = t.struct(
        {
            "featureColumn": t.string().optional(),
            "categoricalValue": t.proxy(renames["CategoricalValueOut"]).optional(),
            "numericalValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureValueOut"])
    types["DatasetListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "datasets": t.array(
                t.struct(
                    {
                        "friendlyName": t.string().optional(),
                        "datasetReference": t.proxy(
                            renames["DatasetReferenceIn"]
                        ).optional(),
                        "kind": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "id": t.string().optional(),
                        "location": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["DatasetListIn"])
    types["DatasetListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "datasets": t.array(
                t.struct(
                    {
                        "friendlyName": t.string().optional(),
                        "datasetReference": t.proxy(
                            renames["DatasetReferenceOut"]
                        ).optional(),
                        "kind": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "id": t.string().optional(),
                        "location": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetListOut"])
    types["JobStatusIn"] = t.struct(
        {
            "errorResult": t.proxy(renames["ErrorProtoIn"]).optional(),
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
        }
    ).named(renames["JobStatusIn"])
    types["JobStatusOut"] = t.struct(
        {
            "errorResult": t.proxy(renames["ErrorProtoOut"]).optional(),
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatusOut"])
    types["BqmlIterationResultIn"] = t.struct(
        {
            "trainingLoss": t.number().optional(),
            "index": t.integer().optional(),
            "learnRate": t.number().optional(),
            "durationMs": t.string().optional(),
            "evalLoss": t.number().optional(),
        }
    ).named(renames["BqmlIterationResultIn"])
    types["BqmlIterationResultOut"] = t.struct(
        {
            "trainingLoss": t.number().optional(),
            "index": t.integer().optional(),
            "learnRate": t.number().optional(),
            "durationMs": t.string().optional(),
            "evalLoss": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BqmlIterationResultOut"])
    types["ClusteringMetricsIn"] = t.struct(
        {
            "daviesBouldinIndex": t.number().optional(),
            "meanSquaredDistance": t.number().optional(),
            "clusters": t.array(t.proxy(renames["ClusterIn"])).optional(),
        }
    ).named(renames["ClusteringMetricsIn"])
    types["ClusteringMetricsOut"] = t.struct(
        {
            "daviesBouldinIndex": t.number().optional(),
            "meanSquaredDistance": t.number().optional(),
            "clusters": t.array(t.proxy(renames["ClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusteringMetricsOut"])
    types["TransactionInfoIn"] = t.struct(
        {"transactionId": t.string().optional()}
    ).named(renames["TransactionInfoIn"])
    types["TransactionInfoOut"] = t.struct(
        {
            "transactionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransactionInfoOut"])
    types["ViewDefinitionIn"] = t.struct(
        {
            "useExplicitColumnNames": t.boolean().optional(),
            "useLegacySql": t.boolean().optional(),
            "query": t.string().optional(),
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceIn"])
            ).optional(),
        }
    ).named(renames["ViewDefinitionIn"])
    types["ViewDefinitionOut"] = t.struct(
        {
            "useExplicitColumnNames": t.boolean().optional(),
            "useLegacySql": t.boolean().optional(),
            "query": t.string().optional(),
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewDefinitionOut"])
    types["SparkStatisticsIn"] = t.struct(
        {
            "spark_job_location": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "spark_job_id": t.string().optional(),
            "logging_info": t.proxy(renames["SparkLoggingInfoIn"]).optional(),
        }
    ).named(renames["SparkStatisticsIn"])
    types["SparkStatisticsOut"] = t.struct(
        {
            "spark_job_location": t.string().optional(),
            "endpoints": t.struct({"_": t.string().optional()}).optional(),
            "spark_job_id": t.string().optional(),
            "logging_info": t.proxy(renames["SparkLoggingInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkStatisticsOut"])
    types["ExplainQueryStepIn"] = t.struct(
        {"substeps": t.array(t.string()).optional(), "kind": t.string().optional()}
    ).named(renames["ExplainQueryStepIn"])
    types["ExplainQueryStepOut"] = t.struct(
        {
            "substeps": t.array(t.string()).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplainQueryStepOut"])
    types["CategoricalValueIn"] = t.struct(
        {"categoryCounts": t.array(t.proxy(renames["CategoryCountIn"])).optional()}
    ).named(renames["CategoricalValueIn"])
    types["CategoricalValueOut"] = t.struct(
        {
            "categoryCounts": t.array(t.proxy(renames["CategoryCountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoricalValueOut"])
    types["ExplainQueryStageIn"] = t.struct(
        {
            "startMs": t.string().optional(),
            "steps": t.array(t.proxy(renames["ExplainQueryStepIn"])).optional(),
            "recordsWritten": t.string().optional(),
            "status": t.string().optional(),
            "computeRatioMax": t.number().optional(),
            "writeMsMax": t.string().optional(),
            "writeRatioMax": t.number().optional(),
            "shuffleOutputBytes": t.string().optional(),
            "writeRatioAvg": t.number().optional(),
            "waitRatioMax": t.number().optional(),
            "parallelInputs": t.string().optional(),
            "readMsMax": t.string().optional(),
            "computeRatioAvg": t.number().optional(),
            "readMsAvg": t.string().optional(),
            "writeMsAvg": t.string().optional(),
            "id": t.string().optional(),
            "waitMsAvg": t.string().optional(),
            "slotMs": t.string().optional(),
            "waitRatioAvg": t.number().optional(),
            "completedParallelInputs": t.string().optional(),
            "waitMsMax": t.string().optional(),
            "recordsRead": t.string().optional(),
            "inputStages": t.array(t.string()).optional(),
            "endMs": t.string().optional(),
            "name": t.string().optional(),
            "computeMsMax": t.string().optional(),
            "readRatioAvg": t.number().optional(),
            "computeMsAvg": t.string().optional(),
            "readRatioMax": t.number().optional(),
            "shuffleOutputBytesSpilled": t.string().optional(),
        }
    ).named(renames["ExplainQueryStageIn"])
    types["ExplainQueryStageOut"] = t.struct(
        {
            "startMs": t.string().optional(),
            "steps": t.array(t.proxy(renames["ExplainQueryStepOut"])).optional(),
            "recordsWritten": t.string().optional(),
            "status": t.string().optional(),
            "computeRatioMax": t.number().optional(),
            "writeMsMax": t.string().optional(),
            "writeRatioMax": t.number().optional(),
            "shuffleOutputBytes": t.string().optional(),
            "writeRatioAvg": t.number().optional(),
            "waitRatioMax": t.number().optional(),
            "parallelInputs": t.string().optional(),
            "readMsMax": t.string().optional(),
            "computeRatioAvg": t.number().optional(),
            "readMsAvg": t.string().optional(),
            "writeMsAvg": t.string().optional(),
            "id": t.string().optional(),
            "waitMsAvg": t.string().optional(),
            "slotMs": t.string().optional(),
            "waitRatioAvg": t.number().optional(),
            "completedParallelInputs": t.string().optional(),
            "waitMsMax": t.string().optional(),
            "recordsRead": t.string().optional(),
            "inputStages": t.array(t.string()).optional(),
            "endMs": t.string().optional(),
            "name": t.string().optional(),
            "computeMsMax": t.string().optional(),
            "readRatioAvg": t.number().optional(),
            "computeMsAvg": t.string().optional(),
            "readRatioMax": t.number().optional(),
            "shuffleOutputBytesSpilled": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExplainQueryStageOut"])
    types["CsvOptionsIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "null_marker": t.string().optional(),
            "quote": t.string().optional(),
            "skipLeadingRows": t.string().optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "fieldDelimiter": t.string().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "allowQuotedNewlines": t.boolean().optional(),
        }
    ).named(renames["CsvOptionsIn"])
    types["CsvOptionsOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "null_marker": t.string().optional(),
            "quote": t.string().optional(),
            "skipLeadingRows": t.string().optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "fieldDelimiter": t.string().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "allowQuotedNewlines": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CsvOptionsOut"])
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
    types["RankingMetricsIn"] = t.struct(
        {
            "meanSquaredError": t.number().optional(),
            "normalizedDiscountedCumulativeGain": t.number().optional(),
            "averageRank": t.number().optional(),
            "meanAveragePrecision": t.number().optional(),
        }
    ).named(renames["RankingMetricsIn"])
    types["RankingMetricsOut"] = t.struct(
        {
            "meanSquaredError": t.number().optional(),
            "normalizedDiscountedCumulativeGain": t.number().optional(),
            "averageRank": t.number().optional(),
            "meanAveragePrecision": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RankingMetricsOut"])
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
    types["ArimaCoefficientsIn"] = t.struct(
        {
            "autoRegressiveCoefficients": t.array(t.number()).optional(),
            "movingAverageCoefficients": t.array(t.number()).optional(),
            "interceptCoefficient": t.number().optional(),
        }
    ).named(renames["ArimaCoefficientsIn"])
    types["ArimaCoefficientsOut"] = t.struct(
        {
            "autoRegressiveCoefficients": t.array(t.number()).optional(),
            "movingAverageCoefficients": t.array(t.number()).optional(),
            "interceptCoefficient": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaCoefficientsOut"])
    types["ScriptStackFrameIn"] = t.struct(
        {
            "text": t.string().optional(),
            "startColumn": t.integer().optional(),
            "endLine": t.integer().optional(),
            "procedureId": t.string().optional(),
            "endColumn": t.integer().optional(),
            "startLine": t.integer().optional(),
        }
    ).named(renames["ScriptStackFrameIn"])
    types["ScriptStackFrameOut"] = t.struct(
        {
            "text": t.string().optional(),
            "startColumn": t.integer().optional(),
            "endLine": t.integer().optional(),
            "procedureId": t.string().optional(),
            "endColumn": t.integer().optional(),
            "startLine": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptStackFrameOut"])
    types["ModelIn"] = t.struct(
        {
            "trainingRuns": t.array(t.proxy(renames["TrainingRunIn"])).optional(),
            "bestTrialId": t.string().optional(),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "expirationTime": t.string().optional(),
            "description": t.string().optional(),
            "modelReference": t.proxy(renames["ModelReferenceIn"]),
            "friendlyName": t.string().optional(),
        }
    ).named(renames["ModelIn"])
    types["ModelOut"] = t.struct(
        {
            "modelType": t.string().optional(),
            "creationTime": t.string().optional(),
            "trainingRuns": t.array(t.proxy(renames["TrainingRunOut"])).optional(),
            "bestTrialId": t.string().optional(),
            "optimalTrialIds": t.array(t.string()).optional(),
            "hparamSearchSpaces": t.proxy(renames["HparamSearchSpacesOut"]).optional(),
            "location": t.string().optional(),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "lastModifiedTime": t.string().optional(),
            "featureColumns": t.array(
                t.proxy(renames["StandardSqlFieldOut"])
            ).optional(),
            "hparamTrials": t.array(
                t.proxy(renames["HparamTuningTrialOut"])
            ).optional(),
            "labelColumns": t.array(t.proxy(renames["StandardSqlFieldOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "remoteModelInfo": t.proxy(renames["RemoteModelInfoOut"]).optional(),
            "etag": t.string().optional(),
            "expirationTime": t.string().optional(),
            "description": t.string().optional(),
            "defaultTrialId": t.string().optional(),
            "modelReference": t.proxy(renames["ModelReferenceOut"]),
            "friendlyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelOut"])
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
    types["RowLevelSecurityStatisticsIn"] = t.struct(
        {"rowLevelSecurityApplied": t.boolean().optional()}
    ).named(renames["RowLevelSecurityStatisticsIn"])
    types["RowLevelSecurityStatisticsOut"] = t.struct(
        {
            "rowLevelSecurityApplied": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowLevelSecurityStatisticsOut"])
    types["StandardSqlDataTypeIn"] = t.struct(
        {
            "structType": t.proxy(renames["StandardSqlStructTypeIn"]).optional(),
            "arrayElementType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
            "typeKind": t.string(),
        }
    ).named(renames["StandardSqlDataTypeIn"])
    types["StandardSqlDataTypeOut"] = t.struct(
        {
            "structType": t.proxy(renames["StandardSqlStructTypeOut"]).optional(),
            "arrayElementType": t.proxy(renames["StandardSqlDataTypeOut"]).optional(),
            "typeKind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlDataTypeOut"])
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
    types["TableCellIn"] = t.struct(
        {"v": t.struct({"_": t.string().optional()})}
    ).named(renames["TableCellIn"])
    types["TableCellOut"] = t.struct(
        {
            "v": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableCellOut"])
    types["ExternalDataConfigurationIn"] = t.struct(
        {
            "maxBadRecords": t.integer().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "connectionId": t.string().optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsIn"]).optional(),
            "googleSheetsOptions": t.proxy(renames["GoogleSheetsOptionsIn"]).optional(),
            "sourceUris": t.array(t.string()).optional(),
            "objectMetadata": t.string().optional(),
            "autodetect": t.boolean().optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsIn"]
            ).optional(),
            "sourceFormat": t.string().optional(),
            "avroOptions": t.proxy(renames["AvroOptionsIn"]).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "csvOptions": t.proxy(renames["CsvOptionsIn"]).optional(),
            "metadataCacheMode": t.string().optional(),
            "bigtableOptions": t.proxy(renames["BigtableOptionsIn"]).optional(),
            "compression": t.string().optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
        }
    ).named(renames["ExternalDataConfigurationIn"])
    types["ExternalDataConfigurationOut"] = t.struct(
        {
            "maxBadRecords": t.integer().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "connectionId": t.string().optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsOut"]).optional(),
            "googleSheetsOptions": t.proxy(
                renames["GoogleSheetsOptionsOut"]
            ).optional(),
            "sourceUris": t.array(t.string()).optional(),
            "objectMetadata": t.string().optional(),
            "autodetect": t.boolean().optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsOut"]
            ).optional(),
            "sourceFormat": t.string().optional(),
            "avroOptions": t.proxy(renames["AvroOptionsOut"]).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "csvOptions": t.proxy(renames["CsvOptionsOut"]).optional(),
            "metadataCacheMode": t.string().optional(),
            "bigtableOptions": t.proxy(renames["BigtableOptionsOut"]).optional(),
            "compression": t.string().optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalDataConfigurationOut"])
    types["TableDataListIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "etag": t.string().optional(),
            "totalRows": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["TableDataListIn"])
    types["TableDataListOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "etag": t.string().optional(),
            "totalRows": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableDataListOut"])
    types["IndexUnusedReasonIn"] = t.struct(
        {
            "code": t.string().optional(),
            "index_name": t.string().optional(),
            "base_table": t.proxy(renames["TableReferenceIn"]).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["IndexUnusedReasonIn"])
    types["IndexUnusedReasonOut"] = t.struct(
        {
            "code": t.string().optional(),
            "index_name": t.string().optional(),
            "base_table": t.proxy(renames["TableReferenceOut"]).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IndexUnusedReasonOut"])
    types["ArimaOrderIn"] = t.struct(
        {
            "q": t.string().optional(),
            "d": t.string().optional(),
            "p": t.string().optional(),
        }
    ).named(renames["ArimaOrderIn"])
    types["ArimaOrderOut"] = t.struct(
        {
            "q": t.string().optional(),
            "d": t.string().optional(),
            "p": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaOrderOut"])
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
    types["TrainingOptionsIn"] = t.struct(
        {
            "tfVersion": t.string().optional(),
            "colorSpace": t.string().optional(),
            "learnRate": t.number().optional(),
            "autoArima": t.boolean().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderIn"]).optional(),
            "integratedGradientsNumSteps": t.string().optional(),
            "itemColumn": t.string().optional(),
            "numFactors": t.string().optional(),
            "instanceWeightColumn": t.string().optional(),
            "optimizationStrategy": t.string().optional(),
            "maxTimeSeriesLength": t.string().optional(),
            "colsampleBynode": t.number().optional(),
            "feedbackType": t.string().optional(),
            "labelClassWeights": t.struct({"_": t.string().optional()}).optional(),
            "autoArimaMinOrder": t.string().optional(),
            "batchSize": t.string().optional(),
            "minTreeChildWeight": t.string().optional(),
            "enableGlobalExplain": t.boolean().optional(),
            "holidayRegion": t.string().optional(),
            "learnRateStrategy": t.string().optional(),
            "warmStart": t.boolean().optional(),
            "numClusters": t.string().optional(),
            "earlyStop": t.boolean().optional(),
            "decomposeTimeSeries": t.boolean().optional(),
            "timeSeriesTimestampColumn": t.string().optional(),
            "numParallelTree": t.string().optional(),
            "l2Regularization": t.number().optional(),
            "timeSeriesIdColumns": t.array(t.string()).optional(),
            "dataFrequency": t.string().optional(),
            "timeSeriesDataColumn": t.string().optional(),
            "numTrials": t.string().optional(),
            "maxIterations": t.string().optional(),
            "hiddenUnits": t.array(t.string()).optional(),
            "lossType": t.string().optional(),
            "userColumn": t.string().optional(),
            "timeSeriesLengthFraction": t.number().optional(),
            "trendSmoothingWindowSize": t.string().optional(),
            "modelUri": t.string().optional(),
            "maxParallelTrials": t.string().optional(),
            "timeSeriesIdColumn": t.string().optional(),
            "xgboostVersion": t.string().optional(),
            "dropout": t.number().optional(),
            "walsAlpha": t.number().optional(),
            "dartNormalizeType": t.string().optional(),
            "kmeansInitializationColumn": t.string().optional(),
            "kmeansInitializationMethod": t.string().optional(),
            "minRelativeProgress": t.number().optional(),
            "treeMethod": t.string().optional(),
            "dataSplitEvalFraction": t.number().optional(),
            "includeDrift": t.boolean().optional(),
            "boosterType": t.string().optional(),
            "minSplitLoss": t.number().optional(),
            "distanceType": t.string().optional(),
            "l1Regularization": t.number().optional(),
            "preserveInputStructs": t.boolean().optional(),
            "sampledShapleyNumPaths": t.string().optional(),
            "autoArimaMaxOrder": t.string().optional(),
            "horizon": t.string().optional(),
            "initialLearnRate": t.number().optional(),
            "cleanSpikesAndDips": t.boolean().optional(),
            "subsample": t.number().optional(),
            "colsampleBylevel": t.number().optional(),
            "colsampleBytree": t.number().optional(),
            "minTimeSeriesLength": t.string().optional(),
            "calculatePValues": t.boolean().optional(),
            "inputLabelColumns": t.array(t.string()).optional(),
            "maxTreeDepth": t.string().optional(),
            "dataSplitColumn": t.string().optional(),
            "dataSplitMethod": t.string().optional(),
            "hparamTuningObjectives": t.array(t.string()).optional(),
            "adjustStepChanges": t.boolean().optional(),
        }
    ).named(renames["TrainingOptionsIn"])
    types["TrainingOptionsOut"] = t.struct(
        {
            "tfVersion": t.string().optional(),
            "colorSpace": t.string().optional(),
            "learnRate": t.number().optional(),
            "autoArima": t.boolean().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderOut"]).optional(),
            "integratedGradientsNumSteps": t.string().optional(),
            "itemColumn": t.string().optional(),
            "numFactors": t.string().optional(),
            "instanceWeightColumn": t.string().optional(),
            "optimizationStrategy": t.string().optional(),
            "maxTimeSeriesLength": t.string().optional(),
            "colsampleBynode": t.number().optional(),
            "feedbackType": t.string().optional(),
            "labelClassWeights": t.struct({"_": t.string().optional()}).optional(),
            "autoArimaMinOrder": t.string().optional(),
            "batchSize": t.string().optional(),
            "minTreeChildWeight": t.string().optional(),
            "enableGlobalExplain": t.boolean().optional(),
            "holidayRegion": t.string().optional(),
            "learnRateStrategy": t.string().optional(),
            "warmStart": t.boolean().optional(),
            "numClusters": t.string().optional(),
            "earlyStop": t.boolean().optional(),
            "decomposeTimeSeries": t.boolean().optional(),
            "timeSeriesTimestampColumn": t.string().optional(),
            "numParallelTree": t.string().optional(),
            "l2Regularization": t.number().optional(),
            "timeSeriesIdColumns": t.array(t.string()).optional(),
            "dataFrequency": t.string().optional(),
            "timeSeriesDataColumn": t.string().optional(),
            "numTrials": t.string().optional(),
            "maxIterations": t.string().optional(),
            "hiddenUnits": t.array(t.string()).optional(),
            "lossType": t.string().optional(),
            "userColumn": t.string().optional(),
            "timeSeriesLengthFraction": t.number().optional(),
            "trendSmoothingWindowSize": t.string().optional(),
            "modelUri": t.string().optional(),
            "maxParallelTrials": t.string().optional(),
            "timeSeriesIdColumn": t.string().optional(),
            "xgboostVersion": t.string().optional(),
            "dropout": t.number().optional(),
            "walsAlpha": t.number().optional(),
            "dartNormalizeType": t.string().optional(),
            "kmeansInitializationColumn": t.string().optional(),
            "kmeansInitializationMethod": t.string().optional(),
            "minRelativeProgress": t.number().optional(),
            "treeMethod": t.string().optional(),
            "dataSplitEvalFraction": t.number().optional(),
            "includeDrift": t.boolean().optional(),
            "boosterType": t.string().optional(),
            "minSplitLoss": t.number().optional(),
            "distanceType": t.string().optional(),
            "l1Regularization": t.number().optional(),
            "preserveInputStructs": t.boolean().optional(),
            "sampledShapleyNumPaths": t.string().optional(),
            "autoArimaMaxOrder": t.string().optional(),
            "horizon": t.string().optional(),
            "initialLearnRate": t.number().optional(),
            "cleanSpikesAndDips": t.boolean().optional(),
            "subsample": t.number().optional(),
            "colsampleBylevel": t.number().optional(),
            "colsampleBytree": t.number().optional(),
            "minTimeSeriesLength": t.string().optional(),
            "calculatePValues": t.boolean().optional(),
            "inputLabelColumns": t.array(t.string()).optional(),
            "maxTreeDepth": t.string().optional(),
            "dataSplitColumn": t.string().optional(),
            "dataSplitMethod": t.string().optional(),
            "hparamTuningObjectives": t.array(t.string()).optional(),
            "adjustStepChanges": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrainingOptionsOut"])
    types["BigtableColumnFamilyIn"] = t.struct(
        {
            "onlyReadLatest": t.boolean().optional(),
            "encoding": t.string().optional(),
            "columns": t.array(t.proxy(renames["BigtableColumnIn"])).optional(),
            "type": t.string().optional(),
            "familyId": t.string().optional(),
        }
    ).named(renames["BigtableColumnFamilyIn"])
    types["BigtableColumnFamilyOut"] = t.struct(
        {
            "onlyReadLatest": t.boolean().optional(),
            "encoding": t.string().optional(),
            "columns": t.array(t.proxy(renames["BigtableColumnOut"])).optional(),
            "type": t.string().optional(),
            "familyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigtableColumnFamilyOut"])
    types["DmlStatisticsIn"] = t.struct(
        {
            "updatedRowCount": t.string().optional(),
            "deletedRowCount": t.string().optional(),
            "insertedRowCount": t.string().optional(),
        }
    ).named(renames["DmlStatisticsIn"])
    types["DmlStatisticsOut"] = t.struct(
        {
            "updatedRowCount": t.string().optional(),
            "deletedRowCount": t.string().optional(),
            "insertedRowCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DmlStatisticsOut"])
    types["IntArrayHparamSearchSpaceIn"] = t.struct(
        {"candidates": t.array(t.proxy(renames["IntArrayIn"])).optional()}
    ).named(renames["IntArrayHparamSearchSpaceIn"])
    types["IntArrayHparamSearchSpaceOut"] = t.struct(
        {
            "candidates": t.array(t.proxy(renames["IntArrayOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntArrayHparamSearchSpaceOut"])
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
    types["QueryResponseIn"] = t.struct(
        {
            "cacheHit": t.boolean().optional(),
            "rows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "jobComplete": t.boolean().optional(),
            "totalRows": t.string().optional(),
            "totalBytesProcessed": t.string().optional(),
            "sessionInfo": t.proxy(renames["SessionInfoIn"]).optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsIn"]).optional(),
            "kind": t.string().optional(),
            "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["QueryResponseIn"])
    types["QueryResponseOut"] = t.struct(
        {
            "cacheHit": t.boolean().optional(),
            "rows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "jobComplete": t.boolean().optional(),
            "totalRows": t.string().optional(),
            "totalBytesProcessed": t.string().optional(),
            "sessionInfo": t.proxy(renames["SessionInfoOut"]).optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsOut"]).optional(),
            "kind": t.string().optional(),
            "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryResponseOut"])
    types["EntryIn"] = t.struct(
        {"predictedLabel": t.string().optional(), "itemCount": t.string().optional()}
    ).named(renames["EntryIn"])
    types["EntryOut"] = t.struct(
        {
            "predictedLabel": t.string().optional(),
            "itemCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntryOut"])
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
    types["BinaryConfusionMatrixIn"] = t.struct(
        {
            "falsePositives": t.string().optional(),
            "f1Score": t.number().optional(),
            "falseNegatives": t.string().optional(),
            "precision": t.number().optional(),
            "positiveClassThreshold": t.number().optional(),
            "truePositives": t.string().optional(),
            "recall": t.number().optional(),
            "trueNegatives": t.string().optional(),
            "accuracy": t.number().optional(),
        }
    ).named(renames["BinaryConfusionMatrixIn"])
    types["BinaryConfusionMatrixOut"] = t.struct(
        {
            "falsePositives": t.string().optional(),
            "f1Score": t.number().optional(),
            "falseNegatives": t.string().optional(),
            "precision": t.number().optional(),
            "positiveClassThreshold": t.number().optional(),
            "truePositives": t.string().optional(),
            "recall": t.number().optional(),
            "trueNegatives": t.string().optional(),
            "accuracy": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinaryConfusionMatrixOut"])
    types["SnapshotDefinitionIn"] = t.struct(
        {
            "snapshotTime": t.string().optional(),
            "baseTableReference": t.proxy(renames["TableReferenceIn"]).optional(),
        }
    ).named(renames["SnapshotDefinitionIn"])
    types["SnapshotDefinitionOut"] = t.struct(
        {
            "snapshotTime": t.string().optional(),
            "baseTableReference": t.proxy(renames["TableReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotDefinitionOut"])
    types["DimensionalityReductionMetricsIn"] = t.struct(
        {"totalExplainedVarianceRatio": t.number().optional()}
    ).named(renames["DimensionalityReductionMetricsIn"])
    types["DimensionalityReductionMetricsOut"] = t.struct(
        {
            "totalExplainedVarianceRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DimensionalityReductionMetricsOut"])
    types["TimePartitioningIn"] = t.struct(
        {
            "field": t.string().optional(),
            "type": t.string().optional(),
            "requirePartitionFilter": t.boolean(),
            "expirationMs": t.string().optional(),
        }
    ).named(renames["TimePartitioningIn"])
    types["TimePartitioningOut"] = t.struct(
        {
            "field": t.string().optional(),
            "type": t.string().optional(),
            "requirePartitionFilter": t.boolean(),
            "expirationMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePartitioningOut"])
    types["ArimaSingleModelForecastingMetricsIn"] = t.struct(
        {
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesIds": t.array(t.string()).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "arimaFittingMetrics": t.proxy(renames["ArimaFittingMetricsIn"]).optional(),
            "timeSeriesId": t.string().optional(),
            "hasDrift": t.boolean().optional(),
            "hasStepChanges": t.boolean().optional(),
            "hasSpikesAndDips": t.boolean().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderIn"]).optional(),
        }
    ).named(renames["ArimaSingleModelForecastingMetricsIn"])
    types["ArimaSingleModelForecastingMetricsOut"] = t.struct(
        {
            "hasHolidayEffect": t.boolean().optional(),
            "timeSeriesIds": t.array(t.string()).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "arimaFittingMetrics": t.proxy(
                renames["ArimaFittingMetricsOut"]
            ).optional(),
            "timeSeriesId": t.string().optional(),
            "hasDrift": t.boolean().optional(),
            "hasStepChanges": t.boolean().optional(),
            "hasSpikesAndDips": t.boolean().optional(),
            "nonSeasonalOrder": t.proxy(renames["ArimaOrderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaSingleModelForecastingMetricsOut"])
    types["HparamTuningTrialIn"] = t.struct(
        {
            "trainingLoss": t.number().optional(),
            "errorMessage": t.string().optional(),
            "hparamTuningEvaluationMetrics": t.proxy(
                renames["EvaluationMetricsIn"]
            ).optional(),
            "trialId": t.string().optional(),
            "status": t.string().optional(),
            "hparams": t.proxy(renames["TrainingOptionsIn"]).optional(),
            "endTimeMs": t.string().optional(),
            "startTimeMs": t.string().optional(),
            "evaluationMetrics": t.proxy(renames["EvaluationMetricsIn"]).optional(),
            "evalLoss": t.number().optional(),
        }
    ).named(renames["HparamTuningTrialIn"])
    types["HparamTuningTrialOut"] = t.struct(
        {
            "trainingLoss": t.number().optional(),
            "errorMessage": t.string().optional(),
            "hparamTuningEvaluationMetrics": t.proxy(
                renames["EvaluationMetricsOut"]
            ).optional(),
            "trialId": t.string().optional(),
            "status": t.string().optional(),
            "hparams": t.proxy(renames["TrainingOptionsOut"]).optional(),
            "endTimeMs": t.string().optional(),
            "startTimeMs": t.string().optional(),
            "evaluationMetrics": t.proxy(renames["EvaluationMetricsOut"]).optional(),
            "evalLoss": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HparamTuningTrialOut"])
    types["ClusterIn"] = t.struct(
        {
            "count": t.string().optional(),
            "featureValues": t.array(t.proxy(renames["FeatureValueIn"])).optional(),
            "centroidId": t.string().optional(),
        }
    ).named(renames["ClusterIn"])
    types["ClusterOut"] = t.struct(
        {
            "count": t.string().optional(),
            "featureValues": t.array(t.proxy(renames["FeatureValueOut"])).optional(),
            "centroidId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterOut"])
    types["ArimaForecastingMetricsIn"] = t.struct(
        {
            "arimaSingleModelForecastingMetrics": t.array(
                t.proxy(renames["ArimaSingleModelForecastingMetricsIn"])
            ).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "arimaFittingMetrics": t.array(
                t.proxy(renames["ArimaFittingMetricsIn"])
            ).optional(),
            "timeSeriesId": t.array(t.string()).optional(),
            "hasDrift": t.array(t.boolean()).optional(),
            "nonSeasonalOrder": t.array(t.proxy(renames["ArimaOrderIn"])).optional(),
        }
    ).named(renames["ArimaForecastingMetricsIn"])
    types["ArimaForecastingMetricsOut"] = t.struct(
        {
            "arimaSingleModelForecastingMetrics": t.array(
                t.proxy(renames["ArimaSingleModelForecastingMetricsOut"])
            ).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "arimaFittingMetrics": t.array(
                t.proxy(renames["ArimaFittingMetricsOut"])
            ).optional(),
            "timeSeriesId": t.array(t.string()).optional(),
            "hasDrift": t.array(t.boolean()).optional(),
            "nonSeasonalOrder": t.array(t.proxy(renames["ArimaOrderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaForecastingMetricsOut"])
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
    types["ProjectReferenceIn"] = t.struct({"projectId": t.string().optional()}).named(
        renames["ProjectReferenceIn"]
    )
    types["ProjectReferenceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectReferenceOut"])
    types["JobReferenceIn"] = t.struct(
        {
            "jobId": t.string().optional(),
            "location": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["JobReferenceIn"])
    types["JobReferenceOut"] = t.struct(
        {
            "jobId": t.string().optional(),
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobReferenceOut"])
    types["EncryptionConfigurationIn"] = t.struct(
        {"kmsKeyName": t.string().optional()}
    ).named(renames["EncryptionConfigurationIn"])
    types["EncryptionConfigurationOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionConfigurationOut"])
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
    types["JobConfigurationLoadIn"] = t.struct(
        {
            "useAvroLogicalTypes": t.boolean().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
            "projectionFields": t.array(t.string()).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
            "createDisposition": t.string().optional(),
            "encoding": t.string().optional(),
            "fieldDelimiter": t.string().optional(),
            "autodetect": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "schemaInlineFormat": t.string().optional(),
            "jsonExtension": t.string().optional(),
            "quote": t.string().optional(),
            "schemaInline": t.string().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsIn"]
            ).optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "maxBadRecords": t.integer().optional(),
            "createSession": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "nullMarker": t.string().optional(),
            "destinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyIn"])
            ).optional(),
            "skipLeadingRows": t.integer().optional(),
            "clustering": t.proxy(renames["ClusteringIn"]).optional(),
            "allowQuotedNewlines": t.boolean().optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsIn"]).optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "destinationTableProperties": t.proxy(
                renames["DestinationTablePropertiesIn"]
            ).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "sourceUris": t.array(t.string()).optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
        }
    ).named(renames["JobConfigurationLoadIn"])
    types["JobConfigurationLoadOut"] = t.struct(
        {
            "useAvroLogicalTypes": t.boolean().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningOut"]).optional(),
            "projectionFields": t.array(t.string()).optional(),
            "referenceFileSchemaUri": t.string().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningOut"]).optional(),
            "createDisposition": t.string().optional(),
            "encoding": t.string().optional(),
            "fieldDelimiter": t.string().optional(),
            "autodetect": t.boolean().optional(),
            "writeDisposition": t.string().optional(),
            "schemaInlineFormat": t.string().optional(),
            "jsonExtension": t.string().optional(),
            "quote": t.string().optional(),
            "schemaInline": t.string().optional(),
            "allowJaggedRows": t.boolean().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "hivePartitioningOptions": t.proxy(
                renames["HivePartitioningOptionsOut"]
            ).optional(),
            "decimalTargetTypes": t.array(t.string()).optional(),
            "maxBadRecords": t.integer().optional(),
            "createSession": t.boolean().optional(),
            "sourceFormat": t.string().optional(),
            "nullMarker": t.string().optional(),
            "destinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyOut"])
            ).optional(),
            "skipLeadingRows": t.integer().optional(),
            "clustering": t.proxy(renames["ClusteringOut"]).optional(),
            "allowQuotedNewlines": t.boolean().optional(),
            "parquetOptions": t.proxy(renames["ParquetOptionsOut"]).optional(),
            "preserveAsciiControlCharacters": t.boolean().optional(),
            "destinationTableProperties": t.proxy(
                renames["DestinationTablePropertiesOut"]
            ).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "sourceUris": t.array(t.string()).optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationLoadOut"])
    types["RowAccessPolicyReferenceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "policyId": t.string().optional(),
        }
    ).named(renames["RowAccessPolicyReferenceIn"])
    types["RowAccessPolicyReferenceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "policyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowAccessPolicyReferenceOut"])
    types["StandardSqlFieldIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
        }
    ).named(renames["StandardSqlFieldIn"])
    types["StandardSqlFieldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.proxy(renames["StandardSqlDataTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlFieldOut"])
    types["PrincipalComponentInfoIn"] = t.struct(
        {
            "explainedVariance": t.number().optional(),
            "explainedVarianceRatio": t.number().optional(),
            "principalComponentId": t.string().optional(),
            "cumulativeExplainedVarianceRatio": t.number().optional(),
        }
    ).named(renames["PrincipalComponentInfoIn"])
    types["PrincipalComponentInfoOut"] = t.struct(
        {
            "explainedVariance": t.number().optional(),
            "explainedVarianceRatio": t.number().optional(),
            "principalComponentId": t.string().optional(),
            "cumulativeExplainedVarianceRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrincipalComponentInfoOut"])
    types["RegressionMetricsIn"] = t.struct(
        {
            "meanAbsoluteError": t.number().optional(),
            "medianAbsoluteError": t.number().optional(),
            "meanSquaredLogError": t.number().optional(),
            "meanSquaredError": t.number().optional(),
            "rSquared": t.number().optional(),
        }
    ).named(renames["RegressionMetricsIn"])
    types["RegressionMetricsOut"] = t.struct(
        {
            "meanAbsoluteError": t.number().optional(),
            "medianAbsoluteError": t.number().optional(),
            "meanSquaredLogError": t.number().optional(),
            "meanSquaredError": t.number().optional(),
            "rSquared": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegressionMetricsOut"])
    types["JobListIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "jobs": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
                        "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
                        "status": t.proxy(renames["JobStatusIn"]).optional(),
                        "errorResult": t.proxy(renames["ErrorProtoIn"]).optional(),
                        "state": t.string().optional(),
                        "kind": t.string().optional(),
                        "configuration": t.proxy(
                            renames["JobConfigurationIn"]
                        ).optional(),
                        "user_email": t.string().optional(),
                    }
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["JobListIn"])
    types["JobListOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "jobs": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "statistics": t.proxy(renames["JobStatisticsOut"]).optional(),
                        "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
                        "status": t.proxy(renames["JobStatusOut"]).optional(),
                        "errorResult": t.proxy(renames["ErrorProtoOut"]).optional(),
                        "state": t.string().optional(),
                        "kind": t.string().optional(),
                        "configuration": t.proxy(
                            renames["JobConfigurationOut"]
                        ).optional(),
                        "user_email": t.string().optional(),
                    }
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobListOut"])
    types["TableFieldSchemaIn"] = t.struct(
        {
            "collation": t.string().optional(),
            "categories": t.struct(
                {"names": t.array(t.string()).optional()}
            ).optional(),
            "description": t.string().optional(),
            "policyTags": t.struct({"names": t.array(t.string()).optional()}),
            "roundingMode": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "maxLength": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional(),
            "defaultValueExpression": t.string().optional(),
            "mode": t.string().optional(),
            "scale": t.string().optional(),
            "precision": t.string().optional(),
        }
    ).named(renames["TableFieldSchemaIn"])
    types["TableFieldSchemaOut"] = t.struct(
        {
            "collation": t.string().optional(),
            "categories": t.struct(
                {"names": t.array(t.string()).optional()}
            ).optional(),
            "description": t.string().optional(),
            "policyTags": t.struct({"names": t.array(t.string()).optional()}),
            "roundingMode": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "maxLength": t.string().optional(),
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "defaultValueExpression": t.string().optional(),
            "mode": t.string().optional(),
            "scale": t.string().optional(),
            "precision": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableFieldSchemaOut"])
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
    types["SessionInfoIn"] = t.struct({"sessionId": t.string().optional()}).named(
        renames["SessionInfoIn"]
    )
    types["SessionInfoOut"] = t.struct(
        {
            "sessionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionInfoOut"])
    types["BinaryClassificationMetricsIn"] = t.struct(
        {
            "positiveLabel": t.string().optional(),
            "binaryConfusionMatrixList": t.array(
                t.proxy(renames["BinaryConfusionMatrixIn"])
            ).optional(),
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsIn"]
            ).optional(),
            "negativeLabel": t.string().optional(),
        }
    ).named(renames["BinaryClassificationMetricsIn"])
    types["BinaryClassificationMetricsOut"] = t.struct(
        {
            "positiveLabel": t.string().optional(),
            "binaryConfusionMatrixList": t.array(
                t.proxy(renames["BinaryConfusionMatrixOut"])
            ).optional(),
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsOut"]
            ).optional(),
            "negativeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BinaryClassificationMetricsOut"])
    types["MultiClassClassificationMetricsIn"] = t.struct(
        {
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsIn"]
            ).optional(),
            "confusionMatrixList": t.array(
                t.proxy(renames["ConfusionMatrixIn"])
            ).optional(),
        }
    ).named(renames["MultiClassClassificationMetricsIn"])
    types["MultiClassClassificationMetricsOut"] = t.struct(
        {
            "aggregateClassificationMetrics": t.proxy(
                renames["AggregateClassificationMetricsOut"]
            ).optional(),
            "confusionMatrixList": t.array(
                t.proxy(renames["ConfusionMatrixOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MultiClassClassificationMetricsOut"])
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
    types["JobConfigurationQueryIn"] = t.struct(
        {
            "parameterMode": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyIn"])
            ).optional(),
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceIn"])
            ).optional(),
            "useQueryCache": t.boolean().optional(),
            "flattenResults": t.boolean().optional(),
            "query": t.string().optional(),
            "tableDefinitions": t.struct({"_": t.string().optional()}).optional(),
            "queryParameters": t.array(t.proxy(renames["QueryParameterIn"])).optional(),
            "createDisposition": t.string().optional(),
            "allowLargeResults": t.boolean().optional(),
            "createSession": t.boolean().optional(),
            "clustering": t.proxy(renames["ClusteringIn"]).optional(),
            "useLegacySql": t.boolean().optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
            "continuous": t.boolean().optional(),
            "priority": t.string().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
            "preserveNulls": t.boolean().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
            "destinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "maximumBillingTier": t.integer().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "maximumBytesBilled": t.string().optional(),
        }
    ).named(renames["JobConfigurationQueryIn"])
    types["JobConfigurationQueryOut"] = t.struct(
        {
            "parameterMode": t.string().optional(),
            "writeDisposition": t.string().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyOut"])
            ).optional(),
            "userDefinedFunctionResources": t.array(
                t.proxy(renames["UserDefinedFunctionResourceOut"])
            ).optional(),
            "useQueryCache": t.boolean().optional(),
            "flattenResults": t.boolean().optional(),
            "query": t.string().optional(),
            "tableDefinitions": t.struct({"_": t.string().optional()}).optional(),
            "queryParameters": t.array(
                t.proxy(renames["QueryParameterOut"])
            ).optional(),
            "createDisposition": t.string().optional(),
            "allowLargeResults": t.boolean().optional(),
            "createSession": t.boolean().optional(),
            "clustering": t.proxy(renames["ClusteringOut"]).optional(),
            "useLegacySql": t.boolean().optional(),
            "schemaUpdateOptions": t.array(t.string()).optional(),
            "continuous": t.boolean().optional(),
            "priority": t.string().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningOut"]).optional(),
            "preserveNulls": t.boolean().optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningOut"]).optional(),
            "destinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "maximumBillingTier": t.integer().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "maximumBytesBilled": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationQueryOut"])
    types["CloneDefinitionIn"] = t.struct(
        {
            "baseTableReference": t.proxy(renames["TableReferenceIn"]).optional(),
            "cloneTime": t.string().optional(),
        }
    ).named(renames["CloneDefinitionIn"])
    types["CloneDefinitionOut"] = t.struct(
        {
            "baseTableReference": t.proxy(renames["TableReferenceOut"]).optional(),
            "cloneTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneDefinitionOut"])
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
    types["IntCandidatesIn"] = t.struct(
        {"candidates": t.array(t.string()).optional()}
    ).named(renames["IntCandidatesIn"])
    types["IntCandidatesOut"] = t.struct(
        {
            "candidates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntCandidatesOut"])
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
    types["ProjectListIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "projects": t.array(
                t.struct(
                    {
                        "numericId": t.string().optional(),
                        "id": t.string().optional(),
                        "friendlyName": t.string().optional(),
                        "kind": t.string().optional(),
                        "projectReference": t.proxy(
                            renames["ProjectReferenceIn"]
                        ).optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["ProjectListIn"])
    types["ProjectListOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "projects": t.array(
                t.struct(
                    {
                        "numericId": t.string().optional(),
                        "id": t.string().optional(),
                        "friendlyName": t.string().optional(),
                        "kind": t.string().optional(),
                        "projectReference": t.proxy(
                            renames["ProjectReferenceOut"]
                        ).optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectListOut"])
    types["StringHparamSearchSpaceIn"] = t.struct(
        {"candidates": t.array(t.string()).optional()}
    ).named(renames["StringHparamSearchSpaceIn"])
    types["StringHparamSearchSpaceOut"] = t.struct(
        {
            "candidates": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringHparamSearchSpaceOut"])
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
    types["ArimaResultIn"] = t.struct(
        {
            "arimaModelInfo": t.array(t.proxy(renames["ArimaModelInfoIn"])).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
        }
    ).named(renames["ArimaResultIn"])
    types["ArimaResultOut"] = t.struct(
        {
            "arimaModelInfo": t.array(t.proxy(renames["ArimaModelInfoOut"])).optional(),
            "seasonalPeriods": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArimaResultOut"])
    types["TrainingRunIn"] = t.struct({"vertexAiModelId": t.string().optional()}).named(
        renames["TrainingRunIn"]
    )
    types["TrainingRunOut"] = t.struct(
        {
            "dataSplitResult": t.proxy(renames["DataSplitResultOut"]).optional(),
            "classLevelGlobalExplanations": t.array(
                t.proxy(renames["GlobalExplanationOut"])
            ).optional(),
            "vertexAiModelId": t.string().optional(),
            "startTime": t.string().optional(),
            "trainingOptions": t.proxy(renames["TrainingOptionsOut"]).optional(),
            "vertexAiModelVersion": t.string().optional(),
            "trainingStartTime": t.string().optional(),
            "results": t.array(t.proxy(renames["IterationResultOut"])).optional(),
            "modelLevelGlobalExplanation": t.proxy(
                renames["GlobalExplanationOut"]
            ).optional(),
            "evaluationMetrics": t.proxy(renames["EvaluationMetricsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrainingRunOut"])
    types["JobStatistics4In"] = t.struct(
        {
            "inputBytes": t.string().optional(),
            "destinationUriFileCounts": t.array(t.string()).optional(),
        }
    ).named(renames["JobStatistics4In"])
    types["JobStatistics4Out"] = t.struct(
        {
            "inputBytes": t.string().optional(),
            "destinationUriFileCounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatistics4Out"])
    types["StandardSqlStructTypeIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["StandardSqlFieldIn"]))}
    ).named(renames["StandardSqlStructTypeIn"])
    types["StandardSqlStructTypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["StandardSqlFieldOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSqlStructTypeOut"])
    types["DataSplitResultIn"] = t.struct(
        {
            "evaluationTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "trainingTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "testTable": t.proxy(renames["TableReferenceIn"]).optional(),
        }
    ).named(renames["DataSplitResultIn"])
    types["DataSplitResultOut"] = t.struct(
        {
            "evaluationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "trainingTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "testTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSplitResultOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RowIn"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["EntryIn"])).optional(),
            "actualLabel": t.string().optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["EntryOut"])).optional(),
            "actualLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["JobStatistics3In"] = t.struct(
        {
            "inputFileBytes": t.string().optional(),
            "outputBytes": t.string().optional(),
            "outputRows": t.string().optional(),
            "inputFiles": t.string().optional(),
            "badRecords": t.string().optional(),
        }
    ).named(renames["JobStatistics3In"])
    types["JobStatistics3Out"] = t.struct(
        {
            "inputFileBytes": t.string().optional(),
            "outputBytes": t.string().optional(),
            "outputRows": t.string().optional(),
            "inputFiles": t.string().optional(),
            "badRecords": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatistics3Out"])
    types["TableDataInsertAllResponseIn"] = t.struct(
        {
            "insertErrors": t.array(
                t.struct(
                    {
                        "index": t.integer().optional(),
                        "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
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
                        "index": t.integer().optional(),
                        "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableDataInsertAllResponseOut"])
    types["RoutineReferenceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "routineId": t.string().optional(),
        }
    ).named(renames["RoutineReferenceIn"])
    types["RoutineReferenceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "routineId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutineReferenceOut"])
    types["ListModelsResponseIn"] = t.struct(
        {
            "models": t.array(t.proxy(renames["ModelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListModelsResponseIn"])
    types["ListModelsResponseOut"] = t.struct(
        {
            "models": t.array(t.proxy(renames["ModelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListModelsResponseOut"])
    types["ListRoutinesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "routines": t.array(t.proxy(renames["RoutineIn"])).optional(),
        }
    ).named(renames["ListRoutinesResponseIn"])
    types["ListRoutinesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "routines": t.array(t.proxy(renames["RoutineOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRoutinesResponseOut"])
    types["JobConfigurationTableCopyIn"] = t.struct(
        {
            "sourceTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "createDisposition": t.string().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "operationType": t.string().optional(),
            "destinationExpirationTime": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "writeDisposition": t.string().optional(),
            "sourceTables": t.array(t.proxy(renames["TableReferenceIn"])).optional(),
            "destinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
        }
    ).named(renames["JobConfigurationTableCopyIn"])
    types["JobConfigurationTableCopyOut"] = t.struct(
        {
            "sourceTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "createDisposition": t.string().optional(),
            "destinationEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "operationType": t.string().optional(),
            "destinationExpirationTime": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "writeDisposition": t.string().optional(),
            "sourceTables": t.array(t.proxy(renames["TableReferenceOut"])).optional(),
            "destinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobConfigurationTableCopyOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["IterationResultIn"] = t.struct(
        {
            "evalLoss": t.number().optional(),
            "trainingLoss": t.number().optional(),
            "learnRate": t.number().optional(),
            "index": t.integer().optional(),
            "durationMs": t.string().optional(),
        }
    ).named(renames["IterationResultIn"])
    types["IterationResultOut"] = t.struct(
        {
            "evalLoss": t.number().optional(),
            "trainingLoss": t.number().optional(),
            "learnRate": t.number().optional(),
            "index": t.integer().optional(),
            "durationMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IterationResultOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListRowAccessPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rowAccessPolicies": t.array(
                t.proxy(renames["RowAccessPolicyIn"])
            ).optional(),
        }
    ).named(renames["ListRowAccessPoliciesResponseIn"])
    types["ListRowAccessPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rowAccessPolicies": t.array(
                t.proxy(renames["RowAccessPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRowAccessPoliciesResponseOut"])
    types["HivePartitioningOptionsIn"] = t.struct(
        {
            "sourceUriPrefix": t.string().optional(),
            "fields": t.array(t.string()).optional(),
            "mode": t.string().optional(),
            "requirePartitionFilter": t.boolean().optional(),
        }
    ).named(renames["HivePartitioningOptionsIn"])
    types["HivePartitioningOptionsOut"] = t.struct(
        {
            "sourceUriPrefix": t.string().optional(),
            "fields": t.array(t.string()).optional(),
            "mode": t.string().optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HivePartitioningOptionsOut"])
    types["StreamingbufferIn"] = t.struct(
        {
            "estimatedRows": t.string().optional(),
            "oldestEntryTime": t.string().optional(),
            "estimatedBytes": t.string().optional(),
        }
    ).named(renames["StreamingbufferIn"])
    types["StreamingbufferOut"] = t.struct(
        {
            "estimatedRows": t.string().optional(),
            "oldestEntryTime": t.string().optional(),
            "estimatedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamingbufferOut"])
    types["ArgumentIn"] = t.struct(
        {
            "mode": t.string().optional(),
            "name": t.string().optional(),
            "dataType": t.proxy(renames["StandardSqlDataTypeIn"]),
            "argumentKind": t.string().optional(),
        }
    ).named(renames["ArgumentIn"])
    types["ArgumentOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "name": t.string().optional(),
            "dataType": t.proxy(renames["StandardSqlDataTypeOut"]),
            "argumentKind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArgumentOut"])
    types["GoogleSheetsOptionsIn"] = t.struct(
        {"skipLeadingRows": t.string().optional(), "range": t.string().optional()}
    ).named(renames["GoogleSheetsOptionsIn"])
    types["GoogleSheetsOptionsOut"] = t.struct(
        {
            "skipLeadingRows": t.string().optional(),
            "range": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSheetsOptionsOut"])
    types["IntArrayIn"] = t.struct({"elements": t.array(t.string()).optional()}).named(
        renames["IntArrayIn"]
    )
    types["IntArrayOut"] = t.struct(
        {
            "elements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntArrayOut"])
    types["RemoteFunctionOptionsIn"] = t.struct(
        {
            "userDefinedContext": t.struct({"_": t.string().optional()}).optional(),
            "endpoint": t.string().optional(),
            "maxBatchingRows": t.string().optional(),
            "connection": t.string().optional(),
        }
    ).named(renames["RemoteFunctionOptionsIn"])
    types["RemoteFunctionOptionsOut"] = t.struct(
        {
            "userDefinedContext": t.struct({"_": t.string().optional()}).optional(),
            "endpoint": t.string().optional(),
            "maxBatchingRows": t.string().optional(),
            "connection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteFunctionOptionsOut"])
    types["DoubleRangeIn"] = t.struct(
        {"max": t.number().optional(), "min": t.number().optional()}
    ).named(renames["DoubleRangeIn"])
    types["DoubleRangeOut"] = t.struct(
        {
            "max": t.number().optional(),
            "min": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleRangeOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["BiEngineStatisticsIn"] = t.struct(
        {
            "biEngineMode": t.string().optional(),
            "accelerationMode": t.string().optional(),
            "biEngineReasons": t.array(t.proxy(renames["BiEngineReasonIn"])).optional(),
        }
    ).named(renames["BiEngineStatisticsIn"])
    types["BiEngineStatisticsOut"] = t.struct(
        {
            "biEngineMode": t.string().optional(),
            "accelerationMode": t.string().optional(),
            "biEngineReasons": t.array(
                t.proxy(renames["BiEngineReasonOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiEngineStatisticsOut"])
    types["TableSchemaIn"] = t.struct(
        {"fields": t.array(t.proxy(renames["TableFieldSchemaIn"])).optional()}
    ).named(renames["TableSchemaIn"])
    types["TableSchemaOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["TableFieldSchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableSchemaOut"])
    types["QueryParameterIn"] = t.struct(
        {
            "parameterType": t.proxy(renames["QueryParameterTypeIn"]).optional(),
            "name": t.string().optional(),
            "parameterValue": t.proxy(renames["QueryParameterValueIn"]).optional(),
        }
    ).named(renames["QueryParameterIn"])
    types["QueryParameterOut"] = t.struct(
        {
            "parameterType": t.proxy(renames["QueryParameterTypeOut"]).optional(),
            "name": t.string().optional(),
            "parameterValue": t.proxy(renames["QueryParameterValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryParameterOut"])
    types["ScriptStatisticsIn"] = t.struct(
        {
            "stackFrames": t.array(t.proxy(renames["ScriptStackFrameIn"])).optional(),
            "evaluationKind": t.string().optional(),
        }
    ).named(renames["ScriptStatisticsIn"])
    types["ScriptStatisticsOut"] = t.struct(
        {
            "stackFrames": t.array(t.proxy(renames["ScriptStackFrameOut"])).optional(),
            "evaluationKind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptStatisticsOut"])
    types["QueryParameterTypeIn"] = t.struct(
        {
            "structTypes": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "description": t.string().optional(),
                        "type": t.proxy(renames["QueryParameterTypeIn"]).optional(),
                    }
                )
            ).optional(),
            "type": t.string().optional(),
            "arrayType": t.proxy(renames["QueryParameterTypeIn"]).optional(),
        }
    ).named(renames["QueryParameterTypeIn"])
    types["QueryParameterTypeOut"] = t.struct(
        {
            "structTypes": t.array(
                t.struct(
                    {
                        "name": t.string().optional(),
                        "description": t.string().optional(),
                        "type": t.proxy(renames["QueryParameterTypeOut"]).optional(),
                    }
                )
            ).optional(),
            "type": t.string().optional(),
            "arrayType": t.proxy(renames["QueryParameterTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryParameterTypeOut"])
    types["SparkOptionsIn"] = t.struct(
        {
            "mainFileUri": t.string().optional(),
            "containerImage": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "jarUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "connection": t.string().optional(),
            "pyFileUris": t.array(t.string()).optional(),
            "runtimeVersion": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
        }
    ).named(renames["SparkOptionsIn"])
    types["SparkOptionsOut"] = t.struct(
        {
            "mainFileUri": t.string().optional(),
            "containerImage": t.string().optional(),
            "archiveUris": t.array(t.string()).optional(),
            "jarUris": t.array(t.string()).optional(),
            "mainClass": t.string().optional(),
            "connection": t.string().optional(),
            "pyFileUris": t.array(t.string()).optional(),
            "runtimeVersion": t.string().optional(),
            "properties": t.struct({"_": t.string().optional()}).optional(),
            "fileUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SparkOptionsOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["RowAccessPolicyIn"] = t.struct(
        {
            "rowAccessPolicyReference": t.proxy(renames["RowAccessPolicyReferenceIn"]),
            "filterPredicate": t.string(),
        }
    ).named(renames["RowAccessPolicyIn"])
    types["RowAccessPolicyOut"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "rowAccessPolicyReference": t.proxy(renames["RowAccessPolicyReferenceOut"]),
            "etag": t.string().optional(),
            "filterPredicate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowAccessPolicyOut"])
    types["ClusteringIn"] = t.struct({"fields": t.array(t.string()).optional()}).named(
        renames["ClusteringIn"]
    )
    types["ClusteringOut"] = t.struct(
        {
            "fields": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusteringOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["ClusterInfoIn"] = t.struct(
        {
            "centroidId": t.string().optional(),
            "clusterRadius": t.number().optional(),
            "clusterSize": t.string().optional(),
        }
    ).named(renames["ClusterInfoIn"])
    types["ClusterInfoOut"] = t.struct(
        {
            "centroidId": t.string().optional(),
            "clusterRadius": t.number().optional(),
            "clusterSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterInfoOut"])
    types["BigQueryModelTrainingIn"] = t.struct(
        {
            "expectedTotalIterations": t.string().optional(),
            "currentIteration": t.integer().optional(),
        }
    ).named(renames["BigQueryModelTrainingIn"])
    types["BigQueryModelTrainingOut"] = t.struct(
        {
            "expectedTotalIterations": t.string().optional(),
            "currentIteration": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryModelTrainingOut"])
    types["RemoteModelInfoIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoteModelInfoIn"]
    )
    types["RemoteModelInfoOut"] = t.struct(
        {
            "maxBatchingRows": t.string().optional(),
            "endpoint": t.string().optional(),
            "remoteServiceType": t.string().optional(),
            "connection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteModelInfoOut"])
    types["EvaluationMetricsIn"] = t.struct(
        {
            "rankingMetrics": t.proxy(renames["RankingMetricsIn"]).optional(),
            "regressionMetrics": t.proxy(renames["RegressionMetricsIn"]).optional(),
            "arimaForecastingMetrics": t.proxy(
                renames["ArimaForecastingMetricsIn"]
            ).optional(),
            "dimensionalityReductionMetrics": t.proxy(
                renames["DimensionalityReductionMetricsIn"]
            ).optional(),
            "binaryClassificationMetrics": t.proxy(
                renames["BinaryClassificationMetricsIn"]
            ).optional(),
            "clusteringMetrics": t.proxy(renames["ClusteringMetricsIn"]).optional(),
            "multiClassClassificationMetrics": t.proxy(
                renames["MultiClassClassificationMetricsIn"]
            ).optional(),
        }
    ).named(renames["EvaluationMetricsIn"])
    types["EvaluationMetricsOut"] = t.struct(
        {
            "rankingMetrics": t.proxy(renames["RankingMetricsOut"]).optional(),
            "regressionMetrics": t.proxy(renames["RegressionMetricsOut"]).optional(),
            "arimaForecastingMetrics": t.proxy(
                renames["ArimaForecastingMetricsOut"]
            ).optional(),
            "dimensionalityReductionMetrics": t.proxy(
                renames["DimensionalityReductionMetricsOut"]
            ).optional(),
            "binaryClassificationMetrics": t.proxy(
                renames["BinaryClassificationMetricsOut"]
            ).optional(),
            "clusteringMetrics": t.proxy(renames["ClusteringMetricsOut"]).optional(),
            "multiClassClassificationMetrics": t.proxy(
                renames["MultiClassClassificationMetricsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluationMetricsOut"])
    types["TableDataInsertAllRequestIn"] = t.struct(
        {
            "templateSuffix": t.string().optional(),
            "kind": t.string().optional(),
            "skipInvalidRows": t.boolean().optional(),
            "rows": t.array(
                t.struct(
                    {
                        "insertId": t.string().optional(),
                        "json": t.proxy(renames["JsonObjectIn"]).optional(),
                    }
                )
            ).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
        }
    ).named(renames["TableDataInsertAllRequestIn"])
    types["TableDataInsertAllRequestOut"] = t.struct(
        {
            "templateSuffix": t.string().optional(),
            "kind": t.string().optional(),
            "skipInvalidRows": t.boolean().optional(),
            "rows": t.array(
                t.struct(
                    {
                        "insertId": t.string().optional(),
                        "json": t.proxy(renames["JsonObjectOut"]).optional(),
                    }
                )
            ).optional(),
            "ignoreUnknownValues": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableDataInsertAllRequestOut"])
    types["JobStatistics2In"] = t.struct(
        {
            "ddlDestinationTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "queryPlan": t.array(t.proxy(renames["ExplainQueryStageIn"])).optional(),
            "referencedTables": t.array(
                t.proxy(renames["TableReferenceIn"])
            ).optional(),
            "mlStatistics": t.proxy(renames["MlStatisticsIn"]).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "billingTier": t.integer().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "ddlTargetRoutine": t.proxy(renames["RoutineReferenceIn"]).optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsIn"]).optional(),
            "biEngineStatistics": t.proxy(renames["BiEngineStatisticsIn"]).optional(),
            "totalBytesProcessedAccuracy": t.string().optional(),
            "ddlTargetDataset": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "referencedRoutines": t.array(
                t.proxy(renames["RoutineReferenceIn"])
            ).optional(),
            "modelTrainingExpectedTotalIteration": t.string().optional(),
            "estimatedBytesProcessed": t.string().optional(),
            "ddlAffectedRowAccessPolicyCount": t.string().optional(),
            "totalBytesProcessed": t.string().optional(),
            "searchStatistics": t.proxy(renames["SearchStatisticsIn"]).optional(),
            "modelTraining": t.proxy(renames["BigQueryModelTrainingIn"]).optional(),
            "modelTrainingCurrentIteration": t.integer().optional(),
            "cacheHit": t.boolean().optional(),
            "totalSlotMs": t.string().optional(),
            "totalBytesBilled": t.string().optional(),
            "ddlOperationPerformed": t.string().optional(),
            "ddlTargetRowAccessPolicy": t.proxy(
                renames["RowAccessPolicyReferenceIn"]
            ).optional(),
            "ddlTargetTable": t.proxy(renames["TableReferenceIn"]).optional(),
            "statementType": t.string().optional(),
            "transferredBytes": t.string().optional(),
            "sparkStatistics": t.proxy(renames["SparkStatisticsIn"]).optional(),
            "totalPartitionsProcessed": t.string().optional(),
            "undeclaredQueryParameters": t.array(
                t.proxy(renames["QueryParameterIn"])
            ).optional(),
            "timeline": t.array(t.proxy(renames["QueryTimelineSampleIn"])).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"name": t.string().optional(), "slotMs": t.string().optional()}
                )
            ).optional(),
        }
    ).named(renames["JobStatistics2In"])
    types["JobStatistics2Out"] = t.struct(
        {
            "ddlDestinationTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "queryPlan": t.array(t.proxy(renames["ExplainQueryStageOut"])).optional(),
            "referencedTables": t.array(
                t.proxy(renames["TableReferenceOut"])
            ).optional(),
            "mlStatistics": t.proxy(renames["MlStatisticsOut"]).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "billingTier": t.integer().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "ddlTargetRoutine": t.proxy(renames["RoutineReferenceOut"]).optional(),
            "dmlStats": t.proxy(renames["DmlStatisticsOut"]).optional(),
            "biEngineStatistics": t.proxy(renames["BiEngineStatisticsOut"]).optional(),
            "totalBytesProcessedAccuracy": t.string().optional(),
            "ddlTargetDataset": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "referencedRoutines": t.array(
                t.proxy(renames["RoutineReferenceOut"])
            ).optional(),
            "modelTrainingExpectedTotalIteration": t.string().optional(),
            "estimatedBytesProcessed": t.string().optional(),
            "ddlAffectedRowAccessPolicyCount": t.string().optional(),
            "totalBytesProcessed": t.string().optional(),
            "searchStatistics": t.proxy(renames["SearchStatisticsOut"]).optional(),
            "modelTraining": t.proxy(renames["BigQueryModelTrainingOut"]).optional(),
            "modelTrainingCurrentIteration": t.integer().optional(),
            "cacheHit": t.boolean().optional(),
            "totalSlotMs": t.string().optional(),
            "totalBytesBilled": t.string().optional(),
            "ddlOperationPerformed": t.string().optional(),
            "ddlTargetRowAccessPolicy": t.proxy(
                renames["RowAccessPolicyReferenceOut"]
            ).optional(),
            "ddlTargetTable": t.proxy(renames["TableReferenceOut"]).optional(),
            "statementType": t.string().optional(),
            "transferredBytes": t.string().optional(),
            "sparkStatistics": t.proxy(renames["SparkStatisticsOut"]).optional(),
            "totalPartitionsProcessed": t.string().optional(),
            "undeclaredQueryParameters": t.array(
                t.proxy(renames["QueryParameterOut"])
            ).optional(),
            "timeline": t.array(t.proxy(renames["QueryTimelineSampleOut"])).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"name": t.string().optional(), "slotMs": t.string().optional()}
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatistics2Out"])
    types["DoubleCandidatesIn"] = t.struct(
        {"candidates": t.array(t.number()).optional()}
    ).named(renames["DoubleCandidatesIn"])
    types["DoubleCandidatesOut"] = t.struct(
        {
            "candidates": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleCandidatesOut"])
    types["ModelReferenceIn"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "projectId": t.string().optional(),
            "modelId": t.string().optional(),
        }
    ).named(renames["ModelReferenceIn"])
    types["ModelReferenceOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "projectId": t.string().optional(),
            "modelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelReferenceOut"])
    types["TableIn"] = t.struct(
        {
            "num_partitions": t.string().optional(),
            "num_active_logical_bytes": t.string().optional(),
            "materializedView": t.proxy(
                renames["MaterializedViewDefinitionIn"]
            ).optional(),
            "numBytes": t.string().optional(),
            "num_total_physical_bytes": t.string().optional(),
            "num_time_travel_physical_bytes": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
            "creationTime": t.string().optional(),
            "num_active_physical_bytes": t.string().optional(),
            "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "num_long_term_physical_bytes": t.string().optional(),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ).optional(),
            "clustering": t.proxy(renames["ClusteringIn"]).optional(),
            "snapshotDefinition": t.proxy(renames["SnapshotDefinitionIn"]).optional(),
            "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
            "numPhysicalBytes": t.string().optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
            "expirationTime": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
            "selfLink": t.string().optional(),
            "numLongTermBytes": t.string().optional(),
            "id": t.string().optional(),
            "defaultRoundingMode": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "location": t.string().optional(),
            "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
            "numRows": t.string().optional(),
            "defaultCollation": t.string().optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "num_total_logical_bytes": t.string().optional(),
            "friendlyName": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
            "externalDataConfiguration": t.proxy(
                renames["ExternalDataConfigurationIn"]
            ).optional(),
            "num_long_term_logical_bytes": t.string().optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "num_partitions": t.string().optional(),
            "num_active_logical_bytes": t.string().optional(),
            "materializedView": t.proxy(
                renames["MaterializedViewDefinitionOut"]
            ).optional(),
            "numBytes": t.string().optional(),
            "num_total_physical_bytes": t.string().optional(),
            "num_time_travel_physical_bytes": t.string().optional(),
            "maxStaleness": t.string().optional(),
            "streamingBuffer": t.proxy(renames["StreamingbufferOut"]).optional(),
            "creationTime": t.string().optional(),
            "num_active_physical_bytes": t.string().optional(),
            "view": t.proxy(renames["ViewDefinitionOut"]).optional(),
            "rangePartitioning": t.proxy(renames["RangePartitioningOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "num_long_term_physical_bytes": t.string().optional(),
            "encryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ).optional(),
            "clustering": t.proxy(renames["ClusteringOut"]).optional(),
            "snapshotDefinition": t.proxy(renames["SnapshotDefinitionOut"]).optional(),
            "cloneDefinition": t.proxy(renames["CloneDefinitionOut"]).optional(),
            "numPhysicalBytes": t.string().optional(),
            "type": t.string().optional(),
            "kind": t.string().optional(),
            "expirationTime": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "timePartitioning": t.proxy(renames["TimePartitioningOut"]).optional(),
            "selfLink": t.string().optional(),
            "numLongTermBytes": t.string().optional(),
            "id": t.string().optional(),
            "defaultRoundingMode": t.string().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "location": t.string().optional(),
            "model": t.proxy(renames["ModelDefinitionOut"]).optional(),
            "numRows": t.string().optional(),
            "defaultCollation": t.string().optional(),
            "requirePartitionFilter": t.boolean().optional(),
            "num_total_logical_bytes": t.string().optional(),
            "friendlyName": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "tableReference": t.proxy(renames["TableReferenceOut"]).optional(),
            "externalDataConfiguration": t.proxy(
                renames["ExternalDataConfigurationOut"]
            ).optional(),
            "num_long_term_logical_bytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["JobStatisticsIn"] = t.struct(
        {
            "scriptStatistics": t.proxy(renames["ScriptStatisticsIn"]).optional(),
            "totalBytesProcessed": t.string().optional(),
            "query": t.proxy(renames["JobStatistics2In"]).optional(),
            "parentJobId": t.string().optional(),
            "startTime": t.string().optional(),
            "numChildJobs": t.string().optional(),
            "endTime": t.string().optional(),
            "extract": t.proxy(renames["JobStatistics4In"]).optional(),
            "reservation_id": t.string().optional(),
            "transactionInfo": t.proxy(renames["TransactionInfoIn"]).optional(),
            "quotaDeferments": t.array(t.string()).optional(),
            "totalSlotMs": t.string().optional(),
            "creationTime": t.string().optional(),
            "rowLevelSecurityStatistics": t.proxy(
                renames["RowLevelSecurityStatisticsIn"]
            ).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"name": t.string().optional(), "slotMs": t.string().optional()}
                )
            ).optional(),
            "load": t.proxy(renames["JobStatistics3In"]).optional(),
            "sessionInfo": t.proxy(renames["SessionInfoIn"]).optional(),
            "dataMaskingStatistics": t.proxy(
                renames["DataMaskingStatisticsIn"]
            ).optional(),
            "completionRatio": t.number().optional(),
            "copy": t.proxy(renames["JobStatistics5In"]).optional(),
        }
    ).named(renames["JobStatisticsIn"])
    types["JobStatisticsOut"] = t.struct(
        {
            "scriptStatistics": t.proxy(renames["ScriptStatisticsOut"]).optional(),
            "totalBytesProcessed": t.string().optional(),
            "query": t.proxy(renames["JobStatistics2Out"]).optional(),
            "parentJobId": t.string().optional(),
            "startTime": t.string().optional(),
            "numChildJobs": t.string().optional(),
            "endTime": t.string().optional(),
            "extract": t.proxy(renames["JobStatistics4Out"]).optional(),
            "reservation_id": t.string().optional(),
            "transactionInfo": t.proxy(renames["TransactionInfoOut"]).optional(),
            "quotaDeferments": t.array(t.string()).optional(),
            "totalSlotMs": t.string().optional(),
            "creationTime": t.string().optional(),
            "rowLevelSecurityStatistics": t.proxy(
                renames["RowLevelSecurityStatisticsOut"]
            ).optional(),
            "reservationUsage": t.array(
                t.struct(
                    {"name": t.string().optional(), "slotMs": t.string().optional()}
                )
            ).optional(),
            "load": t.proxy(renames["JobStatistics3Out"]).optional(),
            "sessionInfo": t.proxy(renames["SessionInfoOut"]).optional(),
            "dataMaskingStatistics": t.proxy(
                renames["DataMaskingStatisticsOut"]
            ).optional(),
            "completionRatio": t.number().optional(),
            "copy": t.proxy(renames["JobStatistics5Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobStatisticsOut"])
    types["AggregateClassificationMetricsIn"] = t.struct(
        {
            "logLoss": t.number().optional(),
            "accuracy": t.number().optional(),
            "threshold": t.number().optional(),
            "rocAuc": t.number().optional(),
            "recall": t.number().optional(),
            "precision": t.number().optional(),
            "f1Score": t.number().optional(),
        }
    ).named(renames["AggregateClassificationMetricsIn"])
    types["AggregateClassificationMetricsOut"] = t.struct(
        {
            "logLoss": t.number().optional(),
            "accuracy": t.number().optional(),
            "threshold": t.number().optional(),
            "rocAuc": t.number().optional(),
            "recall": t.number().optional(),
            "precision": t.number().optional(),
            "f1Score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateClassificationMetricsOut"])
    types["BqmlTrainingRunIn"] = t.struct(
        {
            "iterationResults": t.array(
                t.proxy(renames["BqmlIterationResultIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "trainingOptions": t.struct(
                {
                    "l2Reg": t.number(),
                    "learnRateStrategy": t.string(),
                    "maxIteration": t.string(),
                    "warmStart": t.boolean(),
                    "minRelProgress": t.number(),
                    "earlyStop": t.boolean(),
                    "lineSearchInitLearnRate": t.number(),
                    "l1Reg": t.number(),
                    "learnRate": t.number(),
                }
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["BqmlTrainingRunIn"])
    types["BqmlTrainingRunOut"] = t.struct(
        {
            "iterationResults": t.array(
                t.proxy(renames["BqmlIterationResultOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "trainingOptions": t.struct(
                {
                    "l2Reg": t.number(),
                    "learnRateStrategy": t.string(),
                    "maxIteration": t.string(),
                    "warmStart": t.boolean(),
                    "minRelProgress": t.number(),
                    "earlyStop": t.boolean(),
                    "lineSearchInitLearnRate": t.number(),
                    "l1Reg": t.number(),
                    "learnRate": t.number(),
                }
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BqmlTrainingRunOut"])
    types["LocationMetadataIn"] = t.struct(
        {"legacyLocationId": t.string().optional()}
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "legacyLocationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["RoutineIn"] = t.struct(
        {
            "routineReference": t.proxy(renames["RoutineReferenceIn"]),
            "definitionBody": t.string(),
            "strictMode": t.boolean().optional(),
            "remoteFunctionOptions": t.proxy(
                renames["RemoteFunctionOptionsIn"]
            ).optional(),
            "language": t.string().optional(),
            "returnType": t.proxy(renames["StandardSqlDataTypeIn"]).optional(),
            "sparkOptions": t.proxy(renames["SparkOptionsIn"]).optional(),
            "returnTableType": t.proxy(renames["StandardSqlTableTypeIn"]).optional(),
            "description": t.string().optional(),
            "importedLibraries": t.array(t.string()).optional(),
            "determinismLevel": t.string().optional(),
            "arguments": t.array(t.proxy(renames["ArgumentIn"])).optional(),
            "routineType": t.string(),
        }
    ).named(renames["RoutineIn"])
    types["RoutineOut"] = t.struct(
        {
            "routineReference": t.proxy(renames["RoutineReferenceOut"]),
            "definitionBody": t.string(),
            "strictMode": t.boolean().optional(),
            "creationTime": t.string().optional(),
            "remoteFunctionOptions": t.proxy(
                renames["RemoteFunctionOptionsOut"]
            ).optional(),
            "language": t.string().optional(),
            "returnType": t.proxy(renames["StandardSqlDataTypeOut"]).optional(),
            "sparkOptions": t.proxy(renames["SparkOptionsOut"]).optional(),
            "returnTableType": t.proxy(renames["StandardSqlTableTypeOut"]).optional(),
            "lastModifiedTime": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "importedLibraries": t.array(t.string()).optional(),
            "determinismLevel": t.string().optional(),
            "arguments": t.array(t.proxy(renames["ArgumentOut"])).optional(),
            "routineType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutineOut"])
    types["JsonObjectIn"] = t.struct({"_": t.string().optional()}).named(
        renames["JsonObjectIn"]
    )
    types["JsonObjectOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["JsonObjectOut"])
    types["JobIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "user_email": t.string().optional(),
            "configuration": t.proxy(renames["JobConfigurationIn"]).optional(),
            "id": t.string().optional(),
            "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
            "statistics": t.proxy(renames["JobStatisticsIn"]).optional(),
            "selfLink": t.string().optional(),
            "status": t.proxy(renames["JobStatusIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "user_email": t.string().optional(),
            "configuration": t.proxy(renames["JobConfigurationOut"]).optional(),
            "id": t.string().optional(),
            "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
            "statistics": t.proxy(renames["JobStatisticsOut"]).optional(),
            "selfLink": t.string().optional(),
            "status": t.proxy(renames["JobStatusOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
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
    types["TableListIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "tables": t.array(
                t.struct(
                    {
                        "kind": t.string().optional(),
                        "tableReference": t.proxy(
                            renames["TableReferenceIn"]
                        ).optional(),
                        "type": t.string().optional(),
                        "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                        "id": t.string().optional(),
                        "expirationTime": t.string().optional(),
                        "rangePartitioning": t.proxy(
                            renames["RangePartitioningIn"]
                        ).optional(),
                        "creationTime": t.string().optional(),
                        "view": t.struct(
                            {"useLegacySql": t.boolean().optional()}
                        ).optional(),
                        "friendlyName": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "timePartitioning": t.proxy(
                            renames["TimePartitioningIn"]
                        ).optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["TableListIn"])
    types["TableListOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "tables": t.array(
                t.struct(
                    {
                        "kind": t.string().optional(),
                        "tableReference": t.proxy(
                            renames["TableReferenceOut"]
                        ).optional(),
                        "type": t.string().optional(),
                        "clustering": t.proxy(renames["ClusteringOut"]).optional(),
                        "id": t.string().optional(),
                        "expirationTime": t.string().optional(),
                        "rangePartitioning": t.proxy(
                            renames["RangePartitioningOut"]
                        ).optional(),
                        "creationTime": t.string().optional(),
                        "view": t.struct(
                            {"useLegacySql": t.boolean().optional()}
                        ).optional(),
                        "friendlyName": t.string().optional(),
                        "labels": t.struct({"_": t.string().optional()}).optional(),
                        "timePartitioning": t.proxy(
                            renames["TimePartitioningOut"]
                        ).optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableListOut"])
    types["QueryRequestIn"] = t.struct(
        {
            "queryParameters": t.array(t.proxy(renames["QueryParameterIn"])).optional(),
            "parameterMode": t.string().optional(),
            "createSession": t.boolean().optional(),
            "useLegacySql": t.boolean().optional(),
            "useQueryCache": t.boolean().optional(),
            "location": t.string().optional(),
            "continuous": t.boolean().optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "maximumBytesBilled": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "maxResults": t.integer().optional(),
            "requestId": t.string().optional(),
            "kind": t.string().optional(),
            "preserveNulls": t.boolean().optional(),
            "dryRun": t.boolean().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyIn"])
            ).optional(),
            "timeoutMs": t.integer().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["QueryRequestIn"])
    types["QueryRequestOut"] = t.struct(
        {
            "queryParameters": t.array(
                t.proxy(renames["QueryParameterOut"])
            ).optional(),
            "parameterMode": t.string().optional(),
            "createSession": t.boolean().optional(),
            "useLegacySql": t.boolean().optional(),
            "useQueryCache": t.boolean().optional(),
            "location": t.string().optional(),
            "continuous": t.boolean().optional(),
            "defaultDataset": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "maximumBytesBilled": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "maxResults": t.integer().optional(),
            "requestId": t.string().optional(),
            "kind": t.string().optional(),
            "preserveNulls": t.boolean().optional(),
            "dryRun": t.boolean().optional(),
            "connectionProperties": t.array(
                t.proxy(renames["ConnectionPropertyOut"])
            ).optional(),
            "timeoutMs": t.integer().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QueryRequestOut"])
    types["BigtableColumnIn"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "type": t.string().optional(),
            "qualifierString": t.string(),
            "encoding": t.string().optional(),
            "onlyReadLatest": t.boolean().optional(),
            "qualifierEncoded": t.string().optional(),
        }
    ).named(renames["BigtableColumnIn"])
    types["BigtableColumnOut"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "type": t.string().optional(),
            "qualifierString": t.string(),
            "encoding": t.string().optional(),
            "onlyReadLatest": t.boolean().optional(),
            "qualifierEncoded": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigtableColumnOut"])
    types["GetQueryResultsResponseIn"] = t.struct(
        {
            "jobReference": t.proxy(renames["JobReferenceIn"]).optional(),
            "totalBytesProcessed": t.string().optional(),
            "pageToken": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoIn"])).optional(),
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowIn"])).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "jobComplete": t.boolean().optional(),
            "schema": t.proxy(renames["TableSchemaIn"]).optional(),
            "etag": t.string().optional(),
            "totalRows": t.string().optional(),
        }
    ).named(renames["GetQueryResultsResponseIn"])
    types["GetQueryResultsResponseOut"] = t.struct(
        {
            "jobReference": t.proxy(renames["JobReferenceOut"]).optional(),
            "totalBytesProcessed": t.string().optional(),
            "pageToken": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "errors": t.array(t.proxy(renames["ErrorProtoOut"])).optional(),
            "kind": t.string().optional(),
            "rows": t.array(t.proxy(renames["TableRowOut"])).optional(),
            "numDmlAffectedRows": t.string().optional(),
            "jobComplete": t.boolean().optional(),
            "schema": t.proxy(renames["TableSchemaOut"]).optional(),
            "etag": t.string().optional(),
            "totalRows": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetQueryResultsResponseOut"])
    types["DatasetIn"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "defaultCollation": t.string().optional(),
            "datasetReference": t.proxy(renames["DatasetReferenceIn"]).optional(),
            "access": t.array(
                t.struct(
                    {
                        "specialGroup": t.string().optional(),
                        "routine": t.proxy(renames["RoutineReferenceIn"]).optional(),
                        "iamMember": t.string().optional(),
                        "domain": t.string().optional(),
                        "dataset": t.proxy(renames["DatasetAccessEntryIn"]).optional(),
                        "userByEmail": t.string().optional(),
                        "view": t.proxy(renames["TableReferenceIn"]).optional(),
                        "groupByEmail": t.string().optional(),
                        "role": t.string().optional(),
                    }
                )
            ).optional(),
            "defaultTableExpirationMs": t.string().optional(),
            "defaultEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationIn"]
            ),
            "maxTimeTravelHours": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "etag": t.string().optional(),
            "isCaseInsensitive": t.boolean().optional(),
            "defaultRoundingMode": t.string().optional(),
            "tags": t.array(
                t.struct(
                    {"tagKey": t.string().optional(), "tagValue": t.string().optional()}
                )
            ).optional(),
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "defaultPartitionExpirationMs": t.string().optional(),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
            "kind": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "location": t.string().optional(),
            "storageBillingModel": t.string().optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "defaultCollation": t.string().optional(),
            "datasetReference": t.proxy(renames["DatasetReferenceOut"]).optional(),
            "access": t.array(
                t.struct(
                    {
                        "specialGroup": t.string().optional(),
                        "routine": t.proxy(renames["RoutineReferenceOut"]).optional(),
                        "iamMember": t.string().optional(),
                        "domain": t.string().optional(),
                        "dataset": t.proxy(renames["DatasetAccessEntryOut"]).optional(),
                        "userByEmail": t.string().optional(),
                        "view": t.proxy(renames["TableReferenceOut"]).optional(),
                        "groupByEmail": t.string().optional(),
                        "role": t.string().optional(),
                    }
                )
            ).optional(),
            "defaultTableExpirationMs": t.string().optional(),
            "defaultEncryptionConfiguration": t.proxy(
                renames["EncryptionConfigurationOut"]
            ),
            "maxTimeTravelHours": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "etag": t.string().optional(),
            "isCaseInsensitive": t.boolean().optional(),
            "defaultRoundingMode": t.string().optional(),
            "tags": t.array(
                t.struct(
                    {"tagKey": t.string().optional(), "tagValue": t.string().optional()}
                )
            ).optional(),
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "defaultPartitionExpirationMs": t.string().optional(),
            "description": t.string().optional(),
            "friendlyName": t.string().optional(),
            "kind": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "location": t.string().optional(),
            "storageBillingModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["RangePartitioningIn"] = t.struct(
        {
            "range": t.struct(
                {
                    "end": t.string().optional(),
                    "start": t.string().optional(),
                    "interval": t.string().optional(),
                }
            ).optional(),
            "field": t.string().optional(),
        }
    ).named(renames["RangePartitioningIn"])
    types["RangePartitioningOut"] = t.struct(
        {
            "range": t.struct(
                {
                    "end": t.string().optional(),
                    "start": t.string().optional(),
                    "interval": t.string().optional(),
                }
            ).optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangePartitioningOut"])

    functions = {}
    functions["jobsGet"] = bigquery.delete(
        "projects/{projectId}/jobs/{jobId}/delete",
        t.struct(
            {
                "projectId": t.string(),
                "jobId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsQuery"] = bigquery.delete(
        "projects/{projectId}/jobs/{jobId}/delete",
        t.struct(
            {
                "projectId": t.string(),
                "jobId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsCancel"] = bigquery.delete(
        "projects/{projectId}/jobs/{jobId}/delete",
        t.struct(
            {
                "projectId": t.string(),
                "jobId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsGetQueryResults"] = bigquery.delete(
        "projects/{projectId}/jobs/{jobId}/delete",
        t.struct(
            {
                "projectId": t.string(),
                "jobId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsList"] = bigquery.delete(
        "projects/{projectId}/jobs/{jobId}/delete",
        t.struct(
            {
                "projectId": t.string(),
                "jobId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsInsert"] = bigquery.delete(
        "projects/{projectId}/jobs/{jobId}/delete",
        t.struct(
            {
                "projectId": t.string(),
                "jobId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsDelete"] = bigquery.delete(
        "projects/{projectId}/jobs/{jobId}/delete",
        t.struct(
            {
                "projectId": t.string(),
                "jobId": t.string(),
                "location": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetServiceAccount"] = bigquery.get(
        "projects",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = bigquery.get(
        "projects",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["rowAccessPoliciesGetIamPolicy"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies",
        t.struct(
            {
                "datasetId": t.string(),
                "tableId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string(),
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
                "datasetId": t.string(),
                "tableId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string(),
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
                "datasetId": t.string(),
                "tableId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string(),
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
                "datasetId": t.string(),
                "tableId": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsUpdate"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}",
        t.struct(
            {
                "deleteContents": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsInsert"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}",
        t.struct(
            {
                "deleteContents": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsGet"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}",
        t.struct(
            {
                "deleteContents": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsList"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}",
        t.struct(
            {
                "deleteContents": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsPatch"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}",
        t.struct(
            {
                "deleteContents": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["datasetsDelete"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}",
        t.struct(
            {
                "deleteContents": t.boolean().optional(),
                "projectId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesList"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
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
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
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
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesInsert"] = bigquery.patch(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
        t.struct(
            {
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
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
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
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
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
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
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
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
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
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
                "tableId": t.string().optional(),
                "datasetId": t.string().optional(),
                "projectId": t.string().optional(),
                "autodetect_schema": t.boolean().optional(),
                "num_partitions": t.string().optional(),
                "num_active_logical_bytes": t.string().optional(),
                "materializedView": t.proxy(
                    renames["MaterializedViewDefinitionIn"]
                ).optional(),
                "numBytes": t.string().optional(),
                "num_total_physical_bytes": t.string().optional(),
                "num_time_travel_physical_bytes": t.string().optional(),
                "maxStaleness": t.string().optional(),
                "streamingBuffer": t.proxy(renames["StreamingbufferIn"]).optional(),
                "creationTime": t.string().optional(),
                "num_active_physical_bytes": t.string().optional(),
                "view": t.proxy(renames["ViewDefinitionIn"]).optional(),
                "rangePartitioning": t.proxy(renames["RangePartitioningIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "num_long_term_physical_bytes": t.string().optional(),
                "encryptionConfiguration": t.proxy(
                    renames["EncryptionConfigurationIn"]
                ).optional(),
                "clustering": t.proxy(renames["ClusteringIn"]).optional(),
                "snapshotDefinition": t.proxy(
                    renames["SnapshotDefinitionIn"]
                ).optional(),
                "cloneDefinition": t.proxy(renames["CloneDefinitionIn"]).optional(),
                "numPhysicalBytes": t.string().optional(),
                "type": t.string().optional(),
                "kind": t.string().optional(),
                "expirationTime": t.string().optional(),
                "lastModifiedTime": t.string().optional(),
                "timePartitioning": t.proxy(renames["TimePartitioningIn"]).optional(),
                "selfLink": t.string().optional(),
                "numLongTermBytes": t.string().optional(),
                "id": t.string().optional(),
                "defaultRoundingMode": t.string().optional(),
                "schema": t.proxy(renames["TableSchemaIn"]).optional(),
                "location": t.string().optional(),
                "model": t.proxy(renames["ModelDefinitionIn"]).optional(),
                "numRows": t.string().optional(),
                "defaultCollation": t.string().optional(),
                "requirePartitionFilter": t.boolean().optional(),
                "num_total_logical_bytes": t.string().optional(),
                "friendlyName": t.string().optional(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "tableReference": t.proxy(renames["TableReferenceIn"]).optional(),
                "externalDataConfiguration": t.proxy(
                    renames["ExternalDataConfigurationIn"]
                ).optional(),
                "num_long_term_logical_bytes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["modelsGet"] = bigquery.delete(
        "projects/{projectId}/datasets/{datasetId}/models/{modelId}",
        t.struct(
            {
                "datasetId": t.string(),
                "projectId": t.string(),
                "modelId": t.string(),
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
                "datasetId": t.string(),
                "projectId": t.string(),
                "modelId": t.string(),
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
                "datasetId": t.string(),
                "projectId": t.string(),
                "modelId": t.string(),
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
                "datasetId": t.string(),
                "projectId": t.string(),
                "modelId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesDelete"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "datasetId": t.string(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRoutinesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesGet"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "datasetId": t.string(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRoutinesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesUpdate"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "datasetId": t.string(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRoutinesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesInsert"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "datasetId": t.string(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRoutinesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["routinesList"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/routines",
        t.struct(
            {
                "projectId": t.string(),
                "pageToken": t.string().optional(),
                "datasetId": t.string(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRoutinesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tabledataInsertAll"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "startIndex": t.string().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string().optional(),
                "tableId": t.string().optional(),
                "selectedFields": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableDataListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tabledataList"] = bigquery.get(
        "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data",
        t.struct(
            {
                "datasetId": t.string().optional(),
                "startIndex": t.string().optional(),
                "pageToken": t.string().optional(),
                "projectId": t.string().optional(),
                "tableId": t.string().optional(),
                "selectedFields": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TableDataListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigquery", renames=renames, types=Box(types), functions=Box(functions)
    )
