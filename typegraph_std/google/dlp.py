from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_dlp() -> Import:
    dlp = HTTPRuntime("https://dlp.googleapis.com/")

    renames = {
        "ErrorResponse": "_dlp_1_ErrorResponse",
        "GooglePrivacyDlpV2TableDataProfileIn": "_dlp_2_GooglePrivacyDlpV2TableDataProfileIn",
        "GooglePrivacyDlpV2TableDataProfileOut": "_dlp_3_GooglePrivacyDlpV2TableDataProfileOut",
        "GooglePrivacyDlpV2TransformationErrorHandlingIn": "_dlp_4_GooglePrivacyDlpV2TransformationErrorHandlingIn",
        "GooglePrivacyDlpV2TransformationErrorHandlingOut": "_dlp_5_GooglePrivacyDlpV2TransformationErrorHandlingOut",
        "GooglePrivacyDlpV2PartitionIdIn": "_dlp_6_GooglePrivacyDlpV2PartitionIdIn",
        "GooglePrivacyDlpV2PartitionIdOut": "_dlp_7_GooglePrivacyDlpV2PartitionIdOut",
        "GooglePrivacyDlpV2InspectContentResponseIn": "_dlp_8_GooglePrivacyDlpV2InspectContentResponseIn",
        "GooglePrivacyDlpV2InspectContentResponseOut": "_dlp_9_GooglePrivacyDlpV2InspectContentResponseOut",
        "GooglePrivacyDlpV2DataProfileConfigSnapshotIn": "_dlp_10_GooglePrivacyDlpV2DataProfileConfigSnapshotIn",
        "GooglePrivacyDlpV2DataProfileConfigSnapshotOut": "_dlp_11_GooglePrivacyDlpV2DataProfileConfigSnapshotOut",
        "GooglePrivacyDlpV2TransformationConfigIn": "_dlp_12_GooglePrivacyDlpV2TransformationConfigIn",
        "GooglePrivacyDlpV2TransformationConfigOut": "_dlp_13_GooglePrivacyDlpV2TransformationConfigOut",
        "GooglePrivacyDlpV2KeyIn": "_dlp_14_GooglePrivacyDlpV2KeyIn",
        "GooglePrivacyDlpV2KeyOut": "_dlp_15_GooglePrivacyDlpV2KeyOut",
        "GooglePrivacyDlpV2RequestedOptionsIn": "_dlp_16_GooglePrivacyDlpV2RequestedOptionsIn",
        "GooglePrivacyDlpV2RequestedOptionsOut": "_dlp_17_GooglePrivacyDlpV2RequestedOptionsOut",
        "GooglePrivacyDlpV2PrimitiveTransformationIn": "_dlp_18_GooglePrivacyDlpV2PrimitiveTransformationIn",
        "GooglePrivacyDlpV2PrimitiveTransformationOut": "_dlp_19_GooglePrivacyDlpV2PrimitiveTransformationOut",
        "GooglePrivacyDlpV2KAnonymityConfigIn": "_dlp_20_GooglePrivacyDlpV2KAnonymityConfigIn",
        "GooglePrivacyDlpV2KAnonymityConfigOut": "_dlp_21_GooglePrivacyDlpV2KAnonymityConfigOut",
        "GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn": "_dlp_22_GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn",
        "GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut": "_dlp_23_GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut",
        "GooglePrivacyDlpV2StoredTypeIn": "_dlp_24_GooglePrivacyDlpV2StoredTypeIn",
        "GooglePrivacyDlpV2StoredTypeOut": "_dlp_25_GooglePrivacyDlpV2StoredTypeOut",
        "GooglePrivacyDlpV2HybridInspectDlpJobRequestIn": "_dlp_26_GooglePrivacyDlpV2HybridInspectDlpJobRequestIn",
        "GooglePrivacyDlpV2HybridInspectDlpJobRequestOut": "_dlp_27_GooglePrivacyDlpV2HybridInspectDlpJobRequestOut",
        "GoogleTypeDateIn": "_dlp_28_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_dlp_29_GoogleTypeDateOut",
        "GooglePrivacyDlpV2CustomInfoTypeIn": "_dlp_30_GooglePrivacyDlpV2CustomInfoTypeIn",
        "GooglePrivacyDlpV2CustomInfoTypeOut": "_dlp_31_GooglePrivacyDlpV2CustomInfoTypeOut",
        "GooglePrivacyDlpV2LeaveUntransformedIn": "_dlp_32_GooglePrivacyDlpV2LeaveUntransformedIn",
        "GooglePrivacyDlpV2LeaveUntransformedOut": "_dlp_33_GooglePrivacyDlpV2LeaveUntransformedOut",
        "GooglePrivacyDlpV2ListDlpJobsResponseIn": "_dlp_34_GooglePrivacyDlpV2ListDlpJobsResponseIn",
        "GooglePrivacyDlpV2ListDlpJobsResponseOut": "_dlp_35_GooglePrivacyDlpV2ListDlpJobsResponseOut",
        "GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn": "_dlp_36_GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn",
        "GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut": "_dlp_37_GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut",
        "GooglePrivacyDlpV2ActionDetailsIn": "_dlp_38_GooglePrivacyDlpV2ActionDetailsIn",
        "GooglePrivacyDlpV2ActionDetailsOut": "_dlp_39_GooglePrivacyDlpV2ActionDetailsOut",
        "GooglePrivacyDlpV2HybridInspectStatisticsIn": "_dlp_40_GooglePrivacyDlpV2HybridInspectStatisticsIn",
        "GooglePrivacyDlpV2HybridInspectStatisticsOut": "_dlp_41_GooglePrivacyDlpV2HybridInspectStatisticsOut",
        "GooglePrivacyDlpV2TableLocationIn": "_dlp_42_GooglePrivacyDlpV2TableLocationIn",
        "GooglePrivacyDlpV2TableLocationOut": "_dlp_43_GooglePrivacyDlpV2TableLocationOut",
        "GooglePrivacyDlpV2UnwrappedCryptoKeyIn": "_dlp_44_GooglePrivacyDlpV2UnwrappedCryptoKeyIn",
        "GooglePrivacyDlpV2UnwrappedCryptoKeyOut": "_dlp_45_GooglePrivacyDlpV2UnwrappedCryptoKeyOut",
        "GooglePrivacyDlpV2ReplaceDictionaryConfigIn": "_dlp_46_GooglePrivacyDlpV2ReplaceDictionaryConfigIn",
        "GooglePrivacyDlpV2ReplaceDictionaryConfigOut": "_dlp_47_GooglePrivacyDlpV2ReplaceDictionaryConfigOut",
        "GooglePrivacyDlpV2TransformationOverviewIn": "_dlp_48_GooglePrivacyDlpV2TransformationOverviewIn",
        "GooglePrivacyDlpV2TransformationOverviewOut": "_dlp_49_GooglePrivacyDlpV2TransformationOverviewOut",
        "GooglePrivacyDlpV2PubSubExpressionsIn": "_dlp_50_GooglePrivacyDlpV2PubSubExpressionsIn",
        "GooglePrivacyDlpV2PubSubExpressionsOut": "_dlp_51_GooglePrivacyDlpV2PubSubExpressionsOut",
        "GooglePrivacyDlpV2ContentItemIn": "_dlp_52_GooglePrivacyDlpV2ContentItemIn",
        "GooglePrivacyDlpV2ContentItemOut": "_dlp_53_GooglePrivacyDlpV2ContentItemOut",
        "GooglePrivacyDlpV2BucketingConfigIn": "_dlp_54_GooglePrivacyDlpV2BucketingConfigIn",
        "GooglePrivacyDlpV2BucketingConfigOut": "_dlp_55_GooglePrivacyDlpV2BucketingConfigOut",
        "GooglePrivacyDlpV2HotwordRuleIn": "_dlp_56_GooglePrivacyDlpV2HotwordRuleIn",
        "GooglePrivacyDlpV2HotwordRuleOut": "_dlp_57_GooglePrivacyDlpV2HotwordRuleOut",
        "GooglePrivacyDlpV2RecordSuppressionIn": "_dlp_58_GooglePrivacyDlpV2RecordSuppressionIn",
        "GooglePrivacyDlpV2RecordSuppressionOut": "_dlp_59_GooglePrivacyDlpV2RecordSuppressionOut",
        "GooglePrivacyDlpV2TransformationLocationIn": "_dlp_60_GooglePrivacyDlpV2TransformationLocationIn",
        "GooglePrivacyDlpV2TransformationLocationOut": "_dlp_61_GooglePrivacyDlpV2TransformationLocationOut",
        "GooglePrivacyDlpV2KMapEstimationConfigIn": "_dlp_62_GooglePrivacyDlpV2KMapEstimationConfigIn",
        "GooglePrivacyDlpV2KMapEstimationConfigOut": "_dlp_63_GooglePrivacyDlpV2KMapEstimationConfigOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn": "_dlp_64_GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut": "_dlp_65_GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationResultIn": "_dlp_66_GooglePrivacyDlpV2DeltaPresenceEstimationResultIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationResultOut": "_dlp_67_GooglePrivacyDlpV2DeltaPresenceEstimationResultOut",
        "GooglePrivacyDlpV2DlpJobIn": "_dlp_68_GooglePrivacyDlpV2DlpJobIn",
        "GooglePrivacyDlpV2DlpJobOut": "_dlp_69_GooglePrivacyDlpV2DlpJobOut",
        "GooglePrivacyDlpV2TaggedFieldIn": "_dlp_70_GooglePrivacyDlpV2TaggedFieldIn",
        "GooglePrivacyDlpV2TaggedFieldOut": "_dlp_71_GooglePrivacyDlpV2TaggedFieldOut",
        "GooglePrivacyDlpV2LocationIn": "_dlp_72_GooglePrivacyDlpV2LocationIn",
        "GooglePrivacyDlpV2LocationOut": "_dlp_73_GooglePrivacyDlpV2LocationOut",
        "GooglePrivacyDlpV2TransformationDetailsStorageConfigIn": "_dlp_74_GooglePrivacyDlpV2TransformationDetailsStorageConfigIn",
        "GooglePrivacyDlpV2TransformationDetailsStorageConfigOut": "_dlp_75_GooglePrivacyDlpV2TransformationDetailsStorageConfigOut",
        "GooglePrivacyDlpV2ThrowErrorIn": "_dlp_76_GooglePrivacyDlpV2ThrowErrorIn",
        "GooglePrivacyDlpV2ThrowErrorOut": "_dlp_77_GooglePrivacyDlpV2ThrowErrorOut",
        "GooglePrivacyDlpV2ContentLocationIn": "_dlp_78_GooglePrivacyDlpV2ContentLocationIn",
        "GooglePrivacyDlpV2ContentLocationOut": "_dlp_79_GooglePrivacyDlpV2ContentLocationOut",
        "GooglePrivacyDlpV2DateShiftConfigIn": "_dlp_80_GooglePrivacyDlpV2DateShiftConfigIn",
        "GooglePrivacyDlpV2DateShiftConfigOut": "_dlp_81_GooglePrivacyDlpV2DateShiftConfigOut",
        "GooglePrivacyDlpV2RiskAnalysisJobConfigIn": "_dlp_82_GooglePrivacyDlpV2RiskAnalysisJobConfigIn",
        "GooglePrivacyDlpV2RiskAnalysisJobConfigOut": "_dlp_83_GooglePrivacyDlpV2RiskAnalysisJobConfigOut",
        "GooglePrivacyDlpV2TransientCryptoKeyIn": "_dlp_84_GooglePrivacyDlpV2TransientCryptoKeyIn",
        "GooglePrivacyDlpV2TransientCryptoKeyOut": "_dlp_85_GooglePrivacyDlpV2TransientCryptoKeyOut",
        "GooglePrivacyDlpV2InspectionRuleSetIn": "_dlp_86_GooglePrivacyDlpV2InspectionRuleSetIn",
        "GooglePrivacyDlpV2InspectionRuleSetOut": "_dlp_87_GooglePrivacyDlpV2InspectionRuleSetOut",
        "GooglePrivacyDlpV2CategoricalStatsResultIn": "_dlp_88_GooglePrivacyDlpV2CategoricalStatsResultIn",
        "GooglePrivacyDlpV2CategoricalStatsResultOut": "_dlp_89_GooglePrivacyDlpV2CategoricalStatsResultOut",
        "GooglePrivacyDlpV2DeidentifyConfigIn": "_dlp_90_GooglePrivacyDlpV2DeidentifyConfigIn",
        "GooglePrivacyDlpV2DeidentifyConfigOut": "_dlp_91_GooglePrivacyDlpV2DeidentifyConfigOut",
        "GooglePrivacyDlpV2DeidentifyTemplateIn": "_dlp_92_GooglePrivacyDlpV2DeidentifyTemplateIn",
        "GooglePrivacyDlpV2DeidentifyTemplateOut": "_dlp_93_GooglePrivacyDlpV2DeidentifyTemplateOut",
        "GooglePrivacyDlpV2ExcludeByHotwordIn": "_dlp_94_GooglePrivacyDlpV2ExcludeByHotwordIn",
        "GooglePrivacyDlpV2ExcludeByHotwordOut": "_dlp_95_GooglePrivacyDlpV2ExcludeByHotwordOut",
        "GooglePrivacyDlpV2LDiversityHistogramBucketIn": "_dlp_96_GooglePrivacyDlpV2LDiversityHistogramBucketIn",
        "GooglePrivacyDlpV2LDiversityHistogramBucketOut": "_dlp_97_GooglePrivacyDlpV2LDiversityHistogramBucketOut",
        "GooglePrivacyDlpV2DeidentifyIn": "_dlp_98_GooglePrivacyDlpV2DeidentifyIn",
        "GooglePrivacyDlpV2DeidentifyOut": "_dlp_99_GooglePrivacyDlpV2DeidentifyOut",
        "GooglePrivacyDlpV2QuoteInfoIn": "_dlp_100_GooglePrivacyDlpV2QuoteInfoIn",
        "GooglePrivacyDlpV2QuoteInfoOut": "_dlp_101_GooglePrivacyDlpV2QuoteInfoOut",
        "GooglePrivacyDlpV2VersionDescriptionIn": "_dlp_102_GooglePrivacyDlpV2VersionDescriptionIn",
        "GooglePrivacyDlpV2VersionDescriptionOut": "_dlp_103_GooglePrivacyDlpV2VersionDescriptionOut",
        "GooglePrivacyDlpV2TransformationDescriptionIn": "_dlp_104_GooglePrivacyDlpV2TransformationDescriptionIn",
        "GooglePrivacyDlpV2TransformationDescriptionOut": "_dlp_105_GooglePrivacyDlpV2TransformationDescriptionOut",
        "GooglePrivacyDlpV2InspectContentRequestIn": "_dlp_106_GooglePrivacyDlpV2InspectContentRequestIn",
        "GooglePrivacyDlpV2InspectContentRequestOut": "_dlp_107_GooglePrivacyDlpV2InspectContentRequestOut",
        "GooglePrivacyDlpV2AllTextIn": "_dlp_108_GooglePrivacyDlpV2AllTextIn",
        "GooglePrivacyDlpV2AllTextOut": "_dlp_109_GooglePrivacyDlpV2AllTextOut",
        "GooglePrivacyDlpV2AuxiliaryTableIn": "_dlp_110_GooglePrivacyDlpV2AuxiliaryTableIn",
        "GooglePrivacyDlpV2AuxiliaryTableOut": "_dlp_111_GooglePrivacyDlpV2AuxiliaryTableOut",
        "GooglePrivacyDlpV2CryptoDeterministicConfigIn": "_dlp_112_GooglePrivacyDlpV2CryptoDeterministicConfigIn",
        "GooglePrivacyDlpV2CryptoDeterministicConfigOut": "_dlp_113_GooglePrivacyDlpV2CryptoDeterministicConfigOut",
        "GooglePrivacyDlpV2BigQueryOptionsIn": "_dlp_114_GooglePrivacyDlpV2BigQueryOptionsIn",
        "GooglePrivacyDlpV2BigQueryOptionsOut": "_dlp_115_GooglePrivacyDlpV2BigQueryOptionsOut",
        "GooglePrivacyDlpV2TransformationResultStatusIn": "_dlp_116_GooglePrivacyDlpV2TransformationResultStatusIn",
        "GooglePrivacyDlpV2TransformationResultStatusOut": "_dlp_117_GooglePrivacyDlpV2TransformationResultStatusOut",
        "GooglePrivacyDlpV2CryptoHashConfigIn": "_dlp_118_GooglePrivacyDlpV2CryptoHashConfigIn",
        "GooglePrivacyDlpV2CryptoHashConfigOut": "_dlp_119_GooglePrivacyDlpV2CryptoHashConfigOut",
        "GooglePrivacyDlpV2ConditionIn": "_dlp_120_GooglePrivacyDlpV2ConditionIn",
        "GooglePrivacyDlpV2ConditionOut": "_dlp_121_GooglePrivacyDlpV2ConditionOut",
        "GooglePrivacyDlpV2ListJobTriggersResponseIn": "_dlp_122_GooglePrivacyDlpV2ListJobTriggersResponseIn",
        "GooglePrivacyDlpV2ListJobTriggersResponseOut": "_dlp_123_GooglePrivacyDlpV2ListJobTriggersResponseOut",
        "GooglePrivacyDlpV2InfoTypeStatsIn": "_dlp_124_GooglePrivacyDlpV2InfoTypeStatsIn",
        "GooglePrivacyDlpV2InfoTypeStatsOut": "_dlp_125_GooglePrivacyDlpV2InfoTypeStatsOut",
        "GooglePrivacyDlpV2InspectDataSourceDetailsIn": "_dlp_126_GooglePrivacyDlpV2InspectDataSourceDetailsIn",
        "GooglePrivacyDlpV2InspectDataSourceDetailsOut": "_dlp_127_GooglePrivacyDlpV2InspectDataSourceDetailsOut",
        "GooglePrivacyDlpV2ColorIn": "_dlp_128_GooglePrivacyDlpV2ColorIn",
        "GooglePrivacyDlpV2ColorOut": "_dlp_129_GooglePrivacyDlpV2ColorOut",
        "GooglePrivacyDlpV2InspectionRuleIn": "_dlp_130_GooglePrivacyDlpV2InspectionRuleIn",
        "GooglePrivacyDlpV2InspectionRuleOut": "_dlp_131_GooglePrivacyDlpV2InspectionRuleOut",
        "GooglePrivacyDlpV2ReidentifyContentRequestIn": "_dlp_132_GooglePrivacyDlpV2ReidentifyContentRequestIn",
        "GooglePrivacyDlpV2ReidentifyContentRequestOut": "_dlp_133_GooglePrivacyDlpV2ReidentifyContentRequestOut",
        "GooglePrivacyDlpV2SelectedInfoTypesIn": "_dlp_134_GooglePrivacyDlpV2SelectedInfoTypesIn",
        "GooglePrivacyDlpV2SelectedInfoTypesOut": "_dlp_135_GooglePrivacyDlpV2SelectedInfoTypesOut",
        "GooglePrivacyDlpV2PublishSummaryToCsccIn": "_dlp_136_GooglePrivacyDlpV2PublishSummaryToCsccIn",
        "GooglePrivacyDlpV2PublishSummaryToCsccOut": "_dlp_137_GooglePrivacyDlpV2PublishSummaryToCsccOut",
        "GooglePrivacyDlpV2InspectTemplateIn": "_dlp_138_GooglePrivacyDlpV2InspectTemplateIn",
        "GooglePrivacyDlpV2InspectTemplateOut": "_dlp_139_GooglePrivacyDlpV2InspectTemplateOut",
        "GooglePrivacyDlpV2StorageMetadataLabelIn": "_dlp_140_GooglePrivacyDlpV2StorageMetadataLabelIn",
        "GooglePrivacyDlpV2StorageMetadataLabelOut": "_dlp_141_GooglePrivacyDlpV2StorageMetadataLabelOut",
        "GooglePrivacyDlpV2RequestedDeidentifyOptionsIn": "_dlp_142_GooglePrivacyDlpV2RequestedDeidentifyOptionsIn",
        "GooglePrivacyDlpV2RequestedDeidentifyOptionsOut": "_dlp_143_GooglePrivacyDlpV2RequestedDeidentifyOptionsOut",
        "GooglePrivacyDlpV2InfoTypeIn": "_dlp_144_GooglePrivacyDlpV2InfoTypeIn",
        "GooglePrivacyDlpV2InfoTypeOut": "_dlp_145_GooglePrivacyDlpV2InfoTypeOut",
        "GooglePrivacyDlpV2RangeIn": "_dlp_146_GooglePrivacyDlpV2RangeIn",
        "GooglePrivacyDlpV2RangeOut": "_dlp_147_GooglePrivacyDlpV2RangeOut",
        "GooglePrivacyDlpV2HybridOptionsIn": "_dlp_148_GooglePrivacyDlpV2HybridOptionsIn",
        "GooglePrivacyDlpV2HybridOptionsOut": "_dlp_149_GooglePrivacyDlpV2HybridOptionsOut",
        "GooglePrivacyDlpV2CloudStoragePathIn": "_dlp_150_GooglePrivacyDlpV2CloudStoragePathIn",
        "GooglePrivacyDlpV2CloudStoragePathOut": "_dlp_151_GooglePrivacyDlpV2CloudStoragePathOut",
        "GooglePrivacyDlpV2ImageRedactionConfigIn": "_dlp_152_GooglePrivacyDlpV2ImageRedactionConfigIn",
        "GooglePrivacyDlpV2ImageRedactionConfigOut": "_dlp_153_GooglePrivacyDlpV2ImageRedactionConfigOut",
        "GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn": "_dlp_154_GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn",
        "GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut": "_dlp_155_GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut",
        "GooglePrivacyDlpV2InfoTypeCategoryIn": "_dlp_156_GooglePrivacyDlpV2InfoTypeCategoryIn",
        "GooglePrivacyDlpV2InfoTypeCategoryOut": "_dlp_157_GooglePrivacyDlpV2InfoTypeCategoryOut",
        "GooglePrivacyDlpV2NumericalStatsResultIn": "_dlp_158_GooglePrivacyDlpV2NumericalStatsResultIn",
        "GooglePrivacyDlpV2NumericalStatsResultOut": "_dlp_159_GooglePrivacyDlpV2NumericalStatsResultOut",
        "GooglePrivacyDlpV2InfoTypeSummaryIn": "_dlp_160_GooglePrivacyDlpV2InfoTypeSummaryIn",
        "GooglePrivacyDlpV2InfoTypeSummaryOut": "_dlp_161_GooglePrivacyDlpV2InfoTypeSummaryOut",
        "GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestIn": "_dlp_162_GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestIn",
        "GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestOut": "_dlp_163_GooglePrivacyDlpV2UpdateDeidentifyTemplateRequestOut",
        "GooglePrivacyDlpV2ImageLocationIn": "_dlp_164_GooglePrivacyDlpV2ImageLocationIn",
        "GooglePrivacyDlpV2ImageLocationOut": "_dlp_165_GooglePrivacyDlpV2ImageLocationOut",
        "GooglePrivacyDlpV2StoredInfoTypeIn": "_dlp_166_GooglePrivacyDlpV2StoredInfoTypeIn",
        "GooglePrivacyDlpV2StoredInfoTypeOut": "_dlp_167_GooglePrivacyDlpV2StoredInfoTypeOut",
        "GooglePrivacyDlpV2LDiversityConfigIn": "_dlp_168_GooglePrivacyDlpV2LDiversityConfigIn",
        "GooglePrivacyDlpV2LDiversityConfigOut": "_dlp_169_GooglePrivacyDlpV2LDiversityConfigOut",
        "GooglePrivacyDlpV2LargeCustomDictionaryConfigIn": "_dlp_170_GooglePrivacyDlpV2LargeCustomDictionaryConfigIn",
        "GooglePrivacyDlpV2LargeCustomDictionaryConfigOut": "_dlp_171_GooglePrivacyDlpV2LargeCustomDictionaryConfigOut",
        "GooglePrivacyDlpV2FileSetIn": "_dlp_172_GooglePrivacyDlpV2FileSetIn",
        "GooglePrivacyDlpV2FileSetOut": "_dlp_173_GooglePrivacyDlpV2FileSetOut",
        "GooglePrivacyDlpV2CategoricalStatsConfigIn": "_dlp_174_GooglePrivacyDlpV2CategoricalStatsConfigIn",
        "GooglePrivacyDlpV2CategoricalStatsConfigOut": "_dlp_175_GooglePrivacyDlpV2CategoricalStatsConfigOut",
        "GooglePrivacyDlpV2FieldIdIn": "_dlp_176_GooglePrivacyDlpV2FieldIdIn",
        "GooglePrivacyDlpV2FieldIdOut": "_dlp_177_GooglePrivacyDlpV2FieldIdOut",
        "GooglePrivacyDlpV2StorageConfigIn": "_dlp_178_GooglePrivacyDlpV2StorageConfigIn",
        "GooglePrivacyDlpV2StorageConfigOut": "_dlp_179_GooglePrivacyDlpV2StorageConfigOut",
        "GooglePrivacyDlpV2RecordConditionIn": "_dlp_180_GooglePrivacyDlpV2RecordConditionIn",
        "GooglePrivacyDlpV2RecordConditionOut": "_dlp_181_GooglePrivacyDlpV2RecordConditionOut",
        "GooglePrivacyDlpV2KAnonymityResultIn": "_dlp_182_GooglePrivacyDlpV2KAnonymityResultIn",
        "GooglePrivacyDlpV2KAnonymityResultOut": "_dlp_183_GooglePrivacyDlpV2KAnonymityResultOut",
        "GooglePrivacyDlpV2TimeZoneIn": "_dlp_184_GooglePrivacyDlpV2TimeZoneIn",
        "GooglePrivacyDlpV2TimeZoneOut": "_dlp_185_GooglePrivacyDlpV2TimeZoneOut",
        "GooglePrivacyDlpV2DateTimeIn": "_dlp_186_GooglePrivacyDlpV2DateTimeIn",
        "GooglePrivacyDlpV2DateTimeOut": "_dlp_187_GooglePrivacyDlpV2DateTimeOut",
        "GooglePrivacyDlpV2AllInfoTypesIn": "_dlp_188_GooglePrivacyDlpV2AllInfoTypesIn",
        "GooglePrivacyDlpV2AllInfoTypesOut": "_dlp_189_GooglePrivacyDlpV2AllInfoTypesOut",
        "GooglePrivacyDlpV2ProximityIn": "_dlp_190_GooglePrivacyDlpV2ProximityIn",
        "GooglePrivacyDlpV2ProximityOut": "_dlp_191_GooglePrivacyDlpV2ProximityOut",
        "GoogleRpcStatusIn": "_dlp_192_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_dlp_193_GoogleRpcStatusOut",
        "GooglePrivacyDlpV2LargeCustomDictionaryStatsIn": "_dlp_194_GooglePrivacyDlpV2LargeCustomDictionaryStatsIn",
        "GooglePrivacyDlpV2LargeCustomDictionaryStatsOut": "_dlp_195_GooglePrivacyDlpV2LargeCustomDictionaryStatsOut",
        "GooglePrivacyDlpV2PublishToStackdriverIn": "_dlp_196_GooglePrivacyDlpV2PublishToStackdriverIn",
        "GooglePrivacyDlpV2PublishToStackdriverOut": "_dlp_197_GooglePrivacyDlpV2PublishToStackdriverOut",
        "GooglePrivacyDlpV2RecordTransformationsIn": "_dlp_198_GooglePrivacyDlpV2RecordTransformationsIn",
        "GooglePrivacyDlpV2RecordTransformationsOut": "_dlp_199_GooglePrivacyDlpV2RecordTransformationsOut",
        "GooglePrivacyDlpV2FixedSizeBucketingConfigIn": "_dlp_200_GooglePrivacyDlpV2FixedSizeBucketingConfigIn",
        "GooglePrivacyDlpV2FixedSizeBucketingConfigOut": "_dlp_201_GooglePrivacyDlpV2FixedSizeBucketingConfigOut",
        "GooglePrivacyDlpV2LikelihoodAdjustmentIn": "_dlp_202_GooglePrivacyDlpV2LikelihoodAdjustmentIn",
        "GooglePrivacyDlpV2LikelihoodAdjustmentOut": "_dlp_203_GooglePrivacyDlpV2LikelihoodAdjustmentOut",
        "GooglePrivacyDlpV2DataProfilePubSubMessageIn": "_dlp_204_GooglePrivacyDlpV2DataProfilePubSubMessageIn",
        "GooglePrivacyDlpV2DataProfilePubSubMessageOut": "_dlp_205_GooglePrivacyDlpV2DataProfilePubSubMessageOut",
        "GooglePrivacyDlpV2BigQueryKeyIn": "_dlp_206_GooglePrivacyDlpV2BigQueryKeyIn",
        "GooglePrivacyDlpV2BigQueryKeyOut": "_dlp_207_GooglePrivacyDlpV2BigQueryKeyOut",
        "GooglePrivacyDlpV2HybridContentItemIn": "_dlp_208_GooglePrivacyDlpV2HybridContentItemIn",
        "GooglePrivacyDlpV2HybridContentItemOut": "_dlp_209_GooglePrivacyDlpV2HybridContentItemOut",
        "GooglePrivacyDlpV2KindExpressionIn": "_dlp_210_GooglePrivacyDlpV2KindExpressionIn",
        "GooglePrivacyDlpV2KindExpressionOut": "_dlp_211_GooglePrivacyDlpV2KindExpressionOut",
        "GooglePrivacyDlpV2ReplaceValueConfigIn": "_dlp_212_GooglePrivacyDlpV2ReplaceValueConfigIn",
        "GooglePrivacyDlpV2ReplaceValueConfigOut": "_dlp_213_GooglePrivacyDlpV2ReplaceValueConfigOut",
        "GooglePrivacyDlpV2TransformationDetailsIn": "_dlp_214_GooglePrivacyDlpV2TransformationDetailsIn",
        "GooglePrivacyDlpV2TransformationDetailsOut": "_dlp_215_GooglePrivacyDlpV2TransformationDetailsOut",
        "GooglePrivacyDlpV2CreateInspectTemplateRequestIn": "_dlp_216_GooglePrivacyDlpV2CreateInspectTemplateRequestIn",
        "GooglePrivacyDlpV2CreateInspectTemplateRequestOut": "_dlp_217_GooglePrivacyDlpV2CreateInspectTemplateRequestOut",
        "GooglePrivacyDlpV2LDiversityResultIn": "_dlp_218_GooglePrivacyDlpV2LDiversityResultIn",
        "GooglePrivacyDlpV2LDiversityResultOut": "_dlp_219_GooglePrivacyDlpV2LDiversityResultOut",
        "GooglePrivacyDlpV2InfoTypeLimitIn": "_dlp_220_GooglePrivacyDlpV2InfoTypeLimitIn",
        "GooglePrivacyDlpV2InfoTypeLimitOut": "_dlp_221_GooglePrivacyDlpV2InfoTypeLimitOut",
        "GooglePrivacyDlpV2KAnonymityEquivalenceClassIn": "_dlp_222_GooglePrivacyDlpV2KAnonymityEquivalenceClassIn",
        "GooglePrivacyDlpV2KAnonymityEquivalenceClassOut": "_dlp_223_GooglePrivacyDlpV2KAnonymityEquivalenceClassOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn": "_dlp_224_GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut": "_dlp_225_GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut",
        "GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn": "_dlp_226_GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn",
        "GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut": "_dlp_227_GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut",
        "GooglePrivacyDlpV2ExportIn": "_dlp_228_GooglePrivacyDlpV2ExportIn",
        "GooglePrivacyDlpV2ExportOut": "_dlp_229_GooglePrivacyDlpV2ExportOut",
        "GooglePrivacyDlpV2PubSubNotificationIn": "_dlp_230_GooglePrivacyDlpV2PubSubNotificationIn",
        "GooglePrivacyDlpV2PubSubNotificationOut": "_dlp_231_GooglePrivacyDlpV2PubSubNotificationOut",
        "GooglePrivacyDlpV2BoundingBoxIn": "_dlp_232_GooglePrivacyDlpV2BoundingBoxIn",
        "GooglePrivacyDlpV2BoundingBoxOut": "_dlp_233_GooglePrivacyDlpV2BoundingBoxOut",
        "GooglePrivacyDlpV2DeidentifyContentResponseIn": "_dlp_234_GooglePrivacyDlpV2DeidentifyContentResponseIn",
        "GooglePrivacyDlpV2DeidentifyContentResponseOut": "_dlp_235_GooglePrivacyDlpV2DeidentifyContentResponseOut",
        "GooglePrivacyDlpV2ManualIn": "_dlp_236_GooglePrivacyDlpV2ManualIn",
        "GooglePrivacyDlpV2ManualOut": "_dlp_237_GooglePrivacyDlpV2ManualOut",
        "GooglePrivacyDlpV2QuasiIdFieldIn": "_dlp_238_GooglePrivacyDlpV2QuasiIdFieldIn",
        "GooglePrivacyDlpV2QuasiIdFieldOut": "_dlp_239_GooglePrivacyDlpV2QuasiIdFieldOut",
        "GooglePrivacyDlpV2QuasiIdentifierFieldIn": "_dlp_240_GooglePrivacyDlpV2QuasiIdentifierFieldIn",
        "GooglePrivacyDlpV2QuasiIdentifierFieldOut": "_dlp_241_GooglePrivacyDlpV2QuasiIdentifierFieldOut",
        "GooglePrivacyDlpV2SaveFindingsIn": "_dlp_242_GooglePrivacyDlpV2SaveFindingsIn",
        "GooglePrivacyDlpV2SaveFindingsOut": "_dlp_243_GooglePrivacyDlpV2SaveFindingsOut",
        "GooglePrivacyDlpV2OtherInfoTypeSummaryIn": "_dlp_244_GooglePrivacyDlpV2OtherInfoTypeSummaryIn",
        "GooglePrivacyDlpV2OtherInfoTypeSummaryOut": "_dlp_245_GooglePrivacyDlpV2OtherInfoTypeSummaryOut",
        "GooglePrivacyDlpV2CancelDlpJobRequestIn": "_dlp_246_GooglePrivacyDlpV2CancelDlpJobRequestIn",
        "GooglePrivacyDlpV2CancelDlpJobRequestOut": "_dlp_247_GooglePrivacyDlpV2CancelDlpJobRequestOut",
        "GooglePrivacyDlpV2InspectJobConfigIn": "_dlp_248_GooglePrivacyDlpV2InspectJobConfigIn",
        "GooglePrivacyDlpV2InspectJobConfigOut": "_dlp_249_GooglePrivacyDlpV2InspectJobConfigOut",
        "GooglePrivacyDlpV2LDiversityEquivalenceClassIn": "_dlp_250_GooglePrivacyDlpV2LDiversityEquivalenceClassIn",
        "GooglePrivacyDlpV2LDiversityEquivalenceClassOut": "_dlp_251_GooglePrivacyDlpV2LDiversityEquivalenceClassOut",
        "GooglePrivacyDlpV2DeidentifyDataSourceStatsIn": "_dlp_252_GooglePrivacyDlpV2DeidentifyDataSourceStatsIn",
        "GooglePrivacyDlpV2DeidentifyDataSourceStatsOut": "_dlp_253_GooglePrivacyDlpV2DeidentifyDataSourceStatsOut",
        "GoogleTypeTimeOfDayIn": "_dlp_254_GoogleTypeTimeOfDayIn",
        "GoogleTypeTimeOfDayOut": "_dlp_255_GoogleTypeTimeOfDayOut",
        "GooglePrivacyDlpV2BigQueryTableIn": "_dlp_256_GooglePrivacyDlpV2BigQueryTableIn",
        "GooglePrivacyDlpV2BigQueryTableOut": "_dlp_257_GooglePrivacyDlpV2BigQueryTableOut",
        "GooglePrivacyDlpV2TableOptionsIn": "_dlp_258_GooglePrivacyDlpV2TableOptionsIn",
        "GooglePrivacyDlpV2TableOptionsOut": "_dlp_259_GooglePrivacyDlpV2TableOptionsOut",
        "GooglePrivacyDlpV2OutputStorageConfigIn": "_dlp_260_GooglePrivacyDlpV2OutputStorageConfigIn",
        "GooglePrivacyDlpV2OutputStorageConfigOut": "_dlp_261_GooglePrivacyDlpV2OutputStorageConfigOut",
        "GooglePrivacyDlpV2DetectionRuleIn": "_dlp_262_GooglePrivacyDlpV2DetectionRuleIn",
        "GooglePrivacyDlpV2DetectionRuleOut": "_dlp_263_GooglePrivacyDlpV2DetectionRuleOut",
        "GooglePrivacyDlpV2NumericalStatsConfigIn": "_dlp_264_GooglePrivacyDlpV2NumericalStatsConfigIn",
        "GooglePrivacyDlpV2NumericalStatsConfigOut": "_dlp_265_GooglePrivacyDlpV2NumericalStatsConfigOut",
        "GooglePrivacyDlpV2ReidentifyContentResponseIn": "_dlp_266_GooglePrivacyDlpV2ReidentifyContentResponseIn",
        "GooglePrivacyDlpV2ReidentifyContentResponseOut": "_dlp_267_GooglePrivacyDlpV2ReidentifyContentResponseOut",
        "GooglePrivacyDlpV2HybridFindingDetailsIn": "_dlp_268_GooglePrivacyDlpV2HybridFindingDetailsIn",
        "GooglePrivacyDlpV2HybridFindingDetailsOut": "_dlp_269_GooglePrivacyDlpV2HybridFindingDetailsOut",
        "GooglePrivacyDlpV2ErrorIn": "_dlp_270_GooglePrivacyDlpV2ErrorIn",
        "GooglePrivacyDlpV2ErrorOut": "_dlp_271_GooglePrivacyDlpV2ErrorOut",
        "GooglePrivacyDlpV2InspectConfigIn": "_dlp_272_GooglePrivacyDlpV2InspectConfigIn",
        "GooglePrivacyDlpV2InspectConfigOut": "_dlp_273_GooglePrivacyDlpV2InspectConfigOut",
        "GooglePrivacyDlpV2ImageTransformationIn": "_dlp_274_GooglePrivacyDlpV2ImageTransformationIn",
        "GooglePrivacyDlpV2ImageTransformationOut": "_dlp_275_GooglePrivacyDlpV2ImageTransformationOut",
        "GooglePrivacyDlpV2DatastoreOptionsIn": "_dlp_276_GooglePrivacyDlpV2DatastoreOptionsIn",
        "GooglePrivacyDlpV2DatastoreOptionsOut": "_dlp_277_GooglePrivacyDlpV2DatastoreOptionsOut",
        "GooglePrivacyDlpV2DataProfileActionIn": "_dlp_278_GooglePrivacyDlpV2DataProfileActionIn",
        "GooglePrivacyDlpV2DataProfileActionOut": "_dlp_279_GooglePrivacyDlpV2DataProfileActionOut",
        "GooglePrivacyDlpV2CryptoKeyIn": "_dlp_280_GooglePrivacyDlpV2CryptoKeyIn",
        "GooglePrivacyDlpV2CryptoKeyOut": "_dlp_281_GooglePrivacyDlpV2CryptoKeyOut",
        "GooglePrivacyDlpV2CharsToIgnoreIn": "_dlp_282_GooglePrivacyDlpV2CharsToIgnoreIn",
        "GooglePrivacyDlpV2CharsToIgnoreOut": "_dlp_283_GooglePrivacyDlpV2CharsToIgnoreOut",
        "GooglePrivacyDlpV2ActionIn": "_dlp_284_GooglePrivacyDlpV2ActionIn",
        "GooglePrivacyDlpV2ActionOut": "_dlp_285_GooglePrivacyDlpV2ActionOut",
        "GooglePrivacyDlpV2DictionaryIn": "_dlp_286_GooglePrivacyDlpV2DictionaryIn",
        "GooglePrivacyDlpV2DictionaryOut": "_dlp_287_GooglePrivacyDlpV2DictionaryOut",
        "GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn": "_dlp_288_GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn",
        "GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut": "_dlp_289_GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut",
        "GooglePrivacyDlpV2InfoTypeTransformationIn": "_dlp_290_GooglePrivacyDlpV2InfoTypeTransformationIn",
        "GooglePrivacyDlpV2InfoTypeTransformationOut": "_dlp_291_GooglePrivacyDlpV2InfoTypeTransformationOut",
        "GooglePrivacyDlpV2StatisticalTableIn": "_dlp_292_GooglePrivacyDlpV2StatisticalTableIn",
        "GooglePrivacyDlpV2StatisticalTableOut": "_dlp_293_GooglePrivacyDlpV2StatisticalTableOut",
        "GoogleProtobufEmptyIn": "_dlp_294_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_dlp_295_GoogleProtobufEmptyOut",
        "GooglePrivacyDlpV2BigQueryFieldIn": "_dlp_296_GooglePrivacyDlpV2BigQueryFieldIn",
        "GooglePrivacyDlpV2BigQueryFieldOut": "_dlp_297_GooglePrivacyDlpV2BigQueryFieldOut",
        "GooglePrivacyDlpV2TimePartConfigIn": "_dlp_298_GooglePrivacyDlpV2TimePartConfigIn",
        "GooglePrivacyDlpV2TimePartConfigOut": "_dlp_299_GooglePrivacyDlpV2TimePartConfigOut",
        "GooglePrivacyDlpV2JobTriggerIn": "_dlp_300_GooglePrivacyDlpV2JobTriggerIn",
        "GooglePrivacyDlpV2JobTriggerOut": "_dlp_301_GooglePrivacyDlpV2JobTriggerOut",
        "GooglePrivacyDlpV2TriggerIn": "_dlp_302_GooglePrivacyDlpV2TriggerIn",
        "GooglePrivacyDlpV2TriggerOut": "_dlp_303_GooglePrivacyDlpV2TriggerOut",
        "GooglePrivacyDlpV2FindingIn": "_dlp_304_GooglePrivacyDlpV2FindingIn",
        "GooglePrivacyDlpV2FindingOut": "_dlp_305_GooglePrivacyDlpV2FindingOut",
        "GooglePrivacyDlpV2InfoTypeTransformationsIn": "_dlp_306_GooglePrivacyDlpV2InfoTypeTransformationsIn",
        "GooglePrivacyDlpV2InfoTypeTransformationsOut": "_dlp_307_GooglePrivacyDlpV2InfoTypeTransformationsOut",
        "GooglePrivacyDlpV2ExpressionsIn": "_dlp_308_GooglePrivacyDlpV2ExpressionsIn",
        "GooglePrivacyDlpV2ExpressionsOut": "_dlp_309_GooglePrivacyDlpV2ExpressionsOut",
        "GooglePrivacyDlpV2ListInspectTemplatesResponseIn": "_dlp_310_GooglePrivacyDlpV2ListInspectTemplatesResponseIn",
        "GooglePrivacyDlpV2ListInspectTemplatesResponseOut": "_dlp_311_GooglePrivacyDlpV2ListInspectTemplatesResponseOut",
        "GooglePrivacyDlpV2RegexIn": "_dlp_312_GooglePrivacyDlpV2RegexIn",
        "GooglePrivacyDlpV2RegexOut": "_dlp_313_GooglePrivacyDlpV2RegexOut",
        "GooglePrivacyDlpV2ListInfoTypesResponseIn": "_dlp_314_GooglePrivacyDlpV2ListInfoTypesResponseIn",
        "GooglePrivacyDlpV2ListInfoTypesResponseOut": "_dlp_315_GooglePrivacyDlpV2ListInfoTypesResponseOut",
        "GooglePrivacyDlpV2WordListIn": "_dlp_316_GooglePrivacyDlpV2WordListIn",
        "GooglePrivacyDlpV2WordListOut": "_dlp_317_GooglePrivacyDlpV2WordListOut",
        "GooglePrivacyDlpV2PrivacyMetricIn": "_dlp_318_GooglePrivacyDlpV2PrivacyMetricIn",
        "GooglePrivacyDlpV2PrivacyMetricOut": "_dlp_319_GooglePrivacyDlpV2PrivacyMetricOut",
        "GooglePrivacyDlpV2FieldTransformationIn": "_dlp_320_GooglePrivacyDlpV2FieldTransformationIn",
        "GooglePrivacyDlpV2FieldTransformationOut": "_dlp_321_GooglePrivacyDlpV2FieldTransformationOut",
        "GooglePrivacyDlpV2ExclusionRuleIn": "_dlp_322_GooglePrivacyDlpV2ExclusionRuleIn",
        "GooglePrivacyDlpV2ExclusionRuleOut": "_dlp_323_GooglePrivacyDlpV2ExclusionRuleOut",
        "GooglePrivacyDlpV2RowIn": "_dlp_324_GooglePrivacyDlpV2RowIn",
        "GooglePrivacyDlpV2RowOut": "_dlp_325_GooglePrivacyDlpV2RowOut",
        "GooglePrivacyDlpV2MetadataLocationIn": "_dlp_326_GooglePrivacyDlpV2MetadataLocationIn",
        "GooglePrivacyDlpV2MetadataLocationOut": "_dlp_327_GooglePrivacyDlpV2MetadataLocationOut",
        "GooglePrivacyDlpV2TimespanConfigIn": "_dlp_328_GooglePrivacyDlpV2TimespanConfigIn",
        "GooglePrivacyDlpV2TimespanConfigOut": "_dlp_329_GooglePrivacyDlpV2TimespanConfigOut",
        "GooglePrivacyDlpV2RecordTransformationIn": "_dlp_330_GooglePrivacyDlpV2RecordTransformationIn",
        "GooglePrivacyDlpV2RecordTransformationOut": "_dlp_331_GooglePrivacyDlpV2RecordTransformationOut",
        "GooglePrivacyDlpV2UpdateJobTriggerRequestIn": "_dlp_332_GooglePrivacyDlpV2UpdateJobTriggerRequestIn",
        "GooglePrivacyDlpV2UpdateJobTriggerRequestOut": "_dlp_333_GooglePrivacyDlpV2UpdateJobTriggerRequestOut",
        "GooglePrivacyDlpV2EntityIdIn": "_dlp_334_GooglePrivacyDlpV2EntityIdIn",
        "GooglePrivacyDlpV2EntityIdOut": "_dlp_335_GooglePrivacyDlpV2EntityIdOut",
        "GooglePrivacyDlpV2CloudStorageFileSetIn": "_dlp_336_GooglePrivacyDlpV2CloudStorageFileSetIn",
        "GooglePrivacyDlpV2CloudStorageFileSetOut": "_dlp_337_GooglePrivacyDlpV2CloudStorageFileSetOut",
        "GooglePrivacyDlpV2JobNotificationEmailsIn": "_dlp_338_GooglePrivacyDlpV2JobNotificationEmailsIn",
        "GooglePrivacyDlpV2JobNotificationEmailsOut": "_dlp_339_GooglePrivacyDlpV2JobNotificationEmailsOut",
        "GooglePrivacyDlpV2UpdateInspectTemplateRequestIn": "_dlp_340_GooglePrivacyDlpV2UpdateInspectTemplateRequestIn",
        "GooglePrivacyDlpV2UpdateInspectTemplateRequestOut": "_dlp_341_GooglePrivacyDlpV2UpdateInspectTemplateRequestOut",
        "GooglePrivacyDlpV2RecordKeyIn": "_dlp_342_GooglePrivacyDlpV2RecordKeyIn",
        "GooglePrivacyDlpV2RecordKeyOut": "_dlp_343_GooglePrivacyDlpV2RecordKeyOut",
        "GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn": "_dlp_344_GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn",
        "GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut": "_dlp_345_GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut",
        "GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn": "_dlp_346_GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn",
        "GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut": "_dlp_347_GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut",
        "GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn": "_dlp_348_GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn",
        "GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut": "_dlp_349_GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut",
        "GooglePrivacyDlpV2HybridInspectJobTriggerRequestIn": "_dlp_350_GooglePrivacyDlpV2HybridInspectJobTriggerRequestIn",
        "GooglePrivacyDlpV2HybridInspectJobTriggerRequestOut": "_dlp_351_GooglePrivacyDlpV2HybridInspectJobTriggerRequestOut",
        "GooglePrivacyDlpV2PubSubConditionIn": "_dlp_352_GooglePrivacyDlpV2PubSubConditionIn",
        "GooglePrivacyDlpV2PubSubConditionOut": "_dlp_353_GooglePrivacyDlpV2PubSubConditionOut",
        "GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn": "_dlp_354_GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn",
        "GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut": "_dlp_355_GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut",
        "GooglePrivacyDlpV2DataProfileLocationIn": "_dlp_356_GooglePrivacyDlpV2DataProfileLocationIn",
        "GooglePrivacyDlpV2DataProfileLocationOut": "_dlp_357_GooglePrivacyDlpV2DataProfileLocationOut",
        "GooglePrivacyDlpV2RedactImageResponseIn": "_dlp_358_GooglePrivacyDlpV2RedactImageResponseIn",
        "GooglePrivacyDlpV2RedactImageResponseOut": "_dlp_359_GooglePrivacyDlpV2RedactImageResponseOut",
        "GooglePrivacyDlpV2ListStoredInfoTypesResponseIn": "_dlp_360_GooglePrivacyDlpV2ListStoredInfoTypesResponseIn",
        "GooglePrivacyDlpV2ListStoredInfoTypesResponseOut": "_dlp_361_GooglePrivacyDlpV2ListStoredInfoTypesResponseOut",
        "GooglePrivacyDlpV2RedactConfigIn": "_dlp_362_GooglePrivacyDlpV2RedactConfigIn",
        "GooglePrivacyDlpV2RedactConfigOut": "_dlp_363_GooglePrivacyDlpV2RedactConfigOut",
        "GooglePrivacyDlpV2DocumentLocationIn": "_dlp_364_GooglePrivacyDlpV2DocumentLocationIn",
        "GooglePrivacyDlpV2DocumentLocationOut": "_dlp_365_GooglePrivacyDlpV2DocumentLocationOut",
        "GooglePrivacyDlpV2CharacterMaskConfigIn": "_dlp_366_GooglePrivacyDlpV2CharacterMaskConfigIn",
        "GooglePrivacyDlpV2CharacterMaskConfigOut": "_dlp_367_GooglePrivacyDlpV2CharacterMaskConfigOut",
        "GooglePrivacyDlpV2InspectResultIn": "_dlp_368_GooglePrivacyDlpV2InspectResultIn",
        "GooglePrivacyDlpV2InspectResultOut": "_dlp_369_GooglePrivacyDlpV2InspectResultOut",
        "GooglePrivacyDlpV2SurrogateTypeIn": "_dlp_370_GooglePrivacyDlpV2SurrogateTypeIn",
        "GooglePrivacyDlpV2SurrogateTypeOut": "_dlp_371_GooglePrivacyDlpV2SurrogateTypeOut",
        "GooglePrivacyDlpV2KMapEstimationResultIn": "_dlp_372_GooglePrivacyDlpV2KMapEstimationResultIn",
        "GooglePrivacyDlpV2KMapEstimationResultOut": "_dlp_373_GooglePrivacyDlpV2KMapEstimationResultOut",
        "GooglePrivacyDlpV2CloudStorageRegexFileSetIn": "_dlp_374_GooglePrivacyDlpV2CloudStorageRegexFileSetIn",
        "GooglePrivacyDlpV2CloudStorageRegexFileSetOut": "_dlp_375_GooglePrivacyDlpV2CloudStorageRegexFileSetOut",
        "GooglePrivacyDlpV2ValueFrequencyIn": "_dlp_376_GooglePrivacyDlpV2ValueFrequencyIn",
        "GooglePrivacyDlpV2ValueFrequencyOut": "_dlp_377_GooglePrivacyDlpV2ValueFrequencyOut",
        "GooglePrivacyDlpV2ActivateJobTriggerRequestIn": "_dlp_378_GooglePrivacyDlpV2ActivateJobTriggerRequestIn",
        "GooglePrivacyDlpV2ActivateJobTriggerRequestOut": "_dlp_379_GooglePrivacyDlpV2ActivateJobTriggerRequestOut",
        "GooglePrivacyDlpV2HybridInspectResponseIn": "_dlp_380_GooglePrivacyDlpV2HybridInspectResponseIn",
        "GooglePrivacyDlpV2HybridInspectResponseOut": "_dlp_381_GooglePrivacyDlpV2HybridInspectResponseOut",
        "GooglePrivacyDlpV2CreateDlpJobRequestIn": "_dlp_382_GooglePrivacyDlpV2CreateDlpJobRequestIn",
        "GooglePrivacyDlpV2CreateDlpJobRequestOut": "_dlp_383_GooglePrivacyDlpV2CreateDlpJobRequestOut",
        "GooglePrivacyDlpV2DataRiskLevelIn": "_dlp_384_GooglePrivacyDlpV2DataRiskLevelIn",
        "GooglePrivacyDlpV2DataRiskLevelOut": "_dlp_385_GooglePrivacyDlpV2DataRiskLevelOut",
        "GooglePrivacyDlpV2KMapEstimationHistogramBucketIn": "_dlp_386_GooglePrivacyDlpV2KMapEstimationHistogramBucketIn",
        "GooglePrivacyDlpV2KMapEstimationHistogramBucketOut": "_dlp_387_GooglePrivacyDlpV2KMapEstimationHistogramBucketOut",
        "GooglePrivacyDlpV2KAnonymityHistogramBucketIn": "_dlp_388_GooglePrivacyDlpV2KAnonymityHistogramBucketIn",
        "GooglePrivacyDlpV2KAnonymityHistogramBucketOut": "_dlp_389_GooglePrivacyDlpV2KAnonymityHistogramBucketOut",
        "GooglePrivacyDlpV2ResultIn": "_dlp_390_GooglePrivacyDlpV2ResultIn",
        "GooglePrivacyDlpV2ResultOut": "_dlp_391_GooglePrivacyDlpV2ResultOut",
        "GooglePrivacyDlpV2RedactImageRequestIn": "_dlp_392_GooglePrivacyDlpV2RedactImageRequestIn",
        "GooglePrivacyDlpV2RedactImageRequestOut": "_dlp_393_GooglePrivacyDlpV2RedactImageRequestOut",
        "GooglePrivacyDlpV2BucketIn": "_dlp_394_GooglePrivacyDlpV2BucketIn",
        "GooglePrivacyDlpV2BucketOut": "_dlp_395_GooglePrivacyDlpV2BucketOut",
        "GooglePrivacyDlpV2InfoTypeDescriptionIn": "_dlp_396_GooglePrivacyDlpV2InfoTypeDescriptionIn",
        "GooglePrivacyDlpV2InfoTypeDescriptionOut": "_dlp_397_GooglePrivacyDlpV2InfoTypeDescriptionOut",
        "GooglePrivacyDlpV2PathElementIn": "_dlp_398_GooglePrivacyDlpV2PathElementIn",
        "GooglePrivacyDlpV2PathElementOut": "_dlp_399_GooglePrivacyDlpV2PathElementOut",
        "GooglePrivacyDlpV2StoredInfoTypeStatsIn": "_dlp_400_GooglePrivacyDlpV2StoredInfoTypeStatsIn",
        "GooglePrivacyDlpV2StoredInfoTypeStatsOut": "_dlp_401_GooglePrivacyDlpV2StoredInfoTypeStatsOut",
        "GooglePrivacyDlpV2ContainerIn": "_dlp_402_GooglePrivacyDlpV2ContainerIn",
        "GooglePrivacyDlpV2ContainerOut": "_dlp_403_GooglePrivacyDlpV2ContainerOut",
        "GooglePrivacyDlpV2CloudStorageOptionsIn": "_dlp_404_GooglePrivacyDlpV2CloudStorageOptionsIn",
        "GooglePrivacyDlpV2CloudStorageOptionsOut": "_dlp_405_GooglePrivacyDlpV2CloudStorageOptionsOut",
        "GooglePrivacyDlpV2DatastoreKeyIn": "_dlp_406_GooglePrivacyDlpV2DatastoreKeyIn",
        "GooglePrivacyDlpV2DatastoreKeyOut": "_dlp_407_GooglePrivacyDlpV2DatastoreKeyOut",
        "GooglePrivacyDlpV2StoredInfoTypeConfigIn": "_dlp_408_GooglePrivacyDlpV2StoredInfoTypeConfigIn",
        "GooglePrivacyDlpV2StoredInfoTypeConfigOut": "_dlp_409_GooglePrivacyDlpV2StoredInfoTypeConfigOut",
        "GooglePrivacyDlpV2ByteContentItemIn": "_dlp_410_GooglePrivacyDlpV2ByteContentItemIn",
        "GooglePrivacyDlpV2ByteContentItemOut": "_dlp_411_GooglePrivacyDlpV2ByteContentItemOut",
        "GooglePrivacyDlpV2PublishToPubSubIn": "_dlp_412_GooglePrivacyDlpV2PublishToPubSubIn",
        "GooglePrivacyDlpV2PublishToPubSubOut": "_dlp_413_GooglePrivacyDlpV2PublishToPubSubOut",
        "GooglePrivacyDlpV2StoredInfoTypeVersionIn": "_dlp_414_GooglePrivacyDlpV2StoredInfoTypeVersionIn",
        "GooglePrivacyDlpV2StoredInfoTypeVersionOut": "_dlp_415_GooglePrivacyDlpV2StoredInfoTypeVersionOut",
        "GooglePrivacyDlpV2ValueIn": "_dlp_416_GooglePrivacyDlpV2ValueIn",
        "GooglePrivacyDlpV2ValueOut": "_dlp_417_GooglePrivacyDlpV2ValueOut",
        "GooglePrivacyDlpV2CreateJobTriggerRequestIn": "_dlp_418_GooglePrivacyDlpV2CreateJobTriggerRequestIn",
        "GooglePrivacyDlpV2CreateJobTriggerRequestOut": "_dlp_419_GooglePrivacyDlpV2CreateJobTriggerRequestOut",
        "GooglePrivacyDlpV2FindingLimitsIn": "_dlp_420_GooglePrivacyDlpV2FindingLimitsIn",
        "GooglePrivacyDlpV2FindingLimitsOut": "_dlp_421_GooglePrivacyDlpV2FindingLimitsOut",
        "GooglePrivacyDlpV2CreateStoredInfoTypeRequestIn": "_dlp_422_GooglePrivacyDlpV2CreateStoredInfoTypeRequestIn",
        "GooglePrivacyDlpV2CreateStoredInfoTypeRequestOut": "_dlp_423_GooglePrivacyDlpV2CreateStoredInfoTypeRequestOut",
        "GooglePrivacyDlpV2SensitivityScoreIn": "_dlp_424_GooglePrivacyDlpV2SensitivityScoreIn",
        "GooglePrivacyDlpV2SensitivityScoreOut": "_dlp_425_GooglePrivacyDlpV2SensitivityScoreOut",
        "GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn": "_dlp_426_GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn",
        "GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut": "_dlp_427_GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut",
        "GooglePrivacyDlpV2DataProfilePubSubConditionIn": "_dlp_428_GooglePrivacyDlpV2DataProfilePubSubConditionIn",
        "GooglePrivacyDlpV2DataProfilePubSubConditionOut": "_dlp_429_GooglePrivacyDlpV2DataProfilePubSubConditionOut",
        "GooglePrivacyDlpV2ProfileStatusIn": "_dlp_430_GooglePrivacyDlpV2ProfileStatusIn",
        "GooglePrivacyDlpV2ProfileStatusOut": "_dlp_431_GooglePrivacyDlpV2ProfileStatusOut",
        "GooglePrivacyDlpV2DataProfileJobConfigIn": "_dlp_432_GooglePrivacyDlpV2DataProfileJobConfigIn",
        "GooglePrivacyDlpV2DataProfileJobConfigOut": "_dlp_433_GooglePrivacyDlpV2DataProfileJobConfigOut",
        "GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn": "_dlp_434_GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn",
        "GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut": "_dlp_435_GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut",
        "GooglePrivacyDlpV2KmsWrappedCryptoKeyIn": "_dlp_436_GooglePrivacyDlpV2KmsWrappedCryptoKeyIn",
        "GooglePrivacyDlpV2KmsWrappedCryptoKeyOut": "_dlp_437_GooglePrivacyDlpV2KmsWrappedCryptoKeyOut",
        "GooglePrivacyDlpV2SummaryResultIn": "_dlp_438_GooglePrivacyDlpV2SummaryResultIn",
        "GooglePrivacyDlpV2SummaryResultOut": "_dlp_439_GooglePrivacyDlpV2SummaryResultOut",
        "GooglePrivacyDlpV2ConditionsIn": "_dlp_440_GooglePrivacyDlpV2ConditionsIn",
        "GooglePrivacyDlpV2ConditionsOut": "_dlp_441_GooglePrivacyDlpV2ConditionsOut",
        "GooglePrivacyDlpV2QuasiIdIn": "_dlp_442_GooglePrivacyDlpV2QuasiIdIn",
        "GooglePrivacyDlpV2QuasiIdOut": "_dlp_443_GooglePrivacyDlpV2QuasiIdOut",
        "GooglePrivacyDlpV2TransformationSummaryIn": "_dlp_444_GooglePrivacyDlpV2TransformationSummaryIn",
        "GooglePrivacyDlpV2TransformationSummaryOut": "_dlp_445_GooglePrivacyDlpV2TransformationSummaryOut",
        "GooglePrivacyDlpV2ExcludeInfoTypesIn": "_dlp_446_GooglePrivacyDlpV2ExcludeInfoTypesIn",
        "GooglePrivacyDlpV2ExcludeInfoTypesOut": "_dlp_447_GooglePrivacyDlpV2ExcludeInfoTypesOut",
        "GooglePrivacyDlpV2ScheduleIn": "_dlp_448_GooglePrivacyDlpV2ScheduleIn",
        "GooglePrivacyDlpV2ScheduleOut": "_dlp_449_GooglePrivacyDlpV2ScheduleOut",
        "GooglePrivacyDlpV2TableIn": "_dlp_450_GooglePrivacyDlpV2TableIn",
        "GooglePrivacyDlpV2TableOut": "_dlp_451_GooglePrivacyDlpV2TableOut",
        "GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn": "_dlp_452_GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn",
        "GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut": "_dlp_453_GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut",
        "GooglePrivacyDlpV2ImageTransformationsIn": "_dlp_454_GooglePrivacyDlpV2ImageTransformationsIn",
        "GooglePrivacyDlpV2ImageTransformationsOut": "_dlp_455_GooglePrivacyDlpV2ImageTransformationsOut",
        "GooglePrivacyDlpV2FinishDlpJobRequestIn": "_dlp_456_GooglePrivacyDlpV2FinishDlpJobRequestIn",
        "GooglePrivacyDlpV2FinishDlpJobRequestOut": "_dlp_457_GooglePrivacyDlpV2FinishDlpJobRequestOut",
        "GooglePrivacyDlpV2DeidentifyContentRequestIn": "_dlp_458_GooglePrivacyDlpV2DeidentifyContentRequestIn",
        "GooglePrivacyDlpV2DeidentifyContentRequestOut": "_dlp_459_GooglePrivacyDlpV2DeidentifyContentRequestOut",
        "GooglePrivacyDlpV2RecordLocationIn": "_dlp_460_GooglePrivacyDlpV2RecordLocationIn",
        "GooglePrivacyDlpV2RecordLocationOut": "_dlp_461_GooglePrivacyDlpV2RecordLocationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GooglePrivacyDlpV2TableDataProfileIn"] = t.struct(
        {
            "encryptionStatus": t.string().optional(),
            "resourceVisibility": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "configSnapshot": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileConfigSnapshotIn"]
            ).optional(),
            "expirationTime": t.string().optional(),
            "predictedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeSummaryIn"])
            ).optional(),
            "otherInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryIn"])
            ).optional(),
            "tableId": t.string().optional(),
            "datasetLocation": t.string().optional(),
            "datasetProjectId": t.string().optional(),
            "rowCount": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "state": t.string().optional(),
            "profileStatus": t.proxy(
                renames["GooglePrivacyDlpV2ProfileStatusIn"]
            ).optional(),
            "profileLastGenerated": t.string().optional(),
            "datasetId": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "fullResource": t.string().optional(),
            "dataRiskLevel": t.proxy(
                renames["GooglePrivacyDlpV2DataRiskLevelIn"]
            ).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "tableSizeBytes": t.string().optional(),
            "failedColumnCount": t.string().optional(),
            "scannedColumnCount": t.string().optional(),
            "projectDataProfile": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableDataProfileIn"])
    types["GooglePrivacyDlpV2TableDataProfileOut"] = t.struct(
        {
            "encryptionStatus": t.string().optional(),
            "resourceVisibility": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "configSnapshot": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileConfigSnapshotOut"]
            ).optional(),
            "expirationTime": t.string().optional(),
            "predictedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeSummaryOut"])
            ).optional(),
            "otherInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryOut"])
            ).optional(),
            "tableId": t.string().optional(),
            "datasetLocation": t.string().optional(),
            "datasetProjectId": t.string().optional(),
            "rowCount": t.string().optional(),
            "lastModifiedTime": t.string().optional(),
            "state": t.string().optional(),
            "profileStatus": t.proxy(
                renames["GooglePrivacyDlpV2ProfileStatusOut"]
            ).optional(),
            "profileLastGenerated": t.string().optional(),
            "datasetId": t.string().optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "fullResource": t.string().optional(),
            "dataRiskLevel": t.proxy(
                renames["GooglePrivacyDlpV2DataRiskLevelOut"]
            ).optional(),
            "resourceLabels": t.struct({"_": t.string().optional()}).optional(),
            "tableSizeBytes": t.string().optional(),
            "failedColumnCount": t.string().optional(),
            "scannedColumnCount": t.string().optional(),
            "projectDataProfile": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableDataProfileOut"])
    types["GooglePrivacyDlpV2TransformationErrorHandlingIn"] = t.struct(
        {
            "leaveUntransformed": t.proxy(
                renames["GooglePrivacyDlpV2LeaveUntransformedIn"]
            ).optional(),
            "throwError": t.proxy(renames["GooglePrivacyDlpV2ThrowErrorIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationErrorHandlingIn"])
    types["GooglePrivacyDlpV2TransformationErrorHandlingOut"] = t.struct(
        {
            "leaveUntransformed": t.proxy(
                renames["GooglePrivacyDlpV2LeaveUntransformedOut"]
            ).optional(),
            "throwError": t.proxy(
                renames["GooglePrivacyDlpV2ThrowErrorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationErrorHandlingOut"])
    types["GooglePrivacyDlpV2PartitionIdIn"] = t.struct(
        {"namespaceId": t.string().optional(), "projectId": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PartitionIdIn"])
    types["GooglePrivacyDlpV2PartitionIdOut"] = t.struct(
        {
            "namespaceId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PartitionIdOut"])
    types["GooglePrivacyDlpV2InspectContentResponseIn"] = t.struct(
        {"result": t.proxy(renames["GooglePrivacyDlpV2InspectResultIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2InspectContentResponseIn"])
    types["GooglePrivacyDlpV2InspectContentResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["GooglePrivacyDlpV2InspectResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectContentResponseOut"])
    types["GooglePrivacyDlpV2DataProfileConfigSnapshotIn"] = t.struct(
        {
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "dataProfileJob": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileJobConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileConfigSnapshotIn"])
    types["GooglePrivacyDlpV2DataProfileConfigSnapshotOut"] = t.struct(
        {
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "dataProfileJob": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileJobConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileConfigSnapshotOut"])
    types["GooglePrivacyDlpV2TransformationConfigIn"] = t.struct(
        {
            "structuredDeidentifyTemplate": t.string().optional(),
            "imageRedactTemplate": t.string().optional(),
            "deidentifyTemplate": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationConfigIn"])
    types["GooglePrivacyDlpV2TransformationConfigOut"] = t.struct(
        {
            "structuredDeidentifyTemplate": t.string().optional(),
            "imageRedactTemplate": t.string().optional(),
            "deidentifyTemplate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationConfigOut"])
    types["GooglePrivacyDlpV2KeyIn"] = t.struct(
        {
            "path": t.array(
                t.proxy(renames["GooglePrivacyDlpV2PathElementIn"])
            ).optional(),
            "partitionId": t.proxy(
                renames["GooglePrivacyDlpV2PartitionIdIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KeyIn"])
    types["GooglePrivacyDlpV2KeyOut"] = t.struct(
        {
            "path": t.array(
                t.proxy(renames["GooglePrivacyDlpV2PathElementOut"])
            ).optional(),
            "partitionId": t.proxy(
                renames["GooglePrivacyDlpV2PartitionIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KeyOut"])
    types["GooglePrivacyDlpV2RequestedOptionsIn"] = t.struct(
        {
            "jobConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigIn"]
            ).optional(),
            "snapshotInspectTemplate": t.proxy(
                renames["GooglePrivacyDlpV2InspectTemplateIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RequestedOptionsIn"])
    types["GooglePrivacyDlpV2RequestedOptionsOut"] = t.struct(
        {
            "jobConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigOut"]
            ).optional(),
            "snapshotInspectTemplate": t.proxy(
                renames["GooglePrivacyDlpV2InspectTemplateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RequestedOptionsOut"])
    types["GooglePrivacyDlpV2PrimitiveTransformationIn"] = t.struct(
        {
            "dateShiftConfig": t.proxy(
                renames["GooglePrivacyDlpV2DateShiftConfigIn"]
            ).optional(),
            "bucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2BucketingConfigIn"]
            ).optional(),
            "cryptoHashConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoHashConfigIn"]
            ).optional(),
            "timePartConfig": t.proxy(
                renames["GooglePrivacyDlpV2TimePartConfigIn"]
            ).optional(),
            "characterMaskConfig": t.proxy(
                renames["GooglePrivacyDlpV2CharacterMaskConfigIn"]
            ).optional(),
            "fixedSizeBucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2FixedSizeBucketingConfigIn"]
            ).optional(),
            "cryptoReplaceFfxFpeConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn"]
            ).optional(),
            "replaceConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceValueConfigIn"]
            ).optional(),
            "replaceDictionaryConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceDictionaryConfigIn"]
            ).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn"]
            ).optional(),
            "redactConfig": t.proxy(
                renames["GooglePrivacyDlpV2RedactConfigIn"]
            ).optional(),
            "cryptoDeterministicConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoDeterministicConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrimitiveTransformationIn"])
    types["GooglePrivacyDlpV2PrimitiveTransformationOut"] = t.struct(
        {
            "dateShiftConfig": t.proxy(
                renames["GooglePrivacyDlpV2DateShiftConfigOut"]
            ).optional(),
            "bucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2BucketingConfigOut"]
            ).optional(),
            "cryptoHashConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoHashConfigOut"]
            ).optional(),
            "timePartConfig": t.proxy(
                renames["GooglePrivacyDlpV2TimePartConfigOut"]
            ).optional(),
            "characterMaskConfig": t.proxy(
                renames["GooglePrivacyDlpV2CharacterMaskConfigOut"]
            ).optional(),
            "fixedSizeBucketingConfig": t.proxy(
                renames["GooglePrivacyDlpV2FixedSizeBucketingConfigOut"]
            ).optional(),
            "cryptoReplaceFfxFpeConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut"]
            ).optional(),
            "replaceConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceValueConfigOut"]
            ).optional(),
            "replaceDictionaryConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceDictionaryConfigOut"]
            ).optional(),
            "replaceWithInfoTypeConfig": t.proxy(
                renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut"]
            ).optional(),
            "redactConfig": t.proxy(
                renames["GooglePrivacyDlpV2RedactConfigOut"]
            ).optional(),
            "cryptoDeterministicConfig": t.proxy(
                renames["GooglePrivacyDlpV2CryptoDeterministicConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrimitiveTransformationOut"])
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
    types["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn"] = t.struct(
        {
            "kAnonymityResult": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityResultIn"]
            ).optional(),
            "categoricalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsResultIn"]
            ).optional(),
            "kMapEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationResultIn"]
            ).optional(),
            "requestedPrivacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricIn"]
            ).optional(),
            "requestedSourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional(),
            "deltaPresenceEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationResultIn"]
            ).optional(),
            "lDiversityResult": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityResultIn"]
            ).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsIn"]
            ).optional(),
            "numericalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsResultIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn"])
    types["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut"] = t.struct(
        {
            "kAnonymityResult": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityResultOut"]
            ).optional(),
            "categoricalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsResultOut"]
            ).optional(),
            "kMapEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationResultOut"]
            ).optional(),
            "requestedPrivacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricOut"]
            ).optional(),
            "requestedSourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "deltaPresenceEstimationResult": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationResultOut"]
            ).optional(),
            "lDiversityResult": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityResultOut"]
            ).optional(),
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedRiskAnalysisOptionsOut"]
            ).optional(),
            "numericalStatsResult": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsResultOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut"])
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
    types["GooglePrivacyDlpV2CustomInfoTypeIn"] = t.struct(
        {
            "dictionary": t.proxy(renames["GooglePrivacyDlpV2DictionaryIn"]).optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "exclusionType": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "surrogateType": t.proxy(
                renames["GooglePrivacyDlpV2SurrogateTypeIn"]
            ).optional(),
            "storedType": t.proxy(renames["GooglePrivacyDlpV2StoredTypeIn"]).optional(),
            "detectionRules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DetectionRuleIn"])
            ).optional(),
            "likelihood": t.string().optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CustomInfoTypeIn"])
    types["GooglePrivacyDlpV2CustomInfoTypeOut"] = t.struct(
        {
            "dictionary": t.proxy(
                renames["GooglePrivacyDlpV2DictionaryOut"]
            ).optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "exclusionType": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "surrogateType": t.proxy(
                renames["GooglePrivacyDlpV2SurrogateTypeOut"]
            ).optional(),
            "storedType": t.proxy(
                renames["GooglePrivacyDlpV2StoredTypeOut"]
            ).optional(),
            "detectionRules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DetectionRuleOut"])
            ).optional(),
            "likelihood": t.string().optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CustomInfoTypeOut"])
    types["GooglePrivacyDlpV2LeaveUntransformedIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2LeaveUntransformedIn"])
    types["GooglePrivacyDlpV2LeaveUntransformedOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2LeaveUntransformedOut"])
    types["GooglePrivacyDlpV2ListDlpJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GooglePrivacyDlpV2DlpJobIn"])).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDlpJobsResponseIn"])
    types["GooglePrivacyDlpV2ListDlpJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["GooglePrivacyDlpV2DlpJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDlpJobsResponseOut"])
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
    types["GooglePrivacyDlpV2HybridInspectStatisticsIn"] = t.struct(
        {
            "abortedCount": t.string().optional(),
            "pendingCount": t.string().optional(),
            "processedCount": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectStatisticsIn"])
    types["GooglePrivacyDlpV2HybridInspectStatisticsOut"] = t.struct(
        {
            "abortedCount": t.string().optional(),
            "pendingCount": t.string().optional(),
            "processedCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridInspectStatisticsOut"])
    types["GooglePrivacyDlpV2TableLocationIn"] = t.struct(
        {"rowIndex": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2TableLocationIn"])
    types["GooglePrivacyDlpV2TableLocationOut"] = t.struct(
        {
            "rowIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableLocationOut"])
    types["GooglePrivacyDlpV2UnwrappedCryptoKeyIn"] = t.struct(
        {"key": t.string()}
    ).named(renames["GooglePrivacyDlpV2UnwrappedCryptoKeyIn"])
    types["GooglePrivacyDlpV2UnwrappedCryptoKeyOut"] = t.struct(
        {"key": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2UnwrappedCryptoKeyOut"])
    types["GooglePrivacyDlpV2ReplaceDictionaryConfigIn"] = t.struct(
        {"wordList": t.proxy(renames["GooglePrivacyDlpV2WordListIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceDictionaryConfigIn"])
    types["GooglePrivacyDlpV2ReplaceDictionaryConfigOut"] = t.struct(
        {
            "wordList": t.proxy(renames["GooglePrivacyDlpV2WordListOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReplaceDictionaryConfigOut"])
    types["GooglePrivacyDlpV2TransformationOverviewIn"] = t.struct(
        {
            "transformationSummaries": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationSummaryIn"])
            ).optional(),
            "transformedBytes": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationOverviewIn"])
    types["GooglePrivacyDlpV2TransformationOverviewOut"] = t.struct(
        {
            "transformationSummaries": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationSummaryOut"])
            ).optional(),
            "transformedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationOverviewOut"])
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
    types["GooglePrivacyDlpV2ContentItemIn"] = t.struct(
        {
            "value": t.string().optional(),
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemIn"]
            ).optional(),
            "table": t.proxy(renames["GooglePrivacyDlpV2TableIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentItemIn"])
    types["GooglePrivacyDlpV2ContentItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemOut"]
            ).optional(),
            "table": t.proxy(renames["GooglePrivacyDlpV2TableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentItemOut"])
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
    types["GooglePrivacyDlpV2HotwordRuleIn"] = t.struct(
        {
            "likelihoodAdjustment": t.proxy(
                renames["GooglePrivacyDlpV2LikelihoodAdjustmentIn"]
            ).optional(),
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HotwordRuleIn"])
    types["GooglePrivacyDlpV2HotwordRuleOut"] = t.struct(
        {
            "likelihoodAdjustment": t.proxy(
                renames["GooglePrivacyDlpV2LikelihoodAdjustmentOut"]
            ).optional(),
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HotwordRuleOut"])
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
    types["GooglePrivacyDlpV2TransformationLocationIn"] = t.struct(
        {
            "containerType": t.string().optional(),
            "recordTransformation": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationIn"]
            ).optional(),
            "findingId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationLocationIn"])
    types["GooglePrivacyDlpV2TransformationLocationOut"] = t.struct(
        {
            "containerType": t.string().optional(),
            "recordTransformation": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationOut"]
            ).optional(),
            "findingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationLocationOut"])
    types["GooglePrivacyDlpV2KMapEstimationConfigIn"] = t.struct(
        {
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2AuxiliaryTableIn"])
            ).optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2TaggedFieldIn"])),
            "regionCode": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationConfigIn"])
    types["GooglePrivacyDlpV2KMapEstimationConfigOut"] = t.struct(
        {
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2AuxiliaryTableOut"])
            ).optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2TaggedFieldOut"])),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationConfigOut"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn"] = t.struct(
        {
            "bucketValueCount": t.string().optional(),
            "maxProbability": t.number().optional(),
            "bucketValues": t.array(
                t.proxy(
                    renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn"]
                )
            ).optional(),
            "bucketSize": t.string().optional(),
            "minProbability": t.number().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketIn"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut"] = t.struct(
        {
            "bucketValueCount": t.string().optional(),
            "maxProbability": t.number().optional(),
            "bucketValues": t.array(
                t.proxy(
                    renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut"]
                )
            ).optional(),
            "bucketSize": t.string().optional(),
            "minProbability": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucketOut"])
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
    types["GooglePrivacyDlpV2DlpJobIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["GooglePrivacyDlpV2ErrorIn"])).optional(),
            "type": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "jobTriggerName": t.string().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "actionDetails": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionDetailsIn"])
            ).optional(),
            "riskDetails": t.proxy(
                renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsIn"]
            ).optional(),
            "inspectDetails": t.proxy(
                renames["GooglePrivacyDlpV2InspectDataSourceDetailsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DlpJobIn"])
    types["GooglePrivacyDlpV2DlpJobOut"] = t.struct(
        {
            "errors": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ErrorOut"])
            ).optional(),
            "type": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "jobTriggerName": t.string().optional(),
            "startTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "actionDetails": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionDetailsOut"])
            ).optional(),
            "riskDetails": t.proxy(
                renames["GooglePrivacyDlpV2AnalyzeDataSourceRiskDetailsOut"]
            ).optional(),
            "inspectDetails": t.proxy(
                renames["GooglePrivacyDlpV2InspectDataSourceDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DlpJobOut"])
    types["GooglePrivacyDlpV2TaggedFieldIn"] = t.struct(
        {
            "customTag": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "inferred": t.proxy(renames["GoogleProtobufEmptyIn"]).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2TaggedFieldIn"])
    types["GooglePrivacyDlpV2TaggedFieldOut"] = t.struct(
        {
            "customTag": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "inferred": t.proxy(renames["GoogleProtobufEmptyOut"]).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TaggedFieldOut"])
    types["GooglePrivacyDlpV2LocationIn"] = t.struct(
        {
            "container": t.proxy(renames["GooglePrivacyDlpV2ContainerIn"]).optional(),
            "codepointRange": t.proxy(renames["GooglePrivacyDlpV2RangeIn"]).optional(),
            "contentLocations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ContentLocationIn"])
            ).optional(),
            "byteRange": t.proxy(renames["GooglePrivacyDlpV2RangeIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LocationIn"])
    types["GooglePrivacyDlpV2LocationOut"] = t.struct(
        {
            "container": t.proxy(renames["GooglePrivacyDlpV2ContainerOut"]).optional(),
            "codepointRange": t.proxy(renames["GooglePrivacyDlpV2RangeOut"]).optional(),
            "contentLocations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ContentLocationOut"])
            ).optional(),
            "byteRange": t.proxy(renames["GooglePrivacyDlpV2RangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LocationOut"])
    types["GooglePrivacyDlpV2TransformationDetailsStorageConfigIn"] = t.struct(
        {"table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigIn"])
    types["GooglePrivacyDlpV2TransformationDetailsStorageConfigOut"] = t.struct(
        {
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigOut"])
    types["GooglePrivacyDlpV2ThrowErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ThrowErrorIn"])
    types["GooglePrivacyDlpV2ThrowErrorOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ThrowErrorOut"])
    types["GooglePrivacyDlpV2ContentLocationIn"] = t.struct(
        {
            "documentLocation": t.proxy(
                renames["GooglePrivacyDlpV2DocumentLocationIn"]
            ).optional(),
            "imageLocation": t.proxy(
                renames["GooglePrivacyDlpV2ImageLocationIn"]
            ).optional(),
            "containerTimestamp": t.string().optional(),
            "containerName": t.string().optional(),
            "containerVersion": t.string().optional(),
            "recordLocation": t.proxy(
                renames["GooglePrivacyDlpV2RecordLocationIn"]
            ).optional(),
            "metadataLocation": t.proxy(
                renames["GooglePrivacyDlpV2MetadataLocationIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentLocationIn"])
    types["GooglePrivacyDlpV2ContentLocationOut"] = t.struct(
        {
            "documentLocation": t.proxy(
                renames["GooglePrivacyDlpV2DocumentLocationOut"]
            ).optional(),
            "imageLocation": t.proxy(
                renames["GooglePrivacyDlpV2ImageLocationOut"]
            ).optional(),
            "containerTimestamp": t.string().optional(),
            "containerName": t.string().optional(),
            "containerVersion": t.string().optional(),
            "recordLocation": t.proxy(
                renames["GooglePrivacyDlpV2RecordLocationOut"]
            ).optional(),
            "metadataLocation": t.proxy(
                renames["GooglePrivacyDlpV2MetadataLocationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContentLocationOut"])
    types["GooglePrivacyDlpV2DateShiftConfigIn"] = t.struct(
        {
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyIn"]).optional(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "upperBoundDays": t.integer(),
            "lowerBoundDays": t.integer(),
        }
    ).named(renames["GooglePrivacyDlpV2DateShiftConfigIn"])
    types["GooglePrivacyDlpV2DateShiftConfigOut"] = t.struct(
        {
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyOut"]).optional(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "upperBoundDays": t.integer(),
            "lowerBoundDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DateShiftConfigOut"])
    types["GooglePrivacyDlpV2RiskAnalysisJobConfigIn"] = t.struct(
        {
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionIn"])
            ).optional(),
            "privacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricIn"]
            ).optional(),
            "sourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RiskAnalysisJobConfigIn"])
    types["GooglePrivacyDlpV2RiskAnalysisJobConfigOut"] = t.struct(
        {
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionOut"])
            ).optional(),
            "privacyMetric": t.proxy(
                renames["GooglePrivacyDlpV2PrivacyMetricOut"]
            ).optional(),
            "sourceTable": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RiskAnalysisJobConfigOut"])
    types["GooglePrivacyDlpV2TransientCryptoKeyIn"] = t.struct(
        {"name": t.string()}
    ).named(renames["GooglePrivacyDlpV2TransientCryptoKeyIn"])
    types["GooglePrivacyDlpV2TransientCryptoKeyOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2TransientCryptoKeyOut"])
    types["GooglePrivacyDlpV2InspectionRuleSetIn"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"])
            ).optional(),
            "rules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectionRuleSetIn"])
    types["GooglePrivacyDlpV2InspectionRuleSetOut"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])
            ).optional(),
            "rules": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectionRuleSetOut"])
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
    types["GooglePrivacyDlpV2DeidentifyConfigIn"] = t.struct(
        {
            "recordTransformations": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationsIn"]
            ).optional(),
            "transformationErrorHandling": t.proxy(
                renames["GooglePrivacyDlpV2TransformationErrorHandlingIn"]
            ).optional(),
            "imageTransformations": t.proxy(
                renames["GooglePrivacyDlpV2ImageTransformationsIn"]
            ).optional(),
            "infoTypeTransformations": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeTransformationsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyConfigIn"])
    types["GooglePrivacyDlpV2DeidentifyConfigOut"] = t.struct(
        {
            "recordTransformations": t.proxy(
                renames["GooglePrivacyDlpV2RecordTransformationsOut"]
            ).optional(),
            "transformationErrorHandling": t.proxy(
                renames["GooglePrivacyDlpV2TransformationErrorHandlingOut"]
            ).optional(),
            "imageTransformations": t.proxy(
                renames["GooglePrivacyDlpV2ImageTransformationsOut"]
            ).optional(),
            "infoTypeTransformations": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeTransformationsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyConfigOut"])
    types["GooglePrivacyDlpV2DeidentifyTemplateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyTemplateIn"])
    types["GooglePrivacyDlpV2DeidentifyTemplateOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"])
    types["GooglePrivacyDlpV2ExcludeByHotwordIn"] = t.struct(
        {
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExcludeByHotwordIn"])
    types["GooglePrivacyDlpV2ExcludeByHotwordOut"] = t.struct(
        {
            "hotwordRegex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "proximity": t.proxy(renames["GooglePrivacyDlpV2ProximityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExcludeByHotwordOut"])
    types["GooglePrivacyDlpV2LDiversityHistogramBucketIn"] = t.struct(
        {
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassIn"])
            ).optional(),
            "sensitiveValueFrequencyLowerBound": t.string().optional(),
            "sensitiveValueFrequencyUpperBound": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "bucketSize": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityHistogramBucketIn"])
    types["GooglePrivacyDlpV2LDiversityHistogramBucketOut"] = t.struct(
        {
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassOut"])
            ).optional(),
            "sensitiveValueFrequencyLowerBound": t.string().optional(),
            "sensitiveValueFrequencyUpperBound": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "bucketSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityHistogramBucketOut"])
    types["GooglePrivacyDlpV2DeidentifyIn"] = t.struct(
        {
            "cloudStorageOutput": t.string(),
            "transformationConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationConfigIn"]
            ).optional(),
            "fileTypesToTransform": t.array(t.string()).optional(),
            "transformationDetailsStorageConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyIn"])
    types["GooglePrivacyDlpV2DeidentifyOut"] = t.struct(
        {
            "cloudStorageOutput": t.string(),
            "transformationConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationConfigOut"]
            ).optional(),
            "fileTypesToTransform": t.array(t.string()).optional(),
            "transformationDetailsStorageConfig": t.proxy(
                renames["GooglePrivacyDlpV2TransformationDetailsStorageConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyOut"])
    types["GooglePrivacyDlpV2QuoteInfoIn"] = t.struct(
        {"dateTime": t.proxy(renames["GooglePrivacyDlpV2DateTimeIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2QuoteInfoIn"])
    types["GooglePrivacyDlpV2QuoteInfoOut"] = t.struct(
        {
            "dateTime": t.proxy(renames["GooglePrivacyDlpV2DateTimeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuoteInfoOut"])
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
    types["GooglePrivacyDlpV2TransformationDescriptionIn"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDescriptionIn"])
    types["GooglePrivacyDlpV2TransformationDescriptionOut"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "description": t.string().optional(),
            "condition": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDescriptionOut"])
    types["GooglePrivacyDlpV2InspectContentRequestIn"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
            "locationId": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectContentRequestIn"])
    types["GooglePrivacyDlpV2InspectContentRequestOut"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "locationId": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectContentRequestOut"])
    types["GooglePrivacyDlpV2AllTextIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooglePrivacyDlpV2AllTextIn"]
    )
    types["GooglePrivacyDlpV2AllTextOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2AllTextOut"])
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
    types["GooglePrivacyDlpV2BigQueryOptionsIn"] = t.struct(
        {
            "rowsLimit": t.string().optional(),
            "tableReference": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableIn"]
            ).optional(),
            "includedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
            "sampleMethod": t.string(),
            "excludedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
            "rowsLimitPercent": t.integer().optional(),
            "identifyingFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryOptionsIn"])
    types["GooglePrivacyDlpV2BigQueryOptionsOut"] = t.struct(
        {
            "rowsLimit": t.string().optional(),
            "tableReference": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryTableOut"]
            ).optional(),
            "includedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "sampleMethod": t.string(),
            "excludedFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "rowsLimitPercent": t.integer().optional(),
            "identifyingFields": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BigQueryOptionsOut"])
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
    types["GooglePrivacyDlpV2CryptoHashConfigIn"] = t.struct(
        {"cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2CryptoHashConfigIn"])
    types["GooglePrivacyDlpV2CryptoHashConfigOut"] = t.struct(
        {
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoHashConfigOut"])
    types["GooglePrivacyDlpV2ConditionIn"] = t.struct(
        {
            "value": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
            "operator": t.string(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2ConditionIn"])
    types["GooglePrivacyDlpV2ConditionOut"] = t.struct(
        {
            "value": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "operator": t.string(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ConditionOut"])
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
    types["GooglePrivacyDlpV2InspectDataSourceDetailsIn"] = t.struct(
        {
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedOptionsIn"]
            ).optional(),
            "result": t.proxy(renames["GooglePrivacyDlpV2ResultIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectDataSourceDetailsIn"])
    types["GooglePrivacyDlpV2InspectDataSourceDetailsOut"] = t.struct(
        {
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedOptionsOut"]
            ).optional(),
            "result": t.proxy(renames["GooglePrivacyDlpV2ResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectDataSourceDetailsOut"])
    types["GooglePrivacyDlpV2ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ColorIn"])
    types["GooglePrivacyDlpV2ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ColorOut"])
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
    types["GooglePrivacyDlpV2ReidentifyContentRequestIn"] = t.struct(
        {
            "reidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
            ).optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
            "reidentifyTemplateName": t.string().optional(),
            "locationId": t.string().optional(),
            "inspectTemplateName": t.string().optional(),
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
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "reidentifyTemplateName": t.string().optional(),
            "locationId": t.string().optional(),
            "inspectTemplateName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReidentifyContentRequestOut"])
    types["GooglePrivacyDlpV2SelectedInfoTypesIn"] = t.struct(
        {"infoTypes": t.array(t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]))}
    ).named(renames["GooglePrivacyDlpV2SelectedInfoTypesIn"])
    types["GooglePrivacyDlpV2SelectedInfoTypesOut"] = t.struct(
        {
            "infoTypes": t.array(t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SelectedInfoTypesOut"])
    types["GooglePrivacyDlpV2PublishSummaryToCsccIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishSummaryToCsccIn"])
    types["GooglePrivacyDlpV2PublishSummaryToCsccOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2PublishSummaryToCsccOut"])
    types["GooglePrivacyDlpV2InspectTemplateIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectTemplateIn"])
    types["GooglePrivacyDlpV2InspectTemplateOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectTemplateOut"])
    types["GooglePrivacyDlpV2StorageMetadataLabelIn"] = t.struct(
        {"key": t.string()}
    ).named(renames["GooglePrivacyDlpV2StorageMetadataLabelIn"])
    types["GooglePrivacyDlpV2StorageMetadataLabelOut"] = t.struct(
        {"key": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2StorageMetadataLabelOut"])
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
    types["GooglePrivacyDlpV2HybridOptionsIn"] = t.struct(
        {
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsIn"]
            ).optional(),
            "requiredFindingLabelKeys": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridOptionsIn"])
    types["GooglePrivacyDlpV2HybridOptionsOut"] = t.struct(
        {
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsOut"]
            ).optional(),
            "requiredFindingLabelKeys": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridOptionsOut"])
    types["GooglePrivacyDlpV2CloudStoragePathIn"] = t.struct(
        {"path": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2CloudStoragePathIn"])
    types["GooglePrivacyDlpV2CloudStoragePathOut"] = t.struct(
        {
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStoragePathOut"])
    types["GooglePrivacyDlpV2ImageRedactionConfigIn"] = t.struct(
        {
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorIn"]).optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "redactAllText": t.boolean().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
    types["GooglePrivacyDlpV2ImageRedactionConfigOut"] = t.struct(
        {
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorOut"]).optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "redactAllText": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageRedactionConfigOut"])
    types["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn"] = t.struct(
        {
            "commonAlphabet": t.string().optional(),
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyIn"]),
            "customAlphabet": t.string().optional(),
            "radix": t.integer().optional(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "surrogateInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigIn"])
    types["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut"] = t.struct(
        {
            "commonAlphabet": t.string().optional(),
            "cryptoKey": t.proxy(renames["GooglePrivacyDlpV2CryptoKeyOut"]),
            "customAlphabet": t.string().optional(),
            "radix": t.integer().optional(),
            "context": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "surrogateInfoType": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CryptoReplaceFfxFpeConfigOut"])
    types["GooglePrivacyDlpV2InfoTypeCategoryIn"] = t.struct(
        {
            "industryCategory": t.string().optional(),
            "locationCategory": t.string().optional(),
            "typeCategory": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeCategoryIn"])
    types["GooglePrivacyDlpV2InfoTypeCategoryOut"] = t.struct(
        {
            "industryCategory": t.string().optional(),
            "locationCategory": t.string().optional(),
            "typeCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeCategoryOut"])
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
    types["GooglePrivacyDlpV2InfoTypeSummaryIn"] = t.struct(
        {
            "estimatedPrevalence": t.integer().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeSummaryIn"])
    types["GooglePrivacyDlpV2InfoTypeSummaryOut"] = t.struct(
        {
            "estimatedPrevalence": t.integer().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
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
    types["GooglePrivacyDlpV2StoredInfoTypeIn"] = t.struct(
        {
            "pendingVersions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeVersionIn"])
            ).optional(),
            "name": t.string().optional(),
            "currentVersion": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeVersionIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeIn"])
    types["GooglePrivacyDlpV2StoredInfoTypeOut"] = t.struct(
        {
            "pendingVersions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeVersionOut"])
            ).optional(),
            "name": t.string().optional(),
            "currentVersion": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeVersionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeOut"])
    types["GooglePrivacyDlpV2LDiversityConfigIn"] = t.struct(
        {
            "sensitiveAttribute": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdIn"]
            ).optional(),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityConfigIn"])
    types["GooglePrivacyDlpV2LDiversityConfigOut"] = t.struct(
        {
            "sensitiveAttribute": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdOut"]
            ).optional(),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityConfigOut"])
    types["GooglePrivacyDlpV2LargeCustomDictionaryConfigIn"] = t.struct(
        {
            "cloudStorageFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageFileSetIn"]
            ).optional(),
            "bigQueryField": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryFieldIn"]
            ).optional(),
            "outputPath": t.proxy(
                renames["GooglePrivacyDlpV2CloudStoragePathIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigIn"])
    types["GooglePrivacyDlpV2LargeCustomDictionaryConfigOut"] = t.struct(
        {
            "cloudStorageFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageFileSetOut"]
            ).optional(),
            "bigQueryField": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryFieldOut"]
            ).optional(),
            "outputPath": t.proxy(
                renames["GooglePrivacyDlpV2CloudStoragePathOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigOut"])
    types["GooglePrivacyDlpV2FileSetIn"] = t.struct(
        {
            "url": t.string().optional(),
            "regexFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageRegexFileSetIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FileSetIn"])
    types["GooglePrivacyDlpV2FileSetOut"] = t.struct(
        {
            "url": t.string().optional(),
            "regexFileSet": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageRegexFileSetOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FileSetOut"])
    types["GooglePrivacyDlpV2CategoricalStatsConfigIn"] = t.struct(
        {"field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsConfigIn"])
    types["GooglePrivacyDlpV2CategoricalStatsConfigOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsConfigOut"])
    types["GooglePrivacyDlpV2FieldIdIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2FieldIdIn"])
    types["GooglePrivacyDlpV2FieldIdOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FieldIdOut"])
    types["GooglePrivacyDlpV2StorageConfigIn"] = t.struct(
        {
            "datastoreOptions": t.proxy(
                renames["GooglePrivacyDlpV2DatastoreOptionsIn"]
            ).optional(),
            "bigQueryOptions": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryOptionsIn"]
            ).optional(),
            "hybridOptions": t.proxy(
                renames["GooglePrivacyDlpV2HybridOptionsIn"]
            ).optional(),
            "cloudStorageOptions": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageOptionsIn"]
            ).optional(),
            "timespanConfig": t.proxy(renames["GooglePrivacyDlpV2TimespanConfigIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2StorageConfigIn"])
    types["GooglePrivacyDlpV2StorageConfigOut"] = t.struct(
        {
            "datastoreOptions": t.proxy(
                renames["GooglePrivacyDlpV2DatastoreOptionsOut"]
            ).optional(),
            "bigQueryOptions": t.proxy(
                renames["GooglePrivacyDlpV2BigQueryOptionsOut"]
            ).optional(),
            "hybridOptions": t.proxy(
                renames["GooglePrivacyDlpV2HybridOptionsOut"]
            ).optional(),
            "cloudStorageOptions": t.proxy(
                renames["GooglePrivacyDlpV2CloudStorageOptionsOut"]
            ).optional(),
            "timespanConfig": t.proxy(renames["GooglePrivacyDlpV2TimespanConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StorageConfigOut"])
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
    types["GooglePrivacyDlpV2TimeZoneIn"] = t.struct(
        {"offsetMinutes": t.integer().optional()}
    ).named(renames["GooglePrivacyDlpV2TimeZoneIn"])
    types["GooglePrivacyDlpV2TimeZoneOut"] = t.struct(
        {
            "offsetMinutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimeZoneOut"])
    types["GooglePrivacyDlpV2DateTimeIn"] = t.struct(
        {
            "time": t.proxy(renames["GoogleTypeTimeOfDayIn"]).optional(),
            "date": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "dayOfWeek": t.string().optional(),
            "timeZone": t.proxy(renames["GooglePrivacyDlpV2TimeZoneIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DateTimeIn"])
    types["GooglePrivacyDlpV2DateTimeOut"] = t.struct(
        {
            "time": t.proxy(renames["GoogleTypeTimeOfDayOut"]).optional(),
            "date": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "dayOfWeek": t.string().optional(),
            "timeZone": t.proxy(renames["GooglePrivacyDlpV2TimeZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DateTimeOut"])
    types["GooglePrivacyDlpV2AllInfoTypesIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2AllInfoTypesIn"])
    types["GooglePrivacyDlpV2AllInfoTypesOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2AllInfoTypesOut"])
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
    types["GooglePrivacyDlpV2LargeCustomDictionaryStatsIn"] = t.struct(
        {"approxNumPhrases": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryStatsIn"])
    types["GooglePrivacyDlpV2LargeCustomDictionaryStatsOut"] = t.struct(
        {
            "approxNumPhrases": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LargeCustomDictionaryStatsOut"])
    types["GooglePrivacyDlpV2PublishToStackdriverIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishToStackdriverIn"])
    types["GooglePrivacyDlpV2PublishToStackdriverOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2PublishToStackdriverOut"])
    types["GooglePrivacyDlpV2RecordTransformationsIn"] = t.struct(
        {
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationIn"])
            ).optional(),
            "recordSuppressions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2RecordSuppressionIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationsIn"])
    types["GooglePrivacyDlpV2RecordTransformationsOut"] = t.struct(
        {
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationOut"])
            ).optional(),
            "recordSuppressions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2RecordSuppressionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationsOut"])
    types["GooglePrivacyDlpV2FixedSizeBucketingConfigIn"] = t.struct(
        {
            "lowerBound": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]),
            "upperBound": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]),
            "bucketSize": t.number(),
        }
    ).named(renames["GooglePrivacyDlpV2FixedSizeBucketingConfigIn"])
    types["GooglePrivacyDlpV2FixedSizeBucketingConfigOut"] = t.struct(
        {
            "lowerBound": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]),
            "upperBound": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]),
            "bucketSize": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FixedSizeBucketingConfigOut"])
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
    types["GooglePrivacyDlpV2KindExpressionIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2KindExpressionIn"])
    types["GooglePrivacyDlpV2KindExpressionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KindExpressionOut"])
    types["GooglePrivacyDlpV2ReplaceValueConfigIn"] = t.struct(
        {"newValue": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceValueConfigIn"])
    types["GooglePrivacyDlpV2ReplaceValueConfigOut"] = t.struct(
        {
            "newValue": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ReplaceValueConfigOut"])
    types["GooglePrivacyDlpV2TransformationDetailsIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "transformedBytes": t.string().optional(),
            "statusDetails": t.proxy(
                renames["GooglePrivacyDlpV2TransformationResultStatusIn"]
            ).optional(),
            "transformation": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationDescriptionIn"])
            ).optional(),
            "transformationLocation": t.proxy(
                renames["GooglePrivacyDlpV2TransformationLocationIn"]
            ).optional(),
            "containerName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsIn"])
    types["GooglePrivacyDlpV2TransformationDetailsOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "transformedBytes": t.string().optional(),
            "statusDetails": t.proxy(
                renames["GooglePrivacyDlpV2TransformationResultStatusOut"]
            ).optional(),
            "transformation": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TransformationDescriptionOut"])
            ).optional(),
            "transformationLocation": t.proxy(
                renames["GooglePrivacyDlpV2TransformationLocationOut"]
            ).optional(),
            "containerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationDetailsOut"])
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
    types["GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn"] = t.struct(
        {
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StatisticalTableIn"])
            ).optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2QuasiIdIn"])),
            "regionCode": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut"] = t.struct(
        {
            "auxiliaryTables": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StatisticalTableOut"])
            ).optional(),
            "quasiIds": t.array(t.proxy(renames["GooglePrivacyDlpV2QuasiIdOut"])),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut"])
    types["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn"] = t.struct(
        {
            "estimatedAnonymity": t.string().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn"])
    types["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut"] = t.struct(
        {
            "estimatedAnonymity": t.string().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut"])
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
    types["GooglePrivacyDlpV2PubSubNotificationIn"] = t.struct(
        {
            "pubsubCondition": t.proxy(
                renames["GooglePrivacyDlpV2DataProfilePubSubConditionIn"]
            ).optional(),
            "detailOfMessage": t.string().optional(),
            "topic": t.string().optional(),
            "event": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubNotificationIn"])
    types["GooglePrivacyDlpV2PubSubNotificationOut"] = t.struct(
        {
            "pubsubCondition": t.proxy(
                renames["GooglePrivacyDlpV2DataProfilePubSubConditionOut"]
            ).optional(),
            "detailOfMessage": t.string().optional(),
            "topic": t.string().optional(),
            "event": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubNotificationOut"])
    types["GooglePrivacyDlpV2BoundingBoxIn"] = t.struct(
        {
            "left": t.integer().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "top": t.integer().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BoundingBoxIn"])
    types["GooglePrivacyDlpV2BoundingBoxOut"] = t.struct(
        {
            "left": t.integer().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "top": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BoundingBoxOut"])
    types["GooglePrivacyDlpV2DeidentifyContentResponseIn"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
            "overview": t.proxy(
                renames["GooglePrivacyDlpV2TransformationOverviewIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentResponseIn"])
    types["GooglePrivacyDlpV2DeidentifyContentResponseOut"] = t.struct(
        {
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "overview": t.proxy(
                renames["GooglePrivacyDlpV2TransformationOverviewOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"])
    types["GooglePrivacyDlpV2ManualIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GooglePrivacyDlpV2ManualIn"]
    )
    types["GooglePrivacyDlpV2ManualOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ManualOut"])
    types["GooglePrivacyDlpV2QuasiIdFieldIn"] = t.struct(
        {
            "customTag": t.string().optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdFieldIn"])
    types["GooglePrivacyDlpV2QuasiIdFieldOut"] = t.struct(
        {
            "customTag": t.string().optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2QuasiIdFieldOut"])
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
    types["GooglePrivacyDlpV2OtherInfoTypeSummaryIn"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "estimatedPrevalence": t.integer().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryIn"])
    types["GooglePrivacyDlpV2OtherInfoTypeSummaryOut"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "estimatedPrevalence": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2OtherInfoTypeSummaryOut"])
    types["GooglePrivacyDlpV2CancelDlpJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2CancelDlpJobRequestIn"])
    types["GooglePrivacyDlpV2CancelDlpJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2CancelDlpJobRequestOut"])
    types["GooglePrivacyDlpV2InspectJobConfigIn"] = t.struct(
        {
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "storageConfig": t.proxy(
                renames["GooglePrivacyDlpV2StorageConfigIn"]
            ).optional(),
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectJobConfigIn"])
    types["GooglePrivacyDlpV2InspectJobConfigOut"] = t.struct(
        {
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "inspectTemplateName": t.string().optional(),
            "storageConfig": t.proxy(
                renames["GooglePrivacyDlpV2StorageConfigOut"]
            ).optional(),
            "actions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ActionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectJobConfigOut"])
    types["GooglePrivacyDlpV2LDiversityEquivalenceClassIn"] = t.struct(
        {
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
            "topSensitiveValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyIn"])
            ).optional(),
            "equivalenceClassSize": t.string().optional(),
            "numDistinctSensitiveValues": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassIn"])
    types["GooglePrivacyDlpV2LDiversityEquivalenceClassOut"] = t.struct(
        {
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "topSensitiveValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyOut"])
            ).optional(),
            "equivalenceClassSize": t.string().optional(),
            "numDistinctSensitiveValues": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2LDiversityEquivalenceClassOut"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceStatsIn"] = t.struct(
        {
            "transformationCount": t.string().optional(),
            "transformationErrorCount": t.string().optional(),
            "transformedBytes": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsIn"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceStatsOut"] = t.struct(
        {
            "transformationCount": t.string().optional(),
            "transformationErrorCount": t.string().optional(),
            "transformedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsOut"])
    types["GoogleTypeTimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["GoogleTypeTimeOfDayIn"])
    types["GoogleTypeTimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeTimeOfDayOut"])
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
    types["GooglePrivacyDlpV2NumericalStatsConfigIn"] = t.struct(
        {"field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2NumericalStatsConfigIn"])
    types["GooglePrivacyDlpV2NumericalStatsConfigOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2NumericalStatsConfigOut"])
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
    types["GooglePrivacyDlpV2HybridFindingDetailsIn"] = t.struct(
        {
            "rowOffset": t.string().optional(),
            "fileOffset": t.string().optional(),
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "containerDetails": t.proxy(
                renames["GooglePrivacyDlpV2ContainerIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridFindingDetailsIn"])
    types["GooglePrivacyDlpV2HybridFindingDetailsOut"] = t.struct(
        {
            "rowOffset": t.string().optional(),
            "fileOffset": t.string().optional(),
            "tableOptions": t.proxy(
                renames["GooglePrivacyDlpV2TableOptionsOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "containerDetails": t.proxy(
                renames["GooglePrivacyDlpV2ContainerOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2HybridFindingDetailsOut"])
    types["GooglePrivacyDlpV2ErrorIn"] = t.struct(
        {
            "details": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "timestamps": t.array(t.string()).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ErrorIn"])
    types["GooglePrivacyDlpV2ErrorOut"] = t.struct(
        {
            "details": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "timestamps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ErrorOut"])
    types["GooglePrivacyDlpV2InspectConfigIn"] = t.struct(
        {
            "minLikelihood": t.string().optional(),
            "excludeInfoTypes": t.boolean().optional(),
            "contentOptions": t.array(t.string()).optional(),
            "includeQuote": t.boolean().optional(),
            "ruleSet": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleSetIn"])
            ).optional(),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"])
            ).optional(),
            "limits": t.proxy(renames["GooglePrivacyDlpV2FindingLimitsIn"]).optional(),
            "customInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CustomInfoTypeIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectConfigIn"])
    types["GooglePrivacyDlpV2InspectConfigOut"] = t.struct(
        {
            "minLikelihood": t.string().optional(),
            "excludeInfoTypes": t.boolean().optional(),
            "contentOptions": t.array(t.string()).optional(),
            "includeQuote": t.boolean().optional(),
            "ruleSet": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectionRuleSetOut"])
            ).optional(),
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])
            ).optional(),
            "limits": t.proxy(renames["GooglePrivacyDlpV2FindingLimitsOut"]).optional(),
            "customInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CustomInfoTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectConfigOut"])
    types["GooglePrivacyDlpV2ImageTransformationIn"] = t.struct(
        {
            "allInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2AllInfoTypesIn"]
            ).optional(),
            "allText": t.proxy(renames["GooglePrivacyDlpV2AllTextIn"]).optional(),
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorIn"]).optional(),
            "selectedInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2SelectedInfoTypesIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageTransformationIn"])
    types["GooglePrivacyDlpV2ImageTransformationOut"] = t.struct(
        {
            "allInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2AllInfoTypesOut"]
            ).optional(),
            "allText": t.proxy(renames["GooglePrivacyDlpV2AllTextOut"]).optional(),
            "redactionColor": t.proxy(renames["GooglePrivacyDlpV2ColorOut"]).optional(),
            "selectedInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2SelectedInfoTypesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ImageTransformationOut"])
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
    types["GooglePrivacyDlpV2DataProfileActionIn"] = t.struct(
        {
            "pubSubNotification": t.proxy(
                renames["GooglePrivacyDlpV2PubSubNotificationIn"]
            ).optional(),
            "exportData": t.proxy(renames["GooglePrivacyDlpV2ExportIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileActionIn"])
    types["GooglePrivacyDlpV2DataProfileActionOut"] = t.struct(
        {
            "pubSubNotification": t.proxy(
                renames["GooglePrivacyDlpV2PubSubNotificationOut"]
            ).optional(),
            "exportData": t.proxy(renames["GooglePrivacyDlpV2ExportOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileActionOut"])
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
    types["GooglePrivacyDlpV2CharsToIgnoreIn"] = t.struct(
        {
            "charactersToSkip": t.string().optional(),
            "commonCharactersToIgnore": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharsToIgnoreIn"])
    types["GooglePrivacyDlpV2CharsToIgnoreOut"] = t.struct(
        {
            "charactersToSkip": t.string().optional(),
            "commonCharactersToIgnore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharsToIgnoreOut"])
    types["GooglePrivacyDlpV2ActionIn"] = t.struct(
        {
            "saveFindings": t.proxy(
                renames["GooglePrivacyDlpV2SaveFindingsIn"]
            ).optional(),
            "publishFindingsToCloudDataCatalog": t.proxy(
                renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn"]
            ).optional(),
            "publishSummaryToCscc": t.proxy(
                renames["GooglePrivacyDlpV2PublishSummaryToCsccIn"]
            ).optional(),
            "publishToStackdriver": t.proxy(
                renames["GooglePrivacyDlpV2PublishToStackdriverIn"]
            ).optional(),
            "jobNotificationEmails": t.proxy(
                renames["GooglePrivacyDlpV2JobNotificationEmailsIn"]
            ).optional(),
            "deidentify": t.proxy(renames["GooglePrivacyDlpV2DeidentifyIn"]).optional(),
            "pubSub": t.proxy(
                renames["GooglePrivacyDlpV2PublishToPubSubIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ActionIn"])
    types["GooglePrivacyDlpV2ActionOut"] = t.struct(
        {
            "saveFindings": t.proxy(
                renames["GooglePrivacyDlpV2SaveFindingsOut"]
            ).optional(),
            "publishFindingsToCloudDataCatalog": t.proxy(
                renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut"]
            ).optional(),
            "publishSummaryToCscc": t.proxy(
                renames["GooglePrivacyDlpV2PublishSummaryToCsccOut"]
            ).optional(),
            "publishToStackdriver": t.proxy(
                renames["GooglePrivacyDlpV2PublishToStackdriverOut"]
            ).optional(),
            "jobNotificationEmails": t.proxy(
                renames["GooglePrivacyDlpV2JobNotificationEmailsOut"]
            ).optional(),
            "deidentify": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyOut"]
            ).optional(),
            "pubSub": t.proxy(
                renames["GooglePrivacyDlpV2PublishToPubSubOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ActionOut"])
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
    types["GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn"] = t.struct(
        {
            "bucketSize": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "valueFrequencyUpperBound": t.string().optional(),
            "valueFrequencyLowerBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsHistogramBucketIn"])
    types["GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut"] = t.struct(
        {
            "bucketSize": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "valueFrequencyUpperBound": t.string().optional(),
            "valueFrequencyLowerBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueFrequencyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CategoricalStatsHistogramBucketOut"])
    types["GooglePrivacyDlpV2InfoTypeTransformationIn"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"])
            ).optional(),
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationIn"]
            ),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeTransformationIn"])
    types["GooglePrivacyDlpV2InfoTypeTransformationOut"] = t.struct(
        {
            "infoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"])
            ).optional(),
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeTransformationOut"])
    types["GooglePrivacyDlpV2StatisticalTableIn"] = t.struct(
        {
            "relativeFrequency": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2QuasiIdentifierFieldIn"])
            ),
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2StatisticalTableIn"])
    types["GooglePrivacyDlpV2StatisticalTableOut"] = t.struct(
        {
            "relativeFrequency": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]),
            "quasiIds": t.array(
                t.proxy(renames["GooglePrivacyDlpV2QuasiIdentifierFieldOut"])
            ),
            "table": t.proxy(renames["GooglePrivacyDlpV2BigQueryTableOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StatisticalTableOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GooglePrivacyDlpV2TimePartConfigIn"] = t.struct(
        {"partToExtract": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2TimePartConfigIn"])
    types["GooglePrivacyDlpV2TimePartConfigOut"] = t.struct(
        {
            "partToExtract": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimePartConfigOut"])
    types["GooglePrivacyDlpV2JobTriggerIn"] = t.struct(
        {
            "triggers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TriggerIn"])
            ).optional(),
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "status": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2JobTriggerIn"])
    types["GooglePrivacyDlpV2JobTriggerOut"] = t.struct(
        {
            "triggers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2TriggerOut"])
            ).optional(),
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigOut"]
            ).optional(),
            "name": t.string().optional(),
            "lastRunTime": t.string().optional(),
            "errors": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ErrorOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "status": t.string(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2JobTriggerOut"])
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
    types["GooglePrivacyDlpV2FindingIn"] = t.struct(
        {
            "jobName": t.string().optional(),
            "quoteInfo": t.proxy(renames["GooglePrivacyDlpV2QuoteInfoIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "location": t.proxy(renames["GooglePrivacyDlpV2LocationIn"]).optional(),
            "createTime": t.string().optional(),
            "quote": t.string().optional(),
            "triggerName": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "findingId": t.string().optional(),
            "likelihood": t.string().optional(),
            "jobCreateTime": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingIn"])
    types["GooglePrivacyDlpV2FindingOut"] = t.struct(
        {
            "jobName": t.string().optional(),
            "quoteInfo": t.proxy(renames["GooglePrivacyDlpV2QuoteInfoOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "location": t.proxy(renames["GooglePrivacyDlpV2LocationOut"]).optional(),
            "createTime": t.string().optional(),
            "quote": t.string().optional(),
            "triggerName": t.string().optional(),
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "findingId": t.string().optional(),
            "likelihood": t.string().optional(),
            "jobCreateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingOut"])
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
    types["GooglePrivacyDlpV2ExpressionsIn"] = t.struct(
        {
            "logicalOperator": t.string().optional(),
            "conditions": t.proxy(renames["GooglePrivacyDlpV2ConditionsIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExpressionsIn"])
    types["GooglePrivacyDlpV2ExpressionsOut"] = t.struct(
        {
            "logicalOperator": t.string().optional(),
            "conditions": t.proxy(
                renames["GooglePrivacyDlpV2ConditionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExpressionsOut"])
    types["GooglePrivacyDlpV2ListInspectTemplatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inspectTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectTemplateIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseIn"])
    types["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inspectTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListInspectTemplatesResponseOut"])
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
    types["GooglePrivacyDlpV2WordListIn"] = t.struct(
        {"words": t.array(t.string()).optional()}
    ).named(renames["GooglePrivacyDlpV2WordListIn"])
    types["GooglePrivacyDlpV2WordListOut"] = t.struct(
        {
            "words": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2WordListOut"])
    types["GooglePrivacyDlpV2PrivacyMetricIn"] = t.struct(
        {
            "deltaPresenceEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigIn"]
            ).optional(),
            "lDiversityConfig": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityConfigIn"]
            ).optional(),
            "kAnonymityConfig": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityConfigIn"]
            ).optional(),
            "categoricalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsConfigIn"]
            ).optional(),
            "kMapEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationConfigIn"]
            ).optional(),
            "numericalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrivacyMetricIn"])
    types["GooglePrivacyDlpV2PrivacyMetricOut"] = t.struct(
        {
            "deltaPresenceEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeltaPresenceEstimationConfigOut"]
            ).optional(),
            "lDiversityConfig": t.proxy(
                renames["GooglePrivacyDlpV2LDiversityConfigOut"]
            ).optional(),
            "kAnonymityConfig": t.proxy(
                renames["GooglePrivacyDlpV2KAnonymityConfigOut"]
            ).optional(),
            "categoricalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2CategoricalStatsConfigOut"]
            ).optional(),
            "kMapEstimationConfig": t.proxy(
                renames["GooglePrivacyDlpV2KMapEstimationConfigOut"]
            ).optional(),
            "numericalStatsConfig": t.proxy(
                renames["GooglePrivacyDlpV2NumericalStatsConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PrivacyMetricOut"])
    types["GooglePrivacyDlpV2FieldTransformationIn"] = t.struct(
        {
            "condition": t.proxy(
                renames["GooglePrivacyDlpV2RecordConditionIn"]
            ).optional(),
            "infoTypeTransformations": t.proxy(
                renames["GooglePrivacyDlpV2InfoTypeTransformationsIn"]
            ).optional(),
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationIn"]
            ).optional(),
            "fields": t.array(t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])),
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
            "primitiveTransformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationOut"]
            ).optional(),
            "fields": t.array(t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FieldTransformationOut"])
    types["GooglePrivacyDlpV2ExclusionRuleIn"] = t.struct(
        {
            "dictionary": t.proxy(renames["GooglePrivacyDlpV2DictionaryIn"]).optional(),
            "matchingType": t.string().optional(),
            "excludeInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeInfoTypesIn"]
            ).optional(),
            "excludeByHotword": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeByHotwordIn"]
            ).optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExclusionRuleIn"])
    types["GooglePrivacyDlpV2ExclusionRuleOut"] = t.struct(
        {
            "dictionary": t.proxy(
                renames["GooglePrivacyDlpV2DictionaryOut"]
            ).optional(),
            "matchingType": t.string().optional(),
            "excludeInfoTypes": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeInfoTypesOut"]
            ).optional(),
            "excludeByHotword": t.proxy(
                renames["GooglePrivacyDlpV2ExcludeByHotwordOut"]
            ).optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ExclusionRuleOut"])
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
    types["GooglePrivacyDlpV2TimespanConfigIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "enableAutoPopulationOfTimespanConfig": t.boolean().optional(),
            "timestampField": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdIn"]
            ).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimespanConfigIn"])
    types["GooglePrivacyDlpV2TimespanConfigOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "enableAutoPopulationOfTimespanConfig": t.boolean().optional(),
            "timestampField": t.proxy(
                renames["GooglePrivacyDlpV2FieldIdOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TimespanConfigOut"])
    types["GooglePrivacyDlpV2RecordTransformationIn"] = t.struct(
        {
            "containerVersion": t.string().optional(),
            "containerTimestamp": t.string().optional(),
            "fieldId": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationIn"])
    types["GooglePrivacyDlpV2RecordTransformationOut"] = t.struct(
        {
            "containerVersion": t.string().optional(),
            "containerTimestamp": t.string().optional(),
            "fieldId": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordTransformationOut"])
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
    types["GooglePrivacyDlpV2EntityIdIn"] = t.struct(
        {"field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2EntityIdIn"])
    types["GooglePrivacyDlpV2EntityIdOut"] = t.struct(
        {
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2EntityIdOut"])
    types["GooglePrivacyDlpV2CloudStorageFileSetIn"] = t.struct(
        {"url": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2CloudStorageFileSetIn"])
    types["GooglePrivacyDlpV2CloudStorageFileSetOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageFileSetOut"])
    types["GooglePrivacyDlpV2JobNotificationEmailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2JobNotificationEmailsIn"])
    types["GooglePrivacyDlpV2JobNotificationEmailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2JobNotificationEmailsOut"])
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
    types["GooglePrivacyDlpV2RecordKeyIn"] = t.struct(
        {
            "idValues": t.array(t.string()).optional(),
            "datastoreKey": t.proxy(renames["GooglePrivacyDlpV2DatastoreKeyIn"]),
            "bigQueryKey": t.proxy(renames["GooglePrivacyDlpV2BigQueryKeyIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2RecordKeyIn"])
    types["GooglePrivacyDlpV2RecordKeyOut"] = t.struct(
        {
            "idValues": t.array(t.string()).optional(),
            "datastoreKey": t.proxy(renames["GooglePrivacyDlpV2DatastoreKeyOut"]),
            "bigQueryKey": t.proxy(renames["GooglePrivacyDlpV2BigQueryKeyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RecordKeyOut"])
    types["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn"] = t.struct(
        {
            "deidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
            ),
            "locationId": t.string().optional(),
            "templateId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestIn"])
    types["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut"] = t.struct(
        {
            "deidentifyTemplate": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]
            ),
            "locationId": t.string().optional(),
            "templateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDeidentifyTemplateRequestOut"])
    types["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigIn"])
    types["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ReplaceWithInfoTypeConfigOut"])
    types["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn"] = t.struct(
        {
            "deidentifyTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseIn"])
    types["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"] = t.struct(
        {
            "deidentifyTemplates": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListDeidentifyTemplatesResponseOut"])
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
    types["GooglePrivacyDlpV2PubSubConditionIn"] = t.struct(
        {
            "minimumSensitivityScore": t.string().optional(),
            "minimumRiskScore": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubConditionIn"])
    types["GooglePrivacyDlpV2PubSubConditionOut"] = t.struct(
        {
            "minimumSensitivityScore": t.string().optional(),
            "minimumRiskScore": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PubSubConditionOut"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn"] = t.struct(
        {
            "estimatedProbability": t.number().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesIn"])
    types["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut"] = t.struct(
        {
            "estimatedProbability": t.number().optional(),
            "quasiIdsValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValuesOut"])
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
    types["GooglePrivacyDlpV2RedactImageResponseIn"] = t.struct(
        {
            "inspectResult": t.proxy(
                renames["GooglePrivacyDlpV2InspectResultIn"]
            ).optional(),
            "extractedText": t.string().optional(),
            "redactedImage": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageResponseIn"])
    types["GooglePrivacyDlpV2RedactImageResponseOut"] = t.struct(
        {
            "inspectResult": t.proxy(
                renames["GooglePrivacyDlpV2InspectResultOut"]
            ).optional(),
            "extractedText": t.string().optional(),
            "redactedImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageResponseOut"])
    types["GooglePrivacyDlpV2ListStoredInfoTypesResponseIn"] = t.struct(
        {
            "storedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseIn"])
    types["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"] = t.struct(
        {
            "storedInfoTypes": t.array(
                t.proxy(renames["GooglePrivacyDlpV2StoredInfoTypeOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"])
    types["GooglePrivacyDlpV2RedactConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2RedactConfigIn"])
    types["GooglePrivacyDlpV2RedactConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2RedactConfigOut"])
    types["GooglePrivacyDlpV2DocumentLocationIn"] = t.struct(
        {"fileOffset": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2DocumentLocationIn"])
    types["GooglePrivacyDlpV2DocumentLocationOut"] = t.struct(
        {
            "fileOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DocumentLocationOut"])
    types["GooglePrivacyDlpV2CharacterMaskConfigIn"] = t.struct(
        {
            "charactersToIgnore": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CharsToIgnoreIn"])
            ).optional(),
            "reverseOrder": t.boolean().optional(),
            "numberToMask": t.integer().optional(),
            "maskingCharacter": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharacterMaskConfigIn"])
    types["GooglePrivacyDlpV2CharacterMaskConfigOut"] = t.struct(
        {
            "charactersToIgnore": t.array(
                t.proxy(renames["GooglePrivacyDlpV2CharsToIgnoreOut"])
            ).optional(),
            "reverseOrder": t.boolean().optional(),
            "numberToMask": t.integer().optional(),
            "maskingCharacter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CharacterMaskConfigOut"])
    types["GooglePrivacyDlpV2InspectResultIn"] = t.struct(
        {
            "findings": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FindingIn"])
            ).optional(),
            "findingsTruncated": t.boolean().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectResultIn"])
    types["GooglePrivacyDlpV2InspectResultOut"] = t.struct(
        {
            "findings": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FindingOut"])
            ).optional(),
            "findingsTruncated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InspectResultOut"])
    types["GooglePrivacyDlpV2SurrogateTypeIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2SurrogateTypeIn"])
    types["GooglePrivacyDlpV2SurrogateTypeOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2SurrogateTypeOut"])
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
    types["GooglePrivacyDlpV2CloudStorageRegexFileSetIn"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "excludeRegex": t.array(t.string()).optional(),
            "includeRegex": t.array(t.string()).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageRegexFileSetIn"])
    types["GooglePrivacyDlpV2CloudStorageRegexFileSetOut"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "excludeRegex": t.array(t.string()).optional(),
            "includeRegex": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageRegexFileSetOut"])
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
    types["GooglePrivacyDlpV2ActivateJobTriggerRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ActivateJobTriggerRequestIn"])
    types["GooglePrivacyDlpV2ActivateJobTriggerRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2ActivateJobTriggerRequestOut"])
    types["GooglePrivacyDlpV2HybridInspectResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2HybridInspectResponseIn"])
    types["GooglePrivacyDlpV2HybridInspectResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2HybridInspectResponseOut"])
    types["GooglePrivacyDlpV2CreateDlpJobRequestIn"] = t.struct(
        {
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigIn"]
            ).optional(),
            "jobId": t.string().optional(),
            "locationId": t.string().optional(),
            "riskJob": t.proxy(
                renames["GooglePrivacyDlpV2RiskAnalysisJobConfigIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDlpJobRequestIn"])
    types["GooglePrivacyDlpV2CreateDlpJobRequestOut"] = t.struct(
        {
            "inspectJob": t.proxy(
                renames["GooglePrivacyDlpV2InspectJobConfigOut"]
            ).optional(),
            "jobId": t.string().optional(),
            "locationId": t.string().optional(),
            "riskJob": t.proxy(
                renames["GooglePrivacyDlpV2RiskAnalysisJobConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateDlpJobRequestOut"])
    types["GooglePrivacyDlpV2DataRiskLevelIn"] = t.struct(
        {"score": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2DataRiskLevelIn"])
    types["GooglePrivacyDlpV2DataRiskLevelOut"] = t.struct(
        {
            "score": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataRiskLevelOut"])
    types["GooglePrivacyDlpV2KMapEstimationHistogramBucketIn"] = t.struct(
        {
            "maxAnonymity": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "bucketSize": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesIn"])
            ).optional(),
            "minAnonymity": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationHistogramBucketIn"])
    types["GooglePrivacyDlpV2KMapEstimationHistogramBucketOut"] = t.struct(
        {
            "maxAnonymity": t.string().optional(),
            "bucketValueCount": t.string().optional(),
            "bucketSize": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KMapEstimationQuasiIdValuesOut"])
            ).optional(),
            "minAnonymity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KMapEstimationHistogramBucketOut"])
    types["GooglePrivacyDlpV2KAnonymityHistogramBucketIn"] = t.struct(
        {
            "equivalenceClassSizeLowerBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KAnonymityEquivalenceClassIn"])
            ).optional(),
            "bucketValueCount": t.string().optional(),
            "equivalenceClassSizeUpperBound": t.string().optional(),
            "bucketSize": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityHistogramBucketIn"])
    types["GooglePrivacyDlpV2KAnonymityHistogramBucketOut"] = t.struct(
        {
            "equivalenceClassSizeLowerBound": t.string().optional(),
            "bucketValues": t.array(
                t.proxy(renames["GooglePrivacyDlpV2KAnonymityEquivalenceClassOut"])
            ).optional(),
            "bucketValueCount": t.string().optional(),
            "equivalenceClassSizeUpperBound": t.string().optional(),
            "bucketSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KAnonymityHistogramBucketOut"])
    types["GooglePrivacyDlpV2ResultIn"] = t.struct(
        {
            "totalEstimatedBytes": t.string().optional(),
            "hybridStats": t.proxy(
                renames["GooglePrivacyDlpV2HybridInspectStatisticsIn"]
            ).optional(),
            "infoTypeStats": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeStatsIn"])
            ).optional(),
            "processedBytes": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ResultIn"])
    types["GooglePrivacyDlpV2ResultOut"] = t.struct(
        {
            "totalEstimatedBytes": t.string().optional(),
            "hybridStats": t.proxy(
                renames["GooglePrivacyDlpV2HybridInspectStatisticsOut"]
            ).optional(),
            "infoTypeStats": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeStatsOut"])
            ).optional(),
            "processedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ResultOut"])
    types["GooglePrivacyDlpV2RedactImageRequestIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "includeFindings": t.boolean().optional(),
            "imageRedactionConfigs": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
            ).optional(),
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageRequestIn"])
    types["GooglePrivacyDlpV2RedactImageRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "includeFindings": t.boolean().optional(),
            "imageRedactionConfigs": t.array(
                t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigOut"])
            ).optional(),
            "byteItem": t.proxy(
                renames["GooglePrivacyDlpV2ByteContentItemOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2RedactImageRequestOut"])
    types["GooglePrivacyDlpV2BucketIn"] = t.struct(
        {
            "min": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
            "max": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]).optional(),
            "replacementValue": t.proxy(renames["GooglePrivacyDlpV2ValueIn"]),
        }
    ).named(renames["GooglePrivacyDlpV2BucketIn"])
    types["GooglePrivacyDlpV2BucketOut"] = t.struct(
        {
            "min": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "max": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]).optional(),
            "replacementValue": t.proxy(renames["GooglePrivacyDlpV2ValueOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2BucketOut"])
    types["GooglePrivacyDlpV2InfoTypeDescriptionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2VersionDescriptionIn"])
            ).optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreIn"]
            ).optional(),
            "categories": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeCategoryIn"])
            ).optional(),
            "supportedBy": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeDescriptionIn"])
    types["GooglePrivacyDlpV2InfoTypeDescriptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "versions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2VersionDescriptionOut"])
            ).optional(),
            "sensitivityScore": t.proxy(
                renames["GooglePrivacyDlpV2SensitivityScoreOut"]
            ).optional(),
            "categories": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeCategoryOut"])
            ).optional(),
            "supportedBy": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2InfoTypeDescriptionOut"])
    types["GooglePrivacyDlpV2PathElementIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PathElementIn"])
    types["GooglePrivacyDlpV2PathElementOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PathElementOut"])
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
    types["GooglePrivacyDlpV2ContainerIn"] = t.struct(
        {
            "version": t.string().optional(),
            "rootPath": t.string().optional(),
            "updateTime": t.string().optional(),
            "projectId": t.string().optional(),
            "fullPath": t.string().optional(),
            "type": t.string().optional(),
            "relativePath": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContainerIn"])
    types["GooglePrivacyDlpV2ContainerOut"] = t.struct(
        {
            "version": t.string().optional(),
            "rootPath": t.string().optional(),
            "updateTime": t.string().optional(),
            "projectId": t.string().optional(),
            "fullPath": t.string().optional(),
            "type": t.string().optional(),
            "relativePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ContainerOut"])
    types["GooglePrivacyDlpV2CloudStorageOptionsIn"] = t.struct(
        {
            "filesLimitPercent": t.integer().optional(),
            "fileTypes": t.array(t.string()).optional(),
            "sampleMethod": t.string(),
            "bytesLimitPerFile": t.string().optional(),
            "bytesLimitPerFilePercent": t.integer().optional(),
            "fileSet": t.proxy(renames["GooglePrivacyDlpV2FileSetIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageOptionsIn"])
    types["GooglePrivacyDlpV2CloudStorageOptionsOut"] = t.struct(
        {
            "filesLimitPercent": t.integer().optional(),
            "fileTypes": t.array(t.string()).optional(),
            "sampleMethod": t.string(),
            "bytesLimitPerFile": t.string().optional(),
            "bytesLimitPerFilePercent": t.integer().optional(),
            "fileSet": t.proxy(renames["GooglePrivacyDlpV2FileSetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CloudStorageOptionsOut"])
    types["GooglePrivacyDlpV2DatastoreKeyIn"] = t.struct(
        {"entityKey": t.proxy(renames["GooglePrivacyDlpV2KeyIn"]).optional()}
    ).named(renames["GooglePrivacyDlpV2DatastoreKeyIn"])
    types["GooglePrivacyDlpV2DatastoreKeyOut"] = t.struct(
        {
            "entityKey": t.proxy(renames["GooglePrivacyDlpV2KeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DatastoreKeyOut"])
    types["GooglePrivacyDlpV2StoredInfoTypeConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "dictionary": t.proxy(renames["GooglePrivacyDlpV2DictionaryIn"]).optional(),
            "largeCustomDictionary": t.proxy(
                renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"])
    types["GooglePrivacyDlpV2StoredInfoTypeConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "dictionary": t.proxy(
                renames["GooglePrivacyDlpV2DictionaryOut"]
            ).optional(),
            "largeCustomDictionary": t.proxy(
                renames["GooglePrivacyDlpV2LargeCustomDictionaryConfigOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "regex": t.proxy(renames["GooglePrivacyDlpV2RegexOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeConfigOut"])
    types["GooglePrivacyDlpV2ByteContentItemIn"] = t.struct(
        {"type": t.string().optional(), "data": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ByteContentItemIn"])
    types["GooglePrivacyDlpV2ByteContentItemOut"] = t.struct(
        {
            "type": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ByteContentItemOut"])
    types["GooglePrivacyDlpV2PublishToPubSubIn"] = t.struct(
        {"topic": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishToPubSubIn"])
    types["GooglePrivacyDlpV2PublishToPubSubOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2PublishToPubSubOut"])
    types["GooglePrivacyDlpV2StoredInfoTypeVersionIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "errors": t.array(t.proxy(renames["GooglePrivacyDlpV2ErrorIn"])).optional(),
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]
            ).optional(),
            "state": t.string().optional(),
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
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "stats": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2StoredInfoTypeVersionOut"])
    types["GooglePrivacyDlpV2ValueIn"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "timeValue": t.proxy(renames["GoogleTypeTimeOfDayIn"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "floatValue": t.number().optional(),
            "dayOfWeekValue": t.string().optional(),
            "timestampValue": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ValueIn"])
    types["GooglePrivacyDlpV2ValueOut"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "integerValue": t.string().optional(),
            "timeValue": t.proxy(renames["GoogleTypeTimeOfDayOut"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "floatValue": t.number().optional(),
            "dayOfWeekValue": t.string().optional(),
            "timestampValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ValueOut"])
    types["GooglePrivacyDlpV2CreateJobTriggerRequestIn"] = t.struct(
        {
            "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerIn"]),
            "triggerId": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateJobTriggerRequestIn"])
    types["GooglePrivacyDlpV2CreateJobTriggerRequestOut"] = t.struct(
        {
            "jobTrigger": t.proxy(renames["GooglePrivacyDlpV2JobTriggerOut"]),
            "triggerId": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2CreateJobTriggerRequestOut"])
    types["GooglePrivacyDlpV2FindingLimitsIn"] = t.struct(
        {
            "maxFindingsPerRequest": t.integer().optional(),
            "maxFindingsPerItem": t.integer().optional(),
            "maxFindingsPerInfoType": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeLimitIn"])
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingLimitsIn"])
    types["GooglePrivacyDlpV2FindingLimitsOut"] = t.struct(
        {
            "maxFindingsPerRequest": t.integer().optional(),
            "maxFindingsPerItem": t.integer().optional(),
            "maxFindingsPerInfoType": t.array(
                t.proxy(renames["GooglePrivacyDlpV2InfoTypeLimitOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2FindingLimitsOut"])
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
    types["GooglePrivacyDlpV2SensitivityScoreIn"] = t.struct(
        {"score": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2SensitivityScoreIn"])
    types["GooglePrivacyDlpV2SensitivityScoreOut"] = t.struct(
        {
            "score": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SensitivityScoreOut"])
    types["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogIn"])
    types["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2PublishFindingsToCloudDataCatalogOut"])
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
    types["GooglePrivacyDlpV2DataProfileJobConfigIn"] = t.struct(
        {
            "inspectTemplates": t.array(t.string()).optional(),
            "location": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileLocationIn"]
            ).optional(),
            "dataProfileActions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DataProfileActionIn"])
            ).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileJobConfigIn"])
    types["GooglePrivacyDlpV2DataProfileJobConfigOut"] = t.struct(
        {
            "inspectTemplates": t.array(t.string()).optional(),
            "location": t.proxy(
                renames["GooglePrivacyDlpV2DataProfileLocationOut"]
            ).optional(),
            "dataProfileActions": t.array(
                t.proxy(renames["GooglePrivacyDlpV2DataProfileActionOut"])
            ).optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DataProfileJobConfigOut"])
    types["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn"] = t.struct(
        {
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigIn"]
            ).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestIn"])
    types["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut"] = t.struct(
        {
            "config": t.proxy(
                renames["GooglePrivacyDlpV2StoredInfoTypeConfigOut"]
            ).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2UpdateStoredInfoTypeRequestOut"])
    types["GooglePrivacyDlpV2KmsWrappedCryptoKeyIn"] = t.struct(
        {"wrappedKey": t.string(), "cryptoKeyName": t.string()}
    ).named(renames["GooglePrivacyDlpV2KmsWrappedCryptoKeyIn"])
    types["GooglePrivacyDlpV2KmsWrappedCryptoKeyOut"] = t.struct(
        {
            "wrappedKey": t.string(),
            "cryptoKeyName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2KmsWrappedCryptoKeyOut"])
    types["GooglePrivacyDlpV2SummaryResultIn"] = t.struct(
        {
            "code": t.string().optional(),
            "details": t.string().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SummaryResultIn"])
    types["GooglePrivacyDlpV2SummaryResultOut"] = t.struct(
        {
            "code": t.string().optional(),
            "details": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2SummaryResultOut"])
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
    types["GooglePrivacyDlpV2TransformationSummaryIn"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeIn"]).optional(),
            "transformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationIn"]
            ).optional(),
            "recordSuppress": t.proxy(
                renames["GooglePrivacyDlpV2RecordSuppressionIn"]
            ).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"]).optional(),
            "results": t.array(
                t.proxy(renames["GooglePrivacyDlpV2SummaryResultIn"])
            ).optional(),
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationIn"])
            ).optional(),
            "transformedBytes": t.string().optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationSummaryIn"])
    types["GooglePrivacyDlpV2TransformationSummaryOut"] = t.struct(
        {
            "infoType": t.proxy(renames["GooglePrivacyDlpV2InfoTypeOut"]).optional(),
            "transformation": t.proxy(
                renames["GooglePrivacyDlpV2PrimitiveTransformationOut"]
            ).optional(),
            "recordSuppress": t.proxy(
                renames["GooglePrivacyDlpV2RecordSuppressionOut"]
            ).optional(),
            "field": t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"]).optional(),
            "results": t.array(
                t.proxy(renames["GooglePrivacyDlpV2SummaryResultOut"])
            ).optional(),
            "fieldTransformations": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldTransformationOut"])
            ).optional(),
            "transformedBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TransformationSummaryOut"])
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
    types["GooglePrivacyDlpV2ScheduleIn"] = t.struct(
        {"recurrencePeriodDuration": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2ScheduleIn"])
    types["GooglePrivacyDlpV2ScheduleOut"] = t.struct(
        {
            "recurrencePeriodDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2ScheduleOut"])
    types["GooglePrivacyDlpV2TableIn"] = t.struct(
        {
            "headers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdIn"])
            ).optional(),
            "rows": t.array(t.proxy(renames["GooglePrivacyDlpV2RowIn"])).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableIn"])
    types["GooglePrivacyDlpV2TableOut"] = t.struct(
        {
            "headers": t.array(
                t.proxy(renames["GooglePrivacyDlpV2FieldIdOut"])
            ).optional(),
            "rows": t.array(t.proxy(renames["GooglePrivacyDlpV2RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2TableOut"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn"] = t.struct(
        {
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedDeidentifyOptionsIn"]
            ).optional(),
            "deidentifyStats": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsIn"]
            ).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceDetailsIn"])
    types["GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut"] = t.struct(
        {
            "requestedOptions": t.proxy(
                renames["GooglePrivacyDlpV2RequestedDeidentifyOptionsOut"]
            ).optional(),
            "deidentifyStats": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyDataSourceStatsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyDataSourceDetailsOut"])
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
    types["GooglePrivacyDlpV2FinishDlpJobRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GooglePrivacyDlpV2FinishDlpJobRequestIn"])
    types["GooglePrivacyDlpV2FinishDlpJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GooglePrivacyDlpV2FinishDlpJobRequestOut"])
    types["GooglePrivacyDlpV2DeidentifyContentRequestIn"] = t.struct(
        {
            "inspectTemplateName": t.string().optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
            ).optional(),
            "deidentifyTemplateName": t.string().optional(),
            "locationId": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigIn"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentRequestIn"])
    types["GooglePrivacyDlpV2DeidentifyContentRequestOut"] = t.struct(
        {
            "inspectTemplateName": t.string().optional(),
            "deidentifyConfig": t.proxy(
                renames["GooglePrivacyDlpV2DeidentifyConfigOut"]
            ).optional(),
            "deidentifyTemplateName": t.string().optional(),
            "locationId": t.string().optional(),
            "inspectConfig": t.proxy(
                renames["GooglePrivacyDlpV2InspectConfigOut"]
            ).optional(),
            "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePrivacyDlpV2DeidentifyContentRequestOut"])
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

    functions = {}
    functions["locationsInfoTypesList"] = dlp.get(
        "v2/{parent}/infoTypes",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "parent": t.string().optional(),
                "filter": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersPatch"] = dlp.get(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "type": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListJobTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersGet"] = dlp.get(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "type": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListJobTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersDelete"] = dlp.get(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "type": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListJobTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersCreate"] = dlp.get(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "type": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListJobTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsJobTriggersList"] = dlp.get(
        "v2/{parent}/jobTriggers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "type": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListJobTriggersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDlpJobsList"] = dlp.get(
        "v2/{parent}/dlpJobs",
        t.struct(
            {
                "type": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "locationId": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListDlpJobsResponseOut"]),
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
    functions["organizationsLocationsDeidentifyTemplatesDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesPatch"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsDeidentifyTemplatesGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesPatch"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesCreate"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesList"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesGet"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInspectTemplatesDelete"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsInspectTemplatesList"] = dlp.post(
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
    functions["organizationsInspectTemplatesDelete"] = dlp.post(
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
    functions["organizationsInspectTemplatesPatch"] = dlp.post(
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
    functions["organizationsInspectTemplatesGet"] = dlp.post(
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
    functions["organizationsInspectTemplatesCreate"] = dlp.post(
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
    functions["organizationsStoredInfoTypesDelete"] = dlp.get(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesCreate"] = dlp.get(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesPatch"] = dlp.get(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesGet"] = dlp.get(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsStoredInfoTypesList"] = dlp.get(
        "v2/{parent}/storedInfoTypes",
        t.struct(
            {
                "parent": t.string(),
                "locationId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListStoredInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesPatch"] = dlp.post(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "templateId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesList"] = dlp.post(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "templateId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesGet"] = dlp.post(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "templateId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesDelete"] = dlp.post(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "templateId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsDeidentifyTemplatesCreate"] = dlp.post(
        "v2/{parent}/deidentifyTemplates",
        t.struct(
            {
                "parent": t.string(),
                "deidentifyTemplate": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyTemplateIn"]
                ),
                "locationId": t.string().optional(),
                "templateId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeidentifyTemplatesList"] = dlp.patch(
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
    functions["projectsDeidentifyTemplatesGet"] = dlp.patch(
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
    functions["projectsDeidentifyTemplatesCreate"] = dlp.patch(
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
    functions["projectsDeidentifyTemplatesDelete"] = dlp.patch(
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
    functions["projectsDeidentifyTemplatesPatch"] = dlp.patch(
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
    functions["projectsLocationsImageRedact"] = dlp.post(
        "v2/{parent}/image:redact",
        t.struct(
            {
                "parent": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "includeFindings": t.boolean().optional(),
                "imageRedactionConfigs": t.array(
                    t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
                ).optional(),
                "byteItem": t.proxy(
                    renames["GooglePrivacyDlpV2ByteContentItemIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2RedactImageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsJobTriggersGet"] = dlp.patch(
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
    functions["projectsLocationsJobTriggersList"] = dlp.patch(
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
    functions["projectsLocationsJobTriggersCreate"] = dlp.patch(
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
    functions["projectsLocationsJobTriggersActivate"] = dlp.patch(
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
    functions["projectsLocationsJobTriggersHybridInspect"] = dlp.patch(
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
    functions["projectsLocationsJobTriggersDelete"] = dlp.patch(
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
    functions["projectsLocationsJobTriggersPatch"] = dlp.patch(
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
    functions["projectsLocationsInspectTemplatesList"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesDelete"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesPatch"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesCreate"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInspectTemplatesGet"] = dlp.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePrivacyDlpV2InspectTemplateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContentInspect"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsContentReidentify"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
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
                "inspectTemplateName": t.string().optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeidentifyTemplatesCreate"] = dlp.patch(
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
    functions["projectsLocationsDeidentifyTemplatesGet"] = dlp.patch(
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
    functions["projectsLocationsDeidentifyTemplatesDelete"] = dlp.patch(
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
    functions["projectsLocationsDeidentifyTemplatesList"] = dlp.patch(
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
    functions["projectsLocationsDeidentifyTemplatesPatch"] = dlp.patch(
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
    functions["projectsLocationsDlpJobsCancel"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsGet"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsList"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsHybridInspect"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsCreate"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsFinish"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDlpJobsDelete"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsStoredInfoTypesPatch"] = dlp.post(
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
    functions["projectsLocationsStoredInfoTypesGet"] = dlp.post(
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
    functions["projectsLocationsStoredInfoTypesList"] = dlp.post(
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
    functions["projectsLocationsStoredInfoTypesDelete"] = dlp.post(
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
    functions["projectsLocationsStoredInfoTypesCreate"] = dlp.post(
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
    functions["projectsImageRedact"] = dlp.post(
        "v2/{parent}/image:redact",
        t.struct(
            {
                "parent": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "includeFindings": t.boolean().optional(),
                "imageRedactionConfigs": t.array(
                    t.proxy(renames["GooglePrivacyDlpV2ImageRedactionConfigIn"])
                ).optional(),
                "byteItem": t.proxy(
                    renames["GooglePrivacyDlpV2ByteContentItemIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2RedactImageResponseOut"]),
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
    functions["projectsStoredInfoTypesCreate"] = dlp.get(
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
    functions["projectsStoredInfoTypesPatch"] = dlp.get(
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
    functions["projectsDlpJobsCancel"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsGet"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsCreate"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsList"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDlpJobsDelete"] = dlp.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsContentInspect"] = dlp.post(
        "v2/{parent}/content:deidentify",
        t.struct(
            {
                "parent": t.string().optional(),
                "inspectTemplateName": t.string().optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
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
                "inspectTemplateName": t.string().optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
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
                "inspectTemplateName": t.string().optional(),
                "deidentifyConfig": t.proxy(
                    renames["GooglePrivacyDlpV2DeidentifyConfigIn"]
                ).optional(),
                "deidentifyTemplateName": t.string().optional(),
                "locationId": t.string().optional(),
                "inspectConfig": t.proxy(
                    renames["GooglePrivacyDlpV2InspectConfigIn"]
                ).optional(),
                "item": t.proxy(renames["GooglePrivacyDlpV2ContentItemIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2DeidentifyContentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsJobTriggersList"] = dlp.patch(
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
    functions["projectsJobTriggersActivate"] = dlp.patch(
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
    functions["projectsJobTriggersCreate"] = dlp.patch(
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
    functions["projectsJobTriggersGet"] = dlp.patch(
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
    functions["projectsJobTriggersDelete"] = dlp.patch(
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
    functions["projectsJobTriggersPatch"] = dlp.patch(
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
    functions["infoTypesList"] = dlp.get(
        "v2/infoTypes",
        t.struct(
            {
                "filter": t.string().optional(),
                "locationId": t.string().optional(),
                "parent": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePrivacyDlpV2ListInfoTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="dlp", renames=renames, types=types, functions=functions)
