from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_documentai() -> Import:
    documentai = HTTPRuntime("https://documentai.googleapis.com/")

    renames = {
        "ErrorResponse": "_documentai_1_ErrorResponse",
        "GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn": "_documentai_2_GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut": "_documentai_3_GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut",
        "GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataIn": "_documentai_4_GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataOut": "_documentai_5_GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentEntityIn": "_documentai_6_GoogleCloudDocumentaiV1beta1DocumentEntityIn",
        "GoogleCloudDocumentaiV1beta1DocumentEntityOut": "_documentai_7_GoogleCloudDocumentaiV1beta1DocumentEntityOut",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataIn": "_documentai_8_GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataOut": "_documentai_9_GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataOut",
        "GoogleProtobufEmptyIn": "_documentai_10_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_documentai_11_GoogleProtobufEmptyOut",
        "GoogleCloudDocumentaiV1EvaluationCountersIn": "_documentai_12_GoogleCloudDocumentaiV1EvaluationCountersIn",
        "GoogleCloudDocumentaiV1EvaluationCountersOut": "_documentai_13_GoogleCloudDocumentaiV1EvaluationCountersOut",
        "GoogleCloudLocationLocationIn": "_documentai_14_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_documentai_15_GoogleCloudLocationLocationOut",
        "GoogleTypeDateIn": "_documentai_16_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_documentai_17_GoogleTypeDateOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn": "_documentai_18_GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut": "_documentai_19_GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataIn": "_documentai_20_GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataOut": "_documentai_21_GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataIn": "_documentai_22_GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataOut": "_documentai_23_GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1GcsDocumentsIn": "_documentai_24_GoogleCloudDocumentaiV1GcsDocumentsIn",
        "GoogleCloudDocumentaiV1GcsDocumentsOut": "_documentai_25_GoogleCloudDocumentaiV1GcsDocumentsOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn": "_documentai_26_GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut": "_documentai_27_GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1beta2DocumentShardInfoIn": "_documentai_28_GoogleCloudDocumentaiV1beta2DocumentShardInfoIn",
        "GoogleCloudDocumentaiV1beta2DocumentShardInfoOut": "_documentai_29_GoogleCloudDocumentaiV1beta2DocumentShardInfoOut",
        "GoogleCloudDocumentaiV1DocumentPageTableIn": "_documentai_30_GoogleCloudDocumentaiV1DocumentPageTableIn",
        "GoogleCloudDocumentaiV1DocumentPageTableOut": "_documentai_31_GoogleCloudDocumentaiV1DocumentPageTableOut",
        "GoogleLongrunningOperationIn": "_documentai_32_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_documentai_33_GoogleLongrunningOperationOut",
        "GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn": "_documentai_34_GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn",
        "GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut": "_documentai_35_GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut",
        "GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataIn": "_documentai_36_GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataOut": "_documentai_37_GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentIn": "_documentai_38_GoogleCloudDocumentaiV1beta2DocumentIn",
        "GoogleCloudDocumentaiV1beta2DocumentOut": "_documentai_39_GoogleCloudDocumentaiV1beta2DocumentOut",
        "GoogleCloudDocumentaiV1beta2ProcessDocumentResponseIn": "_documentai_40_GoogleCloudDocumentaiV1beta2ProcessDocumentResponseIn",
        "GoogleCloudDocumentaiV1beta2ProcessDocumentResponseOut": "_documentai_41_GoogleCloudDocumentaiV1beta2ProcessDocumentResponseOut",
        "GoogleCloudDocumentaiV1beta2OperationMetadataIn": "_documentai_42_GoogleCloudDocumentaiV1beta2OperationMetadataIn",
        "GoogleCloudDocumentaiV1beta2OperationMetadataOut": "_documentai_43_GoogleCloudDocumentaiV1beta2OperationMetadataOut",
        "GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn": "_documentai_44_GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut": "_documentai_45_GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageBlockIn": "_documentai_46_GoogleCloudDocumentaiV1beta1DocumentPageBlockIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageBlockOut": "_documentai_47_GoogleCloudDocumentaiV1beta1DocumentPageBlockOut",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataIn": "_documentai_48_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataOut": "_documentai_49_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableIn": "_documentai_50_GoogleCloudDocumentaiV1beta1DocumentPageTableIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableOut": "_documentai_51_GoogleCloudDocumentaiV1beta1DocumentPageTableOut",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn": "_documentai_52_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut": "_documentai_53_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn": "_documentai_54_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut": "_documentai_55_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataIn": "_documentai_56_GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataOut": "_documentai_57_GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn": "_documentai_58_GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut": "_documentai_59_GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut",
        "GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn": "_documentai_60_GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn",
        "GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut": "_documentai_61_GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut",
        "GoogleCloudDocumentaiV1GcsDocumentIn": "_documentai_62_GoogleCloudDocumentaiV1GcsDocumentIn",
        "GoogleCloudDocumentaiV1GcsDocumentOut": "_documentai_63_GoogleCloudDocumentaiV1GcsDocumentOut",
        "GoogleCloudDocumentaiV1beta1GcsSourceIn": "_documentai_64_GoogleCloudDocumentaiV1beta1GcsSourceIn",
        "GoogleCloudDocumentaiV1beta1GcsSourceOut": "_documentai_65_GoogleCloudDocumentaiV1beta1GcsSourceOut",
        "GoogleCloudDocumentaiV1DocumentPageTableTableRowIn": "_documentai_66_GoogleCloudDocumentaiV1DocumentPageTableTableRowIn",
        "GoogleCloudDocumentaiV1DocumentPageTableTableRowOut": "_documentai_67_GoogleCloudDocumentaiV1DocumentPageTableTableRowOut",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn": "_documentai_68_GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut": "_documentai_69_GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn": "_documentai_70_GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut": "_documentai_71_GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn": "_documentai_72_GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut": "_documentai_73_GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn": "_documentai_74_GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut": "_documentai_75_GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataIn": "_documentai_76_GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataOut": "_documentai_77_GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1EnableProcessorMetadataIn": "_documentai_78_GoogleCloudDocumentaiV1EnableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1EnableProcessorMetadataOut": "_documentai_79_GoogleCloudDocumentaiV1EnableProcessorMetadataOut",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn": "_documentai_80_GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut": "_documentai_81_GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn": "_documentai_82_GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn",
        "GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut": "_documentai_83_GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn": "_documentai_84_GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut": "_documentai_85_GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn": "_documentai_86_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut": "_documentai_87_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut",
        "GoogleCloudDocumentaiV1DocumentProvenanceIn": "_documentai_88_GoogleCloudDocumentaiV1DocumentProvenanceIn",
        "GoogleCloudDocumentaiV1DocumentProvenanceOut": "_documentai_89_GoogleCloudDocumentaiV1DocumentProvenanceOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageIn": "_documentai_90_GoogleCloudDocumentaiV1beta2DocumentPageImageIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageOut": "_documentai_91_GoogleCloudDocumentaiV1beta2DocumentPageImageOut",
        "GoogleCloudDocumentaiV1DocumentIn": "_documentai_92_GoogleCloudDocumentaiV1DocumentIn",
        "GoogleCloudDocumentaiV1DocumentOut": "_documentai_93_GoogleCloudDocumentaiV1DocumentOut",
        "GoogleCloudDocumentaiV1DocumentPageImageIn": "_documentai_94_GoogleCloudDocumentaiV1DocumentPageImageIn",
        "GoogleCloudDocumentaiV1DocumentPageImageOut": "_documentai_95_GoogleCloudDocumentaiV1DocumentPageImageOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn": "_documentai_96_GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut": "_documentai_97_GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn": "_documentai_98_GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut": "_documentai_99_GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn": "_documentai_100_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut": "_documentai_101_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut",
        "GoogleCloudDocumentaiV1beta1InputConfigIn": "_documentai_102_GoogleCloudDocumentaiV1beta1InputConfigIn",
        "GoogleCloudDocumentaiV1beta1InputConfigOut": "_documentai_103_GoogleCloudDocumentaiV1beta1InputConfigOut",
        "GoogleCloudDocumentaiV1FetchProcessorTypesResponseIn": "_documentai_104_GoogleCloudDocumentaiV1FetchProcessorTypesResponseIn",
        "GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut": "_documentai_105_GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut",
        "GoogleCloudDocumentaiV1DocumentSchemaMetadataIn": "_documentai_106_GoogleCloudDocumentaiV1DocumentSchemaMetadataIn",
        "GoogleCloudDocumentaiV1DocumentSchemaMetadataOut": "_documentai_107_GoogleCloudDocumentaiV1DocumentSchemaMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn": "_documentai_108_GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut": "_documentai_109_GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn": "_documentai_110_GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut": "_documentai_111_GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn": "_documentai_112_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut": "_documentai_113_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut",
        "GoogleCloudDocumentaiV1beta1DocumentShardInfoIn": "_documentai_114_GoogleCloudDocumentaiV1beta1DocumentShardInfoIn",
        "GoogleCloudDocumentaiV1beta1DocumentShardInfoOut": "_documentai_115_GoogleCloudDocumentaiV1beta1DocumentShardInfoOut",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn": "_documentai_116_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut": "_documentai_117_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut",
        "GoogleCloudDocumentaiV1ListEvaluationsResponseIn": "_documentai_118_GoogleCloudDocumentaiV1ListEvaluationsResponseIn",
        "GoogleCloudDocumentaiV1ListEvaluationsResponseOut": "_documentai_119_GoogleCloudDocumentaiV1ListEvaluationsResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn": "_documentai_120_GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut": "_documentai_121_GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenIn": "_documentai_122_GoogleCloudDocumentaiV1beta2DocumentPageTokenIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenOut": "_documentai_123_GoogleCloudDocumentaiV1beta2DocumentPageTokenOut",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseIn": "_documentai_124_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseOut": "_documentai_125_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1DocumentShardInfoIn": "_documentai_126_GoogleCloudDocumentaiV1DocumentShardInfoIn",
        "GoogleCloudDocumentaiV1DocumentShardInfoOut": "_documentai_127_GoogleCloudDocumentaiV1DocumentShardInfoOut",
        "GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn": "_documentai_128_GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn",
        "GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut": "_documentai_129_GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut",
        "GoogleCloudDocumentaiV1ProcessorTypeIn": "_documentai_130_GoogleCloudDocumentaiV1ProcessorTypeIn",
        "GoogleCloudDocumentaiV1ProcessorTypeOut": "_documentai_131_GoogleCloudDocumentaiV1ProcessorTypeOut",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseIn": "_documentai_132_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseOut": "_documentai_133_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn": "_documentai_134_GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut": "_documentai_135_GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentTextChangeIn": "_documentai_136_GoogleCloudDocumentaiV1beta1DocumentTextChangeIn",
        "GoogleCloudDocumentaiV1beta1DocumentTextChangeOut": "_documentai_137_GoogleCloudDocumentaiV1beta1DocumentTextChangeOut",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn": "_documentai_138_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut": "_documentai_139_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataIn": "_documentai_140_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataOut": "_documentai_141_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta2BoundingPolyIn": "_documentai_142_GoogleCloudDocumentaiV1beta2BoundingPolyIn",
        "GoogleCloudDocumentaiV1beta2BoundingPolyOut": "_documentai_143_GoogleCloudDocumentaiV1beta2BoundingPolyOut",
        "GoogleCloudDocumentaiV1ListProcessorVersionsResponseIn": "_documentai_144_GoogleCloudDocumentaiV1ListProcessorVersionsResponseIn",
        "GoogleCloudDocumentaiV1ListProcessorVersionsResponseOut": "_documentai_145_GoogleCloudDocumentaiV1ListProcessorVersionsResponseOut",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn": "_documentai_146_GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut": "_documentai_147_GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut",
        "GoogleCloudDocumentaiV1EvaluationIn": "_documentai_148_GoogleCloudDocumentaiV1EvaluationIn",
        "GoogleCloudDocumentaiV1EvaluationOut": "_documentai_149_GoogleCloudDocumentaiV1EvaluationOut",
        "GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentIn": "_documentai_150_GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentIn",
        "GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentOut": "_documentai_151_GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentOut",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn": "_documentai_152_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut": "_documentai_153_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1ProcessorVersionIn": "_documentai_154_GoogleCloudDocumentaiV1ProcessorVersionIn",
        "GoogleCloudDocumentaiV1ProcessorVersionOut": "_documentai_155_GoogleCloudDocumentaiV1ProcessorVersionOut",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn": "_documentai_156_GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut": "_documentai_157_GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageLineIn": "_documentai_158_GoogleCloudDocumentaiV1DocumentPageLineIn",
        "GoogleCloudDocumentaiV1DocumentPageLineOut": "_documentai_159_GoogleCloudDocumentaiV1DocumentPageLineOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn": "_documentai_160_GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut": "_documentai_161_GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataIn": "_documentai_162_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataOut": "_documentai_163_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseIn": "_documentai_164_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseOut": "_documentai_165_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn": "_documentai_166_GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut": "_documentai_167_GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn": "_documentai_168_GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut": "_documentai_169_GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut",
        "GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataIn": "_documentai_170_GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataOut": "_documentai_171_GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn": "_documentai_172_GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut": "_documentai_173_GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut",
        "GoogleCloudDocumentaiV1DocumentEntityRelationIn": "_documentai_174_GoogleCloudDocumentaiV1DocumentEntityRelationIn",
        "GoogleCloudDocumentaiV1DocumentEntityRelationOut": "_documentai_175_GoogleCloudDocumentaiV1DocumentEntityRelationOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn": "_documentai_176_GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut": "_documentai_177_GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataIn": "_documentai_178_GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataOut": "_documentai_179_GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseIn": "_documentai_180_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseOut": "_documentai_181_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentStyleIn": "_documentai_182_GoogleCloudDocumentaiV1beta2DocumentStyleIn",
        "GoogleCloudDocumentaiV1beta2DocumentStyleOut": "_documentai_183_GoogleCloudDocumentaiV1beta2DocumentStyleOut",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataIn": "_documentai_184_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataOut": "_documentai_185_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn": "_documentai_186_GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut": "_documentai_187_GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageLineIn": "_documentai_188_GoogleCloudDocumentaiV1beta2DocumentPageLineIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageLineOut": "_documentai_189_GoogleCloudDocumentaiV1beta2DocumentPageLineOut",
        "GoogleCloudDocumentaiV1beta2GcsSourceIn": "_documentai_190_GoogleCloudDocumentaiV1beta2GcsSourceIn",
        "GoogleCloudDocumentaiV1beta2GcsSourceOut": "_documentai_191_GoogleCloudDocumentaiV1beta2GcsSourceOut",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataIn": "_documentai_192_GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataOut": "_documentai_193_GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenIn": "_documentai_194_GoogleCloudDocumentaiV1beta1DocumentPageTokenIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenOut": "_documentai_195_GoogleCloudDocumentaiV1beta1DocumentPageTokenOut",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataIn": "_documentai_196_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataOut": "_documentai_197_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn": "_documentai_198_GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut": "_documentai_199_GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceIn": "_documentai_200_GoogleCloudDocumentaiV1beta1DocumentProvenanceIn",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceOut": "_documentai_201_GoogleCloudDocumentaiV1beta1DocumentProvenanceOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn": "_documentai_202_GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut": "_documentai_203_GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableIn": "_documentai_204_GoogleCloudDocumentaiV1beta2DocumentPageTableIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableOut": "_documentai_205_GoogleCloudDocumentaiV1beta2DocumentPageTableOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn": "_documentai_206_GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut": "_documentai_207_GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn": "_documentai_208_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut": "_documentai_209_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn": "_documentai_210_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut": "_documentai_211_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut",
        "GoogleCloudDocumentaiV1DocumentOutputConfigIn": "_documentai_212_GoogleCloudDocumentaiV1DocumentOutputConfigIn",
        "GoogleCloudDocumentaiV1DocumentOutputConfigOut": "_documentai_213_GoogleCloudDocumentaiV1DocumentOutputConfigOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn": "_documentai_214_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut": "_documentai_215_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn": "_documentai_216_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut": "_documentai_217_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut",
        "GoogleTypePostalAddressIn": "_documentai_218_GoogleTypePostalAddressIn",
        "GoogleTypePostalAddressOut": "_documentai_219_GoogleTypePostalAddressOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageBlockIn": "_documentai_220_GoogleCloudDocumentaiV1beta2DocumentPageBlockIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageBlockOut": "_documentai_221_GoogleCloudDocumentaiV1beta2DocumentPageBlockOut",
        "GoogleCloudDocumentaiV1DocumentRevisionIn": "_documentai_222_GoogleCloudDocumentaiV1DocumentRevisionIn",
        "GoogleCloudDocumentaiV1DocumentRevisionOut": "_documentai_223_GoogleCloudDocumentaiV1DocumentRevisionOut",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn": "_documentai_224_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut": "_documentai_225_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn": "_documentai_226_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut": "_documentai_227_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataIn": "_documentai_228_GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataOut": "_documentai_229_GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn": "_documentai_230_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut": "_documentai_231_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn": "_documentai_232_GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut": "_documentai_233_GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut",
        "GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn": "_documentai_234_GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn",
        "GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut": "_documentai_235_GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn": "_documentai_236_GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut": "_documentai_237_GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentTextChangeIn": "_documentai_238_GoogleCloudDocumentaiV1beta2DocumentTextChangeIn",
        "GoogleCloudDocumentaiV1beta2DocumentTextChangeOut": "_documentai_239_GoogleCloudDocumentaiV1beta2DocumentTextChangeOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn": "_documentai_240_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut": "_documentai_241_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataIn": "_documentai_242_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataOut": "_documentai_243_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn": "_documentai_244_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut": "_documentai_245_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut",
        "GoogleCloudDocumentaiV1BatchProcessMetadataIn": "_documentai_246_GoogleCloudDocumentaiV1BatchProcessMetadataIn",
        "GoogleCloudDocumentaiV1BatchProcessMetadataOut": "_documentai_247_GoogleCloudDocumentaiV1BatchProcessMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn": "_documentai_248_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut": "_documentai_249_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn": "_documentai_250_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut": "_documentai_251_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn": "_documentai_252_GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut": "_documentai_253_GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn": "_documentai_254_GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn",
        "GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut": "_documentai_255_GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn": "_documentai_256_GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut": "_documentai_257_GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn": "_documentai_258_GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut": "_documentai_259_GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut",
        "GoogleCloudDocumentaiV1DocumentSchemaIn": "_documentai_260_GoogleCloudDocumentaiV1DocumentSchemaIn",
        "GoogleCloudDocumentaiV1DocumentSchemaOut": "_documentai_261_GoogleCloudDocumentaiV1DocumentSchemaOut",
        "GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseIn": "_documentai_262_GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseIn",
        "GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseOut": "_documentai_263_GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseOut",
        "GoogleCloudDocumentaiV1beta2GcsDestinationIn": "_documentai_264_GoogleCloudDocumentaiV1beta2GcsDestinationIn",
        "GoogleCloudDocumentaiV1beta2GcsDestinationOut": "_documentai_265_GoogleCloudDocumentaiV1beta2GcsDestinationOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn": "_documentai_266_GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut": "_documentai_267_GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageIn": "_documentai_268_GoogleCloudDocumentaiV1beta1DocumentPageIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageOut": "_documentai_269_GoogleCloudDocumentaiV1beta1DocumentPageOut",
        "GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn": "_documentai_270_GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn",
        "GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut": "_documentai_271_GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn": "_documentai_272_GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut": "_documentai_273_GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut",
        "GoogleCloudDocumentaiV1beta2OutputConfigIn": "_documentai_274_GoogleCloudDocumentaiV1beta2OutputConfigIn",
        "GoogleCloudDocumentaiV1beta2OutputConfigOut": "_documentai_275_GoogleCloudDocumentaiV1beta2OutputConfigOut",
        "GoogleCloudDocumentaiV1ProcessRequestIn": "_documentai_276_GoogleCloudDocumentaiV1ProcessRequestIn",
        "GoogleCloudDocumentaiV1ProcessRequestOut": "_documentai_277_GoogleCloudDocumentaiV1ProcessRequestOut",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn": "_documentai_278_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut": "_documentai_279_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut",
        "GoogleCloudDocumentaiV1DocumentProvenanceParentIn": "_documentai_280_GoogleCloudDocumentaiV1DocumentProvenanceParentIn",
        "GoogleCloudDocumentaiV1DocumentProvenanceParentOut": "_documentai_281_GoogleCloudDocumentaiV1DocumentProvenanceParentOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageLineIn": "_documentai_282_GoogleCloudDocumentaiV1beta1DocumentPageLineIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageLineOut": "_documentai_283_GoogleCloudDocumentaiV1beta1DocumentPageLineOut",
        "GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn": "_documentai_284_GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut": "_documentai_285_GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataIn": "_documentai_286_GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataOut": "_documentai_287_GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn": "_documentai_288_GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut": "_documentai_289_GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut",
        "GoogleCloudDocumentaiV1beta1NormalizedVertexIn": "_documentai_290_GoogleCloudDocumentaiV1beta1NormalizedVertexIn",
        "GoogleCloudDocumentaiV1beta1NormalizedVertexOut": "_documentai_291_GoogleCloudDocumentaiV1beta1NormalizedVertexOut",
        "GoogleCloudDocumentaiV1VertexIn": "_documentai_292_GoogleCloudDocumentaiV1VertexIn",
        "GoogleCloudDocumentaiV1VertexOut": "_documentai_293_GoogleCloudDocumentaiV1VertexOut",
        "GoogleCloudDocumentaiV1beta2BarcodeIn": "_documentai_294_GoogleCloudDocumentaiV1beta2BarcodeIn",
        "GoogleCloudDocumentaiV1beta2BarcodeOut": "_documentai_295_GoogleCloudDocumentaiV1beta2BarcodeOut",
        "GoogleCloudDocumentaiV1DocumentPageIn": "_documentai_296_GoogleCloudDocumentaiV1DocumentPageIn",
        "GoogleCloudDocumentaiV1DocumentPageOut": "_documentai_297_GoogleCloudDocumentaiV1DocumentPageOut",
        "GoogleCloudDocumentaiV1beta1OutputConfigIn": "_documentai_298_GoogleCloudDocumentaiV1beta1OutputConfigIn",
        "GoogleCloudDocumentaiV1beta1OutputConfigOut": "_documentai_299_GoogleCloudDocumentaiV1beta1OutputConfigOut",
        "GoogleCloudDocumentaiV1DocumentPageTableTableCellIn": "_documentai_300_GoogleCloudDocumentaiV1DocumentPageTableTableCellIn",
        "GoogleCloudDocumentaiV1DocumentPageTableTableCellOut": "_documentai_301_GoogleCloudDocumentaiV1DocumentPageTableTableCellOut",
        "GoogleCloudDocumentaiV1DocumentStyleIn": "_documentai_302_GoogleCloudDocumentaiV1DocumentStyleIn",
        "GoogleCloudDocumentaiV1DocumentStyleOut": "_documentai_303_GoogleCloudDocumentaiV1DocumentStyleOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn": "_documentai_304_GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut": "_documentai_305_GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut",
        "GoogleCloudDocumentaiV1DocumentPageSymbolIn": "_documentai_306_GoogleCloudDocumentaiV1DocumentPageSymbolIn",
        "GoogleCloudDocumentaiV1DocumentPageSymbolOut": "_documentai_307_GoogleCloudDocumentaiV1DocumentPageSymbolOut",
        "GoogleCloudDocumentaiV1beta2DocumentLabelIn": "_documentai_308_GoogleCloudDocumentaiV1beta2DocumentLabelIn",
        "GoogleCloudDocumentaiV1beta2DocumentLabelOut": "_documentai_309_GoogleCloudDocumentaiV1beta2DocumentLabelOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn": "_documentai_310_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut": "_documentai_311_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdIn": "_documentai_312_GoogleCloudDocumentaiUiv1beta3DocumentIdIn",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdOut": "_documentai_313_GoogleCloudDocumentaiUiv1beta3DocumentIdOut",
        "GoogleCloudDocumentaiV1BoundingPolyIn": "_documentai_314_GoogleCloudDocumentaiV1BoundingPolyIn",
        "GoogleCloudDocumentaiV1BoundingPolyOut": "_documentai_315_GoogleCloudDocumentaiV1BoundingPolyOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn": "_documentai_316_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut": "_documentai_317_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataIn": "_documentai_318_GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataOut": "_documentai_319_GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataIn": "_documentai_320_GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataIn",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataOut": "_documentai_321_GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataIn": "_documentai_322_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataOut": "_documentai_323_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn": "_documentai_324_GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn",
        "GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut": "_documentai_325_GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut",
        "GoogleCloudDocumentaiV1ProcessorIn": "_documentai_326_GoogleCloudDocumentaiV1ProcessorIn",
        "GoogleCloudDocumentaiV1ProcessorOut": "_documentai_327_GoogleCloudDocumentaiV1ProcessorOut",
        "GoogleTypeColorIn": "_documentai_328_GoogleTypeColorIn",
        "GoogleTypeColorOut": "_documentai_329_GoogleTypeColorOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageIn": "_documentai_330_GoogleCloudDocumentaiV1beta2DocumentPageIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageOut": "_documentai_331_GoogleCloudDocumentaiV1beta2DocumentPageOut",
        "GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn": "_documentai_332_GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn",
        "GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut": "_documentai_333_GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn": "_documentai_334_GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut": "_documentai_335_GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut",
        "GoogleTypeTimeZoneIn": "_documentai_336_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_documentai_337_GoogleTypeTimeZoneOut",
        "GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataIn": "_documentai_338_GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataIn",
        "GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataOut": "_documentai_339_GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataOut",
        "GoogleCloudDocumentaiV1DisableProcessorMetadataIn": "_documentai_340_GoogleCloudDocumentaiV1DisableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1DisableProcessorMetadataOut": "_documentai_341_GoogleCloudDocumentaiV1DisableProcessorMetadataOut",
        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn": "_documentai_342_GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn",
        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut": "_documentai_343_GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn": "_documentai_344_GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut": "_documentai_345_GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut",
        "GoogleCloudDocumentaiV1DocumentPageFormFieldIn": "_documentai_346_GoogleCloudDocumentaiV1DocumentPageFormFieldIn",
        "GoogleCloudDocumentaiV1DocumentPageFormFieldOut": "_documentai_347_GoogleCloudDocumentaiV1DocumentPageFormFieldOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn": "_documentai_348_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut": "_documentai_349_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn": "_documentai_350_GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut": "_documentai_351_GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut",
        "GoogleCloudDocumentaiV1DisableProcessorRequestIn": "_documentai_352_GoogleCloudDocumentaiV1DisableProcessorRequestIn",
        "GoogleCloudDocumentaiV1DisableProcessorRequestOut": "_documentai_353_GoogleCloudDocumentaiV1DisableProcessorRequestOut",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusIn": "_documentai_354_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusIn",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusOut": "_documentai_355_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusOut",
        "GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn": "_documentai_356_GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn",
        "GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut": "_documentai_357_GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut",
        "GoogleCloudDocumentaiV1beta1OperationMetadataIn": "_documentai_358_GoogleCloudDocumentaiV1beta1OperationMetadataIn",
        "GoogleCloudDocumentaiV1beta1OperationMetadataOut": "_documentai_359_GoogleCloudDocumentaiV1beta1OperationMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn": "_documentai_360_GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut": "_documentai_361_GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut",
        "GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataIn": "_documentai_362_GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataOut": "_documentai_363_GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentEntityIn": "_documentai_364_GoogleCloudDocumentaiV1DocumentEntityIn",
        "GoogleCloudDocumentaiV1DocumentEntityOut": "_documentai_365_GoogleCloudDocumentaiV1DocumentEntityOut",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn": "_documentai_366_GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut": "_documentai_367_GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1NormalizedVertexIn": "_documentai_368_GoogleCloudDocumentaiV1NormalizedVertexIn",
        "GoogleCloudDocumentaiV1NormalizedVertexOut": "_documentai_369_GoogleCloudDocumentaiV1NormalizedVertexOut",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn": "_documentai_370_GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut": "_documentai_371_GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn": "_documentai_372_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut": "_documentai_373_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceIn": "_documentai_374_GoogleCloudDocumentaiV1beta2DocumentProvenanceIn",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceOut": "_documentai_375_GoogleCloudDocumentaiV1beta2DocumentProvenanceOut",
        "GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn": "_documentai_376_GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn",
        "GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut": "_documentai_377_GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageIn": "_documentai_378_GoogleCloudDocumentaiV1beta1DocumentPageImageIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageOut": "_documentai_379_GoogleCloudDocumentaiV1beta1DocumentPageImageOut",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn": "_documentai_380_GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut": "_documentai_381_GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut",
        "GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn": "_documentai_382_GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn",
        "GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut": "_documentai_383_GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut",
        "GoogleTypeDateTimeIn": "_documentai_384_GoogleTypeDateTimeIn",
        "GoogleTypeDateTimeOut": "_documentai_385_GoogleTypeDateTimeOut",
        "GoogleCloudDocumentaiV1beta2NormalizedVertexIn": "_documentai_386_GoogleCloudDocumentaiV1beta2NormalizedVertexIn",
        "GoogleCloudDocumentaiV1beta2NormalizedVertexOut": "_documentai_387_GoogleCloudDocumentaiV1beta2NormalizedVertexOut",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn": "_documentai_388_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut": "_documentai_389_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut",
        "GoogleCloudDocumentaiV1DocumentPageDimensionIn": "_documentai_390_GoogleCloudDocumentaiV1DocumentPageDimensionIn",
        "GoogleCloudDocumentaiV1DocumentPageDimensionOut": "_documentai_391_GoogleCloudDocumentaiV1DocumentPageDimensionOut",
        "GoogleCloudDocumentaiV1ListProcessorsResponseIn": "_documentai_392_GoogleCloudDocumentaiV1ListProcessorsResponseIn",
        "GoogleCloudDocumentaiV1ListProcessorsResponseOut": "_documentai_393_GoogleCloudDocumentaiV1ListProcessorsResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn": "_documentai_394_GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn",
        "GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut": "_documentai_395_GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut",
        "GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn": "_documentai_396_GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn",
        "GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut": "_documentai_397_GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn": "_documentai_398_GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn",
        "GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut": "_documentai_399_GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn": "_documentai_400_GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut": "_documentai_401_GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut",
        "GoogleCloudDocumentaiV1beta1DocumentIn": "_documentai_402_GoogleCloudDocumentaiV1beta1DocumentIn",
        "GoogleCloudDocumentaiV1beta1DocumentOut": "_documentai_403_GoogleCloudDocumentaiV1beta1DocumentOut",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataIn": "_documentai_404_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataOut": "_documentai_405_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageParagraphIn": "_documentai_406_GoogleCloudDocumentaiV1DocumentPageParagraphIn",
        "GoogleCloudDocumentaiV1DocumentPageParagraphOut": "_documentai_407_GoogleCloudDocumentaiV1DocumentPageParagraphOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIn": "_documentai_408_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataOut": "_documentai_409_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn": "_documentai_410_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut": "_documentai_411_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut",
        "GoogleCloudDocumentaiV1ListProcessorTypesResponseIn": "_documentai_412_GoogleCloudDocumentaiV1ListProcessorTypesResponseIn",
        "GoogleCloudDocumentaiV1ListProcessorTypesResponseOut": "_documentai_413_GoogleCloudDocumentaiV1ListProcessorTypesResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn": "_documentai_414_GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut": "_documentai_415_GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut",
        "GoogleCloudDocumentaiV1ReviewDocumentResponseIn": "_documentai_416_GoogleCloudDocumentaiV1ReviewDocumentResponseIn",
        "GoogleCloudDocumentaiV1ReviewDocumentResponseOut": "_documentai_417_GoogleCloudDocumentaiV1ReviewDocumentResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageTokenIn": "_documentai_418_GoogleCloudDocumentaiV1DocumentPageTokenIn",
        "GoogleCloudDocumentaiV1DocumentPageTokenOut": "_documentai_419_GoogleCloudDocumentaiV1DocumentPageTokenOut",
        "GoogleCloudDocumentaiV1DocumentTextAnchorIn": "_documentai_420_GoogleCloudDocumentaiV1DocumentTextAnchorIn",
        "GoogleCloudDocumentaiV1DocumentTextAnchorOut": "_documentai_421_GoogleCloudDocumentaiV1DocumentTextAnchorOut",
        "GoogleCloudDocumentaiV1DeployProcessorVersionMetadataIn": "_documentai_422_GoogleCloudDocumentaiV1DeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1DeployProcessorVersionMetadataOut": "_documentai_423_GoogleCloudDocumentaiV1DeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn": "_documentai_424_GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn",
        "GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut": "_documentai_425_GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut",
        "GoogleCloudDocumentaiV1ProcessResponseIn": "_documentai_426_GoogleCloudDocumentaiV1ProcessResponseIn",
        "GoogleCloudDocumentaiV1ProcessResponseOut": "_documentai_427_GoogleCloudDocumentaiV1ProcessResponseOut",
        "GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn": "_documentai_428_GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn",
        "GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut": "_documentai_429_GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataIn": "_documentai_430_GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataOut": "_documentai_431_GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataOut",
        "GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn": "_documentai_432_GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn",
        "GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut": "_documentai_433_GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn": "_documentai_434_GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut": "_documentai_435_GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionIn": "_documentai_436_GoogleCloudDocumentaiV1beta2DocumentRevisionIn",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionOut": "_documentai_437_GoogleCloudDocumentaiV1beta2DocumentRevisionOut",
        "GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn": "_documentai_438_GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn",
        "GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut": "_documentai_439_GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut",
        "GoogleCloudDocumentaiV1EnableProcessorRequestIn": "_documentai_440_GoogleCloudDocumentaiV1EnableProcessorRequestIn",
        "GoogleCloudDocumentaiV1EnableProcessorRequestOut": "_documentai_441_GoogleCloudDocumentaiV1EnableProcessorRequestOut",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn": "_documentai_442_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut": "_documentai_443_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn": "_documentai_444_GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut": "_documentai_445_GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn": "_documentai_446_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut": "_documentai_447_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentIn": "_documentai_448_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentIn",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentOut": "_documentai_449_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentOut",
        "GoogleCloudDocumentaiV1DocumentTextChangeIn": "_documentai_450_GoogleCloudDocumentaiV1DocumentTextChangeIn",
        "GoogleCloudDocumentaiV1DocumentTextChangeOut": "_documentai_451_GoogleCloudDocumentaiV1DocumentTextChangeOut",
        "GoogleCloudDocumentaiV1DisableProcessorResponseIn": "_documentai_452_GoogleCloudDocumentaiV1DisableProcessorResponseIn",
        "GoogleCloudDocumentaiV1DisableProcessorResponseOut": "_documentai_453_GoogleCloudDocumentaiV1DisableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataIn": "_documentai_454_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataOut": "_documentai_455_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageLayoutIn": "_documentai_456_GoogleCloudDocumentaiV1DocumentPageLayoutIn",
        "GoogleCloudDocumentaiV1DocumentPageLayoutOut": "_documentai_457_GoogleCloudDocumentaiV1DocumentPageLayoutOut",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn": "_documentai_458_GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut": "_documentai_459_GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn": "_documentai_460_GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut": "_documentai_461_GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut",
        "GoogleCloudDocumentaiV1beta1BarcodeIn": "_documentai_462_GoogleCloudDocumentaiV1beta1BarcodeIn",
        "GoogleCloudDocumentaiV1beta1BarcodeOut": "_documentai_463_GoogleCloudDocumentaiV1beta1BarcodeOut",
        "GoogleCloudDocumentaiV1DocumentPageAnchorIn": "_documentai_464_GoogleCloudDocumentaiV1DocumentPageAnchorIn",
        "GoogleCloudDocumentaiV1DocumentPageAnchorOut": "_documentai_465_GoogleCloudDocumentaiV1DocumentPageAnchorOut",
        "GoogleCloudDocumentaiV1beta1DocumentStyleIn": "_documentai_466_GoogleCloudDocumentaiV1beta1DocumentStyleIn",
        "GoogleCloudDocumentaiV1beta1DocumentStyleOut": "_documentai_467_GoogleCloudDocumentaiV1beta1DocumentStyleOut",
        "GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseIn": "_documentai_468_GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseIn",
        "GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseOut": "_documentai_469_GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseOut",
        "GoogleCloudDocumentaiV1BatchProcessRequestIn": "_documentai_470_GoogleCloudDocumentaiV1BatchProcessRequestIn",
        "GoogleCloudDocumentaiV1BatchProcessRequestOut": "_documentai_471_GoogleCloudDocumentaiV1BatchProcessRequestOut",
        "GoogleCloudDocumentaiV1EvaluationMetricsIn": "_documentai_472_GoogleCloudDocumentaiV1EvaluationMetricsIn",
        "GoogleCloudDocumentaiV1EvaluationMetricsOut": "_documentai_473_GoogleCloudDocumentaiV1EvaluationMetricsOut",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataIn": "_documentai_474_GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataOut": "_documentai_475_GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn": "_documentai_476_GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut": "_documentai_477_GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionIn": "_documentai_478_GoogleCloudDocumentaiV1beta1DocumentRevisionIn",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionOut": "_documentai_479_GoogleCloudDocumentaiV1beta1DocumentRevisionOut",
        "GoogleLongrunningListOperationsResponseIn": "_documentai_480_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_documentai_481_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseIn": "_documentai_482_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseOut": "_documentai_483_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseOut",
        "GoogleCloudLocationListLocationsResponseIn": "_documentai_484_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_documentai_485_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn": "_documentai_486_GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut": "_documentai_487_GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1beta1VertexIn": "_documentai_488_GoogleCloudDocumentaiV1beta1VertexIn",
        "GoogleCloudDocumentaiV1beta1VertexOut": "_documentai_489_GoogleCloudDocumentaiV1beta1VertexOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn": "_documentai_490_GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut": "_documentai_491_GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn": "_documentai_492_GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut": "_documentai_493_GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1EvaluationReferenceIn": "_documentai_494_GoogleCloudDocumentaiV1EvaluationReferenceIn",
        "GoogleCloudDocumentaiV1EvaluationReferenceOut": "_documentai_495_GoogleCloudDocumentaiV1EvaluationReferenceOut",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn": "_documentai_496_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut": "_documentai_497_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut",
        "GoogleTypeMoneyIn": "_documentai_498_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_documentai_499_GoogleTypeMoneyOut",
        "GoogleRpcStatusIn": "_documentai_500_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_documentai_501_GoogleRpcStatusOut",
        "GoogleCloudDocumentaiV1DeleteProcessorMetadataIn": "_documentai_502_GoogleCloudDocumentaiV1DeleteProcessorMetadataIn",
        "GoogleCloudDocumentaiV1DeleteProcessorMetadataOut": "_documentai_503_GoogleCloudDocumentaiV1DeleteProcessorMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn": "_documentai_504_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut": "_documentai_505_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut",
        "GoogleCloudDocumentaiV1EnableProcessorResponseIn": "_documentai_506_GoogleCloudDocumentaiV1EnableProcessorResponseIn",
        "GoogleCloudDocumentaiV1EnableProcessorResponseOut": "_documentai_507_GoogleCloudDocumentaiV1EnableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn": "_documentai_508_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut": "_documentai_509_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut",
        "GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn": "_documentai_510_GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn",
        "GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut": "_documentai_511_GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut",
        "GoogleCloudDocumentaiV1beta3HumanReviewStatusIn": "_documentai_512_GoogleCloudDocumentaiV1beta3HumanReviewStatusIn",
        "GoogleCloudDocumentaiV1beta3HumanReviewStatusOut": "_documentai_513_GoogleCloudDocumentaiV1beta3HumanReviewStatusOut",
        "GoogleCloudDocumentaiV1BarcodeIn": "_documentai_514_GoogleCloudDocumentaiV1BarcodeIn",
        "GoogleCloudDocumentaiV1BarcodeOut": "_documentai_515_GoogleCloudDocumentaiV1BarcodeOut",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn": "_documentai_516_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut": "_documentai_517_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut",
        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn": "_documentai_518_GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn",
        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut": "_documentai_519_GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut",
        "GoogleCloudDocumentaiV1HumanReviewStatusIn": "_documentai_520_GoogleCloudDocumentaiV1HumanReviewStatusIn",
        "GoogleCloudDocumentaiV1HumanReviewStatusOut": "_documentai_521_GoogleCloudDocumentaiV1HumanReviewStatusOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn": "_documentai_522_GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut": "_documentai_523_GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn": "_documentai_524_GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut": "_documentai_525_GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentIn": "_documentai_526_GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentIn",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentOut": "_documentai_527_GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentOut",
        "GoogleCloudDocumentaiV1DocumentPageVisualElementIn": "_documentai_528_GoogleCloudDocumentaiV1DocumentPageVisualElementIn",
        "GoogleCloudDocumentaiV1DocumentPageVisualElementOut": "_documentai_529_GoogleCloudDocumentaiV1DocumentPageVisualElementOut",
        "GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn": "_documentai_530_GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn",
        "GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut": "_documentai_531_GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestIn": "_documentai_532_GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestOut": "_documentai_533_GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1beta3BatchProcessResponseIn": "_documentai_534_GoogleCloudDocumentaiV1beta3BatchProcessResponseIn",
        "GoogleCloudDocumentaiV1beta3BatchProcessResponseOut": "_documentai_535_GoogleCloudDocumentaiV1beta3BatchProcessResponseOut",
        "GoogleCloudDocumentaiV1beta1BoundingPolyIn": "_documentai_536_GoogleCloudDocumentaiV1beta1BoundingPolyIn",
        "GoogleCloudDocumentaiV1beta1BoundingPolyOut": "_documentai_537_GoogleCloudDocumentaiV1beta1BoundingPolyOut",
        "GoogleCloudDocumentaiV1beta2VertexIn": "_documentai_538_GoogleCloudDocumentaiV1beta2VertexIn",
        "GoogleCloudDocumentaiV1beta2VertexOut": "_documentai_539_GoogleCloudDocumentaiV1beta2VertexOut",
        "GoogleCloudDocumentaiV1beta2InputConfigIn": "_documentai_540_GoogleCloudDocumentaiV1beta2InputConfigIn",
        "GoogleCloudDocumentaiV1beta2InputConfigOut": "_documentai_541_GoogleCloudDocumentaiV1beta2InputConfigOut",
        "GoogleCloudDocumentaiV1beta2DocumentEntityIn": "_documentai_542_GoogleCloudDocumentaiV1beta2DocumentEntityIn",
        "GoogleCloudDocumentaiV1beta2DocumentEntityOut": "_documentai_543_GoogleCloudDocumentaiV1beta2DocumentEntityOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn": "_documentai_544_GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut": "_documentai_545_GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataIn": "_documentai_546_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataOut": "_documentai_547_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta3DisableProcessorMetadataIn": "_documentai_548_GoogleCloudDocumentaiV1beta3DisableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1beta3DisableProcessorMetadataOut": "_documentai_549_GoogleCloudDocumentaiV1beta3DisableProcessorMetadataOut",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn": "_documentai_550_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut": "_documentai_551_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn": "_documentai_552_GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut": "_documentai_553_GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataIn": "_documentai_554_GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataOut": "_documentai_555_GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn": "_documentai_556_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut": "_documentai_557_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut",
        "GoogleCloudDocumentaiV1RawDocumentIn": "_documentai_558_GoogleCloudDocumentaiV1RawDocumentIn",
        "GoogleCloudDocumentaiV1RawDocumentOut": "_documentai_559_GoogleCloudDocumentaiV1RawDocumentOut",
        "GoogleCloudDocumentaiV1ReviewDocumentRequestIn": "_documentai_560_GoogleCloudDocumentaiV1ReviewDocumentRequestIn",
        "GoogleCloudDocumentaiV1ReviewDocumentRequestOut": "_documentai_561_GoogleCloudDocumentaiV1ReviewDocumentRequestOut",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn": "_documentai_562_GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut": "_documentai_563_GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn": "_documentai_564_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut": "_documentai_565_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn": "_documentai_566_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut": "_documentai_567_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut",
        "GoogleCloudDocumentaiV1DocumentPageMatrixIn": "_documentai_568_GoogleCloudDocumentaiV1DocumentPageMatrixIn",
        "GoogleCloudDocumentaiV1DocumentPageMatrixOut": "_documentai_569_GoogleCloudDocumentaiV1DocumentPageMatrixOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn": "_documentai_570_GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut": "_documentai_571_GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut",
        "GoogleCloudDocumentaiV1beta1GcsDestinationIn": "_documentai_572_GoogleCloudDocumentaiV1beta1GcsDestinationIn",
        "GoogleCloudDocumentaiV1beta1GcsDestinationOut": "_documentai_573_GoogleCloudDocumentaiV1beta1GcsDestinationOut",
        "GoogleCloudDocumentaiV1GcsPrefixIn": "_documentai_574_GoogleCloudDocumentaiV1GcsPrefixIn",
        "GoogleCloudDocumentaiV1GcsPrefixOut": "_documentai_575_GoogleCloudDocumentaiV1GcsPrefixOut",
        "GoogleCloudDocumentaiV1BatchProcessResponseIn": "_documentai_576_GoogleCloudDocumentaiV1BatchProcessResponseIn",
        "GoogleCloudDocumentaiV1BatchProcessResponseOut": "_documentai_577_GoogleCloudDocumentaiV1BatchProcessResponseOut",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn": "_documentai_578_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut": "_documentai_579_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut",
        "GoogleCloudDocumentaiV1DocumentPageBlockIn": "_documentai_580_GoogleCloudDocumentaiV1DocumentPageBlockIn",
        "GoogleCloudDocumentaiV1DocumentPageBlockOut": "_documentai_581_GoogleCloudDocumentaiV1DocumentPageBlockOut",
        "GoogleCloudDocumentaiV1CommonOperationMetadataIn": "_documentai_582_GoogleCloudDocumentaiV1CommonOperationMetadataIn",
        "GoogleCloudDocumentaiV1CommonOperationMetadataOut": "_documentai_583_GoogleCloudDocumentaiV1CommonOperationMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn": "_documentai_584_GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut": "_documentai_585_GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut",
        "GoogleCloudDocumentaiV1DocumentStyleFontSizeIn": "_documentai_586_GoogleCloudDocumentaiV1DocumentStyleFontSizeIn",
        "GoogleCloudDocumentaiV1DocumentStyleFontSizeOut": "_documentai_587_GoogleCloudDocumentaiV1DocumentStyleFontSizeOut",
        "GoogleCloudDocumentaiUiv1beta3RevisionRefIn": "_documentai_588_GoogleCloudDocumentaiUiv1beta3RevisionRefIn",
        "GoogleCloudDocumentaiUiv1beta3RevisionRefOut": "_documentai_589_GoogleCloudDocumentaiUiv1beta3RevisionRefOut",
        "GoogleCloudDocumentaiV1beta3EnableProcessorMetadataIn": "_documentai_590_GoogleCloudDocumentaiV1beta3EnableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1beta3EnableProcessorMetadataOut": "_documentai_591_GoogleCloudDocumentaiV1beta3EnableProcessorMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn"] = t.struct(
        {
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "valueType": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "correctedValueText": t.string().optional(),
            "correctedKeyText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut"] = t.struct(
        {
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "valueType": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "correctedValueText": t.string().optional(),
            "correctedKeyText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut"])
    types["GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityIn"] = t.struct(
        {
            "type": t.string(),
            "confidence": t.number().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
            "mentionText": t.string().optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn"]
            ).optional(),
            "mentionId": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityIn"])
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn"]
            ).optional(),
            "id": t.string().optional(),
            "redacted": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityOut"] = t.struct(
        {
            "type": t.string(),
            "confidence": t.number().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "mentionText": t.string().optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut"]
            ).optional(),
            "mentionId": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityOut"])
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut"]
            ).optional(),
            "id": t.string().optional(),
            "redacted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityOut"])
    types["GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDocumentaiV1EvaluationCountersIn"] = t.struct(
        {
            "evaluatedDocumentsCount": t.integer().optional(),
            "failedDocumentsCount": t.integer().optional(),
            "invalidDocumentsCount": t.integer().optional(),
            "inputDocumentsCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationCountersIn"])
    types["GoogleCloudDocumentaiV1EvaluationCountersOut"] = t.struct(
        {
            "evaluatedDocumentsCount": t.integer().optional(),
            "failedDocumentsCount": t.integer().optional(),
            "invalidDocumentsCount": t.integer().optional(),
            "inputDocumentsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationCountersOut"])
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn"] = t.struct(
        {
            "type": t.integer().optional(),
            "rows": t.integer().optional(),
            "data": t.string().optional(),
            "cols": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut"] = t.struct(
        {
            "type": t.integer().optional(),
            "rows": t.integer().optional(),
            "data": t.string().optional(),
            "cols": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut"])
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1GcsDocumentsIn"] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1GcsDocumentIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1GcsDocumentsIn"])
    types["GoogleCloudDocumentaiV1GcsDocumentsOut"] = t.struct(
        {
            "documents": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1GcsDocumentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1GcsDocumentsOut"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn"] = t.struct(
        {
            "baseProcessorVersion": t.string().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
            ).optional(),
            "inputData": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                ]
            ).optional(),
            "processorVersion": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
            ),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut"] = t.struct(
        {
            "baseProcessorVersion": t.string().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaOut"]
            ).optional(),
            "inputData": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut"
                ]
            ).optional(),
            "processorVersion": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentShardInfoIn"] = t.struct(
        {
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
            "textOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentShardInfoOut"] = t.struct(
        {
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
            "textOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTableIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "bodyRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowIn"])
            ).optional(),
            "headerRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTableOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "bodyRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowOut"])
            ).optional(),
            "headerRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn"])
    types["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut"])
    types["GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataIn"])
    types[
        "GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1beta2DocumentIn"] = t.struct(
        {
            "text": t.string().optional(),
            "uri": t.string().optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn"])
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageIn"])
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoIn"]
            ).optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityIn"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeIn"])
            ).optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentStyleIn"])
            ).optional(),
            "labels": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentLabelIn"])
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentOut"] = t.struct(
        {
            "text": t.string().optional(),
            "uri": t.string().optional(),
            "entityRelations": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageOut"])
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoOut"]
            ).optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityOut"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeOut"])
            ).optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentStyleOut"])
            ).optional(),
            "labels": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentLabelOut"])
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentOut"])
    types["GoogleCloudDocumentaiV1beta2ProcessDocumentResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2OutputConfigIn"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2InputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2ProcessDocumentResponseIn"])
    types["GoogleCloudDocumentaiV1beta2ProcessDocumentResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2OutputConfigOut"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2InputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2ProcessDocumentResponseOut"])
    types["GoogleCloudDocumentaiV1beta2OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta2OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OperationMetadataOut"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageBlockIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageBlockOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockOut"])
    types["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableIn"] = t.struct(
        {
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn"]
                )
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "headerRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableOut"] = t.struct(
        {
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut"]
                )
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "headerRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableOut"])
    types["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn"] = t.struct(
        {
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut"] = t.struct(
        {
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn"] = t.struct(
        {
            "pageRefs": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut"] = t.struct(
        {
            "pageRefs": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut"])
    types["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn"] = t.struct(
        {
            "replacementProcessorVersion": t.string().optional(),
            "deprecationTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn"])
    types["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut"] = t.struct(
        {
            "replacementProcessorVersion": t.string().optional(),
            "deprecationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut"])
    types["GoogleCloudDocumentaiV1GcsDocumentIn"] = t.struct(
        {"gcsUri": t.string().optional(), "mimeType": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1GcsDocumentIn"])
    types["GoogleCloudDocumentaiV1GcsDocumentOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1GcsDocumentOut"])
    types["GoogleCloudDocumentaiV1beta1GcsSourceIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsSourceIn"])
    types["GoogleCloudDocumentaiV1beta1GcsSourceOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsSourceOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTableTableRowIn"] = t.struct(
        {
            "cells": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableCellIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTableTableRowOut"] = t.struct(
        {
            "cells": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableCellOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowOut"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "occurrenceType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "occurrenceType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn"] = t.struct(
        {
            "page": t.string(),
            "layoutType": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "layoutId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut"] = t.struct(
        {
            "page": t.string(),
            "layoutType": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "layoutId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn"] = t.struct(
        {"defaultProcessorVersion": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut"] = t.struct(
        {
            "defaultProcessorVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"] = t.struct(
        {
            "trainingDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
            ).optional(),
            "testDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut"] = t.struct(
        {
            "trainingDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"]
            ).optional(),
            "testDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1EnableProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorMetadataIn"])
    types["GoogleCloudDocumentaiV1EnableProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorMetadataOut"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"] = t.struct(
        {"languageCode": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"])
    types["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut"])
    types["GoogleCloudDocumentaiV1DocumentProvenanceIn"] = t.struct(
        {
            "id": t.integer().optional(),
            "type": t.string().optional(),
            "parents": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentProvenanceParentIn"])
            ).optional(),
            "revision": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"])
    types["GoogleCloudDocumentaiV1DocumentProvenanceOut"] = t.struct(
        {
            "id": t.integer().optional(),
            "type": t.string().optional(),
            "parents": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentProvenanceParentOut"])
            ).optional(),
            "revision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageImageIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "height": t.integer().optional(),
            "content": t.string().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageImageIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageImageOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "height": t.integer().optional(),
            "content": t.string().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageImageOut"])
    types["GoogleCloudDocumentaiV1DocumentIn"] = t.struct(
        {
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentRevisionIn"])
            ).optional(),
            "uri": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageIn"])
            ).optional(),
            "mimeType": t.string().optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentShardInfoIn"]
            ).optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityIn"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentTextChangeIn"])
            ).optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityRelationIn"])
            ).optional(),
            "text": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentStyleIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentIn"])
    types["GoogleCloudDocumentaiV1DocumentOut"] = t.struct(
        {
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentRevisionOut"])
            ).optional(),
            "uri": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageOut"])
            ).optional(),
            "mimeType": t.string().optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentShardInfoOut"]
            ).optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityOut"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentTextChangeOut"])
            ).optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityRelationOut"])
            ).optional(),
            "text": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentStyleOut"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOut"])
    types["GoogleCloudDocumentaiV1DocumentPageImageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "mimeType": t.string().optional(),
            "width": t.integer().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageIn"])
    types["GoogleCloudDocumentaiV1DocumentPageImageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "mimeType": t.string().optional(),
            "width": t.integer().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"] = t.struct(
        {"languageCode": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn"] = t.struct(
        {
            "italic": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "smallcaps": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "fontSize": t.integer().optional(),
            "fontWeight": t.integer().optional(),
            "fontType": t.string().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "subscript": t.boolean().optional(),
            "strikeout": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "superscript": t.boolean().optional(),
            "pixelFontSize": t.number().optional(),
            "bold": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut"] = t.struct(
        {
            "italic": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "smallcaps": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "fontSize": t.integer().optional(),
            "fontWeight": t.integer().optional(),
            "fontType": t.string().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "subscript": t.boolean().optional(),
            "strikeout": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "superscript": t.boolean().optional(),
            "pixelFontSize": t.number().optional(),
            "bold": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut"])
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut"])
    types["GoogleCloudDocumentaiV1beta1InputConfigIn"] = t.struct(
        {
            "mimeType": t.string(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1GcsSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1InputConfigIn"])
    types["GoogleCloudDocumentaiV1beta1InputConfigOut"] = t.struct(
        {
            "mimeType": t.string(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1GcsSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1InputConfigOut"])
    types["GoogleCloudDocumentaiV1FetchProcessorTypesResponseIn"] = t.struct(
        {
            "processorTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1FetchProcessorTypesResponseIn"])
    types["GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut"] = t.struct(
        {
            "processorTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentSchemaMetadataIn"] = t.struct(
        {
            "skipNamingValidation": t.boolean().optional(),
            "documentSplitter": t.boolean().optional(),
            "documentAllowMultipleLabels": t.boolean().optional(),
            "prefixedNamingOnProperties": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaMetadataOut"] = t.struct(
        {
            "skipNamingValidation": t.boolean().optional(),
            "documentSplitter": t.boolean().optional(),
            "documentAllowMultipleLabels": t.boolean().optional(),
            "prefixedNamingOnProperties": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn"] = t.struct(
        {
            "type": t.integer().optional(),
            "rows": t.integer().optional(),
            "cols": t.integer().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut"] = t.struct(
        {
            "type": t.integer().optional(),
            "rows": t.integer().optional(),
            "cols": t.integer().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"] = t.struct(
        {"confidence": t.number().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn"
    ] = t.struct(
        {
            "datasetInconsistencyType": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut"
    ] = t.struct(
        {
            "datasetInconsistencyType": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1beta1DocumentShardInfoIn"] = t.struct(
        {
            "shardCount": t.string().optional(),
            "textOffset": t.string().optional(),
            "shardIndex": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentShardInfoIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentShardInfoOut"] = t.struct(
        {
            "shardCount": t.string().optional(),
            "textOffset": t.string().optional(),
            "shardIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentShardInfoOut"])
    types["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "shardingConfig": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn"
                ]
            ).optional(),
            "fieldMask": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn"])
    types["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "shardingConfig": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut"
                ]
            ).optional(),
            "fieldMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut"])
    types["GoogleCloudDocumentaiV1ListEvaluationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "evaluations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1EvaluationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListEvaluationsResponseIn"])
    types["GoogleCloudDocumentaiV1ListEvaluationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "evaluations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1EvaluationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListEvaluationsResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn"] = t.struct(
        {"state": t.string().optional(), "stateMessage": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseIn"
    ] = t.struct({"evaluation": t.string().optional()}).named(
        renames["GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseOut"
    ] = t.struct(
        {
            "evaluation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseOut"]
    )
    types["GoogleCloudDocumentaiV1DocumentShardInfoIn"] = t.struct(
        {
            "textOffset": t.string().optional(),
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentShardInfoIn"])
    types["GoogleCloudDocumentaiV1DocumentShardInfoOut"] = t.struct(
        {
            "textOffset": t.string().optional(),
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentShardInfoOut"])
    types["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn"] = t.struct(
        {
            "auprc": t.number().optional(),
            "confidenceLevelMetrics": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn"]
                )
            ).optional(),
            "confidenceLevelMetricsExact": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn"]
                )
            ).optional(),
            "estimatedCalibrationError": t.number().optional(),
            "auprcExact": t.number().optional(),
            "estimatedCalibrationErrorExact": t.number().optional(),
            "metricsType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn"])
    types["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut"] = t.struct(
        {
            "auprc": t.number().optional(),
            "confidenceLevelMetrics": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut"
                    ]
                )
            ).optional(),
            "confidenceLevelMetricsExact": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut"
                    ]
                )
            ).optional(),
            "estimatedCalibrationError": t.number().optional(),
            "auprcExact": t.number().optional(),
            "estimatedCalibrationErrorExact": t.number().optional(),
            "metricsType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut"])
    types["GoogleCloudDocumentaiV1ProcessorTypeIn"] = t.struct(
        {
            "category": t.string().optional(),
            "allowCreation": t.boolean().optional(),
            "launchStage": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "availableLocations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn"])
            ).optional(),
            "sampleDocumentUris": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeIn"])
    types["GoogleCloudDocumentaiV1ProcessorTypeOut"] = t.struct(
        {
            "category": t.string().optional(),
            "allowCreation": t.boolean().optional(),
            "launchStage": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "availableLocations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut"])
            ).optional(),
            "sampleDocumentUris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseOut"]
    )
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentTextChangeIn"] = t.struct(
        {
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentTextChangeOut"] = t.struct(
        {
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeOut"])
    types["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn"] = t.struct(
        {"evaluation": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut"] = t.struct(
        {
            "evaluation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataIn"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1beta2BoundingPolyIn"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2NormalizedVertexIn"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2VertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BoundingPolyIn"])
    types["GoogleCloudDocumentaiV1beta2BoundingPolyOut"] = t.struct(
        {
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2NormalizedVertexOut"])
            ).optional(),
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2VertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BoundingPolyOut"])
    types["GoogleCloudDocumentaiV1ListProcessorVersionsResponseIn"] = t.struct(
        {
            "processorVersions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorVersionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorVersionsResponseIn"])
    types["GoogleCloudDocumentaiV1ListProcessorVersionsResponseOut"] = t.struct(
        {
            "processorVersions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorVersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorVersionsResponseOut"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn"] = t.struct(
        {
            "state": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "gcsDestination": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "gcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut"])
    types["GoogleCloudDocumentaiV1EvaluationIn"] = t.struct(
        {
            "entityMetrics": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyVersionName": t.string().optional(),
            "createTime": t.string().optional(),
            "allEntitiesMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn"]
            ).optional(),
            "name": t.string().optional(),
            "documentCounters": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationCountersIn"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationIn"])
    types["GoogleCloudDocumentaiV1EvaluationOut"] = t.struct(
        {
            "entityMetrics": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyVersionName": t.string().optional(),
            "createTime": t.string().optional(),
            "allEntitiesMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut"]
            ).optional(),
            "name": t.string().optional(),
            "documentCounters": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationCountersOut"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationOut"])
    types["GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentIn"] = t.struct(
        {"startIndex": t.string().optional(), "endIndex": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentIn"])
    types["GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentOut"] = t.struct(
        {
            "startIndex": t.string().optional(),
            "endIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentOut"])
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn"] = t.struct(
        {
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut"] = t.struct(
        {
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1ProcessorVersionIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
            ).optional(),
            "googleManaged": t.boolean().optional(),
            "latestEvaluation": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationReferenceIn"]
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "deprecationInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorVersionIn"])
    types["GoogleCloudDocumentaiV1ProcessorVersionOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaOut"]
            ).optional(),
            "googleManaged": t.boolean().optional(),
            "latestEvaluation": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationReferenceOut"]
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "deprecationInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorVersionOut"])
    types["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentPageLineIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLineIn"])
    types["GoogleCloudDocumentaiV1DocumentPageLineOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLineOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut"])
    types["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseIn"] = t.struct(
        {
            "selectedDocuments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseOut"] = t.struct(
        {
            "selectedDocuments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn"] = t.struct(
        {
            "barcode": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BarcodeIn"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut"] = t.struct(
        {
            "barcode": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BarcodeOut"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut"])
    types[
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn"
    ] = t.struct(
        {
            "inputGcsSource": t.string().optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusIn"]
            ).optional(),
            "humanReviewOperation": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "outputGcsDestination": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut"
    ] = t.struct(
        {
            "inputGcsSource": t.string().optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusOut"]
            ).optional(),
            "humanReviewOperation": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "outputGcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataIn"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn"] = t.struct(
        {
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut"] = t.struct(
        {
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut"])
    types["GoogleCloudDocumentaiV1DocumentEntityRelationIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
            "relation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityRelationIn"])
    types["GoogleCloudDocumentaiV1DocumentEntityRelationOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
            "relation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityRelationOut"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseOut"]
    )
    types["GoogleCloudDocumentaiV1beta2DocumentStyleIn"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontFamily": t.string().optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "textStyle": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontWeight": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentStyleIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentStyleOut"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontFamily": t.string().optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "textStyle": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontWeight": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentStyleOut"])
    types["GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataIn"] = t.struct(
        {
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataOut"] = t.struct(
        {
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn"] = t.struct(
        {"gcsUri": t.string(), "cwDocId": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut"] = t.struct(
        {
            "gcsUri": t.string(),
            "cwDocId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageLineIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageLineOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineOut"])
    types["GoogleCloudDocumentaiV1beta2GcsSourceIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsSourceIn"])
    types["GoogleCloudDocumentaiV1beta2GcsSourceOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsSourceOut"])
    types["GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenOut"])
    types["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn"]
                )
            ).optional(),
            "id": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut"]
                )
            ).optional(),
            "id": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "width": t.number().optional(),
            "height": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "width": t.number().optional(),
            "height": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "headerRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "headerRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut"])
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn"] = t.struct(
        {
            "individualImportStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
            "importConfigValidationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut"] = t.struct(
        {
            "individualImportStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
            "importConfigValidationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut"])
    types[
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn"
    ] = t.struct(
        {
            "datasetErrorCount": t.integer().optional(),
            "documentErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "documentErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut"
    ] = t.struct(
        {
            "datasetErrorCount": t.integer().optional(),
            "documentErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "documentErrors": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentOutputConfigIn"] = t.struct(
        {
            "gcsOutputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOutputConfigIn"])
    types["GoogleCloudDocumentaiV1DocumentOutputConfigOut"] = t.struct(
        {
            "gcsOutputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOutputConfigOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn"] = t.struct(
        {
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn"
                    ]
                )
            ).optional(),
            "qualityScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut"] = t.struct(
        {
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut"
                    ]
                )
            ).optional(),
            "qualityScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn"
    ] = t.struct(
        {
            "totalDocumentCount": t.integer().optional(),
            "splitType": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut"
    ] = t.struct(
        {
            "totalDocumentCount": t.integer().optional(),
            "splitType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut"
        ]
    )
    types["GoogleTypePostalAddressIn"] = t.struct(
        {
            "locality": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "sortingCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
        }
    ).named(renames["GoogleTypePostalAddressIn"])
    types["GoogleTypePostalAddressOut"] = t.struct(
        {
            "locality": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "sortingCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypePostalAddressOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageBlockIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageBlockOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockOut"])
    types["GoogleCloudDocumentaiV1DocumentRevisionIn"] = t.struct(
        {
            "parentIds": t.array(t.string()).optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn"]
            ).optional(),
            "agent": t.string().optional(),
            "id": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "processor": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentRevisionIn"])
    types["GoogleCloudDocumentaiV1DocumentRevisionOut"] = t.struct(
        {
            "parentIds": t.array(t.string()).optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut"]
            ).optional(),
            "agent": t.string().optional(),
            "id": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "processor": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentRevisionOut"])
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut"])
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn"
    ] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut"
    ] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn"] = t.struct(
        {"state": t.string().optional(), "stateMessage": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn"] = t.struct(
        {"unit": t.string().optional(), "size": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "size": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut"])
    types["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextChangeIn"] = t.struct(
        {
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextChangeOut"] = t.struct(
        {
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn"] = t.struct(
        {
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn"
                    ]
                )
            ).optional(),
            "qualityScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut"] = t.struct(
        {
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut"
                    ]
                )
            ).optional(),
            "qualityScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut"])
    types["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"]
            ).optional(),
            "outputGcsDestination": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"]
            ).optional(),
            "outputGcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1BatchProcessMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn"
                    ]
                )
            ).optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessMetadataIn"])
    types["GoogleCloudDocumentaiV1BatchProcessMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut"
                    ]
                )
            ).optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn"] = t.struct(
        {
            "totalDocumentCount": t.integer().optional(),
            "individualBatchDeleteStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
            "errorDocumentCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut"] = t.struct(
        {
            "totalDocumentCount": t.integer().optional(),
            "individualBatchDeleteStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "errorDocumentCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn"] = t.struct(
        {"unit": t.string().optional(), "size": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "size": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut"])
    types["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut"])
    types["GoogleCloudDocumentaiV1DocumentSchemaIn"] = t.struct(
        {
            "metadata": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataIn"]
            ).optional(),
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaOut"] = t.struct(
        {
            "metadata": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataOut"]
            ).optional(),
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaOut"])
    types["GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2ProcessDocumentResponseIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseIn"])
    types["GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2ProcessDocumentResponseOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseOut"])
    types["GoogleCloudDocumentaiV1beta2GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsDestinationIn"])
    types["GoogleCloudDocumentaiV1beta2GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsDestinationOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "type": t.string().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "type": t.string().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn"])
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineIn"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn"]
                )
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn"])
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableIn"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockIn"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn"]
                )
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn"]
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenIn"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageIn"]
            ).optional(),
            "pageNumber": t.integer().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn"])
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut"])
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineOut"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut"
                    ]
                )
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut"])
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableOut"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockOut"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut"]
                )
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut"]
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenOut"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageOut"]
            ).optional(),
            "pageNumber": t.integer().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut"])
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
            "relation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
            "relation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn"] = t.struct(
        {
            "pixelFontSize": t.number().optional(),
            "smallcaps": t.boolean().optional(),
            "subscript": t.boolean().optional(),
            "fontType": t.string().optional(),
            "superscript": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "italic": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "strikeout": t.boolean().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "bold": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "fontWeight": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut"] = t.struct(
        {
            "pixelFontSize": t.number().optional(),
            "smallcaps": t.boolean().optional(),
            "subscript": t.boolean().optional(),
            "fontType": t.string().optional(),
            "superscript": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "italic": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "strikeout": t.boolean().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "bold": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "fontWeight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut"])
    types["GoogleCloudDocumentaiV1beta2OutputConfigIn"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsDestinationIn"]
            ).optional(),
            "pagesPerShard": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OutputConfigIn"])
    types["GoogleCloudDocumentaiV1beta2OutputConfigOut"] = t.struct(
        {
            "gcsDestination": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsDestinationOut"]
            ).optional(),
            "pagesPerShard": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OutputConfigOut"])
    types["GoogleCloudDocumentaiV1ProcessRequestIn"] = t.struct(
        {
            "rawDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1RawDocumentIn"]
            ).optional(),
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentIn"]
            ).optional(),
            "fieldMask": t.string().optional(),
            "skipHumanReview": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessRequestIn"])
    types["GoogleCloudDocumentaiV1ProcessRequestOut"] = t.struct(
        {
            "rawDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1RawDocumentOut"]
            ).optional(),
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOut"]
            ).optional(),
            "fieldMask": t.string().optional(),
            "skipHumanReview": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessRequestOut"])
    types[
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn"
    ] = t.struct(
        {"confidence": t.number().optional(), "type": t.string().optional()}
    ).named(
        renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn"]
    )
    types[
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut"
    ] = t.struct(
        {
            "confidence": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentProvenanceParentIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
            "id": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentProvenanceParentIn"])
    types["GoogleCloudDocumentaiV1DocumentProvenanceParentOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
            "id": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentProvenanceParentOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageLineIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageLineOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineOut"])
    types["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataIn"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn"] = t.struct(
        {
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut"] = t.struct(
        {
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut"])
    types["GoogleCloudDocumentaiV1beta1NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1NormalizedVertexIn"])
    types["GoogleCloudDocumentaiV1beta1NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1NormalizedVertexOut"])
    types["GoogleCloudDocumentaiV1VertexIn"] = t.struct(
        {"x": t.integer().optional(), "y": t.integer().optional()}
    ).named(renames["GoogleCloudDocumentaiV1VertexIn"])
    types["GoogleCloudDocumentaiV1VertexOut"] = t.struct(
        {
            "x": t.integer().optional(),
            "y": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1VertexOut"])
    types["GoogleCloudDocumentaiV1beta2BarcodeIn"] = t.struct(
        {
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
            "format": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BarcodeIn"])
    types["GoogleCloudDocumentaiV1beta2BarcodeOut"] = t.struct(
        {
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BarcodeOut"])
    types["GoogleCloudDocumentaiV1DocumentPageIn"] = t.struct(
        {
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableIn"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn"])
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldIn"])
            ).optional(),
            "visualElements": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementIn"])
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn"]
            ).optional(),
            "pageNumber": t.integer().optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageLineIn"])
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageSymbolIn"])
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTokenIn"])
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageMatrixIn"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageParagraphIn"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageIn"]
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageDimensionIn"]
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageBlockIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageIn"])
    types["GoogleCloudDocumentaiV1DocumentPageOut"] = t.struct(
        {
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableOut"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut"]
                )
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldOut"])
            ).optional(),
            "visualElements": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementOut"])
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut"]
            ).optional(),
            "pageNumber": t.integer().optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageLineOut"])
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageSymbolOut"])
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTokenOut"])
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageMatrixOut"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageParagraphOut"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageOut"]
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageDimensionOut"]
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageBlockOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageOut"])
    types["GoogleCloudDocumentaiV1beta1OutputConfigIn"] = t.struct(
        {
            "pagesPerShard": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1OutputConfigIn"])
    types["GoogleCloudDocumentaiV1beta1OutputConfigOut"] = t.struct(
        {
            "pagesPerShard": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1OutputConfigOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTableTableCellIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "colSpan": t.integer().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "rowSpan": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableTableCellIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTableTableCellOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "colSpan": t.integer().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "rowSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableTableCellOut"])
    types["GoogleCloudDocumentaiV1DocumentStyleIn"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeIn"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontFamily": t.string().optional(),
            "fontWeight": t.string().optional(),
            "textStyle": t.string().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleIn"])
    types["GoogleCloudDocumentaiV1DocumentStyleOut"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeOut"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontFamily": t.string().optional(),
            "fontWeight": t.string().optional(),
            "textStyle": t.string().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"] = t.struct(
        {
            "orientation": t.string().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyIn"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"] = t.struct(
        {
            "orientation": t.string().optional(),
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyOut"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"])
    types["GoogleCloudDocumentaiV1DocumentPageSymbolIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageSymbolIn"])
    types["GoogleCloudDocumentaiV1DocumentPageSymbolOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageSymbolOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentLabelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "automlModel": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentLabelIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentLabelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "automlModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentLabelOut"])
    types[
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn"
    ] = t.struct(
        {"confidence": t.number().optional(), "type": t.string().optional()}
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut"
    ] = t.struct(
        {
            "confidence": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut"
        ]
    )
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"] = t.struct(
        {
            "revisionRef": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3RevisionRefIn"]
            ).optional(),
            "gcsManagedDocId": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"] = t.struct(
        {
            "revisionRef": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3RevisionRefOut"]
            ).optional(),
            "gcsManagedDocId": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"])
    types["GoogleCloudDocumentaiV1BoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1VertexIn"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1NormalizedVertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BoundingPolyIn"])
    types["GoogleCloudDocumentaiV1BoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1VertexOut"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BoundingPolyOut"])
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn"] = t.struct(
        {
            "individualExportStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
            "splitExportStats": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut"] = t.struct(
        {
            "individualExportStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "splitExportStats": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut"])
    types["GoogleCloudDocumentaiV1ProcessorIn"] = t.struct(
        {
            "defaultProcessorVersion": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorIn"])
    types["GoogleCloudDocumentaiV1ProcessorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "defaultProcessorVersion": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "processEndpoint": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorOut"])
    types["GoogleTypeColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["GoogleTypeColorIn"])
    types["GoogleTypeColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeColorOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableIn"])
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockIn"])
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn"])
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn"]
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineIn"])
            ).optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn"]
                )
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenIn"])
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn"]
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableOut"])
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockOut"])
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut"])
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut"]
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineOut"])
            ).optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut"]
                )
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenOut"])
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut"]
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageOut"])
    types["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"] = t.struct(
        {
            "gcsDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsDocumentsIn"]
            ).optional(),
            "gcsPrefix": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsPrefixIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"])
    types["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"] = t.struct(
        {
            "gcsDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsDocumentsOut"]
            ).optional(),
            "gcsPrefix": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsPrefixOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"])
    types["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut"])
    types["GoogleTypeTimeZoneIn"] = t.struct(
        {"version": t.string().optional(), "id": t.string().optional()}
    ).named(renames["GoogleTypeTimeZoneIn"])
    types["GoogleTypeTimeZoneOut"] = t.struct(
        {
            "version": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeTimeZoneOut"])
    types["GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataIn"] = t.struct(
        {
            "questionId": t.string().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataIn"])
    types["GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataOut"] = t.struct(
        {
            "questionId": t.string().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataOut"])
    types["GoogleCloudDocumentaiV1DisableProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorMetadataIn"])
    types["GoogleCloudDocumentaiV1DisableProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorMetadataOut"])
    types["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn"] = t.struct(
        {
            "confidenceLevel": t.number().optional(),
            "metrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn"])
    types["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut"] = t.struct(
        {
            "confidenceLevel": t.number().optional(),
            "metrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut"])
    types["GoogleCloudDocumentaiV1DocumentPageFormFieldIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "correctedKeyText": t.string().optional(),
            "correctedValueText": t.string().optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldIn"])
    types["GoogleCloudDocumentaiV1DocumentPageFormFieldOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "correctedKeyText": t.string().optional(),
            "correctedValueText": t.string().optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn"
    ] = t.struct(
        {
            "outputGcsDestination": t.string().optional(),
            "inputGcsSource": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut"
    ] = t.struct(
        {
            "outputGcsDestination": t.string().optional(),
            "inputGcsSource": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn"] = t.struct(
        {
            "pageRefs": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut"] = t.struct(
        {
            "pageRefs": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut"])
    types["GoogleCloudDocumentaiV1DisableProcessorRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorRequestIn"])
    types["GoogleCloudDocumentaiV1DisableProcessorRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorRequestOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusOut"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn"] = t.struct(
        {
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "booleanValue": t.boolean().optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressIn"]).optional(),
            "text": t.string().optional(),
            "floatValue": t.number().optional(),
            "integerValue": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn"])
    types["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut"] = t.struct(
        {
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "booleanValue": t.boolean().optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressOut"]).optional(),
            "text": t.string().optional(),
            "floatValue": t.number().optional(),
            "integerValue": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut"])
    types["GoogleCloudDocumentaiV1beta1OperationMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1OperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta1OperationMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1OperationMetadataOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"] = t.struct(
        {
            "content": t.string().optional(),
            "textSegments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"] = t.struct(
        {
            "content": t.string().optional(),
            "textSegments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"])
    types["GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1DocumentEntityIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "mentionId": t.string().optional(),
            "redacted": t.boolean().optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
            "id": t.string().optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageAnchorIn"]
            ).optional(),
            "mentionText": t.string().optional(),
            "type": t.string(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityIn"])
    types["GoogleCloudDocumentaiV1DocumentEntityOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "mentionId": t.string().optional(),
            "redacted": t.boolean().optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "id": t.string().optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageAnchorOut"]
            ).optional(),
            "mentionText": t.string().optional(),
            "type": t.string(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityOut"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut"])
    types["GoogleCloudDocumentaiV1NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1NormalizedVertexIn"])
    types["GoogleCloudDocumentaiV1NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1NormalizedVertexOut"])
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn"] = t.struct(
        {"evaluation": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut"] = t.struct(
        {
            "evaluation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn"] = t.struct(
        {
            "destDatasetType": t.string().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
            "individualBatchMoveStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusIn"
                    ]
                )
            ).optional(),
            "destSplitType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut"] = t.struct(
        {
            "destDatasetType": t.string().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "individualBatchMoveStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusOut"
                    ]
                )
            ).optional(),
            "destSplitType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"] = t.struct(
        {
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
            "type": t.string().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"] = t.struct(
        {
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
            "type": t.string().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn"] = t.struct(
        {
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "booleanValue": t.boolean().optional(),
            "text": t.string().optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "integerValue": t.integer().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressIn"]).optional(),
            "floatValue": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut"] = t.struct(
        {
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "booleanValue": t.boolean().optional(),
            "text": t.string().optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "integerValue": t.integer().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressOut"]).optional(),
            "floatValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "content": t.string().optional(),
            "width": t.integer().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "content": t.string().optional(),
            "width": t.integer().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"] = t.struct(
        {
            "textSegments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentIn"
                    ]
                )
            ).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"] = t.struct(
        {
            "textSegments": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentOut"
                    ]
                )
            ).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn"] = t.struct(
        {
            "subjectId": t.string().optional(),
            "objectId": t.string().optional(),
            "relation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut"] = t.struct(
        {
            "subjectId": t.string().optional(),
            "objectId": t.string().optional(),
            "relation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut"])
    types["GoogleTypeDateTimeIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "hours": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
            "year": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateTimeIn"])
    types["GoogleTypeDateTimeOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "hours": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "year": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateTimeOut"])
    types["GoogleCloudDocumentaiV1beta2NormalizedVertexIn"] = t.struct(
        {"y": t.number().optional(), "x": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2NormalizedVertexIn"])
    types["GoogleCloudDocumentaiV1beta2NormalizedVertexOut"] = t.struct(
        {
            "y": t.number().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2NormalizedVertexOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn"
    ] = t.struct(
        {
            "documentErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "documentErrorCount": t.integer().optional(),
            "datasetErrorCount": t.integer().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut"
    ] = t.struct(
        {
            "documentErrors": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "documentErrorCount": t.integer().optional(),
            "datasetErrorCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentPageDimensionIn"] = t.struct(
        {
            "height": t.number().optional(),
            "width": t.number().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDimensionIn"])
    types["GoogleCloudDocumentaiV1DocumentPageDimensionOut"] = t.struct(
        {
            "height": t.number().optional(),
            "width": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDimensionOut"])
    types["GoogleCloudDocumentaiV1ListProcessorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processors": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorsResponseIn"])
    types["GoogleCloudDocumentaiV1ListProcessorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processors": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorsResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn"] = t.struct(
        {
            "handwritten": t.boolean().optional(),
            "smallcaps": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "letterSpacing": t.number().optional(),
            "superscript": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "subscript": t.boolean().optional(),
            "pixelFontSize": t.number().optional(),
            "fontType": t.string().optional(),
            "fontWeight": t.integer().optional(),
            "strikeout": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "fontSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut"] = t.struct(
        {
            "handwritten": t.boolean().optional(),
            "smallcaps": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "letterSpacing": t.number().optional(),
            "superscript": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "subscript": t.boolean().optional(),
            "pixelFontSize": t.number().optional(),
            "fontType": t.string().optional(),
            "fontWeight": t.integer().optional(),
            "strikeout": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut"])
    types["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1OutputConfigIn"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1InputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn"])
    types["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut"] = t.struct(
        {
            "outputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1OutputConfigOut"]
            ).optional(),
            "inputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1InputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "barcode": t.proxy(renames["GoogleCloudDocumentaiV1BarcodeIn"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn"])
    types["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "barcode": t.proxy(renames["GoogleCloudDocumentaiV1BarcodeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn"] = t.struct(
        {
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut"] = t.struct(
        {
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentIn"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityIn"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeIn"])
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionIn"])
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageIn"])
            ).optional(),
            "text": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentStyleIn"])
            ).optional(),
            "content": t.string().optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn"])
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentShardInfoIn"]
            ).optional(),
            "uri": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentOut"] = t.struct(
        {
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityOut"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeOut"])
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageOut"])
            ).optional(),
            "text": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentStyleOut"])
            ).optional(),
            "content": t.string().optional(),
            "entityRelations": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut"]
                )
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentShardInfoOut"]
            ).optional(),
            "uri": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataIn"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1DocumentPageParagraphIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageParagraphIn"])
    types["GoogleCloudDocumentaiV1DocumentPageParagraphOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageParagraphOut"])
    types["GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIn"] = t.struct(
        {
            "individualDocumentResyncStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
            "datasetResyncStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataOut"] = t.struct(
        {
            "individualDocumentResyncStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut"
                    ]
                )
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "datasetResyncStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataOut"])
    types[
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn"
    ] = t.struct(
        {
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "datasetErrorCount": t.integer().optional(),
            "documentErrorCount": t.integer().optional(),
            "documentErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut"
    ] = t.struct(
        {
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "datasetErrorCount": t.integer().optional(),
            "documentErrorCount": t.integer().optional(),
            "documentErrors": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut"
        ]
    )
    types["GoogleCloudDocumentaiV1ListProcessorTypesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processorTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorTypesResponseIn"])
    types["GoogleCloudDocumentaiV1ListProcessorTypesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processorTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorTypesResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn"] = t.struct(
        {"endIndex": t.string().optional(), "startIndex": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut"] = t.struct(
        {
            "endIndex": t.string().optional(),
            "startIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut"])
    types["GoogleCloudDocumentaiV1ReviewDocumentResponseIn"] = t.struct(
        {
            "state": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "gcsDestination": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentResponseIn"])
    types["GoogleCloudDocumentaiV1ReviewDocumentResponseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "gcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenOut"])
    types["GoogleCloudDocumentaiV1DocumentTextAnchorIn"] = t.struct(
        {
            "textSegments": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentIn"]
                )
            ).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"])
    types["GoogleCloudDocumentaiV1DocumentTextAnchorOut"] = t.struct(
        {
            "textSegments": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentOut"]
                )
            ).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut"])
    types["GoogleCloudDocumentaiV1ProcessResponseIn"] = t.struct(
        {
            "document": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentIn"]
            ).optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessResponseIn"])
    types["GoogleCloudDocumentaiV1ProcessResponseOut"] = t.struct(
        {
            "document": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOut"]
            ).optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessResponseOut"])
    types["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataIn"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn"] = t.struct(
        {
            "page": t.string(),
            "layoutType": t.string().optional(),
            "layoutId": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut"] = t.struct(
        {
            "page": t.string(),
            "layoutType": t.string().optional(),
            "layoutId": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionIn"] = t.struct(
        {
            "processor": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "agent": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionOut"] = t.struct(
        {
            "processor": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "agent": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressIn"]).optional(),
            "integerValue": t.integer().optional(),
            "floatValue": t.number().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "text": t.string().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut"] = t.struct(
        {
            "booleanValue": t.boolean().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressOut"]).optional(),
            "integerValue": t.integer().optional(),
            "floatValue": t.number().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "text": t.string().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut"])
    types["GoogleCloudDocumentaiV1EnableProcessorRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorRequestIn"])
    types["GoogleCloudDocumentaiV1EnableProcessorRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorRequestOut"])
    types["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn"] = t.struct(
        {"gcsUri": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn"] = t.struct(
        {
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut"] = t.struct(
        {
            "cells": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut"])
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentIn"
    ] = t.struct({"documentId": t.string().optional()}).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentOut"
    ] = t.struct(
        {
            "documentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentTextChangeIn"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextChangeIn"])
    types["GoogleCloudDocumentaiV1DocumentTextChangeOut"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextChangeOut"])
    types["GoogleCloudDocumentaiV1DisableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1DisableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorResponseOut"])
    types[
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataIn"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataIn"]
    )
    types[
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1DocumentPageLayoutIn"] = t.struct(
        {
            "orientation": t.string().optional(),
            "confidence": t.number().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"])
    types["GoogleCloudDocumentaiV1DocumentPageLayoutOut"] = t.struct(
        {
            "orientation": t.string().optional(),
            "confidence": t.number().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn"] = t.struct(
        {
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn"
                    ]
                )
            ).optional(),
            "stateMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut"] = t.struct(
        {
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut"
                    ]
                )
            ).optional(),
            "stateMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn"] = t.struct(
        {
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "correctedKeyText": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "valueType": t.string().optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "correctedValueText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut"] = t.struct(
        {
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "correctedKeyText": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "valueType": t.string().optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "correctedValueText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut"])
    types["GoogleCloudDocumentaiV1beta1BarcodeIn"] = t.struct(
        {
            "format": t.string().optional(),
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1BarcodeIn"])
    types["GoogleCloudDocumentaiV1beta1BarcodeOut"] = t.struct(
        {
            "format": t.string().optional(),
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1BarcodeOut"])
    types["GoogleCloudDocumentaiV1DocumentPageAnchorIn"] = t.struct(
        {
            "pageRefs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageAnchorIn"])
    types["GoogleCloudDocumentaiV1DocumentPageAnchorOut"] = t.struct(
        {
            "pageRefs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageAnchorOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentStyleIn"] = t.struct(
        {
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
            "color": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontWeight": t.string().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontFamily": t.string().optional(),
            "textStyle": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentStyleIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentStyleOut"] = t.struct(
        {
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "color": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontWeight": t.string().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontFamily": t.string().optional(),
            "textStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentStyleOut"])
    types["GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseIn"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseIn"])
    types["GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseOut"])
    types["GoogleCloudDocumentaiV1BatchProcessRequestIn"] = t.struct(
        {
            "documentOutputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOutputConfigIn"]
            ).optional(),
            "inputDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
            ).optional(),
            "skipHumanReview": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessRequestIn"])
    types["GoogleCloudDocumentaiV1BatchProcessRequestOut"] = t.struct(
        {
            "documentOutputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOutputConfigOut"]
            ).optional(),
            "inputDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"]
            ).optional(),
            "skipHumanReview": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessRequestOut"])
    types["GoogleCloudDocumentaiV1EvaluationMetricsIn"] = t.struct(
        {
            "groundTruthOccurrencesCount": t.integer().optional(),
            "f1Score": t.number().optional(),
            "falsePositivesCount": t.integer().optional(),
            "predictedDocumentCount": t.integer().optional(),
            "groundTruthDocumentCount": t.integer().optional(),
            "totalDocumentsCount": t.integer().optional(),
            "truePositivesCount": t.integer().optional(),
            "predictedOccurrencesCount": t.integer().optional(),
            "recall": t.number().optional(),
            "precision": t.number().optional(),
            "falseNegativesCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMetricsIn"])
    types["GoogleCloudDocumentaiV1EvaluationMetricsOut"] = t.struct(
        {
            "groundTruthOccurrencesCount": t.integer().optional(),
            "f1Score": t.number().optional(),
            "falsePositivesCount": t.integer().optional(),
            "predictedDocumentCount": t.integer().optional(),
            "groundTruthDocumentCount": t.integer().optional(),
            "totalDocumentsCount": t.integer().optional(),
            "truePositivesCount": t.integer().optional(),
            "predictedOccurrencesCount": t.integer().optional(),
            "recall": t.number().optional(),
            "precision": t.number().optional(),
            "falseNegativesCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMetricsOut"])
    types["GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentRevisionIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "processor": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn"]
            ).optional(),
            "parent": t.array(t.integer()).optional(),
            "agent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentRevisionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "processor": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut"]
            ).optional(),
            "parent": t.array(t.integer()).optional(),
            "agent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types[
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseIn"]
    )
    types[
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseOut"]
    )
    types["GoogleCloudLocationListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseIn"])
    types["GoogleCloudLocationListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseOut"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut"])
    types["GoogleCloudDocumentaiV1beta1VertexIn"] = t.struct(
        {"x": t.integer().optional(), "y": t.integer().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1VertexIn"])
    types["GoogleCloudDocumentaiV1beta1VertexOut"] = t.struct(
        {
            "x": t.integer().optional(),
            "y": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1VertexOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyIn"]
            ).optional(),
            "orientation": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyOut"]
            ).optional(),
            "orientation": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1EvaluationReferenceIn"] = t.struct(
        {
            "operation": t.string().optional(),
            "aggregateMetricsExact": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsIn"]
            ).optional(),
            "evaluation": t.string().optional(),
            "aggregateMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationReferenceIn"])
    types["GoogleCloudDocumentaiV1EvaluationReferenceOut"] = t.struct(
        {
            "operation": t.string().optional(),
            "aggregateMetricsExact": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsOut"]
            ).optional(),
            "evaluation": t.string().optional(),
            "aggregateMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationReferenceOut"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "enumValues": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn"]
            ).optional(),
            "baseTypes": t.array(t.string()).optional(),
            "properties": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn"]
                )
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "enumValues": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut"]
            ).optional(),
            "baseTypes": t.array(t.string()).optional(),
            "properties": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut"
                    ]
                )
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDocumentaiV1DeleteProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1DeleteProcessorMetadataIn"])
    types["GoogleCloudDocumentaiV1DeleteProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DeleteProcessorMetadataOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"]
            ).optional(),
            "documentInconsistencyType": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"]
            ).optional(),
            "documentInconsistencyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1EnableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1EnableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorResponseOut"])
    types[
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn"
    ] = t.struct(
        {"type": t.string().optional(), "confidence": t.number().optional()}
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut"
    ] = t.struct(
        {
            "type": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn"] = t.struct(
        {"stateMessage": t.string().optional(), "state": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn"])
    types["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut"])
    types["GoogleCloudDocumentaiV1beta3HumanReviewStatusIn"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusIn"])
    types["GoogleCloudDocumentaiV1beta3HumanReviewStatusOut"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusOut"])
    types["GoogleCloudDocumentaiV1BarcodeIn"] = t.struct(
        {
            "format": t.string().optional(),
            "rawValue": t.string().optional(),
            "valueFormat": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BarcodeIn"])
    types["GoogleCloudDocumentaiV1BarcodeOut"] = t.struct(
        {
            "format": t.string().optional(),
            "rawValue": t.string().optional(),
            "valueFormat": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BarcodeOut"])
    types[
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn"
    ] = t.struct(
        {
            "pagesPerShard": t.integer().optional(),
            "pagesOverlap": t.integer().optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut"
    ] = t.struct(
        {
            "pagesPerShard": t.integer().optional(),
            "pagesOverlap": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusIn"]
            ).optional(),
            "inputGcsSource": t.string().optional(),
            "outputGcsDestination": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn"]
    )
    types[
        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusOut"]
            ).optional(),
            "inputGcsSource": t.string().optional(),
            "outputGcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut"]
    )
    types["GoogleCloudDocumentaiV1HumanReviewStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1HumanReviewStatusIn"])
    types["GoogleCloudDocumentaiV1HumanReviewStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1HumanReviewStatusOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "colSpan": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut"] = t.struct(
        {
            "rowSpan": t.integer().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "colSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentIn"] = t.struct(
        {"endIndex": t.string().optional(), "startIndex": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentOut"] = t.struct(
        {
            "endIndex": t.string().optional(),
            "startIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentOut"])
    types["GoogleCloudDocumentaiV1DocumentPageVisualElementIn"] = t.struct(
        {
            "type": t.string().optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementIn"])
    types["GoogleCloudDocumentaiV1DocumentPageVisualElementOut"] = t.struct(
        {
            "type": t.string().optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementOut"])
    types["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "page": t.string(),
            "layoutId": t.string().optional(),
            "layoutType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn"])
    types["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "page": t.string(),
            "layoutId": t.string().optional(),
            "layoutType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut"])
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestIn"] = t.struct(
        {
            "evaluationDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestOut"] = t.struct(
        {
            "evaluationDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestOut"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessResponseIn"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessResponseOut"])
    types["GoogleCloudDocumentaiV1beta1BoundingPolyIn"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1VertexIn"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1NormalizedVertexIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1BoundingPolyIn"])
    types["GoogleCloudDocumentaiV1beta1BoundingPolyOut"] = t.struct(
        {
            "vertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1VertexOut"])
            ).optional(),
            "normalizedVertices": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1NormalizedVertexOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1BoundingPolyOut"])
    types["GoogleCloudDocumentaiV1beta2VertexIn"] = t.struct(
        {"y": t.integer().optional(), "x": t.integer().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2VertexIn"])
    types["GoogleCloudDocumentaiV1beta2VertexOut"] = t.struct(
        {
            "y": t.integer().optional(),
            "x": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2VertexOut"])
    types["GoogleCloudDocumentaiV1beta2InputConfigIn"] = t.struct(
        {
            "mimeType": t.string(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsSourceIn"]
            ).optional(),
            "contents": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2InputConfigIn"])
    types["GoogleCloudDocumentaiV1beta2InputConfigOut"] = t.struct(
        {
            "mimeType": t.string(),
            "gcsSource": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsSourceOut"]
            ).optional(),
            "contents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2InputConfigOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityIn"] = t.struct(
        {
            "type": t.string(),
            "confidence": t.number().optional(),
            "redacted": t.boolean().optional(),
            "id": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
            "mentionText": t.string().optional(),
            "mentionId": t.string().optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn"]
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityOut"] = t.struct(
        {
            "type": t.string(),
            "confidence": t.number().optional(),
            "redacted": t.boolean().optional(),
            "id": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "mentionText": t.string().optional(),
            "mentionId": t.string().optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut"]
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "height": t.number().optional(),
            "width": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "height": t.number().optional(),
            "width": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataIn"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataIn"]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataOut"
    ] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataOut"]
    )
    types["GoogleCloudDocumentaiV1beta3DisableProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DisableProcessorMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3DisableProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3DisableProcessorMetadataOut"])
    types["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "colSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "colSpan": t.integer().optional(),
            "rowSpan": t.integer().optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut"])
    types["GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn"
    ] = t.struct(
        {
            "inputGcsSource": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut"
    ] = t.struct(
        {
            "inputGcsSource": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut"
        ]
    )
    types["GoogleCloudDocumentaiV1RawDocumentIn"] = t.struct(
        {"content": t.string().optional(), "mimeType": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1RawDocumentIn"])
    types["GoogleCloudDocumentaiV1RawDocumentOut"] = t.struct(
        {
            "content": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1RawDocumentOut"])
    types["GoogleCloudDocumentaiV1ReviewDocumentRequestIn"] = t.struct(
        {
            "enableSchemaValidation": t.boolean().optional(),
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentIn"]
            ).optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
            ).optional(),
            "priority": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentRequestIn"])
    types["GoogleCloudDocumentaiV1ReviewDocumentRequestOut"] = t.struct(
        {
            "enableSchemaValidation": t.boolean().optional(),
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOut"]
            ).optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaOut"]
            ).optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentRequestOut"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "questionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "questionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn"] = t.struct(
        {
            "individualAutoLabelStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn"
                    ]
                )
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut"] = t.struct(
        {
            "individualAutoLabelStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut"
                    ]
                )
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn"] = t.struct(
        {
            "qualityScore": t.number().optional(),
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn"])
    types["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut"] = t.struct(
        {
            "qualityScore": t.number().optional(),
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut"])
    types["GoogleCloudDocumentaiV1DocumentPageMatrixIn"] = t.struct(
        {
            "rows": t.integer().optional(),
            "data": t.string().optional(),
            "type": t.integer().optional(),
            "cols": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageMatrixIn"])
    types["GoogleCloudDocumentaiV1DocumentPageMatrixOut"] = t.struct(
        {
            "rows": t.integer().optional(),
            "data": t.string().optional(),
            "type": t.integer().optional(),
            "cols": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageMatrixOut"])
    types["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut"])
    types["GoogleCloudDocumentaiV1beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsDestinationIn"])
    types["GoogleCloudDocumentaiV1beta1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsDestinationOut"])
    types["GoogleCloudDocumentaiV1GcsPrefixIn"] = t.struct(
        {"gcsUriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1GcsPrefixIn"])
    types["GoogleCloudDocumentaiV1GcsPrefixOut"] = t.struct(
        {
            "gcsUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1GcsPrefixOut"])
    types["GoogleCloudDocumentaiV1BatchProcessResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessResponseIn"])
    types["GoogleCloudDocumentaiV1BatchProcessResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessResponseOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentPageBlockIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageBlockIn"])
    types["GoogleCloudDocumentaiV1DocumentPageBlockOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageBlockOut"])
    types["GoogleCloudDocumentaiV1CommonOperationMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"])
    types["GoogleCloudDocumentaiV1CommonOperationMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "resource": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "barcode": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BarcodeIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "barcode": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BarcodeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut"])
    types["GoogleCloudDocumentaiV1DocumentStyleFontSizeIn"] = t.struct(
        {"size": t.number().optional(), "unit": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeIn"])
    types["GoogleCloudDocumentaiV1DocumentStyleFontSizeOut"] = t.struct(
        {
            "size": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeOut"])
    types["GoogleCloudDocumentaiUiv1beta3RevisionRefIn"] = t.struct(
        {
            "revisionCase": t.string().optional(),
            "revisionId": t.string().optional(),
            "latestProcessorVersion": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3RevisionRefIn"])
    types["GoogleCloudDocumentaiUiv1beta3RevisionRefOut"] = t.struct(
        {
            "revisionCase": t.string().optional(),
            "revisionId": t.string().optional(),
            "latestProcessorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3RevisionRefOut"])
    types["GoogleCloudDocumentaiV1beta3EnableProcessorMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3EnableProcessorMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3EnableProcessorMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3EnableProcessorMetadataOut"])

    functions = {}
    functions["operationsDelete"] = documentai.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = documentai.get(
        "v1/{parent}:fetchProcessorTypes",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = documentai.get(
        "v1/{parent}:fetchProcessorTypes",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFetchProcessorTypes"] = documentai.get(
        "v1/{parent}:fetchProcessorTypes",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = documentai.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = documentai.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = documentai.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcess"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsCreate"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsBatchProcess"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsDisable"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsList"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProcessorsSetDefaultProcessorVersion"
    ] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsGet"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsDelete"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsEnable"] = documentai.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProcessorsProcessorVersionsBatchProcess"
    ] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsGet"] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsDelete"] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsUndeploy"] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProcessorsProcessorVersionsEvaluateProcessorVersion"
    ] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsProcess"] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsList"] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsDeploy"] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsTrain"] = documentai.post(
        "v1/{parent}/processorVersions:train",
        t.struct(
            {
                "parent": t.string(),
                "baseProcessorVersion": t.string().optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "inputData": t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                    ]
                ).optional(),
                "processorVersion": t.proxy(
                    renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProcessorsProcessorVersionsEvaluationsList"
    ] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDocumentaiV1EvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProcessorsProcessorVersionsEvaluationsGet"
    ] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDocumentaiV1EvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsProcessorsHumanReviewConfigReviewDocument"
    ] = documentai.post(
        "v1/{humanReviewConfig}:reviewDocument",
        t.struct(
            {
                "humanReviewConfig": t.string(),
                "enableSchemaValidation": t.boolean().optional(),
                "inlineDocument": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentIn"]
                ).optional(),
                "documentSchema": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
                ).optional(),
                "priority": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorTypesGet"] = documentai.get(
        "v1/{parent}/processorTypes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDocumentaiV1ListProcessorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorTypesList"] = documentai.get(
        "v1/{parent}/processorTypes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDocumentaiV1ListProcessorTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="documentai",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
