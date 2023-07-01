from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_documentai():
    documentai = HTTPRuntime("https://documentai.googleapis.com/")

    renames = {
        "ErrorResponse": "_documentai_1_ErrorResponse",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn": "_documentai_2_GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut": "_documentai_3_GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenIn": "_documentai_4_GoogleCloudDocumentaiV1beta2DocumentPageTokenIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenOut": "_documentai_5_GoogleCloudDocumentaiV1beta2DocumentPageTokenOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn": "_documentai_6_GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut": "_documentai_7_GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut",
        "GoogleCloudDocumentaiV1DisableProcessorResponseIn": "_documentai_8_GoogleCloudDocumentaiV1DisableProcessorResponseIn",
        "GoogleCloudDocumentaiV1DisableProcessorResponseOut": "_documentai_9_GoogleCloudDocumentaiV1DisableProcessorResponseOut",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentIn": "_documentai_10_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentIn",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentOut": "_documentai_11_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseSelectedDocumentOut",
        "GoogleCloudDocumentaiV1DocumentSchemaMetadataIn": "_documentai_12_GoogleCloudDocumentaiV1DocumentSchemaMetadataIn",
        "GoogleCloudDocumentaiV1DocumentSchemaMetadataOut": "_documentai_13_GoogleCloudDocumentaiV1DocumentSchemaMetadataOut",
        "GoogleCloudDocumentaiV1beta2BarcodeIn": "_documentai_14_GoogleCloudDocumentaiV1beta2BarcodeIn",
        "GoogleCloudDocumentaiV1beta2BarcodeOut": "_documentai_15_GoogleCloudDocumentaiV1beta2BarcodeOut",
        "GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn": "_documentai_16_GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn",
        "GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut": "_documentai_17_GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn": "_documentai_18_GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut": "_documentai_19_GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta1InputConfigIn": "_documentai_20_GoogleCloudDocumentaiV1beta1InputConfigIn",
        "GoogleCloudDocumentaiV1beta1InputConfigOut": "_documentai_21_GoogleCloudDocumentaiV1beta1InputConfigOut",
        "GoogleTypeColorIn": "_documentai_22_GoogleTypeColorIn",
        "GoogleTypeColorOut": "_documentai_23_GoogleTypeColorOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn": "_documentai_24_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut": "_documentai_25_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn": "_documentai_26_GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut": "_documentai_27_GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut",
        "GoogleCloudDocumentaiV1beta1BoundingPolyIn": "_documentai_28_GoogleCloudDocumentaiV1beta1BoundingPolyIn",
        "GoogleCloudDocumentaiV1beta1BoundingPolyOut": "_documentai_29_GoogleCloudDocumentaiV1beta1BoundingPolyOut",
        "GoogleCloudDocumentaiV1DocumentPageImageIn": "_documentai_30_GoogleCloudDocumentaiV1DocumentPageImageIn",
        "GoogleCloudDocumentaiV1DocumentPageImageOut": "_documentai_31_GoogleCloudDocumentaiV1DocumentPageImageOut",
        "GoogleCloudDocumentaiV1beta2GcsSourceIn": "_documentai_32_GoogleCloudDocumentaiV1beta2GcsSourceIn",
        "GoogleCloudDocumentaiV1beta2GcsSourceOut": "_documentai_33_GoogleCloudDocumentaiV1beta2GcsSourceOut",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn": "_documentai_34_GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut": "_documentai_35_GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn": "_documentai_36_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut": "_documentai_37_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn": "_documentai_38_GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut": "_documentai_39_GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut",
        "GoogleCloudDocumentaiV1ReviewDocumentResponseIn": "_documentai_40_GoogleCloudDocumentaiV1ReviewDocumentResponseIn",
        "GoogleCloudDocumentaiV1ReviewDocumentResponseOut": "_documentai_41_GoogleCloudDocumentaiV1ReviewDocumentResponseOut",
        "GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseIn": "_documentai_42_GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseIn",
        "GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseOut": "_documentai_43_GoogleCloudDocumentaiV1beta1BatchProcessDocumentsResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn": "_documentai_44_GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut": "_documentai_45_GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut",
        "GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn": "_documentai_46_GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn",
        "GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut": "_documentai_47_GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn": "_documentai_48_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut": "_documentai_49_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1beta3HumanReviewStatusIn": "_documentai_50_GoogleCloudDocumentaiV1beta3HumanReviewStatusIn",
        "GoogleCloudDocumentaiV1beta3HumanReviewStatusOut": "_documentai_51_GoogleCloudDocumentaiV1beta3HumanReviewStatusOut",
        "GoogleCloudDocumentaiV1DocumentPageSymbolIn": "_documentai_52_GoogleCloudDocumentaiV1DocumentPageSymbolIn",
        "GoogleCloudDocumentaiV1DocumentPageSymbolOut": "_documentai_53_GoogleCloudDocumentaiV1DocumentPageSymbolOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageIn": "_documentai_54_GoogleCloudDocumentaiV1beta1DocumentPageIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageOut": "_documentai_55_GoogleCloudDocumentaiV1beta1DocumentPageOut",
        "GoogleTypeDateTimeIn": "_documentai_56_GoogleTypeDateTimeIn",
        "GoogleTypeDateTimeOut": "_documentai_57_GoogleTypeDateTimeOut",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn": "_documentai_58_GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut": "_documentai_59_GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut",
        "GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataIn": "_documentai_60_GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataOut": "_documentai_61_GoogleCloudDocumentaiUiv1beta3CreateLabelerPoolOperationMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageLineIn": "_documentai_62_GoogleCloudDocumentaiV1beta1DocumentPageLineIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageLineOut": "_documentai_63_GoogleCloudDocumentaiV1beta1DocumentPageLineOut",
        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn": "_documentai_64_GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn",
        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut": "_documentai_65_GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestIn": "_documentai_66_GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestOut": "_documentai_67_GoogleCloudDocumentaiV1EvaluateProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1EvaluationReferenceIn": "_documentai_68_GoogleCloudDocumentaiV1EvaluationReferenceIn",
        "GoogleCloudDocumentaiV1EvaluationReferenceOut": "_documentai_69_GoogleCloudDocumentaiV1EvaluationReferenceOut",
        "GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn": "_documentai_70_GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn",
        "GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut": "_documentai_71_GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn": "_documentai_72_GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut": "_documentai_73_GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn": "_documentai_74_GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut": "_documentai_75_GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut",
        "GoogleCloudDocumentaiV1DocumentPageDimensionIn": "_documentai_76_GoogleCloudDocumentaiV1DocumentPageDimensionIn",
        "GoogleCloudDocumentaiV1DocumentPageDimensionOut": "_documentai_77_GoogleCloudDocumentaiV1DocumentPageDimensionOut",
        "GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn": "_documentai_78_GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut": "_documentai_79_GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn": "_documentai_80_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut": "_documentai_81_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut",
        "GoogleCloudDocumentaiV1beta2VertexIn": "_documentai_82_GoogleCloudDocumentaiV1beta2VertexIn",
        "GoogleCloudDocumentaiV1beta2VertexOut": "_documentai_83_GoogleCloudDocumentaiV1beta2VertexOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn": "_documentai_84_GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut": "_documentai_85_GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut",
        "GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn": "_documentai_86_GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn",
        "GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut": "_documentai_87_GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut",
        "GoogleCloudDocumentaiUiv1beta3RevisionRefIn": "_documentai_88_GoogleCloudDocumentaiUiv1beta3RevisionRefIn",
        "GoogleCloudDocumentaiUiv1beta3RevisionRefOut": "_documentai_89_GoogleCloudDocumentaiUiv1beta3RevisionRefOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn": "_documentai_90_GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut": "_documentai_91_GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut",
        "GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn": "_documentai_92_GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn",
        "GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut": "_documentai_93_GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut",
        "GoogleCloudDocumentaiV1BatchProcessRequestIn": "_documentai_94_GoogleCloudDocumentaiV1BatchProcessRequestIn",
        "GoogleCloudDocumentaiV1BatchProcessRequestOut": "_documentai_95_GoogleCloudDocumentaiV1BatchProcessRequestOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn": "_documentai_96_GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut": "_documentai_97_GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut",
        "GoogleCloudDocumentaiV1beta2ProcessDocumentResponseIn": "_documentai_98_GoogleCloudDocumentaiV1beta2ProcessDocumentResponseIn",
        "GoogleCloudDocumentaiV1beta2ProcessDocumentResponseOut": "_documentai_99_GoogleCloudDocumentaiV1beta2ProcessDocumentResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageIn": "_documentai_100_GoogleCloudDocumentaiV1beta2DocumentPageIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageOut": "_documentai_101_GoogleCloudDocumentaiV1beta2DocumentPageOut",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn": "_documentai_102_GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut": "_documentai_103_GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut",
        "GoogleCloudDocumentaiV1beta2GcsDestinationIn": "_documentai_104_GoogleCloudDocumentaiV1beta2GcsDestinationIn",
        "GoogleCloudDocumentaiV1beta2GcsDestinationOut": "_documentai_105_GoogleCloudDocumentaiV1beta2GcsDestinationOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn": "_documentai_106_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut": "_documentai_107_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn": "_documentai_108_GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut": "_documentai_109_GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn": "_documentai_110_GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut": "_documentai_111_GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta2OperationMetadataIn": "_documentai_112_GoogleCloudDocumentaiV1beta2OperationMetadataIn",
        "GoogleCloudDocumentaiV1beta2OperationMetadataOut": "_documentai_113_GoogleCloudDocumentaiV1beta2OperationMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceIn": "_documentai_114_GoogleCloudDocumentaiV1beta2DocumentProvenanceIn",
        "GoogleCloudDocumentaiV1beta2DocumentProvenanceOut": "_documentai_115_GoogleCloudDocumentaiV1beta2DocumentProvenanceOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageLineIn": "_documentai_116_GoogleCloudDocumentaiV1beta2DocumentPageLineIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageLineOut": "_documentai_117_GoogleCloudDocumentaiV1beta2DocumentPageLineOut",
        "GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn": "_documentai_118_GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn",
        "GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut": "_documentai_119_GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut",
        "GoogleCloudLocationLocationIn": "_documentai_120_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_documentai_121_GoogleCloudLocationLocationOut",
        "GoogleTypePostalAddressIn": "_documentai_122_GoogleTypePostalAddressIn",
        "GoogleTypePostalAddressOut": "_documentai_123_GoogleTypePostalAddressOut",
        "GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataIn": "_documentai_124_GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataIn",
        "GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataOut": "_documentai_125_GoogleCloudDocumentaiV1ReviewDocumentOperationMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataIn": "_documentai_126_GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataOut": "_documentai_127_GoogleCloudDocumentaiUiv1beta3UpdateLabelerPoolOperationMetadataOut",
        "GoogleCloudDocumentaiV1BatchProcessMetadataIn": "_documentai_128_GoogleCloudDocumentaiV1BatchProcessMetadataIn",
        "GoogleCloudDocumentaiV1BatchProcessMetadataOut": "_documentai_129_GoogleCloudDocumentaiV1BatchProcessMetadataOut",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseIn": "_documentai_130_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseOut": "_documentai_131_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta3EnableProcessorMetadataIn": "_documentai_132_GoogleCloudDocumentaiV1beta3EnableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1beta3EnableProcessorMetadataOut": "_documentai_133_GoogleCloudDocumentaiV1beta3EnableProcessorMetadataOut",
        "GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn": "_documentai_134_GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn",
        "GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut": "_documentai_135_GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut",
        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn": "_documentai_136_GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn",
        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut": "_documentai_137_GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataIn": "_documentai_138_GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataOut": "_documentai_139_GoogleCloudDocumentaiV1beta3DeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta3DisableProcessorMetadataIn": "_documentai_140_GoogleCloudDocumentaiV1beta3DisableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1beta3DisableProcessorMetadataOut": "_documentai_141_GoogleCloudDocumentaiV1beta3DisableProcessorMetadataOut",
        "GoogleTypeMoneyIn": "_documentai_142_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_documentai_143_GoogleTypeMoneyOut",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataIn": "_documentai_144_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataOut": "_documentai_145_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn": "_documentai_146_GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn",
        "GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut": "_documentai_147_GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataIn": "_documentai_148_GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataIn",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataOut": "_documentai_149_GoogleCloudDocumentaiV1beta3DeleteProcessorMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn": "_documentai_150_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut": "_documentai_151_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn": "_documentai_152_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut": "_documentai_153_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut",
        "GoogleCloudDocumentaiV1beta1DocumentShardInfoIn": "_documentai_154_GoogleCloudDocumentaiV1beta1DocumentShardInfoIn",
        "GoogleCloudDocumentaiV1beta1DocumentShardInfoOut": "_documentai_155_GoogleCloudDocumentaiV1beta1DocumentShardInfoOut",
        "GoogleCloudDocumentaiV1DocumentStyleIn": "_documentai_156_GoogleCloudDocumentaiV1DocumentStyleIn",
        "GoogleCloudDocumentaiV1DocumentStyleOut": "_documentai_157_GoogleCloudDocumentaiV1DocumentStyleOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn": "_documentai_158_GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut": "_documentai_159_GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn": "_documentai_160_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut": "_documentai_161_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn": "_documentai_162_GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut": "_documentai_163_GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenIn": "_documentai_164_GoogleCloudDocumentaiV1beta1DocumentPageTokenIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenOut": "_documentai_165_GoogleCloudDocumentaiV1beta1DocumentPageTokenOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn": "_documentai_166_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut": "_documentai_167_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn": "_documentai_168_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn",
        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut": "_documentai_169_GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn": "_documentai_170_GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut": "_documentai_171_GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1ProcessorTypeIn": "_documentai_172_GoogleCloudDocumentaiV1ProcessorTypeIn",
        "GoogleCloudDocumentaiV1ProcessorTypeOut": "_documentai_173_GoogleCloudDocumentaiV1ProcessorTypeOut",
        "GoogleCloudDocumentaiV1DocumentRevisionIn": "_documentai_174_GoogleCloudDocumentaiV1DocumentRevisionIn",
        "GoogleCloudDocumentaiV1DocumentRevisionOut": "_documentai_175_GoogleCloudDocumentaiV1DocumentRevisionOut",
        "GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn": "_documentai_176_GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn",
        "GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut": "_documentai_177_GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataIn": "_documentai_178_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataOut": "_documentai_179_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentEntityRelationIn": "_documentai_180_GoogleCloudDocumentaiV1DocumentEntityRelationIn",
        "GoogleCloudDocumentaiV1DocumentEntityRelationOut": "_documentai_181_GoogleCloudDocumentaiV1DocumentEntityRelationOut",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataIn": "_documentai_182_GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataOut": "_documentai_183_GoogleCloudDocumentaiV1beta3DeleteProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn": "_documentai_184_GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn",
        "GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut": "_documentai_185_GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut",
        "GoogleCloudDocumentaiV1beta1VertexIn": "_documentai_186_GoogleCloudDocumentaiV1beta1VertexIn",
        "GoogleCloudDocumentaiV1beta1VertexOut": "_documentai_187_GoogleCloudDocumentaiV1beta1VertexOut",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionIn": "_documentai_188_GoogleCloudDocumentaiV1beta2DocumentRevisionIn",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionOut": "_documentai_189_GoogleCloudDocumentaiV1beta2DocumentRevisionOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn": "_documentai_190_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut": "_documentai_191_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut",
        "GoogleCloudDocumentaiV1DocumentTextChangeIn": "_documentai_192_GoogleCloudDocumentaiV1DocumentTextChangeIn",
        "GoogleCloudDocumentaiV1DocumentTextChangeOut": "_documentai_193_GoogleCloudDocumentaiV1DocumentTextChangeOut",
        "GoogleLongrunningOperationIn": "_documentai_194_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_documentai_195_GoogleLongrunningOperationOut",
        "GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataIn": "_documentai_196_GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataOut": "_documentai_197_GoogleCloudDocumentaiUiv1beta3UpdateDatasetOperationMetadataOut",
        "GoogleCloudDocumentaiV1DocumentTextAnchorIn": "_documentai_198_GoogleCloudDocumentaiV1DocumentTextAnchorIn",
        "GoogleCloudDocumentaiV1DocumentTextAnchorOut": "_documentai_199_GoogleCloudDocumentaiV1DocumentTextAnchorOut",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn": "_documentai_200_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut": "_documentai_201_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut",
        "GoogleCloudDocumentaiV1DocumentPageTableTableRowIn": "_documentai_202_GoogleCloudDocumentaiV1DocumentPageTableTableRowIn",
        "GoogleCloudDocumentaiV1DocumentPageTableTableRowOut": "_documentai_203_GoogleCloudDocumentaiV1DocumentPageTableTableRowOut",
        "GoogleCloudDocumentaiV1EvaluationMetricsIn": "_documentai_204_GoogleCloudDocumentaiV1EvaluationMetricsIn",
        "GoogleCloudDocumentaiV1EvaluationMetricsOut": "_documentai_205_GoogleCloudDocumentaiV1EvaluationMetricsOut",
        "GoogleCloudDocumentaiV1beta1GcsSourceIn": "_documentai_206_GoogleCloudDocumentaiV1beta1GcsSourceIn",
        "GoogleCloudDocumentaiV1beta1GcsSourceOut": "_documentai_207_GoogleCloudDocumentaiV1beta1GcsSourceOut",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusIn": "_documentai_208_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusIn",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusOut": "_documentai_209_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatusOut",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn": "_documentai_210_GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut": "_documentai_211_GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseIn": "_documentai_212_GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseIn",
        "GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseOut": "_documentai_213_GoogleCloudDocumentaiV1beta2BatchProcessDocumentsResponseOut",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn": "_documentai_214_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut": "_documentai_215_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataIn": "_documentai_216_GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataOut": "_documentai_217_GoogleCloudDocumentaiUiv1beta3EnableProcessorMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn": "_documentai_218_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut": "_documentai_219_GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta3BatchProcessResponseIn": "_documentai_220_GoogleCloudDocumentaiV1beta3BatchProcessResponseIn",
        "GoogleCloudDocumentaiV1beta3BatchProcessResponseOut": "_documentai_221_GoogleCloudDocumentaiV1beta3BatchProcessResponseOut",
        "GoogleCloudDocumentaiV1ListProcessorsResponseIn": "_documentai_222_GoogleCloudDocumentaiV1ListProcessorsResponseIn",
        "GoogleCloudDocumentaiV1ListProcessorsResponseOut": "_documentai_223_GoogleCloudDocumentaiV1ListProcessorsResponseOut",
        "GoogleCloudDocumentaiV1CommonOperationMetadataIn": "_documentai_224_GoogleCloudDocumentaiV1CommonOperationMetadataIn",
        "GoogleCloudDocumentaiV1CommonOperationMetadataOut": "_documentai_225_GoogleCloudDocumentaiV1CommonOperationMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseIn": "_documentai_226_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseOut": "_documentai_227_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta1BarcodeIn": "_documentai_228_GoogleCloudDocumentaiV1beta1BarcodeIn",
        "GoogleCloudDocumentaiV1beta1BarcodeOut": "_documentai_229_GoogleCloudDocumentaiV1beta1BarcodeOut",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn": "_documentai_230_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut": "_documentai_231_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn": "_documentai_232_GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn",
        "GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut": "_documentai_233_GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta1NormalizedVertexIn": "_documentai_234_GoogleCloudDocumentaiV1beta1NormalizedVertexIn",
        "GoogleCloudDocumentaiV1beta1NormalizedVertexOut": "_documentai_235_GoogleCloudDocumentaiV1beta1NormalizedVertexOut",
        "GoogleCloudDocumentaiV1beta1DocumentTextChangeIn": "_documentai_236_GoogleCloudDocumentaiV1beta1DocumentTextChangeIn",
        "GoogleCloudDocumentaiV1beta1DocumentTextChangeOut": "_documentai_237_GoogleCloudDocumentaiV1beta1DocumentTextChangeOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn": "_documentai_238_GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut": "_documentai_239_GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut",
        "GoogleProtobufEmptyIn": "_documentai_240_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_documentai_241_GoogleProtobufEmptyOut",
        "GoogleCloudDocumentaiV1DocumentPageVisualElementIn": "_documentai_242_GoogleCloudDocumentaiV1DocumentPageVisualElementIn",
        "GoogleCloudDocumentaiV1DocumentPageVisualElementOut": "_documentai_243_GoogleCloudDocumentaiV1DocumentPageVisualElementOut",
        "GoogleCloudDocumentaiV1ProcessorIn": "_documentai_244_GoogleCloudDocumentaiV1ProcessorIn",
        "GoogleCloudDocumentaiV1ProcessorOut": "_documentai_245_GoogleCloudDocumentaiV1ProcessorOut",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdIn": "_documentai_246_GoogleCloudDocumentaiUiv1beta3DocumentIdIn",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdOut": "_documentai_247_GoogleCloudDocumentaiUiv1beta3DocumentIdOut",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn": "_documentai_248_GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut": "_documentai_249_GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut",
        "GoogleCloudDocumentaiV1DisableProcessorRequestIn": "_documentai_250_GoogleCloudDocumentaiV1DisableProcessorRequestIn",
        "GoogleCloudDocumentaiV1DisableProcessorRequestOut": "_documentai_251_GoogleCloudDocumentaiV1DisableProcessorRequestOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn": "_documentai_252_GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut": "_documentai_253_GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn": "_documentai_254_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut": "_documentai_255_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut",
        "GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn": "_documentai_256_GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn",
        "GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut": "_documentai_257_GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn": "_documentai_258_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut": "_documentai_259_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIn": "_documentai_260_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataOut": "_documentai_261_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataOut",
        "GoogleCloudDocumentaiV1beta2OutputConfigIn": "_documentai_262_GoogleCloudDocumentaiV1beta2OutputConfigIn",
        "GoogleCloudDocumentaiV1beta2OutputConfigOut": "_documentai_263_GoogleCloudDocumentaiV1beta2OutputConfigOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn": "_documentai_264_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut": "_documentai_265_GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn": "_documentai_266_GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut": "_documentai_267_GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut",
        "GoogleTypeTimeZoneIn": "_documentai_268_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_documentai_269_GoogleTypeTimeZoneOut",
        "GoogleCloudDocumentaiV1ListProcessorTypesResponseIn": "_documentai_270_GoogleCloudDocumentaiV1ListProcessorTypesResponseIn",
        "GoogleCloudDocumentaiV1ListProcessorTypesResponseOut": "_documentai_271_GoogleCloudDocumentaiV1ListProcessorTypesResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn": "_documentai_272_GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn",
        "GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut": "_documentai_273_GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn": "_documentai_274_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut": "_documentai_275_GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn": "_documentai_276_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut": "_documentai_277_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn": "_documentai_278_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut": "_documentai_279_GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageTokenIn": "_documentai_280_GoogleCloudDocumentaiV1DocumentPageTokenIn",
        "GoogleCloudDocumentaiV1DocumentPageTokenOut": "_documentai_281_GoogleCloudDocumentaiV1DocumentPageTokenOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageBlockIn": "_documentai_282_GoogleCloudDocumentaiV1beta1DocumentPageBlockIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageBlockOut": "_documentai_283_GoogleCloudDocumentaiV1beta1DocumentPageBlockOut",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn": "_documentai_284_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut": "_documentai_285_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn": "_documentai_286_GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut": "_documentai_287_GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut",
        "GoogleCloudDocumentaiV1beta2NormalizedVertexIn": "_documentai_288_GoogleCloudDocumentaiV1beta2NormalizedVertexIn",
        "GoogleCloudDocumentaiV1beta2NormalizedVertexOut": "_documentai_289_GoogleCloudDocumentaiV1beta2NormalizedVertexOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn": "_documentai_290_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut": "_documentai_291_GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1EvaluationCountersIn": "_documentai_292_GoogleCloudDocumentaiV1EvaluationCountersIn",
        "GoogleCloudDocumentaiV1EvaluationCountersOut": "_documentai_293_GoogleCloudDocumentaiV1EvaluationCountersOut",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn": "_documentai_294_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut": "_documentai_295_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1ProcessResponseIn": "_documentai_296_GoogleCloudDocumentaiV1ProcessResponseIn",
        "GoogleCloudDocumentaiV1ProcessResponseOut": "_documentai_297_GoogleCloudDocumentaiV1ProcessResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageTableIn": "_documentai_298_GoogleCloudDocumentaiV1DocumentPageTableIn",
        "GoogleCloudDocumentaiV1DocumentPageTableOut": "_documentai_299_GoogleCloudDocumentaiV1DocumentPageTableOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn": "_documentai_300_GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut": "_documentai_301_GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn": "_documentai_302_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut": "_documentai_303_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn": "_documentai_304_GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut": "_documentai_305_GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut",
        "GoogleCloudDocumentaiV1ProcessRequestIn": "_documentai_306_GoogleCloudDocumentaiV1ProcessRequestIn",
        "GoogleCloudDocumentaiV1ProcessRequestOut": "_documentai_307_GoogleCloudDocumentaiV1ProcessRequestOut",
        "GoogleCloudDocumentaiV1beta1DocumentStyleIn": "_documentai_308_GoogleCloudDocumentaiV1beta1DocumentStyleIn",
        "GoogleCloudDocumentaiV1beta1DocumentStyleOut": "_documentai_309_GoogleCloudDocumentaiV1beta1DocumentStyleOut",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataIn": "_documentai_310_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataOut": "_documentai_311_GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn": "_documentai_312_GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut": "_documentai_313_GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut",
        "GoogleCloudDocumentaiV1beta1GcsDestinationIn": "_documentai_314_GoogleCloudDocumentaiV1beta1GcsDestinationIn",
        "GoogleCloudDocumentaiV1beta1GcsDestinationOut": "_documentai_315_GoogleCloudDocumentaiV1beta1GcsDestinationOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn": "_documentai_316_GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut": "_documentai_317_GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut",
        "GoogleCloudDocumentaiV1DocumentOutputConfigIn": "_documentai_318_GoogleCloudDocumentaiV1DocumentOutputConfigIn",
        "GoogleCloudDocumentaiV1DocumentOutputConfigOut": "_documentai_319_GoogleCloudDocumentaiV1DocumentOutputConfigOut",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataIn": "_documentai_320_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataOut": "_documentai_321_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn": "_documentai_322_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut": "_documentai_323_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageBlockIn": "_documentai_324_GoogleCloudDocumentaiV1DocumentPageBlockIn",
        "GoogleCloudDocumentaiV1DocumentPageBlockOut": "_documentai_325_GoogleCloudDocumentaiV1DocumentPageBlockOut",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataIn": "_documentai_326_GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataOut": "_documentai_327_GoogleCloudDocumentaiV1EvaluateProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageIn": "_documentai_328_GoogleCloudDocumentaiV1beta2DocumentPageImageIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageOut": "_documentai_329_GoogleCloudDocumentaiV1beta2DocumentPageImageOut",
        "GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn": "_documentai_330_GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn",
        "GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut": "_documentai_331_GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn": "_documentai_332_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn",
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut": "_documentai_333_GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn": "_documentai_334_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut": "_documentai_335_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn": "_documentai_336_GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut": "_documentai_337_GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1DocumentProvenanceIn": "_documentai_338_GoogleCloudDocumentaiV1DocumentProvenanceIn",
        "GoogleCloudDocumentaiV1DocumentProvenanceOut": "_documentai_339_GoogleCloudDocumentaiV1DocumentProvenanceOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn": "_documentai_340_GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut": "_documentai_341_GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut",
        "GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn": "_documentai_342_GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn",
        "GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut": "_documentai_343_GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseIn": "_documentai_344_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseOut": "_documentai_345_GoogleCloudDocumentaiUiv1beta3SetDefaultProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataIn": "_documentai_346_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataOut": "_documentai_347_GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataIn": "_documentai_348_GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataOut": "_documentai_349_GoogleCloudDocumentaiUiv1beta3UpdateHumanReviewConfigMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn": "_documentai_350_GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut": "_documentai_351_GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn": "_documentai_352_GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut": "_documentai_353_GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataIn": "_documentai_354_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataOut": "_documentai_355_GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn": "_documentai_356_GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn",
        "GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut": "_documentai_357_GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn": "_documentai_358_GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut": "_documentai_359_GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn": "_documentai_360_GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut": "_documentai_361_GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceIn": "_documentai_362_GoogleCloudDocumentaiV1beta1DocumentProvenanceIn",
        "GoogleCloudDocumentaiV1beta1DocumentProvenanceOut": "_documentai_363_GoogleCloudDocumentaiV1beta1DocumentProvenanceOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableIn": "_documentai_364_GoogleCloudDocumentaiV1beta1DocumentPageTableIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTableOut": "_documentai_365_GoogleCloudDocumentaiV1beta1DocumentPageTableOut",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn": "_documentai_366_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut": "_documentai_367_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn": "_documentai_368_GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut": "_documentai_369_GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageBlockIn": "_documentai_370_GoogleCloudDocumentaiV1beta2DocumentPageBlockIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageBlockOut": "_documentai_371_GoogleCloudDocumentaiV1beta2DocumentPageBlockOut",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsIn": "_documentai_372_GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsIn",
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsOut": "_documentai_373_GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsOut",
        "GoogleCloudDocumentaiV1DocumentEntityIn": "_documentai_374_GoogleCloudDocumentaiV1DocumentEntityIn",
        "GoogleCloudDocumentaiV1DocumentEntityOut": "_documentai_375_GoogleCloudDocumentaiV1DocumentEntityOut",
        "GoogleLongrunningListOperationsResponseIn": "_documentai_376_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_documentai_377_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn": "_documentai_378_GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut": "_documentai_379_GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn": "_documentai_380_GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut": "_documentai_381_GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn": "_documentai_382_GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn",
        "GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut": "_documentai_383_GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn": "_documentai_384_GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut": "_documentai_385_GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut",
        "GoogleCloudDocumentaiV1ListProcessorVersionsResponseIn": "_documentai_386_GoogleCloudDocumentaiV1ListProcessorVersionsResponseIn",
        "GoogleCloudDocumentaiV1ListProcessorVersionsResponseOut": "_documentai_387_GoogleCloudDocumentaiV1ListProcessorVersionsResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn": "_documentai_388_GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut": "_documentai_389_GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut",
        "GoogleCloudDocumentaiV1DocumentPageParagraphIn": "_documentai_390_GoogleCloudDocumentaiV1DocumentPageParagraphIn",
        "GoogleCloudDocumentaiV1DocumentPageParagraphOut": "_documentai_391_GoogleCloudDocumentaiV1DocumentPageParagraphOut",
        "GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn": "_documentai_392_GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn",
        "GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut": "_documentai_393_GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataIn": "_documentai_394_GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataOut": "_documentai_395_GoogleCloudDocumentaiUiv1beta3DeleteProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn": "_documentai_396_GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn",
        "GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut": "_documentai_397_GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseIn": "_documentai_398_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseOut": "_documentai_399_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1VertexIn": "_documentai_400_GoogleCloudDocumentaiV1VertexIn",
        "GoogleCloudDocumentaiV1VertexOut": "_documentai_401_GoogleCloudDocumentaiV1VertexOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn": "_documentai_402_GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut": "_documentai_403_GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut",
        "GoogleCloudDocumentaiV1beta1OperationMetadataIn": "_documentai_404_GoogleCloudDocumentaiV1beta1OperationMetadataIn",
        "GoogleCloudDocumentaiV1beta1OperationMetadataOut": "_documentai_405_GoogleCloudDocumentaiV1beta1OperationMetadataOut",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataIn": "_documentai_406_GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataOut": "_documentai_407_GoogleCloudDocumentaiV1UndeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1GcsPrefixIn": "_documentai_408_GoogleCloudDocumentaiV1GcsPrefixIn",
        "GoogleCloudDocumentaiV1GcsPrefixOut": "_documentai_409_GoogleCloudDocumentaiV1GcsPrefixOut",
        "GoogleCloudDocumentaiV1DocumentShardInfoIn": "_documentai_410_GoogleCloudDocumentaiV1DocumentShardInfoIn",
        "GoogleCloudDocumentaiV1DocumentShardInfoOut": "_documentai_411_GoogleCloudDocumentaiV1DocumentShardInfoOut",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataIn": "_documentai_412_GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataOut": "_documentai_413_GoogleCloudDocumentaiV1beta3ImportProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DeleteProcessorMetadataIn": "_documentai_414_GoogleCloudDocumentaiV1DeleteProcessorMetadataIn",
        "GoogleCloudDocumentaiV1DeleteProcessorMetadataOut": "_documentai_415_GoogleCloudDocumentaiV1DeleteProcessorMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn": "_documentai_416_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut": "_documentai_417_GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut",
        "GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn": "_documentai_418_GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn",
        "GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut": "_documentai_419_GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut",
        "GoogleCloudDocumentaiV1BoundingPolyIn": "_documentai_420_GoogleCloudDocumentaiV1BoundingPolyIn",
        "GoogleCloudDocumentaiV1BoundingPolyOut": "_documentai_421_GoogleCloudDocumentaiV1BoundingPolyOut",
        "GoogleCloudDocumentaiV1beta2DocumentIn": "_documentai_422_GoogleCloudDocumentaiV1beta2DocumentIn",
        "GoogleCloudDocumentaiV1beta2DocumentOut": "_documentai_423_GoogleCloudDocumentaiV1beta2DocumentOut",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionIn": "_documentai_424_GoogleCloudDocumentaiV1beta1DocumentRevisionIn",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionOut": "_documentai_425_GoogleCloudDocumentaiV1beta1DocumentRevisionOut",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataIn": "_documentai_426_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataOut": "_documentai_427_GoogleCloudDocumentaiUiv1beta3UndeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DeployProcessorVersionMetadataIn": "_documentai_428_GoogleCloudDocumentaiV1DeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1DeployProcessorVersionMetadataOut": "_documentai_429_GoogleCloudDocumentaiV1DeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn": "_documentai_430_GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut": "_documentai_431_GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut",
        "GoogleCloudDocumentaiV1DocumentPageAnchorIn": "_documentai_432_GoogleCloudDocumentaiV1DocumentPageAnchorIn",
        "GoogleCloudDocumentaiV1DocumentPageAnchorOut": "_documentai_433_GoogleCloudDocumentaiV1DocumentPageAnchorOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn": "_documentai_434_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut": "_documentai_435_GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut",
        "GoogleCloudDocumentaiV1EnableProcessorRequestIn": "_documentai_436_GoogleCloudDocumentaiV1EnableProcessorRequestIn",
        "GoogleCloudDocumentaiV1EnableProcessorRequestOut": "_documentai_437_GoogleCloudDocumentaiV1EnableProcessorRequestOut",
        "GoogleCloudDocumentaiV1FetchProcessorTypesResponseIn": "_documentai_438_GoogleCloudDocumentaiV1FetchProcessorTypesResponseIn",
        "GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut": "_documentai_439_GoogleCloudDocumentaiV1FetchProcessorTypesResponseOut",
        "GoogleCloudDocumentaiV1DisableProcessorMetadataIn": "_documentai_440_GoogleCloudDocumentaiV1DisableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1DisableProcessorMetadataOut": "_documentai_441_GoogleCloudDocumentaiV1DisableProcessorMetadataOut",
        "GoogleCloudDocumentaiV1ProcessorVersionIn": "_documentai_442_GoogleCloudDocumentaiV1ProcessorVersionIn",
        "GoogleCloudDocumentaiV1ProcessorVersionOut": "_documentai_443_GoogleCloudDocumentaiV1ProcessorVersionOut",
        "GoogleCloudDocumentaiV1beta1OutputConfigIn": "_documentai_444_GoogleCloudDocumentaiV1beta1OutputConfigIn",
        "GoogleCloudDocumentaiV1beta1OutputConfigOut": "_documentai_445_GoogleCloudDocumentaiV1beta1OutputConfigOut",
        "GoogleCloudDocumentaiV1HumanReviewStatusIn": "_documentai_446_GoogleCloudDocumentaiV1HumanReviewStatusIn",
        "GoogleCloudDocumentaiV1HumanReviewStatusOut": "_documentai_447_GoogleCloudDocumentaiV1HumanReviewStatusOut",
        "GoogleCloudDocumentaiV1beta2InputConfigIn": "_documentai_448_GoogleCloudDocumentaiV1beta2InputConfigIn",
        "GoogleCloudDocumentaiV1beta2InputConfigOut": "_documentai_449_GoogleCloudDocumentaiV1beta2InputConfigOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn": "_documentai_450_GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut": "_documentai_451_GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn": "_documentai_452_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn",
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut": "_documentai_453_GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn": "_documentai_454_GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut": "_documentai_455_GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1DocumentStyleFontSizeIn": "_documentai_456_GoogleCloudDocumentaiV1DocumentStyleFontSizeIn",
        "GoogleCloudDocumentaiV1DocumentStyleFontSizeOut": "_documentai_457_GoogleCloudDocumentaiV1DocumentStyleFontSizeOut",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentIn": "_documentai_458_GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentIn",
        "GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentOut": "_documentai_459_GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegmentOut",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn": "_documentai_460_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn",
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut": "_documentai_461_GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn": "_documentai_462_GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut": "_documentai_463_GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn": "_documentai_464_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn",
        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut": "_documentai_465_GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut",
        "GoogleCloudLocationListLocationsResponseIn": "_documentai_466_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_documentai_467_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudDocumentaiV1beta1DocumentEntityIn": "_documentai_468_GoogleCloudDocumentaiV1beta1DocumentEntityIn",
        "GoogleCloudDocumentaiV1beta1DocumentEntityOut": "_documentai_469_GoogleCloudDocumentaiV1beta1DocumentEntityOut",
        "GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataIn": "_documentai_470_GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataOut": "_documentai_471_GoogleCloudDocumentaiV1DeleteProcessorVersionMetadataOut",
        "GoogleTypeDateIn": "_documentai_472_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_documentai_473_GoogleTypeDateOut",
        "GoogleCloudDocumentaiV1RawDocumentIn": "_documentai_474_GoogleCloudDocumentaiV1RawDocumentIn",
        "GoogleCloudDocumentaiV1RawDocumentOut": "_documentai_475_GoogleCloudDocumentaiV1RawDocumentOut",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataIn": "_documentai_476_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataOut": "_documentai_477_GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn": "_documentai_478_GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn",
        "GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut": "_documentai_479_GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataIn": "_documentai_480_GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataOut": "_documentai_481_GoogleCloudDocumentaiUiv1beta3SampleDocumentsMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentIn": "_documentai_482_GoogleCloudDocumentaiV1beta1DocumentIn",
        "GoogleCloudDocumentaiV1beta1DocumentOut": "_documentai_483_GoogleCloudDocumentaiV1beta1DocumentOut",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataIn": "_documentai_484_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataOut": "_documentai_485_GoogleCloudDocumentaiUiv1beta3EvaluateProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn": "_documentai_486_GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut": "_documentai_487_GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataIn": "_documentai_488_GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataOut": "_documentai_489_GoogleCloudDocumentaiUiv1beta3DisableProcessorMetadataOut",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseIn": "_documentai_490_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseIn",
        "GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseOut": "_documentai_491_GoogleCloudDocumentaiUiv1beta3SampleDocumentsResponseOut",
        "GoogleCloudDocumentaiV1DocumentSchemaIn": "_documentai_492_GoogleCloudDocumentaiV1DocumentSchemaIn",
        "GoogleCloudDocumentaiV1DocumentSchemaOut": "_documentai_493_GoogleCloudDocumentaiV1DocumentSchemaOut",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn": "_documentai_494_GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut": "_documentai_495_GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1GcsDocumentsIn": "_documentai_496_GoogleCloudDocumentaiV1GcsDocumentsIn",
        "GoogleCloudDocumentaiV1GcsDocumentsOut": "_documentai_497_GoogleCloudDocumentaiV1GcsDocumentsOut",
        "GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn": "_documentai_498_GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn",
        "GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut": "_documentai_499_GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut",
        "GoogleCloudDocumentaiV1DocumentPageMatrixIn": "_documentai_500_GoogleCloudDocumentaiV1DocumentPageMatrixIn",
        "GoogleCloudDocumentaiV1DocumentPageMatrixOut": "_documentai_501_GoogleCloudDocumentaiV1DocumentPageMatrixOut",
        "GoogleCloudDocumentaiV1DocumentPageLayoutIn": "_documentai_502_GoogleCloudDocumentaiV1DocumentPageLayoutIn",
        "GoogleCloudDocumentaiV1DocumentPageLayoutOut": "_documentai_503_GoogleCloudDocumentaiV1DocumentPageLayoutOut",
        "GoogleCloudDocumentaiV1NormalizedVertexIn": "_documentai_504_GoogleCloudDocumentaiV1NormalizedVertexIn",
        "GoogleCloudDocumentaiV1NormalizedVertexOut": "_documentai_505_GoogleCloudDocumentaiV1NormalizedVertexOut",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn": "_documentai_506_GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut": "_documentai_507_GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataIn": "_documentai_508_GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataOut": "_documentai_509_GoogleCloudDocumentaiV1SetDefaultProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1EnableProcessorResponseIn": "_documentai_510_GoogleCloudDocumentaiV1EnableProcessorResponseIn",
        "GoogleCloudDocumentaiV1EnableProcessorResponseOut": "_documentai_511_GoogleCloudDocumentaiV1EnableProcessorResponseOut",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn": "_documentai_512_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut": "_documentai_513_GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentLabelIn": "_documentai_514_GoogleCloudDocumentaiV1beta2DocumentLabelIn",
        "GoogleCloudDocumentaiV1beta2DocumentLabelOut": "_documentai_515_GoogleCloudDocumentaiV1beta2DocumentLabelOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn": "_documentai_516_GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut": "_documentai_517_GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut",
        "GoogleCloudDocumentaiV1EvaluationIn": "_documentai_518_GoogleCloudDocumentaiV1EvaluationIn",
        "GoogleCloudDocumentaiV1EvaluationOut": "_documentai_519_GoogleCloudDocumentaiV1EvaluationOut",
        "GoogleCloudDocumentaiV1BarcodeIn": "_documentai_520_GoogleCloudDocumentaiV1BarcodeIn",
        "GoogleCloudDocumentaiV1BarcodeOut": "_documentai_521_GoogleCloudDocumentaiV1BarcodeOut",
        "GoogleCloudDocumentaiV1DocumentIn": "_documentai_522_GoogleCloudDocumentaiV1DocumentIn",
        "GoogleCloudDocumentaiV1DocumentOut": "_documentai_523_GoogleCloudDocumentaiV1DocumentOut",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataIn": "_documentai_524_GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataOut": "_documentai_525_GoogleCloudDocumentaiUiv1beta3DeleteProcessorMetadataOut",
        "GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn": "_documentai_526_GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn",
        "GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut": "_documentai_527_GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn": "_documentai_528_GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn",
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut": "_documentai_529_GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut",
        "GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentIn": "_documentai_530_GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentIn",
        "GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentOut": "_documentai_531_GoogleCloudDocumentaiV1DocumentTextAnchorTextSegmentOut",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn": "_documentai_532_GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn",
        "GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut": "_documentai_533_GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut",
        "GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn": "_documentai_534_GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut": "_documentai_535_GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageIn": "_documentai_536_GoogleCloudDocumentaiV1beta1DocumentPageImageIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageImageOut": "_documentai_537_GoogleCloudDocumentaiV1beta1DocumentPageImageOut",
        "GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn": "_documentai_538_GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn",
        "GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut": "_documentai_539_GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut",
        "GoogleRpcStatusIn": "_documentai_540_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_documentai_541_GoogleRpcStatusOut",
        "GoogleCloudDocumentaiV1DocumentPageIn": "_documentai_542_GoogleCloudDocumentaiV1DocumentPageIn",
        "GoogleCloudDocumentaiV1DocumentPageOut": "_documentai_543_GoogleCloudDocumentaiV1DocumentPageOut",
        "GoogleCloudDocumentaiV1ReviewDocumentRequestIn": "_documentai_544_GoogleCloudDocumentaiV1ReviewDocumentRequestIn",
        "GoogleCloudDocumentaiV1ReviewDocumentRequestOut": "_documentai_545_GoogleCloudDocumentaiV1ReviewDocumentRequestOut",
        "GoogleCloudDocumentaiV1beta2BoundingPolyIn": "_documentai_546_GoogleCloudDocumentaiV1beta2BoundingPolyIn",
        "GoogleCloudDocumentaiV1beta2BoundingPolyOut": "_documentai_547_GoogleCloudDocumentaiV1beta2BoundingPolyOut",
        "GoogleCloudDocumentaiV1beta2DocumentStyleIn": "_documentai_548_GoogleCloudDocumentaiV1beta2DocumentStyleIn",
        "GoogleCloudDocumentaiV1beta2DocumentStyleOut": "_documentai_549_GoogleCloudDocumentaiV1beta2DocumentStyleOut",
        "GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn": "_documentai_550_GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn",
        "GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut": "_documentai_551_GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut",
        "GoogleCloudDocumentaiV1BatchProcessResponseIn": "_documentai_552_GoogleCloudDocumentaiV1BatchProcessResponseIn",
        "GoogleCloudDocumentaiV1BatchProcessResponseOut": "_documentai_553_GoogleCloudDocumentaiV1BatchProcessResponseOut",
        "GoogleCloudDocumentaiV1GcsDocumentIn": "_documentai_554_GoogleCloudDocumentaiV1GcsDocumentIn",
        "GoogleCloudDocumentaiV1GcsDocumentOut": "_documentai_555_GoogleCloudDocumentaiV1GcsDocumentOut",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn": "_documentai_556_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn",
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut": "_documentai_557_GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut",
        "GoogleCloudDocumentaiV1beta2DocumentShardInfoIn": "_documentai_558_GoogleCloudDocumentaiV1beta2DocumentShardInfoIn",
        "GoogleCloudDocumentaiV1beta2DocumentShardInfoOut": "_documentai_559_GoogleCloudDocumentaiV1beta2DocumentShardInfoOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn": "_documentai_560_GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut": "_documentai_561_GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn": "_documentai_562_GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut": "_documentai_563_GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn": "_documentai_564_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn",
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut": "_documentai_565_GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut",
        "GoogleCloudDocumentaiV1DocumentPageLineIn": "_documentai_566_GoogleCloudDocumentaiV1DocumentPageLineIn",
        "GoogleCloudDocumentaiV1DocumentPageLineOut": "_documentai_567_GoogleCloudDocumentaiV1DocumentPageLineOut",
        "GoogleCloudDocumentaiV1ListEvaluationsResponseIn": "_documentai_568_GoogleCloudDocumentaiV1ListEvaluationsResponseIn",
        "GoogleCloudDocumentaiV1ListEvaluationsResponseOut": "_documentai_569_GoogleCloudDocumentaiV1ListEvaluationsResponseOut",
        "GoogleCloudDocumentaiV1beta2DocumentEntityIn": "_documentai_570_GoogleCloudDocumentaiV1beta2DocumentEntityIn",
        "GoogleCloudDocumentaiV1beta2DocumentEntityOut": "_documentai_571_GoogleCloudDocumentaiV1beta2DocumentEntityOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn": "_documentai_572_GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut": "_documentai_573_GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut",
        "GoogleCloudDocumentaiV1DocumentPageTableTableCellIn": "_documentai_574_GoogleCloudDocumentaiV1DocumentPageTableTableCellIn",
        "GoogleCloudDocumentaiV1DocumentPageTableTableCellOut": "_documentai_575_GoogleCloudDocumentaiV1DocumentPageTableTableCellOut",
        "GoogleCloudDocumentaiV1DocumentPageFormFieldIn": "_documentai_576_GoogleCloudDocumentaiV1DocumentPageFormFieldIn",
        "GoogleCloudDocumentaiV1DocumentPageFormFieldOut": "_documentai_577_GoogleCloudDocumentaiV1DocumentPageFormFieldOut",
        "GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn": "_documentai_578_GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn",
        "GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut": "_documentai_579_GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableIn": "_documentai_580_GoogleCloudDocumentaiV1beta2DocumentPageTableIn",
        "GoogleCloudDocumentaiV1beta2DocumentPageTableOut": "_documentai_581_GoogleCloudDocumentaiV1beta2DocumentPageTableOut",
        "GoogleCloudDocumentaiV1EnableProcessorMetadataIn": "_documentai_582_GoogleCloudDocumentaiV1EnableProcessorMetadataIn",
        "GoogleCloudDocumentaiV1EnableProcessorMetadataOut": "_documentai_583_GoogleCloudDocumentaiV1EnableProcessorMetadataOut",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataIn": "_documentai_584_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataIn",
        "GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataOut": "_documentai_585_GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionMetadataOut",
        "GoogleCloudDocumentaiV1DocumentProvenanceParentIn": "_documentai_586_GoogleCloudDocumentaiV1DocumentProvenanceParentIn",
        "GoogleCloudDocumentaiV1DocumentProvenanceParentOut": "_documentai_587_GoogleCloudDocumentaiV1DocumentProvenanceParentOut",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdIn": "_documentai_588_GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdIn",
        "GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdOut": "_documentai_589_GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdOut",
        "GoogleCloudDocumentaiV1beta2DocumentTextChangeIn": "_documentai_590_GoogleCloudDocumentaiV1beta2DocumentTextChangeIn",
        "GoogleCloudDocumentaiV1beta2DocumentTextChangeOut": "_documentai_591_GoogleCloudDocumentaiV1beta2DocumentTextChangeOut",
        "GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataIn": "_documentai_592_GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataIn",
        "GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataOut": "_documentai_593_GoogleCloudDocumentaiUiv1beta3DeleteLabelerPoolOperationMetadataOut",
        "GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn": "_documentai_594_GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn",
        "GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut": "_documentai_595_GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn"] = t.struct(
        {
            "inputData": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataIn"
                ]
            ).optional(),
            "customDocumentExtractionOptions": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsIn"
                ]
            ).optional(),
            "processorVersion": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionIn"]
            ),
            "baseProcessorVersion": t.string().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut"] = t.struct(
        {
            "inputData": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionRequestInputDataOut"
                ]
            ).optional(),
            "customDocumentExtractionOptions": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsOut"
                ]
            ).optional(),
            "processorVersion": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionOut"]
            ),
            "baseProcessorVersion": t.string().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionRequestOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenIn"] = t.struct(
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
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenOut"] = t.struct(
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
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn"] = t.struct(
        {
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "correctedKeyText": t.string().optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "correctedValueText": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut"] = t.struct(
        {
            "nameDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "correctedKeyText": t.string().optional(),
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "correctedValueText": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut"])
    types["GoogleCloudDocumentaiV1DisableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1DisableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorResponseOut"])
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
    types["GoogleCloudDocumentaiV1DocumentSchemaMetadataIn"] = t.struct(
        {
            "prefixedNamingOnProperties": t.boolean().optional(),
            "documentAllowMultipleLabels": t.boolean().optional(),
            "skipNamingValidation": t.boolean().optional(),
            "documentSplitter": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaMetadataOut"] = t.struct(
        {
            "prefixedNamingOnProperties": t.boolean().optional(),
            "documentAllowMultipleLabels": t.boolean().optional(),
            "skipNamingValidation": t.boolean().optional(),
            "documentSplitter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataOut"])
    types["GoogleCloudDocumentaiV1beta2BarcodeIn"] = t.struct(
        {
            "format": t.string().optional(),
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BarcodeIn"])
    types["GoogleCloudDocumentaiV1beta2BarcodeOut"] = t.struct(
        {
            "format": t.string().optional(),
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2BarcodeOut"])
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
    types["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3TrainProcessorVersionResponseOut"])
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
    types["GoogleTypeColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["GoogleTypeColorIn"])
    types["GoogleTypeColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeColorOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "inputGcsSource": t.string().optional(),
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
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "inputGcsSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut"
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
    types["GoogleCloudDocumentaiV1DocumentPageImageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "width": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageIn"])
    types["GoogleCloudDocumentaiV1DocumentPageImageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageOut"])
    types["GoogleCloudDocumentaiV1beta2GcsSourceIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsSourceIn"])
    types["GoogleCloudDocumentaiV1beta2GcsSourceOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsSourceOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "id": t.integer().optional(),
            "index": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "id": t.integer().optional(),
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut"])
    types["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DeployProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn"] = t.struct(
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
            "rowSpan": t.integer().optional(),
            "colSpan": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut"] = t.struct(
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
            "rowSpan": t.integer().optional(),
            "colSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableCellOut"])
    types["GoogleCloudDocumentaiV1ReviewDocumentResponseIn"] = t.struct(
        {
            "gcsDestination": t.string().optional(),
            "state": t.string().optional(),
            "rejectionReason": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentResponseIn"])
    types["GoogleCloudDocumentaiV1ReviewDocumentResponseOut"] = t.struct(
        {
            "gcsDestination": t.string().optional(),
            "state": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentResponseOut"])
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
    types["GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn"] = t.struct(
        {
            "rows": t.integer().optional(),
            "cols": t.integer().optional(),
            "type": t.integer().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut"] = t.struct(
        {
            "rows": t.integer().optional(),
            "cols": t.integer().optional(),
            "type": t.integer().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn"] = t.struct(
        {
            "floatValue": t.number().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "text": t.string().optional(),
            "integerValue": t.integer().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "booleanValue": t.boolean().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressIn"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut"] = t.struct(
        {
            "floatValue": t.number().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "text": t.string().optional(),
            "integerValue": t.integer().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "booleanValue": t.boolean().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut"])
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
            "individualBatchDeleteStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusIn"
                    ]
                )
            ).optional(),
            "errorDocumentCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
            "individualBatchDeleteStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataIndividualBatchDeleteStatusOut"
                    ]
                )
            ).optional(),
            "errorDocumentCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiV1beta3HumanReviewStatusIn"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusIn"])
    types["GoogleCloudDocumentaiV1beta3HumanReviewStatusOut"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusOut"])
    types["GoogleCloudDocumentaiV1DocumentPageSymbolIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageSymbolIn"])
    types["GoogleCloudDocumentaiV1DocumentPageSymbolOut"] = t.struct(
        {
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
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageSymbolOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageIn"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldIn"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn"]
                )
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn"])
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn"]
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixIn"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeIn"]
                )
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn"]
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableIn"])
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenIn"])
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineIn"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageOut"] = t.struct(
        {
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageFormFieldOut"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut"]
                )
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut"])
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut"]
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageMatrixOut"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedBarcodeOut"
                    ]
                )
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut"]
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableOut"])
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenOut"])
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineOut"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageOut"])
    types["GoogleTypeDateTimeIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "year": t.integer().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
            "hours": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateTimeIn"])
    types["GoogleTypeDateTimeOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "year": t.integer().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "hours": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateTimeOut"])
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
    types["GoogleCloudDocumentaiV1beta1DocumentPageLineIn"] = t.struct(
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
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageLineOut"] = t.struct(
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
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLineOut"])
    types[
        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "inputGcsSource": t.string().optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusIn"]
            ).optional(),
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
            "inputGcsSource": t.string().optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusOut"]
            ).optional(),
            "outputGcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut"]
    )
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
    types["GoogleCloudDocumentaiV1EvaluationReferenceIn"] = t.struct(
        {
            "aggregateMetricsExact": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsIn"]
            ).optional(),
            "evaluation": t.string().optional(),
            "operation": t.string().optional(),
            "aggregateMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationReferenceIn"])
    types["GoogleCloudDocumentaiV1EvaluationReferenceOut"] = t.struct(
        {
            "aggregateMetricsExact": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsOut"]
            ).optional(),
            "evaluation": t.string().optional(),
            "operation": t.string().optional(),
            "aggregateMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMetricsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationReferenceOut"])
    types["GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DisableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DisableProcessorResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn"] = t.struct(
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
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut"] = t.struct(
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyIn"]
            ).optional(),
            "orientation": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"] = t.struct(
        {
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyOut"]
            ).optional(),
            "orientation": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"])
    types["GoogleCloudDocumentaiV1DocumentPageDimensionIn"] = t.struct(
        {
            "height": t.number().optional(),
            "unit": t.string().optional(),
            "width": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDimensionIn"])
    types["GoogleCloudDocumentaiV1DocumentPageDimensionOut"] = t.struct(
        {
            "height": t.number().optional(),
            "unit": t.string().optional(),
            "width": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDimensionOut"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionRequestOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusIn"
    ] = t.struct(
        {
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
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
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"]
            ).optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "outputGcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIndividualExportStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1beta2VertexIn"] = t.struct(
        {"x": t.integer().optional(), "y": t.integer().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2VertexIn"])
    types["GoogleCloudDocumentaiV1beta2VertexOut"] = t.struct(
        {
            "x": t.integer().optional(),
            "y": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2VertexOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "correctedValueText": t.string().optional(),
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
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "correctedKeyText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "correctedValueText": t.string().optional(),
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
            "fieldValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "correctedKeyText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut"])
    types["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn"])
    types["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut"])
    types["GoogleCloudDocumentaiUiv1beta3RevisionRefIn"] = t.struct(
        {
            "revisionCase": t.string().optional(),
            "latestProcessorVersion": t.string().optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3RevisionRefIn"])
    types["GoogleCloudDocumentaiUiv1beta3RevisionRefOut"] = t.struct(
        {
            "revisionCase": t.string().optional(),
            "latestProcessorVersion": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3RevisionRefOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn"] = t.struct(
        {
            "fontWeight": t.integer().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "pixelFontSize": t.number().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontSize": t.integer().optional(),
            "bold": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "subscript": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "fontType": t.string().optional(),
            "italic": t.boolean().optional(),
            "smallcaps": t.boolean().optional(),
            "superscript": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "strikeout": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut"] = t.struct(
        {
            "fontWeight": t.integer().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "pixelFontSize": t.number().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontSize": t.integer().optional(),
            "bold": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "subscript": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "fontType": t.string().optional(),
            "italic": t.boolean().optional(),
            "smallcaps": t.boolean().optional(),
            "superscript": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "strikeout": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut"])
    types["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn"] = t.struct(
        {
            "moneyValue": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "floatValue": t.number().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "booleanValue": t.boolean().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "text": t.string().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressIn"]).optional(),
            "integerValue": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn"])
    types["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut"] = t.struct(
        {
            "moneyValue": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "floatValue": t.number().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "booleanValue": t.boolean().optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "text": t.string().optional(),
            "addressValue": t.proxy(renames["GoogleTypePostalAddressOut"]).optional(),
            "integerValue": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut"])
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
    types["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn"] = t.struct(
        {
            "type": t.string().optional(),
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
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut"] = t.struct(
        {
            "type": t.string().optional(),
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
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageVisualElementOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentPageIn"] = t.struct(
        {
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineIn"])
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolIn"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockIn"])
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableIn"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn"])
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementIn"]
                )
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresIn"]
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldIn"])
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn"]
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageIn"]
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageOut"] = t.struct(
        {
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineOut"])
            ).optional(),
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageSymbolOut"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockOut"])
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableOut"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut"])
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedBarcodeOut"
                    ]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "visualElements": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageVisualElementOut"]
                )
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresOut"]
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageFormFieldOut"])
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut"]
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageImageOut"]
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageOut"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn"] = t.struct(
        {
            "gcsDestination": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseIn"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut"] = t.struct(
        {
            "gcsDestination": t.string().optional(),
            "rejectionReason": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentResponseOut"])
    types["GoogleCloudDocumentaiV1beta2GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsDestinationIn"])
    types["GoogleCloudDocumentaiV1beta2GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2GcsDestinationOut"])
    types[
        "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn"
    ] = t.struct(
        {
            "documentErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "documentErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "datasetErrorCount": t.integer().optional(),
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
            "documentErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "documentErrors": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "datasetErrorCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut"
        ]
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
    types["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ImportProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta2OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta2OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OperationMetadataOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "type": t.string().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentIn"]
                )
            ).optional(),
            "id": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "type": t.string().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceParentOut"]
                )
            ).optional(),
            "id": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageLineIn"] = t.struct(
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
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageLineOut"] = t.struct(
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
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLineOut"])
    types["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"] = t.struct(
        {
            "gcsPrefix": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsPrefixIn"]
            ).optional(),
            "gcsDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsDocumentsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"])
    types["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"] = t.struct(
        {
            "gcsPrefix": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsPrefixOut"]
            ).optional(),
            "gcsDocuments": t.proxy(
                renames["GoogleCloudDocumentaiV1GcsDocumentsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigOut"])
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
    types["GoogleTypePostalAddressIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "addressLines": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
        }
    ).named(renames["GoogleTypePostalAddressIn"])
    types["GoogleTypePostalAddressOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "addressLines": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypePostalAddressOut"])
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
    types["GoogleCloudDocumentaiV1BatchProcessMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusIn"
                    ]
                )
            ).optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessMetadataIn"])
    types["GoogleCloudDocumentaiV1BatchProcessMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1BatchProcessMetadataIndividualProcessStatusOut"
                    ]
                )
            ).optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessMetadataOut"])
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
    types["GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3EnableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3EnableProcessorResponseOut"])
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
    types["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"] = t.struct(
        {"confidence": t.number().optional(), "languageCode": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"])
    types["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"])
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
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchDeleteDocumentsResponseOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn"
    ] = t.struct(
        {
            "splitType": t.string().optional(),
            "totalDocumentCount": t.integer().optional(),
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
            "splitType": t.string().optional(),
            "totalDocumentCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut"
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
    types["GoogleCloudDocumentaiV1DocumentStyleIn"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontFamily": t.string().optional(),
            "fontWeight": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeIn"]
            ).optional(),
            "textStyle": t.string().optional(),
            "textDecoration": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorIn"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleIn"])
    types["GoogleCloudDocumentaiV1DocumentStyleOut"] = t.struct(
        {
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontFamily": t.string().optional(),
            "fontWeight": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeOut"]
            ).optional(),
            "textStyle": t.string().optional(),
            "textDecoration": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleOut"])
    types["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ResyncDatasetResponseOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "inputGcsSource": t.string().optional(),
            "outputGcsDestination": t.string().optional(),
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
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "inputGcsSource": t.string().optional(),
            "outputGcsDestination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIndividualImportStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyIn"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
            "orientation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyOut"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "orientation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenStyleInfoOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageOut"
                    ]
                )
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut"]
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenOut"])
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
    types["GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1ProcessorTypeIn"] = t.struct(
        {
            "sampleDocumentUris": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "category": t.string().optional(),
            "allowCreation": t.boolean().optional(),
            "availableLocations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoIn"])
            ).optional(),
            "launchStage": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeIn"])
    types["GoogleCloudDocumentaiV1ProcessorTypeOut"] = t.struct(
        {
            "sampleDocumentUris": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "category": t.string().optional(),
            "allowCreation": t.boolean().optional(),
            "availableLocations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeLocationInfoOut"])
            ).optional(),
            "launchStage": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorTypeOut"])
    types["GoogleCloudDocumentaiV1DocumentRevisionIn"] = t.struct(
        {
            "parentIds": t.array(t.string()).optional(),
            "processor": t.string().optional(),
            "agent": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "id": t.string().optional(),
            "createTime": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentRevisionIn"])
    types["GoogleCloudDocumentaiV1DocumentRevisionOut"] = t.struct(
        {
            "parentIds": t.array(t.string()).optional(),
            "processor": t.string().optional(),
            "agent": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "id": t.string().optional(),
            "createTime": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentRevisionHumanReviewOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentRevisionOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn"] = t.struct(
        {
            "pixelFontSize": t.number().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "superscript": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "smallcaps": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "letterSpacing": t.number().optional(),
            "strikeout": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "fontWeight": t.integer().optional(),
            "subscript": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "fontType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut"] = t.struct(
        {
            "pixelFontSize": t.number().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "superscript": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "italic": t.boolean().optional(),
            "smallcaps": t.boolean().optional(),
            "bold": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "letterSpacing": t.number().optional(),
            "strikeout": t.boolean().optional(),
            "fontSize": t.integer().optional(),
            "fontWeight": t.integer().optional(),
            "subscript": t.boolean().optional(),
            "handwritten": t.boolean().optional(),
            "fontType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut"])
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
    types["GoogleCloudDocumentaiV1DocumentEntityRelationIn"] = t.struct(
        {
            "relation": t.string().optional(),
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityRelationIn"])
    types["GoogleCloudDocumentaiV1DocumentEntityRelationOut"] = t.struct(
        {
            "relation": t.string().optional(),
            "objectId": t.string().optional(),
            "subjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityRelationOut"])
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
    types["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn"] = t.struct(
        {
            "barcode": t.proxy(renames["GoogleCloudDocumentaiV1BarcodeIn"]).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn"])
    types["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut"] = t.struct(
        {
            "barcode": t.proxy(renames["GoogleCloudDocumentaiV1BarcodeOut"]).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "agent": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn"]
            ).optional(),
            "id": t.string().optional(),
            "processor": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "parent": t.array(t.integer()).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "agent": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut"]
            ).optional(),
            "id": t.string().optional(),
            "processor": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "parent": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "documentInconsistencyType": t.string().optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"]
            ).optional(),
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
            "documentInconsistencyType": t.string().optional(),
            "documentId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataIndividualDocumentResyncStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentTextChangeIn"] = t.struct(
        {
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextChangeIn"])
    types["GoogleCloudDocumentaiV1DocumentTextChangeOut"] = t.struct(
        {
            "changedText": t.string().optional(),
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentTextChangeOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types[
        "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationIn"
    ] = t.struct(
        {
            "documentErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "datasetErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "documentErrorCount": t.integer().optional(),
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
            "documentErrors": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "datasetErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "documentErrorCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidationOut"
        ]
    )
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
    types["GoogleCloudDocumentaiV1EvaluationMetricsIn"] = t.struct(
        {
            "groundTruthOccurrencesCount": t.integer().optional(),
            "falsePositivesCount": t.integer().optional(),
            "predictedOccurrencesCount": t.integer().optional(),
            "precision": t.number().optional(),
            "totalDocumentsCount": t.integer().optional(),
            "falseNegativesCount": t.integer().optional(),
            "predictedDocumentCount": t.integer().optional(),
            "truePositivesCount": t.integer().optional(),
            "groundTruthDocumentCount": t.integer().optional(),
            "f1Score": t.number().optional(),
            "recall": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMetricsIn"])
    types["GoogleCloudDocumentaiV1EvaluationMetricsOut"] = t.struct(
        {
            "groundTruthOccurrencesCount": t.integer().optional(),
            "falsePositivesCount": t.integer().optional(),
            "predictedOccurrencesCount": t.integer().optional(),
            "precision": t.number().optional(),
            "totalDocumentsCount": t.integer().optional(),
            "falseNegativesCount": t.integer().optional(),
            "predictedDocumentCount": t.integer().optional(),
            "truePositivesCount": t.integer().optional(),
            "groundTruthDocumentCount": t.integer().optional(),
            "f1Score": t.number().optional(),
            "recall": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMetricsOut"])
    types["GoogleCloudDocumentaiV1beta1GcsSourceIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsSourceIn"])
    types["GoogleCloudDocumentaiV1beta1GcsSourceOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsSourceOut"])
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
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionResponseOut"])
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
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn"] = t.struct(
        {
            "totalDocumentCount": t.integer().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
            "individualAutoLabelStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut"] = t.struct(
        {
            "totalDocumentCount": t.integer().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
            "individualAutoLabelStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataOut"])
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
    types["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessResponseIn"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessResponseOut"])
    types["GoogleCloudDocumentaiV1ListProcessorsResponseIn"] = t.struct(
        {
            "processors": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorsResponseIn"])
    types["GoogleCloudDocumentaiV1ListProcessorsResponseOut"] = t.struct(
        {
            "processors": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1ProcessorOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListProcessorsResponseOut"])
    types["GoogleCloudDocumentaiV1CommonOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"])
    types["GoogleCloudDocumentaiV1CommonOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"])
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
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsResponseOut"])
    types["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3EnableProcessorResponseOut"])
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
    types["GoogleCloudDocumentaiV1beta1DocumentTextChangeIn"] = t.struct(
        {
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"])
            ).optional(),
            "changedText": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentTextChangeOut"] = t.struct(
        {
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"])
            ).optional(),
            "changedText": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDocumentaiV1DocumentPageVisualElementIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementIn"])
    types["GoogleCloudDocumentaiV1DocumentPageVisualElementOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementOut"])
    types["GoogleCloudDocumentaiV1ProcessorIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "defaultProcessorVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorIn"])
    types["GoogleCloudDocumentaiV1ProcessorOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "defaultProcessorVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "processEndpoint": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorOut"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"] = t.struct(
        {
            "unmanagedDocId": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdIn"]
            ).optional(),
            "gcsManagedDocId": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn"
                ]
            ).optional(),
            "revisionRef": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3RevisionRefIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdIn"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"] = t.struct(
        {
            "unmanagedDocId": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdOut"
                ]
            ).optional(),
            "gcsManagedDocId": t.proxy(
                renames[
                    "GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut"
                ]
            ).optional(),
            "revisionRef": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3RevisionRefOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn"] = t.struct(
        {"startIndex": t.string().optional(), "endIndex": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut"] = t.struct(
        {
            "startIndex": t.string().optional(),
            "endIndex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorTextSegmentOut"])
    types["GoogleCloudDocumentaiV1DisableProcessorRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorRequestIn"])
    types["GoogleCloudDocumentaiV1DisableProcessorRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DisableProcessorRequestOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn"] = t.struct(
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
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut"] = t.struct(
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageParagraphOut"])
    types["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn"] = t.struct(
        {
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn"
                    ]
                )
            ).optional(),
            "qualityScore": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn"])
    types["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut"] = t.struct(
        {
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut"
                    ]
                )
            ).optional(),
            "qualityScore": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut"])
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
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn"] = t.struct(
        {"processorVersion": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut"] = t.struct(
        {
            "processorVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionResponseOut"])
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
    types["GoogleCloudDocumentaiV1beta2OutputConfigIn"] = t.struct(
        {
            "pagesPerShard": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsDestinationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OutputConfigIn"])
    types["GoogleCloudDocumentaiV1beta2OutputConfigOut"] = t.struct(
        {
            "pagesPerShard": t.integer().optional(),
            "gcsDestination": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsDestinationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2OutputConfigOut"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn"] = t.struct(
        {
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataIn"]
            ).optional(),
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut"] = t.struct(
        {
            "trainingDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1CommonOperationMetadataOut"]
            ).optional(),
            "testDatasetValidation": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1TrainProcessorVersionMetadataDatasetValidationOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1TrainProcessorVersionMetadataOut"])
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
    types["GoogleTypeTimeZoneIn"] = t.struct(
        {"id": t.string().optional(), "version": t.string().optional()}
    ).named(renames["GoogleTypeTimeZoneIn"])
    types["GoogleTypeTimeZoneOut"] = t.struct(
        {
            "id": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeTimeZoneOut"])
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
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn"] = t.struct(
        {
            "splitExportStats": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatIn"
                    ]
                )
            ).optional(),
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
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut"] = t.struct(
        {
            "splitExportStats": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataSplitExportStatOut"
                    ]
                )
            ).optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"]
            ).optional(),
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
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut"] = t.struct(
        {
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"]
            ).optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn"] = t.struct(
        {
            "destSplitType": t.string().optional(),
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
            "destDatasetType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut"] = t.struct(
        {
            "destSplitType": t.string().optional(),
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
            "destDatasetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "styleInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenStyleInfoOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "detectedBreak": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageBlockIn"] = t.struct(
        {
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
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageBlockOut"] = t.struct(
        {
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
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageBlockOut"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn"] = t.struct(
        {"values": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn"] = t.struct(
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
            "rowSpan": t.integer().optional(),
            "colSpan": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut"] = t.struct(
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
            "rowSpan": t.integer().optional(),
            "colSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableCellOut"])
    types["GoogleCloudDocumentaiV1beta2NormalizedVertexIn"] = t.struct(
        {"x": t.number().optional(), "y": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2NormalizedVertexIn"])
    types["GoogleCloudDocumentaiV1beta2NormalizedVertexOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2NormalizedVertexOut"])
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn"] = t.struct(
        {
            "importConfigValidationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultIn"
                    ]
                )
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
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
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut"] = t.struct(
        {
            "importConfigValidationResults": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataImportConfigValidationResultOut"
                    ]
                )
            ).optional(),
            "totalDocumentCount": t.integer().optional(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsMetadataOut"])
    types["GoogleCloudDocumentaiV1EvaluationCountersIn"] = t.struct(
        {
            "inputDocumentsCount": t.integer().optional(),
            "failedDocumentsCount": t.integer().optional(),
            "invalidDocumentsCount": t.integer().optional(),
            "evaluatedDocumentsCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationCountersIn"])
    types["GoogleCloudDocumentaiV1EvaluationCountersOut"] = t.struct(
        {
            "inputDocumentsCount": t.integer().optional(),
            "failedDocumentsCount": t.integer().optional(),
            "invalidDocumentsCount": t.integer().optional(),
            "evaluatedDocumentsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationCountersOut"])
    types["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn"] = t.struct(
        {"gcsUri": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut"] = t.struct(
        {
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1ProcessResponseIn"] = t.struct(
        {
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusIn"]
            ).optional(),
            "document": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessResponseIn"])
    types["GoogleCloudDocumentaiV1ProcessResponseOut"] = t.struct(
        {
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1HumanReviewStatusOut"]
            ).optional(),
            "document": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentPageTableIn"] = t.struct(
        {
            "bodyRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowIn"])
            ).optional(),
            "headerRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowIn"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTableOut"] = t.struct(
        {
            "bodyRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowOut"])
            ).optional(),
            "headerRows": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableTableRowOut"])
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableOut"])
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
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn"] = t.struct(
        {
            "qualityScore": t.number().optional(),
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut"] = t.struct(
        {
            "qualityScore": t.number().optional(),
            "detectedDefects": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresDetectedDefectOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageQualityScoresOut"])
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
    types["GoogleCloudDocumentaiV1ProcessRequestIn"] = t.struct(
        {
            "fieldMask": t.string().optional(),
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentIn"]
            ).optional(),
            "skipHumanReview": t.boolean().optional(),
            "rawDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1RawDocumentIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessRequestIn"])
    types["GoogleCloudDocumentaiV1ProcessRequestOut"] = t.struct(
        {
            "fieldMask": t.string().optional(),
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOut"]
            ).optional(),
            "skipHumanReview": t.boolean().optional(),
            "rawDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1RawDocumentOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessRequestOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentStyleIn"] = t.struct(
        {
            "textStyle": t.string().optional(),
            "fontFamily": t.string().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeIn"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
            "fontWeight": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorIn"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentStyleIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentStyleOut"] = t.struct(
        {
            "textStyle": t.string().optional(),
            "fontFamily": t.string().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentStyleFontSizeOut"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "fontWeight": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentStyleOut"])
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
    types["GoogleCloudDocumentaiV1beta1GcsDestinationIn"] = t.struct(
        {"uri": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsDestinationIn"])
    types["GoogleCloudDocumentaiV1beta1GcsDestinationOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1GcsDestinationOut"])
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
    types["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn"] = t.struct(
        {"evaluation": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut"] = t.struct(
        {
            "evaluation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentPageBlockIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageBlockIn"])
    types["GoogleCloudDocumentaiV1DocumentPageBlockOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageBlockOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentPageImageIn"] = t.struct(
        {
            "content": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageImageIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageImageOut"] = t.struct(
        {
            "content": t.string().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageImageOut"])
    types["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1InputConfigIn"]
            ).optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1OutputConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseIn"])
    types["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut"] = t.struct(
        {
            "inputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1InputConfigOut"]
            ).optional(),
            "outputConfig": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1OutputConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1ProcessDocumentResponseOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "datasetInconsistencyType": t.string().optional(),
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
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "datasetInconsistencyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3ResyncDatasetMetadataDatasetResyncStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn"] = t.struct(
        {
            "shardingConfig": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn"
                ]
            ).optional(),
            "fieldMask": t.string().optional(),
            "gcsUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigIn"])
    types["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut"] = t.struct(
        {
            "shardingConfig": t.proxy(
                renames[
                    "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut"
                ]
            ).optional(),
            "fieldMask": t.string().optional(),
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigOut"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1UndeployProcessorVersionRequestOut"])
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
    types["GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn"] = t.struct(
        {
            "height": t.number().optional(),
            "width": t.number().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut"] = t.struct(
        {
            "height": t.number().optional(),
            "width": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageDimensionOut"])
    types["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn"] = t.struct(
        {
            "cols": t.integer().optional(),
            "rows": t.integer().optional(),
            "data": t.string().optional(),
            "type": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut"] = t.struct(
        {
            "cols": t.integer().optional(),
            "rows": t.integer().optional(),
            "data": t.string().optional(),
            "type": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageMatrixOut"])
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ImportDocumentsResponseOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn"] = t.struct(
        {"stateMessage": t.string().optional(), "state": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionHumanReviewOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
            "id": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "index": t.integer().optional(),
            "id": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut"])
    types["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DisableProcessorResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "id": t.integer().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentIn"]
                )
            ).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "id": t.integer().optional(),
            "parents": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceParentOut"]
                )
            ).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableIn"] = t.struct(
        {
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
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowIn"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTableOut"] = t.struct(
        {
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
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentPageTableTableRowOut"]
                )
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTableOut"])
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsResponseOut"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "individualProcessStatuses": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3BatchProcessMetadataOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageBlockIn"] = t.struct(
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
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageBlockOut"] = t.struct(
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
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageBlockOut"])
    types[
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsIn"
    ] = t.struct({"trainingMethod": t.string().optional()}).named(
        renames[
            "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsOut"
    ] = t.struct(
        {
            "trainingMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1TrainProcessorVersionRequestCustomDocumentExtractionOptionsOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentEntityIn"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "type": t.string(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueIn"]
            ).optional(),
            "id": t.string().optional(),
            "mentionText": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityIn"])
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageAnchorIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "mentionId": t.string().optional(),
            "redacted": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityIn"])
    types["GoogleCloudDocumentaiV1DocumentEntityOut"] = t.struct(
        {
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "type": t.string(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentEntityNormalizedValueOut"]
            ).optional(),
            "id": t.string().optional(),
            "mentionText": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityOut"])
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageAnchorOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "mentionId": t.string().optional(),
            "redacted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentEntityOut"])
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
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "name": t.string().optional(),
            "occurrenceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "name": t.string().optional(),
            "occurrenceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn"] = t.struct(
        {"defaultProcessorVersion": t.string()}
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestIn"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut"] = t.struct(
        {
            "defaultProcessorVersion": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequestOut"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataIn"]
            ).optional(),
            "stateMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "questionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "commonMetadata": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3CommonOperationMetadataOut"]
            ).optional(),
            "stateMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "questionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadataOut"])
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseIn"])
    types["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3ExportDocumentsResponseOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn"] = t.struct(
        {
            "fontSize": t.integer().optional(),
            "strikeout": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "fontType": t.string().optional(),
            "pixelFontSize": t.number().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "handwritten": t.boolean().optional(),
            "superscript": t.boolean().optional(),
            "subscript": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "bold": t.boolean().optional(),
            "fontWeight": t.integer().optional(),
            "smallcaps": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut"] = t.struct(
        {
            "fontSize": t.integer().optional(),
            "strikeout": t.boolean().optional(),
            "underlined": t.boolean().optional(),
            "fontType": t.string().optional(),
            "pixelFontSize": t.number().optional(),
            "italic": t.boolean().optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "handwritten": t.boolean().optional(),
            "superscript": t.boolean().optional(),
            "subscript": t.boolean().optional(),
            "letterSpacing": t.number().optional(),
            "textColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "bold": t.boolean().optional(),
            "fontWeight": t.integer().optional(),
            "smallcaps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenStyleInfoOut"])
    types["GoogleCloudDocumentaiV1DocumentPageParagraphIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageParagraphIn"])
    types["GoogleCloudDocumentaiV1DocumentPageParagraphOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
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
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageParagraphOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn"] = t.struct(
        {
            "objectId": t.string().optional(),
            "relation": t.string().optional(),
            "subjectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut"] = t.struct(
        {
            "objectId": t.string().optional(),
            "relation": t.string().optional(),
            "subjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut"])
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
    types["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn"] = t.struct(
        {
            "layoutId": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyIn"]
            ).optional(),
            "layoutType": t.string().optional(),
            "confidence": t.number().optional(),
            "page": t.string(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefIn"])
    types["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut"] = t.struct(
        {
            "layoutId": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyOut"]
            ).optional(),
            "layoutType": t.string().optional(),
            "confidence": t.number().optional(),
            "page": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageAnchorPageRefOut"])
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
    types["GoogleCloudDocumentaiV1VertexIn"] = t.struct(
        {"y": t.integer().optional(), "x": t.integer().optional()}
    ).named(renames["GoogleCloudDocumentaiV1VertexIn"])
    types["GoogleCloudDocumentaiV1VertexOut"] = t.struct(
        {
            "y": t.integer().optional(),
            "x": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1VertexOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta1DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut"] = t.struct(
        {
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
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
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageParagraphOut"])
    types["GoogleCloudDocumentaiV1beta1OperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1OperationMetadataIn"])
    types["GoogleCloudDocumentaiV1beta1OperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1OperationMetadataOut"])
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
    types["GoogleCloudDocumentaiV1GcsPrefixIn"] = t.struct(
        {"gcsUriPrefix": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1GcsPrefixIn"])
    types["GoogleCloudDocumentaiV1GcsPrefixOut"] = t.struct(
        {
            "gcsUriPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1GcsPrefixOut"])
    types["GoogleCloudDocumentaiV1DocumentShardInfoIn"] = t.struct(
        {
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
            "textOffset": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentShardInfoIn"])
    types["GoogleCloudDocumentaiV1DocumentShardInfoOut"] = t.struct(
        {
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
            "textOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentShardInfoOut"])
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
    types["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreakOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentIn"] = t.struct(
        {
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeIn"])
            ).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionIn"])
            ).optional(),
            "labels": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentLabelIn"])
            ).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageIn"])
            ).optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentStyleIn"])
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoIn"]
            ).optional(),
            "text": t.string().optional(),
            "mimeType": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityIn"])
            ).optional(),
            "uri": t.string().optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn"])
            ).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentOut"] = t.struct(
        {
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentRevisionOut"])
            ).optional(),
            "labels": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentLabelOut"])
            ).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentPageOut"])
            ).optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentStyleOut"])
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoOut"]
            ).optional(),
            "text": t.string().optional(),
            "mimeType": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityOut"])
            ).optional(),
            "uri": t.string().optional(),
            "entityRelations": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut"]
                )
            ).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentRevisionIn"] = t.struct(
        {
            "id": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewIn"]
            ).optional(),
            "processor": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "agent": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentRevisionOut"] = t.struct(
        {
            "id": t.string().optional(),
            "humanReview": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentRevisionHumanReviewOut"]
            ).optional(),
            "processor": t.string().optional(),
            "parentIds": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "parent": t.array(t.integer()).optional(),
            "agent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTokenDetectedBreakOut"])
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
    types[
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn"
    ] = t.struct(
        {"confidence": t.number().optional(), "type": t.string().optional()}
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectIn"
        ]
    )
    types[
        "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut"
    ] = t.struct(
        {
            "confidence": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta2DocumentPageImageQualityScoresDetectedDefectOut"
        ]
    )
    types["GoogleCloudDocumentaiV1EnableProcessorRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorRequestIn"])
    types["GoogleCloudDocumentaiV1EnableProcessorRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorRequestOut"])
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
    types["GoogleCloudDocumentaiV1ProcessorVersionIn"] = t.struct(
        {
            "googleManaged": t.boolean().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "displayName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "latestEvaluation": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationReferenceIn"]
            ).optional(),
            "name": t.string().optional(),
            "deprecationInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoIn"]
            ).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorVersionIn"])
    types["GoogleCloudDocumentaiV1ProcessorVersionOut"] = t.struct(
        {
            "googleManaged": t.boolean().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaOut"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "displayName": t.string().optional(),
            "kmsKeyVersionName": t.string().optional(),
            "latestEvaluation": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationReferenceOut"]
            ).optional(),
            "name": t.string().optional(),
            "deprecationInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1ProcessorVersionDeprecationInfoOut"]
            ).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ProcessorVersionOut"])
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
    types["GoogleCloudDocumentaiV1HumanReviewStatusIn"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1HumanReviewStatusIn"])
    types["GoogleCloudDocumentaiV1HumanReviewStatusOut"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "humanReviewOperation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1HumanReviewStatusOut"])
    types["GoogleCloudDocumentaiV1beta2InputConfigIn"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsSourceIn"]
            ).optional(),
            "mimeType": t.string(),
            "contents": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2InputConfigIn"])
    types["GoogleCloudDocumentaiV1beta2InputConfigOut"] = t.struct(
        {
            "gcsSource": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2GcsSourceOut"]
            ).optional(),
            "mimeType": t.string(),
            "contents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2InputConfigOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "height": t.number().optional(),
            "width": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "height": t.number().optional(),
            "width": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageDimensionOut"])
    types[
        "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationIn"
    ] = t.struct(
        {
            "documentErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "documentErrors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
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
            "documentErrorCount": t.integer().optional(),
            "datasetErrors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "documentErrors": t.array(
                t.proxy(renames["GoogleRpcStatusOut"])
            ).optional(),
            "datasetErrorCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidationOut"
        ]
    )
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn"] = t.struct(
        {"evaluation": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut"] = t.struct(
        {
            "evaluation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluateProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1DocumentStyleFontSizeIn"] = t.struct(
        {"unit": t.string().optional(), "size": t.number().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeIn"])
    types["GoogleCloudDocumentaiV1DocumentStyleFontSizeOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "size": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentStyleFontSizeOut"])
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
    types[
        "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigIn"
    ] = t.struct(
        {
            "pagesOverlap": t.integer().optional(),
            "pagesPerShard": t.integer().optional(),
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
            "pagesOverlap": t.integer().optional(),
            "pagesPerShard": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1DocumentOutputConfigGcsOutputConfigShardingConfigOut"
        ]
    )
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
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn"] = t.struct(
        {
            "enumValues": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "baseTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "properties": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut"] = t.struct(
        {
            "enumValues": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeEnumValuesOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "baseTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "properties": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1DocumentSchemaEntityTypePropertyOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut"])
    types["GoogleCloudLocationListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseIn"])
    types["GoogleCloudLocationListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityIn"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceIn"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorIn"]
            ).optional(),
            "mentionText": t.string().optional(),
            "redacted": t.boolean().optional(),
            "type": t.string(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityIn"])
            ).optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueIn"]
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorIn"]
            ).optional(),
            "id": t.string().optional(),
            "confidence": t.number().optional(),
            "mentionId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentEntityOut"] = t.struct(
        {
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentProvenanceOut"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentTextAnchorOut"]
            ).optional(),
            "mentionText": t.string().optional(),
            "redacted": t.boolean().optional(),
            "type": t.string(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityOut"])
            ).optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValueOut"]
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorOut"]
            ).optional(),
            "id": t.string().optional(),
            "confidence": t.number().optional(),
            "mentionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentEntityOut"])
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
    types["GoogleCloudDocumentaiV1RawDocumentIn"] = t.struct(
        {"mimeType": t.string().optional(), "content": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1RawDocumentIn"])
    types["GoogleCloudDocumentaiV1RawDocumentOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1RawDocumentOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn"] = t.struct(
        {
            "addressValue": t.proxy(renames["GoogleTypePostalAddressIn"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "floatValue": t.number().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "booleanValue": t.boolean().optional(),
            "integerValue": t.integer().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut"] = t.struct(
        {
            "addressValue": t.proxy(renames["GoogleTypePostalAddressOut"]).optional(),
            "dateValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "floatValue": t.number().optional(),
            "datetimeValue": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "moneyValue": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "booleanValue": t.boolean().optional(),
            "integerValue": t.integer().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut"])
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
    types["GoogleCloudDocumentaiV1beta1DocumentIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageIn"])
            ).optional(),
            "uri": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentStyleIn"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeIn"])
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionIn"])
            ).optional(),
            "content": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityIn"])
            ).optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationIn"])
            ).optional(),
            "mimeType": t.string().optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentShardInfoIn"]
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentPageOut"])
            ).optional(),
            "uri": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentStyleOut"])
            ).optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentTextChangeOut"])
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentRevisionOut"])
            ).optional(),
            "content": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta1DocumentEntityOut"])
            ).optional(),
            "entityRelations": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta1DocumentEntityRelationOut"]
                )
            ).optional(),
            "mimeType": t.string().optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1DocumentShardInfoOut"]
            ).optional(),
            "text": t.string().optional(),
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
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageTokenDetectedBreakOut"])
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
    types["GoogleCloudDocumentaiV1DocumentSchemaIn"] = t.struct(
        {
            "description": t.string().optional(),
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaIn"])
    types["GoogleCloudDocumentaiV1DocumentSchemaOut"] = t.struct(
        {
            "description": t.string().optional(),
            "entityTypes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentSchemaEntityTypeOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentSchemaOut"])
    types["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3DeployProcessorVersionResponseOut"])
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
    types["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn"] = t.struct(
        {
            "estimatedCalibrationErrorExact": t.number().optional(),
            "auprcExact": t.number().optional(),
            "auprc": t.number().optional(),
            "confidenceLevelMetrics": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn"]
                )
            ).optional(),
            "metricsType": t.string().optional(),
            "confidenceLevelMetricsExact": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsIn"]
                )
            ).optional(),
            "estimatedCalibrationError": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn"])
    types["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut"] = t.struct(
        {
            "estimatedCalibrationErrorExact": t.number().optional(),
            "auprcExact": t.number().optional(),
            "auprc": t.number().optional(),
            "confidenceLevelMetrics": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut"
                    ]
                )
            ).optional(),
            "metricsType": t.string().optional(),
            "confidenceLevelMetricsExact": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1EvaluationConfidenceLevelMetricsOut"
                    ]
                )
            ).optional(),
            "estimatedCalibrationError": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut"])
    types["GoogleCloudDocumentaiV1DocumentPageMatrixIn"] = t.struct(
        {
            "type": t.integer().optional(),
            "cols": t.integer().optional(),
            "rows": t.integer().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageMatrixIn"])
    types["GoogleCloudDocumentaiV1DocumentPageMatrixOut"] = t.struct(
        {
            "type": t.integer().optional(),
            "cols": t.integer().optional(),
            "rows": t.integer().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageMatrixOut"])
    types["GoogleCloudDocumentaiV1DocumentPageLayoutIn"] = t.struct(
        {
            "orientation": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyIn"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"])
    types["GoogleCloudDocumentaiV1DocumentPageLayoutOut"] = t.struct(
        {
            "orientation": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1BoundingPolyOut"]
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentTextAnchorOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"])
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
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn"] = t.struct(
        {"cwDocId": t.string().optional(), "gcsUri": t.string()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdIn"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut"] = t.struct(
        {
            "cwDocId": t.string().optional(),
            "gcsUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdGCSManagedDocumentIdOut"])
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
    types["GoogleCloudDocumentaiV1EnableProcessorResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorResponseIn"])
    types["GoogleCloudDocumentaiV1EnableProcessorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1EnableProcessorResponseOut"])
    types["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1beta3UndeployProcessorVersionResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentLabelIn"] = t.struct(
        {
            "automlModel": t.string().optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentLabelIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentLabelOut"] = t.struct(
        {
            "automlModel": t.string().optional(),
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentLabelOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn"] = t.struct(
        {
            "layoutType": t.string().optional(),
            "confidence": t.number().optional(),
            "layoutId": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyIn"]
            ).optional(),
            "page": t.string(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut"] = t.struct(
        {
            "layoutType": t.string().optional(),
            "confidence": t.number().optional(),
            "layoutId": t.string().optional(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta1BoundingPolyOut"]
            ).optional(),
            "page": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageAnchorPageRefOut"])
    types["GoogleCloudDocumentaiV1EvaluationIn"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "entityMetrics": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyVersionName": t.string().optional(),
            "documentCounters": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationCountersIn"]
            ).optional(),
            "allEntitiesMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationIn"])
    types["GoogleCloudDocumentaiV1EvaluationOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "entityMetrics": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyVersionName": t.string().optional(),
            "documentCounters": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationCountersOut"]
            ).optional(),
            "allEntitiesMetrics": t.proxy(
                renames["GoogleCloudDocumentaiV1EvaluationMultiConfidenceMetricsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1EvaluationOut"])
    types["GoogleCloudDocumentaiV1BarcodeIn"] = t.struct(
        {
            "format": t.string().optional(),
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BarcodeIn"])
    types["GoogleCloudDocumentaiV1BarcodeOut"] = t.struct(
        {
            "format": t.string().optional(),
            "valueFormat": t.string().optional(),
            "rawValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1BarcodeOut"])
    types["GoogleCloudDocumentaiV1DocumentIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "mimeType": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityIn"])
            ).optional(),
            "uri": t.string().optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentTextChangeIn"])
            ).optional(),
            "content": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentStyleIn"])
            ).optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityRelationIn"])
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentShardInfoIn"]
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentRevisionIn"])
            ).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageIn"])
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentIn"])
    types["GoogleCloudDocumentaiV1DocumentOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "mimeType": t.string().optional(),
            "entities": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityOut"])
            ).optional(),
            "uri": t.string().optional(),
            "textChanges": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentTextChangeOut"])
            ).optional(),
            "content": t.string().optional(),
            "textStyles": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentStyleOut"])
            ).optional(),
            "entityRelations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentEntityRelationOut"])
            ).optional(),
            "shardInfo": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentShardInfoOut"]
            ).optional(),
            "revisions": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentRevisionOut"])
            ).optional(),
            "pages": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageOut"])
            ).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn"] = t.struct(
        {
            "relation": t.string().optional(),
            "subjectId": t.string().optional(),
            "objectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut"] = t.struct(
        {
            "relation": t.string().optional(),
            "subjectId": t.string().optional(),
            "objectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityRelationOut"])
    types[
        "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusIn"
    ] = t.struct(
        {
            "outputGcsDestination": t.string().optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusIn"]
            ).optional(),
            "inputGcsSource": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "humanReviewOperation": t.string().optional(),
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
            "outputGcsDestination": t.string().optional(),
            "humanReviewStatus": t.proxy(
                renames["GoogleCloudDocumentaiV1beta3HumanReviewStatusOut"]
            ).optional(),
            "inputGcsSource": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "humanReviewOperation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatusOut"
        ]
    )
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
    types["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataIn"])
    types["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiUiv1beta3CommonOperationMetadataOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageIn"] = t.struct(
        {
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageImageOut"] = t.struct(
        {
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "mimeType": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageImageOut"])
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
    types["GoogleCloudDocumentaiV1DocumentPageIn"] = t.struct(
        {
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageMatrixIn"])
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTokenIn"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageSymbolIn"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageIn"]
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageLineIn"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageParagraphIn"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeIn"])
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "visualElements": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementIn"])
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageDimensionIn"]
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresIn"]
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldIn"])
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableIn"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageBlockIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageIn"])
    types["GoogleCloudDocumentaiV1DocumentPageOut"] = t.struct(
        {
            "transforms": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageMatrixOut"])
            ).optional(),
            "tokens": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTokenOut"])
            ).optional(),
            "pageNumber": t.integer().optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "symbols": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageSymbolOut"])
            ).optional(),
            "image": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageOut"]
            ).optional(),
            "lines": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageLineOut"])
            ).optional(),
            "paragraphs": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageParagraphOut"])
            ).optional(),
            "detectedBarcodes": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedBarcodeOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "visualElements": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageVisualElementOut"])
            ).optional(),
            "dimension": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageDimensionOut"]
            ).optional(),
            "imageQualityScores": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresOut"]
            ).optional(),
            "formFields": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldOut"])
            ).optional(),
            "tables": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageTableOut"])
            ).optional(),
            "blocks": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1DocumentPageBlockOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageOut"])
    types["GoogleCloudDocumentaiV1ReviewDocumentRequestIn"] = t.struct(
        {
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentIn"]
            ).optional(),
            "enableSchemaValidation": t.boolean().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaIn"]
            ).optional(),
            "priority": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentRequestIn"])
    types["GoogleCloudDocumentaiV1ReviewDocumentRequestOut"] = t.struct(
        {
            "inlineDocument": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentOut"]
            ).optional(),
            "enableSchemaValidation": t.boolean().optional(),
            "documentSchema": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentSchemaOut"]
            ).optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ReviewDocumentRequestOut"])
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
    types["GoogleCloudDocumentaiV1beta2DocumentStyleIn"] = t.struct(
        {
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeIn"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "textStyle": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "fontWeight": t.string().optional(),
            "fontFamily": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentStyleIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentStyleOut"] = t.struct(
        {
            "fontSize": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentStyleFontSizeOut"]
            ).optional(),
            "textDecoration": t.string().optional(),
            "color": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "textStyle": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "fontWeight": t.string().optional(),
            "fontFamily": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentStyleOut"])
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
    types["GoogleCloudDocumentaiV1BatchProcessResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessResponseIn"])
    types["GoogleCloudDocumentaiV1BatchProcessResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1BatchProcessResponseOut"])
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
    types[
        "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusIn"
    ] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "gcsUri": t.string().optional(),
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
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "gcsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiUiv1beta3AutoLabelDocumentsMetadataIndividualAutoLabelStatusOut"
        ]
    )
    types["GoogleCloudDocumentaiV1beta2DocumentShardInfoIn"] = t.struct(
        {
            "textOffset": t.string().optional(),
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentShardInfoOut"] = t.struct(
        {
            "textOffset": t.string().optional(),
            "shardIndex": t.string().optional(),
            "shardCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentShardInfoOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn"] = t.struct(
        {
            "layoutId": t.string().optional(),
            "layoutType": t.string().optional(),
            "page": t.string(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyIn"]
            ).optional(),
            "confidence": t.number().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut"] = t.struct(
        {
            "layoutId": t.string().optional(),
            "layoutType": t.string().optional(),
            "page": t.string(),
            "boundingPoly": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2BoundingPolyOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorPageRefOut"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1SetDefaultProcessorVersionResponseOut"])
    types[
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn"
    ] = t.struct(
        {"type": t.string().optional(), "confidence": t.number().optional()}
    ).named(
        renames["GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectIn"]
    )
    types[
        "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut"
    ] = t.struct(
        {
            "type": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefectOut"
        ]
    )
    types["GoogleCloudDocumentaiV1DocumentPageLineIn"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLineIn"])
    types["GoogleCloudDocumentaiV1DocumentPageLineOut"] = t.struct(
        {
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageLineOut"])
    types["GoogleCloudDocumentaiV1ListEvaluationsResponseIn"] = t.struct(
        {
            "evaluations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1EvaluationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListEvaluationsResponseIn"])
    types["GoogleCloudDocumentaiV1ListEvaluationsResponseOut"] = t.struct(
        {
            "evaluations": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1EvaluationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1ListEvaluationsResponseOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityIn"] = t.struct(
        {
            "id": t.string().optional(),
            "mentionId": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
            "mentionText": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityIn"])
            ).optional(),
            "redacted": t.boolean().optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueIn"]
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorIn"]
            ).optional(),
            "confidence": t.number().optional(),
            "type": t.string(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentEntityOut"] = t.struct(
        {
            "id": t.string().optional(),
            "mentionId": t.string().optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "mentionText": t.string().optional(),
            "properties": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentEntityOut"])
            ).optional(),
            "redacted": t.boolean().optional(),
            "normalizedValue": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValueOut"]
            ).optional(),
            "pageAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageAnchorOut"]
            ).optional(),
            "confidence": t.number().optional(),
            "type": t.string(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentEntityOut"])
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
    types["GoogleCloudDocumentaiV1DocumentPageTableTableCellIn"] = t.struct(
        {
            "colSpan": t.integer().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
            "rowSpan": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableTableCellIn"])
    types["GoogleCloudDocumentaiV1DocumentPageTableTableCellOut"] = t.struct(
        {
            "colSpan": t.integer().optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "rowSpan": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageTableTableCellOut"])
    types["GoogleCloudDocumentaiV1DocumentPageFormFieldIn"] = t.struct(
        {
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
            "correctedValueText": t.string().optional(),
            "correctedKeyText": t.string().optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutIn"]
            ).optional(),
            "valueType": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldIn"])
    types["GoogleCloudDocumentaiV1DocumentPageFormFieldOut"] = t.struct(
        {
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
            "correctedValueText": t.string().optional(),
            "correctedKeyText": t.string().optional(),
            "fieldName": t.proxy(
                renames["GoogleCloudDocumentaiV1DocumentPageLayoutOut"]
            ).optional(),
            "valueType": t.string().optional(),
            "valueDetectedLanguages": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentPageDetectedLanguageOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentPageFormFieldOut"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn"] = t.struct(
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
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolIn"])
    types["GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut"] = t.struct(
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta1DocumentPageSymbolOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableIn"] = t.struct(
        {
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutIn"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"]
            ).optional(),
            "headerRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowIn"]
                )
            ).optional(),
            "detectedLanguages": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudDocumentaiV1beta2DocumentPageDetectedLanguageIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentPageTableOut"] = t.struct(
        {
            "bodyRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut"]
                )
            ).optional(),
            "layout": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentPageLayoutOut"]
            ).optional(),
            "provenance": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"]
            ).optional(),
            "headerRows": t.array(
                t.proxy(
                    renames["GoogleCloudDocumentaiV1beta2DocumentPageTableTableRowOut"]
                )
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
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentPageTableOut"])
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
    types["GoogleCloudDocumentaiV1DocumentProvenanceParentIn"] = t.struct(
        {
            "index": t.integer().optional(),
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentProvenanceParentIn"])
    types["GoogleCloudDocumentaiV1DocumentProvenanceParentOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "id": t.integer().optional(),
            "revision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1DocumentProvenanceParentOut"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdIn"] = t.struct(
        {"docId": t.string()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdIn"])
    types["GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdOut"] = t.struct(
        {"docId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiUiv1beta3DocumentIdUnmanagedDocumentIdOut"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextChangeIn"] = t.struct(
        {
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceIn"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorIn"]
            ).optional(),
            "changedText": t.string().optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeIn"])
    types["GoogleCloudDocumentaiV1beta2DocumentTextChangeOut"] = t.struct(
        {
            "provenance": t.array(
                t.proxy(renames["GoogleCloudDocumentaiV1beta2DocumentProvenanceOut"])
            ).optional(),
            "textAnchor": t.proxy(
                renames["GoogleCloudDocumentaiV1beta2DocumentTextAnchorOut"]
            ).optional(),
            "changedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDocumentaiV1beta2DocumentTextChangeOut"])
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
    types["GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionResponseIn"])
    types["GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDocumentaiV1DeployProcessorVersionResponseOut"])

    functions = {}
    functions["operationsDelete"] = documentai.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudLocationLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFetchProcessorTypes"] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudLocationLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudLocationLocationOut"]),
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
    functions["projectsLocationsProcessorTypesList"] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorTypesGet"] = documentai.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDocumentaiV1ProcessorTypeOut"]),
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
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsProcess"] = documentai.post(
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsUndeploy"] = documentai.post(
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsList"] = documentai.post(
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsGet"] = documentai.post(
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsTrain"] = documentai.post(
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsDeploy"] = documentai.post(
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProcessorsProcessorVersionsDelete"] = documentai.post(
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
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
        "v1/{processorVersion}:evaluateProcessorVersion",
        t.struct(
            {
                "processorVersion": t.string(),
                "evaluationDocuments": t.proxy(
                    renames["GoogleCloudDocumentaiV1BatchDocumentsInputConfigIn"]
                ).optional(),
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
                "inlineDocument": t.proxy(
                    renames["GoogleCloudDocumentaiV1DocumentIn"]
                ).optional(),
                "enableSchemaValidation": t.boolean().optional(),
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
