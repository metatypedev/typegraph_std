from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_dlp():
    dlp = HTTPRuntime("https://dlp.googleapis.com/")

    renames = {
        "ErrorResponse": "_dlp_1_ErrorResponse",
        "GooglePrivacyDlpV2HybridFindingDetailsIn": "_dlp_2_GooglePrivacyDlpV2HybridFindingDetailsIn",
        "GooglePrivacyDlpV2HybridFindingDetailsOut": "_dlp_3_GooglePrivacyDlpV2HybridFindingDetailsOut",
        "GooglePrivacyDlpV2InspectContentRequestIn": "_dlp_4_GooglePrivacyDlpV2InspectContentRequestIn",
        "GooglePrivacyDlpV2InspectContentRequestOut": "_dlp_5_GooglePrivacyDlpV2InspectContentRequestOut",
        "GooglePrivacyDlpV2RedactConfigIn": "_dlp_6_GooglePrivacyDlpV2RedactConfigIn",
        "GooglePrivacyDlpV2RedactConfigOut": "_dlp_7_GooglePrivacyDlpV2RedactConfigOut",
        "GooglePrivacyDlpV2DeidentifyDataSourceStatsIn": "_dlp_8_GooglePrivacyDlpV2DeidentifyDataSourceStatsIn",
        "GooglePrivacyDlpV2DeidentifyDataSourceStatsOut": "_dlp_9_GooglePrivacyDlpV2DeidentifyDataSourceStatsOut",
        "GooglePrivacyDlpV2LocationIn": "_dlp_10_GooglePrivacyDlpV2LocationIn",
        "GooglePrivacyDlpV2LocationOut": "_dlp_11_GooglePrivacyDlpV2LocationOut",
        "GooglePrivacyDlpV2ContainerIn": "_dlp_12_GooglePrivacyDlpV2ContainerIn",
        "GooglePrivacyDlpV2ContainerOut": "_dlp_13_GooglePrivacyDlpV2ContainerOut",
        "GooglePrivacyDlpV2SurrogateTypeIn": "_dlp_14_GooglePrivacyDlpV2SurrogateTypeIn",
        "GooglePrivacyDlpV2SurrogateTypeOut": "_dlp_15_GooglePrivacyDlpV2SurrogateTypeOut",
        "GooglePrivacyDlpV2SensitivityScoreIn": "_dlp_16_GooglePrivacyDlpV2SensitivityScoreIn",
        "GooglePrivacyDlpV2SensitivityScoreOut": "_dlp_17_GooglePrivacyDlpV2SensitivityScoreOut",
        "GooglePrivacyDlpV2RecordTransformationIn": "_dlp_18_GooglePrivacyDlpV2RecordTransformationIn",
        "GooglePrivacyDlpV2RecordTransformationOut": "_dlp_19_GooglePrivacyDlpV2RecordTransformationOut",
        "GooglePrivacyDlpV2HybridInspectDlpJobRequestIn": "_dlp_20_GooglePrivacyDlpV2HybridInspectDlpJobRequestIn",
        "GooglePrivacyDlpV2HybridInspectDlpJobRequestOut": "_dlp_21_GooglePrivacyDlpV2HybridInspectDlpJobRequestOut",
        "GoogleProtobufEmptyIn": "_dlp_22_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_dlp_23_GoogleProtobufEmptyOut",
        "GooglePrivacyDlpV2TableOptionsIn": "_dlp_24_GooglePrivacyDlpV2TableOptionsIn",
        "GooglePrivacyDlpV2TableOptionsOut": "_dlp_25_GooglePrivacyDlpV2TableOptionsOut",
        "GooglePrivacyDlpV2DataProfileBigQueryRowSchemaIn": "_dlp_26_GooglePrivacyDlpV2DataProfileBigQueryRowSchemaIn",
        "GooglePrivacyDlpV2DataProfileBigQueryRowSchemaOut": "_dlp_27_GooglePrivacyDlpV2DataProfileBigQueryRowSchemaOut",
        "GooglePrivacyDlpV2BigQueryOptionsIn": "_dlp_28_GooglePrivacyDlpV2BigQueryOptionsIn",
        "GooglePrivacyDlpV2BigQueryOptionsOut": "_dlp_29_GooglePrivacyDlpV2BigQueryOptionsOut",
        "GooglePrivacyDlpV2TransformationOverviewIn": "_dlp_30_GooglePrivacyDlpV2TransformationOverviewIn",
        "GooglePrivacyDlpV2TransformationOverviewOut": "_dlp_31_GooglePrivacyDlpV2TransformationOverviewOut",
        "GooglePrivacyDlpV2DataProfilePubSubConditionIn": "_dlp_32_GooglePrivacyDlpV2DataProfilePubSubConditionIn",
        "GooglePrivacyDlpV2DataProfilePubSubConditionOut": "_dlp_33_GooglePrivacyDlpV2DataProfilePubSubConditionOut",
        "GooglePrivacyDlpV2UpdateJobTriggerRequestIn": "_dlp_34_GooglePrivacyDlpV2UpdateJobTriggerRequestIn",
        "GooglePrivacyDlpV2UpdateJobTriggerRequestOut": "_dlp_35_GooglePrivacyDlpV2UpdateJobTriggerRequestOut",
        "GooglePrivacyDlpV2NumericalStatsConfigIn": "_dlp_36_GooglePrivacyDlpV2NumericalStatsConfigIn",
        "GooglePrivacyDlpV2NumericalStatsConfigOut": "_dlp_37_GooglePrivacyDlpV2NumericalStatsConfigOut",
        "GooglePrivacyDlpV2InspectTemplateIn": "_dlp_38_GooglePrivacyDlpV2InspectTemplateIn",
        "GooglePrivacyDlpV2InspectTemplateOut": "_dlp_39_GooglePrivacyDlpV2InspectTemplateOut",
        "GooglePrivacyDlpV2StatisticalTableIn": "_dlp_40_GooglePrivacyDlpV2StatisticalTableIn",
        "GooglePrivacyDlpV2StatisticalTableOut": "_dlp_41_GooglePrivacyDlpV2StatisticalTableOut",
        "GooglePrivacyDlpV2RiskAnalysisJobConfigIn": "_dlp_42_GooglePrivacyDlpV2RiskAnalysisJobConfigIn",
        "GooglePrivacyDlpV2RiskAnalysisJobConfigOut": "_dlp_43_GooglePrivacyDlpV2RiskAnalysisJobConfigOut",
        "GooglePrivacyDlpV2VersionDescriptionIn": "_dlp_44_GooglePrivacyDlpV2VersionDescriptionIn",
        "GooglePrivacyDlpV2VersionDescriptionOut": "_dlp_45_GooglePrivacyDlpV2VersionDescriptionOut",
        "GooglePrivacyDlpV2HybridOptionsIn": "_dlp_46_GooglePrivacyDlpV2HybridOptionsIn",
        "GooglePrivacyDlpV2HybridOptionsOut": "_dlp_47_GooglePrivacyDlpV2HybridOptionsOut",
        "GooglePrivacyDlpV2DataProfileActionIn": "_dlp_48_GooglePrivacyDlpV2DataProfileActionIn",
        "GooglePrivacyDlpV2DataProfileActionOut": "_dlp_49_GooglePrivacyDlpV2DataProfileActionOut",
        "GooglePrivacyDlpV2RecordKeyIn": "_dlp_50_GooglePrivacyDlpV2RecordKeyIn",
        "GooglePrivacyDlpV2RecordKeyOut": "_dlp_51_GooglePrivacyDlpV2RecordKeyOut",
        "GooglePrivacyDlpV2InfoTypeTransformationsIn": "_dlp_52_GooglePrivacyDlpV2InfoTypeTransformationsIn",
        "GooglePrivacyDlpV2InfoTypeTransformationsOut": "_dlp_53_GooglePrivacyDlpV2InfoTypeTransformationsOut",
        "GooglePrivacyDlpV2DataProfileJobConfigIn": "_dlp_54_GooglePrivacyDlpV2DataProfileJobConfigIn",
        "GooglePrivacyDlpV2DataProfileJobConfigOut": "_dlp_55_GooglePrivacyDlpV2DataProfileJobConfigOut",
        "GooglePrivacyDlpV2OutputStorageConfigIn": "_dlp_56_GooglePrivacyDlpV2OutputStorageConfigIn",
        "GooglePrivacyDlpV2OutputStorageConfigOut": "_dlp_57_GooglePrivacyDlpV2OutputStorageConfigOut",
        "GooglePrivacyDlpV2AllInfoTypesIn": "_dlp_58_GooglePrivacyDlpV2AllInfoTypesIn",
        "GooglePrivacyDlpV2AllInfoTypesOut": "_dlp_59_GooglePrivacyDlpV2AllInfoTypesOut",
        "GooglePrivacyDlpV2CustomInfoTypeIn": "_dlp_60_GooglePrivacyDlpV2CustomInfoTypeIn",
        "GooglePrivacyDlpV2CustomInfoTypeOut": "_dlp_61_GooglePrivacyDlpV2CustomInfoTypeOut",
        "GooglePrivacyDlpV2MetadataLocationIn": "_dlp_62_GooglePrivacyDlpV2MetadataLocationIn",
        "GooglePrivacyDlpV2MetadataLocationOut": "_dlp_63_GooglePrivacyDlpV2MetadataLocationOut",
        "GooglePrivacyDlpV2RecordLocationIn": "_dlp_64_GooglePrivacyDlpV2RecordLocationIn",
        "GooglePrivacyDlpV2RecordLocationOut": "_dlp_65_GooglePrivacyDlpV2RecordLocationOut",
        "GooglePrivacyDlpV2ResultIn": "_dlp_66_GooglePrivacyDlpV2ResultIn",
        "GooglePrivacyDlpV2ResultOut": "_dlp_67_GooglePrivacyDlpV2ResultOut",
        "GooglePrivacyDlpV2ReidentifyContentResponseIn": "_dlp_68_GooglePrivacyDlpV2ReidentifyContentResponseIn",
        "GooglePrivacyDlpV2ReidentifyContentResponseOut": "_dlp_69_GooglePrivacyDlpV2ReidentifyContentResponseOut",
        "GooglePrivacyDlpV2StoredTypeIn": "_dlp_70_GooglePrivacyDlpV2StoredTypeIn",
        "GooglePrivacyDlpV2StoredTypeOut": "_dlp_71_GooglePrivacyDlpV2StoredTypeOut",
        "GooglePrivacyDlpV2ListDlpJobsResponseIn": "_dlp_72_GooglePrivacyDlpV2ListDlpJobsResponseIn",
        "GooglePrivacyDlpV2ListDlpJobsResponseOut": "_dlp_73_GooglePrivacyDlpV2ListDlpJobsResponseOut",
        "GooglePrivacyDlpV2ReplaceValueConfigIn": "_dlp_74_GooglePrivacyDlpV2ReplaceValueConfigIn",
        "GooglePrivacyDlpV2ReplaceValueConfigOut": "_dlp_75_GooglePrivacyDlpV2ReplaceValueConfigOut",
        "GooglePrivacyDlpV2WordListIn": "_dlp_76_GooglePrivacyDlpV2WordListIn",
        "GooglePrivacyDlpV2WordListOut": "_dlp_77_GooglePrivacyDlpV2WordListOut",
        "GooglePrivacyDlpV2CloudStoragePathIn": "_dlp_78_GooglePrivacyDlpV2CloudStoragePathIn",
        "GooglePrivacyDlpV2CloudStoragePathOut": "_dlp_79_GooglePrivacyDlpV2CloudStoragePathOut",
        "GooglePrivacyDlpV2DatastoreKeyIn": "_dlp_80_GooglePrivacyDlpV2DatastoreKeyIn",
        "GooglePrivacyDlpV2DatastoreKeyOut": "_dlp_81_GooglePrivacyDlpV2DatastoreKeyOut",
        "GooglePrivacyDlpV2RegexIn": "_dlp_82_GooglePrivacyDlpV2RegexIn",
        "GooglePrivacyDlpV2RegexOut": "_dlp_83_GooglePrivacyDlpV2RegexOut",
        "GooglePrivacyDlpV2DeidentifyContentRequestIn": "_dlp_84_GooglePrivacyDlpV2DeidentifyContentRequestIn",
        "GooglePrivacyDlpV2DeidentifyContentRequestOut": "_dlp_85_GooglePrivacyDlpV2DeidentifyContentRequestOut",
        "GooglePrivacyDlpV2SaveFindingsIn": "_dlp_86_GooglePrivacyDlpV2SaveFindingsIn",
        "GooglePrivacyDlpV2SaveFindingsOut": "_dlp_87_GooglePrivacyDlpV2SaveFindingsOut",
        "GooglePrivacyDlpV2PublishToStackdriverIn": "_dlp_88_GooglePrivacyDlpV2PublishToStackdriverIn",
        "GooglePrivacyDlpV2PublishToStackdriverOut": "_dlp_89_GooglePrivacyDlpV2PublishToStackdriverOut",
        "GooglePrivacyDlpV2ContentItemIn": "_dlp_90_GooglePrivacyDlpV2ContentItemIn",
        "GooglePrivacyDlpV2ContentItemOut": "_dlp_91_GooglePrivacyDlpV2ContentItemOut",
        "GooglePrivacyDlpV2InspectResultIn": "_dlp_92_GooglePrivacyDlpV2InspectResultIn",
        "GooglePrivacyDlpV2InspectResultOut": "_dlp_93_GooglePrivacyDlpV2InspectResultOut",
        "GooglePrivacyDlpV2InfoTypeIn": "_dlp_94_GooglePrivacyDlpV2InfoTypeIn",
        "GooglePrivacyDlpV2InfoTypeOut": "_dlp_95_GooglePrivacyDlpV2InfoTypeOut",
        "GooglePrivacyDlpV2DlpJobIn": "_dlp_96_GooglePrivacyDlpV2DlpJobIn",
        "GooglePrivacyDlpV2DlpJobOut": "_dlp_97_GooglePrivacyDlpV2DlpJobOut",
        "GooglePrivacyDlpV2CreateInspectTemplateRequestIn": "_dlp_98_GooglePrivacyDlpV2CreateInspectTemplateRequestIn",
        "GooglePrivacyDlpV2CreateInspectTemplateRequestOut": "_dlp_99_GooglePrivacyDlpV2CreateInspectTemplateRequestOut",
        "GooglePrivacyDlpV2TaggedFieldIn": "_dlp_100_GooglePrivacyDlpV2TaggedFieldIn",
        "GooglePrivacyDlpV2TaggedFieldOut": "_dlp_101_GooglePrivacyDlpV2TaggedFieldOut",
        "GooglePrivacyDlpV2CloudStorageRegexFileSetIn": "_dlp_102_GooglePrivacyDlpV2CloudStorageRegexFileSetIn",
        "GooglePrivacyDlpV2CloudStorageRegexFileSetOut": "_dlp_103_GooglePrivacyDlpV2CloudStorageRegexFileSetOut",
        "GooglePrivacyDlpV2TimePartConfigIn": "_dlp_104_GooglePrivacyDlpV2TimePartConfigIn",
        "GooglePrivacyDlpV2TimePartConfigOut": "_dlp_105_GooglePrivacyDlpV2TimePartConfigOut",
        "GooglePrivacyDlpV2DeidentifyTemplateIn": "_dlp_106_GooglePrivacyDlpV2DeidentifyTemplateIn",
        "GooglePrivacyDlpV2DeidentifyTemplateOut": "_dlp_107_GooglePrivacyDlpV2DeidentifyTemplateOut",
        "GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn": "_dlp_108_GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn",
        "GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut": "_dlp_109_GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut",
        "GooglePrivacyDlpV2StoredInfoTypeConfigIn": "_dlp_110_GooglePrivacyDlpV2StoredInfoTypeConfigIn",
        "GooglePrivacyDlpV2StoredInfoTypeConfigOut": "_dlp_111_GooglePrivacyDlpV2StoredInfoTypeConfigOut",
        "GooglePrivacyDlpV2CharsToIgnoreIn": "_dlp_112_GooglePrivacyDlpV2CharsToIgnoreIn",
        "GooglePrivacyDlpV2CharsToIgnoreOut": "_dlp_113_GooglePrivacyDlpV2CharsToIgnoreOut",
        "GooglePrivacyDlpV2TriggerIn": "_dlp_114_GooglePrivacyDlpV2TriggerIn",
        "GooglePrivacyDlpV2TriggerOut": "_dlp_115_GooglePrivacyDlpV2TriggerOut",
        "GooglePrivacyDlpV2ConditionsIn": "_dlp_116_GooglePrivacyDlpV2ConditionsIn",
        "GooglePrivacyDlpV2ConditionsOut": "_dlp_117_GooglePrivacyDlpV2ConditionsOut",
        "GooglePrivacyDlpV2TransientCryptoKeyIn": "_dlp_118_GooglePrivacyDlpV2TransientCryptoKeyIn",
        "GooglePrivacyDlpV2TransientCryptoKeyOut": "_dlp_119_GooglePrivacyDlpV2TransientCryptoKeyOut",
        "GooglePrivacyDlpV2FieldIdIn": "_dlp_120_GooglePrivacyDlpV2FieldIdIn",
        "GooglePrivacyDlpV2FieldIdOut": "_dlp_121_GooglePrivacyDlpV2FieldIdOut",
        "GooglePrivacyDlpV2TransformationResultStatusIn": "_dlp_122_GooglePrivacyDlpV2TransformationResultStatusIn",
        "GooglePrivacyDlpV2TransformationResultStatusOut": "_dlp_123_GooglePrivacyDlpV2TransformationResultStatusOut",
        "GooglePrivacyDlpV2RequestedOptionsIn": "_dlp_124_GooglePrivacyDlpV2RequestedOptionsIn",
        "GooglePrivacyDlpV2RequestedOptionsOut": "_dlp_125_GooglePrivacyDlpV2RequestedOptionsOut",
        "GooglePrivacyDlpV2DeidentifyConfigIn": "_dlp_126_GooglePrivacyDlpV2DeidentifyConfigIn",
        "GooglePrivacyDlpV2DeidentifyConfigOut": "_dlp_127_GooglePrivacyDlpV2DeidentifyConfigOut",
        "GooglePrivacyDlpV2TransformationDescriptionIn": "_dlp_128_GooglePrivacyDlpV2TransformationDescriptionIn",
        "GooglePrivacyDlpV2TransformationDescriptionOut": "_dlp_129_GooglePrivacyDlpV2TransformationDescriptionOut",
        "GooglePrivacyDlpV2LDiversityResultIn": "_dlp_130_GooglePrivacyDlpV2LDiversityResultIn",
        "GooglePrivacyDlpV2LDiversityResultOut": "_dlp_131_GooglePrivacyDlpV2LDiversityResultOut",
        "GooglePrivacyDlpV2ExportIn": "_dlp_132_GooglePrivacyDlpV2ExportIn",
        "GooglePrivacyDlpV2ExportOut": "_dlp_133_GooglePrivacyDlpV2ExportOut",
        "GooglePrivacyDlpV2KMapEstimationConfigIn": "_dlp_134_GooglePrivacyDlpV2KMapEstimationConfigIn",
        "GooglePrivacyDlpV2KMapEstimationConfigOut": "_dlp_135_GooglePrivacyDlpV2KMapEstimationConfigOut",
        "GooglePrivacyDlpV2SelectedInfoTypesIn": "_dlp_136_GooglePrivacyDlpV2SelectedInfoTypesIn",
        "GooglePrivacyDlpV2SelectedInfoTypesOut": "_dlp_137_GooglePrivacyDlpV2SelectedInfoTypesOut",
        "GooglePrivacyDlpV2ActionDetailsIn": "_dlp_138_GooglePrivacyDlpV2ActionDetailsIn",
        "GooglePrivacyDlpV2ActionDetailsOut": "_dlp_139_GooglePrivacyDlpV2ActionDetailsOut",
        "GooglePrivacyDlpV2ExcludeByHotwordIn": "_dlp_140_GooglePrivacyDlpV2ExcludeByHotwordIn",
        "GooglePrivacyDlpV2ExcludeByHotwordOut": "_dlp_141_GooglePrivacyDlpV2ExcludeByHotwordOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn": "_dlp_142_GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut": "_dlp_143_GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut",
        "GooglePrivacyDlpV2KAnonymityResultIn": "_dlp_144_GooglePrivacyDlpV2KAnonymityResultIn",
        "GooglePrivacyDlpV2KAnonymityResultOut": "_dlp_145_GooglePrivacyDlpV2KAnonymityResultOut",
        "GooglePrivacyDlpV2RangeIn": "_dlp_146_GooglePrivacyDlpV2RangeIn",
        "GooglePrivacyDlpV2RangeOut": "_dlp_147_GooglePrivacyDlpV2RangeOut",
        "GooglePrivacyDlpV2CryptoKeyIn": "_dlp_148_GooglePrivacyDlpV2CryptoKeyIn",
        "GooglePrivacyDlpV2CryptoKeyOut": "_dlp_149_GooglePrivacyDlpV2CryptoKeyOut",
        "GooglePrivacyDlpV2FieldTransformationIn": "_dlp_150_GooglePrivacyDlpV2FieldTransformationIn",
        "GooglePrivacyDlpV2FieldTransformationOut": "_dlp_151_GooglePrivacyDlpV2FieldTransformationOut",
        "GooglePrivacyDlpV2QuasiIdIn": "_dlp_152_GooglePrivacyDlpV2QuasiIdIn",
        "GooglePrivacyDlpV2QuasiIdOut": "_dlp_153_GooglePrivacyDlpV2QuasiIdOut",
        "GooglePrivacyDlpV2CloudStorageOptionsIn": "_dlp_154_GooglePrivacyDlpV2CloudStorageOptionsIn",
        "GooglePrivacyDlpV2CloudStorageOptionsOut": "_dlp_155_GooglePrivacyDlpV2CloudStorageOptionsOut",
        "GooglePrivacyDlpV2ImageTransformationIn": "_dlp_156_GooglePrivacyDlpV2ImageTransformationIn",
        "GooglePrivacyDlpV2ImageTransformationOut": "_dlp_157_GooglePrivacyDlpV2ImageTransformationOut",
        "GooglePrivacyDlpV2StoredInfoTypeVersionIn": "_dlp_158_GooglePrivacyDlpV2StoredInfoTypeVersionIn",
        "GooglePrivacyDlpV2StoredInfoTypeVersionOut": "_dlp_159_GooglePrivacyDlpV2StoredInfoTypeVersionOut",
        "GooglePrivacyDlpV2OtherInfoTypeSummaryIn": "_dlp_160_GooglePrivacyDlpV2OtherInfoTypeSummaryIn",
        "GooglePrivacyDlpV2OtherInfoTypeSummaryOut": "_dlp_161_GooglePrivacyDlpV2OtherInfoTypeSummaryOut",
        "GooglePrivacyDlpV2KMapEstimationHistogramBucketIn": "_dlp_162_GooglePrivacyDlpV2KMapEstimationHistogramBucketIn",
        "GooglePrivacyDlpV2KMapEstimationHistogramBucketOut": "_dlp_163_GooglePrivacyDlpV2KMapEstimationHistogramBucketOut",
        "GooglePrivacyDlpV2PubSubConditionIn": "_dlp_164_GooglePrivacyDlpV2PubSubConditionIn",
        "GooglePrivacyDlpV2PubSubConditionOut": "_dlp_165_GooglePrivacyDlpV2PubSubConditionOut",
        "GooglePrivacyDlpV2CreateStoredInfoTypeRequestIn": "_dlp_166_GooglePrivacyDlpV2CreateStoredInfoTypeRequestIn",
        "GooglePrivacyDlpV2CreateStoredInfoTypeRequestOut": "_dlp_167_GooglePrivacyDlpV2CreateStoredInfoTypeRequestOut",
        "GooglePrivacyDlpV2UnwrappedCryptoKeyIn": "_dlp_168_GooglePrivacyDlpV2UnwrappedCryptoKeyIn",
        "GooglePrivacyDlpV2UnwrappedCryptoKeyOut": "_dlp_169_GooglePrivacyDlpV2UnwrappedCryptoKeyOut",
        "GooglePrivacyDlpV2ScheduleIn": "_dlp_170_GooglePrivacyDlpV2ScheduleIn",
        "GooglePrivacyDlpV2ScheduleOut": "_dlp_171_GooglePrivacyDlpV2ScheduleOut",
        "GooglePrivacyDlpV2NumericalStatsResultIn": "_dlp_172_GooglePrivacyDlpV2NumericalStatsResultIn",
        "GooglePrivacyDlpV2NumericalStatsResultOut": "_dlp_173_GooglePrivacyDlpV2NumericalStatsResultOut",
        "GooglePrivacyDlpV2KeyIn": "_dlp_174_GooglePrivacyDlpV2KeyIn",
        "GooglePrivacyDlpV2KeyOut": "_dlp_175_GooglePrivacyDlpV2KeyOut",
        "GooglePrivacyDlpV2ExclusionRuleIn": "_dlp_176_GooglePrivacyDlpV2ExclusionRuleIn",
        "GooglePrivacyDlpV2ExclusionRuleOut": "_dlp_177_GooglePrivacyDlpV2ExclusionRuleOut",
        "GooglePrivacyDlpV2TransformationConfigIn": "_dlp_178_GooglePrivacyDlpV2TransformationConfigIn",
        "GooglePrivacyDlpV2TransformationConfigOut": "_dlp_179_GooglePrivacyDlpV2TransformationConfigOut",
        "GooglePrivacyDlpV2ActivateJobTriggerRequestIn": "_dlp_180_GooglePrivacyDlpV2ActivateJobTriggerRequestIn",
        "GooglePrivacyDlpV2ActivateJobTriggerRequestOut": "_dlp_181_GooglePrivacyDlpV2ActivateJobTriggerRequestOut",
        "GooglePrivacyDlpV2RowIn": "_dlp_182_GooglePrivacyDlpV2RowIn",
        "GooglePrivacyDlpV2RowOut": "_dlp_183_GooglePrivacyDlpV2RowOut",
        "GooglePrivacyDlpV2FinishDlpJobRequestIn": "_dlp_184_GooglePrivacyDlpV2FinishDlpJobRequestIn",
        "GooglePrivacyDlpV2FinishDlpJobRequestOut": "_dlp_185_GooglePrivacyDlpV2FinishDlpJobRequestOut",
        "GooglePrivacyDlpV2InspectJobConfigIn": "_dlp_186_GooglePrivacyDlpV2InspectJobConfigIn",
        "GooglePrivacyDlpV2InspectJobConfigOut": "_dlp_187_GooglePrivacyDlpV2InspectJobConfigOut",
        "GooglePrivacyDlpV2HotwordRuleIn": "_dlp_188_GooglePrivacyDlpV2HotwordRuleIn",
        "GooglePrivacyDlpV2HotwordRuleOut": "_dlp_189_GooglePrivacyDlpV2HotwordRuleOut",
        "GooglePrivacyDlpV2ByteContentItemIn": "_dlp_190_GooglePrivacyDlpV2ByteContentItemIn",
        "GooglePrivacyDlpV2ByteContentItemOut": "_dlp_191_GooglePrivacyDlpV2ByteContentItemOut",
        "GooglePrivacyDlpV2ListJobTriggersResponseIn": "_dlp_192_GooglePrivacyDlpV2ListJobTriggersResponseIn",
        "GooglePrivacyDlpV2ListJobTriggersResponseOut": "_dlp_193_GooglePrivacyDlpV2ListJobTriggersResponseOut",
        "GooglePrivacyDlpV2ListInfoTypesResponseIn": "_dlp_194_GooglePrivacyDlpV2ListInfoTypesResponseIn",
        "GooglePrivacyDlpV2ListInfoTypesResponseOut": "_dlp_195_GooglePrivacyDlpV2ListInfoTypesResponseOut",
        "GooglePrivacyDlpV2RedactImageResponseIn": "_dlp_196_GooglePrivacyDlpV2RedactImageResponseIn",
        "GooglePrivacyDlpV2RedactImageResponseOut": "_dlp_197_GooglePrivacyDlpV2RedactImageResponseOut",
        "GooglePrivacyDlpV2CancelDlpJobRequestIn": "_dlp_198_GooglePrivacyDlpV2CancelDlpJobRequestIn",
        "GooglePrivacyDlpV2CancelDlpJobRequestOut": "_dlp_199_GooglePrivacyDlpV2CancelDlpJobRequestOut",
        "GooglePrivacyDlpV2ColorIn": "_dlp_200_GooglePrivacyDlpV2ColorIn",
        "GooglePrivacyDlpV2ColorOut": "_dlp_201_GooglePrivacyDlpV2ColorOut",
        "GooglePrivacyDlpV2CloudStorageFileSetIn": "_dlp_202_GooglePrivacyDlpV2CloudStorageFileSetIn",
        "GooglePrivacyDlpV2CloudStorageFileSetOut": "_dlp_203_GooglePrivacyDlpV2CloudStorageFileSetOut",
        "GooglePrivacyDlpV2DatastoreOptionsIn": "_dlp_204_GooglePrivacyDlpV2DatastoreOptionsIn",
        "GooglePrivacyDlpV2DatastoreOptionsOut": "_dlp_205_GooglePrivacyDlpV2DatastoreOptionsOut",
        "GoogleTypeDateIn": "_dlp_206_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_dlp_207_GoogleTypeDateOut",
        "GooglePrivacyDlpV2ColumnDataProfileIn": "_dlp_208_GooglePrivacyDlpV2ColumnDataProfileIn",
        "GooglePrivacyDlpV2ColumnDataProfileOut": "_dlp_209_GooglePrivacyDlpV2ColumnDataProfileOut",
        "GooglePrivacyDlpV2HybridInspectStatisticsIn": "_dlp_210_GooglePrivacyDlpV2HybridInspectStatisticsIn",
        "GooglePrivacyDlpV2HybridInspectStatisticsOut": "_dlp_211_GooglePrivacyDlpV2HybridInspectStatisticsOut",
        "GooglePrivacyDlpV2ContentLocationIn": "_dlp_212_GooglePrivacyDlpV2ContentLocationIn",
        "GooglePrivacyDlpV2ContentLocationOut": "_dlp_213_GooglePrivacyDlpV2ContentLocationOut",
        "GooglePrivacyDlpV2TimespanConfigIn": "_dlp_214_GooglePrivacyDlpV2TimespanConfigIn",
        "GooglePrivacyDlpV2TimespanConfigOut": "_dlp_215_GooglePrivacyDlpV2TimespanConfigOut",
        "GooglePrivacyDlpV2CategoricalStatsResultIn": "_dlp_216_GooglePrivacyDlpV2CategoricalStatsResultIn",
        "GooglePrivacyDlpV2CategoricalStatsResultOut": "_dlp_217_GooglePrivacyDlpV2CategoricalStatsResultOut",
        "GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn": "_dlp_218_GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn",
        "GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut": "_dlp_219_GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut",
        "GooglePrivacyDlpV2KindExpressionIn": "_dlp_220_GooglePrivacyDlpV2KindExpressionIn",
        "GooglePrivacyDlpV2KindExpressionOut": "_dlp_221_GooglePrivacyDlpV2KindExpressionOut",
        "GooglePrivacyDlpV2StorageMetadataLabelIn": "_dlp_222_GooglePrivacyDlpV2StorageMetadataLabelIn",
        "GooglePrivacyDlpV2StorageMetadataLabelOut": "_dlp_223_GooglePrivacyDlpV2StorageMetadataLabelOut",
        "GooglePrivacyDlpV2SummaryResultIn": "_dlp_224_GooglePrivacyDlpV2SummaryResultIn",
        "GooglePrivacyDlpV2SummaryResultOut": "_dlp_225_GooglePrivacyDlpV2SummaryResultOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationResultIn": "_dlp_226_GooglePrivacyDlpV2DeltaPresenceEstimationResultIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationResultOut": "_dlp_227_GooglePrivacyDlpV2DeltaPresenceEstimationResultOut",
        "GooglePrivacyDlpV2DetectionRuleIn": "_dlp_228_GooglePrivacyDlpV2DetectionRuleIn",
        "GooglePrivacyDlpV2DetectionRuleOut": "_dlp_229_GooglePrivacyDlpV2DetectionRuleOut",
        "GooglePrivacyDlpV2CryptoDeterministicConfigIn": "_dlp_230_GooglePrivacyDlpV2CryptoDeterministicConfigIn",
        "GooglePrivacyDlpV2CryptoDeterministicConfigOut": "_dlp_231_GooglePrivacyDlpV2CryptoDeterministicConfigOut",
        "GooglePrivacyDlpV2KmsWrappedCryptoKeyIn": "_dlp_232_GooglePrivacyDlpV2KmsWrappedCryptoKeyIn",
        "GooglePrivacyDlpV2KmsWrappedCryptoKeyOut": "_dlp_233_GooglePrivacyDlpV2KmsWrappedCryptoKeyOut",
        "GooglePrivacyDlpV2TransformationDetailsStorageConfigIn": "_dlp_234_GooglePrivacyDlpV2TransformationDetailsStorageConfigIn",
        "GooglePrivacyDlpV2TransformationDetailsStorageConfigOut": "_dlp_235_GooglePrivacyDlpV2TransformationDetailsStorageConfigOut",
        "GooglePrivacyDlpV2ManualIn": "_dlp_236_GooglePrivacyDlpV2ManualIn",
        "GooglePrivacyDlpV2ManualOut": "_dlp_237_GooglePrivacyDlpV2ManualOut",
        "GooglePrivacyDlpV2InfoTypeDescriptionIn": "_dlp_238_GooglePrivacyDlpV2InfoTypeDescriptionIn",
        "GooglePrivacyDlpV2InfoTypeDescriptionOut": "_dlp_239_GooglePrivacyDlpV2InfoTypeDescriptionOut",
        "GooglePrivacyDlpV2LeaveUntransformedIn": "_dlp_240_GooglePrivacyDlpV2LeaveUntransformedIn",
        "GooglePrivacyDlpV2LeaveUntransformedOut": "_dlp_241_GooglePrivacyDlpV2LeaveUntransformedOut",
        "GooglePrivacyDlpV2ExcludeInfoTypesIn": "_dlp_242_GooglePrivacyDlpV2ExcludeInfoTypesIn",
        "GooglePrivacyDlpV2ExcludeInfoTypesOut": "_dlp_243_GooglePrivacyDlpV2ExcludeInfoTypesOut",
        "GooglePrivacyDlpV2FindingIn": "_dlp_244_GooglePrivacyDlpV2FindingIn",
        "GooglePrivacyDlpV2FindingOut": "_dlp_245_GooglePrivacyDlpV2FindingOut",
        "GooglePrivacyDlpV2DataRiskLevelIn": "_dlp_246_GooglePrivacyDlpV2DataRiskLevelIn",
        "GooglePrivacyDlpV2DataRiskLevelOut": "_dlp_247_GooglePrivacyDlpV2DataRiskLevelOut",
        "GooglePrivacyDlpV2TimeZoneIn": "_dlp_248_GooglePrivacyDlpV2TimeZoneIn",
        "GooglePrivacyDlpV2TimeZoneOut": "_dlp_249_GooglePrivacyDlpV2TimeZoneOut",
        "GoogleRpcStatusIn": "_dlp_250_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_dlp_251_GoogleRpcStatusOut",
        "GooglePrivacyDlpV2ValueIn": "_dlp_252_GooglePrivacyDlpV2ValueIn",
        "GooglePrivacyDlpV2ValueOut": "_dlp_253_GooglePrivacyDlpV2ValueOut",
        "GooglePrivacyDlpV2InspectConfigIn": "_dlp_254_GooglePrivacyDlpV2InspectConfigIn",
        "GooglePrivacyDlpV2InspectConfigOut": "_dlp_255_GooglePrivacyDlpV2InspectConfigOut",
        "GooglePrivacyDlpV2BucketIn": "_dlp_256_GooglePrivacyDlpV2BucketIn",
        "GooglePrivacyDlpV2BucketOut": "_dlp_257_GooglePrivacyDlpV2BucketOut",
        "GooglePrivacyDlpV2PrivacyMetricIn": "_dlp_258_GooglePrivacyDlpV2PrivacyMetricIn",
        "GooglePrivacyDlpV2PrivacyMetricOut": "_dlp_259_GooglePrivacyDlpV2PrivacyMetricOut",
        "GooglePrivacyDlpV2DateShiftConfigIn": "_dlp_260_GooglePrivacyDlpV2DateShiftConfigIn",
        "GooglePrivacyDlpV2DateShiftConfigOut": "_dlp_261_GooglePrivacyDlpV2DateShiftConfigOut",
        "GooglePrivacyDlpV2DeidentifyIn": "_dlp_262_GooglePrivacyDlpV2DeidentifyIn",
        "GooglePrivacyDlpV2DeidentifyOut": "_dlp_263_GooglePrivacyDlpV2DeidentifyOut",
        "GooglePrivacyDlpV2ReplaceDictionaryConfigIn": "_dlp_264_GooglePrivacyDlpV2ReplaceDictionaryConfigIn",
        "GooglePrivacyDlpV2ReplaceDictionaryConfigOut": "_dlp_265_GooglePrivacyDlpV2ReplaceDictionaryConfigOut",
        "GooglePrivacyDlpV2LDiversityEquivalenceClassIn": "_dlp_266_GooglePrivacyDlpV2LDiversityEquivalenceClassIn",
        "GooglePrivacyDlpV2LDiversityEquivalenceClassOut": "_dlp_267_GooglePrivacyDlpV2LDiversityEquivalenceClassOut",
        "GooglePrivacyDlpV2KMapEstimationResultIn": "_dlp_268_GooglePrivacyDlpV2KMapEstimationResultIn",
        "GooglePrivacyDlpV2KMapEstimationResultOut": "_dlp_269_GooglePrivacyDlpV2KMapEstimationResultOut",
        "GooglePrivacyDlpV2AllTextIn": "_dlp_270_GooglePrivacyDlpV2AllTextIn",
        "GooglePrivacyDlpV2AllTextOut": "_dlp_271_GooglePrivacyDlpV2AllTextOut",
        "GooglePrivacyDlpV2FindingLimitsIn": "_dlp_272_GooglePrivacyDlpV2FindingLimitsIn",
        "GooglePrivacyDlpV2FindingLimitsOut": "_dlp_273_GooglePrivacyDlpV2FindingLimitsOut",
        "GooglePrivacyDlpV2DictionaryIn": "_dlp_274_GooglePrivacyDlpV2DictionaryIn",
        "GooglePrivacyDlpV2DictionaryOut": "_dlp_275_GooglePrivacyDlpV2DictionaryOut",
        "GooglePrivacyDlpV2FileSetIn": "_dlp_276_GooglePrivacyDlpV2FileSetIn",
        "GooglePrivacyDlpV2FileSetOut": "_dlp_277_GooglePrivacyDlpV2FileSetOut",
        "GooglePrivacyDlpV2RecordConditionIn": "_dlp_278_GooglePrivacyDlpV2RecordConditionIn",
        "GooglePrivacyDlpV2RecordConditionOut": "_dlp_279_GooglePrivacyDlpV2RecordConditionOut",
        "GooglePrivacyDlpV2DataProfilePubSubMessageIn": "_dlp_280_GooglePrivacyDlpV2DataProfilePubSubMessageIn",
        "GooglePrivacyDlpV2DataProfilePubSubMessageOut": "_dlp_281_GooglePrivacyDlpV2DataProfilePubSubMessageOut",
        "GooglePrivacyDlpV2BigQueryTableIn": "_dlp_282_GooglePrivacyDlpV2BigQueryTableIn",
        "GooglePrivacyDlpV2BigQueryTableOut": "_dlp_283_GooglePrivacyDlpV2BigQueryTableOut",
        "GooglePrivacyDlpV2JobNotificationEmailsIn": "_dlp_284_GooglePrivacyDlpV2JobNotificationEmailsIn",
        "GooglePrivacyDlpV2JobNotificationEmailsOut": "_dlp_285_GooglePrivacyDlpV2JobNotificationEmailsOut",
        "GooglePrivacyDlpV2TableDataProfileIn": "_dlp_286_GooglePrivacyDlpV2TableDataProfileIn",
        "GooglePrivacyDlpV2TableDataProfileOut": "_dlp_287_GooglePrivacyDlpV2TableDataProfileOut",
        "GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn": "_dlp_288_GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn",
        "GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut": "_dlp_289_GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut",
        "GooglePrivacyDlpV2ProximityIn": "_dlp_290_GooglePrivacyDlpV2ProximityIn",
        "GooglePrivacyDlpV2ProximityOut": "_dlp_291_GooglePrivacyDlpV2ProximityOut",
        "GooglePrivacyDlpV2InfoTypeTransformationIn": "_dlp_292_GooglePrivacyDlpV2InfoTypeTransformationIn",
        "GooglePrivacyDlpV2InfoTypeTransformationOut": "_dlp_293_GooglePrivacyDlpV2InfoTypeTransformationOut",
        "GooglePrivacyDlpV2InspectDataSourceDetailsIn": "_dlp_294_GooglePrivacyDlpV2InspectDataSourceDetailsIn",
        "GooglePrivacyDlpV2InspectDataSourceDetailsOut": "_dlp_295_GooglePrivacyDlpV2InspectDataSourceDetailsOut",
        "GooglePrivacyDlpV2PathElementIn": "_dlp_296_GooglePrivacyDlpV2PathElementIn",
        "GooglePrivacyDlpV2PathElementOut": "_dlp_297_GooglePrivacyDlpV2PathElementOut",
        "GooglePrivacyDlpV2ImageTransformationsIn": "_dlp_298_GooglePrivacyDlpV2ImageTransformationsIn",
        "GooglePrivacyDlpV2ImageTransformationsOut": "_dlp_299_GooglePrivacyDlpV2ImageTransformationsOut",
        "GooglePrivacyDlpV2ConditionIn": "_dlp_300_GooglePrivacyDlpV2ConditionIn",
        "GooglePrivacyDlpV2ConditionOut": "_dlp_301_GooglePrivacyDlpV2ConditionOut",
        "GooglePrivacyDlpV2UpdateInspectTemplateRequestIn": "_dlp_302_GooglePrivacyDlpV2UpdateInspectTemplateRequestIn",
        "GooglePrivacyDlpV2UpdateInspectTemplateRequestOut": "_dlp_303_GooglePrivacyDlpV2UpdateInspectTemplateRequestOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn": "_dlp_304_GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut": "_dlp_305_GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut",
        "GooglePrivacyDlpV2DataProfileLocationIn": "_dlp_306_GooglePrivacyDlpV2DataProfileLocationIn",
        "GooglePrivacyDlpV2DataProfileLocationOut": "_dlp_307_GooglePrivacyDlpV2DataProfileLocationOut",
        "GooglePrivacyDlpV2HybridContentItemIn": "_dlp_308_GooglePrivacyDlpV2HybridContentItemIn",
        "GooglePrivacyDlpV2HybridContentItemOut": "_dlp_309_GooglePrivacyDlpV2HybridContentItemOut",
        "GooglePrivacyDlpV2ImageLocationIn": "_dlp_310_GooglePrivacyDlpV2ImageLocationIn",
        "GooglePrivacyDlpV2ImageLocationOut": "_dlp_311_GooglePrivacyDlpV2ImageLocationOut",
        "GooglePrivacyDlpV2LargeCustomDictionaryStatsIn": "_dlp_312_GooglePrivacyDlpV2LargeCustomDictionaryStatsIn",
        "GooglePrivacyDlpV2LargeCustomDictionaryStatsOut": "_dlp_313_GooglePrivacyDlpV2LargeCustomDictionaryStatsOut",
        "GooglePrivacyDlpV2ReidentifyContentRequestIn": "_dlp_314_GooglePrivacyDlpV2ReidentifyContentRequestIn",
        "GooglePrivacyDlpV2ReidentifyContentRequestOut": "_dlp_315_GooglePrivacyDlpV2ReidentifyContentRequestOut",
        "GooglePrivacyDlpV2KAnonymityConfigIn": "_dlp_316_GooglePrivacyDlpV2KAnonymityConfigIn",
        "GooglePrivacyDlpV2KAnonymityConfigOut": "_dlp_317_GooglePrivacyDlpV2KAnonymityConfigOut",
        "GooglePrivacyDlpV2HybridInspectJobTriggerRequestIn": "_dlp_318_GooglePrivacyDlpV2HybridInspectJobTriggerRequestIn",
        "GooglePrivacyDlpV2HybridInspectJobTriggerRequestOut": "_dlp_319_GooglePrivacyDlpV2HybridInspectJobTriggerRequestOut",
        "GooglePrivacyDlpV2InfoTypeCategoryIn": "_dlp_320_GooglePrivacyDlpV2InfoTypeCategoryIn",
        "GooglePrivacyDlpV2InfoTypeCategoryOut": "_dlp_321_GooglePrivacyDlpV2InfoTypeCategoryOut",
        "GooglePrivacyDlpV2RecordSuppressionIn": "_dlp_322_GooglePrivacyDlpV2RecordSuppressionIn",
        "GooglePrivacyDlpV2RecordSuppressionOut": "_dlp_323_GooglePrivacyDlpV2RecordSuppressionOut",
        "GooglePrivacyDlpV2BucketingConfigIn": "_dlp_324_GooglePrivacyDlpV2BucketingConfigIn",
        "GooglePrivacyDlpV2BucketingConfigOut": "_dlp_325_GooglePrivacyDlpV2BucketingConfigOut",
        "GooglePrivacyDlpV2TransformationSummaryIn": "_dlp_326_GooglePrivacyDlpV2TransformationSummaryIn",
        "GooglePrivacyDlpV2TransformationSummaryOut": "_dlp_327_GooglePrivacyDlpV2TransformationSummaryOut",
        "GooglePrivacyDlpV2CreateJobTriggerRequestIn": "_dlp_328_GooglePrivacyDlpV2CreateJobTriggerRequestIn",
        "GooglePrivacyDlpV2CreateJobTriggerRequestOut": "_dlp_329_GooglePrivacyDlpV2CreateJobTriggerRequestOut",
        "GooglePrivacyDlpV2TransformationLocationIn": "_dlp_330_GooglePrivacyDlpV2TransformationLocationIn",
        "GooglePrivacyDlpV2TransformationLocationOut": "_dlp_331_GooglePrivacyDlpV2TransformationLocationOut",
        "GooglePrivacyDlpV2FixedSizeBucketingConfigIn": "_dlp_332_GooglePrivacyDlpV2FixedSizeBucketingConfigIn",
        "GooglePrivacyDlpV2FixedSizeBucketingConfigOut": "_dlp_333_GooglePrivacyDlpV2FixedSizeBucketingConfigOut",
        "GooglePrivacyDlpV2DocumentLocationIn": "_dlp_334_GooglePrivacyDlpV2DocumentLocationIn",
        "GooglePrivacyDlpV2DocumentLocationOut": "_dlp_335_GooglePrivacyDlpV2DocumentLocationOut",
        "GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn": "_dlp_336_GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn",
        "GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut": "_dlp_337_GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut",
        "GooglePrivacyDlpV2RedactImageRequestIn": "_dlp_338_GooglePrivacyDlpV2RedactImageRequestIn",
        "GooglePrivacyDlpV2RedactImageRequestOut": "_dlp_339_GooglePrivacyDlpV2RedactImageRequestOut",
        "GooglePrivacyDlpV2StoredInfoTypeIn": "_dlp_340_GooglePrivacyDlpV2StoredInfoTypeIn",
        "GooglePrivacyDlpV2StoredInfoTypeOut": "_dlp_341_GooglePrivacyDlpV2StoredInfoTypeOut",
        "GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn": "_dlp_342_GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn",
        "GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut": "_dlp_343_GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut",
        "GooglePrivacyDlpV2StoredInfoTypeStatsIn": "_dlp_344_GooglePrivacyDlpV2StoredInfoTypeStatsIn",
        "GooglePrivacyDlpV2StoredInfoTypeStatsOut": "_dlp_345_GooglePrivacyDlpV2StoredInfoTypeStatsOut",
        "GooglePrivacyDlpV2ThrowErrorIn": "_dlp_346_GooglePrivacyDlpV2ThrowErrorIn",
        "GooglePrivacyDlpV2ThrowErrorOut": "_dlp_347_GooglePrivacyDlpV2ThrowErrorOut",
        "GooglePrivacyDlpV2DateTimeIn": "_dlp_348_GooglePrivacyDlpV2DateTimeIn",
        "GooglePrivacyDlpV2DateTimeOut": "_dlp_349_GooglePrivacyDlpV2DateTimeOut",
        "GooglePrivacyDlpV2ImageRedactionConfigIn": "_dlp_350_GooglePrivacyDlpV2ImageRedactionConfigIn",
        "GooglePrivacyDlpV2ImageRedactionConfigOut": "_dlp_351_GooglePrivacyDlpV2ImageRedactionConfigOut",
        "GooglePrivacyDlpV2CategoricalStatsConfigIn": "_dlp_352_GooglePrivacyDlpV2CategoricalStatsConfigIn",
        "GooglePrivacyDlpV2CategoricalStatsConfigOut": "_dlp_353_GooglePrivacyDlpV2CategoricalStatsConfigOut",
        "GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn": "_dlp_354_GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn",
        "GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut": "_dlp_355_GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut",
        "GooglePrivacyDlpV2DeidentifyContentResponseIn": "_dlp_356_GooglePrivacyDlpV2DeidentifyContentResponseIn",
        "GooglePrivacyDlpV2DeidentifyContentResponseOut": "_dlp_357_GooglePrivacyDlpV2DeidentifyContentResponseOut",
        "GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn": "_dlp_358_GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn",
        "GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut": "_dlp_359_GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut",
        "GooglePrivacyDlpV2PublishToPubSubIn": "_dlp_360_GooglePrivacyDlpV2PublishToPubSubIn",
        "GooglePrivacyDlpV2PublishToPubSubOut": "_dlp_361_GooglePrivacyDlpV2PublishToPubSubOut",
        "GooglePrivacyDlpV2ListInspectTemplatesResponseIn": "_dlp_362_GooglePrivacyDlpV2ListInspectTemplatesResponseIn",
        "GooglePrivacyDlpV2ListInspectTemplatesResponseOut": "_dlp_363_GooglePrivacyDlpV2ListInspectTemplatesResponseOut",
        "GooglePrivacyDlpV2TransformationDetailsIn": "_dlp_364_GooglePrivacyDlpV2TransformationDetailsIn",
        "GooglePrivacyDlpV2TransformationDetailsOut": "_dlp_365_GooglePrivacyDlpV2TransformationDetailsOut",
        "GooglePrivacyDlpV2EntityIdIn": "_dlp_366_GooglePrivacyDlpV2EntityIdIn",
        "GooglePrivacyDlpV2EntityIdOut": "_dlp_367_GooglePrivacyDlpV2EntityIdOut",
        "GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn": "_dlp_368_GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn",
        "GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut": "_dlp_369_GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut",
        "GooglePrivacyDlpV2ProfileStatusIn": "_dlp_370_GooglePrivacyDlpV2ProfileStatusIn",
        "GooglePrivacyDlpV2ProfileStatusOut": "_dlp_371_GooglePrivacyDlpV2ProfileStatusOut",
        "GoogleTypeTimeOfDayIn": "_dlp_372_GoogleTypeTimeOfDayIn",
        "GoogleTypeTimeOfDayOut": "_dlp_373_GoogleTypeTimeOfDayOut",
        "GooglePrivacyDlpV2ErrorIn": "_dlp_374_GooglePrivacyDlpV2ErrorIn",
        "GooglePrivacyDlpV2ErrorOut": "_dlp_375_GooglePrivacyDlpV2ErrorOut",
        "GooglePrivacyDlpV2PartitionIdIn": "_dlp_376_GooglePrivacyDlpV2PartitionIdIn",
        "GooglePrivacyDlpV2PartitionIdOut": "_dlp_377_GooglePrivacyDlpV2PartitionIdOut",
        "GooglePrivacyDlpV2ActionIn": "_dlp_378_GooglePrivacyDlpV2ActionIn",
        "GooglePrivacyDlpV2ActionOut": "_dlp_379_GooglePrivacyDlpV2ActionOut",
        "GooglePrivacyDlpV2InspectContentResponseIn": "_dlp_380_GooglePrivacyDlpV2InspectContentResponseIn",
        "GooglePrivacyDlpV2InspectContentResponseOut": "_dlp_381_GooglePrivacyDlpV2InspectContentResponseOut",
        "GooglePrivacyDlpV2LikelihoodAdjustmentIn": "_dlp_382_GooglePrivacyDlpV2LikelihoodAdjustmentIn",
        "GooglePrivacyDlpV2LikelihoodAdjustmentOut": "_dlp_383_GooglePrivacyDlpV2LikelihoodAdjustmentOut",
        "GooglePrivacyDlpV2DataProfileConfigSnapshotIn": "_dlp_384_GooglePrivacyDlpV2DataProfileConfigSnapshotIn",
        "GooglePrivacyDlpV2DataProfileConfigSnapshotOut": "_dlp_385_GooglePrivacyDlpV2DataProfileConfigSnapshotOut",
        "GooglePrivacyDlpV2PubSubNotificationIn": "_dlp_386_GooglePrivacyDlpV2PubSubNotificationIn",
        "GooglePrivacyDlpV2PubSubNotificationOut": "_dlp_387_GooglePrivacyDlpV2PubSubNotificationOut",
        "GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn": "_dlp_388_GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn",
        "GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut": "_dlp_389_GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut",
        "GooglePrivacyDlpV2InspectionRuleSetIn": "_dlp_390_GooglePrivacyDlpV2InspectionRuleSetIn",
        "GooglePrivacyDlpV2InspectionRuleSetOut": "_dlp_391_GooglePrivacyDlpV2InspectionRuleSetOut",
        "GooglePrivacyDlpV2RecordTransformationsIn": "_dlp_392_GooglePrivacyDlpV2RecordTransformationsIn",
        "GooglePrivacyDlpV2RecordTransformationsOut": "_dlp_393_GooglePrivacyDlpV2RecordTransformationsOut",
        "GooglePrivacyDlpV2PublishSummaryToCsccIn": "_dlp_394_GooglePrivacyDlpV2PublishSummaryToCsccIn",
        "GooglePrivacyDlpV2PublishSummaryToCsccOut": "_dlp_395_GooglePrivacyDlpV2PublishSummaryToCsccOut",
        "GooglePrivacyDlpV2HybridInspectResponseIn": "_dlp_396_GooglePrivacyDlpV2HybridInspectResponseIn",
        "GooglePrivacyDlpV2HybridInspectResponseOut": "_dlp_397_GooglePrivacyDlpV2HybridInspectResponseOut",
        "GooglePrivacyDlpV2InfoTypeSummaryIn": "_dlp_398_GooglePrivacyDlpV2InfoTypeSummaryIn",
        "GooglePrivacyDlpV2InfoTypeSummaryOut": "_dlp_399_GooglePrivacyDlpV2InfoTypeSummaryOut",
        "GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestIn": "_dlp_400_GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestIn",
        "GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestOut": "_dlp_401_GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestOut",
        "GooglePrivacyDlpV2QuasiIdentifierFieldIn": "_dlp_402_GooglePrivacyDlpV2QuasiIdentifierFieldIn",
        "GooglePrivacyDlpV2QuasiIdentifierFieldOut": "_dlp_403_GooglePrivacyDlpV2QuasiIdentifierFieldOut",
        "GooglePrivacyDlpV2BigQueryKeyIn": "_dlp_404_GooglePrivacyDlpV2BigQueryKeyIn",
        "GooglePrivacyDlpV2BigQueryKeyOut": "_dlp_405_GooglePrivacyDlpV2BigQueryKeyOut",
        "GooglePrivacyDlpV2LDiversityConfigIn": "_dlp_406_GooglePrivacyDlpV2LDiversityConfigIn",
        "GooglePrivacyDlpV2LDiversityConfigOut": "_dlp_407_GooglePrivacyDlpV2LDiversityConfigOut",
        "GooglePrivacyDlpV2RequestedDeidentifyOptionsIn": "_dlp_408_GooglePrivacyDlpV2RequestedDeidentifyOptionsIn",
        "GooglePrivacyDlpV2RequestedDeidentifyOptionsOut": "_dlp_409_GooglePrivacyDlpV2RequestedDeidentifyOptionsOut",
        "GooglePrivacyDlpV2LDiversityHistogramBucketIn": "_dlp_410_GooglePrivacyDlpV2LDiversityHistogramBucketIn",
        "GooglePrivacyDlpV2LDiversityHistogramBucketOut": "_dlp_411_GooglePrivacyDlpV2LDiversityHistogramBucketOut",
        "GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn": "_dlp_412_GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn",
        "GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut": "_dlp_413_GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut",
        "GooglePrivacyDlpV2KAnonymityEquivalenceClassIn": "_dlp_414_GooglePrivacyDlpV2KAnonymityEquivalenceClassIn",
        "GooglePrivacyDlpV2KAnonymityEquivalenceClassOut": "_dlp_415_GooglePrivacyDlpV2KAnonymityEquivalenceClassOut",
        "GooglePrivacyDlpV2TableLocationIn": "_dlp_416_GooglePrivacyDlpV2TableLocationIn",
        "GooglePrivacyDlpV2TableLocationOut": "_dlp_417_GooglePrivacyDlpV2TableLocationOut",
        "GooglePrivacyDlpV2CryptoHashConfigIn": "_dlp_418_GooglePrivacyDlpV2CryptoHashConfigIn",
        "GooglePrivacyDlpV2CryptoHashConfigOut": "_dlp_419_GooglePrivacyDlpV2CryptoHashConfigOut",
        "GooglePrivacyDlpV2InspectionRuleIn": "_dlp_420_GooglePrivacyDlpV2InspectionRuleIn",
        "GooglePrivacyDlpV2InspectionRuleOut": "_dlp_421_GooglePrivacyDlpV2InspectionRuleOut",
        "GooglePrivacyDlpV2PubSubExpressionsIn": "_dlp_422_GooglePrivacyDlpV2PubSubExpressionsIn",
        "GooglePrivacyDlpV2PubSubExpressionsOut": "_dlp_423_GooglePrivacyDlpV2PubSubExpressionsOut",
        "GooglePrivacyDlpV2StorageConfigIn": "_dlp_424_GooglePrivacyDlpV2StorageConfigIn",
        "GooglePrivacyDlpV2StorageConfigOut": "_dlp_425_GooglePrivacyDlpV2StorageConfigOut",
        "GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn": "_dlp_426_GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn",
        "GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut": "_dlp_427_GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut",
        "GooglePrivacyDlpV2QuoteInfoIn": "_dlp_428_GooglePrivacyDlpV2QuoteInfoIn",
        "GooglePrivacyDlpV2QuoteInfoOut": "_dlp_429_GooglePrivacyDlpV2QuoteInfoOut",
        "GooglePrivacyDlpV2InfoTypeLimitIn": "_dlp_430_GooglePrivacyDlpV2InfoTypeLimitIn",
        "GooglePrivacyDlpV2InfoTypeLimitOut": "_dlp_431_GooglePrivacyDlpV2InfoTypeLimitOut",
        "GooglePrivacyDlpV2BigQueryFieldIn": "_dlp_432_GooglePrivacyDlpV2BigQueryFieldIn",
        "GooglePrivacyDlpV2BigQueryFieldOut": "_dlp_433_GooglePrivacyDlpV2BigQueryFieldOut",
        "GooglePrivacyDlpV2ExpressionsIn": "_dlp_434_GooglePrivacyDlpV2ExpressionsIn",
        "GooglePrivacyDlpV2ExpressionsOut": "_dlp_435_GooglePrivacyDlpV2ExpressionsOut",
        "GooglePrivacyDlpV2KAnonymityHistogramBucketIn": "_dlp_436_GooglePrivacyDlpV2KAnonymityHistogramBucketIn",
        "GooglePrivacyDlpV2KAnonymityHistogramBucketOut": "_dlp_437_GooglePrivacyDlpV2KAnonymityHistogramBucketOut",
        "GooglePrivacyDlpV2InfoTypeStatsIn": "_dlp_438_GooglePrivacyDlpV2InfoTypeStatsIn",
        "GooglePrivacyDlpV2InfoTypeStatsOut": "_dlp_439_GooglePrivacyDlpV2InfoTypeStatsOut",
        "GooglePrivacyDlpV2TableIn": "_dlp_440_GooglePrivacyDlpV2TableIn",
        "GooglePrivacyDlpV2TableOut": "_dlp_441_GooglePrivacyDlpV2TableOut",
        "GooglePrivacyDlpV2CharacterMaskConfigIn": "_dlp_442_GooglePrivacyDlpV2CharacterMaskConfigIn",
        "GooglePrivacyDlpV2CharacterMaskConfigOut": "_dlp_443_GooglePrivacyDlpV2CharacterMaskConfigOut",
        "GooglePrivacyDlpV2ValueFrequencyIn": "_dlp_444_GooglePrivacyDlpV2ValueFrequencyIn",
        "GooglePrivacyDlpV2ValueFrequencyOut": "_dlp_445_GooglePrivacyDlpV2ValueFrequencyOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn": "_dlp_446_GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut": "_dlp_447_GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut",
        "GooglePrivacyDlpV2ListStoredInfoTypesResponseIn": "_dlp_448_GooglePrivacyDlpV2ListStoredInfoTypesResponseIn",
        "GooglePrivacyDlpV2ListStoredInfoTypesResponseOut": "_dlp_449_GooglePrivacyDlpV2ListStoredInfoTypesResponseOut",
        "GooglePrivacyDlpV2QuasiIdFieldIn": "_dlp_450_GooglePrivacyDlpV2QuasiIdFieldIn",
        "GooglePrivacyDlpV2QuasiIdFieldOut": "_dlp_451_GooglePrivacyDlpV2QuasiIdFieldOut",
        "GooglePrivacyDlpV2CreateDlpJobRequestIn": "_dlp_452_GooglePrivacyDlpV2CreateDlpJobRequestIn",
        "GooglePrivacyDlpV2CreateDlpJobRequestOut": "_dlp_453_GooglePrivacyDlpV2CreateDlpJobRequestOut",
        "GooglePrivacyDlpV2TransformationErrorHandlingIn": "_dlp_454_GooglePrivacyDlpV2TransformationErrorHandlingIn",
        "GooglePrivacyDlpV2TransformationErrorHandlingOut": "_dlp_455_GooglePrivacyDlpV2TransformationErrorHandlingOut",
        "GooglePrivacyDlpV2LargeCustomDictionaryConfigIn": "_dlp_456_GooglePrivacyDlpV2LargeCustomDictionaryConfigIn",
        "GooglePrivacyDlpV2LargeCustomDictionaryConfigOut": "_dlp_457_GooglePrivacyDlpV2LargeCustomDictionaryConfigOut",
        "GooglePrivacyDlpV2BoundingBoxIn": "_dlp_458_GooglePrivacyDlpV2BoundingBoxIn",
        "GooglePrivacyDlpV2BoundingBoxOut": "_dlp_459_GooglePrivacyDlpV2BoundingBoxOut",
        "GooglePrivacyDlpV2JobTriggerIn": "_dlp_460_GooglePrivacyDlpV2JobTriggerIn",
        "GooglePrivacyDlpV2JobTriggerOut": "_dlp_461_GooglePrivacyDlpV2JobTriggerOut",
        "GooglePrivacyDlpV2AuxiliaryTableIn": "_dlp_462_GooglePrivacyDlpV2AuxiliaryTableIn",
        "GooglePrivacyDlpV2AuxiliaryTableOut": "_dlp_463_GooglePrivacyDlpV2AuxiliaryTableOut",
        "GooglePrivacyDlpV2PrimitiveTransformationIn": "_dlp_464_GooglePrivacyDlpV2PrimitiveTransformationIn",
        "GooglePrivacyDlpV2PrimitiveTransformationOut": "_dlp_465_GooglePrivacyDlpV2PrimitiveTransformationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GooglePrivacyDlpV2HybridFindingDetailsIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsIn"]
            ).optional(),
            "rowOffset": t.string().optional(),
            "fileOffset": t.string().optional(),
            "containerDetails": t.proxy(
                renames["GooglePrivacyDlpV2ContainerIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridFindingDetailsIn"])
    types["GooglePrivacyDlpV2HybridFindingDetailsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsOut"]
            ).optional(),
            "rowOffset": t.string().optional(),
            "fileOffset": t.string().optional(),
            "containerDetails": t.proxy(
                renames["GooglePrivacyDlpV2ContainerOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridFindingDetailsOut"])
    types["GooglePrivacyDlpV2InspectContentRequestIn"] = t.struct(
        {
            "inspectTemplateName": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectContentRequestIn"])
    types["GooglePrivacyDlpV2InspectContentRequestOut"] = t.struct(
        {
            "inspectTemplateName": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectContentRequestOut"])
    types["GooglePrivacyDlpV2RedactConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2RedactConfigIn"])
    types["GooglePrivacyDlpV2RedactConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2RedactConfigOut"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceStatsIn"] = t.struct(
        {
            "transformedBytes": t.string().optional(),
            "transformationCount": t.string().optional(),
            "transformationErrorCount": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsIn"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceStatsOut"] = t.struct(
        {
            "transformedBytes": t.string().optional(),
            "transformationCount": t.string().optional(),
            "transformationErrorCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsOut"])
    types["GooglePrivacyDlpV2LocationIn"] = t.struct(
        {
            "contentLocations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ContentLocationIn"])
            ).optional(),
            "byteRange": t.proxy(renames["GooglePrivacyDlpV2RangeIn"]).optional(),
            "codepointRange": t.proxy(renames["GooglePrivacyDlpV2RangeIn"]).optional(),
            "container": t.proxy(renames["GooglePrivacyDlpV2ContainerIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LocationIn"])
    types["GooglePrivacyDlpV2LocationOut"] = t.struct(
        {
            "contentLocations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ContentLocationOut"])
            ).optional(),
            "byteRange": t.proxy(renames["GooglePrivacyDlpV2RangeOut"]).optional(),
            "codepointRange": t.proxy(renames["GooglePrivacyDlpV2RangeOut"]).optional(),
            "container": t.proxy(renames["GooglePrivacyDlpV2ContainerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LocationOut"])
    types["GooglePrivacyDlpV2ContainerIn"] = t.struct(
        {
            "fullPath": t.string().optional(),
            "type": t.string().optional(),
            "projectId": t.string().optional(),
            "rootPath": t.string().optional(),
            "relativePath": t.string().optional(),
            "version": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContainerIn"])
    types["GooglePrivacyDlpV2ContainerOut"] = t.struct(
        {
            "fullPath": t.string().optional(),
            "type": t.string().optional(),
            "projectId": t.string().optional(),
            "rootPath": t.string().optional(),
            "relativePath": t.string().optional(),
            "version": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContainerOut"])
    types["GooglePrivacyDlpV2SurrogateTypeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2SurrogateTypeIn"])
    types["GooglePrivacyDlpV2SurrogateTypeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2SurrogateTypeOut"])
    types["GooglePrivacyDlpV2SensitivityScoreIn"] = t.struct(
        {"score": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2SensitivityScoreIn"])
    types["GooglePrivacyDlpV2SensitivityScoreOut"] = t.struct(
        {
            "score": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SensitivityScoreOut"])
    types["GooglePrivacyDlpV2RecordTransformationIn"] = t.struct(
        {
            "containerVersion": t.string().optional(),
            "fieldId": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "containerTimestamp": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationIn"])
    types["GooglePrivacyDlpV2RecordTransformationOut"] = t.struct(
        {
            "containerVersion": t.string().optional(),
            "fieldId": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "containerTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationOut"])
    types["GooglePrivacyDlpV2HybridInspectDlpJobRequestIn"] = t.struct(
        {
            "hybridItem": t.proxy(
                renames["GooglePrivacyDlpV2HybridContentItemIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectDlpJobRequestIn"])
    types["GooglePrivacyDlpV2HybridInspectDlpJobRequestOut"] = t.struct(
        {
            "hybridItem": t.proxy(
                renames["GooglePrivacyDlpV2HybridContentItemOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectDlpJobRequestOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GooglePrivacyDlpV2TableOptionsIn"] = t.struct(
        {
            "identifyingFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2TableOptionsIn"])
    types["GooglePrivacyDlpV2TableOptionsOut"] = t.struct(
        {
            "identifyingFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableOptionsOut"])
    types["GooglePrivacyDlpV2DataProfileBigQueryRowSchemaIn"] = t.struct(
        {
            "columnProfile": t.proxy(
                renames["GooglePrivacyDlpV2ColumnDataProfileIn"]
            ).optional(),
            "tableProfile": t.proxy(
                renames["GooglePrivacyDlpV2TableDataProfileIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileBigQueryRowSchemaIn"])
    types["GooglePrivacyDlpV2DataProfileBigQueryRowSchemaOut"] = t.struct(
        {
            "columnProfile": t.proxy(
                renames["GooglePrivacyDlpV2ColumnDataProfileOut"]
            ).optional(),
            "tableProfile": t.proxy(
                renames["GooglePrivacyDlpV2TableDataProfileOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileBigQueryRowSchemaOut"])
    types["GooglePrivacyDlpV2BigQueryOptionsIn"] = t.struct(
        {
            "sampleMethod": t.string(),
            "includedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
            "rowsLimitPercent": t.integer().optional(),
            "identifyingFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
            "rowsLimit": t.string().optional(),
            "excludedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
            "tableReference": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryOptionsIn"])
    types["GooglePrivacyDlpV2BigQueryOptionsOut"] = t.struct(
        {
            "sampleMethod": t.string(),
            "includedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "rowsLimitPercent": t.integer().optional(),
            "identifyingFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "rowsLimit": t.string().optional(),
            "excludedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "tableReference": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryOptionsOut"])
    types["GooglePrivacyDlpV2TransformationOverviewIn"] = t.struct(
        {
            "transformedBytes": t.string().optional(),
            "transformationSummaries": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationSummaryIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationOverviewIn"])
    types["GooglePrivacyDlpV2TransformationOverviewOut"] = t.struct(
        {
            "transformedBytes": t.string().optional(),
            "transformationSummaries": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationSummaryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationOverviewOut"])
    types["GooglePrivacyDlpV2DataProfilePubSubConditionIn"] = t.struct(
        {
            "expressions": t.proxy(
                renames["GooglePrivacyDlpV2PubSubExpressionsIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2DataProfilePubSubConditionIn"])
    types["GooglePrivacyDlpV2DataProfilePubSubConditionOut"] = t.struct(
        {
            "expressions": t.proxy(
                renames["GooglePrivacyDlpV2PubSubExpressionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfilePubSubConditionOut"])
    types["GooglePrivacyDlpV2UpdateJobTriggerRequestIn"] = t.struct(
        {
            "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateJobTriggerRequestIn"])
    types["GooglePrivacyDlpV2UpdateJobTriggerRequestOut"] = t.struct(
        {
            "jobTrigger": t.proxy(
                renames["GooglePrivacyDlpV2JobTriggerOut"]
            ).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateJobTriggerRequestOut"])
    types["GooglePrivacyDlpV2NumericalStatsConfigIn"] = t.struct(
        {"field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2NumericalStatsConfigIn"])
    types["GooglePrivacyDlpV2NumericalStatsConfigOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2NumericalStatsConfigOut"])
    types["GooglePrivacyDlpV2InspectTemplateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectTemplateIn"])
    types["GooglePrivacyDlpV2InspectTemplateOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectTemplateOut"])
    types["GooglePrivacyDlpV2StatisticalTableIn"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableIn"]),
            "relativeFrequency": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2QuasiIdentifierFieldIn"])
            ),
        }
    ).named(renames["GooglePrivacyDlpV2StatisticalTableIn"])
    types["GooglePrivacyDlpV2StatisticalTableOut"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableOut"]),
            "relativeFrequency": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2QuasiIdentifierFieldOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StatisticalTableOut"])
    types["GooglePrivacyDlpV2RiskAnalysisJobConfigIn"] = t.struct(
        {
            "privacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricIn"]
            ).optional(),
            "sourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional(),
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RiskAnalysisJobConfigIn"])
    types["GooglePrivacyDlpV2RiskAnalysisJobConfigOut"] = t.struct(
        {
            "privacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricOut"]
            ).optional(),
            "sourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RiskAnalysisJobConfigOut"])
    types["GooglePrivacyDlpV2VersionDescriptionIn"] = t.struct(
        {"version": t.string().optional(), "description": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2VersionDescriptionIn"])
    types["GooglePrivacyDlpV2VersionDescriptionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2VersionDescriptionOut"])
    types["GooglePrivacyDlpV2HybridOptionsIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "requiredFindingLabelKeys": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridOptionsIn"])
    types["GooglePrivacyDlpV2HybridOptionsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "requiredFindingLabelKeys": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridOptionsOut"])
    types["GooglePrivacyDlpV2DataProfileActionIn"] = t.struct(
        {
            "exportData": t.proxy(renames["GooglePrivacyDlpV2ExportIn"]).optional(),
            "pubSubNotification": t.proxy(
                renames["GooglePrivacyDlpV2PubSubNotificationIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileActionIn"])
    types["GooglePrivacyDlpV2DataProfileActionOut"] = t.struct(
        {
            "exportData": t.proxy(renames["GooglePrivacyDlpV2ExportOut"]).optional(),
            "pubSubNotification": t.proxy(
                renames["GooglePrivacyDlpV2PubSubNotificationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileActionOut"])
    types["GooglePrivacyDlpV2RecordKeyIn"] = t.struct(
        {
            "datastoreKey": t.proxy(renames["GooglePrivacyDlpV2DatastoreKeyIn"]),
            "bigQueryKey": t.proxy(renames["GooglePrivacyDlpV2BigQueryKeyIn"]),
            "idValues": t.array(t.string()).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordKeyIn"])
    types["GooglePrivacyDlpV2RecordKeyOut"] = t.struct(
        {
            "datastoreKey": t.proxy(renames["GooglePrivacyDlpV2DatastoreKeyOut"]),
            "bigQueryKey": t.proxy(renames["GooglePrivacyDlpV2BigQueryKeyOut"]),
            "idValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordKeyOut"])
    types["GooglePrivacyDlpV2InfoTypeTransformationsIn"] = t.struct(
        {
            "transformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeTransformationIn"])
            )
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeTransformationsIn"])
    types["GooglePrivacyDlpV2InfoTypeTransformationsOut"] = t.struct(
        {
            "transformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeTransformationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeTransformationsOut"])
    types["GooglePrivacyDlpV2DataProfileJobConfigIn"] = t.struct(
        {
            "dataProfileActions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DataProfileActionIn"])
            ).optional(),
            "location": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileLocationIn"]
            ).optional(),
            "inspectTemplates": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileJobConfigIn"])
    types["GooglePrivacyDlpV2DataProfileJobConfigOut"] = t.struct(
        {
            "dataProfileActions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DataProfileActionOut"])
            ).optional(),
            "location": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileLocationOut"]
            ).optional(),
            "inspectTemplates": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileJobConfigOut"])
    types["GooglePrivacyDlpV2OutputStorageConfigIn"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableIn"]).optional(),
            "outputSchema": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2OutputStorageConfigIn"])
    types["GooglePrivacyDlpV2OutputStorageConfigOut"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableOut"]).optional(),
            "outputSchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2OutputStorageConfigOut"])
    types["GooglePrivacyDlpV2AllInfoTypesIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2AllInfoTypesIn"])
    types["GooglePrivacyDlpV2AllInfoTypesOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2AllInfoTypesOut"])
    types["GooglePrivacyDlpV2CustomInfoTypeIn"] = t.struct(
        {
            "exclusionType": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
            "likelihood": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "dictionary": t.proxy(renames["GooglePrivacyDlpV2DictionaryIn"]).optional(),
            "detectionRules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DetectionRuleIn"])
            ).optional(),
            "storedType": t.proxy(renames["GooglePrivacyDlpV2StoredTypeIn"]).optional(),
            "surrogateType": t.proxy(
                renames["GooglePrivacyDlpV2SurrogateTypeIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CustomInfoTypeIn"])
    types["GooglePrivacyDlpV2CustomInfoTypeOut"] = t.struct(
        {
            "exclusionType": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "likelihood": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "dictionary": t.proxy(
                renames["GooglePrivacyDlpV2DictionaryOut"]
            ).optional(),
            "detectionRules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DetectionRuleOut"])
            ).optional(),
            "storedType": t.proxy(
                renames["GooglePrivacyDlpV2StoredTypeOut"]
            ).optional(),
            "surrogateType": t.proxy(
                renames["GooglePrivacyDlpV2SurrogateTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CustomInfoTypeOut"])
    types["GooglePrivacyDlpV2MetadataLocationIn"] = t.struct(
        {
            "storageLabel": t.proxy(
                renames["GooglePrivacyDlpV2StorageMetadataLabelIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2MetadataLocationIn"])
    types["GooglePrivacyDlpV2MetadataLocationOut"] = t.struct(
        {
            "storageLabel": t.proxy(
                renames["GooglePrivacyDlpV2StorageMetadataLabelOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2MetadataLocationOut"])
    types["GooglePrivacyDlpV2RecordLocationIn"] = t.struct(
        {
            "recordKey": t.proxy(renames["GooglePrivacyDlpV2RecordKeyIn"]).optional(),
            "fieldId": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "tableLocation": t.proxy(
                renames["GooglePrivacyDlpV2TableLocationIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordLocationIn"])
    types["GooglePrivacyDlpV2RecordLocationOut"] = t.struct(
        {
            "recordKey": t.proxy(renames["GooglePrivacyDlpV2RecordKeyOut"]).optional(),
            "fieldId": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "tableLocation": t.proxy(
                renames["GooglePrivacyDlpV2TableLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordLocationOut"])
    types["GooglePrivacyDlpV2ResultIn"] = t.struct(
        {
            "infoTypeStats": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeStatsIn"])
            ).optional(),
            "hybridStats": t.proxy(
                renames["GooglePrivacyDlpV2HybridInspectStatisticsIn"]
            ).optional(),
            "totalEstimatedBytes": t.string().optional(),
            "processedBytes": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ResultIn"])
    types["GooglePrivacyDlpV2ResultOut"] = t.struct(
        {
            "infoTypeStats": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeStatsOut"])
            ).optional(),
            "hybridStats": t.proxy(
                renames["GooglePrivacyDlpV2HybridInspectStatisticsOut"]
            ).optional(),
            "totalEstimatedBytes": t.string().optional(),
            "processedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ResultOut"])
    types["GooglePrivacyDlpV2ReidentifyContentResponseIn"] = t.struct(
        {
            "overview": t.proxy(
                renames["GooglePrivacyDlpV2TransformationOverviewIn"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReidentifyContentResponseIn"])
    types["GooglePrivacyDlpV2ReidentifyContentResponseOut"] = t.struct(
        {
            "overview": t.proxy(
                renames["GooglePrivacyDlpV2TransformationOverviewOut"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReidentifyContentResponseOut"])
    types["GooglePrivacyDlpV2StoredTypeIn"] = t.struct(
        {"createTime": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2StoredTypeIn"])
    types["GooglePrivacyDlpV2StoredTypeOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredTypeOut"])
    types["GooglePrivacyDlpV2ListDlpJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["GooglePrivacyDlpV2DlpJobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDlpJobsResponseIn"])
    types["GooglePrivacyDlpV2ListDlpJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDlpJobsResponseOut"])
    types["GooglePrivacyDlpV2ReplaceValueConfigIn"] = t.struct(
        {"newValue": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceValueConfigIn"])
    types["GooglePrivacyDlpV2ReplaceValueConfigOut"] = t.struct(
        {
            "newValue": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReplaceValueConfigOut"])
    types["GooglePrivacyDlpV2WordListIn"] = t.struct(
        {"words": t.array(t.string()).optional()}
    ).named(renames["GooglePrivacyDlpV2WordListIn"])
    types["GooglePrivacyDlpV2WordListOut"] = t.struct(
        {
            "words": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2WordListOut"])
    types["GooglePrivacyDlpV2CloudStoragePathIn"] = t.struct(
        {"path": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2CloudStoragePathIn"])
    types["GooglePrivacyDlpV2CloudStoragePathOut"] = t.struct(
        {
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStoragePathOut"])
    types["GooglePrivacyDlpV2DatastoreKeyIn"] = t.struct(
        {"entityKey": t.proxy(renames["GooglePrivacyDlpV2KeyIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2DatastoreKeyIn"])
    types["GooglePrivacyDlpV2DatastoreKeyOut"] = t.struct(
        {
            "entityKey": t.proxy(renames["GooglePrivacyDlpV2KeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DatastoreKeyOut"])
    types["GooglePrivacyDlpV2RegexIn"] = t.struct(
        {
            "groupIndexes": t.array(t.integer()).optional(),
            "pattern": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RegexIn"])
    types["GooglePrivacyDlpV2RegexOut"] = t.struct(
        {
            "groupIndexes": t.array(t.integer()).optional(),
            "pattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RegexOut"])
    types["GooglePrivacyDlpV2DeidentifyContentRequestIn"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
            ).optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "deidentifyTemplateName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentRequestIn"])
    types["GooglePrivacyDlpV2DeidentifyContentRequestOut"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigOut"]
            ).optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "deidentifyTemplateName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentRequestOut"])
    types["GooglePrivacyDlpV2SaveFindingsIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GooglePrivacyDlpV2OutputStorageConfigIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2SaveFindingsIn"])
    types["GooglePrivacyDlpV2SaveFindingsOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GooglePrivacyDlpV2OutputStorageConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SaveFindingsOut"])
    types["GooglePrivacyDlpV2PublishToStackdriverIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishToStackdriverIn"])
    types["GooglePrivacyDlpV2PublishToStackdriverOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2PublishToStackdriverOut"])
    types["GooglePrivacyDlpV2ContentItemIn"] = t.struct(
        {
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemIn"]
            ).optional(),
            "value": t.string().optional(),
            "table": t.proxy(renames["GooglePrivacyDlpV2TableIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentItemIn"])
    types["GooglePrivacyDlpV2ContentItemOut"] = t.struct(
        {
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemOut"]
            ).optional(),
            "value": t.string().optional(),
            "table": t.proxy(renames["GooglePrivacyDlpV2TableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentItemOut"])
    types["GooglePrivacyDlpV2InspectResultIn"] = t.struct(
        {
            "findingsTruncated": t.boolean().optional(),
            "findings": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FindingIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectResultIn"])
    types["GooglePrivacyDlpV2InspectResultOut"] = t.struct(
        {
            "findingsTruncated": t.boolean().optional(),
            "findings": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FindingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectResultOut"])
    types["GooglePrivacyDlpV2InfoTypeIn"] = t.struct(
        {
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeIn"])
    types["GooglePrivacyDlpV2InfoTypeOut"] = t.struct(
        {
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeOut"])
    types["GooglePrivacyDlpV2DlpJobIn"] = t.struct(
        {
            "name": t.string().optional(),
            "inspectDetails": t.proxy(
                renames["GooglePrivacyDlpV2InspectDataSourceDetailsIn"]
            ).optional(),
            "riskDetails": t.proxy(
                renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn"]
            ).optional(),
            "createTime": t.string().optional(),
            "actionDetails": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionDetailsIn"])
            ).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["GooglePrivacyDlpV2ErrorIn"])).optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "jobTriggerName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DlpJobIn"])
    types["GooglePrivacyDlpV2DlpJobOut"] = t.struct(
        {
            "name": t.string().optional(),
            "inspectDetails": t.proxy(
                renames["GooglePrivacyDlpV2InspectDataSourceDetailsOut"]
            ).optional(),
            "riskDetails": t.proxy(
                renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "actionDetails": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionDetailsOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ErrorOut"])
            ).optional(),
            "type": t.string().optional(),
            "startTime": t.string().optional(),
            "jobTriggerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DlpJobOut"])
    types["GooglePrivacyDlpV2CreateInspectTemplateRequestIn"] = t.struct(
        {
            "templateId": t.string().optional(),
            "inspectTemplate": t.proxy(renames["GooglePrivacyDlpV2InspectTemplateIn"]),
            "locationId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateInspectTemplateRequestIn"])
    types["GooglePrivacyDlpV2CreateInspectTemplateRequestOut"] = t.struct(
        {
            "templateId": t.string().optional(),
            "inspectTemplate": t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateInspectTemplateRequestOut"])
    types["GooglePrivacyDlpV2TaggedFieldIn"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "customTag": t.string().optional(),
            "inferred": t.proxy(renames["GoogleProtobufEmptyIn"]).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2TaggedFieldIn"])
    types["GooglePrivacyDlpV2TaggedFieldOut"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "customTag": t.string().optional(),
            "inferred": t.proxy(renames["GoogleProtobufEmptyOut"]).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TaggedFieldOut"])
    types["GooglePrivacyDlpV2CloudStorageRegexFileSetIn"] = t.struct(
        {
            "excludeRegex": t.array(t.string()).optional(),
            "includeRegex": t.array(t.string()).optional(),
            "bucketName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageRegexFileSetIn"])
    types["GooglePrivacyDlpV2CloudStorageRegexFileSetOut"] = t.struct(
        {
            "excludeRegex": t.array(t.string()).optional(),
            "includeRegex": t.array(t.string()).optional(),
            "bucketName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageRegexFileSetOut"])
    types["GooglePrivacyDlpV2TimePartConfigIn"] = t.struct(
        {"partToExtract": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2TimePartConfigIn"])
    types["GooglePrivacyDlpV2TimePartConfigOut"] = t.struct(
        {
            "partToExtract": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimePartConfigOut"])
    types["GooglePrivacyDlpV2DeidentifyTemplateIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyTemplateIn"])
    types["GooglePrivacyDlpV2DeidentifyTemplateOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"])
    types["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn"] = t.struct(
        {
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
            "estimatedAnonymity": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn"])
    types["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut"] = t.struct(
        {
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "estimatedAnonymity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut"])
    types["GooglePrivacyDlpV2StoredInfoTypeConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
            "displayName": t.string().optional(),
            "dictionary": t.proxy(renames["GooglePrivacyDlpV2DictionaryIn"]).optional(),
            "largeCustomDictionary": t.proxy(
                renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"])
    types["GooglePrivacyDlpV2StoredInfoTypeConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "displayName": t.string().optional(),
            "dictionary": t.proxy(
                renames["GooglePrivacyDlpV2DictionaryOut"]
            ).optional(),
            "largeCustomDictionary": t.proxy(
                renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeConfigOut"])
    types["GooglePrivacyDlpV2CharsToIgnoreIn"] = t.struct(
        {
            "commonCharactersToIgnore": t.string().optional(),
            "charactersToSkip": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharsToIgnoreIn"])
    types["GooglePrivacyDlpV2CharsToIgnoreOut"] = t.struct(
        {
            "commonCharactersToIgnore": t.string().optional(),
            "charactersToSkip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharsToIgnoreOut"])
    types["GooglePrivacyDlpV2TriggerIn"] = t.struct(
        {
            "manual": t.proxy(renames["GooglePrivacyDlpV2ManualIn"]).optional(),
            "schedule": t.proxy(renames["GooglePrivacyDlpV2ScheduleIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TriggerIn"])
    types["GooglePrivacyDlpV2TriggerOut"] = t.struct(
        {
            "manual": t.proxy(renames["GooglePrivacyDlpV2ManualOut"]).optional(),
            "schedule": t.proxy(renames["GooglePrivacyDlpV2ScheduleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TriggerOut"])
    types["GooglePrivacyDlpV2ConditionsIn"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ConditionIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2ConditionsIn"])
    types["GooglePrivacyDlpV2ConditionsOut"] = t.struct(
        {
            "conditions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ConditionsOut"])
    types["GooglePrivacyDlpV2TransientCryptoKeyIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["GooglePrivacyDlpV2TransientCryptoKeyIn"])
    types["GooglePrivacyDlpV2TransientCryptoKeyOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2TransientCryptoKeyOut"])
    types["GooglePrivacyDlpV2FieldIdIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2FieldIdIn"])
    types["GooglePrivacyDlpV2FieldIdOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FieldIdOut"])
    types["GooglePrivacyDlpV2TransformationResultStatusIn"] = t.struct(
        {
            "details": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "resultStatusType": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationResultStatusIn"])
    types["GooglePrivacyDlpV2TransformationResultStatusOut"] = t.struct(
        {
            "details": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "resultStatusType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationResultStatusOut"])
    types["GooglePrivacyDlpV2RequestedOptionsIn"] = t.struct(
        {
            "snapshotInspectTemplate": t.proxy(
                renames["GooglePrivacyDlpV2InspectTemplateIn"]
            ).optional(),
            "jobConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RequestedOptionsIn"])
    types["GooglePrivacyDlpV2RequestedOptionsOut"] = t.struct(
        {
            "snapshotInspectTemplate": t.proxy(
                renames["GooglePrivacyDlpV2InspectTemplateOut"]
            ).optional(),
            "jobConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RequestedOptionsOut"])
    types["GooglePrivacyDlpV2DeidentifyConfigIn"] = t.struct(
        {
            "transformationErrorHandling": t.proxy(
                renames["GooglePrivacyDlpV2TransformationErrorHandlingIn"]
            ).optional(),
            "infoTypeTransformations": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeTransformationsIn"]
            ).optional(),
            "imageTransformations": t.proxy(
                renames["GooglePrivacyDlpV2ImageTransformationsIn"]
            ).optional(),
            "recordTransformations": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyConfigIn"])
    types["GooglePrivacyDlpV2DeidentifyConfigOut"] = t.struct(
        {
            "transformationErrorHandling": t.proxy(
                renames["GooglePrivacyDlpV2TransformationErrorHandlingOut"]
            ).optional(),
            "infoTypeTransformations": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeTransformationsOut"]
            ).optional(),
            "imageTransformations": t.proxy(
                renames["GooglePrivacyDlpV2ImageTransformationsOut"]
            ).optional(),
            "recordTransformations": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyConfigOut"])
    types["GooglePrivacyDlpV2TransformationDescriptionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDescriptionIn"])
    types["GooglePrivacyDlpV2TransformationDescriptionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "condition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDescriptionOut"])
    types["GooglePrivacyDlpV2LDiversityResultIn"] = t.struct(
        {
            "sensitiveValueFrequencyHistogramBuckets": t.array(
                t.proxy(renames["GooglePrivacyDlpV2LDiversityHistogramBucketIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityResultIn"])
    types["GooglePrivacyDlpV2LDiversityResultOut"] = t.struct(
        {
            "sensitiveValueFrequencyHistogramBuckets": t.array(
                t.proxy(renames["GooglePrivacyDlpV2LDiversityHistogramBucketOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityResultOut"])
    types["GooglePrivacyDlpV2ExportIn"] = t.struct(
        {
            "profileTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2ExportIn"])
    types["GooglePrivacyDlpV2ExportOut"] = t.struct(
        {
            "profileTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExportOut"])
    types["GooglePrivacyDlpV2KMapEstimationConfigIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2TaggedFieldIn"])),
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2AuxiliaryTableIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationConfigIn"])
    types["GooglePrivacyDlpV2KMapEstimationConfigOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2TaggedFieldOut"])),
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2AuxiliaryTableOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationConfigOut"])
    types["GooglePrivacyDlpV2SelectedInfoTypesIn"] = t.struct(
        {"infoTypes": t.array(t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]))}
    ).named(renames["GooglePrivacyDlpV2SelectedInfoTypesIn"])
    types["GooglePrivacyDlpV2SelectedInfoTypesOut"] = t.struct(
        {
            "infoTypes": t.array(t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SelectedInfoTypesOut"])
    types["GooglePrivacyDlpV2ActionDetailsIn"] = t.struct(
        {
            "deidentifyDetails": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2ActionDetailsIn"])
    types["GooglePrivacyDlpV2ActionDetailsOut"] = t.struct(
        {
            "deidentifyDetails": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ActionDetailsOut"])
    types["GooglePrivacyDlpV2ExcludeByHotwordIn"] = t.struct(
        {
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityIn"]).optional(),
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExcludeByHotwordIn"])
    types["GooglePrivacyDlpV2ExcludeByHotwordOut"] = t.struct(
        {
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityOut"]).optional(),
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExcludeByHotwordOut"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2QuasiIdIn"])),
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StatisticalTableIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2QuasiIdOut"])),
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StatisticalTableOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut"])
    types["GooglePrivacyDlpV2KAnonymityResultIn"] = t.struct(
        {
            "equivalenceClassHistogramBuckets": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KAnonymityHistogramBucketIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityResultIn"])
    types["GooglePrivacyDlpV2KAnonymityResultOut"] = t.struct(
        {
            "equivalenceClassHistogramBuckets": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KAnonymityHistogramBucketOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityResultOut"])
    types["GooglePrivacyDlpV2RangeIn"] = t.struct(
        {"end": t.string().optional(), "start": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2RangeIn"])
    types["GooglePrivacyDlpV2RangeOut"] = t.struct(
        {
            "end": t.string().optional(),
            "start": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RangeOut"])
    types["GooglePrivacyDlpV2CryptoKeyIn"] = t.struct(
        {
            "transient": t.proxy(
                renames["GooglePrivacyDlpV2TransientCryptoKeyIn"]
            ).optional(),
            "unwrapped": t.proxy(
                renames["GooglePrivacyDlpV2UnwrappedCryptoKeyIn"]
            ).optional(),
            "kmsWrapped": t.proxy(
                renames["GooglePrivacyDlpV2KmsWrappedCryptoKeyIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoKeyIn"])
    types["GooglePrivacyDlpV2CryptoKeyOut"] = t.struct(
        {
            "transient": t.proxy(
                renames["GooglePrivacyDlpV2TransientCryptoKeyOut"]
            ).optional(),
            "unwrapped": t.proxy(
                renames["GooglePrivacyDlpV2UnwrappedCryptoKeyOut"]
            ).optional(),
            "kmsWrapped": t.proxy(
                renames["GooglePrivacyDlpV2KmsWrappedCryptoKeyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoKeyOut"])
    types["GooglePrivacyDlpV2FieldTransformationIn"] = t.struct(
        {
            "condition": t.proxy(
                renames["GooglePrivacyDlpV2RecordConditionIn"]
            ).optional(),
            "infoTypeTransformations": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeTransformationsIn"]
            ).optional(),
            "fields": t.array(t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])),
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FieldTransformationIn"])
    types["GooglePrivacyDlpV2FieldTransformationOut"] = t.struct(
        {
            "condition": t.proxy(
                renames["GooglePrivacyDlpV2RecordConditionOut"]
            ).optional(),
            "infoTypeTransformations": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeTransformationsOut"]
            ).optional(),
            "fields": t.array(t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])),
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FieldTransformationOut"])
    types["GooglePrivacyDlpV2QuasiIdIn"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
            "customTag": t.string().optional(),
            "inferred": t.proxy(renames["GoogleProtobufEmptyIn"]).optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdIn"])
    types["GooglePrivacyDlpV2QuasiIdOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "customTag": t.string().optional(),
            "inferred": t.proxy(renames["GoogleProtobufEmptyOut"]).optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdOut"])
    types["GooglePrivacyDlpV2CloudStorageOptionsIn"] = t.struct(
        {
            "sampleMethod": t.string(),
            "fileSet": t.proxy(renames["GooglePrivacyDlpV2FileSetIn"]).optional(),
            "bytesLimitPerFilePercent": t.integer().optional(),
            "bytesLimitPerFile": t.string().optional(),
            "filesLimitPercent": t.integer().optional(),
            "fileTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageOptionsIn"])
    types["GooglePrivacyDlpV2CloudStorageOptionsOut"] = t.struct(
        {
            "sampleMethod": t.string(),
            "fileSet": t.proxy(renames["GooglePrivacyDlpV2FileSetOut"]).optional(),
            "bytesLimitPerFilePercent": t.integer().optional(),
            "bytesLimitPerFile": t.string().optional(),
            "filesLimitPercent": t.integer().optional(),
            "fileTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageOptionsOut"])
    types["GooglePrivacyDlpV2ImageTransformationIn"] = t.struct(
        {
            "selectedInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2SelectedInfoTypesIn"]
            ).optional(),
            "allText": t.proxy(renames["GooglePrivacyDlpV2AllTextIn"]).optional(),
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorIn"]).optional(),
            "allInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2AllInfoTypesIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageTransformationIn"])
    types["GooglePrivacyDlpV2ImageTransformationOut"] = t.struct(
        {
            "selectedInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2SelectedInfoTypesOut"]
            ).optional(),
            "allText": t.proxy(renames["GooglePrivacyDlpV2AllTextOut"]).optional(),
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorOut"]).optional(),
            "allInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2AllInfoTypesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageTransformationOut"])
    types["GooglePrivacyDlpV2StoredInfoTypeVersionIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "errors": t.array(t.proxy(renames["GooglePrivacyDlpV2ErrorIn"])).optional(),
            "state": t.string().optional(),
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]
            ).optional(),
            "stats": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeStatsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeVersionIn"])
    types["GooglePrivacyDlpV2StoredInfoTypeVersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ErrorOut"])
            ).optional(),
            "state": t.string().optional(),
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigOut"]
            ).optional(),
            "stats": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeVersionOut"])
    types["GooglePrivacyDlpV2OtherInfoTypeSummaryIn"] = t.struct(
        {
            "estimatedPrevalence": t.integer().optional(),
            "excludedFromAnalysis": t.boolean().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryIn"])
    types["GooglePrivacyDlpV2OtherInfoTypeSummaryOut"] = t.struct(
        {
            "estimatedPrevalence": t.integer().optional(),
            "excludedFromAnalysis": t.boolean().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryOut"])
    types["GooglePrivacyDlpV2KMapEstimationHistogramBucketIn"] = t.struct(
        {
            "minAnonymity": t.string().optional(),
            "maxAnonymity": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn"])
            ).optional(),
            "bucketValueCount": t.string().optional(),
            "bucketSize": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationHistogramBucketIn"])
    types["GooglePrivacyDlpV2KMapEstimationHistogramBucketOut"] = t.struct(
        {
            "minAnonymity": t.string().optional(),
            "maxAnonymity": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut"])
            ).optional(),
            "bucketValueCount": t.string().optional(),
            "bucketSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationHistogramBucketOut"])
    types["GooglePrivacyDlpV2PubSubConditionIn"] = t.struct(
        {
            "minimumRiskScore": t.string().optional(),
            "minimumSensitivityScore": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubConditionIn"])
    types["GooglePrivacyDlpV2PubSubConditionOut"] = t.struct(
        {
            "minimumRiskScore": t.string().optional(),
            "minimumSensitivityScore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubConditionOut"])
    types["GooglePrivacyDlpV2CreateStoredInfoTypeRequestIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
            "storedInfoTypeId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateStoredInfoTypeRequestIn"])
    types["GooglePrivacyDlpV2CreateStoredInfoTypeRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigOut"]),
            "storedInfoTypeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateStoredInfoTypeRequestOut"])
    types["GooglePrivacyDlpV2UnwrappedCryptoKeyIn"] = t.struct(
        {"key": t.string()}
    ).named(renames["GooglePrivacyDlpV2UnwrappedCryptoKeyIn"])
    types["GooglePrivacyDlpV2UnwrappedCryptoKeyOut"] = t.struct(
        {"key": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2UnwrappedCryptoKeyOut"])
    types["GooglePrivacyDlpV2ScheduleIn"] = t.struct(
        {"recurrencePeriodDuration": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ScheduleIn"])
    types["GooglePrivacyDlpV2ScheduleOut"] = t.struct(
        {
            "recurrencePeriodDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ScheduleOut"])
    types["GooglePrivacyDlpV2NumericalStatsResultIn"] = t.struct(
        {
            "quantileValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
            "maxValue": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
            "minValue": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2NumericalStatsResultIn"])
    types["GooglePrivacyDlpV2NumericalStatsResultOut"] = t.struct(
        {
            "quantileValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "maxValue": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "minValue": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2NumericalStatsResultOut"])
    types["GooglePrivacyDlpV2KeyIn"] = t.struct(
        {
            "partitionId": t.proxy(
                renames["GooglePrivacyDlpV2PartitionIdIn"]
            ).optional(),
            "path": t.array(
                t.proxy(renames["GooglePrivacyDlpV2PathElementIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KeyIn"])
    types["GooglePrivacyDlpV2KeyOut"] = t.struct(
        {
            "partitionId": t.proxy(
                renames["GooglePrivacyDlpV2PartitionIdOut"]
            ).optional(),
            "path": t.array(
                t.proxy(renames["GooglePrivacyDlpV2PathElementOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KeyOut"])
    types["GooglePrivacyDlpV2ExclusionRuleIn"] = t.struct(
        {
            "excludeInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeInfoTypesIn"]
            ).optional(),
            "matchingType": t.string().optional(),
            "excludeByHotword": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeByHotwordIn"]
            ).optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
            "dictionary": t.proxy(renames["GooglePrivacyDlpV2DictionaryIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExclusionRuleIn"])
    types["GooglePrivacyDlpV2ExclusionRuleOut"] = t.struct(
        {
            "excludeInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeInfoTypesOut"]
            ).optional(),
            "matchingType": t.string().optional(),
            "excludeByHotword": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeByHotwordOut"]
            ).optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "dictionary": t.proxy(
                renames["GooglePrivacyDlpV2DictionaryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExclusionRuleOut"])
    types["GooglePrivacyDlpV2TransformationConfigIn"] = t.struct(
        {
            "deidentifyTemplate": t.string().optional(),
            "imageRedactTemplate": t.string().optional(),
            "structuredDeidentifyTemplate": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationConfigIn"])
    types["GooglePrivacyDlpV2TransformationConfigOut"] = t.struct(
        {
            "deidentifyTemplate": t.string().optional(),
            "imageRedactTemplate": t.string().optional(),
            "structuredDeidentifyTemplate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationConfigOut"])
    types["GooglePrivacyDlpV2ActivateJobTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ActivateJobTriggerRequestIn"])
    types["GooglePrivacyDlpV2ActivateJobTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ActivateJobTriggerRequestOut"])
    types["GooglePrivacyDlpV2RowIn"] = t.struct(
        {"values": t.array(t.proxy(renames["GooglePrivacyDlpV2ValueIn"])).optional()}
    ).named(renames["GooglePrivacyDlpV2RowIn"])
    types["GooglePrivacyDlpV2RowOut"] = t.struct(
        {
            "values": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RowOut"])
    types["GooglePrivacyDlpV2FinishDlpJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2FinishDlpJobRequestIn"])
    types["GooglePrivacyDlpV2FinishDlpJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2FinishDlpJobRequestOut"])
    types["GooglePrivacyDlpV2InspectJobConfigIn"] = t.struct(
        {
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "storageConfig": t.proxy(
                renames["GooglePrivacyDlpV2StorageConfigIn"]
            ).optional(),
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionIn"])
            ).optional(),
            "inspectTemplateName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectJobConfigIn"])
    types["GooglePrivacyDlpV2InspectJobConfigOut"] = t.struct(
        {
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "storageConfig": t.proxy(
                renames["GooglePrivacyDlpV2StorageConfigOut"]
            ).optional(),
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionOut"])
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectJobConfigOut"])
    types["GooglePrivacyDlpV2HotwordRuleIn"] = t.struct(
        {
            "likelihoodAdjustment": t.proxy(
                renames["GooglePrivacyDlpV2LikelihoodAdjustmentIn"]
            ).optional(),
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityIn"]).optional(),
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HotwordRuleIn"])
    types["GooglePrivacyDlpV2HotwordRuleOut"] = t.struct(
        {
            "likelihoodAdjustment": t.proxy(
                renames["GooglePrivacyDlpV2LikelihoodAdjustmentOut"]
            ).optional(),
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityOut"]).optional(),
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HotwordRuleOut"])
    types["GooglePrivacyDlpV2ByteContentItemIn"] = t.struct(
        {"data": t.string().optional(), "type": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ByteContentItemIn"])
    types["GooglePrivacyDlpV2ByteContentItemOut"] = t.struct(
        {
            "data": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ByteContentItemOut"])
    types["GooglePrivacyDlpV2ListJobTriggersResponseIn"] = t.struct(
        {
            "jobTriggers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListJobTriggersResponseIn"])
    types["GooglePrivacyDlpV2ListJobTriggersResponseOut"] = t.struct(
        {
            "jobTriggers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListJobTriggersResponseOut"])
    types["GooglePrivacyDlpV2ListInfoTypesResponseIn"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeDescriptionIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2ListInfoTypesResponseIn"])
    types["GooglePrivacyDlpV2ListInfoTypesResponseOut"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeDescriptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListInfoTypesResponseOut"])
    types["GooglePrivacyDlpV2RedactImageResponseIn"] = t.struct(
        {
            "redactedImage": t.string().optional(),
            "inspectResult": t.proxy(
                renames["GooglePrivacyDlpV2InspectResultIn"]
            ).optional(),
            "extractedText": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageResponseIn"])
    types["GooglePrivacyDlpV2RedactImageResponseOut"] = t.struct(
        {
            "redactedImage": t.string().optional(),
            "inspectResult": t.proxy(
                renames["GooglePrivacyDlpV2InspectResultOut"]
            ).optional(),
            "extractedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageResponseOut"])
    types["GooglePrivacyDlpV2CancelDlpJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2CancelDlpJobRequestIn"])
    types["GooglePrivacyDlpV2CancelDlpJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2CancelDlpJobRequestOut"])
    types["GooglePrivacyDlpV2ColorIn"] = t.struct(
        {
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ColorIn"])
    types["GooglePrivacyDlpV2ColorOut"] = t.struct(
        {
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ColorOut"])
    types["GooglePrivacyDlpV2CloudStorageFileSetIn"] = t.struct(
        {"url": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2CloudStorageFileSetIn"])
    types["GooglePrivacyDlpV2CloudStorageFileSetOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageFileSetOut"])
    types["GooglePrivacyDlpV2DatastoreOptionsIn"] = t.struct(
        {
            "partitionId": t.proxy(
                renames["GooglePrivacyDlpV2PartitionIdIn"]
            ).optional(),
            "kind": t.proxy(renames["GooglePrivacyDlpV2KindExpressionIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DatastoreOptionsIn"])
    types["GooglePrivacyDlpV2DatastoreOptionsOut"] = t.struct(
        {
            "partitionId": t.proxy(
                renames["GooglePrivacyDlpV2PartitionIdOut"]
            ).optional(),
            "kind": t.proxy(renames["GooglePrivacyDlpV2KindExpressionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DatastoreOptionsOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GooglePrivacyDlpV2ColumnDataProfileIn"] = t.struct(
        {
            "columnInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeSummaryIn"]
            ).optional(),
            "profileStatus": t.proxy(
                renames["GooglePrivacyDlpV2ProfileStatusIn"]
            ).optional(),
            "policyState": t.string().optional(),
            "state": t.string().optional(),
            "tableId": t.string().optional(),
            "tableFullResource": t.string().optional(),
            "datasetLocation": t.string().optional(),
            "datasetProjectId": t.string().optional(),
            "freeTextScore": t.number().optional(),
            "otherMatches": t.array(
                t.proxy(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryIn"])
            ).optional(),
            "profileLastGenerated": t.string().optional(),
            "tableDataProfile": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "estimatedNullPercentage": t.string().optional(),
            "column": t.string().optional(),
            "dataRiskLevel": t.proxy(
                renames["GooglePrivacyDlpV2DataRiskLevelIn"]
            ).optional(),
            "datasetId": t.string().optional(),
            "name": t.string().optional(),
            "estimatedUniquenessScore": t.string().optional(),
            "columnType": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ColumnDataProfileIn"])
    types["GooglePrivacyDlpV2ColumnDataProfileOut"] = t.struct(
        {
            "columnInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeSummaryOut"]
            ).optional(),
            "profileStatus": t.proxy(
                renames["GooglePrivacyDlpV2ProfileStatusOut"]
            ).optional(),
            "policyState": t.string().optional(),
            "state": t.string().optional(),
            "tableId": t.string().optional(),
            "tableFullResource": t.string().optional(),
            "datasetLocation": t.string().optional(),
            "datasetProjectId": t.string().optional(),
            "freeTextScore": t.number().optional(),
            "otherMatches": t.array(
                t.proxy(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryOut"])
            ).optional(),
            "profileLastGenerated": t.string().optional(),
            "tableDataProfile": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "estimatedNullPercentage": t.string().optional(),
            "column": t.string().optional(),
            "dataRiskLevel": t.proxy(
                renames["GooglePrivacyDlpV2DataRiskLevelOut"]
            ).optional(),
            "datasetId": t.string().optional(),
            "name": t.string().optional(),
            "estimatedUniquenessScore": t.string().optional(),
            "columnType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ColumnDataProfileOut"])
    types["GooglePrivacyDlpV2HybridInspectStatisticsIn"] = t.struct(
        {
            "processedCount": t.string().optional(),
            "abortedCount": t.string().optional(),
            "pendingCount": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectStatisticsIn"])
    types["GooglePrivacyDlpV2HybridInspectStatisticsOut"] = t.struct(
        {
            "processedCount": t.string().optional(),
            "abortedCount": t.string().optional(),
            "pendingCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectStatisticsOut"])
    types["GooglePrivacyDlpV2ContentLocationIn"] = t.struct(
        {
            "metadataLocation": t.proxy(
                renames["GooglePrivacyDlpV2MetadataLocationIn"]
            ).optional(),
            "containerVersion": t.string().optional(),
            "recordLocation": t.proxy(
                renames["GooglePrivacyDlpV2RecordLocationIn"]
            ).optional(),
            "imageLocation": t.proxy(
                renames["GooglePrivacyDlpV2ImageLocationIn"]
            ).optional(),
            "containerName": t.string().optional(),
            "containerTimestamp": t.string().optional(),
            "documentLocation": t.proxy(
                renames["GooglePrivacyDlpV2DocumentLocationIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentLocationIn"])
    types["GooglePrivacyDlpV2ContentLocationOut"] = t.struct(
        {
            "metadataLocation": t.proxy(
                renames["GooglePrivacyDlpV2MetadataLocationOut"]
            ).optional(),
            "containerVersion": t.string().optional(),
            "recordLocation": t.proxy(
                renames["GooglePrivacyDlpV2RecordLocationOut"]
            ).optional(),
            "imageLocation": t.proxy(
                renames["GooglePrivacyDlpV2ImageLocationOut"]
            ).optional(),
            "containerName": t.string().optional(),
            "containerTimestamp": t.string().optional(),
            "documentLocation": t.proxy(
                renames["GooglePrivacyDlpV2DocumentLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentLocationOut"])
    types["GooglePrivacyDlpV2TimespanConfigIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "enableAutoPopulationOfTimespanConfig": t.boolean().optional(),
            "timestampField": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimespanConfigIn"])
    types["GooglePrivacyDlpV2TimespanConfigOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "enableAutoPopulationOfTimespanConfig": t.boolean().optional(),
            "timestampField": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimespanConfigOut"])
    types["GooglePrivacyDlpV2CategoricalStatsResultIn"] = t.struct(
        {
            "valueFrequencyHistogramBuckets": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsResultIn"])
    types["GooglePrivacyDlpV2CategoricalStatsResultOut"] = t.struct(
        {
            "valueFrequencyHistogramBuckets": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsResultOut"])
    types["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn"] = t.struct(
        {
            "deltaPresenceEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationResultIn"]
            ).optional(),
            "lDiversityResult": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityResultIn"]
            ).optional(),
            "requestedPrivacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricIn"]
            ).optional(),
            "kMapEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationResultIn"]
            ).optional(),
            "requestedSourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional(),
            "numericalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsResultIn"]
            ).optional(),
            "kAnonymityResult": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityResultIn"]
            ).optional(),
            "categoricalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsResultIn"]
            ).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn"])
    types["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut"] = t.struct(
        {
            "deltaPresenceEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationResultOut"]
            ).optional(),
            "lDiversityResult": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityResultOut"]
            ).optional(),
            "requestedPrivacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricOut"]
            ).optional(),
            "kMapEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationResultOut"]
            ).optional(),
            "requestedSourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "numericalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsResultOut"]
            ).optional(),
            "kAnonymityResult": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityResultOut"]
            ).optional(),
            "categoricalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsResultOut"]
            ).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut"])
    types["GooglePrivacyDlpV2KindExpressionIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2KindExpressionIn"])
    types["GooglePrivacyDlpV2KindExpressionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KindExpressionOut"])
    types["GooglePrivacyDlpV2StorageMetadataLabelIn"] = t.struct(
        {"key": t.string()}
    ).named(renames["GooglePrivacyDlpV2StorageMetadataLabelIn"])
    types["GooglePrivacyDlpV2StorageMetadataLabelOut"] = t.struct(
        {"key": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2StorageMetadataLabelOut"])
    types["GooglePrivacyDlpV2SummaryResultIn"] = t.struct(
        {
            "details": t.string().optional(),
            "count": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SummaryResultIn"])
    types["GooglePrivacyDlpV2SummaryResultOut"] = t.struct(
        {
            "details": t.string().optional(),
            "count": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SummaryResultOut"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationResultIn"] = t.struct(
        {
            "deltaPresenceEstimationHistogram": t.array(
                t.proxy(
                    renames[
                        "GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationResultIn"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationResultOut"] = t.struct(
        {
            "deltaPresenceEstimationHistogram": t.array(
                t.proxy(
                    renames[
                        "GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationResultOut"])
    types["GooglePrivacyDlpV2DetectionRuleIn"] = t.struct(
        {"hotwordRule": t.proxy(renames["GooglePrivacyDlpV2HotwordRuleIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2DetectionRuleIn"])
    types["GooglePrivacyDlpV2DetectionRuleOut"] = t.struct(
        {
            "hotwordRule": t.proxy(
                renames["GooglePrivacyDlpV2HotwordRuleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DetectionRuleOut"])
    types["GooglePrivacyDlpV2CryptoDeterministicConfigIn"] = t.struct(
        {
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "surrogateInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeIn"]
            ).optional(),
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoDeterministicConfigIn"])
    types["GooglePrivacyDlpV2CryptoDeterministicConfigOut"] = t.struct(
        {
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "surrogateInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeOut"]
            ).optional(),
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoDeterministicConfigOut"])
    types["GooglePrivacyDlpV2KmsWrappedCryptoKeyIn"] = t.struct(
        {"cryptoKeyName": t.string(), "wrappedKey": t.string()}
    ).named(renames["GooglePrivacyDlpV2KmsWrappedCryptoKeyIn"])
    types["GooglePrivacyDlpV2KmsWrappedCryptoKeyOut"] = t.struct(
        {
            "cryptoKeyName": t.string(),
            "wrappedKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KmsWrappedCryptoKeyOut"])
    types["GooglePrivacyDlpV2TransformationDetailsStorageConfigIn"] = t.struct(
        {"table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigIn"])
    types["GooglePrivacyDlpV2TransformationDetailsStorageConfigOut"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigOut"])
    types["GooglePrivacyDlpV2ManualIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooglePrivacyDlpV2ManualIn"]
    )
    types["GooglePrivacyDlpV2ManualOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ManualOut"])
    types["GooglePrivacyDlpV2InfoTypeDescriptionIn"] = t.struct(
        {
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "supportedBy": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2VersionDescriptionIn"])
            ).optional(),
            "categories": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeCategoryIn"])
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeDescriptionIn"])
    types["GooglePrivacyDlpV2InfoTypeDescriptionOut"] = t.struct(
        {
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "supportedBy": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2VersionDescriptionOut"])
            ).optional(),
            "categories": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeCategoryOut"])
            ).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeDescriptionOut"])
    types["GooglePrivacyDlpV2LeaveUntransformedIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2LeaveUntransformedIn"])
    types["GooglePrivacyDlpV2LeaveUntransformedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2LeaveUntransformedOut"])
    types["GooglePrivacyDlpV2ExcludeInfoTypesIn"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2ExcludeInfoTypesIn"])
    types["GooglePrivacyDlpV2ExcludeInfoTypesOut"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExcludeInfoTypesOut"])
    types["GooglePrivacyDlpV2FindingIn"] = t.struct(
        {
            "quoteInfo": t.proxy(renames["GooglePrivacyDlpV2QuoteInfoIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "triggerName": t.string().optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "findingId": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "location": t.proxy(renames["GooglePrivacyDlpV2LocationIn"]).optional(),
            "jobName": t.string().optional(),
            "jobCreateTime": t.string().optional(),
            "quote": t.string().optional(),
            "likelihood": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingIn"])
    types["GooglePrivacyDlpV2FindingOut"] = t.struct(
        {
            "quoteInfo": t.proxy(renames["GooglePrivacyDlpV2QuoteInfoOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "triggerName": t.string().optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "findingId": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "location": t.proxy(renames["GooglePrivacyDlpV2LocationOut"]).optional(),
            "jobName": t.string().optional(),
            "jobCreateTime": t.string().optional(),
            "quote": t.string().optional(),
            "likelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingOut"])
    types["GooglePrivacyDlpV2DataRiskLevelIn"] = t.struct(
        {"score": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2DataRiskLevelIn"])
    types["GooglePrivacyDlpV2DataRiskLevelOut"] = t.struct(
        {
            "score": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataRiskLevelOut"])
    types["GooglePrivacyDlpV2TimeZoneIn"] = t.struct(
        {"offsetMinutes": t.integer().optional()}
    ).named(renames["GooglePrivacyDlpV2TimeZoneIn"])
    types["GooglePrivacyDlpV2TimeZoneOut"] = t.struct(
        {
            "offsetMinutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimeZoneOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GooglePrivacyDlpV2ValueIn"] = t.struct(
        {
            "dayOfWeekValue": t.string().optional(),
            "timeValue": t.proxy(renames["GoogleTypeTimeOfDayIn"]).optional(),
            "booleanValue": t.boolean().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "floatValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "timestampValue": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ValueIn"])
    types["GooglePrivacyDlpV2ValueOut"] = t.struct(
        {
            "dayOfWeekValue": t.string().optional(),
            "timeValue": t.proxy(renames["GoogleTypeTimeOfDayOut"]).optional(),
            "booleanValue": t.boolean().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "floatValue": t.number().optional(),
            "integerValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ValueOut"])
    types["GooglePrivacyDlpV2InspectConfigIn"] = t.struct(
        {
            "minLikelihood": t.string().optional(),
            "ruleSet": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleSetIn"])
            ).optional(),
            "includeQuote": t.boolean().optional(),
            "excludeInfoTypes": t.boolean().optional(),
            "limits": t.proxy(renames["GooglePrivacyDlpV2FindingLimitsIn"]).optional(),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"])
            ).optional(),
            "customInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CustomInfoTypeIn"])
            ).optional(),
            "contentOptions": t.array(t.string()).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectConfigIn"])
    types["GooglePrivacyDlpV2InspectConfigOut"] = t.struct(
        {
            "minLikelihood": t.string().optional(),
            "ruleSet": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleSetOut"])
            ).optional(),
            "includeQuote": t.boolean().optional(),
            "excludeInfoTypes": t.boolean().optional(),
            "limits": t.proxy(renames["GooglePrivacyDlpV2FindingLimitsOut"]).optional(),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])
            ).optional(),
            "customInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CustomInfoTypeOut"])
            ).optional(),
            "contentOptions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectConfigOut"])
    types["GooglePrivacyDlpV2BucketIn"] = t.struct(
        {
            "replacementValue": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]),
            "min": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
            "max": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BucketIn"])
    types["GooglePrivacyDlpV2BucketOut"] = t.struct(
        {
            "replacementValue": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]),
            "min": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "max": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BucketOut"])
    types["GooglePrivacyDlpV2PrivacyMetricIn"] = t.struct(
        {
            "lDiversityConfig": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityConfigIn"]
            ).optional(),
            "categoricalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsConfigIn"]
            ).optional(),
            "numericalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsConfigIn"]
            ).optional(),
            "deltaPresenceEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn"]
            ).optional(),
            "kMapEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationConfigIn"]
            ).optional(),
            "kAnonymityConfig": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrivacyMetricIn"])
    types["GooglePrivacyDlpV2PrivacyMetricOut"] = t.struct(
        {
            "lDiversityConfig": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityConfigOut"]
            ).optional(),
            "categoricalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsConfigOut"]
            ).optional(),
            "numericalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsConfigOut"]
            ).optional(),
            "deltaPresenceEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut"]
            ).optional(),
            "kMapEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationConfigOut"]
            ).optional(),
            "kAnonymityConfig": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrivacyMetricOut"])
    types["GooglePrivacyDlpV2DateShiftConfigIn"] = t.struct(
        {
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyIn"]).optional(),
            "upperBoundDays": t.integer(),
            "lowerBoundDays": t.integer(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DateShiftConfigIn"])
    types["GooglePrivacyDlpV2DateShiftConfigOut"] = t.struct(
        {
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyOut"]).optional(),
            "upperBoundDays": t.integer(),
            "lowerBoundDays": t.integer(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DateShiftConfigOut"])
    types["GooglePrivacyDlpV2DeidentifyIn"] = t.struct(
        {
            "transformationConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationConfigIn"]
            ).optional(),
            "cloudStorageOutput": t.string(),
            "fileTypesToTransform": t.array(t.string()).optional(),
            "transformationDetailsStorageConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyIn"])
    types["GooglePrivacyDlpV2DeidentifyOut"] = t.struct(
        {
            "transformationConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationConfigOut"]
            ).optional(),
            "cloudStorageOutput": t.string(),
            "fileTypesToTransform": t.array(t.string()).optional(),
            "transformationDetailsStorageConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyOut"])
    types["GooglePrivacyDlpV2ReplaceDictionaryConfigIn"] = t.struct(
        {"wordList": t.proxy(renames["GooglePrivacyDlpV2WordListIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceDictionaryConfigIn"])
    types["GooglePrivacyDlpV2ReplaceDictionaryConfigOut"] = t.struct(
        {
            "wordList": t.proxy(renames["GooglePrivacyDlpV2WordListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReplaceDictionaryConfigOut"])
    types["GooglePrivacyDlpV2LDiversityEquivalenceClassIn"] = t.struct(
        {
            "numDistinctSensitiveValues": t.string().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
            "equivalenceClassSize": t.string().optional(),
            "topSensitiveValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassIn"])
    types["GooglePrivacyDlpV2LDiversityEquivalenceClassOut"] = t.struct(
        {
            "numDistinctSensitiveValues": t.string().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "equivalenceClassSize": t.string().optional(),
            "topSensitiveValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassOut"])
    types["GooglePrivacyDlpV2KMapEstimationResultIn"] = t.struct(
        {
            "kMapEstimationHistogram": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KMapEstimationHistogramBucketIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationResultIn"])
    types["GooglePrivacyDlpV2KMapEstimationResultOut"] = t.struct(
        {
            "kMapEstimationHistogram": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KMapEstimationHistogramBucketOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationResultOut"])
    types["GooglePrivacyDlpV2AllTextIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooglePrivacyDlpV2AllTextIn"]
    )
    types["GooglePrivacyDlpV2AllTextOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2AllTextOut"])
    types["GooglePrivacyDlpV2FindingLimitsIn"] = t.struct(
        {
            "maxFindingsPerInfoType": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeLimitIn"])
            ).optional(),
            "maxFindingsPerRequest": t.integer().optional(),
            "maxFindingsPerItem": t.integer().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingLimitsIn"])
    types["GooglePrivacyDlpV2FindingLimitsOut"] = t.struct(
        {
            "maxFindingsPerInfoType": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeLimitOut"])
            ).optional(),
            "maxFindingsPerRequest": t.integer().optional(),
            "maxFindingsPerItem": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingLimitsOut"])
    types["GooglePrivacyDlpV2DictionaryIn"] = t.struct(
        {
            "wordList": t.proxy(renames["GooglePrivacyDlpV2WordListIn"]).optional(),
            "cloudStoragePath": t.proxy(
                renames["GooglePrivacyDlpV2CloudStoragePathIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DictionaryIn"])
    types["GooglePrivacyDlpV2DictionaryOut"] = t.struct(
        {
            "wordList": t.proxy(renames["GooglePrivacyDlpV2WordListOut"]).optional(),
            "cloudStoragePath": t.proxy(
                renames["GooglePrivacyDlpV2CloudStoragePathOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DictionaryOut"])
    types["GooglePrivacyDlpV2FileSetIn"] = t.struct(
        {
            "regexFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageRegexFileSetIn"]
            ).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FileSetIn"])
    types["GooglePrivacyDlpV2FileSetOut"] = t.struct(
        {
            "regexFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageRegexFileSetOut"]
            ).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FileSetOut"])
    types["GooglePrivacyDlpV2RecordConditionIn"] = t.struct(
        {"expressions": t.proxy(renames["GooglePrivacyDlpV2ExpressionsIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2RecordConditionIn"])
    types["GooglePrivacyDlpV2RecordConditionOut"] = t.struct(
        {
            "expressions": t.proxy(
                renames["GooglePrivacyDlpV2ExpressionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordConditionOut"])
    types["GooglePrivacyDlpV2DataProfilePubSubMessageIn"] = t.struct(
        {
            "profile": t.proxy(
                renames["GooglePrivacyDlpV2TableDataProfileIn"]
            ).optional(),
            "event": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfilePubSubMessageIn"])
    types["GooglePrivacyDlpV2DataProfilePubSubMessageOut"] = t.struct(
        {
            "profile": t.proxy(
                renames["GooglePrivacyDlpV2TableDataProfileOut"]
            ).optional(),
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfilePubSubMessageOut"])
    types["GooglePrivacyDlpV2BigQueryTableIn"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryTableIn"])
    types["GooglePrivacyDlpV2BigQueryTableOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryTableOut"])
    types["GooglePrivacyDlpV2JobNotificationEmailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2JobNotificationEmailsIn"])
    types["GooglePrivacyDlpV2JobNotificationEmailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2JobNotificationEmailsOut"])
    types["GooglePrivacyDlpV2TableDataProfileIn"] = t.struct(
        {
            "predictedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeSummaryIn"])
            ).optional(),
            "profileLastGenerated": t.string().optional(),
            "state": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "encryptionStatus": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "projectDataProfile": t.string().optional(),
            "scannedColumnCount": t.string().optional(),
            "expirationTime": t.string().optional(),
            "tableSizeBytes": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "tableId": t.string().optional(),
            "fullResource": t.string().optional(),
            "name": t.string().optional(),
            "otherInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryIn"])
            ).optional(),
            "dataRiskLevel": t.proxy(
                renames["GooglePrivacyDlpV2DataRiskLevelIn"]
            ).optional(),
            "configSnapshot": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileConfigSnapshotIn"]
            ).optional(),
            "resourceVisibility": t.string().optional(),
            "createTime": t.string().optional(),
            "datasetId": t.string().optional(),
            "failedColumnCount": t.string().optional(),
            "datasetProjectId": t.string().optional(),
            "datasetLocation": t.string().optional(),
            "rowCount": t.string().optional(),
            "profileStatus": t.proxy(
                renames["GooglePrivacyDlpV2ProfileStatusIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableDataProfileIn"])
    types["GooglePrivacyDlpV2TableDataProfileOut"] = t.struct(
        {
            "predictedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeSummaryOut"])
            ).optional(),
            "profileLastGenerated": t.string().optional(),
            "state": t.string().optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "encryptionStatus": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "projectDataProfile": t.string().optional(),
            "scannedColumnCount": t.string().optional(),
            "expirationTime": t.string().optional(),
            "tableSizeBytes": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "tableId": t.string().optional(),
            "fullResource": t.string().optional(),
            "name": t.string().optional(),
            "otherInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryOut"])
            ).optional(),
            "dataRiskLevel": t.proxy(
                renames["GooglePrivacyDlpV2DataRiskLevelOut"]
            ).optional(),
            "configSnapshot": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileConfigSnapshotOut"]
            ).optional(),
            "resourceVisibility": t.string().optional(),
            "createTime": t.string().optional(),
            "datasetId": t.string().optional(),
            "failedColumnCount": t.string().optional(),
            "datasetProjectId": t.string().optional(),
            "datasetLocation": t.string().optional(),
            "rowCount": t.string().optional(),
            "profileStatus": t.proxy(
                renames["GooglePrivacyDlpV2ProfileStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableDataProfileOut"])
    types["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deidentifyTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn"])
    types["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deidentifyTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"])
    types["GooglePrivacyDlpV2ProximityIn"] = t.struct(
        {"windowBefore": t.integer().optional(), "windowAfter": t.integer().optional()}
    ).named(renames["GooglePrivacyDlpV2ProximityIn"])
    types["GooglePrivacyDlpV2ProximityOut"] = t.struct(
        {
            "windowBefore": t.integer().optional(),
            "windowAfter": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ProximityOut"])
    types["GooglePrivacyDlpV2InfoTypeTransformationIn"] = t.struct(
        {
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationIn"]
            ),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeTransformationIn"])
    types["GooglePrivacyDlpV2InfoTypeTransformationOut"] = t.struct(
        {
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationOut"]
            ),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeTransformationOut"])
    types["GooglePrivacyDlpV2InspectDataSourceDetailsIn"] = t.struct(
        {
            "result": t.proxy(renames["GooglePrivacyDlpV2ResultIn"]).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedOptionsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectDataSourceDetailsIn"])
    types["GooglePrivacyDlpV2InspectDataSourceDetailsOut"] = t.struct(
        {
            "result": t.proxy(renames["GooglePrivacyDlpV2ResultOut"]).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectDataSourceDetailsOut"])
    types["GooglePrivacyDlpV2PathElementIn"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PathElementIn"])
    types["GooglePrivacyDlpV2PathElementOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PathElementOut"])
    types["GooglePrivacyDlpV2ImageTransformationsIn"] = t.struct(
        {
            "transforms": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ImageTransformationIn"])
            )
        }
    ).named(renames["GooglePrivacyDlpV2ImageTransformationsIn"])
    types["GooglePrivacyDlpV2ImageTransformationsOut"] = t.struct(
        {
            "transforms": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ImageTransformationOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageTransformationsOut"])
    types["GooglePrivacyDlpV2ConditionIn"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
            "value": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
            "operator": t.string(),
        }
    ).named(renames["GooglePrivacyDlpV2ConditionIn"])
    types["GooglePrivacyDlpV2ConditionOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "value": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "operator": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ConditionOut"])
    types["GooglePrivacyDlpV2UpdateInspectTemplateRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "inspectTemplate": t.proxy(
                renames["GooglePrivacyDlpV2InspectTemplateIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateInspectTemplateRequestIn"])
    types["GooglePrivacyDlpV2UpdateInspectTemplateRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "inspectTemplate": t.proxy(
                renames["GooglePrivacyDlpV2InspectTemplateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateInspectTemplateRequestOut"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn"] = t.struct(
        {
            "bucketSize": t.string().optional(),
            "maxProbability": t.number().optional(),
            "minProbability": t.number().optional(),
            "bucketValues": t.array(
                t.proxy(
                    renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn"]
                )
            ).optional(),
            "bucketValueCount": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut"] = t.struct(
        {
            "bucketSize": t.string().optional(),
            "maxProbability": t.number().optional(),
            "minProbability": t.number().optional(),
            "bucketValues": t.array(
                t.proxy(
                    renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut"]
                )
            ).optional(),
            "bucketValueCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut"])
    types["GooglePrivacyDlpV2DataProfileLocationIn"] = t.struct(
        {"organizationId": t.string().optional(), "folderId": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2DataProfileLocationIn"])
    types["GooglePrivacyDlpV2DataProfileLocationOut"] = t.struct(
        {
            "organizationId": t.string().optional(),
            "folderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileLocationOut"])
    types["GooglePrivacyDlpV2HybridContentItemIn"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
            "findingDetails": t.proxy(
                renames["GooglePrivacyDlpV2HybridFindingDetailsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridContentItemIn"])
    types["GooglePrivacyDlpV2HybridContentItemOut"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "findingDetails": t.proxy(
                renames["GooglePrivacyDlpV2HybridFindingDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridContentItemOut"])
    types["GooglePrivacyDlpV2ImageLocationIn"] = t.struct(
        {
            "boundingBoxes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2BoundingBoxIn"])
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2ImageLocationIn"])
    types["GooglePrivacyDlpV2ImageLocationOut"] = t.struct(
        {
            "boundingBoxes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2BoundingBoxOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageLocationOut"])
    types["GooglePrivacyDlpV2LargeCustomDictionaryStatsIn"] = t.struct(
        {"approxNumPhrases": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryStatsIn"])
    types["GooglePrivacyDlpV2LargeCustomDictionaryStatsOut"] = t.struct(
        {
            "approxNumPhrases": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryStatsOut"])
    types["GooglePrivacyDlpV2ReidentifyContentRequestIn"] = t.struct(
        {
            "reidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
            ).optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "reidentifyTemplateName": t.string().optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReidentifyContentRequestIn"])
    types["GooglePrivacyDlpV2ReidentifyContentRequestOut"] = t.struct(
        {
            "reidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigOut"]
            ).optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "reidentifyTemplateName": t.string().optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReidentifyContentRequestOut"])
    types["GooglePrivacyDlpV2KAnonymityConfigIn"] = t.struct(
        {
            "entityId": t.proxy(renames["GooglePrivacyDlpV2EntityIdIn"]).optional(),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityConfigIn"])
    types["GooglePrivacyDlpV2KAnonymityConfigOut"] = t.struct(
        {
            "entityId": t.proxy(renames["GooglePrivacyDlpV2EntityIdOut"]).optional(),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityConfigOut"])
    types["GooglePrivacyDlpV2HybridInspectJobTriggerRequestIn"] = t.struct(
        {
            "hybridItem": t.proxy(
                renames["GooglePrivacyDlpV2HybridContentItemIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectJobTriggerRequestIn"])
    types["GooglePrivacyDlpV2HybridInspectJobTriggerRequestOut"] = t.struct(
        {
            "hybridItem": t.proxy(
                renames["GooglePrivacyDlpV2HybridContentItemOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectJobTriggerRequestOut"])
    types["GooglePrivacyDlpV2InfoTypeCategoryIn"] = t.struct(
        {
            "typeCategory": t.string().optional(),
            "industryCategory": t.string().optional(),
            "locationCategory": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeCategoryIn"])
    types["GooglePrivacyDlpV2InfoTypeCategoryOut"] = t.struct(
        {
            "typeCategory": t.string().optional(),
            "industryCategory": t.string().optional(),
            "locationCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeCategoryOut"])
    types["GooglePrivacyDlpV2RecordSuppressionIn"] = t.struct(
        {
            "condition": t.proxy(
                renames["GooglePrivacyDlpV2RecordConditionIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2RecordSuppressionIn"])
    types["GooglePrivacyDlpV2RecordSuppressionOut"] = t.struct(
        {
            "condition": t.proxy(
                renames["GooglePrivacyDlpV2RecordConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordSuppressionOut"])
    types["GooglePrivacyDlpV2BucketingConfigIn"] = t.struct(
        {"buckets": t.array(t.proxy(renames["GooglePrivacyDlpV2BucketIn"])).optional()}
    ).named(renames["GooglePrivacyDlpV2BucketingConfigIn"])
    types["GooglePrivacyDlpV2BucketingConfigOut"] = t.struct(
        {
            "buckets": t.array(
                t.proxy(renames["GooglePrivacyDlpV2BucketOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BucketingConfigOut"])
    types["GooglePrivacyDlpV2TransformationSummaryIn"] = t.struct(
        {
            "transformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationIn"]
            ).optional(),
            "recordSuppress": t.proxy(
                renames["GooglePrivacyDlpV2RecordSuppressionIn"]
            ).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "transformedBytes": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationIn"])
            ).optional(),
            "results": t.array(
                t.proxy(renames["GooglePrivacyDlpV2SummaryResultIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationSummaryIn"])
    types["GooglePrivacyDlpV2TransformationSummaryOut"] = t.struct(
        {
            "transformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationOut"]
            ).optional(),
            "recordSuppress": t.proxy(
                renames["GooglePrivacyDlpV2RecordSuppressionOut"]
            ).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "transformedBytes": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationOut"])
            ).optional(),
            "results": t.array(
                t.proxy(renames["GooglePrivacyDlpV2SummaryResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationSummaryOut"])
    types["GooglePrivacyDlpV2CreateJobTriggerRequestIn"] = t.struct(
        {
            "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
            "locationId": t.string().optional(),
            "triggerId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateJobTriggerRequestIn"])
    types["GooglePrivacyDlpV2CreateJobTriggerRequestOut"] = t.struct(
        {
            "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
            "locationId": t.string().optional(),
            "triggerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateJobTriggerRequestOut"])
    types["GooglePrivacyDlpV2TransformationLocationIn"] = t.struct(
        {
            "recordTransformation": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationIn"]
            ).optional(),
            "findingId": t.string().optional(),
            "containerType": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationLocationIn"])
    types["GooglePrivacyDlpV2TransformationLocationOut"] = t.struct(
        {
            "recordTransformation": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationOut"]
            ).optional(),
            "findingId": t.string().optional(),
            "containerType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationLocationOut"])
    types["GooglePrivacyDlpV2FixedSizeBucketingConfigIn"] = t.struct(
        {
            "bucketSize": t.number(),
            "upperBound": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]),
            "lowerBound": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2FixedSizeBucketingConfigIn"])
    types["GooglePrivacyDlpV2FixedSizeBucketingConfigOut"] = t.struct(
        {
            "bucketSize": t.number(),
            "upperBound": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]),
            "lowerBound": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FixedSizeBucketingConfigOut"])
    types["GooglePrivacyDlpV2DocumentLocationIn"] = t.struct(
        {"fileOffset": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2DocumentLocationIn"])
    types["GooglePrivacyDlpV2DocumentLocationOut"] = t.struct(
        {
            "fileOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DocumentLocationOut"])
    types["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn"])
    types["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut"])
    types["GooglePrivacyDlpV2RedactImageRequestIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemIn"]
            ).optional(),
            "includeFindings": t.boolean().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "imageRedactionConfigs": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageRequestIn"])
    types["GooglePrivacyDlpV2RedactImageRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemOut"]
            ).optional(),
            "includeFindings": t.boolean().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "imageRedactionConfigs": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageRequestOut"])
    types["GooglePrivacyDlpV2StoredInfoTypeIn"] = t.struct(
        {
            "pendingVersions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeVersionIn"])
            ).optional(),
            "currentVersion": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeVersionIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeIn"])
    types["GooglePrivacyDlpV2StoredInfoTypeOut"] = t.struct(
        {
            "pendingVersions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeVersionOut"])
            ).optional(),
            "currentVersion": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeVersionOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeOut"])
    types["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn"])
    types["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut"])
    types["GooglePrivacyDlpV2StoredInfoTypeStatsIn"] = t.struct(
        {
            "largeCustomDictionary": t.proxy(
                renames["GooglePrivacyDlpV2LargeCustomDictionaryStatsIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeStatsIn"])
    types["GooglePrivacyDlpV2StoredInfoTypeStatsOut"] = t.struct(
        {
            "largeCustomDictionary": t.proxy(
                renames["GooglePrivacyDlpV2LargeCustomDictionaryStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeStatsOut"])
    types["GooglePrivacyDlpV2ThrowErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ThrowErrorIn"])
    types["GooglePrivacyDlpV2ThrowErrorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ThrowErrorOut"])
    types["GooglePrivacyDlpV2DateTimeIn"] = t.struct(
        {
            "timeZone": t.proxy(renames["GooglePrivacyDlpV2TimeZoneIn"]).optional(),
            "date": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "time": t.proxy(renames["GoogleTypeTimeOfDayIn"]).optional(),
            "dayOfWeek": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DateTimeIn"])
    types["GooglePrivacyDlpV2DateTimeOut"] = t.struct(
        {
            "timeZone": t.proxy(renames["GooglePrivacyDlpV2TimeZoneOut"]).optional(),
            "date": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "time": t.proxy(renames["GoogleTypeTimeOfDayOut"]).optional(),
            "dayOfWeek": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DateTimeOut"])
    types["GooglePrivacyDlpV2ImageRedactionConfigIn"] = t.struct(
        {
            "redactAllText": t.boolean().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
    types["GooglePrivacyDlpV2ImageRedactionConfigOut"] = t.struct(
        {
            "redactAllText": t.boolean().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageRedactionConfigOut"])
    types["GooglePrivacyDlpV2CategoricalStatsConfigIn"] = t.struct(
        {"field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsConfigIn"])
    types["GooglePrivacyDlpV2CategoricalStatsConfigOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsConfigOut"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn"] = t.struct(
        {
            "deidentifyStats": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsIn"]
            ).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedDeidentifyOptionsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut"] = t.struct(
        {
            "deidentifyStats": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsOut"]
            ).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedDeidentifyOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut"])
    types["GooglePrivacyDlpV2DeidentifyContentResponseIn"] = t.struct(
        {
            "overview": t.proxy(
                renames["GooglePrivacyDlpV2TransformationOverviewIn"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentResponseIn"])
    types["GooglePrivacyDlpV2DeidentifyContentResponseOut"] = t.struct(
        {
            "overview": t.proxy(
                renames["GooglePrivacyDlpV2TransformationOverviewOut"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"])
    types["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn"] = t.struct(
        {
            "jobConfig": t.proxy(
                renames["GooglePrivacyDlpV2RiskAnalysisJobConfigIn"]
            ).optional()
        }
    ).named(renames["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn"])
    types["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut"] = t.struct(
        {
            "jobConfig": t.proxy(
                renames["GooglePrivacyDlpV2RiskAnalysisJobConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut"])
    types["GooglePrivacyDlpV2PublishToPubSubIn"] = t.struct(
        {"topic": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishToPubSubIn"])
    types["GooglePrivacyDlpV2PublishToPubSubOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PublishToPubSubOut"])
    types["GooglePrivacyDlpV2ListInspectTemplatesResponseIn"] = t.struct(
        {
            "inspectTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectTemplateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseIn"])
    types["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"] = t.struct(
        {
            "inspectTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"])
    types["GooglePrivacyDlpV2TransformationDetailsIn"] = t.struct(
        {
            "statusDetails": t.proxy(
                renames["GooglePrivacyDlpV2TransformationResultStatusIn"]
            ).optional(),
            "resourceName": t.string().optional(),
            "containerName": t.string().optional(),
            "transformedBytes": t.string().optional(),
            "transformationLocation": t.proxy(
                renames["GooglePrivacyDlpV2TransformationLocationIn"]
            ).optional(),
            "transformation": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationDescriptionIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsIn"])
    types["GooglePrivacyDlpV2TransformationDetailsOut"] = t.struct(
        {
            "statusDetails": t.proxy(
                renames["GooglePrivacyDlpV2TransformationResultStatusOut"]
            ).optional(),
            "resourceName": t.string().optional(),
            "containerName": t.string().optional(),
            "transformedBytes": t.string().optional(),
            "transformationLocation": t.proxy(
                renames["GooglePrivacyDlpV2TransformationLocationOut"]
            ).optional(),
            "transformation": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationDescriptionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsOut"])
    types["GooglePrivacyDlpV2EntityIdIn"] = t.struct(
        {"field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2EntityIdIn"])
    types["GooglePrivacyDlpV2EntityIdOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2EntityIdOut"])
    types["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn"])
    types["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut"])
    types["GooglePrivacyDlpV2ProfileStatusIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ProfileStatusIn"])
    types["GooglePrivacyDlpV2ProfileStatusOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ProfileStatusOut"])
    types["GoogleTypeTimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["GoogleTypeTimeOfDayIn"])
    types["GoogleTypeTimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeTimeOfDayOut"])
    types["GooglePrivacyDlpV2ErrorIn"] = t.struct(
        {
            "timestamps": t.array(t.string()).optional(),
            "details": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ErrorIn"])
    types["GooglePrivacyDlpV2ErrorOut"] = t.struct(
        {
            "timestamps": t.array(t.string()).optional(),
            "details": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ErrorOut"])
    types["GooglePrivacyDlpV2PartitionIdIn"] = t.struct(
        {"projectId": t.string().optional(), "namespaceId": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PartitionIdIn"])
    types["GooglePrivacyDlpV2PartitionIdOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "namespaceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PartitionIdOut"])
    types["GooglePrivacyDlpV2ActionIn"] = t.struct(
        {
            "publishToStackdriver": t.proxy(
                renames["GooglePrivacyDlpV2PublishToStackdriverIn"]
            ).optional(),
            "saveFindings": t.proxy(
                renames["GooglePrivacyDlpV2SaveFindingsIn"]
            ).optional(),
            "pubSub": t.proxy(
                renames["GooglePrivacyDlpV2PublishToPubSubIn"]
            ).optional(),
            "publishFindingsToCloudDataCatalog": t.proxy(
                renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn"]
            ).optional(),
            "publishSummaryToCscc": t.proxy(
                renames["GooglePrivacyDlpV2PublishSummaryToCsccIn"]
            ).optional(),
            "jobNotificationEmails": t.proxy(
                renames["GooglePrivacyDlpV2JobNotificationEmailsIn"]
            ).optional(),
            "deidentify": t.proxy(renames["GooglePrivacyDlpV2DeidentifyIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ActionIn"])
    types["GooglePrivacyDlpV2ActionOut"] = t.struct(
        {
            "publishToStackdriver": t.proxy(
                renames["GooglePrivacyDlpV2PublishToStackdriverOut"]
            ).optional(),
            "saveFindings": t.proxy(
                renames["GooglePrivacyDlpV2SaveFindingsOut"]
            ).optional(),
            "pubSub": t.proxy(
                renames["GooglePrivacyDlpV2PublishToPubSubOut"]
            ).optional(),
            "publishFindingsToCloudDataCatalog": t.proxy(
                renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut"]
            ).optional(),
            "publishSummaryToCscc": t.proxy(
                renames["GooglePrivacyDlpV2PublishSummaryToCsccOut"]
            ).optional(),
            "jobNotificationEmails": t.proxy(
                renames["GooglePrivacyDlpV2JobNotificationEmailsOut"]
            ).optional(),
            "deidentify": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ActionOut"])
    types["GooglePrivacyDlpV2InspectContentResponseIn"] = t.struct(
        {"result": t.proxy(renames["GooglePrivacyDlpV2InspectResultIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2InspectContentResponseIn"])
    types["GooglePrivacyDlpV2InspectContentResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["GooglePrivacyDlpV2InspectResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectContentResponseOut"])
    types["GooglePrivacyDlpV2LikelihoodAdjustmentIn"] = t.struct(
        {
            "relativeLikelihood": t.integer().optional(),
            "fixedLikelihood": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LikelihoodAdjustmentIn"])
    types["GooglePrivacyDlpV2LikelihoodAdjustmentOut"] = t.struct(
        {
            "relativeLikelihood": t.integer().optional(),
            "fixedLikelihood": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LikelihoodAdjustmentOut"])
    types["GooglePrivacyDlpV2DataProfileConfigSnapshotIn"] = t.struct(
        {
            "dataProfileJob": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileJobConfigIn"]
            ).optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileConfigSnapshotIn"])
    types["GooglePrivacyDlpV2DataProfileConfigSnapshotOut"] = t.struct(
        {
            "dataProfileJob": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileJobConfigOut"]
            ).optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileConfigSnapshotOut"])
    types["GooglePrivacyDlpV2PubSubNotificationIn"] = t.struct(
        {
            "event": t.string().optional(),
            "pubsubCondition": t.proxy(
                renames["GooglePrivacyDlpV2DataProfilePubSubConditionIn"]
            ).optional(),
            "detailOfMessage": t.string().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubNotificationIn"])
    types["GooglePrivacyDlpV2PubSubNotificationOut"] = t.struct(
        {
            "event": t.string().optional(),
            "pubsubCondition": t.proxy(
                renames["GooglePrivacyDlpV2DataProfilePubSubConditionOut"]
            ).optional(),
            "detailOfMessage": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubNotificationOut"])
    types["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn"] = t.struct(
        {
            "surrogateInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeIn"]
            ).optional(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyIn"]),
            "customAlphabet": t.string().optional(),
            "radix": t.integer().optional(),
            "commonAlphabet": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn"])
    types["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut"] = t.struct(
        {
            "surrogateInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeOut"]
            ).optional(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyOut"]),
            "customAlphabet": t.string().optional(),
            "radix": t.integer().optional(),
            "commonAlphabet": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut"])
    types["GooglePrivacyDlpV2InspectionRuleSetIn"] = t.struct(
        {
            "rules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleIn"])
            ).optional(),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectionRuleSetIn"])
    types["GooglePrivacyDlpV2InspectionRuleSetOut"] = t.struct(
        {
            "rules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleOut"])
            ).optional(),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectionRuleSetOut"])
    types["GooglePrivacyDlpV2RecordTransformationsIn"] = t.struct(
        {
            "recordSuppressions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2RecordSuppressionIn"])
            ).optional(),
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationsIn"])
    types["GooglePrivacyDlpV2RecordTransformationsOut"] = t.struct(
        {
            "recordSuppressions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2RecordSuppressionOut"])
            ).optional(),
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationsOut"])
    types["GooglePrivacyDlpV2PublishSummaryToCsccIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishSummaryToCsccIn"])
    types["GooglePrivacyDlpV2PublishSummaryToCsccOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2PublishSummaryToCsccOut"])
    types["GooglePrivacyDlpV2HybridInspectResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2HybridInspectResponseIn"])
    types["GooglePrivacyDlpV2HybridInspectResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2HybridInspectResponseOut"])
    types["GooglePrivacyDlpV2InfoTypeSummaryIn"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "estimatedPrevalence": t.integer().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeSummaryIn"])
    types["GooglePrivacyDlpV2InfoTypeSummaryOut"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "estimatedPrevalence": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeSummaryOut"])
    types["GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "deidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestIn"])
    types["GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "deidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestOut"])
    types["GooglePrivacyDlpV2QuasiIdentifierFieldIn"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "customTag": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdentifierFieldIn"])
    types["GooglePrivacyDlpV2QuasiIdentifierFieldOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "customTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdentifierFieldOut"])
    types["GooglePrivacyDlpV2BigQueryKeyIn"] = t.struct(
        {
            "tableReference": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional(),
            "rowNumber": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryKeyIn"])
    types["GooglePrivacyDlpV2BigQueryKeyOut"] = t.struct(
        {
            "tableReference": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "rowNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryKeyOut"])
    types["GooglePrivacyDlpV2LDiversityConfigIn"] = t.struct(
        {
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
            "sensitiveAttribute": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityConfigIn"])
    types["GooglePrivacyDlpV2LDiversityConfigOut"] = t.struct(
        {
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "sensitiveAttribute": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityConfigOut"])
    types["GooglePrivacyDlpV2RequestedDeidentifyOptionsIn"] = t.struct(
        {
            "snapshotDeidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
            ).optional(),
            "snapshotImageRedactTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
            ).optional(),
            "snapshotStructuredDeidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RequestedDeidentifyOptionsIn"])
    types["GooglePrivacyDlpV2RequestedDeidentifyOptionsOut"] = t.struct(
        {
            "snapshotDeidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]
            ).optional(),
            "snapshotImageRedactTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]
            ).optional(),
            "snapshotStructuredDeidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RequestedDeidentifyOptionsOut"])
    types["GooglePrivacyDlpV2LDiversityHistogramBucketIn"] = t.struct(
        {
            "sensitiveValueFrequencyLowerBound": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "sensitiveValueFrequencyUpperBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassIn"])
            ).optional(),
            "bucketSize": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityHistogramBucketIn"])
    types["GooglePrivacyDlpV2LDiversityHistogramBucketOut"] = t.struct(
        {
            "sensitiveValueFrequencyLowerBound": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "sensitiveValueFrequencyUpperBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassOut"])
            ).optional(),
            "bucketSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityHistogramBucketOut"])
    types["GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn"] = t.struct(
        {
            "bucketValueCount": t.string().optional(),
            "valueFrequencyLowerBound": t.string().optional(),
            "bucketSize": t.string().optional(),
            "valueFrequencyUpperBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn"])
    types["GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut"] = t.struct(
        {
            "bucketValueCount": t.string().optional(),
            "valueFrequencyLowerBound": t.string().optional(),
            "bucketSize": t.string().optional(),
            "valueFrequencyUpperBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut"])
    types["GooglePrivacyDlpV2KAnonymityEquivalenceClassIn"] = t.struct(
        {
            "equivalenceClassSize": t.string().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityEquivalenceClassIn"])
    types["GooglePrivacyDlpV2KAnonymityEquivalenceClassOut"] = t.struct(
        {
            "equivalenceClassSize": t.string().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityEquivalenceClassOut"])
    types["GooglePrivacyDlpV2TableLocationIn"] = t.struct(
        {"rowIndex": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2TableLocationIn"])
    types["GooglePrivacyDlpV2TableLocationOut"] = t.struct(
        {
            "rowIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableLocationOut"])
    types["GooglePrivacyDlpV2CryptoHashConfigIn"] = t.struct(
        {"cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2CryptoHashConfigIn"])
    types["GooglePrivacyDlpV2CryptoHashConfigOut"] = t.struct(
        {
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoHashConfigOut"])
    types["GooglePrivacyDlpV2InspectionRuleIn"] = t.struct(
        {
            "exclusionRule": t.proxy(
                renames["GooglePrivacyDlpV2ExclusionRuleIn"]
            ).optional(),
            "hotwordRule": t.proxy(
                renames["GooglePrivacyDlpV2HotwordRuleIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectionRuleIn"])
    types["GooglePrivacyDlpV2InspectionRuleOut"] = t.struct(
        {
            "exclusionRule": t.proxy(
                renames["GooglePrivacyDlpV2ExclusionRuleOut"]
            ).optional(),
            "hotwordRule": t.proxy(
                renames["GooglePrivacyDlpV2HotwordRuleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectionRuleOut"])
    types["GooglePrivacyDlpV2PubSubExpressionsIn"] = t.struct(
        {
            "logicalOperator": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2PubSubConditionIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubExpressionsIn"])
    types["GooglePrivacyDlpV2PubSubExpressionsOut"] = t.struct(
        {
            "logicalOperator": t.string().optional(),
            "conditions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2PubSubConditionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubExpressionsOut"])
    types["GooglePrivacyDlpV2StorageConfigIn"] = t.struct(
        {
            "timespanConfig": t.proxy(renames["GooglePrivacyDlpV2TimespanConfigIn"]),
            "hybridOptions": t.proxy(
                renames["GooglePrivacyDlpV2HybridOptionsIn"]
            ).optional(),
            "bigQueryOptions": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryOptionsIn"]
            ).optional(),
            "datastoreOptions": t.proxy(
                renames["GooglePrivacyDlpV2DatastoreOptionsIn"]
            ).optional(),
            "cloudStorageOptions": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageOptionsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StorageConfigIn"])
    types["GooglePrivacyDlpV2StorageConfigOut"] = t.struct(
        {
            "timespanConfig": t.proxy(renames["GooglePrivacyDlpV2TimespanConfigOut"]),
            "hybridOptions": t.proxy(
                renames["GooglePrivacyDlpV2HybridOptionsOut"]
            ).optional(),
            "bigQueryOptions": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryOptionsOut"]
            ).optional(),
            "datastoreOptions": t.proxy(
                renames["GooglePrivacyDlpV2DatastoreOptionsOut"]
            ).optional(),
            "cloudStorageOptions": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StorageConfigOut"])
    types["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "templateId": t.string().optional(),
            "deidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
            ),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn"])
    types["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "templateId": t.string().optional(),
            "deidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut"])
    types["GooglePrivacyDlpV2QuoteInfoIn"] = t.struct(
        {"dateTime": t.proxy(renames["GooglePrivacyDlpV2DateTimeIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2QuoteInfoIn"])
    types["GooglePrivacyDlpV2QuoteInfoOut"] = t.struct(
        {
            "dateTime": t.proxy(renames["GooglePrivacyDlpV2DateTimeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuoteInfoOut"])
    types["GooglePrivacyDlpV2InfoTypeLimitIn"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "maxFindings": t.integer().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeLimitIn"])
    types["GooglePrivacyDlpV2InfoTypeLimitOut"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "maxFindings": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeLimitOut"])
    types["GooglePrivacyDlpV2BigQueryFieldIn"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableIn"]).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryFieldIn"])
    types["GooglePrivacyDlpV2BigQueryFieldOut"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableOut"]).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryFieldOut"])
    types["GooglePrivacyDlpV2ExpressionsIn"] = t.struct(
        {
            "conditions": t.proxy(renames["GooglePrivacyDlpV2ConditionsIn"]).optional(),
            "logicalOperator": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExpressionsIn"])
    types["GooglePrivacyDlpV2ExpressionsOut"] = t.struct(
        {
            "conditions": t.proxy(
                renames["GooglePrivacyDlpV2ConditionsOut"]
            ).optional(),
            "logicalOperator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExpressionsOut"])
    types["GooglePrivacyDlpV2KAnonymityHistogramBucketIn"] = t.struct(
        {
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KAnonymityEquivalenceClassIn"])
            ).optional(),
            "bucketSize": t.string().optional(),
            "equivalenceClassSizeUpperBound": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "equivalenceClassSizeLowerBound": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityHistogramBucketIn"])
    types["GooglePrivacyDlpV2KAnonymityHistogramBucketOut"] = t.struct(
        {
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KAnonymityEquivalenceClassOut"])
            ).optional(),
            "bucketSize": t.string().optional(),
            "equivalenceClassSizeUpperBound": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "equivalenceClassSizeLowerBound": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityHistogramBucketOut"])
    types["GooglePrivacyDlpV2InfoTypeStatsIn"] = t.struct(
        {
            "count": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeStatsIn"])
    types["GooglePrivacyDlpV2InfoTypeStatsOut"] = t.struct(
        {
            "count": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeStatsOut"])
    types["GooglePrivacyDlpV2TableIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["GooglePrivacyDlpV2RowIn"])).optional(),
            "headers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableIn"])
    types["GooglePrivacyDlpV2TableOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["GooglePrivacyDlpV2RowOut"])).optional(),
            "headers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableOut"])
    types["GooglePrivacyDlpV2CharacterMaskConfigIn"] = t.struct(
        {
            "reverseOrder": t.boolean().optional(),
            "maskingCharacter": t.string().optional(),
            "numberToMask": t.integer().optional(),
            "charactersToIgnore": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CharsToIgnoreIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharacterMaskConfigIn"])
    types["GooglePrivacyDlpV2CharacterMaskConfigOut"] = t.struct(
        {
            "reverseOrder": t.boolean().optional(),
            "maskingCharacter": t.string().optional(),
            "numberToMask": t.integer().optional(),
            "charactersToIgnore": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CharsToIgnoreOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharacterMaskConfigOut"])
    types["GooglePrivacyDlpV2ValueFrequencyIn"] = t.struct(
        {
            "value": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
            "count": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ValueFrequencyIn"])
    types["GooglePrivacyDlpV2ValueFrequencyOut"] = t.struct(
        {
            "value": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ValueFrequencyOut"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn"] = t.struct(
        {
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
            "estimatedProbability": t.number().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut"] = t.struct(
        {
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "estimatedProbability": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut"])
    types["GooglePrivacyDlpV2ListStoredInfoTypesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "storedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseIn"])
    types["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "storedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"])
    types["GooglePrivacyDlpV2QuasiIdFieldIn"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "customTag": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdFieldIn"])
    types["GooglePrivacyDlpV2QuasiIdFieldOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "customTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdFieldOut"])
    types["GooglePrivacyDlpV2CreateDlpJobRequestIn"] = t.struct(
        {
            "riskJob": t.proxy(
                renames["GooglePrivacyDlpV2RiskAnalysisJobConfigIn"]
            ).optional(),
            "locationId": t.string().optional(),
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigIn"]
            ).optional(),
            "jobId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDlpJobRequestIn"])
    types["GooglePrivacyDlpV2CreateDlpJobRequestOut"] = t.struct(
        {
            "riskJob": t.proxy(
                renames["GooglePrivacyDlpV2RiskAnalysisJobConfigOut"]
            ).optional(),
            "locationId": t.string().optional(),
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigOut"]
            ).optional(),
            "jobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDlpJobRequestOut"])
    types["GooglePrivacyDlpV2TransformationErrorHandlingIn"] = t.struct(
        {
            "throwError": t.proxy(renames["GooglePrivacyDlpV2ThrowErrorIn"]).optional(),
            "leaveUntransformed": t.proxy(
                renames["GooglePrivacyDlpV2LeaveUntransformedIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationErrorHandlingIn"])
    types["GooglePrivacyDlpV2TransformationErrorHandlingOut"] = t.struct(
        {
            "throwError": t.proxy(
                renames["GooglePrivacyDlpV2ThrowErrorOut"]
            ).optional(),
            "leaveUntransformed": t.proxy(
                renames["GooglePrivacyDlpV2LeaveUntransformedOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationErrorHandlingOut"])
    types["GooglePrivacyDlpV2LargeCustomDictionaryConfigIn"] = t.struct(
        {
            "outputPath": t.proxy(
                renames["GooglePrivacyDlpV2CloudStoragePathIn"]
            ).optional(),
            "bigQueryField": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryFieldIn"]
            ).optional(),
            "cloudStorageFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageFileSetIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigIn"])
    types["GooglePrivacyDlpV2LargeCustomDictionaryConfigOut"] = t.struct(
        {
            "outputPath": t.proxy(
                renames["GooglePrivacyDlpV2CloudStoragePathOut"]
            ).optional(),
            "bigQueryField": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryFieldOut"]
            ).optional(),
            "cloudStorageFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageFileSetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigOut"])
    types["GooglePrivacyDlpV2BoundingBoxIn"] = t.struct(
        {
            "left": t.integer().optional(),
            "height": t.integer().optional(),
            "top": t.integer().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BoundingBoxIn"])
    types["GooglePrivacyDlpV2BoundingBoxOut"] = t.struct(
        {
            "left": t.integer().optional(),
            "height": t.integer().optional(),
            "top": t.integer().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BoundingBoxOut"])
    types["GooglePrivacyDlpV2JobTriggerIn"] = t.struct(
        {
            "description": t.string().optional(),
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigIn"]
            ).optional(),
            "triggers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TriggerIn"])
            ).optional(),
            "name": t.string().optional(),
            "status": t.string(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2JobTriggerIn"])
    types["GooglePrivacyDlpV2JobTriggerOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "triggers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TriggerOut"])
            ).optional(),
            "lastRunTime": t.string().optional(),
            "name": t.string().optional(),
            "status": t.string(),
            "errors": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ErrorOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2JobTriggerOut"])
    types["GooglePrivacyDlpV2AuxiliaryTableIn"] = t.struct(
        {
            "relativeFrequency": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2QuasiIdFieldIn"])),
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2AuxiliaryTableIn"])
    types["GooglePrivacyDlpV2AuxiliaryTableOut"] = t.struct(
        {
            "relativeFrequency": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2QuasiIdFieldOut"])),
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2AuxiliaryTableOut"])
    types["GooglePrivacyDlpV2PrimitiveTransformationIn"] = t.struct(
        {
            "dateShiftConfig": t.proxy(
                renames["GooglePrivacyDlpV2DateShiftConfigIn"]
            ).optional(),
            "timePartConfig": t.proxy(
                renames["GooglePrivacyDlpV2TimePartConfigIn"]
            ).optional(),
            "cryptoDeterministicConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoDeterministicConfigIn"]
            ).optional(),
            "cryptoHashConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoHashConfigIn"]
            ).optional(),
            "fixedSizeBucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2FixedSizeBucketingConfigIn"]
            ).optional(),
            "replaceDictionaryConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceDictionaryConfigIn"]
            ).optional(),
            "replaceConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceValueConfigIn"]
            ).optional(),
            "cryptoReplaceFfxFpeConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn"]
            ).optional(),
            "characterMaskConfig": t.proxy(
                renames["GooglePrivacyDlpV2CharacterMaskConfigIn"]
            ).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn"]
            ).optional(),
            "redactConfig": t.proxy(
                renames["GooglePrivacyDlpV2RedactConfigIn"]
            ).optional(),
            "bucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2BucketingConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrimitiveTransformationIn"])
    types["GooglePrivacyDlpV2PrimitiveTransformationOut"] = t.struct(
        {
            "dateShiftConfig": t.proxy(
                renames["GooglePrivacyDlpV2DateShiftConfigOut"]
            ).optional(),
            "timePartConfig": t.proxy(
                renames["GooglePrivacyDlpV2TimePartConfigOut"]
            ).optional(),
            "cryptoDeterministicConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoDeterministicConfigOut"]
            ).optional(),
            "cryptoHashConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoHashConfigOut"]
            ).optional(),
            "fixedSizeBucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2FixedSizeBucketingConfigOut"]
            ).optional(),
            "replaceDictionaryConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceDictionaryConfigOut"]
            ).optional(),
            "replaceConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceValueConfigOut"]
            ).optional(),
            "cryptoReplaceFfxFpeConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut"]
            ).optional(),
            "characterMaskConfig": t.proxy(
                renames["GooglePrivacyDlpV2CharacterMaskConfigOut"]
            ).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut"]
            ).optional(),
            "redactConfig": t.proxy(
                renames["GooglePrivacyDlpV2RedactConfigOut"]
            ).optional(),
            "bucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2BucketingConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrimitiveTransformationOut"])

    functions = {}
    functions["infoTypesList"] = dlp.get(
        "v2/infoTypes",
        t.struct(
            {
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "locationId": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesList"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesCreate"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesDelete"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesGet"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesPatch"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsStoredInfoTypesPatch"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsStoredInfoTypesGet"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsStoredInfoTypesDelete"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsStoredInfoTypesList"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsStoredInfoTypesCreate"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesPatch"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesCreate"] = dlp.get(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesGet"] = dlp.get(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesDelete"] = dlp.get(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesPatch"] = dlp.get(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesList"] = dlp.get(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersGet"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "jobTrigger": t.proxy(
                    renames["GooglePrivacyDlpV2JobTriggerIn"]
                ).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersDelete"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "jobTrigger": t.proxy(
                    renames["GooglePrivacyDlpV2JobTriggerIn"]
                ).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersCreate"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "jobTrigger": t.proxy(
                    renames["GooglePrivacyDlpV2JobTriggerIn"]
                ).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersList"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "jobTrigger": t.proxy(
                    renames["GooglePrivacyDlpV2JobTriggerIn"]
                ).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersPatch"] = dlp.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "jobTrigger": t.proxy(
                    renames["GooglePrivacyDlpV2JobTriggerIn"]
                ).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDlpJobsList"] = dlp.get(
        "v2/{parent}/dlpJobs",
        t.struct(
            {
                "filter": t.string().optional(),
                "type": t.string().optional(),
                "pageToken": t.string().optional(),
                "locationId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListDlpJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInspectTemplatesGet"] = dlp.get(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "locationId": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInspectTemplatesDelete"] = dlp.get(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "locationId": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInspectTemplatesCreate"] = dlp.get(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "locationId": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInspectTemplatesPatch"] = dlp.get(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "locationId": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInspectTemplatesList"] = dlp.get(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "locationId": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesDelete"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesPatch"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesGet"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesList"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesCreate"] = dlp.post(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "config": t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]),
                "storedInfoTypeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsInfoTypesList"] = dlp.get(
        "v2/{parent}/infoTypes",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string().optional(),
                "locationId": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsCancel"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInspectTemplatesPatch"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInspectTemplatesList"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInspectTemplatesGet"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInspectTemplatesDelete"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsInspectTemplatesCreate"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsStoredInfoTypesPatch"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsStoredInfoTypesList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsStoredInfoTypesDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsStoredInfoTypesCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsStoredInfoTypesGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobTriggersGet"] = dlp.post(
        "v2/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobTriggersPatch"] = dlp.post(
        "v2/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobTriggersCreate"] = dlp.post(
        "v2/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobTriggersDelete"] = dlp.post(
        "v2/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobTriggersList"] = dlp.post(
        "v2/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobTriggersActivate"] = dlp.post(
        "v2/{name}:activate",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsImageRedact"] = dlp.post(
        "v2/{parent}/image:redact",
        t.struct(
            {
                "parent": t.string().optional(),
                "locationId": t.string().optional(),
                "byteItem": t.proxy(
                    renames["GooglePrivacyDlpV2ByteContentItemIn"]
                ).optional(),
                "includeFindings": t.boolean().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "imageRedactionConfigs": t.array(
                    t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2RedactImageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsHybridInspect"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsCancel"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsFinish"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContentReidentify"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContentInspect"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContentDeidentify"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeidentifyTemplatesPatch"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeidentifyTemplatesCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeidentifyTemplatesDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeidentifyTemplatesList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeidentifyTemplatesGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStoredInfoTypesCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStoredInfoTypesDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStoredInfoTypesList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStoredInfoTypesPatch"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStoredInfoTypesGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesPatch"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesGet"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesList"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesDelete"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesCreate"] = dlp.post(
        "v2/{parent}/inspectTemplates",
        t.struct(
            {
                "parent": t.string(),
                "templateId": t.string().optional(),
                "inspectTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2InspectTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersList"] = dlp.post(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "parent": t.string(),
                "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
                "locationId": t.string().optional(),
                "triggerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersActivate"] = dlp.post(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "parent": t.string(),
                "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
                "locationId": t.string().optional(),
                "triggerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersGet"] = dlp.post(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "parent": t.string(),
                "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
                "locationId": t.string().optional(),
                "triggerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersDelete"] = dlp.post(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "parent": t.string(),
                "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
                "locationId": t.string().optional(),
                "triggerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersHybridInspect"] = dlp.post(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "parent": t.string(),
                "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
                "locationId": t.string().optional(),
                "triggerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersPatch"] = dlp.post(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "parent": t.string(),
                "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
                "locationId": t.string().optional(),
                "triggerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersCreate"] = dlp.post(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "parent": t.string(),
                "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
                "locationId": t.string().optional(),
                "triggerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsImageRedact"] = dlp.post(
        "v2/{parent}/image:redact",
        t.struct(
            {
                "parent": t.string().optional(),
                "locationId": t.string().optional(),
                "byteItem": t.proxy(
                    renames["GooglePrivacyDlpV2ByteContentItemIn"]
                ).optional(),
                "includeFindings": t.boolean().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "imageRedactionConfigs": t.array(
                    t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2RedactImageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContentInspect"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContentReidentify"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContentDeidentify"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeidentifyTemplatesCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeidentifyTemplatesDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeidentifyTemplatesList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeidentifyTemplatesPatch"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeidentifyTemplatesGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="dlp", renames=renames, types=Box(types), functions=Box(functions)
    )
